<!-- social-ops-fingerprint:c1885ea3fa25e546614e3f0797b74d4696e04c63822c0e5ac569e6cd61513e67 -->
---
title: Claude Haiku 5.5 vs GPT-6 Luna: Benchmarks, Pricing, Speed
---
# Claude Haiku 5.5 vs GPT-6 Luna: Benchmarks, Pricing, Speed

![Claude Haiku 5.5 vs GPT-6 Luna: Benchmarks, Pricing, Speed](https://resource.cometapi.com/1%E4%B8%8B%E8%BD%BD1.png)

## **TL;DR**

Claude Haiku 5.5 and GPT-6 Luna are low-cost reasoning models for high-volume API workloads. Both start at $0.10 per million input tokens and $0.50 per million output tokens. Haiku scores higher on the six comparisons published in Anthropic's launch materials. Luna retains its base token rates for prompts up to 272K input tokens, compared with Haiku's 100K threshold. For developers, the key measures are acceptance rate, end-to-end latency, API compatibility, and cost per accepted result—the total cost of all attempts divided by the number of outputs that pass predefined checks.

## Key Takeaways

- Haiku 5.5 leads the cited OSWorld 2.1 computer-use comparison, 72.4% versus Luna's 48.9%.
- On Terminal-Bench 4.0, the cited results are 39.2% for Haiku and 16.4% for Luna.
- Both start at identical short-context prices, but Haiku's higher price tier begins beyond 100K prompt tokens, versus Luna's 272K threshold.
- Artificial Analysis's max-effort model pages, checked October 9, 2026, show output speeds of 240.6 tokens/s for Haiku and 123.0 tokens/s for Luna; throughput excludes first-token waiting time.
- Start with Haiku for the computer-use and terminal tasks reflected in the shared benchmarks; consider Luna for large prompts. Keep your current model until a representative pilot demonstrates a useful improvement.

## What Are Claude Haiku 5.5 and GPT-6 Luna?

### Claude Haiku 5.5: Overview

[Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) launched on October 7, 2026. It combines low-priced inference with adjustable reasoning, tool use, long context, and text-and-image inputs. Typical applications include document extraction, database queries, customer support, and lightweight subagents.

### GPT-6 Luna: Overview

[GPT-6 Luna](https://developers.openai.com/api/docs/changelog) launched on September 22, 2026. It is positioned for focused tasks at scale, including classification, information extraction, structured output, programming assistance, and long-document processing. Its flexible reasoning settings include a non-reasoning configuration for simpler work.

### Specifications

| Specification | Claude Haiku 5.5 | GPT-6 Luna |
| --- | --- | --- |
| Developer | Anthropic | OpenAI |
| Release | October 7, 2026 | September 22, 2026 |
| Model ID | claude-haiku-5-5 | gpt-6-luna |
| Context window | 1,000,000 tokens | 1,050,000 tokens |
| Maximum output (standard API) | 128,000 tokens | 128,000 tokens |
| Input | Text and image | Text and image |
| Output | Text | Text |
| Reasoning | Adjustable, Low to Max | None to Max |
| Default effort | Medium | Medium |
| Knowledge cutoff | June 2026 | May 18, 2026 |
| Tool use | Yes | Yes |
| Structured output | Yes | Yes |
| Open weights | No | No |
| Architecture and parameter count | Not specified in the cited official materials | Not specified in the cited official materials |

Specifications use the vendors' standard API model documentation, checked October 9, 2026: [Haiku's standard API specifications](https://platform.claude.com/docs/en/models/haiku-5-5/overview) and [Luna's standard API specifications](https://developers.openai.com/api/docs/models/gpt-6-luna). Architecture and parameter counts are left unspecified because these sources do not establish them.

## Claude Haiku 5.5 vs GPT-6 Luna: Benchmark Results

| Benchmark | Haiku 5.5 | GPT-6 Luna | Leader |
| --- | --- | --- | --- |
| GDPval-AA v2.1 (Elo) | 1,620 | 1,437 | Haiku +183 |
| AA-Briefcase v1.1 (Elo) | 1,578 | 1,336 | Haiku +242 |
| OSWorld 2.1, offline partial score | 72.4% | 48.9% | Haiku +23.5 pp |
| Terminal-Bench 4.0 | 39.2% | 16.4% | Haiku +22.8 pp |
| FrontierCode 1.1 Main | 46.4% | 42.4% | Haiku +4.0 pp |
| Chartography, no tools | 46.4% | 29.1% | Haiku +17.3 pp |

The six rows above reproduce Anthropic's published launch-comparison results, checked October 9, 2026. They are comparisons published by Anthropic, including independent results reproduced there, rather than new tests run for this article. GDPval-AA and AA-Briefcase are Elo scores; percentage gaps are percentage points. These benchmark families measure different tasks and should not be averaged into a universal winner.

![Claude Haiku 5.5 vs GPT-6 Luna: Benchmarks, Pricing, Speed](https://resource.cometapi.com/1280X128001.PNG)

Haiku's strongest relative results in this launch table appear in visual computer interaction and terminal-based tasks. Its smaller lead in FrontierCode cautions against extrapolating a 20-point gap to every coding situation. Use these results to select pilot candidates, then validate your prompts and tool stack.

### Reasoning Effort and Evaluation Limits

Reasoning effort changes the accuracy–cost tradeoff. Compare available settings using the same workload and harness; equal vendor setting names do not guarantee equal reasoning-token budgets. The launch table reports OSWorld's offline subset and Chartography without tools. Harness, task selection, retries, and tool access can change outcomes. Anthropic's system card documents the benchmark-specific conditions. [Read the benchmark methods in Anthropic's system card.](https://www.anthropic.com/claude-haiku-5-5-system-card)

- OSWorld uses the 82-task offline subset, an Ubuntu virtual machine, 1080p screenshots, a 500-action limit, max effort, and five attempts per task. The 72.4%/48.9% comparison is partial-credit scoring, not the percentage of tasks completed perfectly; Haiku's strict pass rate is 37.1%. Anthropic ran Luna on the same task subset through OpenAI's API.
- Terminal-Bench uses 66 containerized tasks; Haiku ran at max effort in Claude Code bare mode, without internet egress or a fallback model, averaging ten trials per task.
- FrontierCode Main contains 100 tasks with five runs per task; Claude models used Claude Code and GPT models used Codex.
- GDPval-AA and AA-Briefcase were independently evaluated by Artificial Analysis and reproduced in the launch materials. These are separate evaluation pipelines, not one shared production harness.

## Claude Haiku 5.5 vs GPT-6 Luna: Feature Comparison

### Computer Use and Agentic Coding

Haiku's strongest advantage is in the shared launch tasks that require interacting with a graphical computer or working in a terminal. The OSWorld partial-score gap is 23.5 percentage points, while Terminal-Bench differs by 22.8 points. FrontierCode's smaller 4.0-point difference shows why the broader coding category should not be treated as a single workload.

For browser automation, test page navigation, form entry, recovery from tool failures, and end-to-end completion. For coding, test whether a patch passes your repository's functional checks and stays within scope. Those acceptance checks are more useful than selecting a model from the largest headline gap.

### Long Context and Document Processing

The 5% difference in nominal context capacity is less significant than the reliability and price of processing substantial prompts. Neither model is inherently superior at retrieving information just because its context window is larger.

The key difference is when higher rates apply: a 150K-token prompt crosses Haiku's threshold while remaining inside Luna's base tier. Luna is therefore the lower-cost starting point for that token workload. Whether it is the better document analyst still depends on extraction accuracy, citations, and the retries required to obtain an acceptable answer.

### Reasoning Controls

Both models expose adjustable reasoning effort, with medium as the default in the cited documentation. Luna also exposes a none setting. Use those controls to fit the task: extraction and routing may require less reasoning than an uncertain multi-step tool workflow. The same effort label does not imply the same compute budget across vendors.

### Multimodal Input and Structured Workflows

Both accept text and images and produce text. This makes them candidates for screenshots, document-image extraction, and structured downstream workflows. Their input support alone does not establish equal accuracy on small text, charts, or visual interfaces; measure those cases separately.

### Speed and Task Economics

| Independent metric (max effort) | Haiku 5.5 — Artificial Analysis | GPT-6 Luna — Artificial Analysis |
| --- | --- | --- |
| Intelligence Index v4.3.2 | 43 | 38 |
| Output speed | 240.6 tokens/s | 123.0 tokens/s |
| Weighted cost per Intelligence Index task | $0.21 | $0.07 |

Artificial Analysis is the independent testing publisher. The table is a snapshot of its max-effort model pages checked October 9, 2026, rather than official vendor performance. Output speed measures tokens received after generation begins; it is separate from time to first token and full task latency. Cost per task is a weighted Intelligence Index metric, not a quote for your production task or a cost per successful outcome.

Haiku's snapshot output throughput is approximately 1.96 times Luna's, while Luna's weighted evaluation-task cost is lower. This does not establish a 1.96-fold advantage in full task completion time. Production testing should record time to first token, completion time, output length, reasoning consumption, and tool execution time separately.

## Claude Haiku 5.5 vs GPT-6 Luna: Pricing and API Access

### Official Standard Rates

| USD per 1M tokens | Haiku ≤100K | Haiku >100K | Luna ≤272K | Luna >272K |
| --- | --- | --- | --- | --- |
| Input | $0.10 | $0.50 | $0.10 | $0.20 |
| Cached read | $0.01 | $0.05 | $0.01 | $0.02 |
| Cache write (Haiku: 5-minute TTL) | $0.125 | $0.625 | $0.125 | $0.25 |
| Output | $0.50 | $2.50 | $0.50 | $0.75 |

USD per million tokens at standard processing rates, checked October 9, 2026. The table uses [Haiku's standard and 5-minute cache-write rates](https://platform.claude.com/docs/en/models/haiku-5-5/overview) and [Luna's short- and long-context rates](https://developers.openai.com/api/docs/models/gpt-6-luna). Tool fees, taxes, regional uplifts, and optional processing-tier adjustments are excluded. Above the input threshold, the applicable higher rates cover the request rather than only the excess tokens.

The central distinction is the billing threshold. Haiku moves to higher rates beyond 100K prompt tokens, while Luna retains its low tier to 272K. Even above that threshold, Luna's cited long-context input and output prices are lower.

Haiku also offers 1-hour cache writes at $0.20/$1.00 per million tokens for short/long prompts. Cache persistence and pricing mechanisms differ between vendors, so compare reuse patterns rather than treating both cache-write rows as identical products. Haiku's 128K output limit is the standard API limit; its Message Batches API can support 300K output with a beta header.

### Illustrative Costs at Fixed Token Budgets

| Workload | Input / Output | Haiku 5.5 | GPT-6 Luna |
| --- | --- | --- | --- |
| Ticket classification | 2K / 200 | $0.0003 | $0.0003 |
| Short report | 40K / 4K | $0.006 | $0.006 |
| Repository analysis | 150K / 5K | $0.0875 | $0.0175 |
| Large document review | 300K / 10K | $0.175 | $0.0675 |
| Massive context analysis | 800K / 20K | $0.45 | $0.175 |

![Claude Haiku 5.5 vs GPT-6 Luna: Benchmarks, Pricing, Speed](https://resource.cometapi.com/677c7aa0-1d72-4607-9759-c67416243731.png)

Author-calculated uncached standard-rate estimate: cost = input tokens × input rate / 1,000,000 + billed output tokens × output rate / 1,000,000. “Output” means total billed output for this estimate, including reasoning tokens where charged as output; it is not necessarily visible answer length. The same reported token counts are used for both models, although tokenizers can differ.

A cheap token is not necessarily a cheap successful outcome. Teams should account for repeated attempts, failed tool calls, reasoning-token consumption, and different tokenizer behavior.

### CometAPI Access and Integration Constraints

CometAPI provides access options for both models. Before comparing or deploying them through the gateway, verify the model IDs, supported endpoints, request parameters, tool behavior, and billing rules for each route. These provider links document access options; they do not replace the vendors' technical or standard-pricing sources.

For direct OpenAI integrations, Luna supports built-in tools through the Responses API; Chat Completions function calling requires none reasoning effort. Haiku uses Anthropic's Messages API and adaptive thinking. A gateway does not make the underlying schemas interchangeable: validate tool definitions, structured-output behavior, streaming events, and accounting with the exact route you intend to use.

## How Can Developers Compare Claude Haiku 5.5 and GPT-6 Luna With the Same Prompt?

### Long-Document Extraction Example

A practical comparison can use a supplier-contract bundle containing effective dates, renewal terms, notice periods, and exceptions. Keep the document bundle, extraction instructions, expected fields, and validation rules identical. The following is an evaluation design, not a new measured model result.

Example prompt: Extract each contract's supplier name, effective date, renewal date, termination notice period, and pricing exceptions. For every extracted value, cite the document title and exact supporting passage. Return null when a field is absent; do not infer missing dates. Flag conflicting clauses and keep the final answer within 1,000 words.

| Check | Acceptance criterion | What to record |
| --- | --- | --- |
| Extraction accuracy | Required fields match an independently checked answer key | Correct, incorrect, and missing values |
| Grounding | Every non-null field has a valid supporting passage | Unsupported claims and wrong document citations |
| Instruction following | No invented dates; absent fields return null | Schema failures and constraint violations |
| Economics | Calculate spend per accepted extraction | Billed input, output, reasoning, retries, and fallback cost |
| Latency | Compare full job completion under the same tool policy | First-token time and end-to-end time |

Run more than one representative bundle and repeat the cases where results vary. Begin with the same available effort level, then test a lower-cost configuration for each model. Report sample size, settings, route, date, and failure counts before presenting a winner.

## Haiku 5.5 or GPT-6 Luna: Which to Choose?

| Dimension | Better-supported starting point | Decision boundary |
| --- | --- | --- |
| GUI interaction | Claude Haiku 5.5 | Shared OSWorld partial scores favor Haiku; verify full task completion |
| Terminal coding | Claude Haiku 5.5 | Shared Terminal-Bench scores favor Haiku; validate repository changes |
| Short prompts and base prices | Test both | Identical base rates; compare billed usage and retries |
| Prompts above 100K tokens | GPT-6 Luna on standard rates | Luna retains the base tier longer; accuracy may alter total cost |
| Streamed token throughput | Claude Haiku 5.5 in the dated snapshot | Throughput differs from full completion latency |
| Simple repeated extraction | Test Luna with low or no reasoning | Select by valid accepted output, rather than price alone |

### Choose Claude Haiku 5.5 for Benchmark-Relevant Interactive Tasks

Start with Haiku when your application resembles the published graphical-computer, terminal-coding, or professional-work tasks, and a higher completion rate would offset extra reasoning or long-context spend. Confirm that advantage on your own tool stack before routing production traffic.

### Choose GPT-6 Luna for Large-Prompt Cost Control

Start with Luna when prompts frequently exceed 100K tokens and standard token costs materially affect your budget. It is also a candidate for repeated extraction or routing that can succeed with low or no reasoning. Keep the recommendation conditional on accepted-result rates and actual billed usage.

### Use Both When Workloads Have Different Needs

A pilot could route long-document extraction to Luna and GUI or terminal tasks to Haiku, then validate each choice against acceptance checks. Trigger a fallback when an output fails schema validation, lacks required evidence, or fails a task-specific check, and include fallback costs and latency in the comparison.

### Validate Before Switching

Include your current model as the baseline. Move only when the candidate meets a predefined correctness target and improves cost per accepted result or end-to-end latency by enough to cover migration and maintenance. Hold rollout if critical tool errors rise. The recommendation changes if your pilot shows that Luna's lower rate is offset by retries, or that Haiku's higher benchmark scores do not improve your task success.

- Use a representative workload sample and score correct, incorrect, and incomplete results.
- Measure first-token latency, end-to-end task time, and tool reliability.
- Track input, cached, output, and reasoning token counts separately.
- Compute cost per successful result, including retries and fallbacks.
- Compare medium and high reasoning effort before enabling maximum settings by default.

## Conclusion

Claude Haiku 5.5 has stronger head-to-head launch evidence across the professional-work, computer-use, and agentic-coding benchmarks compared here. It also has higher output throughput in the independent snapshot. GPT-6 Luna has a clear standard-rate advantage for prompts above Haiku's 100K threshold and a lower weighted evaluation-task cost. Neither observation alone determines production reliability or cost per successful result.

The practical winner is the model that delivers an acceptable result at the lowest fully measured operational cost. Run both against your own prompts, tools, and retry rules rather than treating a single benchmark as the answer.

## FAQ

### Why can task costs differ when both models have the same base token prices?

The same base price does not mean the same total bill. Models can use different amounts of input, output, and reasoning tokens, and may need different numbers of retries or tool calls to produce an acceptable result. Long-context rates and cache usage also affect the total. Compare the total cost of all attempts divided by the number of accepted results, rather than token prices alone.

### Do higher long-context rates apply only to tokens above the threshold?

No. Under the standard pricing described in this article, crossing the input threshold applies the higher rates to the request, not just the excess tokens. For example, a 150K-input-token request crosses Haiku's 100K threshold but remains within Luna's 272K base tier. Use the applicable input and output rates for the whole request when estimating cost.

### Can Claude Haiku 5.5 and GPT-6 Luna share a prompt cache?

Do not assume cache entries transfer between models or providers. Design separate reuse strategies, then measure hit rates and billed usage on each route. Gateway support, retention rules, and request structure can affect whether repeated input is eligible for caching; verify these before forecasting savings.

### What should a Haiku-to-Luna migration test cover?

Test representative text and image inputs, required structured fields, tool arguments, streamed responses, and error recovery. Establish your current system's acceptance rate before migration, then compare both candidates under the same retry and tool policies. Similar token prices or model categories do not establish compatibility.

### Should benchmark scores drive a Haiku or Luna fallback?

Use scores to choose candidates, then trigger fallbacks on observed failures such as invalid tool arguments, missing required fields, or unmet task checks. Track fallback frequency and total billed cost. A second model can add latency and expense, so verify that it improves accepted outcomes rather than simply producing a second answer.

### Can sensitive data be routed through both APIs?

Review the exact vendors and gateway involved, their current retention settings, processing locations, contractual terms, and your organization's data policy before routing sensitive inputs. Model capability and pricing tables do not establish a route's eligibility for regulated or confidential data. Use the approved route when those requirements are decisive.

---

*Originally published at [https://www.cometapi.com/claude-haiku-5-5-vs-gpt-6-luna/](https://www.cometapi.com/claude-haiku-5-5-vs-gpt-6-luna/).*
