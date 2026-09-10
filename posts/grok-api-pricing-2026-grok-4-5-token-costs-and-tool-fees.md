<!-- social-ops-fingerprint:16f53c9e5113d92d514213a7a741407470e22d5e05178b112b8c6d549c55bfe8 -->
---
title: Grok API Pricing 2026: Grok 4.5, Token Costs, and Tool Fees
---
# Grok API Pricing 2026: Grok 4.5, Token Costs, and Tool Fees

![Grok API Pricing 2026: Grok 4.5, Token Costs, and Tool Fees](https://resource.cometapi.com/cfa563ed-0c19-44d0-9d00-7733f8682881.png)

**TL;DR** Grok API pricing is not just one token table. xAI's current API lineup now includes `grok-4.5` at **$2 / $0.50 / $6 per 1M input/cached-input/output tokens**, `grok-4.3` at **$1.25 / $0.20 / $2.50**, and `grok-build-0.1` for code at **$1.00 / $0.20 / $2.00**.

The hidden cost is everything around the base model row: Web Search, X Search, Code Execution, Imagine, Voice, priority processing, batch mode, storage, retries, and usage-guideline violation fees can all change the final bill.

For builders, the practical question is not "Is Grok cheap?" It is: **Which Grok model, tools, and service tier produce the lowest cost per successful task?**

## Grok API Pricing Snapshot

| Item | Current xAI API detail |
| --- | --- |
| Latest flagship model | grok-4.5 |
| Lower-cost chat route | grok-4.3 |
| Coding model | grok-build-0.1 |
| Best first tests | Chat, coding agents, search-grounded workflows, image/video generation |
| Grok 4.5 context | 500k tokens |
| Grok 4.3 context | 1M tokens |
| Grok Build context | 256k tokens |
| Grok 4.5 price | $2.00 input / $0.50 cached input / $6.00 output per 1M tokens |
| Grok 4.3 price | $1.25 input / $0.20 cached input / $2.50 output per 1M tokens |
| Grok Build price | $1.00 input / $0.20 cached input / $2.00 output per 1M tokens |
| Tool cost caveat | Web Search, X Search, and Code Execution are each $5 / 1k calls |
| Priority cost caveat | Priority processing is 2x standard token pricing when applied |
| Required telemetry | tokens, cached tokens, reasoning tokens, tool calls, priority tier, cost\_in\_usd\_ticks, success rate |

## The Three Numbers That Change Your Grok Bill

- **$0.20-$0.50 cached input per 1M tokens**: prompt caching can matter for repeated long prompts.
- **$5 / 1k Web Search, X Search, or Code Execution calls**: tool-heavy agents can spend more on tools than tokens.
- **2x priority token pricing**: priority processing is a latency feature, not a default setting.

## Why Grok API Cost Is More Than Token Pricing

The headline token rate only explains part of a Grok API bill. Search-grounded and agentic workflows may also incur server-side tool fees, while priority processing, media generation, storage, retries, and usage-guideline violation fees change the effective cost of a successful task.

## What Actually Shipped

xAI's `Grok 4.5`documentation and pricing page list grok-4.5 as the latest flagship model, with a **500k** context window and pricing of **$2 input, $0.50 cached input, and $6 output per 1M tokens.** The [models page](https://docs.x.ai/developers/models) positions Grok 4.5 as the flagship route for code, tool calling, and knowledge work, while Grok 4.3 remains a lower-cost 1M-context route and Grok Build remains relevant for code-focused testing.

![Grok API Pricing 2026: Grok 4.5, Token Costs, and Tool Fees](https://resource.cometapi.com/blog/uploads/2026/07/grok-4.5.jpg)

Source: [xAI Grok 4.5 documentation](https://docs.x.ai/developers/grok-4-5)

The key pricing change for builders is that "latest" and "best route" are no longer the same decision. Grok 4.5 is the new frontier option, but Grok 4.3 can still be the better cost route for long-context or high-volume workloads. For a deeper look at the latest release, [CometAPI's Grok 4.5 architecture,](https://www.cometapi.com/grok-4-5-leak-xai-s-1-5t-v9-model-in-private-beta/) release timeline, and availability overview provides additional context.

## What Builders Are Discussing

The public discussions cited here focus less on the headline token rate and more on compounded usage, tool calls, speed, and policy-related request costs. The [Hacker News Grok 4.3 discussion](https://news.ycombinator.com/item?id=47972447) and [Grok API pricing discussion on r/grok](https://www.reddit.com/r/grok/comments/1kyvsol/what_does_everyone_think_of_the_grok_api_pricing/) are useful operational signals, but the pricing figures in this guide follow xAI's official documentation.

## Grok API Pricing Table

xAI's [pricing documentation](https://docs.x.ai/developers/pricing) lists prices in USD and separates code, chat, Imagine, Voice, tools, batch, and priority processing.

| API area | Model or mode | Context / unit | Price |
| --- | --- | --- | --- |
| Code API | grok-build-0.1 | 256k context | $1.00 input / $0.20 cached input / $2.00 output per 1M tokens |
| Chat API | grok-4.5 | 500k context | $2.00 input / $0.50 cached input / $6.00 output per 1M tokens |
| Chat API | grok-4.3 | 1M context | $1.25 input / $0.20 cached input / $2.50 output per 1M tokens |
| Chat API | grok-4.20-multi-agent-0309 | 1M context | $1.25 input / $0.20 cached input / $2.50 output per 1M tokens |
| Chat API | grok-4.20-0309-reasoning | 1M context | $1.25 input / $0.20 cached input / $2.50 output per 1M tokens |
| Chat API | grok-4.20-0309-non-reasoning | 1M context | $1.25 input / $0.20 cached input / $2.50 output per 1M tokens |
| Voice API | Realtime Text Input | per message | $0.004 per message |
| Voice API | Realtime | per minute / hour | $0.05 per minute, or $3.00 per hour |
| Voice API | Text to Speech | characters | $15.00 per 1M characters |
| Voice API | Speech to Text | audio hour | $0.10 / hr REST, $0.20 / hr streaming |

## Grok 4.5 vs Other Mainstream API Prices

The base token row makes Grok 4.5 look cheaper than some frontier routes but more expensive than Grok 4.3. The comparison below uses text pricing from the official provider pages as of July 10, 2026, and should be treated as a snapshot, not a routing decision by itself.

| Provider | Model | Input price | Cached input | Output price | Pricing note |
| --- | --- | --- | --- | --- | --- |
| xAI | grok-4.5 | $2.00 / 1M | $0.50 / 1M | $6.00 / 1M | Latest Grok flagship |
| xAI | grok-4.3 | $1.25 / 1M | $0.20 / 1M | $2.50 / 1M | Lower-cost Grok chat route |
| OpenAI | gpt-5.6 | $5.00 / 1M | $0.50 / 1M | $30.00 / 1M | Standard short-context pricing; Batch/Flex are 50% lower |
| Anthropic | claude-sonnet-5 | $2.00 intro, then $3.00 / 1M | $0.20 intro, then $0.30 / 1M cached read | $10.00 intro, then $15.00 / 1M | Intro pricing through Aug. 31, 2026 |
| Google | gemini-3.1-pro-preview | $1.25 / 1M, or $2.50 over 200k prompts | $0.125 / 1M, or $0.25 over 200k prompts | $10.00 / 1M, or $15.00 over 200k prompts | Output includes thinking tokens |

The takeaway is simple: Grok 4.5 is not the cheapest Grok route, but its output price sits below several high-end text models. For production, compare total cost per successful task, not only input/output token rows.

For image and video generation, the price unit changes from tokens to images or seconds:

| Imagine model | Input cost | Output cost |
| --- | --- | --- |
| grok-imagine-image-quality | $0.01 / input image | $0.05 / 1K image, $0.07 / 2K image |
| grok-imagine-image | $0.002 / input image | $0.02 / 1K or 2K image |
| grok-imagine-video-1.5 | $0.01 / input image | $0.08 / sec at 480p, $0.14 / sec at 720p, $0.25 / sec at 1080p |
| grok-imagine-video | $0.002 / input image, $0.01 / input sec | $0.05 / sec at 480p, $0.07 / sec at 720p |

For teams testing media workflows rather than text-only chat, CometAPI's [Grok Imagine Video API model page](https://www.cometapi.com/models/xai/grok-imagine-video/) is the better next step than a chat-model pricing table alone.

## The Hidden Cost Layer: Server-Side Tools

The Grok API can use server-side tools, and those tools are not free. The pricing page states that requests using xAI-provided tools are billed from two components: model token usage and tool invocations.

| Tool | Tool name | Cost |
| --- | --- | --- |
| Web Search | web\_search | $5 / 1k calls |
| X Search | x\_search | $5 / 1k calls |
| Code Execution | code\_execution, code\_interpreter | $5 / 1k calls |
| File Attachments | attachment\_search | $10 / 1k calls |
| Collections Search | collections\_search, file\_search | $2.50 / 1k calls |
| Image Understanding | view\_image | Token-based |
| X Video Understanding | view\_x\_video | Token-based |
| Remote MCP Tools | Tool name set by each MCP server | No invocation fee; token usage billed |

This is the most important part of the article for teams building search-grounded or agentic apps. A simple answer may be cheap. A tool-heavy answer can include input tokens, reasoning tokens, output tokens, search calls, code execution calls, file search calls, and cached prompt tokens.

Use this as a practical planning lens:

**Workflow cost = request costs + retry request costs + storage and download costs + applicable usage-guideline violation fees**

For each request, token pricing, server-side tool calls, prompt caching, and any applied priority premium are already reflected in `cost_in_usd_ticks`.

If a workflow uses Web Search and X Search on every turn, the tool-call line can matter as much as the model line.

xAI's pricing docs also list a usage-guideline violation fee: if a request is deemed to violate usage guidelines, the request may still be charged; for violations caught before generation in the Responses API, xAI lists a **$0.05 per-request** fee. For public-facing apps, this should be part of the cost and safety plan, not an afterthought.

### Do Not Forget Storage and Download Costs

Tool calls are not the only non-token cost. xAI currently lists file storage at **$0.025 per GiB per day**, collection storage at **$0.10 per GiB per day**, and downloads at **$0.20 per GiB transferred**.

These costs are unlikely to dominate a simple chat app, but they can matter for document-heavy RAG systems, persistent file workflows, and applications that retain large collections over time.

## Example: What Does a Search-Grounded Grok Request Cost?

Here is a simple illustrative example using Grok 4.3 pricing and two Web Search calls:

| Cost component | Assumption | Calculation | Cost |
| --- | --- | --- | --- |
| Input tokens | 2,000 uncached tokens | 2,000 / 1M x $1.25 | $0.0025 |
| Output tokens | 1,000 output tokens | 1,000 / 1M x $2.50 | $0.0025 |
| Successful Web Search tool calls | 2 calls | 2 / 1,000 x $5.00 | $0.0100 |
| Total request cost | tokens + tools | $0.0050 + $0.0100 | $0.0150 |

In this example, token usage costs only **$0.005**, while two Web Search calls cost **$0.01**. That means tools are about **67% of the request cost** even before retries, priority processing, file search, storage, or usage-guideline violation fees. The exact numbers will change by workload, but the lesson is stable: for search-grounded agents, count tool calls first.

## Batch, Priority, and Caching: Three Cost Controls

### 1. Cached input is the first lever

The current pricing table lists cached input at **$0.50 / 1M tokens** for Grok 4.5 and **$0.20 / 1M tokens** for Grok 4.3, Grok Build, and the listed Grok 4.20 variants. That matters for long system prompts, repeated retrieval context, shared instructions, and evaluation harnesses.

Use cached input when:

- the same system prompt repeats across many calls
- the app sends a long policy, tool schema, or product catalog
- the workflow evaluates many similar tasks
- the request pattern is stable enough to reuse prompt blocks

### 2. Batch API is for offline volume

xAI's pricing docs say the Batch API processes large volumes asynchronously, usually within 24 hours, and the listed Grok 4.3 / Grok 4.20 text models receive a **20% batch discount**. The docs also note that image and video generation can use Batch API but are billed at standard rates.

Use batch for:

- offline classification
- nightly enrichment
- synthetic data generation
- bulk summarization
- large eval runs

Do not use batch for low-latency product flows.

### 3. Priority processing is a latency tradeoff

The [release notes](https://docs.x.ai/developers/release-notes) introduced priority processing in June 2026, and the pricing page says priority text requests are billed at a **2x premium** when the response confirms `service_tier: "priority"`.

Use priority only when latency is worth the premium:

- user-facing chat during peak traffic
- customer support escalation
- paid plan experiences
- time-sensitive agent orchestration

Do not turn on priority globally unless you have latency and margin data to justify it.

## How To Track Real Grok API Cost

xAI's [cost tracking documentation](https://docs.x.ai/developers/cost-tracking) says every inference response includes `cost_in_usd_ticks` in the `usage` object across chat completions, Responses API, image generation, and video generation. It also states that tool-heavy requests include token costs and server-side tool invocation costs in that returned value.

That makes Grok unusual in a useful way: you can measure actual request cost without rebuilding the full billing formula yourself.

Track these fields:

- `input_tokens`
- `output_tokens`
- reasoning tokens, where available
- cached prompt tokens
- number of server-side tool calls
- `service_tier`
- `cost_in_usd_ticks`
- retries
- final success or failure

For app analytics, convert ticks to dollars:

```
cost_usd = cost_in_usd_ticks / 10,000,000,000
```

Then report:

```
cost per successful task = total Grok request cost / successful tasks
```

![Grok API Pricing 2026: Grok 4.5, Token Costs, and Tool Fees](https://resource.cometapi.com/blog/uploads/2026/07/grok%20doc.jpg)

Source: [xAI cost tracking documentation](https://docs.x.ai/developers/cost-tracking)

## Which Grok Model Should You Use?

xAI's [model guidance](https://docs.x.ai/developers/models) now points to Grok 4.5 as the flagship model for code and everything else, while Grok 4.3 remains useful as a lower-cost long-context route. Treat the table below as a starting point, then verify with your own cost-per-successful-task data.

| Workload | Start with | Why |
| --- | --- | --- |
| High-stakes chat, coding, tool use, or reasoning | grok-4.5 | Latest flagship route, configurable reasoning, broader capability target |
| Long-context or cost-sensitive chat | grok-4.3 | 1M context and lower token price than Grok 4.5 |
| Dedicated coding cost tests | grok-build-0.1 | Lower input/output token price; still worth testing against Grok 4.5 |
| Image generation or editing | grok-imagine-image or grok-imagine-image-quality | Image-priced, not token-priced |
| Video generation or editing | grok-imagine-video or grok-imagine-video-1.5 | Per-second output pricing |
| Voice agent | Voice API realtime | Per-minute pricing |
| Search-grounded answer | grok-4.5 or grok-4.3 with tools | Include Web/X Search fees in cost model |

## What Builders Should Retest

Do not choose Grok by the base token row alone. Retest:

- Whether Grok 4.5 reduces retries enough to justify its higher token price over Grok 4.3.
- Whether Grok Build is cheaper for coding tasks than using Grok 4.5.
- Whether Web Search and X Search are needed on every turn or only on uncertain turns.
- Whether cached input reduces enough cost to justify prompt-cache engineering.
- Whether priority processing improves p95 latency enough to pay 2x.
- Whether Imagine video costs make sense per generated asset, not per request.
- Whether usage-guideline violation fees affect public chatbot margins.

## A Practical Grok API Cost Eval

Use a 30-task evaluation set:

- 10 general chat or reasoning tasks
- 5 coding tasks
- 5 search-grounded tasks
- 5 image or video generation tasks
- 5 support or classification tasks

Run each workload with:

- Grok 4.5
- Grok 4.3
- Grok Build for coding tasks
- your current default model
- a cheaper fallback model
- a stronger fallback model

Measure:

- pass/fail
- total request cost
- tool invocations
- retries
- p50/p95 latency
- cached input savings
- priority usage
- human edits needed

## What To Watch Next

Watch these over the next few weeks:

1. Whether xAI changes Grok 4.5, Grok 4.3, or Grok Build model aliases.
2. Whether priority processing becomes a default expectation for low-latency apps.
3. Whether tool-heavy Grok apps report predictable costs with `cost_in_usd_ticks`.
4. Whether Grok Imagine video quality improves enough to justify per-second pricing.
5. Whether independent benchmarks confirm Grok 4.5's price/performance claims across real workloads.

## FAQ

### How much does the Grok API cost?

Grok 4.5 costs $2.00 per 1M input tokens, $0.50 per 1M cached input tokens, and $6.00 per 1M output tokens. Grok 4.3 costs $1.25 input, $0.20 cached input, and $2.50 output per 1M tokens. Grok Build 0.1 costs $1.00 input, $0.20 cached input, and $2.00 output per 1M tokens.

### Is Grok API pricing only token-based?

No. Text requests are token-based, but server-side tools add invocation fees, Imagine uses image or per-second video pricing, Voice uses per-minute or per-character pricing, priority processing can add a 2x premium, and certain usage-guideline violations can create per-request fees.

### What is the cheapest Grok model for code?

For code, xAI now positions Grok 4.5 as the flagship model, but `grok-build-0.1` is still the cheaper coding-specific route to test. Use Grok 4.5 when quality or tool-use reliability matters more than the token row; use Grok Build when cost is the first constraint.

### Does Grok charge for Web Search or X Search?

Yes. Web Search and X Search are each listed at $5 per 1,000 calls, in addition to any model token usage.

### Does Grok API show the actual cost of each request?

Yes. xAI's cost tracking docs say API responses include `cost_in_usd_ticks`, which can be converted to dollars by dividing by 10,000,000,000.

### Should I use priority processing?

Only when latency is worth the extra cost. Priority processing is billed at 2x standard token pricing when priority is actually applied.

## Test Grok API Costs With CometAPI

You can use CometAPI to test Grok-style workloads alongside GPT, Claude, Gemini, DeepSeek, and other models in one evaluation workflow. Teams comparing routes can check CometAPI's [pricing page](https://www.cometapi.com/pricing/) before running their own eval. For setup patterns across coding agents, automation tools, and eval frameworks, the [CometAPI Cookbook](https://github.com/cometapi-dev/cometapi-cookbook) is a practical starting point. Start with a small benchmark, log cost per successful task, and choose the model route that wins on your own workload.

---

*Originally published at [https://www.cometapi.com/grok-api-pricing-cost-guide/](https://www.cometapi.com/grok-api-pricing-cost-guide/).*
