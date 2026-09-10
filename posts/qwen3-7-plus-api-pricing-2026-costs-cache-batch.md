<!-- social-ops-fingerprint:45dc2cc280fb5687cea66159cf84fe336e8bdae9712ef57f98cfce244eebb46a -->
---
title: Qwen3.7 Plus API Pricing 2026: Costs, Cache & Batch
---
# Qwen3.7 Plus API Pricing 2026: Costs, Cache & Batch

![Qwen3.7 Plus API Pricing 2026: Costs, Cache & Batch](https://resource.cometapi.com/qwen3-7-plus-api-pricing.png)

**TL;DR Qwen3.7 Plus starts at $0.40/M input** and **$1.60/M output** on Alibaba’s US-local route, while the Global route starts at **$0.276/M and $1.101/M.** For comparison, CometAPI currently lists the model at **$0.32/M** input **and $1.28/M output.** The main cost risk is Alibaba’s 256K threshold: once a request crosses it, the higher tier applies to the entire request.

## Qwen3.7 Plus API Pricing at a Glance

Qwen3.7 Plus does not have one universal API price. The final cost depends on the deployment route, request length, temporary discounts, cache usage, thinking output, Web Search calls, and regional feature availability.

| Route | Input tokens per request | Input price / 1M | Output price / 1M | Current pricing note |
| --- | --- | --- | --- | --- |
| Alibaba US-local qwen3.7-plus-us | 0–256K | $0.40 | $1.60 | No promotion label shown on the current US-local row |
| Alibaba US-local qwen3.7-plus-us | >256K–1M | $1.20 | $4.80 | Higher tier applies to the entire request |
| Alibaba Global qwen3.7-plus | 0–256K | $0.28 | $1.10 | Limited-time daytime and nighttime discounts are currently shown |
| Alibaba Global qwen3.7-plus | >256K–1M | $0.83 | $3.30 | Limited-time daytime and nighttime discounts are currently shown |
| Alibaba International qwen3.7-plus | 0–256K | $0.40 list price | $1.60 list price | Current page shows a limited-time 20% discount |
| Alibaba International qwen3.7-plus | >256K–1M | $1.20 list price | $4.80 list price | Current page shows a limited-time 20% discount |
| CometAPI routed qwen3.7-plus | Check live route | $0.32 | $1.28 | Headline price shown on the current model page |

Alibaba documents a **1,000,000-token** **context window** for `qwen3.7-plus`.

![qwen37-plus-us-global-pricing](https://resource.cometapi.com/qwen37-plus-us-global-pricing.PNG "Alibaba Cloud Qwen3.7 Plus pricing for Global and US-local routes, including the 256K tier boundary.")

*Sources:\*\**[*Alibaba Cloud Model Studio pricing*](https://www.alibabacloud.com/help/en/model-studio/model-pricing)

### A Note on Temporary Alibaba Discounts

Alibaba’s current pricing table labels Global `qwen3.7-plus` with a **limited-time 20% daytime discount and 60% nighttime discount**.

The published nighttime window is **22:00–08:00** **UTC**\*\*+8\*\*, based on billing time. The International route currently shows a **limited-time 20% discount**.

Because these promotions may change or expire, the calculations below use standard list prices unless explicitly stated otherwise. For a live production forecast, check the Model Studio console and pricing page on the day you run traffic.

## Alibaba US-Local vs Global Pricing

The most important distinction for US developers is that Alibaba’s US-local and Global routes do not use the same price row.

The US-local model ID is:

```
qwen3.7-plus-us
```

Its list price starts at:

- $0.40 per 1M input tokens
- $1.60 per 1M output tokens

The Global model ID is:

```
qwen3.7-plus
```

Its list price starts at:

- $0.276 per 1M input tokens
- $1.101 per 1M output tokens

The Global route is cheaper based on the published list price, but cost should not be the only routing factor.

Teams should also consider:

- Data residency requirements
- Regional availability
- Latency
- Tool support
- Compliance requirements
- Service stability
- Temporary provider discounts

A lower-priced Global route may not be suitable for workloads that require processing in a specific region.

## How the 256K Pricing Tier Works

Alibaba Cloud uses the total number of input tokens in a single request to select the pricing tier.

If a request crosses 256K input tokens, the higher unit price applies to every token billed in that request, including output tokens at the output rate shown for the higher tier.

A 300K-token request is not billed as:

- 256K tokens at the lower price
- 44K tokens at the higher price

Instead, the entire request uses the higher pricing tier.

For the US-local route, this means the price changes from:

- $0.40 to $1.20 per 1M input tokens
- $1.60 to $4.80 per 1M output tokens

The higher rates apply to all billable input and output tokens in that request.

## Qwen3.7 Plus Cost Examples

### Example 1: A Request Below 256K

Assume a request contains:

- 100,000 input tokens
- 10,000 output tokens

| Route | Input calculation | Output calculation | Estimated list-price cost |
| --- | --- | --- | --- |
| Alibaba US-local | 100K ÷ 1M × $0.40 = $0.0400 | 10K ÷ 1M × $1.60 = $0.0160 | $0.0560 |
| Alibaba Global | 100K ÷ 1M × $0.276 = $0.0276 | 10K ÷ 1M × $1.101 = $0.0110 | $0.0386 |
| CometAPI | 100K ÷ 1M × $0.32 = $0.0320 | 10K ÷ 1M × $1.28 = $0.0128 | $0.0448 |

The Alibaba figures above use published list prices before any applicable temporary discount.

### Example 2: A Request Above 256K

Now assume a request contains:

- 400,000 input tokens
- 20,000 output tokens

Because the request exceeds 256K input tokens, Alibaba Cloud applies the higher tier to all input and output tokens in the request.

| Route | Input calculation | Output calculation | Estimated cost |
| --- | --- | --- | --- |
| Alibaba US-local | 400K ÷ 1M × $1.20 = $0.4800 | 20K ÷ 1M × $4.80 = $0.0960 | $0.5760 |
| Alibaba Global | 400K ÷ 1M × $0.826 = $0.3304 | 20K ÷ 1M × $3.301 = $0.0660 | $0.3964 |
| CometAPI headline-rate scenario\* | 400K ÷ 1M × $0.32 = $0.1280 | 20K ÷ 1M × $1.28 = $0.0256 | $0.1536\* |

\*The CometAPI figure is a **conditional estimate**, not a confirmed production price for requests above 256K.

CometAPI’s public model page currently displays one headline rate and approximately 991.8K maximum input tokens. However, it does not state whether requests above 256K:

- Keep the same headline price
- Use a separate long-context pricing tier
- Incur an additional routing surcharge

If the headline rates remain unchanged above 256K, the estimated cost would be:

- Input: 400K ÷ 1M × $0.32 = $0.1280
- Output: 20K ÷ 1M × $1.28 = $0.0256
- Total: **$0.1536**
- ![cometapi-qwen37-plus-headline-price](https://resource.cometapi.com/cometapi-qwen37-plus-headline-price.png "CometAPI Qwen3.7 Plus headline token price and context limits")
- *Source*\*:\* [*CometAPI Qwen3.7 Plus Pricing*](https://www.cometapi.com/models/aliyun/qwen3-7-plus/)

### Can Splitting a Large Request Reduce the Cost?

In some cases, yes.

Suppose the 400K-input task can be divided into two independent requests, each containing:

- 200K input tokens
- 10K output tokens

On the US-local route:

| Plan | Calculation | Estimated cost |
| --- | --- | --- |
| One 400K-input request | $0.4800 input + $0.0960 output | $0.576 |
| Two 200K-input requests | 2 × [($0.0800 input) + ($0.0160 output)] | $0.192 |

The two-request version is significantly cheaper because both calls remain below the 256K boundary.

However, this is an illustrative optimization rather than a universal recommendation.

Splitting a task can introduce:

- Duplicated context
- Additional API calls
- More orchestration logic
- Higher latency
- Loss of cross-document context
- Lower answer quality

Use this approach only when the work can be separated without weakening the final result.

## Context Cache Pricing for Qwen3.7 Plus

Context Cache can reduce the cost of repeated system prompts, repository context, policy documents, product catalogs, and other reusable reference material.

Alibaba Cloud offers explicit and implicit Context Cache modes.

| Cache mode | Cache creation | Cached-input price | Operational detail |
| --- | --- | --- | --- |
| Explicit cache | 125% of standard input price | 10% of standard input price | Five-minute validity; timer resets after a hit; deterministic within validity |
| Implicit cache | 100% of standard input price | 20% of standard input price | Automatic common-prefix detection; hit probability is not guaranteed |

Source: [Alibaba Cloud Context Cache documentation](https://www.alibabacloud.com/help/en/model-studio/context-cache).

### Context Cache Cost Example

Assume a US-local workflow repeatedly sends:

- 80K stable prefix tokens
- 5K new input tokens
- 5K output tokens

| Scenario | Input cost | Output cost | Estimated cost per request |
| --- | --- | --- | --- |
| No cache | 85K ÷ 1M × $0.40 = $0.0340 | 5K ÷ 1M × $1.60 = $0.0080 | $0.04 |
| Implicit cache hit on 80K | (80K ÷ 1M × $0.08) + (5K ÷ 1M × $0.40) = $0.0084 | $0.01 | $0.02 |
| Explicit cache hit on 80K | (80K ÷ 1M × $0.04) + (5K ÷ 1M × $0.40) = $0.0052 | $0.01 | $0.01 |

The explicit cache has a **five-minute validity period that resets after a successful hit**, not a one-hour minimum TTL.

Its creation tokens cost 125% of the normal input price, while later cache hits cost 10%.

### When Does Explicit Cache Become Cheaper?

For the stable prefix alone, let **N** represent the total number of identical-prefix requests.

The normalized explicit-cache cost is:

```
1.25 + 0.10 × (N − 1)
```

An ideal implicit-cache sequence is:

```
1.00 + 0.20 × (N − 1)
```

Under the simplifying assumption that every request after the first receives an implicit-cache hit, explicit cache becomes cheaper at **four total requests**:

- One cache-creation request
- Three successful cache reuses

Compared with no caching at all, explicit caching becomes cheaper by the second total request.

In real workloads, the break-even point can vary because implicit-cache hits are not guaranteed.

Track:

- Cached input tokens
- Cache-creation tokens
- Uncached input tokens
- Output tokens
- Cache hit rate
- Retry count
- Task success rate

Lower token spend does not help if cache misses or quality regressions lead to more retries.

## Qwen Web Search Pricing

For `qwen3.7-plus`, Alibaba directs developers to use the Responses API `web_search` tool.

Web Search adds two separate cost components:

1. Retrieved web content is added to the model prompt and billed as normal input tokens.
2. The search policy has a separate per-1,000-call fee.

The current documented `agent` policy rates are:

| Deployment scope | Web Search fee / 1,000 calls |
| --- | --- |
| Chinese mainland and Global | $0.57 |
| International | $10.00 |

Source: [Alibaba Cloud Web Search documentation](https://www.alibabacloud.com/help/en/model-studio/web-search).

The support table currently lists `qwen3.7-plus` for Global and International deployment scopes, but it does **not** list the US-local model ID `qwen3.7-plus-us`.

Verify tool availability before designing a US-local workflow around Alibaba’s built-in Web Search feature.

### International Web Search Cost Example

Assume a request contains:

- 10K normal input tokens
- 2K output tokens
- Two Web Search calls

Before counting the additional tokens returned by the search engine:

| Cost component | Calculation | Cost |
| --- | --- | --- |
| Model input | 10K ÷ 1M × $0.40 list price | $0.0040 |
| Model output | 2K ÷ 1M × $1.60 list price | $0.0032 |
| Web Search | 2 ÷ 1,000 × $10.00 | $0.0200 |
| Total before retrieved-content tokens | $0.0040 + $0.0032 + $0.0200 | $0.0272 |

The search-policy fee represents:

```
$0.0200 ÷ $0.0272 = 73.5%
```

In this example, the search fee accounts for **73.5% of the total before retrieved-content tokens are included**, or 74% when rounded to the nearest whole percentage point.

On the Global route, the per-call policy fee is much lower. However, retrieved web pages can still increase input-token usage significantly or push a long-running agent across the 256K pricing boundary.

For search-grounded workflows, track both:

- Number of search calls
- Number of retrieved-content tokens

## Batch API Pricing and Availability

Alibaba’s Batch File API charges successful input and output tokens at **50% of the corresponding real-time inference price**.

It is designed for offline workloads where immediate responses are not required, including:

- Model evaluations
- Document tagging
- Large-scale classification
- Synthetic data generation
- Nightly enrichment
- Offline multimodal processing
- Benchmark runs

However, the Batch discount should not automatically be included in every Qwen3.7 Plus cost forecast.

The current documentation states that:

- The exact `qwen3.7-plus` model is listed under **China (Beijing)**.
- The Singapore Batch scope lists generic aliases such as `qwen-plus`, rather than the exact `qwen3.7-plus` model ID.
- The documentation does not list `qwen3.7-plus-us` as a supported US-local Batch model.
- Supported Qwen3.7 Plus Batch requests have a maximum context of **256K**, not 1M.
- Batch does **not** support Context Cache.
- Batch and cache discounts cannot be combined.
- Thinking mode is enabled by default for Qwen3.7-series Batch jobs unless explicitly configured.
- Thinking tokens are billed at the output-token rate.
- The configurable `completion_window` is a maximum waiting period between **24 and 336 hours**.
- The completion window is not a guarantee that every job will take 24 hours or complete at a specific time.
- ![qwen37-batch-support-thinking-window](https://resource.cometapi.com/qwen37-batch-support-thinking-window.png "qwen37 batch support thinking window")
- *Source*\*:\* [*Alibaba Cloud OpenAI-compatible Batch API documentation*](https://www.alibabacloud.com/help/en/model-studio/batch-interfaces-compatible-with-openai/)*\*\*.*

### A 50% Batch Discount Does Not Always Mean a 50% Cheaper Task

Batch halves the unit price of input and output tokens. It does not control how many thinking tokens the model generates.

The following example uses the US-local input/output price ratio only to illustrate the arithmetic. It does **not** imply that the US-local route currently supports Batch.

| Illustrative scenario | Input tokens | Output including thinking | Estimated cost |
| --- | --- | --- | --- |
| Real-time, thinking disabled | 100K | 10K | $0.0560 |
| Batch, moderate thinking | 100K | 40K | $0.0520 |
| Batch, heavier thinking | 100K | 50K | $0.0600 |

The real-time example is calculated as:

- Input: 100K ÷ 1M × $0.40 = $0.0400
- Output: 10K ÷ 1M × $1.60 = $0.0160
- Total: **$0.0560**

The moderate-thinking Batch example is calculated using half-price rates:

- Input: 100K ÷ 1M × $0.20 = $0.0200
- Output: 40K ÷ 1M × $0.80 = $0.0320
- Total: **$0.0520**

The heavier-thinking Batch example is:

- Input: 100K ÷ 1M × $0.20 = $0.0200
- Output: 50K ÷ 1M × $0.80 = $0.0400
- Total: **$0.0600**

In the final scenario, additional thinking output completely eliminates the nominal Batch saving.

For deterministic offline workloads such as classification, extraction, tagging, and formatting, explicitly set:

```
{
  "enable_thinking": false
}
```

For harder tasks, set an appropriate `thinking_budget` and compare cost per successful task instead of assuming the headline Batch discount will reduce the final bill by exactly 50%.

For US or Global planning, treat Batch savings as **unconfirmed** until the exact model ID and route appear in your current console or regional documentation.

## Thinking Tokens and Output Costs

Qwen3.7 Plus supports thinking and non-thinking modes.

Thinking can improve performance on complex reasoning, coding, planning, and agent workflows. However, thinking tokens increase output usage and are billed at the output-token rate.

This matters because output tokens are four times more expensive than input tokens on the Alibaba Qwen3.7 Plus pricing tiers.

For the US-local route below 256K:

- Input: $0.40 per 1M tokens
- Output: $1.60 per 1M tokens

Above 256K:

- Input: $1.20 per 1M tokens
- Output: $4.80 per 1M tokens

For cost-sensitive workloads, consider disabling or limiting thinking for straightforward tasks such as:

- Data extraction
- Formatting
- Classification
- Content tagging
- Simple summarization
- Basic routing
- Structured output generation

Use longer thinking budgets only when evaluation data shows that they materially improve task completion.

## Qwen3.7 Plus vs Qwen3.7 Max vs Qwen3.6 Plus

| Model | Current CometAPI listed price | Best first test | Main cost consideration |
| --- | --- | --- | --- |
| qwen3.7-plus | $0.32/M input; $1.28/M output | Multimodal agents, screenshots, visual coding, documents, charts, and UI workflows | 256K boundary on direct Alibaba routes, tool loops, and thinking output |
| qwen3.7-max | $1.36/M input; $4.08/M output | Text-only autonomous coding, deep reasoning, and long-horizon agents | Current Qwen API listings show text input only; do not route image or video workloads to Max |
| qwen3.6-plus | $0.32/M input; $1.92/M output | Migration baseline for existing Qwen3.6 workflows | Higher listed output price than Qwen3.7 Plus |

*Sources:* [*CometAPI Qwen3.7 Plus model page*](https://www.cometapi.com/models/aliyun/qwen3-7-plus/)*\*\*；* [*CometAPI Qwen3.7 Max model page*](https://www.cometapi.com/models/aliyun/qwen3-7-max/)***；***[*CometAPI Qwen3.6 Plus model page*](https://www.cometapi.com/models/aliyun/qwen3-6-plus/)

Qwen positions Qwen3.7 Plus as a multimodal model for visual understanding, coding, GUI interaction, tool use, and productivity workflows.

Current Qwen API listings show Qwen3.7 Max with **text input and text output**, while Alibaba’s visual-understanding documentation lists Qwen3.7 Plus for image and video input.

Start with Plus when the task includes:

- Images
- Video
- Screenshots
- Documents
- Charts
- Interface state
- Visual coding
- GUI interaction

Test Max for text-only work when a stronger solved task rate could justify the higher token cost.

## How to Reduce Qwen3.7 Plus API Costs

### 1. Measure Traffic Around the 256K Boundary

Group production requests by total input length:

- 0–32K
- 32K–128K
- 128K–256K
- Above 256K

Then review which workflows genuinely need the highest pricing tier.

A request should not cross 256K simply because every available document, conversation turn, tool result, or repository file was included by default.

### 2. Add a Preflight Token Guard

Use a model-compatible token counter in the application or API-gateway layer before every request is sent.

The following thresholds are an engineering heuristic rather than an Alibaba rule:

- **Below 220K:** Send normally.
- **Between 220K and 240K:** Log a warning and prevent unnecessary context growth.
- **Above approximately 240K:** Compact the context before sending.
- **Above 256K:** Proceed only when the expected quality gain justifies the higher Alibaba pricing tier.

When the guard is triggered, the workflow can:

1. Summarize older tool outputs.
2. Remove duplicate search results.
3. Replace raw logs with structured error summaries.
4. Retrieve only the most relevant document chunks.
5. Move older conversation turns into a compressed memory block.
6. Split genuinely independent document groups into separate calls.
7. Route the task to a provider with a confirmed flat long-context price, when appropriate.

Leave some safety headroom because:

- Image inputs consume tokens
- Tool schemas add context
- System messages may be large
- Retrieved web content can grow unexpectedly
- Tokenizers can count the same text differently

Observability tools such as Langfuse can help monitor token usage. A gateway such as APISIX can enforce the boundary when paired with a suitable tokenizer or custom routing policy.

### 3. Put Stable Content First

Place reusable content near the beginning of the prompt, including:

- System instructions
- Policy blocks
- Tool schemas
- Repository summaries
- Product catalogs
- Reusable documents
- Brand guidelines
- Output schemas

Place highly variable user content later.

Stable prefixes improve the chance of an implicit cache hit and make explicit cache blocks easier to manage.

### 4. Summarize Old Tool Results

Agent workflows can accumulate large amounts of context through:

- Search results
- Browser output
- Code-execution logs
- Previous model responses
- Error messages
- Tool schemas

Instead of retaining all raw output, periodically summarize older context and keep only the information required for the next step.

### 5. Control Thinking Output

Log thinking tokens separately from visible answer tokens.

For simple tasks, disable thinking where supported or set a smaller reasoning budget.

For complex tasks, compare the additional reasoning cost with the reduction in retries, errors, and human review.

### 6. Count Tool Calls and Retrieved Tokens

For Web Search agents, record:

- Search calls
- Extractor calls
- Retrieved-content tokens
- Search retries
- Model retries
- Fallback calls
- Final task result

The search-tool fee can dominate small requests, while retrieved content can dominate long requests.

### 7. Optimize for Cost per Completed Task

Do not compare routes only by their advertised cost per million tokens.

Measure:

- Cost per request
- Cost per completed task
- Task success rate
- Retry rate
- Fallback rate
- Cache hit rate
- Search calls per task
- Latency
- Human-review time

A cheaper model can become more expensive if it generates incorrect answers, requires additional calls, or creates more manual work.

## A Practical Qwen3.7 Plus Evaluation Plan

Before moving production traffic, create a focused evaluation set based on your actual workloads.

A 30-task test set is usually enough to identify major differences in cost, latency, and completion quality.

| Evaluation slice | Example tasks | Primary metric |
| --- | --- | --- |
| Visual understanding | Screenshots, receipts, charts, and UI pages | Correctness and evidence quality |
| Visual coding | Mockup-to-component, screenshot-to-frontend, and SVG reconstruction | Runnable output and edit time |
| Long context below 256K | Policies, repositories, and document sets | Accuracy, latency, and cache hit rate |
| Over-256K stress | Tasks with 300K–600K input tokens | Quality gained versus additional tier cost |
| Search-grounded QA | Current facts and product research | Search calls, retrieved tokens, and grounded accuracy |
| Agent workflow | Multi-step coding or browser tasks | Solved-task rate, retries, latency, and total cost |

For each task, record:

- Input tokens
- Output tokens
- Thinking tokens
- Cached tokens
- Cache-creation tokens
- Search calls
- Retrieved-content tokens
- Latency
- Number of retries
- Final task result

The [CometAPI Cookbook](https://github.com/cometapi-dev/cometapi-cookbook) includes additional integration and model-routing examples for this type of evaluation.

## FAQ

### How Much Does the Qwen3.7 Plus API Cost?

Alibaba’s US-local `qwen3.7-plus-us` route costs **$0.40 per 1M input tokens and $1.60 per 1M output tokens** for requests with up to 256K input tokens.

For requests above 256K and up to 1M, the price increases to **$1.20 per 1M input tokens and $4.80 per 1M output tokens**.

Alibaba’s Global route has the lowest published list price in this comparison. The model is also available through CometAPI at a listed rate of **$0.32 per 1M input tokens and $1.28 per 1M output tokens.**

### How Are Long-Context Requests Priced Through CometAPI?

The Qwen3.7 Plus listing shows a single rate of $0.32/M input and $1.28/M output, but it does not currently specify whether a separate tier applies above 256K tokens.

At the displayed rate\*\*, a request with 400K input tokens and 20K output tokens would cost $0.1536\*\*. Treat this as an estimate until the long-context billing policy has been confirmed.

### Is Qwen3.7 Plus Available in the US?

Yes. Alibaba lists a US-local model ID called `qwen3.7-plus-us` in the US (Virginia) region.

Alibaba also lists the Global `qwen3.7-plus` route in the same regional pricing section.

Choose a route based on:

- Deployment requirements
- Data-processing location
- Tool support
- Latency
- Availability
- Effective price

### Why Does Qwen3.7 Plus Pricing Jump After 256K Tokens?

Alibaba chooses the pricing tier based on the total input-token count in a single request.

Once the request exceeds 256K input tokens, all billed input and output tokens in that request use the rates shown for the higher tier.

The pricing is not calculated progressively.

### Does Context Cache Reduce Qwen3.7 Plus Costs?

Yes.

Alibaba states that explicit cache hits are billed at **10% of the normal input rate**, while implicit cache hits are billed at **20%**.

Explicit cache creation costs **125% of the normal input price**, and the cache remains valid for five minutes, with the timer resetting after each successful hit.

Under an ideal comparison with repeated implicit-cache hits, explicit cache becomes cheaper after one creation and three successful reuses.

### How Does Qwen Web Search Pricing Work?

Web Search adds two costs:

1. Retrieved web content increases normal input-token usage.
2. The search tool has a separate per-1,000-call fee.

The current documented rate is:

- $0.573411 per 1,000 calls for Global and Chinese-mainland deployment scopes
- $10 per 1,000 calls for International deployment

### Does Qwen3.7 Plus Support the Batch API?

The exact `qwen3.7-plus` model is currently listed for Batch under China (Beijing), where successful tokens are charged at 50% of real-time inference prices and the context is capped at 256K.

The current documentation does not list the US-local `qwen3.7-plus-us` route for Batch.

Do not assume the Batch discount applies to US-local or Global deployments without checking current console availability.

### Is Qwen3.7 Plus Cheaper Than Qwen3.7 Max?

Yes, based on the listed rates used in this comparison.

Qwen3.7 Plus is listed at:

- $0.32 per 1M input tokens
- $1.28 per 1M output tokens

Qwen3.7 Max is listed at:

- $1.36 per 1M input tokens
- $4.08 per 1M output tokens

Max can still be more economical for difficult text-heavy agent tasks if it completes them with fewer retries.

### Should I Use Alibaba Directly or an API Aggregator?

Direct Alibaba access is the clearer choice when a workload depends on a specific deployment scope, native provider feature, regional control, or direct billing relationship.

An aggregation layer can be more practical when the same application needs to test or route across several model families. CometAPI, for example, exposes Qwen3.7 Plus alongside models from providers such as OpenAI, Anthropic, Google, Moonshot, and DeepSeek through an OpenAI-compatible interface.

The better route depends on regional requirements, effective cost, integration effort, fallback needs, and whether native Alibaba features are required.

### Run a Production-Style Comparison Before Choosing a Route

Published token rates are useful for narrowing the options, but the final decision should come from a workload that resembles production.

One practical approach is to run the same evaluation set across Qwen3.7 Plus, Qwen3.7 Max, and a few relevant alternatives. A unified API service such as CometAPI can simplify this comparison by exposing Qwen, Claude, Gemini, GPT, Kimi, and DeepSeek models through the same OpenAI-compatible interface.

During the test, record:

- Input and output tokens
- Thinking-token usage
- Cache usage
- Tool calls
- Retries
- Latency
- Task success

Use the [Qwen3.7 Plus model](https://www.cometapi.com/models/aliyun/qwen3-7-plus/) as a starting point, then choose the route with the lowest cost per completed task—not simply the lowest advertised token price.

---

*Originally published at [https://www.cometapi.com/qwen3-7-plus-api-pricing/](https://www.cometapi.com/qwen3-7-plus-api-pricing/).*
