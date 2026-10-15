<!-- social-ops-fingerprint:e85d3f0a582d5a45fd1bac8bcd8e7c293ac06a4929e7ab92d5bc1679424c2c63 -->
---
title: Gemini 4 Argon Performance: Benchmarks and Limits
---
# Gemini 4 Argon Performance: Benchmarks and Limits

![Gemini 4 Argon Performance: Benchmarks and Limits](https://resource.cometapi.com/1images.jpeg)

## TL;DR

Google announced [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) on September 30, 2026 s a frontier model for complex, long-running workflows. Its published results show a clear pattern: strong performance in professional knowledge work, long-context tasks, and selected software-engineering evaluations, with weaker results on some terminal and computer-use benchmarks. Google is introducing the model through a phased rollout. Separately, CometAPI reports catalog availability as of October 1; account eligibility and a successful test request should be checked before deployment. The more useful performance story is where its gains appear.

Argon scores 68.9% on the Vals Index, 65.4% on Vals Finance Agent v2, 77.9% on DeepSWE v1.1, 91.7% on LVBench, and 84.2% on GraphWalks at 256K–1M context. At the same time, it trails competing frontier models on FrontierSWE v2, Terminal-Bench 4.0, Terminal-Bench Science, and OSWorld-2.0.

The results favor a workload-specific view of Argon. Its strongest scores cluster around professional knowledge work, very-long-context tasks, and selected multimodal and software-engineering evaluations. Other models retain advantages on several terminal and computer-use tests.

## Key Takeaways

- Gemini 4 Argon is strongest in enterprise knowledge work, long-context reasoning, multimodal understanding, and several long-horizon coding evaluations.
- Its 1 million-token maximum output limit provides more generation headroom for long reasoning trajectories; it does not establish a public input-context specification.
- Argon leads several published knowledge-work and long-context results, but GPT-6 Astra and Claude Opus 5.5 remain ahead on selected coding and computer-use evaluations.
- Benchmark scores describe particular model-and-agent configurations. Metrics, input conditions and evaluation settings matter as much as the headline percentages.
- Google's rollout and CometAPI access are separate availability claims. Verify the active route, model identifier and account eligibility before migrating traffic.

## What Is Gemini 4 Argon?

Gemini 4 Argon is Google DeepMind's new frontier Gemini model, built around difficult workflows that require reasoning over many steps rather than answering one short prompt.

Google's official positioning emphasizes real-world software engineering, enterprise knowledge work such as legal and finance, defensive cybersecurity, multimodal understanding, and long-running agentic tasks.

This is an important distinction from the recent Flash releases. [Gemini 3.8 Flash API in CometAPI](https://www.cometapi.com/models/google/gemini-3-8-flash/) is designed as a lower-cost workhorse for agentic workloads at scale. Argon instead represents the frontier end of Google's stack, prioritizing depth and sustained execution.

### Model Specifications

| Specification | Gemini 4 Argon |
| --- | --- |
| Developer | Google DeepMind |
| Announced | September 30, 2026 |
| Model family | Gemini 4 |
| Positioning | Frontier reasoning and long-horizon model |
| Maximum output | 1,000,000 tokens |
| Long-context evaluation | Tested through 256K–1M on GraphWalks |
| Public input context limit | Not formally specified in a standard public API spec table at launch |
| Multimodal understanding | Yes; includes charts, documents and long-video evaluation |
| Agentic coding | Yes |
| Computer use | Evaluated |
| Cybersecurity | Specialized defensive capabilities |
| Google public API model ID | Not announced in Google's initial public documentation; CometAPI uses gemini-4-argon as its catalog identifier. |

## Output Budget and Trade-offs

Google announces a maximum output limit of 1 million tokens for Argon, up from the previous 64K limit cited in its launch announcement. This provides headroom for longer reasoning trajectories. It should not be interpreted as a guaranteed total budget for an entire multi-call agent session, or as proof that every task will improve.

Maximum output is not the same as intelligence. Giving a model more output tokens does not automatically make it more capable; it removes one potential bottleneck. The model still has to use that budget productively.

There is also a cost and latency trade-off. A model that actually consumes hundreds of thousands of generated tokens can be expensive and slow even when the nominal per-token price looks attractive.

![Gemini 4 Argon Performance: Benchmarks and Limits](https://resource.cometapi.com/1280X1280.PNG)

Selected benchmark results reproduced from the article. Compare models within each row; metrics and evaluation conditions differ. This chart replaces the decorative gradient artwork and does not represent independent testing.

A maximum output limit and an input context window describe different capacities. The GraphWalks evaluation range is evidence about the tested inputs, not a substitute for a public API specification.

## How Does Gemini 4 Argon Perform on Benchmarks?

Google DeepMind's performance table covers agent workflows, professional knowledge work and multimodal tasks. The values below reproduce that published comparison. They measure task performance, not token throughput or response latency; “—” means a result is not reported in this comparison.

| Benchmark | Gemini 4 Argon | GPT-6 Astra | Claude Fable 5.1 | Claude Opus 5.5 | Evaluation conditions |
| --- | --- | --- | --- | --- | --- |
| Vals Index | 68.9% | 63.1% | 65.8% | 67.0% | Vals AI |
| AutomationBench | 51.3% | 41.4% | 31.4% | 42.5% | Private set; Zapier leaderboard |
| Vals Finance Agent v2 | 65.4% | 53.5% | 58.9% | 58.6% | Vals AI |
| Harvey's Legal Agent | 19.6% | 5.4% | 6.7% | 3.8% | Vals AI |
| DeepSWE v1.1 | 77.9% | 74.1% | 67.4% | 74.2% | mini-swe harness; mixed sources |
| FrontierSWE v2 | 55.0% | 65.5% | 56.3% | 62.3% | Proximal leaderboard |
| Vibe Code Bench | 91.9% | 89.6% | 90.3% | 90.3% | Vals AI leaderboard |
| Terminal-Bench 4.0 | 57.4% | 58.2% | 57.9% | 66.4% | Self-test / leaderboard |
| PostTrainBench | 45.3% | 44.3% | 40.2% | 49.3% | v1.1; OpenCode; 10h; one H100 |
| Terminal-Bench Science 0.1 | 57.6% | 68.1% | 52.6% | 63.3% | Verifier timeout ×6 |
| LABBench 2 | 88.8% | 85.4% | 68.6% | 73.1% | Linux tools; internet |
| RiemannBench | 76.0% | 72.0% | 65.6% | 69.6% | Surge leaderboard |
| GraphWalks up to 128K | 99.7% | 98.7% | 91.4% | 90.6% | BFS F1; 650 items |
| GraphWalks 256K–1M | 84.2% | 71.8% | 65.0% | 66.8% | BFS F1; 200 items |
| Agent's Last Exam | 39.5% | 34.2% | — | 38.2% | Binary pass; ALE-Claw; 5h |
| OSWorld-2.0 | 69.2% | 72.6% | — | — | Offline partial score; best of 3 runs |
| Chartography | 71.6% | 71.0% | 46.2% | 66.3% | No tools; Surge leaderboard |
| LVBench | 91.7% | 87.5% | 79.7% | 83.7% | No tools; model-specific frame sampling |
| CWE-bench v1 | 68.0% | 68.0% | 58.0% | 67.0% | pass@1; pass@4 breaks ties |

![Gemini 4 Argon Performance: Benchmarks and Limits](https://resource.cometapi.com/1benchmarks.gif)

*Google's official Gemini 4 Argon benchmark comparison*

Unless noted otherwise, Argon results use a single attempt and the highest thinking setting. Other-model results generally come from provider reports, with benchmark-specific exceptions. LVBench uses 1 FPS for Gemini, 800 frames for GPT-6 Astra, 300 for Fable 5.1 and 600 for Opus 5.5. These inputs are not identical, so compare the reported configurations rather than treating every row as a controlled rerun.

## Evaluation Conditions and Limitations

The table is useful, but it should not be interpreted as an independent universal leaderboard.

- The benchmark selection is Google's selection.
- The [benchmark-specific evaluation settings](https://deepmind.google/models/evals-methodology/gemini-4-argon) differ across rows, including agent frameworks, time budgets, tools and input sampling.
- The official methodology identifies provider-reported competitor results as the default, with benchmark-specific leaderboard and self-computed exceptions.
- The highest benchmark setting may not reflect a default production inference configuration.
- A headline benchmark score alone does not reveal token usage, tool calls, retries, elapsed time, or human intervention.

For production systems, a better metric is often cost per successfully completed task rather than price per token or one benchmark percentage.

## Which Workload Is Gemini 4 Argon Best For?

### Knowledge Work Performance

The clearest pattern in Argon's results appears in professional, multi-step knowledge work.

On the Vals Index, Argon reaches 68.9%, compared with 67.0% for Claude Opus 5.5. The numerical gap is modest, but the pattern becomes more obvious in specialized workflows.

- Vals Finance Agent v2: 65.4%, 6.5 points above the strongest competitor shown in Google's table.
- AutomationBench: 51.3%, 8.8 points above Claude Opus 5.5.
- Harvey's Legal Agent Benchmark: 19.6%, compared with 6.7% for the next-highest reported model.

The performance profile suggests that Argon benefits most when the model must collect information, preserve state, reason across several stages, and produce a professional artifact rather than simply answer a closed-ended question.

The low absolute legal-agent score is also important. A 19.6% score alone does not reveal how many criteria or complete workflows failed. The useful conclusion is that Argon shows a large relative improvement on this evaluation, while the result does not establish reliable automation of legal work.

### Long-Context Reasoning

Argon's most striking advantage may be the 256K–1M version of GraphWalks.

- Gemini 4 Argon: 84.2%
- GPT-6 Astra: 71.8%
- Claude Opus 5.5: 66.8%
- Claude Fable 5.1: 65.0%

That is a 12.4-point advantage over the closest model in the published comparison.

The gap is much smaller at shorter context lengths: on GraphWalks up to 128K, Argon scores 99.7% and GPT-6 Astra scores 98.7%. This suggests that Argon degrades less sharply than the compared models on this particular very-long-context evaluation.

What Google has not disclosed is enough architectural information to attribute this difference to a specific attention mechanism, retrieval system, training recipe, or inference-time strategy. Claims such as “Gemini 4 introduces a new attention architecture” would therefore go beyond the public evidence.

### Coding Performance

The official benchmark table does not support a simple yes.

Argon performs extremely well on some forms of coding and loses clearly on others. On DeepSWE v1.1 it reaches 77.9%, versus 74.2% for Claude Opus 5.5 and 74.1% for GPT-6 Astra. Its Vibe Code Bench score is also strong at 91.9%.

- FrontierSWE v2: 55.0% Argon vs. 65.5% GPT-6 Astra.
- Terminal-Bench 4.0: 57.4% Argon vs. 66.4% Claude Opus 5.5.
- Terminal-Bench Science 0.1: 57.6% Argon vs. 68.1% GPT-6 Astra.

This split is important for developers. Argon appears especially strong when coding becomes a long engineering workflow with substantial context and planning, while terminal-heavy execution remains more competitive. A repository migration benchmark and an interactive terminal benchmark should not be treated as interchangeable measures of “coding ability.”

### Defensive Cybersecurity

Cybersecurity is a core deployment area. Google's [defensive cybersecurity positioning](https://deepmind.google/models/gemini/) includes autonomous vulnerability discovery, validation and patching. This is a provider capability claim; the CWE-bench result below measures vulnerability remediation on its own evaluation.

On CWE-bench v1, Argon scores 68%, tied with GPT-6 Astra and slightly ahead of Claude Opus 5.5 at 67%.

Google also highlights stronger safeguards against misuse, indirect prompt injection, risky agent behavior, and execution-environment compromise. This makes Argon as much an agent-security release as a conventional model upgrade.

### Multimodal Understanding

Argon scores 71.6% on Chartography and 91.7% on LVBench for long-video understanding. The LVBench result is 4.2 percentage points above GPT-6 Astra in Google's table. Because the models receive different frame-sampling configurations, this is a comparison of the reported setups rather than a pure model-only advantage.

This matters because many professional workflows are not text-only. A financial research agent may need to inspect a chart; an enterprise assistant may combine reports, PDFs and screenshots; a video-analysis system may need to preserve events across a long sequence rather than process individual frames independently.

Argon's combination of multimodal perception and sustained reasoning is therefore more relevant than multimodal support alone.

### Science and Mathematics Performance

The results are mixed but generally strong. Argon reaches 88.8% on LABBench 2 and 76.0% on RiemannBench, ahead of the compared models in Google's table. However, on Terminal-Bench Science 0.1, GPT-6 Astra reaches 68.1% compared with Argon's 57.6%.

That difference points toward a broader pattern: Argon appears stronger at reasoning over scientific information than at every form of tool-driven scientific execution.

### Computer-Use Performance

On Agent's Last Exam, Argon scores a 39.5% binary pass rate, ahead of GPT-6 Astra at 34.2% and Claude Opus 5.5 at 38.2%. On OSWorld-2.0's offline subset, its partial score is 69.2%, below GPT-6 Astra's 72.6%. The OSWorld value is not a full-task success rate, and missing Claude entries do not imply zero capability.

So the current data does not show an across-the-board computer-use advantage. For production deployment, benchmark scores should be supplemented by task-level testing of navigation accuracy, failed clicks, retry frequency, unintended actions, time to completion, and human correction rate.

## Gemini 4 Argon vs GPT-6 Astra and Claude

| Dimension | Gemini 4 Argon | GPT-6 Astra | Claude Opus 5.5 | Claude Fable 5.1 |
| --- | --- | --- | --- | --- |
| Knowledge work | Very strong | Strong | Very strong | Strong |
| Long-context benchmark | Strongest published result | Strong | Moderate–strong | Moderate |
| Long-horizon coding | Very strong | Very strong | Very strong | Strong |
| Terminal coding | Competitive | Strong | Strongest in selected test | Competitive |
| Scientific terminal agents | Competitive | Strongest in selected test | Strong | Competitive |
| Multimodal understanding | Very strong | Very strong | Strong | Competitive |
| Computer use | Competitive | Strong | Mixed / limited comparison | Limited comparison |
| Cybersecurity | Tied at top on CWE-bench v1 | Tied at top | Very close | Lower |

Argon stands out in this comparison for long-context, document-heavy and professional agent work. Developers can compare it with [GPT-6 Astra](https://www.cometapi.com/models/openai/gpt-6-astra/), [Claude Opus 5.5](https://www.cometapi.com/models/anthropic/claude-opus-5-5/) and [Claude Fable 5.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) through CometAPI.

### Performance-based selection

The qualitative labels above summarize the selected benchmark table, not a universal ranking. Favor Argon for a pilot when the work resembles its leading evaluations; test Astra and Opus on terminal-heavy workloads before selecting a default.

### Specifications and deployment constraints

This performance comparison does not establish an architecture advantage or a general price-performance winner. Argon's parameter count and architecture are not specified in the reviewed Google launch materials. Its public input-context limit requires official API documentation. CometAPI reports a gemini-4-argon route; confirm its supported parameters and account access independently of Google's broader rollout. Compare each route's limits and actual task costs before deploying.

## How Can Developers Access Gemini 4 Argon Through CometAPI?

CometAPI reports the model as available under gemini-4-argon. Use the account dashboard to create an API key, select that identifier in the playground, and run a test request before integration. Its OpenAI-compatible example uses base URL `https://api.cometapi.com/v1`. Confirm the model's supported endpoint and parameters in the account documentation; a catalog badge alone does not verify a successful call.

1. Create a CometAPI account and generate an API key in the dashboard.
2. Choose gemini-4-argon and validate a representative request in the playground.
3. Configure the compatible client with the CometAPI base URL, your key and the model identifier; confirm the supported request schema and billing before deployment.

### CometAPI and official pricing

Google announced introductory pricing of [$2 per million input tokens](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) and $10 per million output tokens, with cached input priced at 95% off the input rate. After the introductory period, the announced rates are $4 input and $20 output per million tokens. These are Google's announced rates, not CometAPI prices or confirmation of immediate general API access.

| Billing basis | Gemini 4 Argon API in CometAPI | Google official announcement | Comparison |
| --- | --- | --- | --- |
| Input / 1M tokens | $3.20 | $4.00 after introductory period | 20% below announced post-intro rate |
| Output / 1M tokens | $16.00 | $20.00 after introductory period | 20% below announced post-intro rate |

## Conclusion

Gemini 4 Argon's benchmark profile is more interesting than a simple leaderboard claim.

**The strongest results in this comparison cluster around professional knowledge work, long context and sustained agent execution.** This pattern is useful for workload selection, but does not identify the underlying architecture or prove which mechanism caused the gains.

The reported finance, legal, long-video and software-engineering results support a focused pilot for those workloads. Whether the same advantage persists in production depends on the input mix, agent framework, inference settings and verification requirements.

At the same time, the results show that frontier-model performance is becoming increasingly specialized. Argon can lead DeepSWE while trailing FrontierSWE; lead Agent's Last Exam while trailing OSWorld; and lead LABBench while trailing Terminal-Bench Science. These benchmarks stress different parts of an agent system.

For developers, the most important lesson is that model selection increasingly needs to happen at the workload level rather than the brand or family level.

## FAQ

### How should developers validate Gemini 4 Argon on their own workloads?

Build a representative task set with explicit acceptance criteria. Keep tools, time limits, input preparation and retry policies comparable across models. Record completed tasks, total tokens, elapsed time and human correction. Start with a small pilot and examine failure cases before routing production traffic.

### Can Gemini 4 Argon's benchmark percentages be averaged into one score?

No. The table combines different metrics, including F1, pass rates, and partial scores. Use task-specific criteria rather than averaging all percentages.

### Should a Gemini 4 Argon agent always use its full output budget?

No. Choose the smallest tested budget that meets your quality and reliability requirements. The maximum output limit is a ceiling, not a target.

### How should teams evaluate Gemini 4 Argon access through CometAPI?

Start with an account-level availability check and a small request using the documented CometAPI route. Measure response quality, latency, limits and billed tokens, then apply the same acceptance tests used for alternative models. Treat CometAPI's access claim separately from Google's broader rollout, and keep routing configurable until the route meets your requirements.

---

*Originally published at [https://www.cometapi.com/gemini-4-argon-performance/](https://www.cometapi.com/gemini-4-argon-performance/).*
