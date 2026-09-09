<!-- social-ops-fingerprint:279ea61ea14b52c4deabe4a6a9c9579a53934b05707a8a13e2c79638099bfc13 -->
---
title: What is Qwen3.8-Flash-Next
---
# What is Qwen3.8-Flash-Next

![What is Qwen3.8-Flash-Next](https://resource.cometapi.com/What%20is%20Qwen3.8-Flash-Next.webp)

[**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) is not simply a smaller or faster member of the Qwen3.8 family. Qwen describes it as an **open-weight multimodal MoE model and an early preview of the architecture used in Qwen4**. Its design changes attention, residual connections, embedding capacity, and optimization at the same time, with the goal of improving capability while sharply reducing the amount of compute required per token.

## TL;DR

[**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) combines a 125B-parameter main model with an additional 51B N-gram embedding table, while [**activating only 6B parameters per token**](https://qwen.ai/blog?id=qwen3.8-flash-next). It natively handles 262,144 tokens and can be extended to 1,000,000 tokens with YaRN. The architecture is built around a 3:1 mix of Gated DeltaNet and Qwen Sparse Attention, four-branch Gated Residual connections, N-gram Embedding, a large ultra-sparse MoE expert pool, Multi-Token Prediction, and Muon-based training.

The most important point is efficiency rather than raw parameter count. Qwen reports that training the model requires [**about one-ninth the cost of Qwen3.7-Plus**](https://qwen.ai/blog?id=qwen3.8-flash-next), yet its launch evaluation places the model ahead of the previous Qwen baselines on many coding, office-agent, and multimodal tasks. These are vendor-reported results and should be read as launch evidence rather than independent validation.

For developers, the open weights are available through Qwen channels, while the managed production version is called Qwen3.8-Flash on QwenCloud. [**CometAPI lists Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) with the model ID **qwen3.8-flash-next**, giving developers a unified route alongside other frontier models.

## **Key Takeaways**

- [**125B main-model parameters + 51B N-gram embedding**](https://qwen.ai/blog?id=qwen3.8-flash-next), with 6B active parameters per token.
- A [**3 GDN : 1 QSA hybrid attention pattern**](https://qwen.ai/blog?id=qwen3.8-flash-next) is designed to combine efficient memory with precise long-range retrieval.
- [**262,144-token native context**](https://qwen.ai/blog?id=qwen3.8-flash-next) and up to 1M tokens through YaRN.
- Qwen reports up to [**7.6x prefill and 4.9x decode kernel speedups at 1M context**](https://qwen.ai/blog?id=qwen3.8-flash-next) for QSA.
- The residual stream is widened into [**four gated branches**](https://qwen.ai/blog?id=qwen3.8-flash-next), improving cross-layer information flow and training stability.
- The official launch table shows strong results in SWE-bench Pro, CoWorkBench, JobBench, Toolathlon, AndroidWorld, and RealWorldQA, but not a clean sweep across every benchmark.
- Qwen positions the release as an architecture preview, so its importance is partly about what the design signals for Qwen4 rather than only its current benchmark rank.

## What Is Qwen3.8-Flash-Next?

[**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) is a causal multimodal language model with a vision encoder and an ultra-sparse Mixture-of-Experts language backbone. The official model card describes a [**48-layer architecture with 512 experts, 10 routed experts plus one shared expert**](https://huggingface.co/Qwen/Qwen3.8-Flash-Next), and a hidden layout that repeats three Gated DeltaNet layers followed by one Qwen Sparse Attention layer.

The release plays a role similar to Qwen3-Next: it exposes architectural changes before they are scaled into the next full family. Qwen explicitly calls the model [**an experimental preview of the architecture that will underpin Qwen4**](https://huggingface.co/Qwen/Qwen3.8-Flash-Next). That makes the model unusually interesting for engineers who care about serving efficiency, long context, and the direction of open-model architecture research.

## 4 core components of Qwen3.8-Flash-Next

The model changes four core components together: attention, residual flow, embedding capacity, and optimization. That co-design matters because efficiency gains in one component can be lost if another component becomes the bottleneck at long context or large scale.

### Hybrid Attention: GDN + Qwen Sparse Attention

Most layers do not perform global attention. Instead, [**three out of every four layers use Gated DeltaNet**](https://qwen.ai/blog?id=qwen3.8-flash-next) to compress historical information into a fixed-size state. The fourth layer uses global attention for exact retrieval, but that global attention is redesigned as Qwen Sparse Attention (QSA).

QSA avoids searching every token independently. A lightweight indexer first groups the sequence into micro-blocks, estimates which blocks matter, and then attends only to selected regions. In Qwen's description, this reduces both the attention computation and the indexing overhead needed to find relevant context. The design is especially compatible with a hybrid network because the sparse index is built independently within each attention layer rather than relying on similarity between adjacent attention layers.

The efficiency numbers are substantial. At a 1M-token context, Qwen reports [**up to 7.6x faster prefill and 4.9x faster decode for the QSA attention kernel**](https://qwen.ai/blog?id=qwen3.8-flash-next). In a high-cache-reuse serving experiment with a 90% prefix-cache hit rate, the full model reaches [**8.6x the prefill throughput of Qwen3.7-Plus**](https://qwen.ai/blog?id=qwen3.8-flash-next) at 1M context.

### Gated Residual: Four Paths Instead of One

A conventional Transformer repeatedly reads and writes a single residual stream. Qwen3.8-Flash-Next instead uses [**Gated Residual to widen that stream into four parallel branches**](https://qwen.ai/blog?id=qwen3.8-flash-next). Element-wise read gates decide how much information to take from each branch, while branch-level write gates determine what is written back.

This is intended to preserve useful features across depth without forcing every feature through the same continuously mixed channel. Qwen also reports that the gate suppresses activation outliers and that the residual state can be stored in FP8, lowering memory traffic. The key idea is not simply more residual capacity; it is controlled routing of information across layers.

### N-gram Embedding: More Capacity Without Proportional Compute

The model adds [**51B N-gram Embedding parameters**](https://qwen.ai/blog?id=qwen3.8-flash-next) beyond the 125B main backbone. Unlike ordinary embedding that indexes from a single token, N-gram Embedding uses local token patterns such as bigrams and trigrams. This gives the model a large lookup-style memory for recurring local patterns.

The unusual part is where the capacity lives. Because the lookup address can be known before the embedding is needed, the table can be kept in host memory and asynchronously prefetched while GPU computation continues. This means the extra 51B parameters do not behave like 51B additional dense matrix-multiplication parameters. The architecture is effectively scaling two different resources: compute-heavy model parameters and low-compute lookup memory.

### Muon and Training Optimization

Qwen trains the architecture with the [**Muon optimizer for two-dimensional linear maps**](https://qwen.ai/blog?id=qwen3.8-flash-next) such as the main weights in attention, GDN, and MoE experts, while embeddings, the router, and low-rank Gated Residual parameters continue to use AdamW. Fused matrices such as QKV and SwiGLU projections are split into their independent linear transformations before orthogonalization.

The team also refitted its scaling law for the new architecture and reports that conventional Batch Size Warmup was unnecessary. Gradually increasing batch size did not improve the final result and instead required [**18.8% more optimizer steps**](https://qwen.ai/blog?id=qwen3.8-flash-next). The final recipe therefore begins directly at the target batch size.

### Ultra-Sparse MoE and Multi-Token Prediction

The official model card lists [**512 experts with 10 routed experts and one shared expert active per token**](https://huggingface.co/Qwen/Qwen3.8-Flash-Next). The large expert pool increases stored capacity without activating the entire model for every token. A one-layer Multi-Token Prediction (MTP) module is trained with multiple steps to improve speculative-decoding acceptance while also supporting the main backbone.

## **Qwen3.8-Flash-Next Benchmark Performance**

Qwen publishes broad language, coding, agent, and vision-language evaluations. These numbers are useful because many comparison models were rerun in Qwen's harness, but they are still [**vendor-reported launch evaluations**](https://qwen.ai/blog?id=qwen3.8-flash-next), not independent benchmark reproductions. Several rows also use benchmark-specific harnesses or judges, so the safest interpretation is directional: they show where Qwen3.8-Flash-Next is strongest and where competitors still lead.

### **Coding and Agent Performance**

| Benchmark | Qwen3.8-Flash-Next | Qwen3.8-27B | Qwen3.7-Plus | DeepSeek V4 Flash | Claude Opus 4.6 |
| --- | --- | --- | --- | --- | --- |
| DeepSWE 1.1 | 58.7 | 42.2 | 16.5 | 54.4 | -- |
| SWE-bench Pro | 62.5 | 61.7 | 55.8 | 56.0 | 53.4 |
| SWE-bench Multilingual | 81.0 | 73.8 | 75.8 | -- | 77.5 |
| NL2Repo-Bench | 48.1 | 42.3 | 41.1 | 54.2 | 47.6 |
| CoWorkBench | 73.9 | 70.7 | 65.1 | 45.1 | 68.2 |
| JobBench | 55.7 | 33.4 | 27.6 | 41.3 | 36.6 |
| Toolathlon Verified | 73.5 | 67.1 | 50.6 | 70.3 | -- |
| IFBench | 81.3 | 79.5 | 79.1 | 79.2 | 62.5 |
| GPQA Diamond | 91.7 | 89.2 | 90.3 | 90.8 | 91.3 |
| HLE | 35.9 | 30.8 | 34.7 | 33.8 | 40.0 |
| LiveCodeBench v6 | 91.9 | 90.3 | 89.6 | 90.6 | 88.8 |

The coding story is strong but nuanced. [**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) leads the listed comparison set on SWE-bench Pro, SWE-bench Multilingual, CoWorkBench, JobBench, Toolathlon Verified, and LiveCodeBench v6. However, [**DeepSeek V4 Flash**](https://www.cometapi.com/models/deepseek/deepseek-v4-flash/) is ahead on NL2Repo-Bench, while [**Claude Opus 4.6**](https://www.cometapi.com/models/anthropic/claude-opus-4-6/) leads HLE. This makes efficiency the more defensible headline than universal benchmark dominance.

The most notable gains over the previous Qwen baselines appear in long-horizon work. CoWorkBench rises from 65.1 on [**Qwen3.7-Plus**](https://www.cometapi.com/models/aliyun/qwen3-7-plus/) to 73.9, while JobBench moves from 27.6 to 55.7. Because CoWorkBench is an in-house Qwen benchmark, those gains deserve independent replication, but they align with the architecture's stated focus on cost-efficient agent and office workflows.

### **Multimodal Performance**

| Benchmark | Qwen3.8-Flash-Next | Qwen3.8-27B | Qwen3.7-Plus | Claude Opus 4.6 |
| --- | --- | --- | --- | --- |
| ClawEval-MM (Pass@3 / Avg) | 64.4 / 60.4 | 57.4 / 56.9 | 57.4 / 60.1 | 52.5 / 54.7 |
| RecreationBench | 49.9 | 47.1 | 30.2 | -- |
| AndroidWorld | 84.5 | 81.9 | 81.0 | 62.0 |
| OSWorld 2.0 (Binary / Partial) | 19.4 / 52.3 | 19.4 / 48.0 | 2.8 / 21.5 | -- |
| Vision2Web | 64.0 | 62.9 | 42.1 | -- |
| ERQA | 72.3 | 65.5 | 69.8 | 40.8 |
| LVBench | 76.6 | 72.4 | 76.2 | 63.0 |
| RealWorldQA | 88.5 | 85.9 | 86.9 | 73.9 |
| MathVision (without / with CI) | 90.6 / 95.7 | 90.0 / 94.6 | 90.3 / 88.7 | 65.5 / -- |
| CharXiv RQ (without / with CI) | 84.6 / 90.6 | 83.7 / 90.2 | 85.8 / 85.9 | 66.0 / -- |

[*Data source: Qwen official launch evaluation*](https://qwen.ai/blog?id=qwen3.8-flash-next)*\*\*.*

The multimodal results support the view that this is not merely a coding-focused Flash model. [**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) scores 84.5 on AndroidWorld, 64.0 on Vision2Web, 76.6 on LVBench, and 88.5 on RealWorldQA in Qwen's table. The model card also provides image and video input examples, including recommendations for higher-frame-rate sampling on hour-scale video workloads. video workloads.

## Qwen3.8-Flash-Next vs Other Models

A useful comparison should separate three questions: how much compute is activated per token, how broad the model's modalities and context are, and how well it performs on representative workflows. Raw total parameter count alone does not answer those questions.

### Qwen3.8-Flash-Next vs Qwen3.8-27B vs Qwen3.7-Plus

| Dimension | Qwen3.8-Flash-Next | Qwen3.8-27B | Qwen3.7-Plus |
| --- | --- | --- | --- |
| Model parameters | 125B + 51B N-gram embedding | 27B | 397B |
| Activated parameters | 6B | 27B | 17B |
| Native context | 262K | 262K in Qwen comparison setup | Prior-generation long-context model |
| DeepSWE 1.1 | 58.7 | 42.2 | 16.5 |
| CoWorkBench | 73.9 | 70.7 | 65.1 |
| JobBench | 55.7 | 33.4 | 27.6 |
| AndroidWorld | 84.5 | 81.9 | 81.0 |

The key result is capability per activated parameter. [**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) activates 6B parameters per token versus 27B for Qwen3.8-27B and 17B for [**Qwen3.7-Plus**](https://www.cometapi.com/models/aliyun/qwen3-7-plus/), yet it is ahead on the listed DeepSWE, CoWorkBench, JobBench, and AndroidWorld scores. The trade-off is memory footprint: sparsity reduces active compute, not the amount of model capacity that must ultimately be stored somewhere.

### Qwen3.8-Flash-Next vs DeepSeek V4 Flash vs Claude Opus 4.6

| Dimension | Qwen3.8-Flash-Next | DeepSeek V4 Flash | Claude Opus 4.6 |
| --- | --- | --- | --- |
| Weights | Open-weight | Open-weight | Closed |
| Reported parameter profile | 125B main + 51B N-gram; 6B active | 284B total; 13B active | Not publicly disclosed |
| Primary efficiency story | QSA + GDN + 6B active MoE + lookup memory | High-throughput sparse MoE | Managed frontier reasoning and agent stack |
| Native multimodality | Text, image, video -> text | Text-oriented Flash family; vision route available separately on CometAPI | Text + vision/files through hosted APIs |
| SWE-bench Pro\* | 62.5 | 56.0 | 53.4 |
| CoWorkBench\* | 73.9 | 45.1 | 68.2 |
| NL2Repo-Bench\* | 48.1 | 54.2 | 47.6 |
| HLE\* | 35.9 | 33.8 | 40.0 |

[**DeepSeek V4 Flash**](https://www.cometapi.com/models/deepseek/deepseek-v4-flash/) remains stronger on NL2Repo-Bench in Qwen's comparison, which matters for repository-level code generation. [**Claude Opus 4.6**](https://www.cometapi.com/models/anthropic/claude-opus-4-6/) is stronger on HLE in the same table and represents a closed managed model rather than an open deployment target. [**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) is most differentiated by the combination of open weights, native multimodality, long-context engineering, and a very small active parameter budget.

### Qwen3.8-Flash-Next vs Qwen3.8-Max

| Dimension | Qwen3.8-Flash-Next | Qwen3.8-Max |
| --- | --- | --- |
| Role | Efficiency-first open architectural preview | Qwen3.8 flagship |
| Main/total scale | 125B main + 51B N-gram; 6B active | 2.4T total; about 95B active on CometAPI model page |
| Architecture emphasis | QSA, GDN, Gated Residual, N-gram Embedding, Muon | Maximum frontier capability at much larger scale |
| Best fit | High-volume agents, coding assistants, multimodal automation, self-hosting | Hardest reasoning, large enterprise agents, capability-first workloads |
| Context | 262K native; up to 1M with YaRN | 1M-class hosted context on current Qwen3.8 flagship routes |

[*Qwen3.8-Max*](https://www.cometapi.com/models/aliyun/qwen3-8-max/) *specifications are based on the current CometAPI model listing.*

The distinction is simple: [**Qwen3.8-Max**](https://www.cometapi.com/models/aliyun/qwen3-8-max/) is the capability-first flagship, while [**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) is the architecture-and-efficiency experiment. Developers choosing between them should ask whether the bottleneck is absolute model capability or the cost of running many long-context, tool-using tasks at scale.

## Qwen3.8-Flash-Next Pricing and Availability

The open weights for [**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) are published through Hugging Face and ModelScope. For managed serving, Qwen states that the production version is called Qwen3.8-Flash on QwenCloud, with 1M context enabled by default and official built-in tools.

Qwen lists the managed production price at [**$0.16 per million input tokens and $0.47 per million output tokens**](https://qwen.ai/blog?id=qwen3.8-flash-next). That price refers to the QwenCloud production model Qwen3.8-Flash, not to self-hosting the open weights.

| Route | Input | Output |
| --- | --- | --- |
| QwenCloud production model (Qwen3.8-Flash) | $0.16 / 1M tokens | $0.47 / 1M tokens |
| Open-weight self-hosting | Infrastructure-dependent | Infrastructure-dependent |
| CometAPI route | Check live model page | Check live model page |

*QwenCloud prices are from the* [*official Qwen launch article*](https://qwen.ai/blog?id=qwen3.8-flash-next)*; CometAPI billing should be checked on the live model page.*

For CometAPI users, the dedicated [Qwen3.8-Flash-Next model](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) identifies the route as **qwen3.8-flash-next**. Because routing, upstream availability, and billing can change independently of the open-weight release, production integrations should read the live CometAPI catalog before hard-coding price assumptions.

### CometAPI Recommendation

Qwen3.8-Flash-Next is expected to become available through CometAPI soon. CometAPI provides a single OpenAI-compatible endpoint (`https://api.cometapi.com/v1`) that aggregates 500+ models from leading providers, including Qwen series models. This approach reduces vendor lock-in, simplifies experimentation with Qwen3.8-Flash (once available through the platform or related Qwen endpoints), and streamlines production deployments that may mix models for different tasks (e.g., Qwen for cost-efficient coding agents + another model for specialized reasoning). Documentation and quick-start guides are available at apidoc.cometapi.com and the main CometAPI site.

Whether you self-host the open weights, use QwenCloud, or route through a unified platform such as CometAPI, Qwen3.8-Flash-Next lowers the barrier to high-performance, long-context multimodal agents.

## What Can Qwen3.8-Flash-Next Do?

### 1. High-Volume Coding Agents

A 6B active-parameter budget combined with a 62.5 SWE-bench Pro score in Qwen's evaluation makes [**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) especially interesting for coding systems that run many parallel sessions. Examples include code review, issue triage, repository navigation, test generation, and iterative patching where throughput matters almost as much as single-run intelligence.

### 2. Long-Horizon Office and Knowledge Work

CoWorkBench and JobBench are central to the model's positioning. The architecture is designed for agent loops that repeatedly read context, call tools, update state, and continue working rather than answer once. That maps naturally to document workflows, spreadsheet analysis, report assembly, research synthesis, and business-process automation.

### 3. Multimodal Computer and Mobile Agents

Image and video inputs, AndroidWorld performance, OSWorld evaluation, and Vision2Web results make the model relevant to GUI agents. It can serve as the reasoning layer behind systems that interpret screenshots, operate mobile interfaces, reproduce application layouts, or combine visual state with tool calls.

### 4. Long-Video and Visual Reasoning

The official model card includes explicit video-input examples and [**guidance for hour-scale video preprocessing**](https://huggingface.co/Qwen/Qwen3.8-Flash-Next). That makes the model useful for video question answering, long-video search, visual event extraction, and workflows that combine video understanding with downstream tools.

### 5. Million-Token Research and Repository Workflows

The open model is [**native at 262,144 tokens and extensible to 1,000,000 with YaRN**](https://qwen.ai/blog?id=qwen3.8-flash-next). That distinction matters: 1M is an extension rather than the open model's native context. For large repositories or research corpora, QSA is intended to make the retrieval cost of those long contexts more practical than dense global attention.

## How Can Developers Run Qwen3.8-Flash-Next?

Developers can download the open weights from Hugging Face and run the model with Transformers, vLLM, SGLang or TokenSpeed. Qwen provides OpenAI-compatible Chat Completions examples for both text and multimodal input.

For example, the official model card demonstrates serving Qwen/Qwen3.8-Flash-Next with vLLM and calling it through /v1/chat/completions. Image and video inputs are also demonstrated through the OpenAI-compatible interface.

Qwen3.8-Flash-Next operates in thinking mode by default. Developers can control thinking behavior through enable\_thinking, preserve\_thinking and reasoning\_effort; the documented reasoning-effort levels are xhigh, medium and low.

## What Are the Limitations of Qwen3.8-Flash-Next?

The biggest practical limitation is hardware cost. Although only 6B language-model parameters are activated, the checkpoint contains 125B language parameters plus the 51B n-gram embedding component and 4B MTP parameters. The current repository is approximately 360 GB, so local deployment is still an infrastructure-heavy task.

The second limitation is that 262K is the native context length, not 1M. The model can be extended to 1M tokens, but a CometAPI or model page should not simply list "1M native context." The correct wording is 262K native context, extensible to 1M.

Finally, benchmark performance is uneven. Qwen3.8-Flash-Next is highly competitive on coding and agentic tasks but does not lead every benchmark. For example, Claude Opus 4.6 scores 40.0 on HLE versus 35.9 for Flash-Next, while DeepSeek-V4-Flash-0731 leads the listed models on NL2Repo-Bench.

## Qwen3.8-Flash-Next : What It Signals for Qwen4

The broader significance of this release is its role as an early preview of the architecture expected to underpin Qwen4. Qwen3.8-Flash-Next brings together Qwen Sparse Attention, Gated DeltaNet, four-branch Gated Residual connections, N-gram Embedding, an ultra-sparse MoE expert pool, and Multi-Token Prediction. These choices show how Qwen is exploring higher capacity, longer context, and stronger multimodal and agent performance without increasing active compute at the same rate.

## Final Verdict

[**Qwen3.8-Flash-Next**](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) is important because it changes the shape of the efficiency problem. Instead of treating all parameters as equivalent, it combines a relatively small active MoE path with a very large lookup-style memory and a sparse retrieval mechanism designed for long context. That gives Qwen several independent levers for increasing capacity without increasing per-token matrix computation at the same rate.

For developers, that makes the model a compelling option for high-volume coding assistants, long-context agents, multimodal automation, and self-hosted experimentation. For the broader Qwen roadmap, it is even more significant: Qwen is explicitly using this release to expose the architectural direction it plans to refine toward Qwen4.

---

*Originally published at [https://www.cometapi.com/what-is-qwen3-8-flash-next/](https://www.cometapi.com/what-is-qwen3-8-flash-next/).*
