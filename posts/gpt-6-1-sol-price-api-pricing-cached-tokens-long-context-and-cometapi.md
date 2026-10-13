<!-- social-ops-fingerprint:96eb0c8f62467fed6df171bacec5c2a962ff5184ff3af7cd2459f3f7e619e78f -->
---
title: GPT-6.1 Sol Price: API Pricing, Cached Tokens, Long Context and CometAPI Cost
---
# GPT-6.1 Sol Price: API Pricing, Cached Tokens, Long Context and CometAPI Cost

![GPT-6.1 Sol Price: API Pricing, Cached Tokens, Long Context and CometAPI Cost](https://resource.cometapi.com/4d70-473c-b87a-39cfc6a8322f.png)

## TL;DR

[GPT-6.1 Sol](https://www.cometapi.com/models/openai/gpt-6-1-sol/) is OpenAI's reasoning model for complex coding, computer use, and professional workflows. It keeps GPT-6 Sol's official Standard fresh-input and output rates at $2/$10 per million tokens, while cutting short-context cache reads from $0.20 to $0.10. Successful cache reuse can lower repeated-context costs. Input above 272K tokens triggers higher rates for the full request, so estimate each request before aggregating a bill. CometAPI has a separate gateway schedule.

## Key Takeaways

- Separate fresh input, cache reads, cache writes, and billed output; output includes reasoning tokens.
- Use the correct context band for each request. A 1.05M context capacity does not imply short-context pricing.
- Compare OpenAI and CometAPI using the same token composition and the applicable account billing terms.
- Choose processing mode according to latency, availability, and route support.
- Judge agent economics by total cost per accepted task, including unsuccessful attempts.

## What Is the GPT-6.1 Sol Price at a Glance?

All token prices below are USD per million tokens. The [official token-price schedule](https://developers.openai.com/api/docs/pricing) provides the OpenAI baseline; cache reads and writes are separate billing categories. Context bands refer to input tokens in an individual request.

| OpenAI mode / input band | Fresh input | Cache read | Cache write | Output |
| --- | --- | --- | --- | --- |
| Standard: at most 272K | $2.00 | $0.10 | $2.50 | $10.00 |
| Standard: above 272K | $4.00 | $0.20 | $5.00 | $15.00 |
| Batch/Flex: at most 272K | $1.00 | $0.05 | $1.25 | $5.00 |
| Batch/Flex: above 272K | $2.00 | $0.10 | $2.50 | $7.50 |
| Fast: at most 272K | $4.00 | $0.20 | $5.00 | $20.00 |
| Fast: above 272K | $8.00 | $0.40 | $10.00 | $30.00 |
| Ultrafast: at most 272K | $12.00 | $0.60 | $15.00 | $60.00 |
| Ultrafast: above 272K | $24.00 | $1.20 | $30.00 | $90.00 |

OpenAI processing-tier rates checked October 9, 2026; the CometAPI comparison retains the source article's gateway schedule.These are OpenAI processing-tier rates, not a guarantee that each tier is exposed through a gateway. Regional processing adds 10% where applicable. Confirm the selected service and account terms before budgeting.

For developers who access GPT-6.1 Sol through CometAPI, the standard-context rate is lower than OpenAI's direct Standard price.

| Token category | CometAPI | OpenAI Standard | Difference |
| --- | --- | --- | --- |
| Input / 1M | $1.60 | $2.00 | 20% lower |
| Cached input / 1M | $0.08 | $0.10 | 20% lower |
| Cache write / 1M | $2.00 | $2.50 | 20% lower |
| Output / 1M | $8.00 | $10.00 | 20% lower |

For long-context requests, GPT-6.1 Sol API in CometAPI uses:

| Long-context tokens | CometAPI | OpenAI |
| --- | --- | --- |
| Input / 1M | $3.20 | $4.00 |
| Cached input / 1M | $0.16 | $0.20 |
| Cache write / 1M | $4.00 | $5.00 |
| Output / 1M | $12.00 | $15.00 |

That preserves an approximately 20% price difference across the main token categories. For budgeting, this matters because a production workload rarely consists only of fresh input tokens. Once cached context, output generation and long-context requests are included, comparing only the advertised input rate can significantly underestimate the difference between routes.

The [CometAPI token-price schedule](https://www.cometapi.com/models/openai/gpt-6-1-sol/) supplies the gateway reference. At 100K fresh input and 10K billed output, OpenAI Standard costs $0.30; the corresponding CometAPI schedule costs $0.24. At 10,000 identical requests, the token-only totals are $3,000 and $2,400. This comparison excludes tools, cache writes, retries, and premiums.

GPT-6.1 Sol is positioned for complex coding, computer use, and professional workflows. Its 1,050,000-token context window and 128,000-token maximum output are capacity limits, not a promise of short-context billing: requests above 272K input tokens use higher rates. It accepts text and images and produces text; use the Responses API for tool calling, while Chat Completions supports tool-free requests. Check gateway tool support and processing tiers separately when choosing a route.

### Additional GPT-6.1 Sol Agent Expenses

An agent budget also includes hosted tools, execution environments, storage, and external service charges. OpenAI lists web-search calls at $10 per 1,000 calls. Retrieved search content is billed at model-token rates. File-search calls are $2.50 per 1,000; storage is $0.10 per GB per day after the free 1 GB allowance.

Hosted Shell and Code Interpreter use separate container charges under the same OpenAI pricing schedule cited above. The published 1 GB rate is $0.03 per 20-minute session per container; eligible sessions use per-minute billing with a five-minute minimum. Use the selected gateway's actual tool and execution terms instead of assuming these direct-service charges apply unchanged.

### Reasoning Effort and Total GPT-6.1 Sol Spend

Reasoning effort is not a separate rate in the token table, but it can alter billed output, tool use, trajectory length, and retries. Compare supported efforts from low through max on the same task set. Record usage rather than estimating reasoning cost from visible answer length alone.

## How Does the 272K Threshold Change GPT-6.1 Sol Cost?

When input exceeds 272K tokens, OpenAI applies long-context rates to the full request: input and cache rates double, while output increases by 50%. The input threshold applies even when much of the input is served from cache.

| Workload | Fresh input | Billed output | OpenAI Standard | CometAPI catalog |
| --- | --- | --- | --- | --- |
| Small analysis | 20K | 2K | $0.06 | $0.048 |
| Document review | 100K | 10K | $0.30 | $0.24 |
| Below threshold | 270K | 10K | $0.64 | $0.512 |
| Above threshold | 280K | 10K | $1.27 | $1.016 |
| Repository analysis | 300K | 20K | $1.50 | $1.20 |

```
270K input: 0.27 x $2 + 0.01 x $10 = $0.64
280K input: 0.28 x $4 + 0.01 x $15 = $1.27
Input grows about 3.7%; token cost grows about 98.4%.
```

These are independent requests with no cache, tool, retry, or premium charges. The threshold effect is why context selection matters even when the model has enough capacity for the entire repository.

## How Does Prompt Caching Change GPT-6.1 Sol Input Costs?

Short-context Standard cache reads cost $0.10/M versus $2/M fresh input. A successful read is therefore 95% cheaper for that token category. A cache write costs $2.50/M. Savings depend on [successful reuse of the cached prefix](https://developers.openai.com/api/docs/guides/prompt-caching), not simply repeating similar text.

Consider ten requests sharing one 100K-token prefix. Each stays in the short-context band. The controlled cached case writes the entire prefix once and reads it successfully nine times, with no additional writes.The first request's 100K-token prefix is billed at the cache-write rate only; those same tokens are not also charged at the fresh-input rate.

| Repeated-prefix cost | No cache | One write + nine reads |
| --- | --- | --- |
| Fresh prefix input | 10 x 0.1 x $2 = $2.00 | $0.00 |
| Cache write | $0.00 | 0.1 x $2.50 = $0.25 |
| Cache reads | $0.00 | 9 x 0.1 x $0.10 = $0.09 |
| Prefix subtotal | $2.00 | $0.34 |

The $1.66 reduction is 83% of this repeated-prefix cost. It is not an 83% reduction in a typical total API bill. If each request also generates 2K billed output tokens, output adds $0.20 across the ten requests: totals become $2.20 and $0.54, a reduction of about 75.5%. New input, misses, extra writes, tools, and long-context bands change the result.

Under these simplified short-context assumptions, write once plus N-1 reads costs 0.25 + 0.01(N-1) dollars for a 100K prefix, compared with 0.20N without caching. Two requests are enough to make the modeled cached case cheaper, provided the second request actually hits and no other costs change.

## How Does GPT-6.1 Sol Pricing Compare with GPT-6 Sol and GPT-6 Astra?

OpenAI documents [GPT-6 Sol specifications](https://developers.openai.com/api/docs/models/gpt-6-sol). The cache-read reduction is a rate comparison, not proof of lower total task cost.

| Official Standard short-context comparison | GPT-6.1 Sol | GPT-6 Sol | GPT-6 Astra |
| --- | --- | --- | --- |
| Fresh input / 1M tokens | $2.00 | $2.00 | $10.00 |
| Cache read / 1M tokens | $0.10 | $0.20 | $1.00 |
| Cache write / 1M tokens | $2.50 | $2.50 | $12.50 |
| Output / 1M tokens | $10.00 | $10.00 | $50.00 |
| Context window / maximum output | 1.05M / 128K | 1.05M / 128K | 1.05M / 128K |

GPT-6.1 Sol halves the short-context cache-read rate. Fresh input, writes, and output are unchanged. The maximum benefit depends on how much of your bill consists of successful cache reads. Re-test effort settings, tool loops, and task outcomes when migrating.

Compared with GPT-6 Sol, GPT-6.1 Sol keeps the same fresh-input, cache-write, and output rates while cutting cache-read rates by 50%. Compared with GPT-6 Astra, use the rates above together with measured task quality and total trajectory cost.

The [GPT-6 Astra rate schedule](https://developers.openai.com/api/docs/models/gpt-6-astra) places Astra in a higher token-price tier.

GPT-6.1 Sol is 80% cheaper for fresh input, cache writes, and output, and 90% cheaper for cache reads in this band. These ratios do not establish equivalent quality. Astra can be worth its premium if better accepted results offset additional spending; GPT-6.1 Sol can be preferable when it meets the same acceptance target at lower cost.

Compare repository patches, document analysis, and computer-use tasks separately. Hold prompts, tool permissions, effort settings, retry limits, and acceptance checks constant. Record unresolved failures as well as successful results; do not infer a universal coding or research ranking from token prices.

## What Does GPT-6.1 Sol Cost for Real API Workloads?

Compute cost per request with its actual band and processing mode, then sum the results. Fresh input excludes cached reads; do not charge the same input tokens as both fresh and cached. Use provider usage records to distinguish writes from other input.In the formula below, fresh\_input excludes both cache\_reads and cache\_writes. Tokens charged at the cache-write rate must not also be counted as fresh input. Treat all three quantities as mutually exclusive billing categories and reconcile them with the provider's usage records.

```
request_token_cost =
  fresh_input / 1_000_000 * fresh_rate
+ cache_reads / 1_000_000 * read_rate
+ cache_writes / 1_000_000 * write_rate
+ billed_output / 1_000_000 * output_rate

period_total = sum(request_token_cost) + other_charges
```

### Aggregate Usage Across Multiple Short Requests

Ten requests each using 100K fresh input and 20K billed output aggregate to 1M input and 200K output. Every individual request remains below 272K input and below the 128K output limit. OpenAI Standard totals $4.00; CometAPI totals $3.20. The 20% difference applies to these modeled token categories only. This is not one request with 1M input and 200K output.

### A Cache-Heavy Period With Separately Billed Writes

Suppose a period records 1M fresh input, 5M cache reads, 500K billed output, and 500K cache writes. All component requests remain in the short-context Standard band. OpenAI costs $2.00 + $0.50 + $5.00 + $1.25 = $8.75. CometAPI costs $1.60 + $0.40 + $4.00 + $1.00 = $7.00. These categories are distinct billing quantities; the example does not assume all repeated input is a cache hit.

### One Long-Context Request

A request with 400K fresh input and 100K billed output uses long-context rates. OpenAI Standard costs 0.4 x $4 + 0.1 x $15 = $3.10. CometAPI costs 0.4 x $3.20 + 0.1 x $12 = $2.48. Both exclude new cache writes and non-token charges. The 100K output quantity includes reasoning and must fit the model's output budget.

## How Do Standard, Batch, Flex, Fast, and Ultrafast Change GPT-6.1 Sol Cost?

For a 300K fresh-input, 20K billed-output request, use the long-context band.

| OpenAI mode | Input cost | Output cost | Token subtotal |
| --- | --- | --- | --- |
| Batch/Flex | $0.60 | $0.15 | $0.75 |
| Standard | $1.20 | $0.30 | $1.50 |
| Fast | $2.40 | $0.60 | $3.00 |
| Ultrafast | $7.20 | $1.80 | $9.00 |

Ultrafast calculation: 0.30M fresh input x $24/M + 0.02M billed output x $90/M = $7.20 + $1.80 = $9.00. This uses the long-context band and excludes cache, tool, and regional charges.

Batch suits offline evaluations, enrichment, backfills, and bulk document processing. Flex offers lower rates for eligible workloads that tolerate variable processing and availability. Standard is the baseline for interactive requests. Fast doubles applicable token rates; select it when reduced waiting has measurable value.

[Ultrafast](https://developers.openai.com/api/docs/guides/ultrafast-mode) prioritizes latency at a higher token price. For GPT-6.1 Sol, set service\_tier to ultrafast in Responses requests. OpenAI recommends WebSockets for rapid agent tool loops; check tier-specific limits and gateway support before routing production traffic. Rates come from the [official OpenAI pricing table](https://developers.openai.com/api/docs/pricing).

These rates do not prove that every tier is enabled for your gateway account. Verify supported routing and regional constraints before rollout. Do not budget an unpriced or unavailable processing option as though it already has the Standard rate.

## Why Is Cost per Successful GPT-6.1 Sol Task the Better Metric?

Divide total measured model, tool, and execution spending across an evaluation set by accepted results. Include failed attempts in the numerator. Report human correction time and unresolved failures separately so cost cannot improve merely by abandoning harder tasks.

```
observed_cost_per_accepted_task =
  all_evaluation_model_tool_execution_cost / accepted_tasks
```

For illustration, a $0.40 attempt with a 60% success probability has expected cost $0.40 / 0.60 = about $0.67 until success. A $0.55 attempt with an 85% probability costs about $0.65 under the same model. These are hypothetical figures, not benchmark results or claims about a particular model.

That estimate assumes independent retries with unchanged cost and success probability, continuing until success. Do not add a second retry allowance: the division already accounts for repeats. Correlated failures, capped retries, different task difficulty, tools, and human intervention can make this model unsuitable. Use observed accepted-task cost for production decisions.

## How Can You Reduce GPT-6.1 Sol API Costs?

**Maximize reusable prompt prefixes.** Put stable system instructions, tool definitions, schemas and background context into reusable prefixes. GPT-6.1 Sol's $0.10/M cached input price makes repeated context inexpensive relative to fresh input.

**Keep requests below 272K when full context is unnecessary.** Crossing 272K input tokens changes pricing for the full request. Retrieval, context compression and selective file loading can therefore reduce cost even when the model technically supports a 1.05M context window.

**Use Batch for bulk asynchronous workflows.** Offline evaluations, enrichment, backfills, and bulk document processing can use Batch when results do not need to return immediately.

**Use Flex for low-priority requests that tolerate slower responses and occasional resource unavailability.** Plan for delays and retries; check eligible workloads and route support. Batch and Flex each use the lower rates shown above, but they serve different processing needs.

**Measure accepted-task cost.** Log fresh input tokens, cached input tokens, cache writes, output tokens, processing mode, tool charges, retries and task success. Then calculate the real cost per successful completion.

**Route simpler tasks to cheaper models.** Not every request requires Sol-level reasoning. Classification, routing, simple extraction and other highly verifiable tasks may fit a lower-cost model, while GPT-6.1 Sol handles the tasks where stronger reasoning materially improves completion rate.

This is especially important for agents because a failed $0.50 run followed by two retries can be more expensive than a single $1.00 successful run.

Use explicit completion limits, tool-loop limits, and retry budgets. Review usage records for fresh input, cache reads, writes, reasoning output, tier, context band, and tool charges. Compare savings against accepted-task quality after each change.

## Conclusion

GPT-6.1 Sol is attractive when a workflow needs complex reasoning at Sol-tier prices and can reuse stable context. It keeps GPT-6 Sol's $2/$10 headline Standard rates while lowering short-context cache reads to $0.10/M. Astra has higher token rates, but the choice should follow workload quality and accepted-task cost.

Start with per-request estimates, separate cache writes from reads, and watch the 272K boundary. Then measure the full agent trajectory and choose a processing tier that fits latency and availability. CometAPI provides a separate price schedule; confirm actual account and tool terms before scaling.

## FAQ

### How Should GPT-6.1 Sol Budgets Handle Failed or Cancelled Requests?

Track provider usage for completed, incomplete, failed, and cancelled requests separately. Do not assume every unsuccessful request is free or every client cancellation prevents server-side work. Reconcile request identifiers and usage with the billing records, then include billed unsuccessful work in the accepted-task calculation. Confirm provider-specific charging and refund rules instead of inferring them from an HTTP status.

### How Should Teams Forecast GPT-6.1 Sol Costs for Variable Traffic?

Segment traffic by input band, processing tier, cache composition, and workload. Use measured token and completion distributions rather than one average prompt. Build a baseline forecast and scenarios for lower hit rates, more retries, and longer outputs; also monitor the share crossing 272K. Update the forecast as task mix changes.

### How Can Teams Reconcile GPT-6.1 Sol Forecasts With Invoices?

Choose a completed billing period and group requests by route, processing tier, and input band. Reconcile recorded usage with invoice categories and credits, including adjustments, tool charges, and any applicable tax or currency conversion. Investigate discrepancies using request identifiers and billing timestamps rather than applying an unexplained correction factor. Confirm delayed reporting and provider rounding rules before changing the forecast.

---

*Originally published at [https://www.cometapi.com/gpt-6-1-sol-price/](https://www.cometapi.com/gpt-6-1-sol-price/).*
