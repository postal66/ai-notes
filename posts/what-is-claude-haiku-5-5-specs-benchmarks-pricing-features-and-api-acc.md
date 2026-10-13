<!-- social-ops-fingerprint:6df120da70bf6f5c7fa765e0baeb322dba15a1d2b251b24127fc9ee5ce076b92 -->
---
title: What Is Claude Haiku 5.5? Specs, Benchmarks, Pricing, Features, and API Access
---
# What Is Claude Haiku 5.5? Specs, Benchmarks, Pricing, Features, and API Access

![What Is Claude Haiku 5.5? Specs, Benchmarks, Pricing, Features, and API Access](https://resource.cometapi.com/89e9b0fbfe0181f6ca565d913686ce8e49b5e9c2-1200x630.jpg)

## TL;DR

Claude Haiku 5.5 is Anthropic's fastest small model at standard speed for high-volume, latency-sensitive tasks. It combines a 1-million-token context window, a 128K standard output limit, adaptive reasoning, and base pricing starting at $0.10 per million input tokens and $0.50 per million output tokens. Rates rise when a prompt exceeds 100,000 tokens. For complex coding and extended agentic work, Sonnet 5.5 and Opus 5.5 remain stronger choices. CometAPI Standard pricing is 20% below the official rates, starting at $0.08 per million input tokens and $0.40 per million output tokens. The CometAPI model page is live and reports production API access.

## Key Takeaways

- Official release: October 7, 2026; Claude API model ID: claude-haiku-5-5.
- Starting API rates: $0.10 input and $0.50 output per million tokens for prompts up to 100K tokens. CometAPI: $0.08 input and $0.40 output per million tokens at 80% of official Standard pricing.
- Context and output: 1M tokens of context and 128K tokens of standard output.
- Focus: classification, document extraction, routing, support, and delegated agent tasks.
- The newer tokenizer can count approximately 30% more tokens for the same text; evaluate cost per accepted task rather than price per token alone.

## What Is Claude Haiku 5.5?

Claude Haiku 5.5 is the lightweight member of Anthropic's current Claude family, developed for large request volumes where responsiveness and operating economics are central. Its primary applications include document processing, conversational support, information extraction, and compact subagent jobs. Anthropic's [model overview](https://platform.claude.com/docs/en/models/haiku-5-5/overview) confirms the launch date, capabilities, and platform identifiers.

Claude Haiku 5.5 is the first Haiku model to support configurable effort levels, allowing developers to trade off reasoning depth, latency, and token usage within the same model.

## What Are the Key Features of Claude Haiku 5.5?

### Adaptive thinking and adjustable effort

Haiku 5.5 can decide when and how much to reason, while the effort parameter offers developers a way to balance response quality, latency, and token use. The default effort is medium. For simple classification, low effort may be preferable; for ambiguous extraction or tool-planning steps, a higher setting may be justified.

### Large-context processing

A 1M-token context window enables long documents and substantial conversation histories to fit within a single request. Developers should still use retrieval, truncation, and caching where appropriate: long contexts can introduce unnecessary cost and accuracy trade-offs, especially beyond the 100K pricing threshold.

### Low-cost high-throughput processing

The new $0.10/$0.50 starting rates make repeated short requests substantially less expensive than the previous Haiku generation on a per-token basis. Yet Anthropic documents a changed tokenizer: identical text produces approximately 30% more tokens than on Haiku 4.5. Actual task-level savings can therefore be smaller than headline rate reductions.

### Computer use and delegated agent tasks

Published evaluations indicate stronger performance on computer-interaction and tool-assisted tasks than the preceding Haiku model. This makes Haiku 5.5 useful for bounded agent steps, but successful automation still depends on strong tool permissions, error recovery, and human approval for risky actions.

## How Does Claude Haiku 5.5 Perform on Benchmarks?

Anthropic reports marked gains across professional knowledge tasks, computer use, coding, and reasoning. The results below use the reported evaluation settings; scores from different benchmarks should not be combined into one “intelligence score.”

| Benchmark | Haiku 4.5 | Haiku 5.5 | Sonnet 5.5 |
| --- | --- | --- | --- |
| GDPval-AA v2.1 (Elo) | 735 | 1,620 | 1,840 |
| AA-Briefcase v1.1 (Elo) | 614 | 1,578 | 1,824 |
| OSWorld 2.1, offline subset, partial credit | 15.7% | 72.4% | 83.9% |
| Humanity's Last Exam, no tools | 10.2% | 45.9% | 56.9% |
| Humanity's Last Exam, with tools | 18.7% | 57.4% | 64.5% |
| Terminal-Bench 4.0 | 0.0% | 39.2% | 70.6% |
| Chartography, no tools | 6.4% | 46.4% | 61.6% |

The system card's standard Haiku 5.5 evaluation configuration uses adaptive thinking at max effort, default sampling and five trials unless otherwise noted; the product default is medium, so headline scores are not default-setting guarantees. OSWorld uses 82 offline tasks, no internet access, 1080p and a 500-action limit. Its 72.4% is a partial-credit score; strict pass rate is 37.1%. GDPval-AA and AA-Briefcase are reported by Anthropic from independently run Artificial Analysis evaluations.

Terminal-Bench 4.0 uses Claude Code in --bare mode with safeguards enabled. Haiku 5.5 uses max effort, no fallback model and no internet egress, with 10 trials per task; Sonnet 5.5 uses five trials and a fallback for some flagged requests. Haiku 4.5 uses a fixed 63,999-token thinking budget. These configuration differences matter when interpreting 39.2% versus 70.6%.
Anthropic's [published benchmark results](https://www.anthropic.com/claude-haiku-5-5) supply the scores above. OSWorld uses its offline subset; Humanity's Last Exam separates tool-enabled and tool-free runs, and Chartography is tool-free. These are vendor-reported results, not independent measurements under a universal configuration. Anthropic provides evaluation details in its [Haiku 5.5 system card](https://www.anthropic.com/claude-haiku-5-5-system-card); reproduce the relevant effort, tool, scaffold and budget settings before comparing your own results. The launch summary does not specify a complete common test environment for every row.

![What Is Claude Haiku 5.5? Specs, Benchmarks, Pricing, Features, and API Access](https://resource.cometapi.com/9349cf-95e2-47a1-952b-a298cf64165b.png)

Anthropic's official evaluation graphic above is reproduced from its system card. It provides additional evidence about the evaluated configurations; it is not a new benchmark produced for this article.

### Benchmark Interpretation

The OSWorld improvement suggests Haiku 5.5 has become significantly more useful for structured graphical tasks. However, Sonnet 5.5's 70.6% versus Haiku 5.5's 39.2% in Terminal-Bench indicates a continued advantage for larger-model agentic coding. Select models according to the failure cost and difficulty of the actual workflow.

## Claude Haiku 5.5 vs Haiku 4.5 vs Sonnet 5.5

| Dimension | Haiku 4.5 | Haiku 5.5 | Sonnet 5.5 |
| --- | --- | --- | --- |
| Context | 200K | 1M | 1M |
| Max standard output | 64K | 128K | 128K |
| Standard input / MTok | $1 | $0.10 up to 100K; $0.50 over | $2 |
| Standard output / MTok | $5 | $0.50 up to 100K; $2.50 over | $10 |
| Reasoning | Extended thinking with a fixed token budget | Adaptive; medium default | Adaptive; high default |
| Relative latency | Fast | Fastest at standard speed | Fast |
| Coding depth | Bounded tasks | Stronger subagents | More complex coding |
| Typical use | Legacy small-model deployments | High-volume workflows | Complex production workflows |

Shared specifications: all three models accept text and image inputs and produce text outputs. They can be accessed through the Claude API and supported partner platforms; model identifiers and account access depend on the provider. The cited product documentation does not establish parameter counts or detailed architectures.

Haiku 5.5 is a sensible first choice for verifiable and repetitive tasks. Sonnet 5.5 becomes more attractive where stronger judgment saves repeated failed calls, tool retries, or human corrections. Opus 5.5 is an option for particularly demanding multi-step assignments.

The comparative latency labels refer to standard-speed modes. Anthropic's [speed qualification](https://www.anthropic.com/claude-haiku-5-5) excludes Opus Fast Mode from the fastest-model claim. Architecture details such as parameter count are not established by these product tiers. Text-and-image input with text output is distinct from image generation.

The capability comparison follows Anthropic's [model specifications](https://platform.claude.com/docs/en/models/overview). Platform access depends on the selected provider and account; no model tier implies a published parameter count.

### Workload Selection

| Workload | Practical default | Why |
| --- | --- | --- |
| Email classification | Haiku 5.5 | Short, repeated, verifiable decisions |
| Document field extraction | Haiku 5.5 | Cost-efficient structured processing |
| Support triage | Haiku 5.5 | Fast responses and escalation |
| Coding subagents | Haiku 5.5 | Low-cost file search and contained edits |
| Complex debugging | Sonnet 5.5 | Stronger coding benchmark performance |
| High-stakes multi-step reasoning | Opus 5.5 | More capable upper-tier model |
| Mixed workload | Haiku + Sonnet | Route by complexity and confidence |

## How Much Does Claude Haiku 5.5 Cost?

**Why is Haiku 5.5 advertised as “around 75% cheaper” if its token price is 90% lower?**

The 90% figure describes the reduction in Standard input and output rates for prompts up to 100,000 tokens; longer prompts receive a 50% reduction. Anthropic reports that Haiku 5.5 costs around 75% less to run on average, accounting for the earlier model's request-length mix and changes in token usage per task. Tokenization is one factor: the same input text can count as approximately 30% more tokens, so cost estimates should use counts measured with the new model.

Anthropic's [official pricing](https://platform.claude.com/docs/en/about-claude/pricing) has two prompt-length bands. The rates in the first table are official USD prices per million tokens; the CometAPI comparison below applies a 20% discount to official Standard input and output rates.

| Rate category | Prompt up to 100K | Prompt over 100K |
| --- | --- | --- |
| Input | $0.10 | $0.50 |
| Output | $0.50 | $2.50 |
| 5-minute cache write | $0.125 | $0.625 |
| 1-hour cache write | $0.20 | $1.00 |
| Cache read | $0.01 | $0.05 |
| Batch input (50% off) | $0.05 | $0.25 |
| Batch output (50% off) | $0.25 | $1.25 |

Official Standard, cache and Batch rates are shown above, checked on October 8, 2026. Prompt length selects the pricing band; the higher band applies to the request rather than only the tokens above 100K. The CometAPI Standard rates below equal the corresponding official Standard rates multiplied by 0.8. This comparison does not assume that the gateway discount stacks with Batch or caching discounts.

| Prompt length | Token category | Official Standard / MTok | CometAPI / MTok |
| --- | --- | --- | --- |
| Up to 100K tokens | Input | $0.10 | $0.08 |
| Up to 100K tokens | Output | $0.50 | $0.40 |
| Over 100K tokens | Input | $0.50 | $0.40 |
| Over 100K tokens | Output | $2.50 | $2.00 |

### Example: 100,000 short requests per month

Assume each request uses 2,000 input tokens and 500 output tokens; each request remains below the 100K threshold. Ignore prompt caching, tools, and retries, and assume identical token counts across models for illustration.

| Model / provider | Input/month | Output/month | Total/month |
| --- | --- | --- | --- |
| Haiku 4.5 — official Standard | $200 | $250 | $450 |
| Haiku 5.5 — official Standard | $20 | $25 | $45 |
| Sonnet 5.5 — official Standard | $400 | $500 | $900 |
| Haiku 5.5 — CometAPI | $16 | $20 | $36 |

In this example, 100,000 requests use 200 million input tokens and 50 million output tokens. CometAPI input costs 200 × $0.08 = $16 and output costs 50 × $0.40 = $20, for $36 per month versus the official $45: a $9 saving, or 20%. The scenario excludes caching, tools and retries and uses fixed token counts; measure cost per accepted task on representative inputs because the newer tokenizer changes token counts.

The $450-to-$45 comparison is a fixed-token illustration of a 90% rate reduction, not a promise of 90% savings for equivalent real workloads. In its [launch announcement](https://www.anthropic.com/claude-haiku-5-5), Anthropic reports around 75% lower average running cost after accounting for request lengths and token-usage changes. Recount representative inputs and measure completed-task cost before estimating your own savings.

## Where Can You Access Claude Haiku 5.5?

### Official access and cloud platforms

Haiku 5.5 is available through the Claude API and supported platforms on Amazon Web Services, Google Cloud, and Microsoft Azure, according to Anthropic's [availability announcement](https://www.anthropic.com/claude-haiku-5-5). The direct Claude API model ID is claude-haiku-5-5; Amazon Bedrock uses anthropic.claude-haiku-5-5. Use credentials issued by your chosen provider and check its current account-access requirements.

### Third-party access through CometAPI

The [CometAPI model page](https://www.cometapi.com/models/anthropic/claude-haiku-5-5/) lists claude-haiku-5-5 as available, with Standard rates starting at $0.08 per million input tokens and $0.40 per million output tokens for prompts up to 100K, 20% below the corresponding official rates. Use a CometAPI-issued key with CometAPI's endpoint and request format; it is a separate access route from direct Anthropic API access. Check the live page for availability, pricing bands, and integration details.

When switching providers or upgrading from Haiku 4.5, verify model IDs, recount tokens, and test response limits and conversation handling. For implementation details and breaking changes, consult Anthropic's [migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide).

### Migration Validation

- Update the model ID and validate endpoint-specific request fields.
- Recount tokens with the updated tokenizer, including stable prefixes and tool definitions.
- Test adaptive-thinking settings, latency distributions, and response-block parsing.
- Check tool calls, failure recovery, and any stored thinking-block account restrictions.
- Compare p50/p95 latency, accepted-task rate, and total billable tokens.
- Use staged rollout and a rollback path for business-critical workflows.
- Assistant prefill is banned

The [Haiku 5.5 migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) explains tokenizer behavior, IDs and request compatibility. Omit temperature, top\_p and top\_k. If explicitly supplied, temperature must be 1 and top\_p must be 0.99; any top\_k value, or supplying both temperature and top\_p, returns a 400 error.

## What Are the Limitations of Claude Haiku 5.5?

Haiku 5.5 is not a universal substitute for larger models. Complex coding and long-horizon reasoning remain meaningful differentiators for Sonnet and Opus. Longer prompts also cost more, so the 1M-token window should be used selectively. Adaptive reasoning introduces variance in generated tokens and latency; benchmarks do not establish guarantees for an individual business workflow.

Risk-sensitive automation should validate structured outputs, limit external-tool permissions, keep audit logs, and require review before consequential actions. Route uncertain tasks to stronger models rather than relying solely on Haiku's lower base token price.

## Conclusion

For high-volume processing with measurable acceptance criteria, Claude Haiku 5.5 is an attractive upgrade: lower entry pricing, larger context, adaptive reasoning, and stronger published evaluations. For complex programming and ambiguous decision-making, Sonnet 5.5 or Opus 5.5 may deliver better overall economics by reducing retries and corrections. The winning strategy is to benchmark the full workflow and route requests according to difficulty.

## FAQ

### How does Haiku 5.5's 100K pricing boundary affect a cached workflow?

Prompt length determines which rate band applies; do not estimate the charge from new text alone or assume only the excess tokens use the higher rate. Count the request for the selected model, including history and tool definitions, then reconcile input, cache-write, cache-read and output usage with the relevant band. Compare invoices on representative cached requests before setting a production budget.

### Can Haiku 5.5 thinking blocks be replayed across accounts?

They work only in the account that produced them or an account linked to it. If an unrelated account sends a stored thinking block, the API discards it before the model sees it; the request can still succeed without that reasoning. See the [official migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide). Preserve the conversation blocks and use the originating or linked account when continuing a tool workflow. A gateway or account change should be tested explicitly; matching a model name does not guarantee that stored thinking blocks remain usable.

### Why can Haiku 5.5 truncate a response that Haiku 4.5 completed?

The newer tokenizer can count more tokens for the same text, so an unchanged max\_tokens limit may hold less equivalent output. Adaptive thinking can also consume output budget. Inspect stop\_reason and usage, recount prompts with the new model, and retune output allowances on real tasks rather than copying legacy limits.

### How should Haiku 5.5 routing thresholds be selected?

Use a labeled sample from the actual workload to measure accepted-task rate, correction cost and latency. Route requests that fail explicit validation or exceed the tested task scope to a stronger model. Tune the threshold against total workflow cost, including retries and escalation, and monitor it after changes to prompts, tools or effort.

---

*Originally published at [https://www.cometapi.com/what-is-claude-haiku-5-5/](https://www.cometapi.com/what-is-claude-haiku-5-5/).*
