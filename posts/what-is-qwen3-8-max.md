<!-- social-ops-fingerprint:31a52b5036c07902bf4299ffc7872fff87ff2a4643e3e273962003e5e00df3fe -->
---
title: What is Qwen3.8 Max
---
# What is Qwen3.8 Max

![What is Qwen3.8 Max](https://resource.cometapi.com/What%20is%20Qwen3.8%20Max.webp)

**TLDR** Alibaba’s Qwen team officially launched Qwen3.8-Max on August 3, 2026 — a sparse Mixture-of-Experts model with 2.4 trillion total parameters (95 billion active), a 1-million-token context window, and native multimodal (text + image + video) support.

It is the first Max-class Qwen model scheduled for open weights (expected the following week). Priced aggressively at $2 per million input tokens and $6 per million output tokens, it delivers strong results on long-horizon agentic tasks, autonomous software engineering (including a documented 16-day self-evolving coding project), research reproduction, and multimodal benchmarks. It competes closely with models such as Kimi K3 and sits above lighter options like DeepSeek V4 Flash in capability while remaining far more cost-efficient than top Western frontier models on output-heavy workloads. Developers can access it today via QwenCloud / Alibaba Cloud Model Studio and through unified platforms such as [CometAPI](https://www.cometapi.com/).

## Key Takeaways

- **Scale and efficiency**: [2.4T total / 95B active MoE architecture](https://qwencloud.com/models/qwen3.8-max/) built on Qwen 3.5 foundations enables frontier-level performance at practical inference cost.
- **Long-horizon strength**: Demonstrated multi-day autonomous coding (265 commits, 127 PRs over ~16 days with zero human intervention), research paper reproduction + improvement, and year-long simulated e-commerce operations.
- **Benchmark highlights**: PaperBench 93.0 (leading), Terminal Bench 2.1 86.6, strong multimodal and document scores; competitive but not dominant on every pure coding agent leaderboard versus Claude Fable 5 or GPT-5.6 Sol.
- **Pricing advantage**: Flat $2 / $6 per 1M tokens across the full 1M context (cached input ~$0.25), undercutting Kimi K3 on output and many Western models.
- **Availability**: [Live on QwenCloud and Alibaba Cloud Model Studio](https://help.aliyun.com/zh/model-studio/opencode) (OpenAI- and Anthropic-compatible APIs); open weights planned; already listed on CometAPI as `qwen3.8-max` for unified access alongside 500+ other models. Open weights coming imminently; smaller Qwen3.8-27B variant also planned for practical local/edge deployment.
- **Practical edge**: Excels at end-to-end deliverable production rather than single-turn answers — ideal for coding agents, research pipelines, office workflows, and sustained agent loops.

## What Is Qwen3.8-Max?

Qwen3.8-Max is Alibaba’s latest and most capable flagship model in the Qwen series, officially released on August 3, 2026 (following a mid-July preview at the World AI Conference in Shanghai). It represents a deliberate shift toward models that can complete complex, multi-day tasks end-to-end with minimal supervision and produce ship-ready deliverables.

Architecturally it is a sparse Mixture-of-Experts (MoE) model scaling to **2.4 trillion total parameters**, of which only approximately **95 billion are activated** per token. This design, built on the Qwen 3.5 foundation, balances massive capacity with inference efficiency. The model supports a **1-million-token context window** (documented max input around 991K tokens and max output around 131K tokens), native multimodal inputs (text, images, and video), and text output. It includes reasoning-effort controls (xhigh / medium / low) and supports both OpenAI Chat Completions and Anthropic-compatible protocols, making it drop-in compatible with popular agent frameworks such as Claude Code, Codex, Qoder CLI, Qwen Code, and OpenClaw.

Unlike earlier Max-class models that remained closed, Alibaba has committed to releasing the weights of Qwen3.8-Max (and a smaller Qwen3.8-27B variant) the week after launch via Hugging Face and ModelScope — the first time a Max-tier Qwen model will be openly available.

The model is positioned for coding agents, real-world professional work (“cowork”), research, long-horizon planning, and multimodal agent loops. Official demos emphasize self-evolving behavior: the model creates issues, assigns them to itself, writes and tests code, iterates on feedback, and improves its own tooling over extended periods.

Sources: [Official Qwen blog](https://qwen.ai/blog?id=qwen3.8) and [Alibaba Cloud announcements](https://www.alibabacloud.com/en/press-room/alibaba-unveils-qwen3-8-max?_p_lc=1) (August 2026); Artificial Analysis model card; independent reviews summarizing the GA release.

## What Is New in Qwen3.8-Max?

Compared with its predecessor Qwen3.7-Max, the 3.8 generation delivers substantial gains in agentic coding, long-horizon reliability, multimodal reasoning, and document/office performance. Key innovations include:

### True long-horizon autonomy:

The model can sustain closed-loop adaptive learning across hundreds of turns or multiple days. Documented examples include a 16-day autonomous software engineering project that produced a self-evolving CLI tool (oh-my-cli) with 265 commits, 127 pull requests, and 151 issues entirely without human intervention; reproduction and improvement of a research paper’s methodology (including GPU training loops and measurable benchmark gains); and a full simulated year of e-commerce operations that significantly outperformed baselines.

### Multimodal as a continuous feedback loop:

Vision is not merely an input modality. The model uses visual understanding for planning, execution monitoring, and self-correction — enabling tasks such as screenshot-to-code recreation, interactive game/animation generation, and 2D-to-3D visualization.

The model ranks highly on Text Arena (fifth reported) and Vision Arena (second reported) in [early post-release data](https://img.alicdn.com/imgextra/i3/O1CN01K8B4Ic27Y7dfp8cyl_!!6000000007808-2-tps-800-800.png_.webp).

![What is Qwen3.8 Max](https://img.alicdn.com/imgextra/i3/O1CN01K8B4Ic27Y7dfp8cyl_!!6000000007808-2-tps-800-800.png_.webp)

![What is Qwen3.8 Max](https://img.alicdn.com/imgextra/i2/O1CN01MNOCjxdbKTG1chua_!!6000000001857-2-tps-800-800.png_.webp)

### End-to-end deliverable focus:

Emphasis on producing production-quality outputs across hundreds of professions rather than isolated answers.

### Thinking and Fast Inference Modes

Two modes: thinking mode and fast inference mode. Thinking mode is for deeper reasoning and complex planning. Fast mode is for lower-latency responses when the task is straightforward. [Alibaba Cloud's OpenCode](https://www.qwencloud.com/models/qwen3.8-max#features) docs show `thinking` enabled for the Qwen3.8 routes and list reasoning controls for the preview route, including `xhigh`, `medium`, and `low`.

This split is valuable for product design. Teams should not use the heaviest reasoning mode for every request. A support bot can classify a simple ticket cheaply, summarize with a faster model, and escalate to Qwen3.8-Max thinking mode only when the user asks for a complicated policy decision, root cause analysis, contract review, or code migration plan.

These capabilities were validated through internal long-running experiments and a comprehensive benchmark suite covering coding agents, general agents, multimodal reasoning, document understanding, and perception/grounding tasks.

## Benchmarking: Data quantization performance

Alibaba published an extensive internal benchmark suite at GA. Independent verification (Artificial Analysis Intelligence Index, LMArena, etc.) was still catching up in the immediate days after release; early Artificial Analysis data placed Qwen3.8-Max at an Intelligence Index of 53 (rank ~16/186 in the tracked set), with noted high verbosity and relatively lower speed.

Selected official/reported scores (Qwen3.8-Max vs selected peers):

| Benchmark | Qwen3.8-Max | Claude Fable 5 / Opus 4.8 | GPT-5.6 Sol (max) | Qwen3.7-Max |
| --- | --- | --- | --- | --- |
| Terminal-Bench 2.1 | 86.6 | 84.6 | 88.8 | 74.5 |
| PaperBench | 93.0 | 88.8 / 80.3 | 90.5 | 64.8 |
| SWE-bench Pro | 67.7 | 80.0 / 69.2 | 64.6 | 60.6 |
| FrontierSWE | 73.5 | 88.8 | — | 40.7 |
| DeepSWE 1.1 | 56.6 | 70.0 | 73.0 | 21.6 |
| IFBench | 82.8 | ~63.5 | — | 79.1 |
| GPQA Diamond | 92.6 | 92.6 | 94.1 | 92.4 |
| OmniDocBench 1.5 | 92.1 | — | — | — |
| OSWorld-Verified | 86.1 | — | — | — |

Qwen3.8-Max frequently leads or places near the top on multimodal reasoning, document/office tasks, and certain agentic coding/research metrics, while trailing the strongest closed models on some pure software-engineering agent suites. The generational leap on FrontierSWE and DeepSWE is especially notable. Treat vendor numbers as directional; independent runs and workload-specific evaluation remain essential.

## API Pricing of [Qwen3.8-Max](https://www.cometapi.com/models/aliyun/qwen3-8-max/)

Official Alibaba Cloud Model Studio / QwenCloud pricing for Qwen3.8-Max (GA rates as of early August 2026):

- Input: $2.00 per 1 million tokens
- Output: $6.00 per 1 million tokens (includes thinking/reasoning tokens)
- Cached input: approximately $0.25 per 1 million tokens (significant savings for repeated long contexts)

Pricing is flat across the entire 1M-token context window — a notable advantage versus many competitors that apply long-context surcharges. Batch and other discounts may apply depending on the deployment region and plan.

**Comparison context (approximate list prices around the same period):**

- [Kimi K3](https://www.cometapi.com/models/moonshotai/kimi-k3/): ~$3 / $15
- Higher-end Claude / GPT frontier models: often $5+ / $15–25+
- DeepSeek [V4 Flash](https://www.cometapi.com/models/deepseek/deepseek-v4-flash/) variants: substantially lower (often under $0.50 combined for many use cases)

For teams that already use multiple providers, aggregated gateways such as **CometAPI** typically offer ~20% discounts relative to official rates, a single OpenAI-compatible endpoint, unified billing, and easy model switching or failover. This makes experimentation with Qwen3.8-Max (and simultaneous comparison against DeepSeek V4 Flash, Kimi models, or others) operationally simpler and often cheaper. Check current CometAPI pricing pages and free-credit offers for the latest effective rates.

## How Qwen3.8-Max Matches Kimi K3 and DeepSeek V4 Flash

| Dimension | Qwen3.8-Max | Kimi K3 | DeepSeek V4 Flash |
| --- | --- | --- | --- |
| Total / Active params | 2.4T / ~95B | ~2.8T / ~104B | 284B / 13B |
| Context | 1M | 1M | 1M |
| Multimodal | Text + Image + Video | Text + Image + Video | Text only |
| Pricing (in/out) | $2 / $6 | $3 / $15 | ~$0.14 / $0.28 (much cheaper) |
| Open weights | Planned (next week) | Already released | MIT, available |
| Strengths | Long-horizon autonomy, multimodal, PaperBench, pricing on output | Strong independent scores, frontend coding Arena leadership | Extreme cost-efficiency, solid agentic coding for size |
| Relative standing | Competitive / leading on several agent & multimodal benches | Slight edge on some audited intelligence indices | Excellent value; lower absolute capability |

Qwen3.8-Max generally matches or exceeds Kimi K3 on cost-efficiency for output-heavy work and multimodal tasks, while DeepSeek V4 Flash remains the budget king for high-volume text workloads where peak capability is secondary. Many teams will use all three via a unified gateway, routing simple traffic to Flash-class models and complex agent sessions to Qwen3.8-Max or Kimi K3.

### Does Qwen3.8-Max match Kimi K3?

In some ways, yes. It matches the 1M-context tier, has strong multimodal positioning, and is cheaper on standard official input/output pricing. It does not match Kimi K3's 2.8T total parameter count, and Kimi's public documentation currently provides especially detailed tool, context caching, structured output, and vision guidance.

### Does Qwen3.8-Max match DeepSeek V4 Flash?

It competes in 1M-context and MoE architecture, but the products are aimed at different jobs. DeepSeek V4 Flash is the economical fast route. Qwen3.8-Max is the larger high-capability route for work where multimodal understanding, advanced reasoning, and enterprise productivity matter more than the lowest possible token price.

## What can Qwen3.8-Max do?

### Coding and Software Engineering

Qwen3.8-Max is a strong candidate for full-stack development, code review, repository understanding, migration planning, API design, debugging, test reasoning, and software architecture. Its long context helps when the model needs to keep many files, logs, and requirements in view. Use it for hard code tasks, not for every autocomplete or simple lint explanation.

### Office and Knowledge Work

The model's "Cowork" positioning matters. Enterprise employees do not only ask chat questions. They compare PDFs, summarize meetings, review slides, interpret spreadsheets, check contracts, write reports, and prepare decisions from messy evidence. Qwen3.8-Max's multimodal and long-context design makes it suitable for office workflows where text, documents, screenshots, and structured data must be reasoned about together.

### Agentic Workflows

Qwen3.8-Max is useful for agent planning: breaking a goal into steps, deciding which tool to call, evaluating results, and revising the plan. In CometAPI, this becomes more practical because the same application can route simple steps to cheaper models and reserve Qwen3.8-Max for planning or verification.

## Getting Started and CometAPI Integration Tips

1. **Direct access**: Use QwenCloud or Alibaba Cloud Model Studio with the model ID `qwen3.8-max`. Both OpenAI-compatible and Anthropic-compatible endpoints are supported.
2. **Unified access via CometAPI**: Sign up at CometAPI.com, obtain an API key, set `base_url` to `https://api.cometapi.com/v1`, and call `model="qwen3.8-max"`. The same key works for DeepSeek V4 Flash, Kimi K3, Claude, GPT, and hundreds of other models — ideal for experimentation, cost control, and production routing. CometAPI emphasizes competitive pricing, low latency, and rapid addition of new models (Qwen3.8-Max was listed shortly after launch).
3. **Agent frameworks**: Plug directly into Claude Code, OpenClaw, or custom harnesses. Enable higher reasoning effort for complex long-horizon jobs.
4. **Open weights**: Monitor Hugging Face / ModelScope for the forthcoming release if you require on-premise or fine-tuned deployments.

---

*Originally published at [https://www.cometapi.com/what-is-qwen3-8-max/](https://www.cometapi.com/what-is-qwen3-8-max/).*
