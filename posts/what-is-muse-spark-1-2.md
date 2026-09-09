<!-- social-ops-fingerprint:4b0470adae398502e30c0181f584bfc0fcb690b17656de365830af7354adc45d -->
---
title: What Is Muse Spark 1.2?
---
# What Is Muse Spark 1.2?

![What Is Muse Spark 1.2?](https://resource.cometapi.com/What%20Is%20Muse%20Spark%201.2.webp)

## TL;DR

Meta [released Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) as a coding-focused update to Muse Spark 1.1. It is designed for code generation, complex debugging, repository understanding, and end-to-end developer workflows rather than as a broad specification reset. The model retains a 1M-token context window and accepts text, image, video, and PDF input while producing text output.

The most important part of the release is the relationship between the model and Muse Code. Meta [co-trained the model with Muse Code](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) using agent trajectories, goal conditioning, context compaction, subagent behavior, and the coding toolset itself. That makes Muse Spark 1.2 especially compelling inside Meta's own coding environment, but it also means the strongest launch scores should be read as model-plus-agent-system results.

In [Meta’s coding evaluation](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2?utm_source=chatgpt.com), Muse Spark 1.2 paired with Muse Code scored 82.9% on Terminal-Bench 2.1 and 59.3% on DeepSWE 1.1. The current Artificial Analysis model page reports an [Intelligence Index score of 57](https://artificialanalysis.ai/models/muse-spark-1-2?utm_source=chatgpt.com), replacing the launch score of 54 under an earlier index version. Its latest [GDPval-AA v2 rating](https://artificialanalysis.ai/evaluations/gdpval-aa) is 1,623 Elo, placing it 15th among 213 evaluated models. Muse Spark 1.2 therefore remains competitive in coding and agentic work but is not the overall leader, with [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/?utm_source=chatgpt.com) ahead on both Meta’s headline coding benchmarks and the current GDPval-AA v2 leaderboard.

## Key Takeaways

- **Coding-first update:** Muse Spark 1.2 concentrates its gains in generation, debugging, codebase understanding, and long-running developer workflows.
- **1M-token context:** The API lists a 1,048,576-token context window for repository-scale work and persistent agent sessions.
- **Multimodal input:** The hosted model accepts text, images, video, and PDF documents and returns text.
- **Agent-system optimization:** The model was trained to operate with Muse Code's planning, tool, compaction, and subagent patterns.
- **Strong but harness-dependent coding results:** Meta reports 82.9% on Terminal-Bench 2.1 and 59.3% on DeepSWE 1.1 with Muse Code.
- **Competitive API economics:** Standard pricing is $1.25 per million input tokens and $4.25 per million output tokens, with a much cheaper Contributor tier under different data terms.
- **Important caveat:** Public parameter count, architecture, and training-token figures have not been disclosed.

## What Is Muse Spark 1.2?

Muse Spark 1.2 is Meta Superintelligence Labs' coding-optimized multimodal reasoning model. Meta describes it as an update to Muse Spark 1.1 with improvements in code generation, complex debugging, codebase understanding, and complete developer workflows. The release was paired with [Muse Code beta](https://developer.meta.com/ai/products/muse-code/), a terminal coding agent designed to plan changes, write code, execute tools, coordinate persistent subagents, and validate results across large repositories.

This positioning matters. Muse Spark 1.2 is not marketed mainly as a better chatbot or a larger general-purpose model. It is designed around the conditions that make software agents difficult: requirements spread across many files, accumulated terminal output, repeated test failures, changing plans, long sessions, and the need to preserve the original objective after many intermediate steps.

### Muse Spark 1.2 Specifications

| Specification | Muse Spark 1.2 |
| --- | --- |
| Developer | Meta Superintelligence Labs |
| Release date | August 5, 2026 |
| API model ID | muse-spark-1.2 |
| Model type | Proprietary multimodal reasoning and coding model |
| Primary focus | Coding agents, debugging, repository understanding, long-horizon development |
| Context window | 1,048,576 tokens |
| Input modalities | Text, image, video, PDF |
| Output modality | Text |
| Reasoning setting in Meta evaluation | xhigh |
| Tool profile | Tool calling and agent-oriented workflows |
| Standard price | $1.25/M input; $0.15/M cached input; $4.25/M output |
| Public parameter count | Not disclosed |
| Public architecture details | Not disclosed |
| Launch deployment | Muse Code and Meta Model API |

**Specification note:** [Meta's model documentation](https://developer.meta.com/ai/models/muse-spark/) supplies the model positioning, context, and pricing; the hosted API documentation supplies the supported input and output modalities. Deployment limits can differ from the theoretical capability of the underlying model.

## What Is New in Muse Spark 1.2?

### More Coding Training

Meta says it significantly increased training compute on coding tasks while expanding the diversity of training environments. The practical goal is not only to generate correct snippets, but to improve first-attempt accuracy when an agent must inspect an unfamiliar repository, identify the relevant files, implement a change, run the build or tests, and revise its work after feedback.

This makes the update more relevant to production engineering than a gain on single-turn code generation. Real repositories contain framework conventions, hidden coupling, incomplete documentation, fragile tests, and requirements that cannot be satisfied by editing one isolated function. Muse Spark 1.2 is explicitly trained for that larger task envelope.

### Co-Training With Muse Code

Meta [co-trained Muse Spark 1.2 with Muse Code](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) so that the model would better match the agent's toolset and runtime. The training included rejection-sampled harness trajectories and recipe optimization for goals, context compaction, and subagents. This is more deliberate than attaching a general model to a command-line wrapper after training.

The benefit is compatibility: the model learns what tool feedback looks like, when a plan should be revised, how background workers communicate, and which state must survive context compression. The trade-off is transferability. A model tuned for one harness can still work elsewhere, but its best result may depend on the prompts, tools, memory system, and control loop it saw during training.

### Long-Horizon Coding

Muse Spark 1.2 was trained on [whole-repository generation and long projects](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2), including auto-research workflows. Meta highlights three behaviors: planning to sequence work, goal conditioning to keep the agent directed toward the original objective, and context compaction to retain critical knowledge as the session grows.

These mechanisms address a common failure mode in coding agents: the system becomes locally productive but globally lost. It may fix a test while breaking the requirement, repeat earlier investigation, or forget why a design choice was made. Long-horizon training is intended to make progress cumulative rather than episodic.

### Self-Improvement With Muse Spark 1.1

Meta also used Muse Spark 1.1 to generate challenging coding environments and instruction-following templates. The earlier model graded candidate solutions against the generated requirements, producing scalable training data for Muse Spark 1.2. This is best understood as model-assisted task generation and evaluation, not as unconstrained self-modification of the deployed model.

### Multimodal Repository Work

The 1M-token window and multimodal inputs matter because many development tasks are not text-only. An agent may need to compare a frontend with a screenshot, inspect a PDF specification, interpret a UI recording, or maintain visual requirements while editing code. The release demonstration in which Muse Code interprets a home fly-through video and produces a marketing and booking page illustrates this perception-to-implementation workflow.

## Muse Spark 1.2 vs Muse Spark 1.1: What Actually Changed?

|  | Muse Spark 1.1 | Muse Spark 1.2 |
| --- | --- | --- |
| Context | 1M | 1M |
| Standard Input | $1.25 | $1.25 |
| Standard Output | $4.25 | $4.25 |
| Intelligence Index | 53 current | 57 current |
| Terminal-Bench | 78% AA | 80% AA |
| Coding focus | High | Higher |
| Muse Code co-training | No | Yes |
| Long-horizon training | Yes | Expanded |
| Open weights | No | No |

## How Muse Spark 1.2 Works With Muse Code

Muse Spark 1.2 is the model; Muse Code is the agent product that turns model calls into persistent software-engineering work. Muse Code runs a main agent alongside asynchronous background agents that remain active through the session. These workers can gather context, execute next steps, and communicate relevant findings back to the main agent without being recreated for every task.

The runtime also maintains a local event log. Every model call, tool execution, approval, and edit is appended to one history, allowing the agent to resume after a crash instead of restarting the task. Built-in skills such as /plan, /grill, and /goal add approval-gated planning, plan stress-testing, and objective-oriented execution.

![What Is Muse Spark 1.2?](https://resource.cometapi.com/blog/uploads/2026/08/Muse%20Spark%201.2.png)

*Figure 1. Muse Code converts Muse Spark 1.2 into a persistent planning, execution, and validation system. Source:* [*Meta launch description*](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)

**Interpretation:** Muse Code's persistence, event log, tools, and subagent orchestration are system capabilities. They should not be attributed to the base model alone.

## Benchmark Performance of Muse Spark 1.2

The following results are reported by Meta. Coding scores measure complete model-and-agent systems, while the later multimodal composite measures Meta Model API configurations with and without tools. They should not be merged with the independent Artificial Analysis metrics that follow.

### Coding Benchmark Performance

| Meta coding benchmarks | Muse Spark 1.2 result | Leading comparison in Meta's chart | Evaluation scope | How to read it |
| --- | --- | --- | --- | --- |
| Terminal-Bench 2.1 | 82.9% with Muse Code | Claude Opus 5: 86.7% with Claude Code | Terminal tasks in selected coding agents | Vendor-reported system result |
| DeepSWE 1.1 | 59.3% with Muse Code | Claude Opus 5: 65.0%; GPT-5.6 Terra: 64.8% | 113 tasks, 91 repositories, five languages | Vendor-reported system result |
| Meta Internal Coding Bench | 70.6% | Claude Opus 5: 79.4% | 440 private tasks derived from Meta pull requests | Private and not independently reproducible |

Meta's [evaluation methodology](https://research.meta.ai/static/muse-spark-1-2-methodology) uses Muse Code for Muse Spark 1.2, Claude Code for [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/), Codex for [GPT-5.6 Terra](https://www.cometapi.com/models/openai/gpt-5-6/), and Grok Build for [Grok 4.5](https://www.cometapi.com/models/xai/grok-4-5/). A higher score can therefore reflect the model, agent loop, prompts, tools, and memory design together. The accurate phrasing is Muse Spark 1.2 in Muse Code scored 82.9%, not the base model alone scored 82.9%.

### Multimodal Benchmark Performance

Meta's [August 20 multimodal evaluation](https://research.meta.ai/blog/multimodal-intelligence-of-muse-spark-1-2) reports a ten-benchmark composite across visual perception, visual knowledge, spatial and UI reasoning, and chart understanding. The largest gain appears when Muse Spark 1.2 can use tools.

| Meta multimodal evaluation | Direct response | With tools | Tool uplift | Interpretation |
| --- | --- | --- | --- | --- |
| Muse Spark 1.2 | 59.8 | 72.0 | +12.2 | Stronger in the tool-enabled configuration |
| Muse Spark 1.1 | 60.2 | 69.1 | +8.9 | Slightly higher without tools, lower with tools |

The official [multimodal methodology](https://research.meta.ai/static/muse-spark-1-2-multimodal-evaluation-methodology) averages BabyVision, PerceptionBench, ZeroBench, WorldVQA, SimpleVQA, ERQA, OmniSpatial, CharXiv Reasoning, ChartMuseum, and ChartQAPro equally. The comparison is useful for measuring tool uplift inside Meta's framework; it is not an independently replicated benchmark.

## Independent Benchmark Results

Under the current [Artificial Analysis Intelligence Index v4.1.1](https://artificialanalysis.ai/models/muse-spark-1-2?utm_source=chatgpt.com), Muse Spark 1.2 scores 57, compared with 53 for Muse Spark 1.1 and an estimated 44 for the original Muse Spark. Its latest [GDPval-AA v2 rating](https://artificialanalysis.ai/evaluations/gdpval-aa?utm_source=chatgpt.com) is 1,623 Elo, placing it 15th among 213 evaluated models. Muse Spark 1.2 also leads the current [AA-LCR long-context benchmark](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning?utm_source=chatgpt.com) with a score of 83.3%, indicating that its strengths extend across agentic knowledge work, coding workflows, and long-context reasoning.

| Evaluation | Score | Environment | What it tells you |
| --- | --- | --- | --- |
| Meta Terminal-Bench 2.1 | 82.90% | Muse Code | Model + Meta's optimized agent |
| Artificial Analysis Terminal-Bench 2.1 | 80% | AA harness | More independent cross-model signal |
| Meta DeepSWE 1.1 | 59.30% | Muse Code | Long-horizon coding |
| Meta Internal Coding | 70.60% | Meta internal | Internal engineering tasks |

![What Is Muse Spark 1.2?](https://resource.cometapi.com/blog/uploads/2026/08/Benchmark%20Muse%20Spark%201.2.png)

Source:[*Artificial Analysis*](https://artificialanalysis.ai/articles/muse-spark-1-2)

The reliability data needs careful interpretation. AA-Omniscience improves from 18 to 22 and the hallucination rate falls from 38% to 28%, but the model's attempt rate also declines from 82% to 67%. Accuracy falls from 41% to 38%. In other words, Muse Spark 1.2 is more willing to abstain when uncertain, which reduces false claims but also produces fewer attempted answers.

Scientific reasoning is comparatively flat. CritPt improves from 15% to 18%, while SciCode declines from 58% to 56% and Humanity's Last Exam falls from 45% to 44%. That pattern supports Meta's own positioning: Muse Spark 1.2 is a specialized coding and agentic update, not a uniform leap across every reasoning domain.

## Muse Spark 1.2 Pricing

Meta offers Standard and Contributor access. The Standard model is priced at $1.25 per million input tokens, $0.15 per million cached input tokens, and $4.25 per million output tokens. The Contributor variant is dramatically cheaper, but Meta states that its data may be used to improve products.

| Tier | Input / 1M | Cached input / 1M | Output / 1M | Data treatment |
| --- | --- | --- | --- | --- |
| Standard | $1.25 | $0.15 | $4.25 | Not used to improve Meta products |
| Contributor | $0.10 | $0.002 | $0.20 | May be used to improve Meta products |

**Pricing source:** [Meta's official model page](https://developer.meta.com/ai/models/muse-spark/). Teams should review the applicable product and data terms before sending proprietary code, credentials, customer data, or internal documents through the Contributor route.

Low token prices do not automatically mean the lowest completed-task cost. Artificial Analysis estimates about $0.40 per Intelligence Index task for Muse Spark 1.2, up from $0.29 for Muse Spark 1.1. The increase is driven by higher token use, especially on professional agentic work. Teams should therefore measure cost per accepted pull request, resolved issue, or verified deliverable rather than comparing only list prices.

## Muse Spark 1.2 vs Other Frontier Coding Models

The most relevant comparison set includes [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/), [GPT-5.6 Terra](https://www.cometapi.com/models/openai/gpt-5-6/), [Grok 4.5](https://www.cometapi.com/models/xai/grok-4-5/), and [Kimi K3](https://www.cometapi.com/models/moonshotai/kimi-k3/). These models overlap in coding, tools, long context, and professional agent workflows, but they differ in deployment, modality breadth, ecosystem, and price-performance priorities.

| Model | Context | Inputs | Terminal-Bench 2.1 signal | Deployment | Best fit |
| --- | --- | --- | --- | --- | --- |
| Muse Spark 1.2 | 1M | Text, image, video, PDF | 82.9% with Muse Code | Meta hosted API | Muse Code, long-running repository work, lower API price |
| Claude Opus 5 | 1M | Text, image, documents | 86.7% with Claude Code | Hosted API | Maximum coding reliability and complex agent judgment |
| GPT-5.6 Terra | ~1.05M | Text, image | 81.8% with Codex | Hosted API | Balanced coding, productivity, and broad tool workflows |
| Grok 4.5 | 500K | Text, image | 81.6% with Grok Build | Hosted API | Coding combined with xAI tools and current information |
| Kimi K3 | 1M | Text, image, video | Not shown in Meta chart | Hosted and open-weight options | Long-horizon work and deployment flexibility |

### Where Muse Spark 1.2 Has the Clearest Advantage

Muse Spark 1.2 is most differentiated when the application can use Muse Code's persistent event log, subagent design, and model-specific training. Its standard API price is also aggressive relative to premium frontier coding models. For teams that value a tightly integrated agent system, the combination may matter more than a small difference on a single benchmark.

### Where [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/) Remains Stronger

[Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/) leads all three Meta coding charts in which it appears. It remains the safer choice when the cost of a failed change is high and maximum end-to-end coding reliability matters more than token price. Muse Spark 1.2 narrows the gap, particularly on terminal tasks, but does not erase it.

### Where [GPT-5.6 Terra](https://www.cometapi.com/models/openai/gpt-5-6/) Fits

[GPT-5.6 Terra](https://www.cometapi.com/models/openai/gpt-5-6/) sits close to Muse Spark 1.2 on Terminal-Bench and ahead on DeepSWE in Meta's evaluation. Its advantage is breadth: teams already using OpenAI's response, search, file, shell, computer, and MCP tooling may prefer a model that fits an existing production stack even when another model is slightly cheaper.

### When [Grok 4.5](https://www.cometapi.com/models/xai/grok-4-5/) or [Kimi K3](https://www.cometapi.com/models/moonshotai/kimi-k3/) May Be Better

[Grok 4.5](https://www.cometapi.com/models/xai/grok-4-5/) is a strong alternative for workflows that combine coding with xAI's current-information and tool ecosystem. [Kimi K3](https://www.cometapi.com/models/moonshotai/kimi-k3/) is more attractive when long-horizon performance, open-weight deployment, or provider control matters. The practical choice depends on the complete runtime: prompts, tools, memory, security requirements, and verification strategy can change outcomes as much as the base model.

## What Can Muse Spark 1.2 Do?

### Repository-Scale Software Engineering

A 1M-token context can hold a substantial amount of source code, documentation, test output, issue history, and agent state. Suitable tasks include multi-file features, framework upgrades, repository-wide refactors, API migrations, test repair, pull-request review, and architecture analysis. Long context is most useful when paired with retrieval and compaction rather than loading a repository indiscriminately.

### Complex Debugging

Muse Spark 1.2 can inspect code, run tools, read failures, form hypotheses, apply edits, and retest. Its coding-focused training is intended to improve this loop, where the difficult part is not proposing a plausible fix but identifying the root cause and verifying that the patch does not create regressions.

### Long-Running Coding Agents

Persistent projects are a central use case. Muse Code's event log and background agents allow work to continue across many model calls and tool steps. This is useful for upgrades, performance tuning, documentation generation, test modernization, and feature slices that cannot be completed safely in one response.

### Automated Technical Research

Meta tested Muse Spark 1.2 on GPU-kernel optimization over more than 1,000 tool calls and up to 24 hours. The agent wrote, compiled, profiled, and refined Triton implementations against reference baselines. The broader lesson is that the model is designed for iterative technical work in which experiments guide the next action.

### Multimodal Development

Image, video, and PDF input expands the development loop beyond source code. A team can use the model to compare a UI against a screenshot, extract requirements from a product document, interpret a recorded interaction, or generate an implementation from a visual reference. Human review remains necessary for accessibility, brand consistency, security, and factual claims embedded in visual content.

## When should you NOT use Muse Spark 1.2?

### Don't choose it primarily for:

- simple chat
- basic code completion
- low-latency autocomplete
- general writing
- tasks where maximum benchmark reliability matters
- highly regulated workloads if Contributor data terms are unsuitable

## Limitations of Muse Spark 1.2

- **Undisclosed architecture:** Meta has not published parameter count, model topology, expert routing, or training-token figures.
- **Harness-dependent launch results:** The strongest scores pair Muse Spark 1.2 with Muse Code while competitors use different coding products.
- **Private internal benchmark:** Meta Internal Coding Bench cannot be independently reproduced or audited by outside developers.
- **Uneven capability gains:** Independent evaluation shows much larger improvements in agentic work than in scientific reasoning.
- **Abstention trade-off:** A lower hallucination rate is accompanied by a lower attempt rate and slightly lower accuracy on AA-Omniscience.
- **Data-policy choice:** The cheapest Contributor tier may use submitted data to improve Meta products and may not suit sensitive code.
- **Long context is not perfect memory:** A 1M-token limit does not guarantee uniform retrieval, attention, or accuracy across every position.
- **Hosted launch:** The release package provides API and Muse Code access rather than downloadable model weights.

## How to Access Muse Spark 1.2

Developers can use Muse Spark 1.2 through [Muse Code](https://developer.meta.com/ai/products/muse-code/) or the [Meta Model API](https://developer.meta.com/ai/products/meta-model-api/). The standard API model ID is muse-spark-1.2; the lower-cost contributor route uses muse-spark-1.2-contributor. Meta's hosted API exposes an OpenAI-compatible base URL, allowing many existing chat-completions clients to be adapted with a different key, base URL, and model name.

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MODEL_API_KEY"],
    base_url="https://api.meta.ai/v1",
)

response = client.chat.completions.create(
    model="muse-spark-1.2",
    messages=[
        {"role": "user", "content": "Review this repository plan and identify the highest-risk implementation steps."}
    ],
)

print(response.choices[0].message.content)
```

**Implementation note:** Verify the active model name, account eligibility, rate limits, supported parameters, and regional availability in [Meta's API documentation](https://ai.developer.meta.com/docs/overview/) before deploying. Do not put an API key directly in source code.

For side-by-side testing, CometAPI already provides unified access to [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/), [GPT-5.6](https://www.cometapi.com/models/openai/gpt-5-6/), [Grok 4.5](https://www.cometapi.com/models/xai/grok-4-5/), and [Kimi K3](https://www.cometapi.com/models/moonshotai/kimi-k3/), which can simplify A/B testing and provider switching. Muse Spark 1.2 will also be available on CometAPI soon.

## Is Muse Spark 1.2 Worth Using?

Muse Spark 1.2 is worth testing when the workload is dominated by repository-scale coding, long-running execution, repeated tool feedback, and multi-agent coordination. Its strongest argument is the combination of a coding-specialized model, a purpose-built persistent agent, a 1M-token multimodal context, and low standard API pricing.

It is not the universal benchmark leader. [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/) remains ahead in Meta's headline coding evaluations, [GPT-5.6 Terra](https://www.cometapi.com/models/openai/gpt-5-6/) is highly competitive across coding and general production tooling, and independent data shows that Muse Spark 1.2's gains are concentrated rather than uniform. The best selection process is therefore workload-based: test each model inside the actual agent runtime, measure verified task completion, and include human review for security-sensitive or high-impact changes.

## **Bottom line:**

Muse Spark 1.2 is Meta's strongest coding-oriented Muse update so far. Its real differentiator is not one benchmark score, but how tightly the model, Muse Code, persistent subagents, long context, and verification loop are designed to work together.

---

*Originally published at [https://www.cometapi.com/what-is-muse-spark-1-2/](https://www.cometapi.com/what-is-muse-spark-1-2/).*
