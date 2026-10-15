<!-- social-ops-fingerprint:359310e583a6ad88b45e194eb81b9e5e3a3e8bf4f14cb9b63680f68342c01e3b -->
---
title: Claude Sonnet 5.5 Price: API Pricing, Token Costs, and Cost per Task
---
# Claude Sonnet 5.5 Price: API Pricing, Token Costs, and Cost per Task

![Claude Sonnet 5.5 Price: API Pricing, Token Costs, and Cost per Task](https://resource.cometapi.com/8dbba81f-5705-44c4-8573-9ad834a485f1.png)

## TL;DR

Anthropic lists Claude Sonnet 5.5 at $2/M input tokens and $10/M output tokens. CometAPI lists separate third-party rates of $1.60/M input and $8/M output. Sonnet 5.5 has the same standard input and output rates as Sonnet 5, but its cache-read rate is lower. Cost per accepted task also depends on cache hits, token usage, tool calls, and retries.

Budget for cache writes and reads, billed output tokens including any billed reasoning tokens, tool use, retries, and human review or correction. The advertised improvement in task cost is workload-dependent; it is not a universal discount on every request.

## Key Takeaways

- Claude Sonnet 5.5 costs $2/M input and $10/M output on the Claude API; CometAPI rates start at $1.60/M input and $8/M output.
- Cache reads cost $0.10/M; writes cost $2.50/M for five minutes or $4/M for one hour. Savings depend on actual cache hits and reuse timing.
- The Claude Batch API reduces input and output rates by 50%; confirm availability and combined cache billing on the route you use.
- Sonnet 5.5 keeps Sonnet 5 standard input and output rates, with a lower cache-read rate. Lower cost per accepted task depends on token usage, retries, tools, and completion quality.
- The 1M-token context and 128K standard output limit support large tasks; 300K output is a Batch API beta option, not the standard limit.

## How Much Does Claude Sonnet 5.5 Cost at a Glance?

The [official Sonnet 5.5 token rates](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) below are in USD per million tokens. Cache writes, reads, and ordinary input are distinct billing categories. Batch is an asynchronous processing option and should not be assumed available through every gateway.

| Claude API mode | Input / 1M | Output / 1M | Cache treatment |
| --- | --- | --- | --- |
| Standard | $2.00 | $10.00 | Read $0.10; 5m write $2.50; 1h write $4.00 |
| Batch | $1.00 | $5.00 | Confirm combined Batch and cache billing |

Sonnet 5.5 has a 1M-token context window. Confirm the selected provider, routing geography, active rates, and cache billing before budgeting. Context capacity is a model limit, not a reason to apply another model's pricing threshold or processing tiers.

## How Much Does Claude Sonnet 5.5 Cost Through CometAPI?

The [Claude Sonnet 5.5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-sonnet-5-5/) has displayed input and output rates 20% below the corresponding Claude API rates. Pricing checked on October 1, 2026; token estimates exclude tools, retries, and other charges.

| Rate or workload | Claude API | CometAPI | Difference |
| --- | --- | --- | --- |
| Input / 1M | $2.00 | $1.60 | 20% lower |
| Output / 1M | $10.00 | $8.00 | 20% lower |
| 10K input + 2K output | $0.040 | $0.032 | $0.008 per request |
| 100K input + 10K output | $0.300 | $0.240 | $0.060 per request |

At 100,000 equivalent 10K-input, 2K-output requests, the simplified token estimates are $4,000 and $3,200, a difference of $800. At 10,000 equivalent 100K-input, 10K-output requests, they are $3,000 and $2,400, a difference of $600. Cache usage, output variation, and retries change these totals.

### Costs Beyond Model Tokens

A coding or research agent also consumes retrieval, browser, storage, application hosting, and execution resources. Tool results can enlarge the next prompt even when the external action itself is inexpensive. Confirm hosted-tool prices with the provider that actually runs the tool; model-token discounts do not automatically discount separate services.

### Reasoning Effort and Total Spend

Effort is not a separate multiplier in this rate table. It can affect the number of billed output tokens, tool iterations, and retries. Compare effort settings on the same task set and report completion quality alongside total cost.

### What Does Claude Sonnet 5.5 Cost Across Realistic Workloads?

These controlled examples use uncached input and billed output at standard rates, excluding tools and retries. Input plus reserved output must fit the active context limits.

| Workload | Input | Output | Claude API estimate | CometAPI estimate |
| --- | --- | --- | --- | --- |
| Small coding request | 10K | 2K | $0.040 | $0.032 |
| Document analysis | 100K | 10K | $0.300 | $0.240 |
| Long agent turn | 300K | 20K | $0.800 | $0.640 |
| Repository task | 800K | 40K | $2.000 | $1.600 |

For the 300K-input, 20K-output example, Claude API cost is (300,000 / 1,000,000 × $2) + (20,000 / 1,000,000 × $10) = $0.80. At $1.60/M input and $8/M output, the corresponding CometAPI calculation is $0.64. Both estimates assume ordinary uncached input and standard billed output, excluding tools and retries.

A multi-turn agent can send accumulated history repeatedly. Estimate the sum of all requests, including unsuccessful runs, rather than pricing only the final answer. Cost per accepted task equals total measured workload spend divided by accepted tasks; human review time can be reported separately.

### What Makes Claude Sonnet 5.5 More Cost-Efficient?

**Faster output generation.** Anthropic says Sonnet 5.5 generates outputs 30%+ faster than Sonnet 5. Faster generation does not directly lower per-token billing, but it can improve throughput and reduce the duration of interactive agent loops.

**Fewer tokens per completed task.** The largest potential saving comes when the model reaches the same result using fewer reasoning, tool, and final-output tokens.

**Fewer agent steps.** Repeated tool calls can multiply context because conversation history and tool outputs are often sent back to the model. Reducing one unnecessary tool iteration can therefore eliminate more than one isolated generation charge.

**Adaptive effort.** Sonnet 5.5 supports adaptive thinking and defaults to high effort on the Claude Platform. Lower effort settings can trade some reasoning depth for shorter, faster, less expensive responses when the workload does not require maximum deliberation.

The important optimization target is therefore not minimum tokens at all costs. It is the lowest cost per accepted result.

## What Is Claude Sonnet 5.5?

Claude Sonnet 5.5 is an Anthropic model released on September 28, 2026. Its 1M-token context and text-and-image inputs support coding, agents, and document analysis with text output. The Claude API defaults to high effort; choose effort using measured quality and cost for your workload.

| Specification | Claude Sonnet 5.5 |
| --- | --- |
| Provider | Anthropic |
| Claude API model ID | claude-sonnet-5-5 |
| Release date | September 28, 2026 |
| Context window | 1M tokens |
| Maximum output | 128K tokens |
| Batch API max output | 300K tokens, beta |
| Input | Text, images |
| Output | Text |
| Thinking | Adaptive |
| Default API effort | High |
| Reliable knowledge cutoff | June 2026 |
| Official input price | $2/M tokens |
| Official output price | $10/M tokens |
| Cache read | $0.20/M tokens |
| 5-minute cache write | $2.50/M tokens |
| 1-hour cache write | $4/M tokens |
| Batch API | 50% discount |

## How Much Performance Are You Buying With Claude Sonnet 5.5?

The [official evaluation methodology](https://www.anthropic.com/claude-sonnet-5-5-system-card) distinguishes test settings. Unless noted otherwise, the summary uses adaptive thinking, Max effort, default sampling, and five trials; historical-model configurations may differ. This price-focused comparison retains three coding and agent benchmarks: Terminal-Bench, FrontierCode, and CursorBench. The five struck-through rows below are removed from the revised article and retained here only for review.

| Benchmark / metric | Claude Sonnet 5.5 | Claude Sonnet 5 | Claude Opus 5.5 | Evaluation setting |
| --- | --- | --- | --- | --- |
| Terminal-Bench 4.0 / success | 70.6% Max | 10.3% | 66.4% Xhigh | 66 containerized terminal tasks; Sonnet uses Claude Code --bare, no internet egress, safeguards enabled |
| FrontierCode 1.1 Main / score | 46.2% Max | 42.4% | 54.4% | Repository patches in containers with internet access; held-out tests and rubric grading |
| CursorBench 4.0 / score | 55.5% Max | 34.1% | 57.8% | Real coding tasks in Cursor production agent harness; independently measured by Cursor |

These three benchmarks cover terminal-agent tasks, repository patching, and coding in a production agent harness. Their scores describe different evaluation setups, rather than a same-effort comparison or a measured cost advantage. To evaluate value for money, replay representative tasks and compare total spend per accepted result, including cache usage, tools, and retries.

## How Does Prompt Caching Change Claude Sonnet 5.5 Input Costs?

Anthropic’s [prompt-cache pricing](https://platform.claude.com/docs/en/about-claude/pricing) distinguishes 5-minute writes, 1-hour writes, and successful reads. A $0.10/M read is 95% below $2/M ordinary input, but that percentage applies only to reused input tokens.

| Operation | Claude API price / 1M |
| --- | --- |
| Ordinary input | $2.00 |
| 5-minute write | $2.50 |
| 1-hour write | $4.00 |
| Successful read | $0.10 |

Consider ten requests, each containing the same 100K-token prefix. Assume one 5-minute write followed by nine successful full-prefix reads before expiry, no additional writes, and enough context for the remaining prompt and output.

| Repeated-prefix component | No caching | One write + nine reads |
| --- | --- | --- |
| Ordinary prefix input | 10 × 100K × $2/M = $2.00 | $0.00 |
| Initial write | $0.00 | 100K × $2.50/M = $0.25 |
| Nine reads | $0.00 | 9 × 100K × $0.10/M = $0.09 |
| Repeated-prefix total | $2.00 | $0.34 |

The reduction is 83% for the repeated prefix alone. If each request also generates 2K billed output tokens, output adds $0.20 across ten requests: model-token totals become $2.20 without caching and $0.54 with caching, a reduction of about 75.5%. Additional input, cache expiry, rewritten prefixes, and tools change the bill again.

Track successful reads and writes separately. A repeated prompt is not proof of a cache hit. The example illustrates Claude API rates; verify the selected CometAPI route’s cache rates and usage reporting before applying the same estimate.

## How Does Claude Sonnet 5.5 Compare With Other Models?

### Claude Sonnet 5.5 vs Claude Sonnet 5

The Claude API pricing comparison gives both models the same $2/M input and $10/M output rates. Sonnet 5 cache reads cost $0.20/M, while Sonnet 5.5 cache reads cost $0.10/M. Developers evaluating the [Claude Sonnet 5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-sonnet-5/) against Sonnet 5.5 should compare accepted-task spend, not infer a token-rate saving from a model upgrade.

Anthropic reports [up to 30% lower task cost](https://www.anthropic.com/claude-sonnet-5-5) and faster output generation for Sonnet 5.5. These are vendor-reported workload results, not a 30% reduction in the rate card. Fewer tokens, tool iterations, and retries can change the bill; measure those quantities using your own acceptance criteria.

If both models consume identical uncached input and output tokens and succeed equally often, the standard token bill is identical. With cache reads, their bills can differ even at identical token counts. A model that completes more tasks or needs fewer corrections can still have better economics. Compare total spend across the full evaluation set, including failed attempts.

![Claude Sonnet 5.5 Price: API Pricing, Token Costs, and Cost per Task](https://resource.cometapi.com/42336ccc-bf3a-46d3-9d86-03ac27d57277.png)

*Anthropic’s published Sonnet 5.5 sand-dunes coding demonstration.*

Anthropic's sand-dunes demo shows a coding output from its [official product demonstration](https://www.anthropic.com/claude-sonnet-5-5). The image illustrates a single example, not a latency guarantee or a reproducible cost benchmark.

### Claude Sonnet 5.5 vs Claude Opus 5.5

| Model | Input / 1M | Output / 1M | Cache Read | Context |
| --- | --- | --- | --- | --- |
| Claude Sonnet 5.5 | $2 | $10 | $0.10 | 1M |
| Claude Opus 5.5 | $4 | $20 | $0.20 | 1M |

Anthropic documents 1M context, 128K output, and $4/M input plus $20/M output for Opus 5.5. The [Claude Opus 5.5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-opus-5-5/) is an alternative for complex, open-ended work. Sonnet 5.5 has half the nominal standard token rates; an escalation route still needs to include failed Sonnet attempts, validation, and retries in its total cost.

### Claude Sonnet 5.5 vs GPT-6 Sol

OpenAI documents [GPT-6 Sol pricing and model limits](https://developers.openai.com/api/docs/models/gpt-6-sol). Standard rates match Sonnet for input up to 272K tokens. Above that input threshold, GPT-6 Sol applies $4/M input and $15/M output to the full request. Context capacity and the lower-rate boundary are different limits.

| Dimension | Claude Sonnet 5.5 | GPT-6 Sol |
| --- | --- | --- |
| Standard input / output, USD per 1M | $2 / $10 | $2 / $10 for input up to 272K |
| Standard input / output above 272K input | $2 / $10 | $4 / $15 for the full request |
| Context / standard max output | 1,000,000 / 128,000 | 1,050,000 / 128,000 |
| Native modalities | Text and images in; text out | Text and images in; text out |
| Reasoning control | Adaptive thinking; default high | Effort none through max; default medium |
| Direct API integration | Claude Messages API | Responses; Chat Completions has tool-calling constraints |

GPT-6 Sol supports built-in tools through Responses; Chat Completions function calling requires reasoning\_effort=none. Developers can evaluate the [GPT-6 Sol API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-sol/), but must check gateway compatibility and live rates separately. For both models, compare total tokens, tools, retries, latency, and accepted-task completion at the selected effort and pricing tier.

## How Can You Reduce Claude Sonnet 5.5 API Costs?

- Cache stable prefixes such as system prompts, tool schemas, coding conventions, and large static documents.
- Reduce unnecessary context growth by pruning or summarizing stale tool results and prior conversation content.
- Match effort to task difficulty instead of using maximum reasoning for simple classification or formatting work.
- Use Batch processing for workloads that do not require immediate responses.
- Evaluate cost per successful task, not just dollars per million tokens.

## Is Claude Sonnet 5.5 Worth the Price?

Claude Sonnet 5.5's pricing story is unusual because Anthropic kept its standard input and output rates unchanged while reducing the cache-read rate. It kept the same $2/M input and $10/M output as Sonnet 5 and instead focused on making each task require less model work.

If a workload simply generates the exact same number of uncached input and output tokens, Sonnet 5.5 does not create an official per-token saving over Sonnet 5. But if stronger coding, tool use, and more concise execution reduce agent turns, retries, or output tokens, the bill can fall even with identical token rates.

Anthropic's claim of up to 30% lower cost per task should therefore be treated as a workload-dependent efficiency result rather than a universal 30% API discount. For migration testing, replay a fixed set of real production tasks and record total input, cached input, generated tokens, tool calls, completion rate, latency, and total cost.

## Conclusion

Claude Sonnet 5.5 combines a familiar token rate with an efficiency-focused upgrade. Use measured task completion, cache reuse, effort, tool activity, and retries to determine its practical value. Before migrating, replay a representative task set on both models and compare accepted-task cost, completion rate, retries, and latency using current provider rates.

## FAQ

### How can a team budget for variable Claude Sonnet 5.5 output lengths?

Group production requests by workload instead of relying on one average response. Measure billed input, output, retries, and cache usage for each group, then calculate expected monthly volume at the applicable rates. Report a central estimate and a higher-usage scenario based on observed long responses; update the budget when the distribution or traffic mix changes.

### When should a Sonnet 5.5 agent use a longer cache lifetime?

Compare expected reuse timing with the cost of rewrites. A one-hour write costs more initially than a five-minute write, but can be worthwhile when useful requests arrive after the shorter cache would expire. Calculate the writes and hits expected under each option using the same prefix, and verify real usage rather than treating every repeated request as a hit.

### How can teams evaluate a Sonnet 5.5 and Opus 5.5 escalation strategy?

Replay the same task set through Sonnet-only, Opus-only, and Sonnet-first routes. Define escalation triggers from validation failures or unmet acceptance criteria, and include the unsuccessful Sonnet attempt in the combined route’s cost. Compare accepted-task completion, total spend, correction time, and latency before deciding whether escalation reduces cost for the workload.

---

*Originally published at [https://www.cometapi.com/claude-sonnet-5-5-price/](https://www.cometapi.com/claude-sonnet-5-5-price/).*
