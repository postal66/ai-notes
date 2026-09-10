<!-- social-ops-fingerprint:fac545b7091e90d998379e44913851f87b072a7d4ef0c8f55807242e944fa998 -->
---
title: GPT-5.6 Pricing 2026: Sol, Terra & Luna API Costs
---
# GPT-5.6 Pricing 2026: Sol, Terra & Luna API Costs

![GPT-5.6 Pricing 2026: Sol, Terra & Luna API Costs](https://resource.cometapi.com/gpt-5-6-pricing.png)

## TL;DR

**Updated pricing:** GPT-5.6 Standard short-context rates are now **$5 input / $30 output for Sol**, **$2 / $12 for Terra**, and **$0.20 / $1.20 for Luna** per 1 million tokens.

On July 30, 2026, OpenAI reduced GPT-5.6 Terra prices by 20% and Luna prices by 80%. Sol pricing remains unchanged.

**Watch the hidden cost drivers:** the generic `gpt-5.6` alias routes to Sol, requests above **272K input tokens** use higher long-context rates, and output tokens still cost **6× more than input tokens** across all three tiers.

For latency-sensitive Sol workloads, OpenAI’s new **Fast mode** offers up to **2.5× faster processing** at **2× the Standard price**.

## OpenAI API Pricing at a Glance

For users searching broadly for **OpenAI** **API pricing**, the first question is usually: *which current model am I actually paying for?* The table below gives a compact view of several current OpenAI text models before we look more closely at GPT-5.6.

(> **Pricing update — July 30, 2026:** OpenAI reduced GPT-5.6 Terra API prices by 20% and Luna prices by 80%. Terra now costs $2 per 1M input tokens and $12 per 1M output tokens, while Luna costs $0.20 input and $1.20 output. Sol pricing remains unchanged.)

| Model | Input / 1M tokens | Cached input | Output / 1M tokens |
| --- | --- | --- | --- |
| gpt-5.6-sol | $5.00 | $0.50 | $30.00 |
| gpt-5.6-terra | $2.00 | $0.20 | $12.00 |
| gpt-5.6-luna | $0.20 | $0.02 | $1.20 |
| gpt-5.5 | $5.00 | $0.50 | $30.00 |
| gpt-5.4 | $2.50 | $0.25 | $15.00 |
| gpt-5.4-mini | $0.75 | $0.075 | $4.50 |
| gpt-5.4-nano | $0.20 | $0.02 | $1.25 |

At its new price, Luna matches GPT-5.4 nano’s $0.20 input rate while offering a slightly lower output rate of $1.20 versus $1.25.

*Source*\*:\* [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)

The most important pattern is easy to miss: **GPT-5.6 output tokens cost 6× as much as input tokens across Sol, Terra, and Luna.** Long answers, verbose agents, and reasoning-heavy workflows can therefore raise costs faster than small changes in prompt length.

For a broader overview of the GPT-5.6 family—including model capabilities, positioning, benchmarks, API access, and key launch features—see OpenAI's [GPT-5.6 announcement](https://openai.com/index/gpt-5-6/) or CometAPI's [GPT-5.6 guide.](https://www.cometapi.com/gpt-5-6-guide-consideration-api-key-access/) This article focuses specifically on pricing, cost calculations, and the factors that can affect your real API bill.

## GPT-5.6 Pricing: Sol vs Terra vs Luna

GPT-5.6 introduces three pricing tiers. OpenAI positions Sol as the flagship route, Terra as the balanced option, and Luna as the lower-cost tier for high-volume workloads.

For a deeper look at the capabilities, how to access to GPT-5.6 API, and use cases of each model,details to see the here about [GPT-5.6 model](https://www.cometapi.com/models/openai/gpt-5-6/) .

**GPT-5.6 Standard pricing for requests with ≤272K input tokens**

| Model | Short input | Cached input | Cache write | Short output | Long input | Long cached input | Long cache write | Long output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-5.6-sol | $5.00 | $0.50 | $6.25 | $30.00 | $10.00 | $1.00 | $12.50 | $45.00 |
| gpt-5.6-terra | $2.00 | $0.20 | $2.50 | $12.00 | $4.00 | $0.40 | $5.00 | $18.00 |
| gpt-5.6-luna | $0.20 | $0.02 | $0.25 | $1.20 | $0.40 | $0.04 | $0.50 | $1.80 |

*Source*\*:\* [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)

> **Long-context pricing:** Requests with more than **272K input tokens** use higher rates. Input, cached input, and cache writes are billed at **2×** the standard rate, while output is billed at **1.5×**. The higher rates apply to the entire request.

A reasonable starting point is to **test** Luna for simpler, high-volume tasks, Terra for balanced application workloads, and Sol for the most difficult or high-impact tasks. These are not universal recommendations: accuracy, retries, tool behavior, and human review can outweigh the difference in list price.

### One important alias detail

OpenAI's [model guidance](https://developers.openai.com/api/docs/guides/latest-model) states that the generic `gpt-5.6` alias routes to `gpt-5.6-sol`.

That means a request sent to `gpt-5.6` uses the Sol price tier. If your workload performs well on Terra or Luna, use the explicit model ID rather than assuming the generic alias selects the cheapest suitable tier.

## Example 1: A Typical API Request

Start with a common request shape:

- **1,000 input tokens**
- **500 output tokens**

| Model | Monthly input cost | Monthly output cost | Total |
| --- | --- | --- | --- |
| gpt-5.6-sol | $10,000 | $15,000 | $25,000 |
| gpt-5.6-terra | $4,000 | $6,000 | $10,000 |
| gpt-5.6-luna | $400 | $600 | $1,000 |

Under this workload, Luna’s new pricing reduces the estimated monthly token bill from $5,000 to $1,000, while Terra falls from $12,500 to $10,000.

Calculation for Sol:

(1,000 / 1,000,000 × $5) + (500 / 1,000,000 × $30) = $0.020

This example also shows why output length matters. Even though the request contains twice as many input tokens as output tokens, the output portion represents **75% of the Sol token cost** because output is priced at six times the input rate.

For chat, agents, and code generation, controlling unnecessary verbosity can sometimes save more than trimming a small system prompt.

## Example 2: Monthly Cost at Scale

Now assume an application handles **1 million requests per month**, averaging:

- 2,000 input tokens per request
- 500 output tokens per request

That equals 2 billion input tokens and 500 million output tokens per month.

| Model | Monthly input cost | Monthly output cost | Total |
| --- | --- | --- | --- |
| gpt-5.6-sol | $10,000 | $15,000 | $25,000 |
| gpt-5.6-terra | $5,000 | $7,500 | $12,500 |
| gpt-5.6-luna | $2,000 | $3,000 | $5,000 |

The gap is large enough to justify routing tests, but the lowest row is not automatically the best production choice. If a cheaper model causes more retries, failed tasks, or manual review, the total workflow cost may be higher.

## Long-Context Pricing: What Happens Above 272K Tokens?

GPT-5.6 models support a 1.05M-token context window, but OpenAI applies higher rates when a request contains **more than 272,000 input tokens**.

For these long-context requests:

- input is charged at **2×** the short-context rate
- cached input and cache writes are also charged at **2×**
- output is charged at **1.5×**
- The higher rates apply to **the full request**, not only the tokens above 272K

For Sol, that changes input from $5 to $10 per 1M tokens and output from $30 to $45. The same multiplier structure applies to Terra and Luna.

This creates a coastal cliff near 272K. For workloads close to the threshold, reduce duplicate retrieval chunks, stale conversation history, unnecessary repository files, or verbose tool output before sending the request. See OpenAI's [cost optimization guide](https://developers.openai.com/api/docs/guides/cost-optimization) for additional token-reduction guidance.

## Standard, Batch, Flex, and Priority Pricing

For eligible GPT-5.6 text workloads, OpenAI offers multiple processing tiers.

| Tier | Sol input/output | Terra input/output | Luna input/output | Typical use |
| --- | --- | --- | --- | --- |
| Standard | $5 / $30 | $2 / $12 | $0.20 / $1.20 | Normal synchronous traffic |
| Batch | $2.50 / $15 | $1 / $6 | $0.10 / $0.60 | Offline asynchronous jobs |
| Flex | $2.50 / $15 | $1 / $6 | $0.10 / $0.60 | Cost-sensitive workloads that can tolerate slower processing |
| Fast mode | $10 / $60 | $4 / $24 | $0.40 / $2.40 | Latency-sensitive short-context traffic |

Batch and Flex remain approximately 50% cheaper than Standard pricing. Priority Processing was renamed Fast mode on July 30, 2026, although existing requests using `service_tier: "priority"` remain compatible.

For GPT-5.6 Sol, Fast mode provides up to 2.5× faster processing than Standard at 2× the Standard token price, with no change in model intelligence. It is most appropriate when user-facing latency matters enough to justify the premium.

## Prompt Caching: When Does It Save Money for GPT-5.6 ?

For GPT-5.6, cache writes cost **1.25× the normal input rate**, while cached reads receive the lower cached-input price.

Consider a reusable **100,000-token prefix** on Sol:

| Action | Cost |
| --- | --- |
| Process once as normal uncached input | $0.50 |
| Write the prefix to cache | $0.63 |
| Read the cached prefix later | $0.05 |

Two uncached uses cost **$1.00**. One cache write plus one matching cached read costs **$0.675**, saving **$0.325** in this simplified example.

> **Boundary of this example:** This calculation compares only the reusable prefix's input cost. It does **not** include output tokens, other uncached input, tools, or retries. Real savings depend on whether the prefix matches the cache requirements and how often it is actually reused.

Caching is therefore most useful for long, stable prompt prefixes that receive repeated matching requests. A cache write that is never reused adds cost rather than reducing it.

OpenAI's [prompt caching guide](https://developers.openai.com/api/docs/guides/prompt-caching) documents cache-write pricing, cached reads, explicit breakpoints, and TTL behavior.

## Other Costs That Can Change Your OpenAI API Bill

### Reasoning tokens and Pro mode

Reasoning tokens are billed as output tokens even when they are not shown as visible response text. Higher reasoning settings can therefore increase total output-token usage and latency.

Where supported, `reasoning.mode = "pro"` is better treated as a configuration to **benchmark**, not a default cost-saving or quality rule. OpenAI does not list a separate fixed Pro surcharge for this mode; the cost impact comes from the resulting token usage. A reasonable baseline is to test Standard and Pro on representative tasks and compare task success, total output tokens, latency, and retries.

### Web search and other tools

OpenAI currently lists standard web search at **$10 per 1,000 calls**, plus search-content tokens billed at the selected model rate. Two web searches on a small Luna request can therefore cost more than the request's model tokens.

OpenAI also lists a separate **web search preview** price for non-reasoning models at **$25 per 1,000 calls**, with search-content tokens free. Check the exact tool and model combination on the [official pricing page](https://developers.openai.com/api/docs/pricing) rather than applying one web-search rate to every endpoint.

### Regional processing

Eligible regional processing or data-residency endpoints for models released on or after March 5, 2026 carry a **10% uplift** according to OpenAI's pricing page. Enterprise teams with residency requirements should include that factor in budget estimates.

## How to Calculate OpenAI API Cost

For a basic request:

Token cost =

(input tokens / 1M × input rate)

- (output tokens / 1M × output rate)

For production planning, expand it to include:

Total workflow cost =

uncached input

- cached input
- cache writes
- output and reasoning tokens
- tool fees
- service-tier adjustments
- regional uplift, if applicable
- retries and fallback requests

The most useful KPI is often:

Cost per successful task = total workflow cost / successful tasks

This prevents a cheaper token rate from looking artificially attractive when it also produces more failures or review work.

## How to Choose the Right Model Without Overpaying

Use the price table as a starting point, then test on real tasks.

1. **Start with the lowest-cost model that appears capable of the task.** Luna can be a sensible first test for simple, high-volume work, but do not assume it will be best for every extraction or summarization workload.
2. **Measure output length.** GPT-5.6 output tokens cost 6× input tokens, so verbose responses deserve attention.
3. **Watch the 272K threshold.** Crossing it changes rates for the full request.
4. **Use Batch or Flex for eligible non-urgent work.** Test operational constraints before moving production traffic.
5. **Cache only reusable prefixes.** Measure actual cache hits rather than assuming a long prompt should be cached.
6. **Track tools and retries.** They can erase savings from a cheaper model.

For teams comparing routes across providers, [CometAPI pricing](https://www.cometapi.com/pricing/) provides a live cross-model view. The [CometAPI Quickstart](https://www.cometapi.com/quickstart/) and [Cookbook](https://github.com/cometapi-dev/cometapi-cookbook) can be used to run the same test set across multiple OpenAI-compatible routes.

## FAQ

### How much does the GPT-5.6 cost in 2026?

Pricing depends on the model. GPT-5.6 Standard short-context rates range from **$1 input / $6 output per 1M tokens for Luna** to **$5 / $30 for Sol**. Lower-cost models such as GPT-5.4 mini and nano are also available. Check the exact model on OpenAI's live pricing page.

### Is ChatGPT API pricing the same as GPT-5.6 pricing?

“ChatGPT API pricing” is often used informally to mean OpenAI API pricing for chat-capable models, but ChatGPT subscriptions and API billing are separate products. API usage is priced by the specific model and usage type.

### Which GPT-5.6 model is cheapest?

`gpt-5.6-luna` is the cheapest GPT-5.6 model, priced at $0.20 per 1M input tokens and $1.20 per 1M output tokens. OpenAI reduced both rates by 80% on July 30, making Luna substantially more economical for high-volume agents, classification, document processing, and well-defined tool workflows.

### What model does `gpt-5.6` use?

OpenAI's model guidance states that the `gpt-5.6` alias routes to `gpt-5.6-sol`. Use explicit Terra or Luna model IDs when you want those tiers.

### When does GPT-5.6 long-context pricing apply?

When input exceeds **272,000 tokens**, GPT-5.6 uses higher long-context rates for the full request: 2× input-related rates and 1.5× output rates.

### Are Batch and Flex cheaper than Standard for GPT-5.6?

For eligible GPT-5.6 workloads, the listed Batch and Flex token rates are about 50% lower than Standard. They have different processing characteristics, so confirm that the workload can tolerate those constraints.

### Do cache writes cost extra for GPT-5.6?

Yes. GPT-5.6 cache writes are priced at 1.25× normal input, while matching cached reads use the discounted cached-input rate. Savings depend on actual reuse.

## Compare GPT-5.6 Costs on Your Own Workload

Pricing tables are a starting point. Your real cost depends on prompts, output length, cache hit rate, tools, retries, and task success.

With CometAPI, you can test GPT-5.6 Sol, Terra, Luna, and other models through one OpenAI-compatible API using the same workload.

**Next steps:** [compare current model pricing](https://www.cometapi.com/pricing/), follow the [CometAPI Quickstart](https://www.cometapi.com/quickstart/), or use the [CometAPI Cookbook](https://github.com/cometapi-dev/cometapi-cookbook) to build repeatable model evaluations.

Choose the lowest-cost route that still meets your quality, latency, and reliability requirements.

---

*Originally published at [https://www.cometapi.com/gpt-5-6-pricing/](https://www.cometapi.com/gpt-5-6-pricing/).*
