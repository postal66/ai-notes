<!-- social-ops-fingerprint:f724d244d0f2ba6c53062318eb67397b91baa02c066ae93c6039c7585cf5aabd -->
---
title: What Is MiniMax M3
---
# What Is MiniMax M3

![What Is MiniMax M3](https://resource.cometapi.com/What%20is%20MiniMax%20M3.png)

## TL;DR

[**MiniMax M3**](https://www.cometapi.com/models/minimax/minimax-m3/) is MiniMax’s frontier model for coding, agentic work, long-context reasoning, and multimodal understanding. It was **officially released on June 1, 2026** and combines three capabilities that MiniMax treated as the center of the release: **up to a 1M-token context window**, native image/video understanding, and long-horizon agent execution.

The open-weight model has **about 428 billion total parameters and about 23 billion activated parameters**. That implies only roughly 5.4% of its disclosed parameter capacity is active on a typical token, helping explain how a very large model can remain practical at inference time. M3 also introduces [**MiniMax Sparse Attention (MSA)**](https://arxiv.org/abs/2606.13392), a blockwise sparse-attention design built for million-token contexts.

For developers, M3 is available through MiniMax’s API and open-weight distribution, and it is also available through [**CometAPI**](https://www.cometapi.com/models/minimax/minimax-m3/) for teams that want one interface for MiniMax and other model providers.

## Key Takeaways

- MiniMax [**released M3 on June 1, 2026**](https://www.minimax.io/blog/minimax-m3) as a frontier model focused on coding, agents, long context, and multimodality.
- The open-weight release discloses [**~428B total parameters and ~23B activated parameters**](https://github.com/MiniMax-AI/MiniMax-M3).
- M3 supports [**up to 1M tokens of context**](https://www.minimax.io/models/text/m3), with MiniMax describing 512K as the guaranteed minimum tier for the API.
- [**MiniMax Sparse Attention**](https://arxiv.org/abs/2606.13392) replaces full global attention with block selection and exact sparse attention over selected context regions.
- M3 was **trained with mixed modalities from Step 0** and supports text, image, and video input.
- Official launch benchmarks include **59.0% SWE-Bench Pro, 66.0% Terminal-Bench 2.1, 83.5 BrowseComp, and 75.2 OSWorld-Verified**.
- MiniMax demonstrated nearly **12 hours of autonomous paper reproduction** and approximately **24 hours of CUDA-kernel optimization with 1,959 tool calls**.
- The API supports configurable reasoning and **text, image, video, function tools, standard/priority service tiers, and long-context pricing**.

## What Is MiniMax M3?

[**MiniMax M3**](https://www.cometapi.com/models/minimax/minimax-m3/) is the successor to the M2 generation and represents a larger architectural shift than a normal point update. [**MiniMax M2.7**](https://www.cometapi.com/models/minimax/minimax-m2-7/) was already positioned around real-world software engineering, office productivity, and agent workflows, but M3 adds a new sparse-attention architecture, native multimodal pretraining, and a million-token context target.

M3 as a **frontier multimodal coding model with a 1M context window**. The official open-weight repository adds the most important scale figures: **approximately 428B parameters in total and 23B activated**. The associated MSA technical report also describes the architecture as operating in a Mixture-of-Experts setting, which is consistent with the disclosed total-versus-active parameter split.

This makes M3 less interesting as “a larger M2.7” and more interesting as a convergence model. It brings together repository-scale context, coding, multimodal perception, computer-oriented agents, and local/open deployment in one system. MiniMax explicitly framed that combination as the release’s main differentiator rather than claiming that M3 wins every benchmark.

### MiniMax M3 Specifications

| Specification | MiniMax M3 |
| --- | --- |
| Release date | June 1, 2026 |
| Model size | ~428B total parameters; ~23B activated |
| Architecture | Sparse Mixture-of-Experts with MiniMax Sparse Attention (MSA) |
| Context window | Up to 1M tokens; API guaranteed minimum 512K |
| Input modalities | Text, image, video |
| Output | Text |
| Reasoning control | Thinking on/adaptive or disabled through API parameters |
| Maximum generation | Recommended 128K; API docs allow up to 512K max\_completion\_tokens |
| Tool use | Function tools; agent-oriented workflows |
| Weights | Open-weight release on Hugging Face / GitHub instructions |

The context, modality, and API behavior above are documented in MiniMax’s [**official model and API documentation**](https://platform.minimax.io/docs/api-reference/text-openai-api); the parameter figures and local-deployment links come from the [**official M3 repository**](https://github.com/MiniMax-AI/MiniMax-M3).

### From MiniMax M2.7 to M3

| Dimension | MiniMax M2.7 | MiniMax M3 |
| --- | --- | --- |
| Context window | 204,800 tokens | Up to 1M tokens |
| Native image/video input | No; M2.x text/tool workflows | Yes; text + image + video |
| Attention direction | Conventional M2-series serving | MSA sparse attention |
| Thinking control | Reasoning cannot be fully disabled in M2.x | Thinking can be disabled for lower latency |
| Primary positioning | Coding, tool calling, office/agent workflows | Coding + agents + multimodality + million-token context |
| Open-weight emphasis | M2.7 open model ecosystem | M3 weights + dedicated MSA implementation |

MiniMax’s API documentation lists [**M2.7 at a 204,800-token context tier**](https://platform.minimax.io/docs/guides/models-intro) while M3 moves to the million-token class. The larger difference is qualitative: M3 accepts visual and video inputs directly, whereas the M2.x API remains text-and-tool oriented.

## What Is New in MiniMax M3?

### A 428B Model with About 23B Parameters Active

The public M3 repository states that the model has [**~428B total parameters and ~23B activated parameters**](https://github.com/MiniMax-AI/MiniMax-M3). In practical terms, the disclosed active fraction is about 5.4%. That is the basic appeal of a sparse expert architecture: total capacity can be very large while the compute path for a given token touches only a fraction of the model.

Parameter count alone does not determine quality, and “428B” should not be read as 428B dense parameters being evaluated for every token. The more useful interpretation is that M3 has a large pool of model capacity paired with conditional activation and an attention system designed to keep long-context cost manageable.

### MiniMax Sparse Attention: Making 1M Context Practical

The central architectural change is [**MiniMax Sparse Attention (MSA)**](https://arxiv.org/abs/2606.13392). Full softmax attention grows quadratically with sequence length, which becomes expensive when agent histories, code repositories, tool logs, images, and long documents accumulate into hundreds of thousands of tokens.

MSA adds a lightweight Index Branch that scores key-value blocks and selects a Top-k subset for each grouped-query attention group. The main branch then performs exact block-sparse attention only on those selected blocks. MiniMax’s technical report describes this as a hardware-oriented design intended to preserve quality while reducing the amount of context that must be processed by full attention.

![What Is MiniMax M3](https://resource.cometapi.com/blog/uploads/2026/08/how%20minimax%20m3%20works.webp)

Figure 1. MiniMax Sparse Attention (MSA) architecture. [*Source: MiniMax official MSA figure*](https://www.minimax.io/blog/minimax-m3)

At 1M context, MiniMax reports that M3 uses **about 1/20 of the previous generation’s per-token compute** and delivers [**more than 9× prefill speedup and more than 15× decoding speedup versus M2**](https://github.com/MiniMax-AI/MiniMax-M3). The separate MSA paper reports additional controlled experiments on a 109B MoE test model, so those paper numbers should not be confused with the production M3-vs-M2 figures.

That distinction matters. The paper validates the attention mechanism in a research setting; the M3 launch numbers describe the production model. The two results point in the same direction, but they are not the same benchmark.

### Native Multimodality from Step 0

M3 is not presented as a text model with a separate visual adapter added at the end. MiniMax says it underwent [**mixed-modality training from Step 0**](https://www.minimax.io/blog/minimax-m3) and rebuilt its pretraining data pipeline to increase interleaved multimodal data.

The production API supports [**text, image, and video input**](https://platform.minimax.io/docs/api-reference/text-openai-api). This matters for coding and agent work because many real tasks are not text-only: debugging may require a screenshot, frontend work may require comparison with a reference image, research may include plots and equations, and computer-use agents operate through visual interfaces.

A useful way to think about M3’s multimodality is therefore not “it can describe an image,” but “visual state can remain inside the same long-running reasoning loop as code, tool output, documents, and user feedback.”

### Interactive Coding and Agent Training

MiniMax argues that classic coding benchmarks are too single-turn to represent how developers actually work. For M3 it built an [**interactive user simulator**](https://www.minimax.io/blog/minimax-m3) that exposes the model to requirement clarification, solution discussion, feedback-based correction, task switching, and multi-round project iteration.

The goal is to move from passive instruction execution toward collaboration. An effective coding agent must be able to decompose a task, call tools, interpret failures, revise a plan, preserve earlier decisions, and continue after the first plausible answer. M3’s long context and tool-oriented training are designed around exactly that loop.

### Long-Horizon Autonomous Execution

MiniMax’s most persuasive M3 demonstrations are not chat examples. They are long-running tasks in which the model must maintain state and continue improving after repeated tool feedback.

| Task | Autonomous runtime | Evidence of persistence | Reported result |
| --- | --- | --- | --- |
| ICLR paper reproduction | Nearly 12 hours | 18 commits; 23 experimental figures | Core experiments reproduced |
| FP8 GEMM kernel optimization | ~24 hours | 147 benchmark submissions; 1,959 tool calls | 7.6% → 71.3% peak utilization; 9.4× speedup |
| PostTrainBench model training | 12-hour task window | Data synthesis → training → evaluation → iteration | Score 0.37; behind Opus 4.7 and GPT-5.5, ahead of other models in MiniMax report |

[In the paper-reproduction task](https://www.minimax.io/blog/minimax-m3), M3 ran **for nearly 12 hours and produced 18 commits plus 23 experimental figures**. The task combined paper reading, chart/formula understanding, code writing, experiments, and iterative interpretation.

![What Is MiniMax M3](https://resource.cometapi.com/blog/uploads/2026/08/filename%20(1).png)

Figure 2. M3’s autonomous paper-reproduction trajectory over roughly 12 hours. [*Source: MiniMax official M3 demonstration*](https://www.minimax.io/blog/minimax-m3)

[In the CUDA optimization task](https://www.minimax.io/blog/minimax-m3), M3 completed **147 benchmark submissions and 1,959 tool calls over roughly 24 hours**, ultimately increasing reported Hopper FP8 peak utilization from **7.6% to 71.3% for a 9.4× speedup** with no human intervention. The notable point is not just the final speedup; MiniMax says the model’s best solution appeared on its 145th submission, after several plateaus.

## Benchmark Performance of MiniMax M3

MiniMax’s launch benchmark chart compares M3 with [**Claude Opus 4.7**](https://www.cometapi.com/models/anthropic/claude-opus-4-7/), [**GPT-5.5**](https://www.cometapi.com/models/openai/gpt-5-5/), and [**Gemini 3.1 Pro**](https://www.cometapi.com/models/google/gemini-3-1-pro/) across coding, terminal, browsing, office, tool-use, and computer-use tasks. These are the most useful direct comparisons because they were published in the same M3 release package.

![minimax m3](https://resource.cometapi.com/blog/uploads/2026/08/minimax%20%20m3.webp)

Figure 3. MiniMax’s official M3 launch benchmark comparison. [*Source: MiniMax official benchmark image*](https://www.minimax.io/blog/minimax-m3)

| Benchmark | MiniMax M3 | Claude Opus 4.7 | GPT-5.5 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- |
| SWE-Bench Pro | 59.0 | 64.3 | 58.6 | 54.2 |
| Terminal-Bench 2.1 | 66.0 | 66.1 | 78.2 | 70.0 |
| VIBE V2 | 50.1 | 55.8 | 50.5 | 28.0 |
| SVG-Bench | 63.7 | 62.3 | 58.2 | 59.2 |
| KernelBench Hard | 28.8 | 30.7 | 20.9 | 18.6 |
| BrowseComp | 83.5 | 79.3 | 84.4 | 85.9 |
| GDPval rubrics | 74.7 | 79.8 | 80.6 | 57.8 |
| BankerToolBench | 76.1 | 81.3 | 75.0 | 67.0 |
| MCP Atlas | 74.2 | 77.0 | 75.3 | 69.2 |
| OSWorld-Verified | 75.2 | 82.8 | 78.7 | 76.2 |

All scores in this table are transcribed from [**MiniMax’s official M3 launch chart**](https://www.minimax.io/blog/minimax-m3). They should be read as vendor-reported launch results, not as a new independent rerun performed by CometAPI.

### What the Benchmark Results Actually Show

First, M3 is genuinely competitive in software engineering. On SWE-Bench Pro it scores 59.0, above the 58.6 and 54.2 values MiniMax reports for GPT-5.5 and Gemini 3.1 Pro, but below Claude Opus 4.7 at 64.3. KernelBench Hard tells a similar story: M3 at 28.8 is close to Opus 4.7 at 30.7 and substantially above the other two values in MiniMax’s chart.

Second, terminal execution is not M3’s strongest relative result. Terminal-Bench 2.1 places M3 at 66.0, essentially tied with Opus 4.7 at 66.1 but well behind GPT-5.5 at 78.2 and Gemini 3.1 Pro at 70.0.

Third, M3 is strong but not dominant on information gathering. BrowseComp is 83.5: higher than Opus 4.7’s 79.3, but slightly below GPT-5.5 at 84.4 and Gemini 3.1 Pro at 85.9. MCP Atlas at 74.2 also sits close to GPT-5.5’s 75.3 and Opus 4.7’s 77.0.

Fourth, the launch chart gives M3 a particularly good result on SVG-Bench: 63.7 versus 62.3 for Opus 4.7, 58.2 for GPT-5.5, and 59.2 for Gemini 3.1 Pro. That fits the broader M3 design: native visual understanding is intended to participate directly in coding and agent workflows rather than remain a separate vision feature.

The overall conclusion is therefore more nuanced than “M3 beats closed models.” M3 enters the same performance band on many agentic tasks, wins selected evaluations, and loses others. Its differentiator is what accompanies those scores: open weights, multimodal training, a million-token context design, and aggressive serving economics.

## **MiniMax M3 vs Claude Opus 5 vs GPT-5.6 Sol vs Gemini 3.7 Flash**

MiniMax M3 launched into a fast-moving market, and its original comparison set is no longer the most useful reference point. A more relevant current-generation comparison is Claude Opus 5, GPT-5.6 Sol, and Gemini 3.7 Flash—newer closed models aimed at coding, agents, and multimodal work. Because these models are not evaluated under one identical harness, the table emphasizes documented capabilities and uses benchmark figures only where the metric is directly reported.

| Dimension | MiniMax M3 | Claude Opus 5 | GPT-5.6 Sol | Gemini 3.7 Flash |
| --- | --- | --- | --- | --- |
| Weights | Open weight | Closed | Closed | Closed / hosted API |
| Public parameter count | ~428B total / ~23B active | Not disclosed | Not disclosed | Not disclosed |
| Context window | Up to 1M | 1M | 1,050,000 | 1M |
| Input modalities | Text, image, video | Text, image, PDF | Text, image | Text, image, video, audio, PDF |
| Coding / agent focus | Coding + long-horizon agents + multimodality | Complex agentic coding + enterprise work | Frontier coding + tool-heavy professional agents | Fast agentic coding + multimodal workflows |
| Computer / tool use | Function tools + MiniMax Code + computer use | Server/client tools + computer use | Web/file search, shell, computer use, MCP | Function calling, search, computer use |
| Terminal-Bench 2.1\* | 66.0 | Not reported in Opus 5 launch | 88.8 | 85.8 |
| Representative coding signal\* | SWE-Bench Pro 59.0 | Frontier-Bench v0.1: SOTA in Anthropic report | DeepSWE v1.1 72.7 | DeepSWE v1.1 65.3 |
| Best reason to choose | Open weights + low cost + 1M multimodal context | Judgment + long-horizon autonomy | Raw coding/terminal performance + broad tool stack | Speed/cost + native multimodality |

These benchmark figures come from different provider evaluation packages and should not be read as a single synchronized leaderboard. [M3’s 66.0 Terminal-Bench 2.1 score](https://www.minimax.io/blog/minimax-m3) comes from MiniMax’s release evaluation; [OpenAI reports 88.8 for GPT-5.6 Sol](https://openai.com/index/gpt-5-6/), while [Google reports 85.8 for Gemini 3.7 Flash](https://deepmind.google/models/gemini/flash/). [Anthropic’s Opus 5 launch emphasizes Frontier-Bench, GDPval-AA, AutomationBench, and OSWorld 2.0](https://www.anthropic.com/news/claude-opus-5) rather than publishing a directly comparable Terminal-Bench 2.1 result. For model selection, benchmark the candidates under one harness on your own workload rather than treating cross-provider launch figures as a permanent ranking.

### Where MiniMax M3 Has the Clearest Advantage

The clearest M3 advantage is deployment choice. Neither the benchmark chart nor parameter count alone explains why developers may care about the model. M3 combines open weights with a context length and multimodal capability set normally associated with hosted frontier systems. That makes it attractive when teams need local deployment, provider independence, specialized serving, or deep control over the inference stack.

Its second advantage is long-context cost architecture. MSA is explicitly designed to keep attention compute from exploding at million-token scale. This does not make 1M-token requests cheap in an absolute sense—KV cache, expert execution, and multimodal inputs still cost resources—but it changes the scaling curve compared with full attention.

### Where Closed Models Still Lead

The same official benchmark chart shows why M3 should not be presented as an automatic replacement for every closed frontier model. Claude Opus 4.7 has stronger results on SWE-Bench Pro, KernelBench Hard, GDPval, BankerToolBench, MCP Atlas, and OSWorld-Verified in MiniMax’s own comparison. GPT-5.5 is much stronger on Terminal-Bench 2.1 and leads GDPval. Gemini 3.1 Pro slightly leads BrowseComp.

For production teams, closed platforms may also provide mature safety controls, hosted tools, observability, throughput guarantees, and integrations that matter more than open weights. M3 becomes most compelling when the deployment and cost benefits are part of the requirement, not when benchmark rank is the only criterion.

## MiniMax M3 API Pricing

MiniMax currently uses two standard context-price tiers. Its [official pricing page](https://platform.minimax.io/docs/guides/pricing-paygo) displays a **“permanent 50% off” rate of $0.30/M input and $1.20/M output for requests at or below 512K input tokens**. Requests above 512K are shown at **$0.60/M input and $2.40/M output**. Priority service is priced at 1.5× the standard tier.

| Route / tier | Input price per 1M tokens | Output price per 1M tokens | Context note |
| --- | --- | --- | --- |
| MiniMax official Standard (current discounted rate) | $0.30 | $1.20 | ≤512K input |
| MiniMax official Standard long-context | $0.60 | $2.40 | >512K input |
| MiniMax official Priority (discounted rate) | $0.45 | $1.80 | ≤512K input; priority admission |
| CometAPI MiniMax-M3 page | $0.48 | $1.92 | Unified gateway pricing shown by CometAPI |

*\**[*CometAPI’s MiniMax-M3*](https://www.cometapi.com/models/minimax/minimax-m3/)  is $0.48/M input and $1.92/M output and compares that with MiniMax’s non-discounted list rate of $0.60/$2.40. Because MiniMax’s own platform is presently displaying a separate 50%-off standard rate, developers should compare the actual live rate they will be billed rather than relying only on a headline discount percentage.

The reason to use CometAPI in this situation is therefore not necessarily the lowest direct promotional price at every moment. Its value is a unified API and billing layer when an application needs to route among M3 and other providers without maintaining separate integrations.

## What Can MiniMax M3 Do?

### Coding and Repository-Scale Engineering

M3’s most obvious use case is software engineering across large repositories. A million-token context can hold far more code, documentation, test output, issue history, and agent state than the 204.8K window of the prior M2 generation. In practice, that enables workflows such as multi-file feature implementation, repository-wide refactoring, bug diagnosis, test repair, build/terminal loops, pull-request review, and performance optimization.

The key is persistence. A repository-scale coding agent is useful only if it can retain the original requirements while accumulating tool output and revisions. The 12-hour and CUDA demonstrations suggest that M3 is designed to keep working after intermediate failures rather than treat each tool call as a separate short task.

### Autonomous Research and Experimentation

The paper-reproduction example is a good template for research agents. M3 can read a paper, inspect figures, reason about formulas, generate code, run experiments, evaluate whether results match expectations, and continue refining the implementation. The ability to keep paper text, code, and experimental logs in one long context reduces the amount of state that must be summarized or externally reconstructed.

This is also why PostTrainBench is relevant. MiniMax asked M3 to synthesize training data, train base models, evaluate them, and iterate without human intervention. M3 did not rank first—it finished behind Opus 4.7 and GPT-5.5 in MiniMax’s report—but the experiment demonstrates a form of research automation that is more complex than ordinary question answering.

### Multimodal Technical Analysis

Because M3 accepts images and video natively, technical workflows can combine visual evidence with text and code. Examples include comparing a frontend implementation against a screenshot, analyzing plots inside a research paper, inspecting UI state during computer use, extracting information from diagrams, or combining video observations with a long maintenance log.

MiniMax’s OpenAI-compatible API documentation explicitly supports [**image\_url and video\_url content parts for M3**](https://platform.minimax.io/docs/api-reference/text-openai-api), including uploaded files for larger videos. This makes multimodal input a developer-facing API feature rather than only a product demo.

### Computer and Office Automation

MiniMax Code is designed as an agent harness around M3. The company says its Agent Team can split complex tasks into multi-stage concurrent workflows and use a Producer + Verifier loop for reflection and correction. M3’s native multimodality also allows computer-use workflows that move across applications, files, spreadsheets, and desktop interfaces.

One official example is an instruction to open a local ERP client and batch-enter invoice information from an Excel spreadsheet. The important capability is cross-application state: the agent needs to understand the spreadsheet, operate the interface, preserve mapping between fields, and recover if the UI changes or an action fails.

### Long-Context Document and Knowledge Work

A 1M context window is useful for more than code. It can support large collections of contracts, policies, technical specifications, research papers, incident reports, or customer records in a single working context. The advantage is not simply “more pages”; it is the ability to reason across distant evidence while preserving a long agent history.

There is still a practical caution: maximum context capacity does not guarantee perfect recall at every position, and very large prompts increase latency and cost. Long context should be paired with retrieval, caching, structured memory, or task segmentation when those approaches improve reliability.

## Final Verdict: Is MiniMax M3 a Frontier Model?

Yes—but the strongest case for that label is not that M3 tops every chart. It does not.

What [**MiniMax M3**](https://www.cometapi.com/models/minimax/minimax-m3/) M3 changes is the trade-off. It offers competitive launch-era frontier performance while also providing open weights, a million-token sparse-attention design, native text-image-video training, long-horizon agent behavior, and much lower per-token API pricing than the closed flagship models in its original comparison set.

## SEO信息

**Suggested URL:** `/blog/minimax-m3-specs-benchmarks-pricing`

**Description:** Explore MiniMax M3’s specs, 1M-token context, sparse attention, multimodal capabilities, benchmark performance, API pricing, use cases, and model comparisons.

**Keywords:** MiniMax M3, MiniMax M3 specs, MiniMax M3 benchmarks, MiniMax M3 API pricing, MiniMax Sparse Attention, 1M-token context window, multimodal coding model, open-weight AI model, long-horizon AI agents, MiniMax M3 vs GPT-5.5

---

*Originally published at [https://www.cometapi.com/what-is-minimax-m3/](https://www.cometapi.com/what-is-minimax-m3/).*
