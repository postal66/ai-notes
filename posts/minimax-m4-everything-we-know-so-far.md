<!-- social-ops-fingerprint:632e4546e6b729030b0ea22becbcb06bc5b89294a5aa5c97cf5a5720fbfa421d -->
---
title: MiniMax M4: Everything We Know So Far
---
# MiniMax M4: Everything We Know So Far

![MiniMax M4: Everything We Know So Far](https://resource.cometapi.com/minimax%20m4.webp)

**TLDR** MiniMax M4 has not been released. MiniMax has publicly committed to a new generation of its M-series (and Hailuo video) models in the second half of 2026. The current flagship remains MiniMax M3 (launched June 1, 2026: ~428B total / ~23B active parameters, 1M-token context via MiniMax Sparse Attention, native multimodal, open weights, 59.0% on SWE-Bench Pro).

A mid-cycle efficiency refresh, Minimax [M3.1 Flash](https://www.cometapi.com/models/minimax/minimax-m3-1-flash-preview/), launched October 19, 2026, delivering roughly 3× faster inference and ~70% lower agentic costs. Developers can already access the live MiniMax lineup (including M3 and M3.1 Flash) through unified gateways such as CometAPI for simplified routing, monitoring, and cost control.

## Key Takeaways

- MiniMax M4 is **not released** as of October 20, 2026. The company has only committed to “a new generation of M-series and Hailuo models in the second half of 2026.”
- Current production models: **MiniMax M3** (June 1, 2026) and the efficiency-focused **M3.1 Flash** (October 19, 2026).
- M3 introduced MSA (MiniMax Sparse Attention) enabling practical 1M-token context, native image/video understanding, strong coding/agent scores, and open weights.
- M3.1 Flash prioritizes speed and cost (claimed ~3× inference speedup and 70% lower agentic costs) while retaining the 1M context and multimodal inputs; open weights are expected shortly after launch.
- A July 2026 report described an internal ~2.7-trillion-parameter effort (internally called M3 Pro) with possible open-weight release targeted as early as Q3 2026; this has not materialized publicly and is distinct from the broader “new generation” commitment.
- Expected M4 improvements (speculative, based on trajectory): further coding/agent gains, refined long-context efficiency, stronger multimodal or computer-use capabilities, and continued aggressive pricing.
- Access recommendation: Use a multi-provider gateway such as **CometAPI** to route traffic across MiniMax M3/M3.1 Flash (and future M4) alongside other frontier models with unified billing, observability, and fallback logic.

## Is MiniMax M4 Really Coming Soon?

### Confirmed Information

The main question is not whether MiniMax is developing future AI systems, but whether there is concrete evidence that a model named MiniMax M4 is approaching release.

MiniMax released M3 in June 2026 and formally launched M3.1 Flash on October 19, 2026. This is a confirmed intermediate release, not proof of an M4 schedule. [Official launch announcement](https://www.minimax.io/blog/minimax-m31f).

The [official research archive](https://www.minimax.io/blog) now includes M3.1 Flash. No M4 launch announcement was found in the official sources reviewed on October 20, 2026.

| Evidence category | Finding | Assessment |
| --- | --- | --- |
| Official M4 announcement | Not verified | Unconfirmed |
| Public M4 model identifier | Not verified | Unconfirmed |
| Leaked M4 benchmark screenshot | No independently verified evidence found | Unconfirmed |
| M4 API endpoint | Not verified | Unconfirmed |
| M4 pricing | Not published | Unknown |
| M4 model weights | Not verified | Unknown |
| MiniMax M3 launch | June 1, 2026 | Confirmed |
| M3.1 Flash release | Released October 19, 2026; available through MiniMax API, M Plan and MiniMax Code | Confirmed |

### Community Reports / Leaks

Two X posts dated September 27, 2026 discuss a possible M4 release. They establish that these claims were circulating in the community, not that MiniMax has confirmed them. Both are treated here as unverified community reports; neither author's paid verification badge establishes the accuracy of the claims.

In a [post by @0x0SojalSec](https://x.com/0x0SojalSec/status/2104328025378832779), the author suggests a roughly three-trillion-parameter model, an open-weight release, and training on Huawei Ascend hardware. The readable excerpt also describes a loop in which the model participates in its own training and evaluation. These are claims made by the poster, not verified M4 specifications.

![MiniMax M4: Everything We Know So Far](https://resource.cometapi.com/blog/uploads/2026/10/MiniMax%20M4%20Leak%20.webp)

A [post by Priya (@Priyannkaaaa)](https://x.com/Priyannkaaaa/status/2104060742630797528/photo/1)suggests a possible October-November 2026 release and a parameter count exceeding three trillion. It also makes an unverified claim about the preceding M3 model's size. That comparison is not adopted as a factual baseline in this article.

![MiniMax M4: Everything We Know So Far](https://resource.cometapi.com/blog/uploads/2026/10/MiniMax%20M4%20Leak%20Could%20Beat%20Fable%205.1.webp)

## When Could MiniMax M4 Be Released?

Earlier models remain useful reference points, including [MiniMax M2.5 API in CometAPI](https://www.cometapi.com/models/minimax/minimax-m2-5/). Their dates establish history, not a forecast of the next release.

MiniMax has not confirmed an M4 launch date. The October-November 2026 window mentioned in Priya's community post is a rumor, not an official schedule; the underlying excerpt and its limitations are discussed in Community Reports / Leaks. The model family’s release history shows both major generations and intermediate versions, but past launch intervals cannot reliably predict the next model’s release.

| Milestone | Official release timeline | Significance |
| --- | --- | --- |
| MiniMax M2.5 | February 12, 2026 | Coding and productivity |
| MiniMax M2.7 | March 18, 2026 | Agent workflow improvements |
| MiniMax M3 | June 1, 2026 | 1M context and multimodality |
| M3.1 Flash | October 19, 2026 — official release | Released efficiency-focused coding and agent model |
| MiniMax M4 | Not announced | No verified timeline |

A formal MiniMax product announcement would be the strongest signal. API documentation or an authenticated model identifier would provide additional support. Benchmark results and public model cards would make it possible to assess technical improvements, while official pricing and rate limits would determine production viability.

## MiniMax M4 Price — What the Leaks and Prior Generations Suggest

No official pricing exists for M4. All figures below are extrapolations from the live M3 and M3.1 Flash rate cards (USD, per million tokens, approximate as of mid-October 2026):

| Model | Input / 1M | Output / 1M | Cached Input | Context | Notes |
| --- | --- | --- | --- | --- | --- |
| MiniMax M3 | $0.30 | $1.20 | ~$0.06 | 1M | “Permanent 50% off” list pricing; higher tier for >512k context |
| MiniMax M3.1 Flash | $0.15 | $0.60 | $0.015 | 1M | ~50% cheaper than M3; optimized for agent throughput |
| Expected M4 range (speculative) | $0.20–$0.40 | $0.80–$1.50 | Similar discount structure | 1M+ | Likely remains among the lowest frontier open-weight offerings |

Sources for current pricing: MiniMax platform documentation, independent aggregators, and launch announcements.

MiniMax has repeatedly positioned its models at a fraction of the cost of leading closed-source Western models while matching or exceeding them on selected coding and agent benchmarks. A full M4 would be expected to continue this strategy, with possible premium tiers for extended context, priority latency, or higher reasoning effort.

**CometAPI recommendation**: Rather than managing multiple MiniMax API keys and rate cards directly, route through a unified gateway such as CometAPI. This allows seamless switching between M3, M3.1 Flash, and (when available) M4, automatic fallbacks, usage analytics, and often better effective pricing via volume aggregation—especially valuable for agentic workloads that burn large numbers of tokens.

## What MiniMax M3.1 Flash Reveals About the Next Generation

MiniMax M3.1 Flash provides a more current reference point for evaluating what a future MiniMax M4 model might deliver. Officially introduced on October 19, 2026, M3.1 Flash focuses on agentic workflows, software development, computer use, and cybersecurity, while emphasizing faster inference and lower usage costs. These improvements offer useful clues about MiniMax's current engineering priorities, although they do not establish an M4 release date or confirm its future specifications.

### 1. Agent Reliability Is Becoming as Important as Raw Intelligence

One of the clearest themes in the M3.1 Flash announcement is the emphasis on completing complex, multi-step tasks. MiniMax reports improvements across agentic workflows, coding, computer use, and enterprise automation.

This direction suggests that the next generation of models may be judged less by isolated question-answering performance and more by their ability to complete entire workflows reliably.

For example, a software engineering agent may need to inspect a repository, identify a defect, modify several files, execute tests, diagnose failures, and verify the final patch. Success depends not only on reasoning quality but also on tool selection, state tracking, error recovery, and consistency across multiple steps.

A future M4 model could build on this direction by improving long-horizon planning, reducing unnecessary tool calls, and recovering more effectively from failed actions. These are reasonable evaluation targets, not confirmed M4 features.

### 2. Inference Efficiency Could Become a Major Competitive Advantage

MiniMax reports that M3.1 Flash delivers nearly three times the online inference speed of its predecessor and reduces overall usage costs by 70% for agentic tasks. The company also attributes its efficiency improvements to more aggressive sparsity.

These claims highlight an important distinction between model intelligence and practical operating efficiency. A model that completes a task with fewer retries, lower latency, and less token consumption may be more valuable than a model that achieves a slightly higher benchmark score but requires substantially more resources.

For a potential M4 release, the relevant questions will include whether it can sustain high throughput on long-running tasks, preserve output quality under tighter inference budgets, and reduce the total cost of successful task completion.

The reported M3.1 Flash improvements are company claims and should be independently evaluated under comparable workloads before being treated as general performance guarantees.

### 3. Coding and Computer Use Are Important Areas to Watch

[The M3.1 Flash announcement](http://MiniMax%20M3.1%20Flash:%20General%20Availability%20and%20Evaluation%20Guide) reports a score of 73.7% on DeepSWE v1.1, 61.7 on OSWorld V2, and 82% on CyberGym. These results cover different aspects of software engineering, computer interaction, and cybersecurity, respectively.

Together, they provide a more useful starting point for evaluating future models than a single general-purpose benchmark.

If MiniMax introduces M4, developers should look for evidence that it improves practical task completion rather than merely producing a higher headline score. Useful tests could include repository-level bug fixes, cross-application workflows, browser automation, vulnerability analysis, and recovery from failed tool calls.

Benchmark comparisons should preserve the dataset version, execution environment, agent scaffold, resource limits, and scoring methodology. Without comparable conditions, differences between model scores may not reflect genuine capability improvements.

### 4. Long Context and Multimodal Reasoning Still Need Practical Evaluation

MiniMax M3 already supports a context window of up to one million tokens and native multimodal inputs, including images and video. The M3.1 Flash release retains a one-million-token context window and combines multimodal understanding with stronger agent-oriented capabilities.

This means that a larger context window alone would not necessarily be a compelling reason to upgrade to M4.

More meaningful advances could include better retrieval from large repositories, stronger consistency across lengthy documents, more accurate interpretation of visual evidence, and more reliable coordination between perception and tool execution.

For instance, a development agent might need to inspect a screen recording, identify a user-interface failure, trace the relevant application code, implement a fix, and verify the result. The quality of the complete workflow matters more than the model's ability to process a large input in isolation.

These scenarios represent possible evaluation priorities for M4, not capabilities that MiniMax has announced.

### 5. Future Model Releases May Be Evaluated by Cost per Completed Task

The M3.1 Flash announcement reinforces the importance of evaluating model economics at the workflow level. Token prices alone do not capture the full cost of using an agent.

A more useful comparison considers the probability of completing a task successfully, the number of attempts required, token consumption, tool costs, latency, and human intervention.

Developers preparing for a future M4 release should establish a baseline with currently available models and use the same task set to compare subsequent releases. This makes it possible to determine whether a new model delivers meaningful improvements in productivity rather than simply changing benchmark rankings.

## How Strong Are MiniMax M3 Benchmarks, and What Would M4 Need to Beat?

MiniMax published a substantial set of benchmark results for M3, providing measurable targets for a future model. The following values are reported M3 results, not M4 predictions.

| Benchmark | MiniMax M3 reported score | What it evaluates | M4 verification target |
| --- | --- | --- | --- |
| SWE-Bench Pro | 59.0% | Real-world software engineering | Higher verified task resolution |
| Terminal-Bench 2.1 | 66.0% | Terminal-based agent execution | More successful end-to-end operations |
| SWE-fficiency | 34.8% | Coding task efficiency | Better performance under comparable budgets |
| KernelBench Hard | 28.8% | GPU kernel optimization | More correct and faster kernels |
| MCP Atlas | 74.2% | Tool-oriented and MCP tasks | Better tool selection and execution |

These are vendor-reported results from the June 1, 2026 launch announcement, not independent replications. The suites measure different outcomes, so their percentages must not be averaged into a single accuracy score.

### Coding and Software Engineering Performance

**What we have confirmed (M3)**

- SWE-Bench Pro: 59.0%
- Terminal-Bench 2.1: 66.0%
- Strong results on real-world bugfix, frontend/backend development, and kernel optimization tasks (internal MiniMax evaluations showed multi-hour autonomous iteration).

**What M3.1 Flash adds**: Claims of further gains on coding, agentic, and cybersecurity benchmarks, plus dramatically higher tokens-per-second and lower cost per completed agent trajectory.

**What remains unconfirmed / expected for M4**: Higher absolute scores on SWE-Bench-style and multi-turn interactive coding benchmarks, better long-horizon project management, and improved ability to maintain consistency across multi-file, multi-day sessions. Any 2.7T-scale model (if released) would be expected to raise the capability ceiling further, though active-parameter count and sparsity will determine real-world cost.

### Long-Context Efficiency and Architecture

**Confirmed**: M3 introduced MSA (MiniMax Sparse Attention), delivering practical 1M-token context with claimed 1/20th the per-token compute of the prior dense-attention generation, >9× prefilling and >15× decoding speedups at extreme lengths, while matching full attention on most capabilities.

**Expected improvements**: Refinements to sparsity patterns, better support for even longer contexts or denser retrieval within the window, lower memory footprint for self-hosting, and improved handling of interleaved multimodal long documents.

### Multimodal and Computer-Use Capabilities

**Confirmed**: Native image and video understanding from the first training stages, plus demonstrated computer-use (desktop operation) in MiniMax Code and agent harnesses.

**Expected for M4**: Tighter integration of video understanding with agent planning, stronger document/screenshot-to-code pipelines, and more reliable multi-application computer control over longer horizons.

### Agentic Workflows, Tool Use, and Self-Improvement

**Confirmed**: M2.7 already experimented with recursive self-improvement loops. M3 and M3.1 Flash emphasize multi-agent collaboration, dynamic tool search, long-running autonomous tasks, and producer-verifier loops inside MiniMax Code.

**Expected**: More robust multi-day agent teams, better recovery from tool failures, native support for larger tool ecosystems, and possibly continued self-improvement or evolutionary search techniques at greater scale.

## MiniMax M4 Price — What the Leaks and Prior Generations Suggest

No official pricing exists for M4. All figures below are extrapolations from the live M3 and M3.1 Flash rate cards (USD, per million tokens, approximate as of mid-October 2026):

| Model | Input / 1M | Output / 1M | Cached Input | Context | Notes |
| --- | --- | --- | --- | --- | --- |
| MiniMax M3 | $0.30 | $1.20 | ~$0.06 | 1M | “Permanent 50% off” list pricing; higher tier for >512k context |
| MiniMax M3.1 Flash | $0.15 | $0.60 | $0.015 | 1M | ~50% cheaper than M3; optimized for agent throughput |
| Expected M4 range (speculative) | $0.20–$0.40 | $0.80–$1.50 | Similar discount structure | 1M+ | Likely remains among the lowest frontier open-weight offerings |

MiniMax has repeatedly positioned its models at a fraction of the cost of leading closed-source Western models while matching or exceeding them on selected coding and agent benchmarks. A full M4 would be expected to continue this strategy, with possible premium tiers for extended context, priority latency, or higher reasoning effort.

**CometAPI recommendation**: Rather than managing multiple MiniMax API keys and rate cards directly, route through a unified gateway such as CometAPI. This allows seamless switching between M3, M3.1 Flash, and (when available) M4, automatic fallbacks, usage analytics, and often better effective pricing via volume aggregation—especially valuable for agentic workloads that burn large numbers of tokens.

## MiniMax M3 vs M3.1 Flash vs Expected M4 Direction

| Dimension | M3 API in CometAPI (Jun 2026) | MiniMax M3.1 Flash (Oct 2026) | Expected M4 Direction (H2 2026+) |
| --- | --- | --- | --- |
| Status | Live, open weights | Live, weights imminent | Not released |
| Parameters (approx.) | 428B total / ~23B active | Similar scale | Unknown (possible larger MoE) |
| Context | 1M tokens (MSA) | 1M tokens | 1M+ with further efficiency |
| Coding (SWE-Bench Pro) | 59.0% | Claimed further gains | Higher absolute scores expected |
| Inference speed | Strong baseline | ~3× faster claimed | Further optimization |
| Agentic cost | Competitive | ~70% lower claimed | Continued aggressive pricing |
| Multimodal | Native image + video | Same + refined | Deeper integration |
| Open weights | Yes | Planned soon | Highly likely |
| API price (in/out) | $0.30 / $1.20 | $0.15 / $0.60 | Expected $0.20–0.40 / $0.80–1.50 range |

### Model Selection by Developer Workflow

Use released M3.1 Flash as a current evaluation candidate and retain M3 and any established M2.7 workflow for comparison. Measure accepted task completion, retries, human interventions and total cost on the same workload. Adjust effort deliberately rather than assuming that maximum thinking is always the best operating point.

M4 is not yet an actionable production choice. The most useful preparation is to build a reproducible benchmark suite against existing models so that a future release can be evaluated quickly.

## How to Access Current MiniMax Models (and Prepare for M4)

While waiting for M4, the practical path is to use the live models:

1. Obtain a MiniMax API key from the official platform.
2. Or, for production reliability, route through a multi-model gateway such as **CometAPI**. CometAPI provides a single endpoint and key that can target MiniMax M3, M3.1 Flash, and other providers, with built-in usage dashboards, rate-limit handling, and the ability to switch models without code changes.
3. For coding agents, pair the model with MiniMax Code (desktop/CLI) or open frameworks that already support Anthropic- or OpenAI-compatible MiniMax endpoints.
4. Monitor official MiniMax channels and aggregator catalogs; the moment a new M-series model ID appears, gateways like CometAPI typically surface it quickly.

This approach minimizes lock-in and lets teams evaluate M3 vs M3.1 Flash (and eventually M4) on real workloads with consistent observability.

## Conclusion

MiniMax M4 remains a future model defined by a clear but high-level company commitment rather than concrete specifications. The M3 generation already established MiniMax as a serious open-weight contender in coding, agents, and long-context multimodal work; M3.1 Flash then pushed the efficiency frontier. Whatever form the H2 2026 “new generation” ultimately takes—whether labeled M3.5, M4, or something else—it will inherit a strong foundation of sparse attention, open weights, and aggressive pricing.

For developers and teams building production agents today, the actionable recommendation is straightforward: integrate the live MiniMax models (M3 and M3.1 Flash) through a flexible multi-provider layer such as CometAPI. This delivers immediate capability and cost advantages while positioning you to adopt M4 the moment it appears on public endpoints—with minimal code changes and full visibility into performance and spend.

---

*Originally published at [https://www.cometapi.com/minimax-m4-everything-we-know-so-far/](https://www.cometapi.com/minimax-m4-everything-we-know-so-far/).*
