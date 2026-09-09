<!-- social-ops-fingerprint:e9c8fb317bbdd137cfed6865b6c0e1eb75a861549ed63f9d1d8a3857200df7bd -->
---
title: Cached Input Pricing of GPT 5.6 and Gemini 3.6 Falsh: What It Costs
---
# Cached Input Pricing of GPT 5.6 and Gemini 3.6 Falsh: What It Costs

![Cached Input Pricing of GPT 5.6 and Gemini 3.6 Falsh: What It Costs](https://resource.cometapi.com/Cached%20Input%20Pricing%20of%20GPT%205.6%20and%20Gemini%203.6%20Falsh.webp)

## DR

Cached input pricing can materially reduce the cost of workloads that resend a large, unchanged prompt prefix, but the savings depend on model-specific cache-read, cache-write, storage, routing, and retention rules. A general “caching supported” label is not enough to estimate cost; use the current price published for the exact model and route.

## TL;DR

- GPT-5.6 Terra has explicit cache-read and cache-write prices from OpenAI, CometAPI, and OpenRouter, although gateway routes and long-context tiers can change the amount.
- Google publishes a $0.15 per 1M-token Standard context-caching rate for Gemini 3.6 Flash plus a storage charge; CometAPI currently publishes the model’s standard input and output prices without a separate cached-input line.
- The relevant comparison is not just standard input versus cache read. It also includes the first cache write, any storage charge, cache lifetime, route consistency, and the number of later cache hits.

## Key messages

- Check prices at the model and service-tier level rather than applying a gateway-wide multiplier.
- Keep cache read, cache write, storage, and response caching separate in cost calculations.
- Verify actual cache usage in API response metadata before forecasting savings from the published rate.

A request that repeats a large, unchanged prefix — a system prompt, a set of tool schemas, a long reference document — doesn't have to be billed at the full input rate on every call. Most current-generation models support some form of cached-input pricing: a reduced rate for the portion of a prompt a provider recognizes as already processed. The mechanism, the discount size, and how clearly it's published all vary by provider and by gateway, and that variation is worth being specific about rather than treating "caching is supported" as one uniform feature.

## What cached input pricing is, and isn't

Cached input pricing discounts the *input* tokens in a request that match a previously sent prefix. It doesn't discount output tokens, and it isn't the same thing as a gateway deduplicating two fully identical requests and returning one response for free — that's a different mechanism some gateways offer separately. Cached input pricing is specifically about paying less for the part of a prompt a model provider has already seen recently, not about skipping generation entirely.

It is also not free to create. [OpenAI’s GPT-5.6 pricing notes](https://openai.com/index/gpt-5-6/) state that cache writes are billed at 1.25 times the uncached input rate, while cache reads receive a 90% discount. That first-write premium affects the break-even point and is easy to miss if a comparison shows only the discounted read rate. Other providers may use storage-based charges instead of the same write model, so write and storage costs should be checked separately.

In practice, the billable cache unit is usually a reusable prompt prefix rather than an arbitrary collection of repeated sentences. Providers tokenize and match content in order, so the reusable material needs to appear before the request-specific tail. Stable system instructions, tool definitions, policies, and reference material belong near the beginning; a changing user message, timestamp, request ID, or retrieved snippet belongs later. Even a semantically harmless change near the front can shift tokenization or break the match for everything that follows.

Eligibility rules are also model specific. A provider may require a minimum prompt length, recognize only documented breakpoints, or expose an explicit cache-control field. A cache entry can expire between calls, and a gateway may need to keep related requests on a compatible upstream route. That means a deployment should treat a cache hit as an observed outcome, not as an assumption made from prompt similarity. A well-structured prompt improves the probability of reuse, but the response metadata and invoice determine whether the discounted rate was actually applied.

## What's actually published, by model and by gateway

The table below is a pricing snapshot checked on July 29, 2026. Prices are in US dollars per 1 million tokens unless another unit is stated. The rows compare current public information for GPT-5.6 Terra and Gemini 3.6 Flash across the model provider, CometAPI, and OpenRouter; they should not be treated as a permanent tariff.

| Model | Gateway | Standard input | Cached input (read) | Cache write | Discount disclosed? |
| --- | --- | --- | --- | --- | --- |
| GPT-5.6 Terra | Official OpenAI rate | $2.50 / 1M | $0.25 / 1M | $3.13 / 1M | Yes — 90% off, stated directly |
| GPT-5.6 Terra | CometAPI | $2.00 / 1M | $0.20 / 1M | $2.50 / 1M | Yes — listed on CometAPI's own pricing page |
| GPT-5.6 Terra | OpenRouter | $2.50 / 1M | Not listed as a specific rate | Not listed | No — described only as "60–80% cheaper" in aggregate, no per-model figure |
| Gemini 3.6 Flash | Official Google rate | $1.50 / 1M | $0.15 / 1M (per Google's own announcement) | Not disclosed | Yes, at launch — via Google's model documentation |
| Gemini 3.6 Flash | CometAPI | $1.20 / 1M | Not listed as a specific rate | Not disclosed | No — CometAPI's page marks "Caching" as a supported feature but doesn't publish a discounted cached figure for this specific model as of this writing |
| Gemini 3.6 Flash | OpenRouter | $1.50 / 1M | Not listed as a specific rate | Not disclosed | No — OpenRouter's own documentation describes Google's cache multiplier generically (0.25x list input) rather than confirming this model's specific rate |

Read the table as a model- and route-specific snapshot. The [CometAPI GPT-5.6 model page](https://www.cometapi.com/models/openai/gpt-5-6/) itemizes GPT-5.6 Terra at $2.00 standard input, $0.20 cached input, and $2.50 cache write per 1 million tokens. Its [Gemini 3.6 Flash model page](https://www.cometapi.com/models/google/gemini-3-6-flash/) currently publishes $1.20 input and $6.00 output, but it does not show a separate cached-input or cache-storage price. Google’s [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) lists the Standard tier at $1.50 input, $0.15 context caching, and $1.00 per 1 million tokens per hour for storage. OpenRouter now exposes model-specific cache fields through its [Models API](https://openrouter.ai/api/v1/model/openai/gpt-5.6-terra): GPT-5.6 Terra’s default route includes lower promotional pricing and a separate higher long-context tier, while its [Gemini 3.6 Flash entry](https://openrouter.ai/api/v1/model/google/gemini-3.6-flash) exposes different Standard, Flex, and Priority values. This is more precise than applying one generic cache multiplier to every model.

## Why gateway and provider prices can diverge

A gateway price is not necessarily a markup on one immutable upstream list price. It may reflect negotiated capacity, a temporary promotion, a different service tier, or a route-specific commercial arrangement. A model name can also map to multiple upstream variants whose prices change with context length or latency guarantees. OpenRouter’s GPT-5.6 Terra entry, for example, publishes a default route and a higher-priced override once the input reaches its long-context threshold. Google separates Standard, Batch, Flex, and Priority pricing for Gemini 3.6 Flash. A single comparison row therefore needs a date, route, tier, and context assumption to remain meaningful.

The inverse is also important: if a gateway page does not publish a separate cache-read line, that absence should not be converted into either “caching is unavailable” or “the provider’s direct discount automatically applies.” The gateway may pass through an upstream feature without itemizing it, expose it only on certain routes, or bill the request under its normal input rate. The defensible approach is to use the gateway’s own current model page for planning, then confirm the actual rate from usage records or billing data. Provider documentation remains useful for understanding the mechanism, but it does not by itself establish the commercial terms of an intermediary.

## Where the discount actually matters

The scenario where this changes real cost meaningfully is a large, static prefix paired with a small, variable request — a system prompt or tool schema set resent on every call in an agent loop, a long reference document queried repeatedly with different questions, or conversation history resent on every chatbot turn. For a workload like that, the gap between paying full input price on the entire prefix every time versus paying the write premium once and the discounted read rate afterward compounds with call volume. It does nothing for workloads that don't repeat a prefix — a one-off request has no cached content to discount in the first place.

A practical break-even calculation compares the uncached cost of the repeated prefix across all calls with the cache write or storage cost plus discounted cache reads on later calls. The result depends on prefix size, the number of successful cache hits, cache expiration, and whether the gateway keeps requests on a compatible provider route. If those conditions are unstable, the headline discount can overstate the savings realized in production.

## A simple cost model for a repeated prefix

Let `P` be the number of tokens in the stable prefix and `N` the number of calls that reuse it. If `U` is the uncached input price per token, the prefix costs `N × P × U` without caching. A simplified cached estimate is `P × W + (N − 1) × P × R + S`, where `W` is the cache-write price, `R` is the cache-read price, and `S` is any storage charge over the period. The formula assumes the first call creates the cache and every later call is a successful hit. It excludes the variable tail of each request, output tokens, retries, and any route change that causes a miss.

Consider an illustrative 100,000-token prefix reused for 20 calls on the official GPT-5.6 Terra rate. At $2.50 per 1 million uncached input tokens, repeatedly processing that prefix would cost $5.00. Using the published 1.25-times write rate and 90%-discounted read rate, one 100,000-token write would cost about $0.3125 and nineteen reads would cost about $0.475, for a combined prefix cost of roughly $0.7875. The difference is about $4.21 before variable input and output costs. This is an illustration, not a quote: it holds only if all nineteen later calls hit the same valid cache and no additional storage or routing charge applies.

The break-even point follows directly from the same model. A write premium is justified only when enough discounted reads occur before expiration. For a workload with short sessions, frequent prompt edits, or weak route affinity, the cache may be recreated more often than expected. For a long-lived agent loop or repeated document analysis with a stable prefix, the number of hits can be much higher. Forecasts should therefore use an observed hit-rate range rather than assuming a perfect sequence after the first call.

## Implementation patterns that improve cache reuse

Prompt construction has a larger effect on hit rate than many pricing spreadsheets imply. Put the most stable material first and keep its serialization deterministic: system instructions, tool schemas, policy text, and shared reference context should retain the same order, whitespace, and field representation across related calls. Append volatile content afterward. Avoid injecting timestamps, random identifiers, continuously changing counters, or request-specific retrieval results into the reusable prefix unless they are genuinely required there.

Version stable material deliberately. If a tool schema or policy changes, assign the new version consistently instead of allowing multiple nearly identical variants to circulate. For conversational or agentic workloads, reuse a stable session identifier or cache key when the API supports one, and avoid switching providers within the same cache-dependent sequence. OpenRouter documents provider-sticky routing for prompt caching and exposes controls such as `session_id` and `prompt_cache_key`; those controls can improve continuity, but they do not guarantee a hit when the upstream cache is cold or expired.

Applications should also degrade cleanly on a miss. Caching is a cost and latency optimization, not a correctness dependency. The request must still produce the same valid result when the cache is unavailable, and retry logic should not blindly create repeated writes. That separation makes it safer to compare routes: teams can change caching policy or gateway configuration without changing the application’s semantic behavior.

## How to verify cache economics in production

Start with per-request telemetry rather than the monthly invoice. Log the exact model identifier, gateway route or provider when exposed, service tier, total input tokens, cached-read tokens, cache-write tokens, output tokens, latency, and billed cost. OpenRouter’s usage object includes `cached_tokens` and `cache_write_tokens`; other providers expose equivalent details under different field names. Preserve raw usage fields so a later pricing change does not erase the evidence needed to reconstruct cost.

Aggregate the data by prompt version and workload, not only by model. Useful measures include the share of eligible requests that hit a cache, the share of input tokens billed at the read rate, writes per successful read, time between write and last hit, and realized cost per request. A high request-level hit rate can still deliver little value if the cached prefix is small, while a lower hit rate on a very large prefix may save more. Pair those measures with latency percentiles, because a cheaper route that repeatedly misses or reroutes may be operationally worse.

Finally, review anomalies instead of smoothing them away. A sudden drop in cached tokens may indicate a prompt-version rollout, unstable serialization, expired entries, a long-context tier boundary, or a gateway route change. Compare the affected requests with the current model page and provider documentation, then verify the billed rate. This closes the gap between a published discount and the savings the application actually realizes.

## What to check before assuming a rate applies

Confirm five items before using a published rate in a budget: the exact model and service tier, the minimum reusable prefix or explicit cache breakpoints, the first-write or storage charge, the cache lifetime, and evidence that requests are actually hitting the cache. OpenAI currently states a 30-minute minimum cache life for GPT-5.6, but that is not a universal retention rule. Google publishes different rates for Standard, Batch, Flex, and Priority service tiers. Gateways can also route among providers or tiers, so the selected route matters. OpenRouter’s [prompt-caching documentation](https://openrouter.ai/docs/guides/best-practices/prompt-caching) recommends checking response usage fields such as `cached_tokens` and `cache_write_tokens`. For any production estimate, compare the current model page with actual billing and usage metadata rather than relying only on a general “caching supported” label.

---

*Originally published at [https://www.cometapi.com/cached-input-pricing-of-gpt-5-6-and-gemini-3-6-falsh-what-it-costs/](https://www.cometapi.com/cached-input-pricing-of-gpt-5-6-and-gemini-3-6-falsh-what-it-costs/).*
