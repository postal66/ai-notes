<!-- social-ops-fingerprint:d4e961416fc9be8d86e8c068480b3dc96ebfd5c0bfacf8d5ed2efb4d7ec5114b -->
---
title: What Is GLM-5.3-FlashX? Specs, Speed, Pricing, Benchmarks and Features
---
# What Is GLM-5.3-FlashX? Specs, Speed, Pricing, Benchmarks and Features

![What Is GLM-5.3-FlashX? Specs, Speed, Pricing, Benchmarks and Features](https://resource.cometapi.com/gpt-image-2-image-1789910881307.png)

## TL;DR

GLM-5.3-FlashX is Z.ai’s high-speed serving variant of GLM-5.3-Flash. Launched on September 18, 2026, it targets peak generation speeds of up to 200 tokens per second a provider-reported peak rather than a guaranteed or independently verified multiple—while retaining the GLM-5.3-Flash capability base. [GLM-5.3-FlashX is now available in CometAPI](https://www.cometapi.com/models/zhipuai/glm-5-3-flashx/) through an OpenAI-compatible chat-completions endpoint.

The important distinction is that FlashX is primarily a serving and inference upgrade, not a separately documented intelligence checkpoint. Its capability base is the [320B-total / 18B-active GLM-5.3-Flash model](https://autoclaw.z.ai/blog/model/glm-5.3-flash/), with native multimodal input, a 1M-token context window, hybrid sparse + linear attention, tool use, and long-horizon agentic workflows.

The reported speed and price multipliers are launch claims rather than guarantees for every provider or request. Production evaluation should compare time to first token, sustained throughput, p95 latency, task-completion time and current provider pricing.

Last verified: September 20, 2026

## Key Takeaways

- **Speed:** Z.ai reports peak generation of up to 200 tokens/s; no official baseline measurement or universal multiplier is stated, so teams should benchmark their own route and workload.
- **Capability base:** FlashX inherits the 320B-total / 18B-active MoE design, native multimodality, hybrid sparse + linear attention, and 1M context of GLM-5.3-Flash.
- **Benchmarks:** Published intelligence scores belong to GLM-5.3-Flash; they are not separate FlashX benchmark runs.
- **Best fit:** Interactive coding agents, browser/computer-use loops, visual coding, enterprise assistants and other multi-step workflows where latency compounds.
- **CometAPI availability:** GLM-5.3-FlashX is live in CometAPI with the model ID `glm-5.3-flashx` and the `/v1/chat/completions` endpoint.

## What Is GLM-5.3-FlashX?

GLM-5.3-FlashX is best understood as a latency-optimized delivery tier for GLM-5.3-Flash. Z.ai’s launch messaging focuses on faster and smoother inference, while the underlying Flash model remains the capability foundation. FlashX therefore differs from a new model generation, a distilled checkpoint, or a separately released set of weights.

The base GLM-5.3-Flash model was designed around efficient inference. Z.ai says it was trained from a new multimodal base, uses a 30-trillion-token multimodal corpus, and combines Mixture-of-Experts routing with hybrid attention. FlashX pushes the serving side further, building on the [inference infrastructure developed for GLM-5.3-Flash](https://z.ai/blog/glm-built-its-inference-infrastructure).

For developers, “What is GLM-5.3-FlashX?” has a practical answer: it is the high-throughput GLM-5.3-Flash serving option available from Z.ai and now also through [CometAPI’s unified API](https://www.cometapi.com/models/zhipuai/glm-5-3-flashx/). The value proposition is lower interaction latency rather than a newly claimed jump in model intelligence.

According to [Zhipu’s launch statements reported by IT Home](https://www.ithome.com/1/004/061.htm), GLM-5.3-Flash first appeared to overseas developers under the anonymous name “Ox Alpha” and saw continued growth in usage. To serve that demand, Zhipu increased infrastructure investment and inference optimization on a production base of roughly 100,000 domestic accelerator chips, then introduced FlashX. The service retains the GLM-5.3-Flash capability base while raising provider-reported peak output to 200 tokens/s. Zhipu positions the release around intelligence, price and speed; for enterprise and developer workloads, this translates into a high-throughput, low-latency option whose commercial value should be validated with sustained throughput, p95 latency, task quality and cost under realistic concurrency.

## GLM-5.3-FlashX Specifications

Because FlashX is a high-speed serving variant, its specification sheet should separate inherited model characteristics from FlashX-specific serving characteristics.

| Specification | GLM-5.3-FlashX |
| --- | --- |
| Provider | Z.ai / Zhipu AI |
| Product positioning | High-speed serving option for GLM-5.3-Flash |
| Total / active parameters | Approximately 320B / 18B per token, inherited from the base model |
| Architecture | Mixture-of-Experts; hybrid sparse + linear attention; mHC |
| Context window | Up to 1,048,576 tokens |
| Inputs / output | Exact modality support, file limits, video constraints and route-specific parameters should be verified against the provider endpoint before production deployment. |
| Reasoning | Supported through the underlying GLM-5.3-Flash model |
| Reasoning effort | low / high / max on supported routes |
| Thinking | Route/API dependent |
| Tool / function calling | Supported |
| Open weights | Underlying GLM-5.3-Flash: MIT-licensed; FlashX is presented as a hosted serving option |
| Reported peak speed | Up to 200 tokens/s |
| Reported relative speed | No official baseline or guaranteed multiplier; benchmark the selected provider route |
| CometAPI price | $60 / 1M input tokens and $60 / 1M output tokens, verified September 20, 2026; recheck live pricing |
| Launch date | September 18, 2026 |
| Z.ai model key | GLM-5.3-FlashX / glm-5.3-flashx |
| CometAPI model ID | glm-5.3-flashx |
| CometAPI endpoint | POST /v1/chat/completions |

## Why Is GLM-5.3-FlashX Faster Than GLM-5.3-Flash?

Two optimization layers sit behind the speed story: the efficient architecture inherited from GLM-5.3-Flash and the serving infrastructure optimized around it.

### Hybrid Sparse + Linear Attention

GLM-5.3-Flash combines linear attention for local dependencies with sparse attention for retrieving relevant information from the wider context. Z.ai also describes IndexPool, which compresses four cached indexer key vectors into one through weighted pooling. In Z.ai’s published comparison, these changes reduce attention compute by roughly 3.0× and KV-cache size by roughly 4.4× versus GLM-5.3 at long context.

![What Is GLM-5.3-FlashX? Specs, Speed, Pricing, Benchmarks and Features](https://resource.cometapi.com/1280X1280.PNG)

Z.ai’s [official GLM-5.3-Flash architecture section](https://autoclaw.z.ai/blog/model/glm-5.3-flash/).

### Inference infrastructure

Z.ai says production GLM-5.3-Flash traffic runs on a cluster of more than 100,000 Chinese-made AI accelerators. Its serving stack includes tensor parallelism, ReplaySSM, W8A8 quantization, mixed INT8/FP8/BF16 cache quantization, Layer Split, and an Encode–Prefill–Decode disaggregated architecture. The company reports roughly a 3× end-to-end serving improvement over its initial baseline on the same hardware.

FlashX should therefore be read as the productization of continued inference optimization: the model reduces compute and cache costs, while FlashX adds a more aggressive low-latency serving layer.

## How Fast Is GLM-5.3-FlashX?

Z.ai reports a peak generation speed of up to 200 tokens/s. Treat this as a maximum service claim, not a guaranteed sustained rate: validate time to first token, sustained output speed, p95 latency, task completion and error rate on the production route.

*“Up to 200 tokens/s” is a peak serving figure, not a guarantee for every request. Real throughput depends on prompt length, reasoning effort, output length, multimodal preprocessing, concurrency, tool calls, region and provider load.*

Useful production metrics include time to first token, sustained output tokens per second, p95 latency, and end-to-end task completion time. Task-completion time matters especially for agents because a 20-step workflow may pay the generation delay 20 times.

## How Does GLM-5.3-FlashX Perform on Benchmarks?

No official FlashX-specific intelligence benchmark suite was published at launch. FlashX is documented as an inference and serving optimization, so its validated differentiator is throughput—not a new task-quality score.

Those results belong to the underlying GLM-5.3-Flash model and may be consulted only as capability context; they are not FlashX measurements because the checkpoint, evaluation harness and task-quality run were not separately reported for FlashX.

For deployment decisions, test FlashX and Flash on the same prompts, reasoning effort and tool configuration, then compare task success, time to first token, sustained throughput, p95 latency and total cost per completed workflow.

## GLM-5.3-FlashX vs GLM-5.3-Flash vs GLM-5.3

| Dimension | GLM-5.3-FlashX | GLM-5.3-Flash | GLM-5.3 |
| --- | --- | --- | --- |
| Positioning | High-speed serving tier | Efficiency-first multimodal model | Flagship capability tier |
| Context | Up to 1M | 1M | 1M-class on supported routes |
| Total / active parameters | Inherited 320B / 18B base | 320B / 18B | Larger flagship configuration |
| Peak output speed | Up to 200 tokens/s reported | Provider-dependent baseline | Provider-dependent |
| Relative price vs Flash | About 2.5× reported | 1× | Higher than Flash |
| Open weights | Service tier; base weights are open | Yes, MIT | Release-dependent |
| Reasoning and tools | Inherited from Flash; verify route controls | Supported | Flagship reasoning tier |
| CometAPI availability | Available | Available | Available |
| Best fit | Interactive low-latency agents | High-volume cost-sensitive multimodal work | Maximum-capability GLM workloads |

CometAPI now provides the [GLM-5.3-FlashX API](https://www.cometapi.com/models/zhipuai/glm-5-3-flashx/), alongside the GLM-5.3-Flash API and [GLM-5.3 API](https://www.cometapi.com/models/zhipuai/glm-5-3/). This makes it possible to compare latency, cost and task quality through one integration.

### Workload-based comparison

| Scenario | Flash | FlashX |
| --- | --- | --- |
| Batch processing | ✓ |  |
| Cost-sensitive workloads | ✓ |  |
| Interactive chat |  | ✓ |
| Coding agents |  | ✓ |
| Browser agents |  | ✓ |
| Human-in-the-loop |  | ✓ |
| Long-running automated jobs | ✓ | Depends |
| Latency-sensitive API |  | ✓ |
| High output volume | ✓ |  |
| Maximum responsiveness |  | ✓ |

## How Much Does GLM-5.3-FlashX Cost?

CometAPI lists GLM-5.3-FlashX at $60 per 1M input tokens and $60 per 1M output tokens. Its comparison table shows an official reference price of $75 per 1M input tokens and $75 per 1M output tokens. Prices can change, so confirm the live model page before budgeting.

| Usage | CometAPI price | Official reference price |
| --- | --- | --- |
| Input | $60 / 1M tokens | $75 / 1M tokens |
| Output | $60 / 1M tokens | $75 / 1M tokens |

### Worked Cost Example

For a workload using 100M input tokens and 20M output tokens, the current CometAPI estimate is: 100 × $60 + 20 × $60 = $7,200. At the official reference rate, the same workload is 100 × $75 + 20 × $75 = $9,000.

At these displayed rates, FlashX should be reserved for workflows where latency materially affects revenue, user experience or sequential agent completion time. Batch processing and cost-sensitive high-volume jobs should be benchmarked against the less expensive Flash route.

Reasoning tokens may also contribute to billed output usage, depending on the provider’s policy; estimate cost from actual usage logs rather than visible answer length alone.

## What Are the Best Use Cases for GLM-5.3-FlashX?

### Real-time coding agents

Coding agents repeatedly generate text, call tools, inspect results, modify files, run tests and loop. Faster generation reduces idle time between actions.

### Browser and computer-use agents

Multimodal input lets the model use screenshots and interface state in the reasoning loop. Low latency matters because browser automation rapidly alternates between observing, deciding, acting and observing again.

### Visual coding and UI iteration

A model can inspect rendered interfaces, compare them with requirements, edit code and inspect the result again. Faster inference shortens the visual feedback loop.

### Interactive enterprise assistants

Customer-facing assistants, internal copilots, research agents and document agents often have a human waiting for each turn. A latency premium is easier to justify here than in overnight batch processing.

### Long-context interactive work

The 1M-token context window is useful for large repositories, long reports and extended agent histories when those contexts still require responsive interaction.

## Is GLM-5.3-FlashX Available in CometAPI?

**Yes.** GLM-5.3-FlashX is live in CometAPI. The model page lists it as available through the production `/v1/chat/completions` endpoint, and the documented model ID is `glm-5.3-flashx`. Developers can use the same OpenAI-compatible integration pattern as other CometAPI text models.

Access details, prices, limits and supported modalities can change. The [live CometAPI model page](https://www.cometapi.com/models/zhipuai/glm-5-3-flashx/) is the authoritative source for the current route.

## When FlashX May Not Be Worth It

- **Offline or batch workloads:** when nobody is waiting for the response, lower-cost Flash serving may deliver better economics.
- **Cost-sensitive high-volume generation:** the displayed FlashX token price can dominate total workflow cost even when jobs finish sooner.
- **Tasks limited by model quality rather than latency:** FlashX has no separate official intelligence benchmark suite, so it should not be purchased as a proven capability upgrade.
- **Workflows bottlenecked elsewhere:** retrieval, tools, browsers, databases and human approval may dominate end-to-end latency, reducing the value of faster token generation.
- **Self-hosting or open-weight requirements:** FlashX is presented as a hosted serving tier; use the underlying GLM-5.3-Flash weights when deployment control matters.
- **Strict throughput guarantees:**

## What Are the GLM-5.3-FlashX Limitations?

- The 200 tokens/s figure is a maximum advertised speed, not a guaranteed sustained rate.
- Reported pricing is higher than Flash and varies across providers.
- There is no separate FlashX intelligence benchmark suite yet.
- Standard output is text rather than native image or video generation.
- A 1M-token limit does not remove the need for retrieval, context selection and latency management.
- Provider-specific rate limits, output limits, modalities and real throughput can differ from Z.ai’s service.

## Should You Use GLM-5.3-FlashX?

GLM-5.3-FlashX is most compelling when GLM-5.3-Flash is capable enough but too slow for an interactive workflow. The launch changes the latency economics more than the core capability story.

Choose GLM-5.3-Flash when token cost dominates and slower generation is acceptable. Choose FlashX when human waiting time or agent-loop latency is more expensive than the serving premium. Consider GLM-5.3 when the flagship capability tier matters more than cost or latency.

For teams already using a unified gateway, the practical next step is to run the same representative workload through GLM-5.3-FlashX and GLM-5.3-Flash in CometAPI, then compare p95 latency, task success and total cost per completed workflow.

## GLM-5.3-FlashX FAQ

### What is GLM-5.3-FlashX?

GLM-5.3-FlashX is Z.ai’s high-speed serving option for the GLM-5.3-Flash capability base. It targets lower latency and higher output throughput rather than a separately announced jump in model intelligence.

### Is GLM-5.3-FlashX a new checkpoint?

Z.ai’s public launch materials emphasize inference and infrastructure optimization. No separate parameter count, weight release or intelligence benchmark suite has been published for FlashX.

### Does GLM-5.3-FlashX support multimodal input?

The underlying GLM-5.3-Flash capability base is multimodal. Provider and route-specific modalities should be confirmed before deployment.

### Are the GLM-5.3-FlashX weights open source?

The underlying GLM-5.3-Flash weights are available under the MIT license. FlashX is presented as a high-speed hosted serving option rather than a separately released weight checkpoint.

### Are there separate GLM-5.3-FlashX benchmark scores?

No separate intelligence benchmark suite was published at launch. Current task-quality benchmarks belong to GLM-5.3-Flash.

---

*Originally published at [https://www.cometapi.com/what-is-glm-5-3-flashx/](https://www.cometapi.com/what-is-glm-5-3-flashx/).*
