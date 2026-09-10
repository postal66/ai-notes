<!-- social-ops-fingerprint:3398d9e774f4c260ffb8f36cd2f0e9f2fcfa7c7466897f348c8844701a5285b2 -->
---
title: How to Use Claude Sonnet 5 API
---
# How to Use Claude Sonnet 5 API

![How to Use Claude Sonnet 5 API](https://resource.cometapi.com/How%20to%20Use%20Claude%20Sonnet%205%20API.webp)

## Quick Answer

[Claude Sonnet 5 API](https://www.cometapi.com/models/anthropic/claude-sonnet-5/) is Anthropic's new Sonnet-class model for coding agents, long-context reasoning, tool use, and professional knowledge work. Anthropic announced Claude Sonnet 5 on June 30, 2026, positioning it as the most agentic Sonnet model yet and a major upgrade from Claude Sonnet 4.6. Developers can use it through [CometAPI](https://www.cometapi.com/) with the model ID `claude-sonnet-5` via the native Anthropic Messages endpoint `POST /v1/messages` or the OpenAI-compatible endpoint `POST /v1/chat/completions`.

## Why Claude Sonnet 5 Matters Now

Anthropic introduced [Claude Sonnet 5](https://www.cometapi.com/models/anthropic/claude-sonnet-5/) on June 30, 2026, and the launch is aimed directly at developers building agentic systems. The company describes Sonnet 5 as the most agentic Sonnet model yet, with stronger planning, tool use, coding, browser work, terminal work, and professional reasoning. The most important positioning is that Sonnet 5 narrows the gap with Claude Opus 4.8 while staying in the faster, more cost-efficient Sonnet tier.

That matters because the market has moved beyond simple chat completions. Production AI applications increasingly need a model to read large context, call tools, write code, inspect documents, use a browser, execute terminal commands, recover from errors, and finish multi-step workflows. Claude Sonnet models have historically been popular for coding and agent workflows, and Sonnet 5 is built for that exact category.

The release also changes how developers should think about API control. Claude Sonnet 5 uses adaptive thinking by default. Manual extended-thinking budgets are removed for this model, and Anthropic's migration notes say that non-default sampling settings such as `temperature`, `top_p`, and `top_k` can return a 400 error. In other words, migrating from Sonnet 4.6 is not just a model-name swap.

## What Is Claude Sonnet 5 API?

Claude Sonnet 5 API is the programmatic interface for Anthropic's Sonnet 5 model. It is designed for text generation, coding, tool use, document reasoning, image understanding, and long-context workflows. On CometAPI, the model ID is:

```
claude-sonnet-5
```

You can call it in two main ways:

1. Use CometAPI's Anthropic Messages endpoint when you want Claude-native behavior, adaptive thinking, effort control, prompt caching, tools, web search, streaming, and Anthropic response shapes.
2. Use CometAPI's OpenAI-compatible chat endpoint when your application already uses OpenAI-style chat completions and you want easier model routing across Claude, GPT, Gemini, and other model families.

For most production teams, the native Messages endpoint is the best first choice for Claude-specific agent workflows. The OpenAI-compatible endpoint is best when portability, model comparison, or minimal migration work matters more than Claude-specific controls.

## Claude Sonnet 5 Quick Specs

| Specification | Claude Sonnet 5 API detail | Practical note |
| --- | --- | --- |
| Provider | Anthropic | Available through Anthropic and supported platforms such as CometAPI |
| CometAPI model ID | claude-sonnet-5 | Use this exact ID in CometAPI requests |
| CometAPI provider code | anthropic | Useful for catalog filtering and routing |
| Native CometAPI endpoint | POST /v1/messages | Best for Claude-native features |
| OpenAI-compatible endpoint | POST /v1/chat/completions | Best for portable chat-completion integrations |
| Input types | Text and image; CometAPI catalog also lists PDF-to-text | Good fit for coding, documents, screenshots, charts, and multimodal review |
| Output type | Text | Use separate tools for file generation, browser actions, or code execution |
| Context window | 1M tokens in Anthropic docs | Recount prompts because of the new tokenizer |
| Maximum output | Up to 128k output tokens on the synchronous Messages API | Adaptive thinking tokens share the response budget |
| Thinking behavior | Adaptive thinking on by default | Do not send old manual extended-thinking budgets |
| Effort control | Supported via output\_config.effort on the Messages API | Use higher effort for hard reasoning and lower effort for speed/cost |
| Sampling controls | Non-default temperature, top\_p, and top\_k rejected in migration notes | Remove old creativity knobs during migration |

## What's New in Claude Sonnet 5 API: Key Innovations

Anthropic positioned Sonnet 5 as a substantial upgrade over Sonnet 4.6, focusing on real-world agentic reliability.

### 1. New Tokenizer and Token Efficiency

Sonnet 5 uses an updated tokenizer (similar to Opus 4.7). The same input text can map to roughly **1.0–1.35× more tokens** depending on content type, averaging around 30% more.

**Impact:** Introductory pricing ($2/$10 per million input/output tokens until Aug 31, 2026) makes the transition roughly cost-neutral. Standard pricing afterward is $3/$15, matching Sonnet 4.6 per token but potentially higher per task due to token inflation. Always re-count tokens with the new model.

### 2. Capability Improvements

Sonnet 5 shows substantial gains over Sonnet 4.6 across benchmarks:

- **Coding & Agentic Tasks**: Closer to Opus 4.8 on SWE-bench-like evaluations, agentic search (BrowseComp), and computer use (OSWorld-Verified).
- **Reasoning & Knowledge Work**: Better sustained focus, self-verification, and handling of brownfield code or multi-step professional tasks.
- **Multimodal & Tool Use**: Stronger parallel tool calling and vision capabilities.

Performance scales with **effort levels** (low/medium/high/xhigh), allowing fine-tuned cost-performance tradeoffs. At higher efforts, it matches or approaches Opus on many tasks.

Early user feedback highlights faster completion of complex tasks, fewer hallucinations, and better real-world execution.

![How to Use Claude Sonnet 5 API](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F9941d610909f28a504e16dd5af823df172ec6035-2600x1234.png&w=3840&q=75)

### 3. Cybersecurity Safeguards & Safety

- Lower overall undesirable behaviors than 4.6.
- Reduced cyber exploit capabilities vs. Opus (scored 0% full exploits on Firefox vuln tests).
- **Cyber safeguards enabled by default** — real-time detection and blocking of dangerous usage (same as Opus 4.7/4.8, less strict than some higher models).

This makes Sonnet 5 safer for production agents in cybersecurity-sensitive environments.

![How to Use Claude Sonnet 5 API](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd018d76aa03c0ef18abc8a68de8f6fcd51c0a574-3840x2160.png&w=3840&q=75)

Claude Sonnet 5 is stronger at cyber-relevant reasoning than Sonnet 4.6, but it is not as strong as Opus 4.8 and is substantially below Mythos 5 on the evaluated cyber tasks.

The important API takeaway is that safeguards scale with model capability. Anthropic describes classifier-based safeguards across traffic, with categories such as prohibited use, high-risk dual use, and dual use. Prohibited use and high-risk dual-use exchanges are blocked by default, while ordinary dual-use security tasks such as vulnerability detection are not blocked by default.

For legitimate security teams, this means Sonnet 5 can be useful for defensive work such as code review, secure configuration guidance, vulnerability triage, incident documentation, and patch planning.

## Adaptive Thinking in Claude Sonnet 5

Adaptive thinking is one of the most important developer-facing changes in Claude Sonnet 5. Instead of asking developers to manually choose a thinking budget for every call, Claude can allocate reasoning effort dynamically based on the task.

Adaptive thinking is one of Sonnet 5's standout features. It dynamically adjusts reasoning depth:

- **Effort Levels**: Low (fast/cheap), Medium, High (deeper analysis), with adaptive options.
- **Defaults**: High on API/Claude Code for Sonnet 5.
- **Benefits**: Balance quality vs. cost/latency. Higher effort excels on complex tasks but consumes more tokens.

**Prompt Example**:

```
Use adaptive thinking for this task: Quick overview first, then detailed analysis and code if critical issues are found.
```

In older Claude integrations, teams often used extended thinking controls like:

```
{
  "thinking": {
    "type": "enabled",
    "budget_tokens": 32000
  }
}
```

For Claude Sonnet 5, do not send that old pattern. Anthropic's Sonnet 5 migration notes say manual extended thinking budgets are removed and can return a 400 error. Use adaptive thinking and effort controls instead.

### How Effort Control Works

The `effort` parameter gives developers a simpler way to influence how much work the model does. Anthropic's current effort levels include `low`, `medium`, `high`, `xhigh`, and `max`; `high` is the default and is equivalent to omitting the parameter. A practical production policy looks like this:

| Effort level | Use when | Avoid when |
| --- | --- | --- |
| low | Short answers, extraction, classification, routing, simple transformations | The task requires multi-step reasoning or high reliability |
| medium | Normal coding help, document summaries, support investigations, business analysis | The task is trivial or latency-sensitive |
| high | Complex reasoning, difficult coding problems, and agentic tasks | You are running high-volume low-value traffic |
| xhigh | Long-running coding agents, repeated tool calling, web search, and large knowledge-base search | The task has a short context and obvious answer |
| max | Genuinely frontier problems where marginal quality matters | Most routine production traffic |

The architectural pattern is stable: route hard tasks to higher effort and simple tasks to lower effort.

## Why Use Claude Sonnet 5 API With CometAPI?

CometAPI is useful when teams want one integration layer for many model families. Instead of building separate provider integrations for every model, you can route Claude, GPT, Gemini, image models, video models, embedding models, and other APIs behind one account and one application architecture.

For Claude Sonnet 5, CometAPI gives three practical advantages.

First, CometAPI exposes Claude Sonnet 5 through both the native Anthropic Messages endpoint and an OpenAI-compatible endpoint. That means a team can use Claude-native features for serious agent workflows while still testing Sonnet 5 inside applications that already use OpenAI-style chat completions.

Second, CometAPI's catalog makes model comparison easier. You can run the same prompt suite against Sonnet 5, Sonnet 4.6, Opus-tier models, GPT-class models, Gemini-class models, and specialized models. That matters because the best model for coding may not be the best model for document extraction, customer support, latency-sensitive chat, or cost-sensitive batch processing.

Third, CometAPI helps with production routing. You can start with Sonnet 5 as the default model for coding and agentic reasoning, then add fallback rules for availability, budget, latency, or refusal behavior. A mature AI system should not be welded to one model name forever.

## How to Use Claude Sonnet 5 API With CometAPI

The examples below use server-side code. Never expose your CometAPI key in browser JavaScript, mobile apps, public repositories, or client-side logs.

### Step 1: Create and Store Your CometAPI Key

Store your API key as an environment variable:

```
export COMETAPI_KEY="your_cometapi_key"
```

On Windows PowerShell:

```
$env:COMETAPI_KEY="your_cometapi_key"
```

### Step 2: Choose the Right Endpoint

Use `POST /v1/messages` when you want Claude-native behavior:

```
https://api.cometapi.com/v1/messages
```

Use `POST /v1/chat/completions` when you want OpenAI-compatible chat:

```
https://api.cometapi.com/v1/chat/completions
```

Recommendation: start with `/v1/messages` for new Claude Sonnet 5 agent systems. Use `/v1/chat/completions` when you already have OpenAI SDK wrappers, model routers, or multi-model eval tools built around chat completions.

### Step 3: Call Claude Sonnet 5 With cURL

This is the simplest native Messages API example:

```
curl https://api.cometapi.com/v1/messages \  -H "Authorization: Bearer $COMETAPI_KEY" \  -H "Content-Type: application/json" \  -d '{    "model": "claude-sonnet-5",    "max_tokens": 1200,    "messages": [      {        "role": "user",        "content": "Write a concise migration checklist for moving a Node.js API from Express 4 to Express 5."      }    ]  }'
```

For Sonnet 5, avoid adding old sampling overrides or manual thinking budgets unless the current documentation explicitly supports them for your route. Let adaptive thinking handle reasoning and use effort control where supported.

### Step 4: Python Example With the Anthropic SDK

Many Anthropic SDK workflows can be pointed at CometAPI by setting the base URL and API key.

```
import osimport anthropic​client = anthropic.Anthropic(    base_url="https://api.cometapi.com",    api_key=os.environ["COMETAPI_KEY"],)​message = client.messages.create(    model="claude-sonnet-5",    max_tokens=1500,    messages=[        {            "role": "user",            "content": (                "Review this deployment plan for a payments API. "                "Return the top risks, missing tests, and rollout checklist."            ),        }    ],)​for block in message.content:    if getattr(block, "type", None) == "text":        print(block.text)
```

If your CometAPI route supports effort control through the same shape as Anthropic's current docs, you can add an effort setting for harder work:

```
message = client.messages.create(    model="claude-sonnet-5",    max_tokens=3000,    thinking={"type": "adaptive"},    output_config={"effort": "high"},    messages=[        {            "role": "user",            "content": "Analyze this incident report and propose a root-cause investigation plan.",        }    ],)
```

Because provider and aggregator schemas can evolve, test effort parameters in staging before production. If a route rejects `output_config`, remove it or use the currently documented CometAPI parameter shape.

### Step 5: OpenAI-Compatible Chat Completion Example

Use this path if your application already uses OpenAI-compatible chat completions.

```
curl https://api.cometapi.com/v1/chat/completions \
  -H "Authorization: Bearer $COMETAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-5",
    "messages": [
      {
        "role": "system",
        "content": "You are a senior backend engineer. Be precise and practical."
      },
      {
        "role": "user",
        "content": "Design a retry strategy for a webhook delivery service. Include database fields and failure states."
      }
    ],
    "max_completion_tokens": 1800,
    "stream": false
  }'
```

The OpenAI-compatible route is excellent for portability, but do not assume every Claude-native feature maps perfectly to chat completions. For advanced Claude workflows, prefer the Messages endpoint.

### Step 6: Streaming Example

Streaming improves perceived latency for chat, coding assistants, and long reports.

```
const response = await fetch("https://api.cometapi.com/v1/messages", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.COMETAPI_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "claude-sonnet-5",
    max_tokens: 2500,
    stream: true,
    messages: [
      {
        role: "user",
        content: "Write a production runbook for investigating elevated API error rates.",
      },
    ],
  }),
});

if (!response.ok) {
  throw new Error(`Stream failed: ${response.status} ${await response.text()}`);
}

for await (const chunk of response.body) {
  process.stdout.write(Buffer.from(chunk).toString("utf8"));
}
```

In production, parse server-sent events rather than printing raw chunks. Also handle network disconnects, partial responses, retry idempotency, and user cancellation.

**Computer Use / Agentic Flows**: Combine with tools for browser/terminal control. Sonnet 5 shines here.

**Best Practices with CometAPI**:

- Monitor usage dashboard for costs.
- A/B test models (e.g., Sonnet 5 vs. Opus 4.8).
- Set budget alerts.
- Use for Claude Code integrations by pointing to CometAPI endpoint.

### Prompting Tips for Claude Sonnet 5

Claude Sonnet 5 performs best when the task is explicit and the success criteria are visible.

Use this structure for coding and agent tasks:

```
Goal: [what should be achieved]
Context: [repo, system, constraints, known facts]
Inputs: [files, logs, tickets, data]
Rules: [must not change, security requirements, output format]
Success criteria: [tests pass, plan quality, risk list, exact schema]
Output: [what you want returned]
```

For example:

```
Goal: Find likely causes of increased checkout API latency.
Context: The service is Node.js, PostgreSQL, Redis, and Stripe webhooks.
Inputs: I will provide logs, traces, recent deploy notes, and database metrics.
Rules: Do not invent metrics. Separate evidence from hypotheses.
Success criteria: Return the top 5 likely causes, what evidence supports each one, and the next query or dashboard to check.
Output: A table followed by a 30-minute investigation plan.
```

## Claude Sonnet 5 Pricing on CometAPI

The live CometAPI catalog checked for this article lists `claude-sonnet-5` at:

| Price item | CometAPI catalog value checked |
| --- | --- |
| Input tokens | $1.60 per 1M tokens |
| Output tokens | $8.00 per 1M tokens |
| Model ID | claude-sonnet-5 |
| Availability | upcoming: false in the live catalog |

Always verify current pricing in the CometAPI dashboard before publishing customer-facing price claims. Model prices can change, and enterprise agreements may differ from public catalog values.

### Cost Estimate Example

```
def estimate_sonnet5_cost(input_tokens, output_tokens):
    input_price_per_million = 1.60
    output_price_per_million = 8.00

    input_cost = (input_tokens / 1_000_000) * input_price_per_million
    output_cost = (output_tokens / 1_000_000) * output_price_per_million
    return round(input_cost + output_cost, 6)

print(estimate_sonnet5_cost(input_tokens=120_000, output_tokens=8_000))
print("Expected output: 0.256")
```

If a long-context analysis uses 120,000 input tokens and 8,000 output tokens, the estimated catalog cost is about `$0.256` at the checked CometAPI price. That does not include any separate platform fees, discounts, taxes, or future pricing changes.

For agent workflows, also measure cost per resolved task. A coding agent that completes a ticket in one high-effort Sonnet 5 run may be cheaper than a lower-cost model that needs repeated retries and human correction.

## Claude Sonnet 4.6 Migration Guide

Migrating is straightforward but requires attention to breaking changes.

### What Changes From Sonnet 4.6 to Sonnet 5?

| Area | Claude Sonnet 4.6 | Claude Sonnet 5 | Migration recommendation |
| --- | --- | --- | --- |
| Model ID | Existing Sonnet 4.6 route | claude-sonnet-5 on CometAPI | Do not switch all traffic at once; stage rollout |
| Context | Smaller than Sonnet 5 in current docs | 1M-token context | Rebuild context packing and retrieval tests |
| Tokenizer | Previous tokenizer | New tokenizer; about 30% more tokens for same text in migration notes | Recount prompts, cached prefixes, chunks, and cost forecasts |
| Thinking control | Manual extended thinking patterns may exist | Adaptive thinking on by default; manual budgets removed | Remove thinking.budget\_tokens style payloads |
| Effort | Less central in older workflows | Use effort for reasoning intensity | Add route policy by task difficulty |
| Sampling | Some workflows may use temperature/top-p/top-k | Non-default sampling parameters can return 400 | Remove unsupported sampling overrides |
| Coding performance | Strong previous baseline | Better on key agentic coding and terminal benchmarks | Re-run internal coding evals before default migration |
| Safety behavior | Older refusal and safeguard profile | Updated refusal and cyber safeguard behavior | Test support, security, and policy-sensitive prompts |

### Migration Checklist:

1. **Update Model Name**: Change `"claude-sonnet-4-6"` to `"claude-sonnet-5"`.
2. **Tokenizer & Costs**: Re-test prompts and re-count tokens. Expect ~30% increase.
3. **Thinking Configuration**: Replace legacy extended thinking with adaptive (`thinking: {type: "adaptive"}`) + effort level. Manual `budget_tokens` is deprecated/removed.
4. **Sampling Parameters**: Remove `temperature`, `top_p`, `top_k`—they are no longer supported (use system prompts for style control).
5. **Test Thoroughly**: Run regression tests on agentic flows, tool use, and output parsing. Validate costs.
6. **Rate Limits**: Increased limits available; check your tier.
7. Increase `max_tokens` where adaptive thinking may need more budget.

### Backward-Compatible Migration Code

```
async function runClaudeTask({ prompt, taskType, useSonnet5 = true }) {
  const model = useSonnet5 ? "claude-sonnet-5" : "claude-sonnet-4-6";
  const effort =
    taskType === "coding_agent" || taskType === "security_review"
      ? "high"
      : "medium";

  const body = {
    model,
    max_tokens: taskType === "coding_agent" ? 5000 : 1800,
    thinking: useSonnet5 ? { type: "adaptive" } : undefined,
    messages: [{ role: "user", content: prompt }],
  };

  if (useSonnet5) {
    body.output_config = { effort };
  }

  const response = await fetch("https://api.cometapi.com/v1/messages", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.COMETAPI_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  if (response.status === 400 && useSonnet5) {
    // Retry once without optional Sonnet 5-only controls in case the route schema changed.
    delete body.output_config;
    const retry = await fetch("https://api.cometapi.com/v1/messages", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.COMETAPI_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (!retry.ok) {
      throw new Error(`Retry failed: ${retry.status} ${await retry.text()}`);
    }

    return retry.json();
  }

  if (!response.ok) {
    throw new Error(`Claude request failed: ${response.status} ${await response.text()}`);
  }

  return response.json();
}
```

This pattern lets you test Sonnet 5 without making your application brittle. You can keep a fallback model, remove optional fields on schema errors, and route hard workloads to higher effort.

## Is There a Free Claude Sonnet 5 API?

There is no reliable public evidence that Anthropic offers an unlimited free Claude Sonnet 5 API. But, developers can start testing Claude Sonnet 5 through CometAPI with free trial credit. After creating a [CometAPI](https://www.cometapi.com/) account, new users can receive $1 in free credit, which can be used to explore supported models and run initial API tests before adding more budget.

## FAQs about Claude Sonnet 5 API

### What is Claude Sonnet 5 API?

Claude Sonnet 5 API is the developer interface for Anthropic's Sonnet 5 model, a high-performance AI model for coding, agents, tool use, long-context reasoning, document analysis, and professional work.

### How do I use Claude Sonnet 5 API with CometAPI?

Use the CometAPI model ID `claude-sonnet-5`. For Claude-native behavior, send requests to `POST` `https://api.cometapi.com/v1/messages`. For OpenAI-compatible chat, use `POST` `https://api.cometapi.com/v1/chat/completions`.

### What is new in Claude Sonnet 5?

Claude Sonnet 5 adds stronger agentic coding and tool-use performance, a 1M-token context window, adaptive thinking by default, effort control, a new tokenizer, and updated safeguards for cyber-relevant and high-risk requests.

### Does Claude Sonnet 5 support adaptive thinking?

Yes. Adaptive thinking is on by default for Claude Sonnet 5. Developers should not use old manual extended-thinking budgets with Sonnet 5; use effort control where supported instead.

### Why does the new Claude Sonnet 5 tokenizer matter?

The new tokenizer can produce about 30% more tokens for the same text than Claude Sonnet 4.6. That affects cost, context packing, prompt caching, chunking, and `max_tokens` planning.

### CometAPI vs. Direct Anthropic: Which is Beter

CometAPI offers unified access, lower prices, and easier multi-model experimentation—ideal for most developers.

### Should I migrate from Claude Sonnet 4.6 to Claude Sonnet 5 immediately?

Migrate in stages. Remove unsupported parameters, recount tokens, run internal evals, monitor cost and refusal behavior, keep Sonnet 4.6 as a fallback, then gradually route more production traffic to Sonnet 5.

## Final Takeaway

Claude Sonnet 5 API is one of the most important developer model releases of 2026 because it pushes Sonnet-class models deeper into agentic work. The strongest use cases are coding agents, terminal workflows, long-context analysis, tool use, multimodal document reasoning, and professional automation. The migration is also more subtle than a model-name change: Sonnet 5 introduces a new tokenizer, adaptive thinking by default, effort-based control, changed sampling behavior, and updated cybersecurity safeguards.

**Recommendation**: Start with **CometAPI** today for seamless access to Sonnet 5 (and 500+ other models) with free credits, lower costs, and unified management. Sign up at [CometAPI](https://www.cometapi.com/), integrate in minutes, and scale confidently.

---

*Originally published at [https://www.cometapi.com/how-to-use-claude-sonnet-5-api/](https://www.cometapi.com/how-to-use-claude-sonnet-5-api/).*
