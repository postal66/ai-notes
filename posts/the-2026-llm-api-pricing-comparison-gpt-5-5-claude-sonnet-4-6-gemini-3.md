<!-- social-ops-fingerprint:f5e2b7343ad41efda82806250a39fd8b25877115f531e6f9ee5cd6de61c9ae55 -->
---
title: The 2026 LLM API Pricing Comparison: GPT-5.5, Claude Sonnet 4.6, Gemini 3.5 Flash and DeepSeek V4
---
# The 2026 LLM API Pricing Comparison: GPT-5.5, Claude Sonnet 4.6, Gemini 3.5 Flash and DeepSeek V4

![The 2026 LLM API Pricing Comparison: GPT-5.5, Claude Sonnet 4.6, Gemini 3.5 Flash and DeepSeek V4](https://resource.cometapi.com/image-1779333673645.jpeg)

Pricing is the single most consequential decision in choosing a frontier LLM, and it is also the dimension where most published comparisons are out of date within a quarter. This article cuts through that. Below is a current, sourced view of input and output token pricing across the four models that account for the majority of production frontier-model traffic in 2026 (OpenAI’s GPT-5.5, Anthropic’s Claude Sonnet 4.6, Google’s Gemini 3.5 Flash, and DeepSeek’s V4), together with the levers that meaningfully change your bill at scale: prompt caching, batch processing, and long-context surcharges.

The piece is built around two questions. First: at list price, what does each model cost per million tokens, and how do the quoted rates compare on the inputs and outputs that actually drive a production bill? Second: when you apply a representative workload (100 million tokens a month, 80% input and 20% output, with realistic cache hit rates), what is the monthly bill in dollars on each model? The first answer establishes the rate card; the second tells you what that rate card becomes once it touches a real production pattern.

> **Quick read:** Across the four frontier models, list pricing spans roughly two orders of magnitude. DeepSeek V4 is the cheapest at $0.435 per million input tokens; Claude Opus 4.7 is the most expensive at $5.00. The shape of your workload, particularly your cache hit rate and your input-to-output ratio, changes which model is cheapest in practice, often by more than the rate card suggests.

## Why a like-for-like pricing comparison is harder than it looks

Provider pricing pages are written for that provider's own customers, not for someone evaluating four options side by side. The result is that comparing them produces three persistent traps:

- **Tokens are not the same across providers.** Claude Opus 4.7 ships with a new tokenizer that can produce up to 35% more tokens for the same input text than Opus 4.6. Gemini's tokenizer differs from OpenAI's. The rate card is per million tokens, but the token count for the identical prompt varies between providers, meaning the headline rate is only a first approximation of relative cost.
- **Long-context pricing tiers create cost cliffs.** OpenAI's GPT-5.5 family has separate short-context and long-context rates that kick in around 270,000 tokens. Anthropic, conversely, holds the same per-token rate across its full 1M context window. Workloads that sit near these thresholds are priced very differently to workloads that sit comfortably inside them.
- **Discounts are stacked, not separate.** Prompt caching, batch processing, and provider-specific volume tiers can each cut effective cost dramatically, and they stack. A cached batch request on Anthropic can cost as little as 5% of a standard non-cached request. A pricing comparison that ignores these levers overstates list cost, sometimes by an order of magnitude.

The comparison below normalises for these traps where it can, and flags them explicitly where it cannot.

## The 2026 frontier LLM pricing comparison

All figures in US dollars per million tokens. Sourced from each provider's official pricing documentation as of May 2026.

| Model | Input | Output | Cached input | Batch (50% off) | Context window | Long-context surcharge |
| --- | --- | --- | --- | --- | --- | --- |
| GPT-5.5 | $5.00 | $30.00 | $0.50 | $2.50 / $15.00 | 1M | Yes (~270K) |
| Claude Sonnet 4.6 | $3.00 | $15.00 | $0.30 | $1.50 / $7.50 | 1M | None |
| Claude Opus 4.7 | $5.00 | $25.00 | $0.50 | $2.50 / $12.50 | 1M | None |
| Gemini 3.5 Flash | $1.50 | $9.00 | $0.15 | $1.00 / $6.00 | 1M | Yes (200K) |
| DeepSeek V4 | $0.435 | $0.87 | $0.0028 | Not offered | 384K | None |

*Reading the table:* Cached input is the rate paid on tokens served from prompt cache (typically system prompts, few-shot examples, or document prefixes that recur across requests). Batch is the rate paid for asynchronous workloads with up to 24-hour latency. Long-context surcharge denotes whether the provider raises rates above a context-length threshold; for those that do, the threshold is given in parentheses.

## Where each model wins

### GPT-5.5: the highest-capability default for hard reasoning and agentic work

GPT-5.5 is OpenAI's frontier model for complex professional workloads: coding agents, multi-step planning, long-running tool use, and document analysis where reasoning depth is the dominant requirement. It is also the most expensive of the major US frontier models on input ($5.00 per million) and the highest on output ($30.00 per million), which means it earns its position on workloads where the alternative is paying a flagship rate to a different model that solves the problem less reliably. GPT-5.5 supports caching at a 90% discount, batch processing at 50% off, and long-context pricing kicks in around the 270K-token mark, which is relevant for very long codebases or full-repository contexts but not for typical RAG workloads.

### Claude Sonnet 4.6: the recommended default for most production traffic

Sonnet 4.6 is Anthropic's recommended model for the majority of production workloads, and the price-to-capability ratio is the reason. At $3 input and $15 output per million tokens, it sits below GPT-5.5 on both rates while delivering near-Opus quality on the workloads that dominate most production systems: coding, analysis, RAG pipelines, customer-facing chat, and structured output generation. Sonnet's distinguishing pricing feature is that the full 1M token context window is available at standard rates (there is no long-context surcharge), which makes it the cheapest credible option for workloads that occasionally need to ingest very long documents or full repositories. Prompt caching cuts cached input to 10% of standard, which is decisive for any workload with a stable system prompt.

### Gemini 3.5 Flash: the most aggressively-priced flagship for short-context work

Gemini 3.5 Flash is the cheapest flagship-class model from a major US provider on raw API pricing, at $1.50 input and $9.00 output per million tokens. For most production traffic, that is the relevant pricing tier, and it materially undercuts both GPT-5.5 and Claude Opus 4.7. Higher price than prior Flash models leads to increased overall costs in token-heavy agentic scenarios (5.5x Intelligence Index cost vs. Gemini 3 Flash due to pricing + usage).. Gemini's other distinguishing feature is the genuinely free tier in Google AI Studio, which is useful for prototyping but not relevant to production cost models.

### DeepSeek V4: dramatically cheaper, with caveats worth understanding

DeepSeek V4 lists at $0.435 per million input tokens and $0.87 per million output tokens, which is between five and seventy times cheaper than the US frontier models depending on which one you compare against. The model itself is competitive on many benchmarks, particularly reasoning and code. The caveats are worth being explicit about: data is processed in China, which is a non-starter for some regulated workloads; English-language quality is strong but the model is optimised differently to the US frontier models, and head-to-head testing on your specific workload is essential rather than optional. For workloads where these caveats are acceptable, DeepSeek genuinely changes the cost equation.

> **A note on Claude Opus 4.7 vs Sonnet 4.6.** Opus is included in the table for completeness, but for the great majority of production traffic, Sonnet 4.6 is the better economic choice. Opus costs 1.67x Sonnet on both input and output, and for workloads where Sonnet is sufficient (which is most of them), that premium has no offsetting benefit. Reach for Opus when evaluations show Sonnet is failing on a specific class of task: highly autonomous coding agents, long-horizon professional workflows, and tasks where instruction-following at the margin is decisive.

## Worked example: what 100 million tokens a month actually costs

Headline pricing per million tokens means little until it touches a representative workload. The example below uses a profile that approximates a non-trivial production system: 100 million total tokens per month, split 80% input (80M) and 20% output (20M), with a 30% cache hit rate on the input portion. This pattern is broadly representative of a customer-facing chat or RAG workload with a stable system prompt and document context.

The math for each model: cached input cost + uncached input cost + output cost. Cached input is billed at 10% of standard for the providers that offer caching.

| Model | Cached input (24M) | Uncached input (56M) | Output (20M) | Total monthly bill |
| --- | --- | --- | --- | --- |
| GPT-5.5 | $12.00 | $280.00 | $600.00 | $892.00 |
| Claude Sonnet 4.6 | $7.20 | $168.00 | $300.00 | $475.20 |
| Claude Opus 4.7 | $12.00 | $280.00 | $500.00 | $792.00 |

*What this tells you.* On a representative workload,Sonnet 4.6 in turn is roughly half the cost of GPT-5.5. DeepSeek is in a different cost universe entirely. These are list-price numbers; applying batch processing where eligible cuts each total by a further 50% on the inputs and outputs (though not the cache hits).

Two observations worth carrying forward. First: caching is the single most impactful lever you control. The example above assumes a 30% cache hit rate; raise it to 60% (entirely achievable for workloads with a stable system prompt), and total cost drops by roughly another 25%. Second: the input-to-output ratio matters a lot. Workloads that are output-heavy (summarisation, long-form writing) bias toward providers with cheaper output rates, while input-heavy workloads (long-context analysis, large RAG retrievals) bias toward providers with cheaper input rates and no long-context surcharge.

## The hidden costs not on the pricing page

List pricing is the floor, not the ceiling. Five additional costs are worth budgeting for explicitly, because they routinely surprise teams scaling from prototype to production:

1. **Reasoning tokens.** Models with extended reasoning modes (GPT-5.5 Thinking, DeepSeek V4 thinking mode) generate internal reasoning content that counts as output tokens. A single high-effort reasoning call on a long prompt can run 20,000 reasoning tokens, which is $0.60 of output cost on GPT-5.5 before the visible response is produced. Budget per workload, not per request.
2. **Long-context surcharges.** Both Gemini 3.5 Flash and GPT-5.5 raise rates above a context-length threshold. RAG pipelines that include large documents can silently push every request into the higher bracket without anyone noticing until the bill arrives. Measure your actual prompt lengths in production and check whether you are crossing the threshold.
3. **Data residency multipliers.** Anthropic charges a 10% premium for US-only inference on Opus 4.7 and Sonnet 4.6. OpenAI applies a 10% uplift on data residency endpoints for the GPT-5.4 family. For regulated workloads where this matters, factor it into the rate card from day one.
4. **Output verbosity drift.** When a new model version is more thorough by default (as Opus 4.7 reportedly is compared to Opus 4.6), output tokens per response can creep up even if input length is constant. Output is priced 5x higher than input on the Anthropic line, so a 20% creep in output verbosity is a 20% increase in the dominant cost driver.
5. **Failed and retried requests.** Most providers do not bill for 4xx and 5xx errors, but they do bill for partial generations and retries that succeed on the second attempt. In production systems with active retry logic, this can add a few percent to the bill. Worth knowing about when reconciling provider invoices against expected cost.

## How CometAPI fits in

All four of these models, plus 500+ others, are available through [CometAPI](https://www.cometapi.com/) on a single OpenAI-compatible endpoint, with one credential, unified billing, and no per-provider account setup. Pricing on CometAPI is metered per token at the same per-model rates published by the underlying providers, with credits purchased upfront and applied across any model in the catalogue. The value of routing through CometAPI is operational rather than per-token: one credential to manage, one invoice to reconcile, and the ability to swap from GPT-5.5 to Claude Sonnet 4.6 to Gemini 3.5 Flash by changing a single string in your code.

There are workloads where direct provider access is the right call. If you run a single-model workload at very high volume on one provider, with a negotiated enterprise contract, the unit economics of going direct are better. If your compliance posture requires a specific vendor-of-record relationship, an aggregator complicates rather than simplifies that conversation. For the majority of teams running multi-model production workloads, however, the operational friction of managing three or four direct provider relationships is itself a meaningful cost, one that the rate card does not capture.

**Try the comparison on your workload.** The free tier on CometAPI lets you run the same prompt against GPT-5.5, Sonnet 4.6, Gemini 3.5 Flash, and DeepSeek V4 from a single endpoint, with no separate signups. For a workload-specific cost decision, that one-hour exercise is worth more than any pricing comparison ever published.

## How to use this comparison

The right model for your workload depends on which dimension of the rate card matters most for your traffic shape. A practical decision framework:

- **If reasoning depth is the bottleneck (**agentic workflows, complex multi-step planning, the hardest coding tasks), start with GPT-5.5 or Claude Opus 4.7. The premium is real but earned on these workloads.
- **If you want the best price-to-capability ratio for general production traffic,** Claude Sonnet 4.6 is the recommended default. Near-frontier capability, full 1M context at standard rates, and strong caching support.
- **If you are cost-sensitive and your workload sits below 200K context,** Gemini 3.5 Flash is the cheapest credible flagship-class option from a major US provider.
- **If your workload is high-volume and price-dominated, and DeepSeek’s data-residency posture is acceptable,** V4 changes the cost equation enough to be worth a serious evaluation, particularly for batch-shaped workloads.

*Want to go further on cost optimization?* The pricing data above is the foundation for routing: the practice of sending different queries to different models based on which one can handle them at the lowest cost. The companion piece, *Cutting LLM API Costs in Half: A Model Routing Guide for Production Workloads in 2026*, walks through the routing patterns that turn this rate card into actual savings on your monthly bill.

---

*Originally published at [https://www.cometapi.com/2026-llm-api-pricing-comparison-gpt-5-5-claude-gemini/](https://www.cometapi.com/2026-llm-api-pricing-comparison-gpt-5-5-claude-gemini/).*
