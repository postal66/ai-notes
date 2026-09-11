<!-- social-ops-fingerprint:5463c9073f1a6b817c4f91717d72a2ac489f1de7e86f14cb19e21ae5ca00f177 -->
---
title: How to Use Gemini 3.1 pro API
---
# How to Use Gemini 3.1 pro API

![How to Use Gemini 3.1 pro API](https://resource.cometapi.com/Gemini%203.1%20Pro%20How%20to%20Use%20the%20API,%20What%E2%80%99s%20New,%20and%20Where%20it%20Fits%20in%20Your%20Toolchain.webp)

A practical, code-forward guide to Gemini 3.1 Pro — what it is, how to call it (including via CometAPI), its multimodal and “thinking level” controls, function-calling/tool use, vibe-coding tips, and integrations with GitHub Copilot, VS Code, the Gemini CLI, and Google Antigravity. Gemini 3.1 pro is rolling forward the frontier of large multimodal models with a focused developer story: bigger context windows, configurable “thinking” modes, improved tool- and function-calling, and explicit support for agentic workflows.

## What is Gemini 3.1 Pro?

Gemini 3.1 Pro is the newest “Pro” tier in the Gemini 3 family: a natively multimodal, reasoning-first model tuned for complex, multi-step tasks and agentic tool use. It is presented as a refinement over Gemini 3 Pro with three practical focuses: stronger reasoning/factual grounding, better token efficiency and controllable execution modes targeted at developer workflows (code, planning, retrieval-augmented tasks). The model card and developer pages describe it as optimized for software engineering behavior, agentic pipelines, and multimodal inputs (text, images, audio, video and repositories).

Why that matters to you: the combination of a million-token context window (on many provider variants), explicit function-calling primitives, and “thinking level” controls gives teams more predictable costs and outputs for everything from rapid prototyping to production agent orchestration. [CometAPI](https://www.cometapi.com/) is already surfacing 3.1 Pro via API marketplaces and OpenAI-compatible bridges, offering pay-as-you-go access patterns.

## How can you use Gemini 3.1 Pro API (CometAPI)?

### What do I need before I start?

### Checklist (prerequisites)

- A CometAPI account and a CometAPI API key (store it in environment variables).
- Optionally a Google Cloud / Google AI Studio project & Gemini API key if you ever call Google directly (not required when going through Comet).
- `python 3.9+` or `node 18+`, `curl` available for quick tests.
- A secure secrets mechanism: env vars, vault, or CI secret store.
- Confirm the Comet model id for Gemini 3.1 Pro in your Comet console (e.g. `"google/gemini-3.1-pro"` or a Comet-specific alias).

CometAPI supports Gemini native format calls, as well as OpenAI's chat format calls. CometAPI simplifies switching models, offers a single base URL and SDKs, and can reduce integration friction for multi-vendor stacks.

Below are two concrete, copy-paste friendly examples: first calling Gemini via CometAPI (OpenAI-compatible client), and second calling Gemini via Google’s official Gemini HTTP endpoint. Replace `YOUR_API_KEY` with your provider key and set model names to the provider-available variant (e.g., `gemini-3.1-pro-preview` where exposed).

### Example: calling Gemini 3.1 Pro using CometAPI (curl + Python)

**Curl (OpenAI-compatible wrapper using CometAPI base URL)**

```
# curl example: CometAPI (OpenAI-compatible)curl https://api.cometapi.com/v1/chat/completions \  -H "Authorization: Bearer YOUR_API_KEY" \  -H "Content-Type: application/json" \  -d '{    "model": "gemini-3.1-pro-preview",    "messages": [      {"role":"system","content":"You are a concise programming assistant."},      {"role":"user","content":"Write a Python function to fetch CSV from a URL and return pandas DataFrame."}    ],    "max_tokens": 800  }'
```

**Python (OpenAI-compatible client configured to CometAPI base\_url)**

```
from openai import OpenAI  # or openai-python-compatible SDK offered by your platformclient = OpenAI(api_key="YOUR_API_KEY", base_url="https://api.cometapi.com/v1")resp = client.chat.completions.create(    model="gemini-3.1-pro-preview",    messages=[        {"role": "system", "content": "You are a concise programming assistant."},        {"role": "user", "content": "Write a Python function to fetch CSV from a URL and return pandas DataFrame."}    ],    max_tokens=800,)print(resp.choices[0].message.content)
```

> Rationale: CometAPI exposes an OpenAI-compatible bridge in many of their docs, which lets you reuse existing OpenAI client code by simply changing the `base_url` and model name. This is convenient for multi-provider experiments and rapid prototyping.

### Example: calling Gemini via the official Gemini API (Node.js / HTTP)

Google’s official Gemini endpoints are best for the full feature set (thinking-level controls, function calling, multimodal uploads). Below is a minimal HTTP example using the Gemini API surface described in Google AI developer docs.

Simply replace the Base URL and API Key in the official SDK or requests to use it:

- **Base URL**: `https://api.cometapi.com` (replace `generativelanguage.googleapis.com`)
- **API Key**: Replace `$GEMINI_API_KEY` with your `$COMETAPI_KEY`

**Curl (official Gemini API — illustrative)**

```
curl "https://api.cometapi.com/v1beta/models/gemini-3-1-pro-preview:generateContent" \
  -H "x-goog-api-key: $COMETAPI_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "How does AI work?"
          }
        ]
      }
    ]
  }'
```

### Common parameters you’ll set

- `temperature` (0.0–1.0) — randomness. Use `0.0` for deterministic code outputs.
- `max_output_tokens` / `max_tokens` — output length budget.
- `top_p` — nucleus sampling.
- `presence_penalty` / `frequency_penalty` — discourage repetition.
- `thinking_level` or model variant — determines reasoning depth (e.g., `-low`, `-medium`, `-high` or explicit `thinking_level`). Use the lowest thinking level that meets accuracy needs to control cost/latency.

## What are the multimodal capabilities of Gemini 3.1 Pro?

### What modalities does Gemini 3.1 Pro support?

Gemini 3.1 Pro accepts text, images, video, audio, and PDFs in many preview builds — and can synthesize text outputs that reference or summarize multimodal content. Comet supports forwarding multimodal inputs to Gemini — either by **image URL**, **file upload** (Comet file API), or by letting Gemini read files stored in cloud storage.

### How should developers think about multimodal prompts?

- Structure multimodal prompts with clear context blocks: for example, include the short text instruction first, then attach metadata or pointers for images/videos/PDFs.
- Use the SDK’s media attachments and file upload fields rather than embedding binary data in text fields — the official clients and the Vertex AI / Gemini API examples demonstrate how to pass media attachments cleanly.

Practical example (pseudocode): show an image plus question

```
# Pseudocode — attach an image with a caption and ask a questionfrom google.gemini import GemSDK  # conceptual import; use official client per docsresponse = client.generate(    model="gemini-3.1-pro-preview",    inputs = [        {"type": "text", "content": "Summarize the visual diagram and list actionable next steps."},        {"type": "image", "uri": "gs://my-bucket/diagram.png", "alt": "system architecture diagram"}    ])print(response.text)
```

Practical tips:

- Use image attachments for UI bug triage: attach a screenshot and ask for diffs or probable causes.
- Combine audio transcriptions with code samples for interview-recording summarization.
- When sending large artifacts (videos, big codebases), prefer a staged approach: upload assets (cloud storage), pass urls + short manifest, and use the model to drive a retrieval-augmented pipeline rather than stuffing everything into a single prompt.

## What are the Thinking Levels (Low, Medium, High) and when should I use them?

### What are “thinking levels”?

Gemini 3 series introduces a `thinking_level` parameter that guides the model’s internal compute/chain-of-thought budget. Think of it like a knob that trades latency + cost for increased depth of reasoning:

- **Low**: minimal reasoning, optimized for throughput and short, deterministic tasks.
- **Medium**: balanced reasoning — new in 3.1 and ideal for many engineering and analytic workflows.
- **High**: deeper reasoning, dynamic chain-of-thought style; best for complex multi-step problems.
  (There’s also a `minimal`/`max` nomenclature in other variants — consult the model docs for exact available options per variant.)

### How should I choose a thinking level?

- Use **Low** for high-throughput user chat, short instructions, or when cost/latency is critical.
- Use **Medium** as a default for most developer tasks that need a measured degree of reasoning (this is the new “sweet spot” in 3.1).
- Use **High** when solving puzzles, doing long logical chains, planning, or when you explicitly want high fidelity and are willing to accept increased latency and token consumption.

### How to set the thinking level in a request

```
curl "https://api.cometapi.com/v1beta/models/gemini-3-1-pro-preview:generateContent" \
  -H "x-goog-api-key: $COMETAPI_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{ "parts": [{ "text": "Explain quantum physics simply." }] }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "LOW"
      }
    }
  }'
```

## How do I implement function calling and tool use with Gemini 3.1 Pro?

### What is function calling / tool use?

Function calling (also called tool use) lets the model emit structured “call” objects that tell your application which external tool or function to run (for example, `get_current_weather(location)`) and with which arguments. The model can chain multiple calls, receive tool outputs, and continue reasoning — enabling agentic behaviors. Gemini SDKs offer built-in support for the model-to-tool loop (MCP/tool registry) so you can automate execution safely.

You can declare tools in the configuration to enable proxy behavior. Supported built-in tools include the google\_search, code\_execution, and url\_context custom functions.

### Safe pattern for tool use

1. **Declare tool interfaces**: register functions/tools with clear schemas and validated argument types.
2. **Let the model propose calls**: the model emits structured JSON describing which tool to call.
3. **The host executes whitelisted tools only**: enforce an allowlist and strict validation.
4. **Return tool outputs to the model**: the SDK loop feeds the tool response back to the model so it can continue planning/execute more calls.

## Gemini 3.1 Pro integration Guide

### GitHub Copilot

GitHub Copilot (Copilot) has since added support for Gemini family models at premium tiers, allowing teams to pick Gemini as the underlying model for Copilot chat and suggestions. That means users on eligible plans can select Gemini variants in the Copilot model picker, enjoying model-level improvements without changing their IDE extension. For teams, Copilot remains a convenient managed path to Gemini reasoning inside VS Code and other supported editors.

### Gemini CLI and Code Assist

The open-source **Gemini CLI** exposes Gemini models to the terminal; it’s lightweight and integrates with existing workflows (diffs, commits, CI, and headless server runs). Use the CLI for quick iteration, scripting agent runs, or embedding the model in DevOps flows. **Gemini Code Assist** is the VS Code extension and broader IDE integration that brings context-aware code suggestions, PR reviews and automated fixes directly into the editor. These tools let you control model selection, context windows, and thinking level preferences.

### Visual Studio Code

Visual Studio Code and its marketplace host both GitHub Copilot and Gemini Code Assist. You can install Code Assist for Gemini or continue using Copilot; each offers different tradeoffs (speed, depth, privacy). VS Code remains the most mature surface for interactive code generation, in-editor chat and direct integration with local runs or test harnesses.

### Google Antigravity

Google Antigravity is an agent-first IDE and platform that treats agents as first-class citizens, offering a “Mission Control” for agent orchestration, built-in browser automation, and a UI for multi-agent projects. Antigravity and Gemini CLI serve different needs: Antigravity is a full agentic IDE surface; Gemini CLI is terminal-native but integrates into Antigravity and VS Code via extensions and MCP (Model Context Protocol) servers. The Antigravity ecosystem is positioned for teams that want heavy agent orchestration and a more opinionated, visual surface.

### Who should use what?

- **Quick prototyping & single-file edits:** Gemini CLI + local tests or Copilot for speed.
- **Deep reasoning, long-running research:** Gemini API (Vertex) with high thinking level and function-calling.
- **Agentic orchestration & multi-step automation:** Antigravity for visual management or a custom agent pipeline using function calling + MCP.
- **Multi-provider experiments / cost control:** Use CometAPI or similar aggregators to switch models or try Flash vs Pro economically.

Design considerations for integrating:

- **Security**: avoid sending secrets or PII in prompts. Use token-scoped service accounts for server-side calls.
- **Local vs cloud**: run lightweight assistant features locally (fast completions) but route heavy multimodal analysis to the cloud.
- **User control**: expose “explain this suggestion” and easy rollback controls for code edits produced by the model.

## Integration patterns & recommended architecture

### Lightweight app (chat or assistant)

- Client (browser/mobile) → backend microservice → Gemini API (thinking\_level=low)
- Use streaming / partial outputs for chat UX. Validate user inputs, and never allow raw tool calls from untrusted clients.

### Agentic backend (automated workflows)

- Orchestrator service: register a small set of whitelisted tools (DB read, CI job runner, internal APIs).
- Let Gemini plan and emit tool calls; the orchestrator executes validated calls and returns results. Use high thinking\_level for planning phases and medium for execution steps.

### Multimodal ingestion pipeline

Preprocess and index large documents, images, or videos.

## When should you pick Gemini 3.1 Pro?

Choose Gemini 3.1 Pro when you need:

- high-fidelity, multi-step reasoning across multimodal inputs;
- reliable tool orchestration and agentic workflows;
- better code synthesis/edit loops in IDEs (via Copilot/CLI/Antigravity); or
- to prototype cross-provider comparisons with a gateway like CometAPI.

If you care about throughput and cost, adopt a mixed strategy: default to **medium** thinking for most workflows, **low** for high-throughput user chat, and **high** only for tasks that demonstrably need deeper reasoning (planning, proofs, multi-step synthesis).

## Final thoughts: where Gemini 3.1 Pro fits in the stack

Gemini 3.1 Pro doubles down on what modern developer-facing LLMs must offer: multimodal understanding, explicit tool orchestration, and pragmatic controls for reasoning budget. Whether you access it directly through Google’s APIs and Vertex, through Copilot on premium plans, or via multi-model platforms such as CometAPI, the critical skills for teams are the same: careful thinking-level orchestration, safe function-calling patterns, and integration into solid developer workflows (CLI, IDE, automated tests).

Developers can access [Gemini 3.1 Pro](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/) via [CometAPI](https://www.cometapi.com/) now.To begin, explore the model’s capabilities in the [Playground](https://blendspace.ai/chat) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions.  Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up fo Gemini 3.1 pro today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-use-gemini-3-1-pro-api/](https://www.cometapi.com/how-to-use-gemini-3-1-pro-api/).*
