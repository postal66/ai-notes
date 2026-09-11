<!-- social-ops-fingerprint:4ca4d14a3a2a29dc6ca9ecc23bb45fa0a91ba0414ea5c7db86117c5d1a936c52 -->
---
title: How to add Claude to an Alexa skill
---
# How to add Claude to an Alexa skill

![How to add Claude to an Alexa skill](https://resource.cometapi.com/blog/uploads/2025/12/How%2520to%2520add%2520Claude%2520to%2520an%2520Alexa%2520skill.webp)

Voice assistants are increasingly powered by large language models. If you want to bring Anthropic’s Claude API into an Alexa skill you maintain or build, this guide walks you through the practical architecture, concrete code patterns, and operational considerations you’ll need — from quick proof-of-concept to a production-grade skill.

CometAPI is an API-aggregation gateway that exposes a unified, OpenAI-compatible surface for hundreds of large-language models (LLMs), including Anthropic’s Claude family (Sonnet, Opus, and related variants). Instead of calling Anthropic’s API directly, customers may call CometAPI endpoints and select a Claude model by name; CometAPI handles model routing, billing aggregation, and, in many cases, a simplified authentication and parameter surface.

From the perspective of an Alexa skill, adding a Claude model via CometAPI offers three practical benefits: (1) quick access to the latest Claude releases (Sonnet / Opus variants) without rewriting client code when model names change; (2) a consistent, OpenAI-style REST surface that many SDKs already support; and (3) centralized usage analytics, throttling, and pricing plans that can be simpler to manage than multiple direct vendor contracts.

## What is Claude and why would you add it to an Alexa skill?

Claude is Anthropic’s family of large language models and conversational APIs (the Messages API) that developers can call from their applications. Claude models (recently updated across the Opus/Sonnet/Haiku series, [Claude Opus 4.5](https://www.cometapi.com/models/anthropic/claude-opus-4-5-20251101/), [Claude Sonnet 4.5](https://www.cometapi.com/models/anthropic/claude-sonnet-4-5/), [Claude Haiku 4.5](https://www.cometapi.com/models/anthropic/claude-haiku-4-5/)) provide high-quality natural language generation, reasoning, and specialized agent capabilities. Integrating Claude into an Alexa skill lets you replace or augment rule-based responses with an LLM-driven conversational brain that can summarize, reason, personalize, or act as an “agent” for complex tasks.

### What pieces talk to one another?

At a high level the integration pattern is straightforward: the Alexa device (Echo) sends voice input to the Alexa Skills backend (your skill). Your backend — typically an AWS Lambda function or an HTTPS service — transforms the user’s intent into a text prompt and calls the Claude API. The Claude response is then turned into speech (SSML) and returned to Alexa for playback. Optionally, you can use streaming, progressive responses, or Agent/Tool patterns to make the experience more responsive and powerful.

### Why choose Claude?

Claude provides a modern Messages API (REST + SDKs) and supports streaming responses (SSE), tools/Agent support (Agent Skills & Model Context Protocol), and tiered models with varying cost/performance profiles — making it well-suited for complex conversational or agentic voice experiences. Use Claude if you want a safety-focused model with tooling for connecting to external data and streaming behavior for lower perceived latency.

## How should you architect an Alexa skill that uses CometAPI’s Claude?

### What high-level architectures are viable?

There are two production-grade patterns you should consider:

**1. Direct Lambda → CometAPI**
An Alexa skill (typically backed by an AWS Lambda function) calls CometAPI’s REST endpoint synchronously for each user turn. The Lambda constructs the chat completion / messages payload, forwards it to CometAPI, and returns the model’s text to Alexa for TTS/SSML. This pattern is simple and works well for low-to-moderate traffic and proof-of-concepts. It minimizes components and therefore reduces places to fail, but it places rate-limit and retry logic in the Lambda.

**2. Skill → Backend service → CometAPI (recommended for production)**
The Alexa skill forwards requests to a dedicated backend microservice (hosted on Fargate/ECS, EKS, or an autoscaling EC2 fleet). That service is responsible for:

- conversation state, context windows, and summarization;
- token/cost accounting and caching;
- retries, backoff and circuit-breaking;
- input/output safety filtering and PII redaction;
- streaming/partial responses (if supported) and progressive updates to Alexa.

This pattern centralizes cross-cutting concerns and enables model-routing logic (e.g., choose Claude Opus for complex reasoning, Sonnet for short answers). It is the recommended approach for teams that expect growth, regulatory requirements, or complex telemetry needs.

### How does Alexa’s voice lifecycle map to a CometAPI Claude call?

1. **User speaks** → Alexa device performs ASR and sends an IntentRequest to your skill (Lambda or webhook).
2. **Your skill extracts text and session context** (locale, device capabilities, user opt-ins).
3. **Your code prepares a prompt** (system + conversation turns + user turn). For voice, prefer a short system instruction that constrains verbosity.
4. **Your service calls CometAPI** — either an OpenAI-compatible `chat/completions` endpoint or a CometAPI-specific messages endpoint — selecting the target Claude model. The backend receives a text or structured response.
5. **Your skill converts the text to SSML / cards** and returns the Alexa response. For long answers, provide a short spoken summary and push the full text to the Alexa companion app as a card.
6. **Monitoring & cost accounting**: correlate the Alexa request ID with CometAPI request IDs and model token usage metrics for observability.

---

## What are the concrete steps to implement Claude in an Alexa skill (end-to-end)?

Below is a practical step-by-step guide plus a sample Node.js Lambda handler to get you started.

### Step 1 — Create the Alexa skill and interaction model

1. In the Alexa Developer Console: create a **Custom** skill.
2. Define

   Intents

   (e.g.,

   ```
   OpenChatIntent
   ```

   ,

   ```
   FollowUpIntent
   ```

   ,

   ```
   StopIntent
   ```

   ) and sample utterances. For example:

   - `OpenChatIntent` utterances: “start a chat”, “ask Claude”, “chat with AI”.
3. Set the **Endpoint** to your AWS Lambda ARN (or HTTPS endpoint). Save and build the model. See Alexa REST APIs and docs for full guidance.

### Step 2 — Implement the Lambda backend

High-level flow inside Lambda:

1. Receive Alexa request (JSON).
2. Extract user utterance and session data.
3. Optionally send Alexa progressive response (so user hears “Thinking…”) while you call Claude.
4. Call Claude (via Anthropic REST API or Bedrock). Use streaming if you want partial responses.
5. Convert Claude response into Alexa output format (SSML recommended).
6. Return the `alexa` response object.

Below is a **concise** Node.js example (for readability we show one approach — direct fetch to Claude REST; in production move secrets to Secrets Manager and add error handling/caching). This uses `node-fetch`-style syntax (available in Node 18+ runtimes) and CometAPI's Claude API.

```
// index.js (AWS Lambda - Node 18+)
import { Handler } from 'aws-lambda';
import fetch from 'node-fetch'; // or global fetch in Node 18+

const CLAUDE_API_URL = process.env.CLAUDE_API_URL || 'https://api.cometapi.com/v1/messages'; // example
const CLAUDE_API_KEY = process.env.CLAUDE_API_KEY; // store in Secrets Manager or Lambda env vars

export const handler = async (event) => {
  // 1. Parse Alexa request
  const alexaRequest = JSON.parse(event.body || JSON.stringify(event));
  const intentName = alexaRequest.request?.intent?.name;
  const userUtterance = alexaRequest.request?.intent?.slots?.userQuery?.value || alexaRequest.request?.intent?.slots?.query?.value;

  // 2. Optional: send progressive response to Alexa (so user gets immediate feedback)
  // (Implementation omitted for brevity; use Alexa Progressive Response API with directive endpoint)

  // 3. Build Claude payload
  const claudePayload = {
    model: "claude-4-opus", // choose model appropriate to your subscription
    messages: [
      { role: "system", content: "You are a helpful assistant for an Alexa skill. Keep responses brief and spoken-friendly." },
      { role: "user", content: userUtterance }
    ],
    max_tokens_to_sample: 800
  };

  // 4. Call Claude (simple non-streaming call example)
  const resp = await fetch(CLAUDE_API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': CLAUDE_API_KEY
    },
    body: JSON.stringify(claudePayload),
    timeout: 20000 // be mindful of latency; Alexa has timeouts
  });

  if (!resp.ok) {
    console.error('Claude API error', await resp.text());
    return buildAlexaResponse("Sorry, I'm having trouble reaching the assistant right now. Please try again later.");
  }

  const claudeJson = await resp.json();
  // The JSON structure depends on the API or Bedrock wrapper you're using
  const assistantText = claudeJson?.completion || claudeJson?.output?.[0]?.content || extractTextFromClaude(claudeJson);

  // 5. Convert to SSML (shorten if needed)
  const ssml = `<speak>${sanitizeForSSML(assistantText)}</speak>`;

  // 6. Return Alexa response
  return {
    statusCode: 200,
    body: JSON.stringify({
      version: "1.0",
      response: {
        outputSpeech: {
          type: "SSML",
          ssml
        },
        shouldEndSession: false
      }
    })
  };
};

function buildAlexaResponse(text) {
  return {
    statusCode: 200,
    body: JSON.stringify({
      version: "1.0",
      response: {
        outputSpeech: { type: "PlainText", text },
        shouldEndSession: true
      }
    })
  };
}

function sanitizeForSSML(text) {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function extractTextFromClaude(json) {
  // implement mapping from Claude API response to string
  if (json?.output && Array.isArray(json.output)) {
    return json.output.map(o => o.content).join("\n");
  }
  return (json?.completion || '') + '';
}
```

> Note: Actual Claude API fields and endpoint names may differ (Anthropic’s docs show `messages` APIs and streaming modes). Always consult the most recent Claude docs for exact payload fields and streaming support.

### Step 3 — (Optional but recommended) Use streaming for faster perceived response

- **Why streaming?** Streaming lets Alexa start speaking partial output while the model is still generating. This reduces perception of latency and improves the conversational feel. Claude supports streaming responses (SSE or websocket) and has "fine-grained tool streaming" for complex operations. Implementing streaming requires an async conduit: Alexa Progressive Response + chunked streaming to the client or an SSE relay to your Lambda, or better, use an intermediary service that can push chunks to the device.
- **Caveat:** Alexa platform imposes its own timing and directive rules. The typical pattern is to send a Progressive Response directive early, then when the model completes provide the final speech output. Native real-time streaming into the Alexa device is constrained by Alexa’s directive model, so simulate streaming by sending progressive responses frequently and then the final response.

### Step 4 — Map Claude output to Alexa voice UX

- **Keep answers short and voice-friendly:** Claude can produce long-form text — transform or truncate to avoid long spoken paragraphs. Use SSML tags (breaks, emphasis) to improve prosody.
- **Handle multi-turn context:** Preserve short context windows (user ID / conversation history) but avoid storing every utterance server-side unless necessary. Use session attributes or a short-term memory store (DynamoDB with TTL) for follow-ups.
- **Error and fallback flows:** If Claude fails or returns unsafe content, have a safe fallback message ("I can't help with that") and a reporting/logging path for analysis.

---

## How should you secure credentials and protect user data?

### Where to store API keys and secrets?

- **AWS Secrets Manager** is the recommended production store for the CometAPI key and any other third-party credentials. Grant your Lambda or backend service an IAM role with a narrow policy that permits reading only the required secret. Rotate keys on a schedule and use automated rotation if supported.
- **Do not embed keys in source code or in public repositories.** If you use environment variables for quick prototypes, ensure CI/CD secret management replaces those values in build pipelines.

### How to avoid sending PII and sensitive voice data?

- **Redact or anonymize** any personally identifiable information (PII) before sending text to CometAPI. Remove names, addresses, account numbers, and any data you would not want to expose.
- **Ask for consent** when the skill must process sensitive personal data or when using personal profile features (as per Alexa policy).
- **Retention & logs:** tag logs and traces so audit processes can remove model inputs on request; implement retention windows aligned to your privacy policy.

## How do you manage latency and the Alexa user experience?

### Why progressive responses and timeouts matter?

Alexa expects a response from your skill within roughly **8 seconds** for most interfaces; if your backend (and model call) will exceed that window, you must use the Progressive Response API to keep users engaged. Progressive responses tell the user the skill is working (for example, “one moment while I fetch that answer”), which significantly improves perceived latency for voice interactions. Implement the progressive response immediately after you receive the intent and before the long LLM call.

### Can you stream model output to Alexa?

CometAPI and some Claude variants support streaming primitives (token or event streaming). However, Alexa devices do not support continuous token streaming in the same way as web UIs. The practical approach is:

- **Use progressive responses** to publish short interim messages while generating the full answer.
- **If your backend receives streaming tokens** from the model, buffer and surface only complete sentences or paragraphs at regular intervals (e.g., every 800–1200 ms) as progressive responses, and deliver the final consolidated TTS when ready. This avoids fragmented or robotic speech and respects Alexa’s response model.

### Design voice-friendly prompts

Constrain verbosity at the prompt level. Use a system instruction like:

> “You are a concise Alexa voice assistant. Provide a spoken answer of no more than 30 words and a card with a longer summary for the Alexa app.”

For structured output, ask the model to return JSON with `speech` and `card` fields. Parse these outputs server-side and map `speech` to SSML and `card` to the Alexa companion card. This reduces surprises and improves TTS quality.

## Can I stream Claude responses to Alexa so users hear text as it’s generated?

### Is streaming supported by Claude, and how does Alexa handle it?

Claude supports streaming via Server-Sent Events (SSE) when you set `stream:true` on the Messages API — that lets your backend receive tokens incrementally. However, Alexa’s device play model does not accept token-by-token speech directly from your backend. The practical pattern is:

1. Use Claude streaming on your backend to start receiving the response while it’s still being generated.
2. While the backend receives streaming chunks, send one or more Alexa progressive responses so the user hears “I’m working on that” or short interim messages.
3. When the backend has a useful chunk (or the full answer), synthesize the chunk (SSML) and respond. For very long replies, consider breaking the response into digestible pieces (and use `shouldEndSession` accordingly).

**Important constraints:** progressive responses are helpful but do not extend the maximum processing window; Alexa still expects an overall response within the allowed time. Streaming can reduce backend wait time and improve UX, but you must design around Alexa’s timing model.

## Recommended engineering and UX best practices?

### Conversation design

- Keep spoken answers short — Alexa users prefer concise responses.
- Use SSML to control pacing and breaks.
- If the model might ask clarifying questions, design a small set of follow-up prompts so the dialog feels natural.

### Failure modes and timeouts

- Provide graceful fallbacks when Claude is slow/unavailable.
- If your LLM call fails, use canned content or a short apology and offer to retry later.
- Track errors and user complaints to iterate rapidly.

### Testing

- Unit test intents with the Alexa Test Simulator and Virtual Alexa tools.
- Load test your backend for expected concurrent calls and long-tail voice sessions.

### What are common pitfalls to avoid?

1. **Blocking Alexa’s time window** — don’t exceed Alexa’s timing limits; use progressive responses and stream intelligently.
2. **Leaking secrets** — never log API keys or embed them in client code; use Secrets Manager.
3. **Excessive token use** — long conversation histories and verbose prompts increase cost; prune and summarize.
4. **Policy mismatch** — sending sensitive data to third-party LLMs without clear user consent or policy checks.

## Practical example prompts and prompt engineering tips for Alexa voice

### Use a short system instruction for voice suitability

Example: `"You are a concise, polite Alexa voice assistant. Keep spoken answers to ~30 words; offer to send longer summaries to the Alexa app."`

### Control verbosity and format for SSML

Ask Claude to emit an output in a small number of sentences or in JSON with `speech` and `card` fields. Then convert `speech` to SSML and `card` to the Skills card. Example prompt suffix: `"Return a JSON object with fields: 'speech' (short, for TTS), 'card' (longer text for the Alexa app). Do not include any extra text."` Parsing structured output reduces ambiguity.

### Prompt for follow-ups and suggestions

Encourage Claude to end with a question when appropriate: `"Would you like me to send this summary to your Alexa app?"` That helps keep voice interactions natural and discoverable.

## Are there no-code or low-code alternatives?

Yes — integration platforms like Zapier and AppyPie offer connectors to link Alexa triggers to Claude actions if you want a quick automation or prototype without writing server code. Those tools are best for simple workflows but won’t give the low-latency or security control you get with a custom backend.

[In low-code alternatives like Zapier, CometAPI](https://apidoc.cometapi.com/zapier) can also help developers.

## Conclusion:

Integrating CometAPI’s Claude into an Alexa skill is an attractive path to rapidly gain access to Anthropic-class LLMs with a single, OpenAI-compatible integration. The technical migration is straightforward for teams already familiar with chat/completion APIs, and CometAPI’s aggregation model accelerates experimentation.

Developers can access Claude API through CometAPI. To begin, explore the model capabilities of [CometAPI](https://www.cometapi.com/) in the [Playground](https://www.cometapi.com/console/playground) and consult the API guide for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. CometAPI offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Free trial of Claude APIs](https://www.cometapi.com/console/login)!

---

*Originally published at [https://www.cometapi.com/how-to-add-claude-to-an-alexa-skill/](https://www.cometapi.com/how-to-add-claude-to-an-alexa-skill/).*
