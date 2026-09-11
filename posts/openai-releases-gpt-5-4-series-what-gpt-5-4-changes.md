<!-- social-ops-fingerprint:da76f8a807eff0d31ef5a4e38d308ebf9cd920ef75263851ec9df16bdee07fb4 -->
---
title: OpenAI Releases GPT-5.4 Series: what GPT-5.4 changes
---
# OpenAI Releases GPT-5.4 Series: what GPT-5.4 changes

![OpenAI Releases GPT-5.4 Series: what GPT-5.4 changes](https://resource.cometapi.com/GPT-5.4%20(1).webp)

OpenAI’s latest release, **GPT-5.4**, arrives as a targeted “professional work” model family with two primary variants — **GPT-5.4 Thinking** and **GPT-5.4 Pro** — and a heavy emphasis on long-context document work, native computer-use (agent) capabilities, and improved factuality and task performance across office, legal and finance workflows. The release follows earlier updates in the GPT-5 line (notably GPT-5.3 Instant and GPT-5.3-Codex) and brings measurable improvements on internal and public benchmarks, deeper tool integration (including a ChatGPT for Excel plug-in), and a larger supported context ( cites up to 1 million tokens).

Now CometAPI supports [GPT-5.4](https://www.cometapi.com/models/openai/gpt-5-4/) and [GPT-5.4 Pro](https://www.cometapi.com/models/openai/gpt-5-4-pro/), and use them in discounts.

## What is GPT-5.4?

### Positioning and variants

GPT-5.4 is presented by OpenAI as the most capable GPT-5-series model tuned for **professional, document-heavy, and agentic workflows**. It is offered in at least two published flavors:

- **GPT-5.4 Thinking** — a reasoning-focused variant that exposes more of the model’s thought process and is optimized for multi-step reasoning and agentic tasks (available within ChatGPT as the “Thinking” mode).
- **GPT-5.4 Pro** — a higher-compute/priority inference tier for high throughput or latency-sensitive enterprise workloads, with higher API pricing (reflecting the extra compute).

OpenAI highlights GPT-5.4’s native **computer-use** capabilities — enabling models to operate software through programmatic mouse/keyboard actions and to orchestrate multi-tool sequences — which is positioned as a step change for building real task-completing agents.

### New and emphasized capabilities

- **Long context support:** GPT-5.4 is reported to support very large contexts ( support up to 1,000,000 tokens in ChatGPT and Codex contexts), enabling the model to keep enormous projects, books, codebases or datasets “in memory” during a session. This is transformational for document review, legal contracts, and multi-file engineering projects.
- **Native computer-use / agenting:** GPT-5.4 is OpenAI’s first general-purpose model with native computer-use capabilities — it can generate sequences of UI actions and code to operate software (e.g., via Playwright or by issuing mouse/keyboard commands informed by screenshots). This capability is designed to let developers build agents that complete tasks across web and desktop apps.
- **Office skill improvements:** Significant emphasis on spreadsheets, presentations and documents — with internal benchmarks showing large gains in spreadsheet modeling, presentation aesthetics and document drafting quality.
- **Factuality and hallucination reduction:** OpenAI reports reductions in factual errors relative to previous models on internally curated evaluation sets (see benchmarks below).

Compared with previous models like GPT-5.2 Thinking and GPT-5.3 Codex, GPT-5.4 merges these capabilities into a single model designed to handle long-running tasks and complex workflows with minimal user intervention.

## Key features and technical highlights of GPT-5.4

### 1) Massive context windows (up to 1,000,000 tokens)

The most immediately visible capability is support for **context windows up to 1,000,000 tokens** via the API. This expands what a single model session can hold: entire books, long codebases, or whole multi-document dossiers without chunking across many calls. For knowledge-intensive enterprise workflows (legal discovery, research synthesis, large-scale code analysis), the ability to maintain a million-token context reduces engineering glue and improves coherence.

**Implication:** workflows that previously required orchestration (retrieval, chunking, external memory) can now keep more of the raw context in the model’s working memory — simplifying pipelines and lowering latency/consistency tradeoffs.

### 2. Native computer and tool use

OpenAI highlights a stronger ability to operate software tools and connectors (e.g., spreadsheets, document editors, code execution environments) more robustly than prior models. GPT-5.4 extends prior “tool-using” work with:

- Better tool selection and tool parameterization.
- More reliable sequence planning when calling external APIs or stepping through UI-like actions.
- Reduced token overhead for agentic workflows via smarter tool-call architecture.

Agentic and developer capabilities:

- **Desktop and web automation:** With explicit support for issuing mouse and keyboard actions informed by screenshots, GPT-5.4 can be embedded in agents that operate real software workflows (for example populating forms, navigating dashboards, or running multi-step procedures). OpenAI reports state-of-the-art results on OS-style benchmarks.
- **Tooling interface and steerability:** GPT-5.4 is more steerable via developer messages and can better decide when and how to call external tools, connectors and APIs — a crucial capability for building reliable multi-tool agents that minimize unnecessary or risky actions.

**Practical impact:** Automation tasks (e.g., “open this spreadsheet, compute these pivots, generate slide notes”) require fewer fail/retry cycles and lower human supervision.

### 3) Five reasoning effort levels, extreme modes

OpenAI indicate **multiple reasoning effort levels** — allowing users to trade latency/cost for deeper internal chain-of-thought computation (modes sometimes referred to informally as xhigh or extreme reasoning). These are intended for problems where more internal deliberation materially improves correctness (complex proofs, long code transformations, multi-step financial analyses). The API pricing and billing logic reflect the added model work performed under these modes.

**Practical impact:** This separation lets customers choose the tradeoffs appropriate to their workloads instead of asking a single model to be “everything.”

### 4) Productivity and content authoring

- **Spreadsheet modeling:** GPT-5.4 shows strong improvements on spreadsheet tasks likely to be used in auditing, finance and analysis workflows. OpenAI reports a mean score of **87.3%** on internal “investment banking modeling” style tasks for GPT-5.4 vs. **68.4%** for GPT-5.2. That’s a dramatic lift in task-level accuracy for numeric modeling and formula construction.
- **Presentations and visual output:** Human raters preferred presentations generated by GPT-5.4 68.0% of the time over those from GPT-5.2 due to better aesthetics, variety, and integration with image generation. This reflects both content and form improvements for producing slide decks.
- **Document drafting and long writing:** GPT-5.4 was optimized for maintaining consistency across long documents, better citation behavior and fewer internal contradictions when handling large contexts, thanks to the extended context window and dedicated reasoning tuning.

### 5) Safety, mitigations and cyber considerations

- **Reduced hallucinations:** OpenAI reports that on a set of de-identified prompts where users flagged factual errors, **individual claims** from GPT-5.4 are **33% less likely to be false**, and **full responses** are **18% less likely to contain any errors**, relative to GPT-5.2 — a key metric for enterprise adoption where factual accuracy matters.
- **Cybersecurity mitigations (Thinking variant):** The GPT-5.4 Thinking highlights an expanded mitigation set for cyber risks, building on protections used for prior Codex/5.3 models. GPT-5.4 Thinking was designed with additional guardrails for high-capability misuse scenarios .

## Performance benchmarks — what the numbers say

OpenAI and several outlets published early benchmark results as part of the rollout. Because different benchmarks test different capabilities (web navigation vs. domain knowledge vs. safety), it’s useful to aggregate the main numbers and what they mean.

![OpenAI Releases GPT-5.4 Series: what GPT-5.4 changes](https://resource.cometapi.com/blog/uploads/2026/03/GPT-5.4.webp)

Reported results show notable improvements vs. earlier GPT-5.x family members and close competition with other top-tier models.

### Web and desktop interaction benchmarks

- **WebArena-Verified (browser use tests):** GPT-5.4 achieves **67.3% success** when using both DOM and screenshot signals, compared with GPT-5.2’s **65.4%** — a visible but not overwhelming lift. This measures tasks where the model must interact with live pages and UI elements.
- **Online-Mind2Web (screenshot-based browser tasks):** GPT-5.4 reached **92.8%** success using screenshot observations alone — an especially strong improvement relative to previous agent-style baselines (OpenAI contrasted this with ChatGPT Atlas’ Agent Mode performance).
- **OSWorld-Verified (desktop navigation):** independent reporting indicated GPT-5.4 scoring **75.0%** on a benchmark assessing desktop environment navigation and task completion. That result positioned 5.4 ahead of many public baselines for end-to-end automation tasks.

**Takeaway:** 5.4’s improvements are most pronounced where understanding visual context, UI affordances, and long action sequences matter — i.e., agentic workflows.

### Health, safety and knowledge benchmarks

OpenAI’s deployment safety reporting shows mixed signals:

- **HealthBench:** GPT-5.4 scored **62.6%** on HealthBench (a modest decline from GPT-5.2’s 63.3%), indicating subtle tradeoffs between capability and certain health-related evaluation metrics in the snapshot tests OpenAI reported.
- **Hard:** GPT-5.4 scored **40.1%** on a “Hard” evaluation suite (down slightly from 42.0%).
- **Consensus:** GPT-5.4 posted **96.6%** on “Consensus,” a metric reflecting agreement with curated consensus answers (an increase of ~2.1 points).

OpenAI also noted changes in average response length on health evaluations (GPT-5.4 averaged ~3,311 characters vs. 2,676 for GPT-5.2), which can affect how a model frames sensitive topics.

**Interpretation:** The safety and health metrics show that 5.4 overall increased consensus alignment and changed answer verbosity, even while some narrow health scores dipped slightly. That pattern often reflects rebalancing model objectives — more decisive, longer form answers may help utility and consensus while requiring careful monitoring on sensitive domains.

### Domain-specific examples and claims

Early tests provided concrete, domainized claims (OpenAI and third-party sources):

- **Legal reasoning benchmark (BigLaw Bench)** — GPT-5.4 achieving **~91%** on legal reasoning slices in early tests, a strong signal for document analysis tasks; note these are early, non-peer-reviewed figures.
- **Hallucination reductions:** GPT-5.4 responses are **~33% less likely** to contain false claims and **~18% less likely** to contain factual errors compared with certain prior baselines. These percentages were highlighted in secondary reporting and company communications; as with any such claim, they depend on the benchmark suite and sampling methodology.

## How to get and pay for GPT-5.4

### ChatGPT tiers and enterprise access

Per OpenAI and product reporting:

- **ChatGPT Plus / Team / Pro** users were the immediate groups to receive GPT-5.4 Thinking in the product. **Enterprise** and **Education** administrators can enable early access through admin controls. Free/Go users are not guaranteed immediate access. Developers can call the `gpt-5.4` and `gpt-5.4-pro` endpoints via the API.

### API pricing snapshot (published developer pricing)

OpenAI’s developer pricing lists GPT-5.4 as a frontier model with per-token charges. As published on the public pricing page at the time of the announcement, sample rates for GPT-5.4 are approximately:

| Model | Input | Cached input | Output |
| --- | --- | --- | --- |
| gpt-5.4 (<272K context length) | $2.50 | $0.25 | $15.00 |
| gpt-5.4 (>272K context length) | $5.00 | $0.50 | $22.50 |
| gpt-5.4-pro (<272K context length) | $30.00 |  | $180.00 |
| gpt-5.4-pro (>272K context length) | $60.00 |  | $270.00 |

In CometAPI(a one-stop aggregation platform for large model APIs):

| Model | Comet Price (USD / M Tokens) | Official Price (USD / M Tokens) | Discount |
| --- | --- | --- | --- |
| gpt-5.4 | Input:$2/M; Output:$16/M | Input:$2.5/M; Output:$20/M | -20% |
| gpt-5.4-pro | Input:$24/MOutput:$192/M | Input:$30/MOutput:$240/M | -20% |

Therefore, I highly recommend CometAPI, as it can greatly reduce API costs.

### Cost management considerations

If you plan to use the model at scale, particularly in long-document or high-throughput settings, you should consider:

- **Caching and deduplication** of inputs (to use cached input pricing where possible).
- **Prompt engineering** to compress context and avoid redundant tokens.
- **Batching strategies** and post-processing that minimize expensive output generation.
- **Monitoring reasoning mode usage**, since deeper reasoning modes can carry higher computational cost.

## Comparison: GPT-5.4 vs GPT-5.3

### Where GPT-5.4 improves on GPT-5.3

- **Reasoning depth and tool orchestration:** 5.4 Thinking was explicitly tuned to out-perform 5.3 on multi-step reasoning and agentic use cases. This shows in web/desktop interaction benchmarks and agent success metrics.
- **Context capacity:** 5.4’s 1M token offering is a clear technical step beyond what 5.3 provided in mainstream API availability, enabling new classes of single-session tasks.
- **Domain performance lifts:** OpenAI’s early numbers and third-party reports point to improvements on certain legal and document benchmarks, where 5.4’s longer context and specialized tuning help.

### Tradeoffs and where 5.3 might still be preferable

- **Lightweight conversational use:** [GPT-5.3 Instant](https://www.cometapi.com/models/openai/gpt-5-3-chat-latest/) remains optimized for quick, economical conversational flows; organizations seeking the smallest latency/cost for short chat interactions may prefer it.
- **Stability of safety metrics:** some health and “hard” evaluation scores showed slight declines for 5.4 versus 5.2 in OpenAI’s snapshots; enterprises in sensitive regulated domains should validate the model on their own evaluation suites before full rollout.

## Use cases and industry implications

GPT-5.4’s combination of deep reasoning, long-context memory, and tool usage opens several practical and strategic opportunities.

### 1. Professional services and consulting

Firms producing long deliverables (e.g., legal briefs, multi-chapter consulting reports, M&A diligence packs) can keep entire documents and datasets in context, allowing coherent cross-document synthesis, automated QA, and generation of executive summaries without manual chunk stitching. Benchmark wins on APEX-Agents align with this positioning.

### 2. Software engineering and code-base reasoning

Longer context means a single model call can include whole repositories or long traces of logs. GPT-5.4’s SWE benchmark improvements indicate better performance for debugging, refactoring, and code review workflows — especially when coupled with Pro for sustained loads.

### 3. Autonomous agents and enterprise automation

Agentic systems that operate over tools (spreadsheets, ticketing systems, web interfaces) benefit from GPT-5.4’s improved tool selection, reduced token overhead for agent workflows, and improved long-term state preservation. This makes GPT-5.4 attractive for enterprise automation pipelines and “assistants that act” across multiple systems.

## Bottom line — what GPT-5.4 changes

GPT-5.4 represents a pragmatic and capability-driven advance toward models that can handle **long, multi-document reasoning**, execute **agentic workflows** with greater reliability, and be scaled into professional pipelines via Pro contracts. For organizations whose workflows are long-horizon and tool-dependent, GPT-5.4 is a step-change in potential productivity

Developers can access [GPT-5.4](https://www.cometapi.com/models/openai/gpt-5-4/), [GPT-5.4-pro](https://www.cometapi.com/models/openai/gpt-5-4-pro/), and [GPT 5.3 Chat](https://www.cometapi.com/models/openai/gpt-5-3-chat-latest/) via [CometAPI](https://www.cometapi.com/) now.To begin, explore the model’s capabilities in the [Playground](https://blendspace.ai/chat) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up fo GPT-5.4 today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/openai-releases-gpt-5-4-series-what-gpt-5-4-changes/](https://www.cometapi.com/openai-releases-gpt-5-4-series-what-gpt-5-4-changes/).*
