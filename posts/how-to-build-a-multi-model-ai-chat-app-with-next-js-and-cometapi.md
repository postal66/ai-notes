<!-- social-ops-fingerprint:c5da8b507f7b8cdfef14424b76723fd48a3ece905226cb577b24c3d1564c9673 -->
---
title: How to Build a Multi-Model AI Chat App with Next.js and CometAPI
---
# How to Build a Multi-Model AI Chat App with Next.js and CometAPI

![How to Build a Multi-Model AI Chat App with Next.js and CometAPI](https://resource.cometapi.com/How%20to%20Build%20a%20Multi-Model%20AI%20Chat%20App%20with%20Next.js.webp)

For a Next.js chatbot that needs several model providers, the most useful backend is one that centralizes authentication while letting the application choose a model per request. [CometAPI](https://www.cometapi.com/) provides that pattern: the server keeps one API key and the OpenAI-compatible base URL `https://api.cometapi.com/v1`, while the request's `model` field selects an available GPT, Claude, Gemini, or other chat model.

This tutorial builds a working App Router project with a server-side model allowlist, a streaming Route Handler, a browser model selector, protected environment variables, a complete chat interface, and deployment guidance. The CometAPI key never reaches the browser.

## What Is a Multi-Model AI Chat App?

A multi-model AI chat architecture places one application-controlled backend between the user interface and several model providers. In this project, the browser sends the conversation to `/api/chat`, while the server keeps the CometAPI credential private, validates the requested model ID, and forwards the request through one compatible API.

## How Does Model Switching Work in Next.js?

Changing models is a routing decision. The browser sends an approved model ID with the conversation to `/api/chat`. The Route Handler adds the CometAPI credential, calls `POST /v1/chat/completions`, and streams the selected model’s response back to the browser.

The shared endpoint does not make every model identical. Output style, tool behavior, supported parameters, context limits, and pricing can differ. Keep model IDs in a server-side allowlist and test each route with the same application prompts before making it available to users.

## What You’ll Build

The finished application has one Next.js backend and three selectable chat routes:

| Model ID | Example role | CometAPI price |
| --- | --- | --- |
| gemini-3.7-flash | Cost-sensitive, high-volume chat | $0.60 input / $3.00 output |
| claude-opus-5 | Focused premium reasoning | $4 input / $20 output |
| gpt-5.6 | gpt-5.6 is the generic CometAPI route for GPT-5.6 and currently maps to the Sol tier. | $3.2 input / $16 output in the short-context tier |

Pricing note: Prices shown below are in USD per million tokens, were checked on August 21, 2026, and may change. Always verify current rates on the model pages before production use. The table is a routing example, not a quality ranking. GPT-5.6 uses a higher price tier above 272,000 tokens. See the linked [Gemini 3.7 Flash](https://www.cometapi.com/models/google/gemini-3-7-flash/), [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/), and [GPT-5.6](https://www.cometapi.com/models/openai/gpt-5-6/) model pages for the dated rates used here.

CometAPI prices models transparently against each provider's official API. Models with unified official pricing — OpenAI, Claude, Gemini, and similar — are billed by token at a 0.8:1 ratio to the official price, a 20% discount; models without official APIs (MidJourney, Kling, Luma) are billed per call at CometAPI's set rates, also discounted 20%. See the [CometAPI Pricing Guide](https://apidoc.cometapi.com/pricing/about-pricing) for the markup formula, per-model rates, and billing units.

The three routes cover different trade-offs. **Gemini 3.7 Flash** is Google’s efficient agentic workhorse, with multimodal input and a 1,048,576-token context window for high-volume chat, coding, and knowledge workflows. **Claude Opus 5** is Anthropic's frontier reasoning model, strong on multi-step analysis, code, and careful long-form writing at a premium price. **GPT-5.6** is OpenAI's general-purpose model, balancing reasoning, tool use, and drafting across a wide context window for everyday production traffic.

## Before You Start

You need Node.js, npm, a CometAPI account, and a server-side API key from the [CometAPI Quick Start](https://apidoc.cometapi.com/overview/quick-start). The three exact model IDs above were available in the live catalog on August 21, 2026, were not marked upcoming, and exposed `POST /v1/chat/completions`.

The tutorial uses these shared settings:

- API key: `COMETAPI_API_KEY`
- Base URL: `https://api.cometapi.com/v1`
- Catalog endpoint: `GET` [`https://api.cometapi.com/api/models`](https://api.cometapi.com/api/models)

## Step 1: Create the Next.js App

```
npx create-next-app@latest multi-model-chat --ts --app --eslintcd multi-model-chatnpm run dev
```

No model-provider SDK is required for this version. The server uses the built-in `fetch` API and forwards the upstream Server-Sent Events stream.

## Step 2: Keep the CometAPI Key on the Server

Create `.env.local` in the project root:

```
COMETAPI_API_KEY=replace_with_your_cometapi_keyCOMETAPI_BASE_URL=https://api.cometapi.com/v1
```

Do not prefix the key with `NEXT_PUBLIC_`. Next.js only exposes variables with that prefix to browser bundles; the API key belongs in the server-side Route Handler.

## Step 3: Define the Model Policy

Put the allowed IDs in the backend, not only in the dropdown. A user can bypass browser controls and call your route directly, so the server must reject unknown model values.

```
const ALLOWED_MODELS = [  "gemini-3.7-flash",  "claude-opus-5",  "gpt-5.6",] as const;​type ModelId = (typeof ALLOWED_MODELS)[number];
```

The client will use the same three IDs for its selector, while the server remains the source of truth.

## Step 4: Stream CometAPI Through a Route Handler

Create `app/api/chat/route.ts`. The route validates a text-only chat payload, calls CometAPI with `stream: true`, and returns the upstream event stream without exposing the credential.

```
export const runtime = "nodejs";export const dynamic = "force-dynamic";​const ALLOWED_MODELS = [  "gemini-3.7-flash",  "claude-opus-5",  "gpt-5.6",] as const;​type ModelId = (typeof ALLOWED_MODELS)[number];type ChatMessage = {  role: "system" | "user" | "assistant";  content: string;};​function isModelId(value: unknown): value is ModelId {  return (    typeof value === "string" &&    (ALLOWED_MODELS as readonly string[]).includes(value)  );}​function isChatMessage(value: unknown): value is ChatMessage {  if (typeof value !== "object" || value === null) return false;​  const message = value as Record<string, unknown>;  return (    ["system", "user", "assistant"].includes(String(message.role)) &&    typeof message.content === "string" &&    message.content.length > 0 &&    message.content.length <= 20_000  );}​export async function POST(request: Request) {  const apiKey = process.env.COMETAPI_API_KEY;  const baseUrl = (    process.env.COMETAPI_BASE_URL || "https://api.cometapi.com/v1"  ).replace(/\/$/, "");​  if (!apiKey) {    return Response.json(      { error: "COMETAPI_API_KEY is not configured." },      { status: 500 },    );  }​  let payload: { model?: unknown; messages?: unknown };​  try {    payload = await request.json();  } catch {    return Response.json({ error: "Invalid JSON body." }, { status: 400 });  }​  if (!isModelId(payload.model)) {    return Response.json({ error: "Unsupported model ID." }, { status: 400 });  }​  if (    !Array.isArray(payload.messages) ||    payload.messages.length === 0 ||    payload.messages.length > 50 ||    !payload.messages.every(isChatMessage)  ) {    return Response.json(      { error: "messages must contain 1 to 50 valid text messages." },      { status: 400 },    );  }​  const upstream = await fetch(`${baseUrl}/chat/completions`, {    method: "POST",    headers: {      Authorization: `Bearer ${apiKey}`,      "Content-Type": "application/json",    },    body: JSON.stringify({      model: payload.model,      messages: payload.messages,      stream: true,    }),    cache: "no-store",    signal: request.signal,  });​  if (!upstream.ok) {    const requestId = upstream.headers.get("x-request-id");​    console.error("CometAPI request failed", {      status: upstream.status,      requestId,    });​    return Response.json(      {        error: "The selected model request failed.",        status: upstream.status,        requestId,      },      { status: upstream.status },    );  }​  if (!upstream.body) {    return Response.json(      { error: "The model returned no response body." },      { status: 502 },    );  }​  return new Response(upstream.body, {    status: 200,    headers: {      "Content-Type": "text/event-stream; charset=utf-8",      "Cache-Control": "no-cache, no-transform",    },  });}
```

The handler passes the browser’s disconnect signal upstream, so closing the request can stop unnecessary generation. It also returns a sanitized error to the client while keeping diagnostic details in server logs.

## Step 5: Add Model Selection and Stream Parsing

Create a client component in `app/page.tsx`. It sends the selected model with the conversation, parses each `data:` event, and appends the incremental `delta.content` text to the last assistant message.

The browser never calls CometAPI directly. Its only destination is your own `/api/chat` route, which keeps the key private and enforces the allowlist.

## Core Project Code

The Route Handler above is the complete `app/api/chat/route.ts` file. Add the following page, layout, and stylesheet to finish the runnable project.

**`app/page.tsx`**

```
"use client";​import { FormEvent, useState } from "react";​const MODEL_OPTIONS = [  { id: "gemini-3.7-flash", label: "Gemini 3.7 Flash" },  { id: "claude-opus-5", label: "Claude Opus 5" },  { id: "gpt-5.6", label: "GPT-5.6" },] as const;​type Role = "user" | "assistant";type Message = { role: Role; content: string };​function textFromSseLine(line: string): string {  const trimmed = line.trim();  if (!trimmed.startsWith("data:")) return "";​  const data = trimmed.slice(5).trim();  if (!data || data === "[DONE]") return "";​  try {    const event = JSON.parse(data);    return event.choices?.[0]?.delta?.content ?? "";  } catch {    return "";  }}​export default function Home() {  const [model, setModel] = useState("gemini-3.7-flash");  const [messages, setMessages] = useState<Message[]>([]);  const [input, setInput] = useState("");  const [loading, setLoading] = useState(false);  const [error, setError] = useState("");​  function appendAssistantText(text: string) {    if (!text) return;​    setMessages((current) => {      const next = [...current];      const lastIndex = next.length - 1;​      if (lastIndex >= 0 && next[lastIndex].role === "assistant") {        next[lastIndex] = {          ...next[lastIndex],          content: next[lastIndex].content + text,        };      }​      return next;    });  }​  async function sendMessage(event: FormEvent<HTMLFormElement>) {    event.preventDefault();​    const content = input.trim();    if (!content || loading) return;​    const outgoing: Message[] = [...messages, { role: "user", content }];    setMessages([...outgoing, { role: "assistant", content: "" }]);    setInput("");    setError("");    setLoading(true);​    try {      const response = await fetch("/api/chat", {        method: "POST",        headers: { "Content-Type": "application/json" },        body: JSON.stringify({ model, messages: outgoing }),      });​      if (!response.ok) {        const body = await response.json().catch(() => ({}));        throw new Error(body.error || `Request failed with ${response.status}`);      }​      if (!response.body) throw new Error("Streaming is not available.");​      const reader = response.body.getReader();      const decoder = new TextDecoder();      let buffer = "";​      while (true) {        const { value, done } = await reader.read();        buffer += decoder.decode(value, { stream: !done });​        const lines = buffer.split("\n");        buffer = lines.pop() ?? "";​        for (const line of lines) {          appendAssistantText(textFromSseLine(line));        }​        if (done) {          appendAssistantText(textFromSseLine(buffer));          break;        }      }    } catch (requestError) {      setError(        requestError instanceof Error ? requestError.message : "Request failed.",      );    } finally {      setLoading(false);    }  }​  return (    <main className="shell">      <section className="chat">        <header>          <p className="eyebrow">Next.js + CometAPI</p>          <h1>Multi-model chat</h1>          <label>            Model            <select              value={model}              onChange={(event) => setModel(event.target.value)}              disabled={loading}            >              {MODEL_OPTIONS.map((option) => (                <option key={option.id} value={option.id}>                  {option.label}                </option>              ))}            </select>          </label>        </header>​        <div className="messages" aria-live="polite">          {messages.length === 0 ? (            <p className="empty">Choose a model and send a message.</p>          ) : (            messages.map((message, index) => (              <article className={message.role} key={`${message.role}-${index}`}>                <b>{message.role === "user" ? "You" : "Assistant"}</b>                <p>{message.content || "…"}</p>              </article>            ))          )}        </div>​        <form onSubmit={sendMessage}>          <textarea            value={input}            onChange={(event) => setInput(event.target.value)}            placeholder="Ask something…"            rows={3}            maxLength={20_000}          />          <button disabled={loading || !input.trim()} type="submit">            {loading ? "Streaming…" : "Send"}          </button>        </form>​        {error ? <p className="error">{error}</p> : null}      </section>    </main>  );}
```

**`app/layout.tsx`**

```
import type { Metadata } from "next";import "./globals.css";​export const metadata: Metadata = {  title: "Multi-Model Chat",  description: "A streaming Next.js chat app powered by CometAPI.",};​export default function RootLayout({  children,}: Readonly<{ children: React.ReactNode }>) {  return (    <html lang="en">      <body>{children}</body>    </html>  );}
```

**`app/globals.css`**

```
:root {  color-scheme: dark;  font-family: Arial, sans-serif;  background: #07111f;  color: #eef4ff;}* { box-sizing: border-box; }body { margin: 0; }button, select, textarea { font: inherit; }​/* Layout shell and chat card */.shell { min-height: 100vh; display: grid; place-items: center; padding: 32px 16px; }.chat { width: min(820px, 100%); background: #0d1b2e; border: 1px solid #223957; border-radius: 20px; padding: 24px; }​/* Message list and bubbles */.messages { min-height: 360px; display: grid; align-content: start; gap: 12px; margin: 24px 0; }.messages article { max-width: 85%; padding: 12px 14px; border-radius: 14px; white-space: pre-wrap; }.user { justify-self: end; background: #164f8f; }.assistant { justify-self: start; background: #182a42; }​/* Form controls, buttons, and error states follow the same dark theme. */
```

## Step 6: Run and Deploy the App

```
npm run dev
```

Open `http://localhost:3000`, select a model, and send a message. For a production Node.js deployment, add `COMETAPI_API_KEY` and `COMETAPI_BASE_URL` to the host’s server-side environment settings, then run:

```
npm run buildnpm run start
```

Use a hosting path that supports streaming responses. A static export cannot run the `/api/chat` Route Handler.

## Test the Streaming Route

With the development server running, call your backend directly:

```
curl -N http://localhost:3000/api/chat \  -H "Content-Type: application/json" \  -d '{    "model": "gemini-3.7-flash",    "messages": [      {"role": "user", "content": "Explain model routing in two sentences."}    ]  }'
```

A successful request returns Server-Sent Events. The exact IDs and text vary, but the stream follows this shape:

```
data: {"choices":[{"delta":{"content":"Model"}}]}​data: {"choices":[{"delta":{"content":" routing"}}]}​data: [DONE]
```

The browser parser reads each SSE event, extracts `choices[0].delta.content`, and appends the streamed text to the assistant message as chunks arrive.

## Common Integration Errors

| Symptom | Cause | Fix |
| --- | --- | --- |
| 401 authentication error | Missing or invalid server-side key | Set COMETAPI\_API\_KEY; do not expose it with NEXT\_PUBLIC\_. |
| 404 or wrong route | The base URL is missing /v1 | Use `https://api.cometapi.com/v1`. |
| 400 unsupported model | The ID is not in the backend allowlist | Use an exact live text model ID and update both selectors. |
| The answer appears all at once | The host or proxy buffers the event stream | Disable response transformation and use a streaming-capable Node.js deployment. |

## Prepare the Chat Backend for Production

- **Authenticate your own users.** Do not expose a public route that spends credits for anonymous traffic.
- **Rate-limit by user and IP.** Bound concurrent streams, requests per minute, message count, and message length.
- **Keep the model allowlist server-side.** The browser selector is a convenience, not a security boundary.
- **Validate the live catalog during deployment.** Query `GET` [`https://api.cometapi.com/api/models`](https://api.cometapi.com/api/models) and fail the release if a configured ID is upcoming, unavailable, or missing the chat-completions endpoint.
- **Track cost by route.** Log the selected model, request ID, latency, token usage, and user ID. Set key quotas or spending caps in the CometAPI dashboard where appropriate.
- **Handle disconnects and timeouts.** Preserve `request.signal`, set an application timeout, and stop work when the client leaves.
- **Do not hide configuration errors with fallback.** Surface 400 and 401 responses. Use another model only for a bounded set of retryable failures and only when the request schema is compatible; see the [CometAPI Model Fallback Guide](https://apidoc.cometapi.com/guides/model-fallback-with-cometapi) for a two-layer fallback chain (CometAPI primary → CometAPI fallback model → official provider).
- **Redact logs.** Keep API keys, full prompts, and sensitive model output out of production error logs.

## One Next.js Backend, Several Model Choices

The model switch belongs in your server policy, not in separate provider accounts. A Next.js Route Handler can keep one CometAPI key private, accept an approved model ID per request, and stream the selected model through one OpenAI-compatible endpoint. The frontend stays simple, while the backend retains control over access, validation, observability, and cost. The same account and key also reach CometAPI's native image and video APIs — such as Flux for image generation and Kling for video generation — so this chat backend can extend to multimodal workflows without a second integration.

Use the [CometAPI public model directory](https://www.cometapi.com/models/) for model discovery and `GET` [`https://api.cometapi.com/api/models`](https://api.cometapi.com/api/models) for automated routing validation.

## Frequently Asked Questions

### Can I use multiple AI models in one Next.js app?

Yes. Keep one server-side route and pass an allowlisted model ID with each request. The browser UI can offer model choices, while the server controls which IDs are accepted.

### How do I switch between GPT, Claude, and Gemini?

Send the selected model ID in the request body. The server validates it against an allowlist and forwards the same chat payload to the chosen model through the OpenAI-compatible endpoint.

### Where should I store my CometAPI API key?

Store it in a server-side environment variable such as `COMETAPI_API_KEY`. Never expose it through a `NEXT_PUBLIC_` variable or client-side code.

### Does an OpenAI-compatible API make all models interchangeable?

No. The request shape is portable, but models can differ in supported parameters, context limits, tool behavior, output style, latency, and price. Test every allowlisted model with your production prompts.

### Can Next.js Route Handlers stream AI responses?

Yes. A Route Handler can return the upstream Server-Sent Events stream with a `text/event-stream` content type, provided the deployment platform and any proxy in front of it do not buffer the response.

### Can I deploy this app as a static Next.js site?

No. A static export cannot run the server-side `/api/chat` Route Handler or protect the API key. Use a Node.js or another compatible server runtime that supports streaming responses.

---

*Originally published at [https://www.cometapi.com/build-a-multi-model-ai-chat-app-with-next-js/](https://www.cometapi.com/build-a-multi-model-ai-chat-app-with-next-js/).*
