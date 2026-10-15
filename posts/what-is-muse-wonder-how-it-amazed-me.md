<!-- social-ops-fingerprint:4d78c11e1ec07082937f2c8c6900303fc20f007c7f34bfa79d47bbf70d54f680 -->
---
title: What Is Muse Wonder? How it amazed me
---
# What Is Muse Wonder? How it amazed me

![What Is Muse Wonder? How it amazed me](https://resource.cometapi.com/muse-wonder-hero-v1.1.png)

**TLDR** Meta launched [Muse Wonder](https://www.cometapi.com/models/meta/muse-wonder/) and [Muse Wonder Full](https://www.cometapi.com/models/meta/muse-wonder-full/) on October 12, 2026 — its most capable models yet, purpose-built for personal and professional agentic tasks. Muse Wonder Full scores 56 on the Artificial Analysis Intelligence Index (just behind Claude Opus 5.5 at 58), while Muse Wonder scores 52. Both feature Active Memory and Active Focus, a 1M-token context window, strong coding and domain expertise (law, finance, health), and multimodal inputs.

Muse Wonder is available via the Meta Model API at $4/$20 per million tokens (input/output); Muse Wonder Full is limited to higher Muse Code subscription tiers. Developers can also access these models (and 500+ others) through unified platforms like CometAPI for simpler integration and potential cost advantages.

## Key Takeaways

- Muse Wonder and Muse Wonder Full are Meta’s frontier models for long-running agents, coding, computer use, and real-world knowledge work.
- Key innovations: **Active Memory** (persistent, relevant context across conversations) and **Active Focus** (persistent goal pursuit, error recovery, and clarification-seeking).
- Independent Artificial Analysis Intelligence Index (max effort): Muse Wonder Full 56, Muse Wonder 52 (up from Muse Spark 1.3’s 48).
- Strong performance on long-horizon coding (DeepSWE, SWE-Marathon), legal/finance agent tasks, and memory benchmarks; competitive or leading in several Meta and third-party evaluations.
- Pricing: Muse Wonder at $4 input / $0.20 cached / $20 output per 1M tokens on the Meta Model API; Muse Wonder Full is subscription-only via Muse Code (Power $50/mo and Maximum $200/mo plans). Standard Muse Wonder API pricing in CometAPI: $3.2/M input, $0.16/M cached input, $20/M output.

## What Is Muse Wonder?

Muse Wonder is Meta’s new family of frontier large language models, announced on October 12, 2026, by Meta Superintelligence Labs.The release builds on Muse Spark and shifts the emphasis from isolated chatbot replies toward long-running assistants that can work with tools, retain useful context, and iterate on difficult work. It consists of two variants:

- **Muse Wonder** — the standard frontier model optimized for real-world coding, long-running agents, and advanced computer use. Available via the Meta Model API and Muse Code.
- **Muse Wonder Full** — the higher-capability version that delivers maximum reasoning performance for the hardest, longest-running professional and agentic workflows. Currently available only to Muse Code subscribers on higher-tier plans.

These models build directly on the foundation laid by Muse Spark (introduced earlier in 2026) and represent Meta’s most significant leap toward “personal superintelligence.” They are explicitly designed for agentic use cases — systems that do not merely answer questions but plan, execute, recover from errors, and complete multi-step real-world tasks over extended periods. Examples include navigating insurance claims, interpreting leases, analyzing financial or health information, building complete applications, and handling complex personal projects.

The models were trained at Meta’s gigawatt-scale Prometheus data center using advanced pretraining and reinforcement learning techniques refined since the Muse Spark series. They support a 1-million-token context window and accept multimodal inputs (text, images, video, audio, and PDFs in many configurations), with text output.

## Muse Wonder API technical specifications

| Specification (official model card) | Muse Wonder | Muse Wonder Full |
| --- | --- | --- |
| Developer | Meta Superintelligence Labs | Meta Superintelligence Labs |
| Release | October 12, 2026 | October 12, 2026 |
| Identifier | muse-wonder-1.0 | muse-wonder-full-1.0 |
| Context window | 1,000,000 tokens | 1,000,000 tokens |
| Inputs | Text, image, audio, video | Text, image, audio, video |
| Output | Text | Text |
| Reasoning | Configurable | Advanced |
| Active Memory / Focus | Supported | Supported |
| Public API | Meta Model API | Not available |
| Access | Meta API and Muse Code | Qualifying Muse Code plans |
| Model weights / parameter count | Not publicly disclosed | Not publicly disclosed |
| Intelligence Index | 52 | 56 |

## Core Features: Active Memory and Active Focus

### Active Memory

The models can carry important user context across conversations and actively retrieve the details relevant to the current task. This goes beyond simple long-context windows; it prioritizes and surfaces the information that matters for ongoing goals, habits, preferences, and prior interactions. Meta highlights strong results on MemoryBench, where both variants score very highly.

### Active Focus

When a task becomes difficult, the models persist: they try alternative approaches, recover from errors, adapt to new information, ask for clarification when needed, and check in before taking important actions. This is evaluated through internal FocusBench and long-horizon coding suites such as SWE-Marathon. The result is agents that stay on track for hours rather than drifting or giving up.

### Additional strengths include:

**Multimodal understanding:** The model family supports text, image, audio and video inputs and produces text output. However, audio-dependent applications must confirm support on the specific release surface. A model-level modality specification does not guarantee that every API or application exposes the same input path.

**Expert-domain reasoning:** Meta's launch evaluations include legal, financial and health-related tasks, such as document review and information synthesis. These scores describe evaluated tasks; they do not establish professional certification or replace expert verification in high-stakes settings.

**Frontier coding and computer use:** Wonder supports application generation, debugging, code modification and tool-based workflows. Success in practice still depends on the surrounding agent harness, permissions and evaluation process.

## How Does Muse Wonder Perform on AI Benchmarks?

The table below reproduces launch-reported scores. It combines independent evaluations, Meta's internal tests and provider-reported competitor results. Higher scores are better within each row; the rows have different metrics and should not be averaged into a new overall score.

| Benchmark (metrics and methodology) | Wonder Full | Wonder | GPT-6 Astra | Claude Opus 5.5 |
| --- | --- | --- | --- | --- |
| AA Intelligence Index v4.3 | 56 | 52 | 53 | 58 |
| Personal Superintelligence Index | 59.1 | 54.3 | 54.5 | 55.2 |
| Harvey LAB-AA | 13.1 | 10.0 | 8.6 | 4.2 |
| Vals Finance Agent V2 | 59.1 | 56.6 | 53.5 | 58.6 |
| HealthBench Pro | 62.3 | 60.5 | 65.3 | 65.6 |
| AutomationBench-AA | 45.4 | 39.1 | 41.6 | 41.2 |
| GDP.pdf | 33.2 | 30.8 | 34.2 | 30.6 |
| JobBench | 75.3 | 70.5 | 66.1 | 75.4 |
| MemoryBench | 85.5 | 85.6 | 81.4 | 81.5 |
| DeepSWE 1.1 | 79.0 | 78.8 | 74.1 | 74.2 |
| SWE-Marathon | 57.5 | 53.1 | 42.5 | 46.3 |
| Terminal-Bench 4.0-AA | 57.1 | 52.0 | 59.1 | 59.6 |
| ProgramBench | 59.0 | 50.0 | 52.5 | 70.5 |

### Evaluation conditions and score interpretation

Meta reports maximum reasoning effort for the general comparison, with benchmark-specific exceptions. Internal competitor runs are best-effort; external results retain their original harnesses. These are launch comparisons rather than a uniform test of all models under one production configuration.

AA Intelligence Index is a composite index from Artificial Analysis. PSI and MemoryBench are internal evaluations. Harvey LAB-AA and AutomationBench-AA use Artificial Analysis results; Vals Finance Agent V2 uses Vals AI; GDP.pdf uses Surge. HealthBench Pro combines Meta runs and Anthropic-reported results. JobBench reports mean task reward.

DeepSWE 1.1 reports pass@1 across 113 tasks and 91 repositories. SWE-Marathon uses Abundant AI results from different agent products; Wonder Full's 57.5 is reported at xhigh effort. ProgramBench uses mini-swe-agent and measures rollouts passing at least 95% of hidden tests. Terminal-Bench uses Artificial Analysis results from executable terminal tasks. MemoryBench tests 64K–100K-token conversations.

### Muse Wonder Full's benchmark strengths

Muse Wonder Full particularly shines on long-running software engineering and memory-intensive agent work, while Claude Opus 5.5 retains edges in some pure terminal/computer-use and from-scratch programming tasks. Knowledge breadth remains a relative area for continued improvement, though hallucination rates are notably low.

### Independent verification comes primarily from Artificial Analysis

**Artificial Analysis Intelligence Index (v4.3, max reasoning effort)**

- Muse Wonder Full: 56
- Muse Wonder: 52
- Claude Opus 5.5: 58
- GPT-6 Astra / Claude Fable 5.1 / Gemini 4 Argon: ~53
- Previous Meta model (Muse Spark 1.3 max): 48

Muse Wonder Full places in the top three on six of the ten component evaluations and leads or near-leads in agentic knowledge work and scientific reasoning (e.g., CritPt, GDP.pdf, GDPval-AA). Both models show large gains in Terminal-Bench and other agentic coding suites compared with Muse Spark 1.3.

## How Much Does Muse Wonder API Cost?

Meta offers Muse Wonder through its Model API with token-based billing. Developers can also explore [Muse Wonder API in CometAPI](https://www.cometapi.com/compare/auto-vs-muse-wonder/), where the platform advertises discounted model access.

The following table compares Meta's official token rates with a **20%-off pricing scenario** for CometAPI.

| Pricing category (official token rates) | Muse Wonder | CometAPI (20%-off target) |
| --- | --- | --- |
| Input | $4.00 per 1M tokens | $3.20 / 1M tokens |
| Cached input | $0.20 per 1M tokens | $0.16 / 1M tokens\* |
| Output | $20.00 per 1M tokens | $16.00 / 1M tokens |
| Context | 1M tokens | Subject to supported deployment |
| Wonder Full API | Not publicly offered | Not publicly offered |

Cached input is 95% cheaper than uncached input at the published rates, potentially useful for repeated agent prompts with substantial shared context.

### Example request cost

For 100,000 uncached input tokens and 20,000 output tokens: input = (100,000 / 1,000,000) × $4 = $0.40; output = (20,000 / 1,000,000) × $20 = $0.40; total estimated model cost = $0.80.

An actual multi-call agent workflow may cost more because of planning, tool calls, retries and evaluation passes.

### Muse Wonder Full subscription pricing

Wonder Full is distributed through qualifying Muse Code subscriptions rather than separately published API token prices. The Power and Maximum plans cost $50 and $200 per month, respectively. They provide 20x and 80x the Everyday Usage allowance; these are limited subscriptions, not unlimited usage or per-token API plans.

## Comparison: Muse Wonder vs GPT-6 Astra vs Claude Opus 5.5

The following comparison combines launch benchmark observations with provider specifications. For alternative integrations, developers can evaluate [GPT-6 Astra API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-astra/) and [Claude Opus 5.5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-opus-5-5/). The table uses official provider specifications and rates; benchmark leadership alone does not determine the best deployment choice.

| Dimension | Wonder Full | GPT-6 Astra | Claude Opus 5.5 |
| --- | --- | --- | --- |
| Overall intelligence | Strong | Strong | Highest listed index |
| Legal agent tasks | Best listed Harvey score | Competitive | Lower listed score |
| Long-horizon coding | Best listed DeepSWE / Marathon | Strong | Strong |
| Terminal execution | Competitive | Strong | Best listed score |
| Program reconstruction | Competitive | Competitive | Best listed score |
| Public standalone API | No | Yes | Yes |
| Context window | 1M tokens | 1.05M tokens | 1M tokens |
| Standard input / output price per 1M tokens | Subscription access; no public token tariff | $10 / $50 for prompts up to 272K input tokens | $4 / $20 |
| Reasoning | Higher-capability Muse variant | Configurable reasoning effort | Adaptive thinking |
| Multimodal integration | Model card lists text/image/audio/video input; surface support varies | Text and image inputs; text output | Text and image inputs; text output |
| Architecture comparison | Insufficient disclosed detail for a like-for-like architecture comparison | Not compared in the cited API specifications | Not compared in the cited API specifications |
| Practical starting point | Muse Code users testing sustained coding workflows | Custom API agents and professional research | Custom API coding and knowledge-work agents |

The Muse Wonder series positions Meta competitively at the frontier for agentic workloads rather than pure chat or short-horizon reasoning. Pricing for Muse Wonder matches Claude Opus 5.5’s list rates while delivering strong specialized performance in memory, long-horizon coding, and professional agent tasks. GPT-6 Astra and Claude Fable 5.1 often carry higher list prices on some platforms. Access models differ: Meta restricts the absolute top variant (Full) to its coding subscription product, while competitors typically offer their highest models via API.

## Where Can You Use Muse Wonder?

**Direct from Meta**

- Sign up for the Meta Model API at dev.meta.ai for Muse Wonder.
- Subscribe to Muse Code for both variants (Full on higher tiers).
- OpenAI- and Anthropic-compatible endpoints are supported for meta API and CometAPI.

### Muse Wonder: Meta Model API

Muse Wonder is available through Meta Model API for teams building applications, research assistants and tool-based agents. This is the programmable access route described in this article, with token-based billing. Readers can consult the [provider model page](https://dev.meta.ai/models/muse-wonder) for access details rather than follow a code tutorial here.

The two access routes serve different needs: Meta Model API is the starting point for custom Wonder applications; qualifying Muse Code subscriptions provide access to Wonder Full within the coding agent. The following sections explain the subscription route and what to check when considering third-party access.

### Use Muse Wonder Full through Muse Code

Qualifying Muse Code Power or Maximum users can access Wonder Full through Muse Code, a terminal-based coding agent. This subscription route differs from calling a separately metered public Wonder Full API.

### Muse Wonder access and CometAPI alternatives

CometAPI provides a single OpenAI-compatible endpoint (`https://api.cometapi.com/v1`) and one API key for 500+ models, including Meta’s Muse series (Muse Wonder and Muse Wonder Full are listed, with some variants noted as available or coming soon and often at discounted rates relative to list prices).

For alternative integrations, developers can access [GPT-6 Astra API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-astra/) and [Claude Opus 5.5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-opus-5-5/). Compare the same task, context and tool settings before changing providers.

To get started on CometAPI: create a free account (test credits included), obtain your key, point your client at the CometAPI base URL, and specify the Muse Wonder model ID. This approach reduces operational overhead when experimenting with or productionizing frontier agent capabilities.

## Conclusion

Muse Wonder and Muse Wonder Full represent Meta’s clearest statement yet that it has returned to the frontier of AI model development. By focusing on the practical requirements of personal and professional agents — reliable memory, persistent focus, domain expertise, and long-horizon coding and computer use — Meta has produced models that are immediately useful for developers building the next generation of agentic systems and that will enhance its own Muse product.

For teams evaluating or deploying these capabilities, starting with the Meta Model API for Muse Wonder and considering aggregation platforms such as CometAPI for multi-model flexibility provides a low-friction path to experimentation and production. As the full safety report and broader Muse agent rollout arrive, the practical impact of these models will become even clearer.

---

*Originally published at [https://www.cometapi.com/what-is-muse-wonder/](https://www.cometapi.com/what-is-muse-wonder/).*
