<!-- social-ops-fingerprint:e621b826eac47d6580e6ccecd73417c45d53d828f0be326126b818491950d4b6 -->
---
title: What Is Claude Fable 5.2? Features, Benchmarks & Pricing
---
# What Is Claude Fable 5.2? Features, Benchmarks & Pricing

![What Is Claude Fable 5.2? Features, Benchmarks & Pricing](https://resource.cometapi.com/console/blog-banner/2026/11/c4cc4ef3a1414244806778010a6ebf49.webp)

## TL;DR

Claude Fable 5.2 is Anthropic’s frontier model for demanding reasoning and long-running agent work. Released on November 9, 2026, it combines a large context window with improved coding, research, and visual reasoning. For developers evaluating an upgrade, the key question is whether those capabilities improve completed work enough to justify the cost.

Its [standard API pricing of $8 per million input tokens and $40 per million output tokens](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2) is 20% below Fable 5.1. The sections below explain the model’s specifications, benchmark tradeoffs, and migration requirements so you can assess it against your own workload.

## Key Takeaways

* Claude Fable 5.2 supports a 1M-token context window, up to 128K output tokens, and text and image inputs.
* Its strongest use cases involve extended engineering and research tasks with tools, intermediate checks, and multiple stages.
* Published benchmarks show substantial gains over Fable 5.1, but results vary by task and reasoning effort.
* Direct API pricing is lower than Fable 5.1; Opus 5.5 remains a less expensive option for routine work.
* Migration requires checking conversation history, computer-use tools, model routing, and data-retention requirements.

## What Is Claude Fable 5.2?

Claude Fable 5.2 is Anthropic’s generally available frontier model for complex technical work. It is designed to sustain reasoning across extended sessions, coordinate tools and agents, and carry ambiguous projects through planning, execution, and verification.

Fable 5.2 is not simply a conversational model with a larger context window. Its positioning is closer to a technical lead or orchestrator for work that involves multiple stages, external tools, and repeated checks. It can also act as an advisor to smaller Claude models or delegate simpler subtasks to them.

### Claude Fable 5.2 Technical Specifications

| Specification         | Claude Fable 5.2                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| Developer             | Anthropic                                                                                                      |
| Release date          | November 9, 2026                                                                                               |
| Claude API model ID   | claude-fable-5-2                                                                                               |
| Model positioning     | Frontier reasoning and long-horizon agentic work                                                               |
| Context window        | 1,000,000 tokens                                                                                               |
| Maximum output        | 128,000 tokens                                                                                                 |
| Input modalities      | Text and images                                                                                                |
| Output modality       | Text                                                                                                           |
| Thinking              | Adaptive; always on                                                                                            |
| Default API effort    | High                                                                                                           |
| Knowledge cutoff      | June 2026                                                                                                      |
| Training data cutoff  | June 2026                                                                                                      |
| Standard input price  | $8 per million tokens                                                                                          |
| Standard output price | $40 per million tokens                                                                                         |
| Fast mode             | Up to 2.5× generation speed; $16/$80 per million input/output tokens                                           |
| Retirement commitment | Not sooner than November 9, 2027                                                                               |
| Availability          | Claude API, Amazon Bedrock, Claude Platform on AWS, Google Cloud, Microsoft Foundry; supported Claude products |

*Specifications and release details are based on the* [*Claude Platform model overview.*](https://platform.claude.com/docs/en/models/fable-5-2/overview)

### Always-On Adaptive Thinking

Fable 5.2 uses [always-on adaptive thinking](https://platform.claude.com/docs/en/models/fable-5-2/overview). You control reasoning depth with the effort setting rather than disabling thinking. The API defaults to High. Start with representative tasks and compare completion quality, latency, and token use across effort levels before choosing a setting for production.

Choose effort to match the job. The API offers Low, Medium, High, Xhigh, and Max, with High as its default. [Anthropic recommends High for most Fable 5.2 work](https://platform.claude.com/docs/en/build-with-claude/effort), Xhigh when harder tasks show a measurable benefit, and Max mainly for exploring the model’s ceiling. The Claude apps and Claude Code default to Medium, so compare settings explicitly when moving a workflow into the API.

## What Are the Main Features of Claude Fable 5.2?

### Long-Horizon Agentic Reasoning

Fable 5.2 is built to manage work that spans many connected steps rather than stopping after a plausible first answer. It can plan a task, coordinate specialized agents, review intermediate results, and change direction when evidence shows that an approach is not working.

In an Anthropic experiment, Fable 5.2 [coordinated more than 1,000 subagents over eight days](https://www.anthropic.com/claude-fable-and-mythos-5-2) to build a prototype operating system. It booted on a laptop and included drivers, permanent storage, a graphical interface, and an installer. This demonstrates the scale of work the model can coordinate; it does not establish that an unattended run will reliably produce production-ready software.

### Stronger Coding and Software Engineering

The model’s coding improvements extend beyond code completion. It can reason across repositories, investigate persistent bugs, migrate services, and continue testing and revising changes.

Anthropic reports that agents using an earlier Fable 5.2 version migrated a production service from Python to Rust, with [startup approximately 26 times faster](https://www.anthropic.com/claude-fable-and-mythos-5-2). For a development team, the relevant test is whether the model can navigate its own repository, preserve intended behavior, and produce changes that pass review.

### Faster Token Generation

Claude Fable 5.2 generates outputs up to 30% faster than Claude Fable 5.1, according to Anthropic's launch testing. Developers can also enable optional Fast Mode to increase token generation speed by up to 2.5 times, at twice the standard input and output token rates. However, faster generation does not necessarily mean an entire agent workflow finishes 2.5 times faster, since tool execution, external services, and approval steps also affect end-to-end latency.

### Scientific Research and Mathematical Reasoning

Anthropic reports that a team of Fable 5.2 agents [formalized Fermat’s Last Theorem in Lean in 30 hours](https://www.anthropic.com/claude-fable-and-mythos-5-2). The result illustrates a useful research pattern: combine model-generated reasoning with tools that can check intermediate work. For other domains, the corresponding checks may be executable calculations, reproducible experiments, or expert review.

### Hardware Design and Robotics

In a collaboration with Diode, Fable 5.2 [designed three electronic-device prototypes](https://www.anthropic.com/research/claude-electronics-design): a home voice-assistant hub, a USB speakerphone, and a handheld virtual pet. Its work covered specifications, circuit layouts, PCB routing, CAD enclosures, firmware, and parts lists.

Diode manufactured the boards from Claude’s design files. Anthropic reports that the prototypes worked without electrical modifications, although they remain early prototypes and have not completed commercial certification or full validation testing.

The strongest signal in these reported results is integration. Circuit designs, board layouts, enclosures, and firmware came together in physical prototypes, showing a path from a written brief to hardware that could be built and tested. For hardware teams, this makes Fable 5.2 a promising assistant for the first prototype cycle, especially when the challenge is coordinating several engineering disciplines.

Our assessment is that its clearest value lies in producing a coherent starting point for engineering validation. A useful pilot would ask it to deliver the schematics, PCB files, enclosure design, firmware, and parts list for a bounded device, then measure how much correction engineers need before the prototype passes defined tests. The examples support testing that workflow; they do not establish repeatable reliability or quantify time saved across other projects. Production release still requires separate evidence on durability, manufacturing consistency, and compliance.

![](https://ucnozuqvdmo4.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjY4YTgzOGNlMjc2MGE2ZGVkMzUzMTk2ODY2MDEyYmZfSUtuTDNSWWNnNzMzR2tuMENiMFVBSm40MGtGaWE5S1BfVG9rZW46VlYxWWJIQTJub2RIMm54TzZldWNwaWhxbndoXzE3OTQzMDU4NzI6MTc5NDMwOTQ3Ml9WNA\&add_watermark=true\&scene_type=CCM)

Anthropic’s photograph shows the handheld virtual pet, voice-assistant hub, and USB speakerphone built from Claude’s designs. [The hardware study](https://www.anthropic.com/research/claude-electronics-design) describes how the prototypes were built and tested.

## How Does Claude Fable 5.2 Perform on Benchmarks?

The first table collects Anthropic-reported results; the independent Artificial Analysis results follow below. Read each score alongside its effort level and test setup. The two sources evaluate different workloads, so their scores and task costs are not interchangeable.

| Benchmark                         | Fable 5.2           | Fable 5.1 | Opus 5.5 | GPT-6 Astra | Gemini 4 Carbon |
| --------------------------------- | ------------------- | --------- | -------- | ----------- | --------------- |
| FrontierCode 2.0                  | 49.1%               | 32.4%     | 45.5%    | 42.8%       | 41.1%           |
| FrontierSWE v2                    | 69.9%               | 56.3%     | 62.3%    | 65.5%       | 61.2%           |
| AutomationBench                   | 51.4%               | 31.4%     | 42.5%    | 41.4%       | 53.9%           |
| Terminal-Bench-Science 0.1        | 74.6%               | 52.6%     | 58.7%    | 68.1%       | 64.8%           |
| WANDR (relaxed score)             | 82.1%               | 68.7%     | 72.3%    | —           | —               |
| OSWorld 2.1 (offline partial set) | 89.3%               | 83.5%     | 87.2%    | 79.5%       | 81.5%           |
| RoboDojo Sim                      | 64.9%               | 27.6%     | 39.4%    | 29.8%       | —               |
| AA-Briefcase v1.1 (rubric)        | 66.1%               | 61.5%     | 61.2%    | 52.0%       | 61.8%           |
| AA-Briefcase v1.1 (Elo)           | 1785                | 1669      | 1800     | 1569        | 1611            |
| Remote Labor Index                | 41.3% (High effort) | 17.9%     | 21.3%    | 20.8%       | —               |
| Humanity’s Last Exam (with tools) | 74.2%               | 65.6%     | 67.7%    | 57.2%       | —               |
| Chartography (no tools)           | 73.4%               | 44.8%     | 64.4%    | 71.0%       | 72.5%           |

Unless noted otherwise, results use each model’s highest available effort; the Claude results use safeguards. FrontierCode 2.0 uses Xhigh for Fable 5.2 and Fable 5.1, and Medium for Gemini 4 Carbon. Fable 5.2’s RLI result uses High. OSWorld covers a partial offline set; RoboDojo Sim was run internally. HLE uses tools and Chartography does not. The [evaluation methodology in Anthropic’s System Card](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card) provides the fuller test setup; the table is not a controlled, identical-environment comparison across providers.

### Coding: FrontierCode 2.0 and FrontierSWE v2

The coding results favor Fable 5.2 in this comparison, making it a candidate for repository-level changes that require sustained execution. Validate that advantage with tasks resembling your own maintenance work, including failing tests, ambiguous requirements, and changes spanning several files.

### Computer Use and Business Workflows

The rankings vary across tasks: Fable 5.2 leads the listed OSWorld results, while Gemini 4 Carbon leads AutomationBench. Opus 5.5 also has the higher AA-Briefcase Elo score, despite Fable 5.2’s higher rubric score. A model that performs well in one workflow may not be the best choice for another; use the metric that reflects your intended outcome.

### Independent Results from Artificial Analysis

As of November 10, 2026, [Artificial Analysis’s Fable 5.2 evaluation](https://artificialanalysis.ai/models/claude-fable-5-2) uses the Max, Default Fallback configuration. Its Intelligence Index score is **65**, compared with a comparable-model median of **40**. The same evaluation reports **46.4 minutes** and **$26.54** per Intelligence Index task; the comparable-model median for time is **12.6 minutes**.

![](https://ucnozuqvdmo4.feishu.cn/space/api/box/stream/download/asynccode/?code=NGEzYjZjNTNmZDI1MjgzYTNmZmRiYThjNmExYmE5MDZfWnJOMGNENzVKVW9CanpmemNJMW1RYXJkaExCVUpnbWtfVG9rZW46UVd0Y2J4YlhCb2dldHh4TTRpNGM1OVBibjNnXzE3OTQzMDU4NzI6MTc5NDMwOTQ3Ml9WNA\&add_watermark=true\&scene_type=CCM)

*Artificial Analysis: Intelligence Index rankings and Intelligence Index versus cost per task. The cost axis in the lower chart is logarithmic. Source:* [*Artificial Analysis’s original post*](https://x.com/ArtificialAnlys/status/2119878995386982508)*.*

The practical tradeoff is stronger evaluated capability with a substantial time and cost commitment at Max. For interactive products, test whether High effort delivers acceptable answers sooner. For difficult background work, judge the model by the quality of the finished result. These task-level figures should not be read as ordinary chat response times or as an independent replication of Anthropic’s FrontierCode cost comparison.

## Claude Fable 5.2 vs Fable 5.1 vs Opus 5.5

| Dimension                  | Fable 5.2                     | Fable 5.1                                             | Opus 5.5                           |
| -------------------------- | ----------------------------- | ----------------------------------------------------- | ---------------------------------- |
| Primary positioning        | Frontier technical reasoning  | Long-running frontier agents                          | Premium daily-driver intelligence  |
| Context window             | 1M tokens                     | 1M tokens                                             | 1M tokens                          |
| Maximum output             | 128K tokens                   | 128K tokens                                           | 128K tokens                        |
| Input price / MTok         | $8                            | $10                                                   | $4                                 |
| Output price / MTok        | $40                           | $50                                                   | $20                                |
| Best fit                   | Hardest technical tasks       | Existing Fable workflows                              | Everyday coding and knowledge work |
| Adaptive thinking / effort | Always on; API default High   | Always on; tune effort against your existing workload | Always on; API default Medium      |
| Coding: FrontierCode 2.0   | 49.1% at Xhigh; 45.3% at High | 32.4% at Xhigh                                        | 45.5% at Max                       |
| Computer use: OSWorld 2.1  | 89.3%                         | 83.5%                                                 | 87.2%                              |

### Fable 5.2 vs. Fable 5.1

Fable 5.2 is a strong upgrade candidate for existing Fable 5.1 workflows: the reported coding and computer-use scores improve while standard input and output prices fall by 20%. The benefit is most relevant when an agent must complete a difficult sequence of actions. Replay your own repository tasks and desktop workflows before switching, because stronger benchmark results do not remove the conversation-history and computer-use compatibility changes described below.

### Fable 5.2 vs. Opus 5.5

Opus 5.5 remains a sensible starting point for everyday coding and document work, but cheaper tokens do not always produce a cheaper completed task. In [Anthropic’s FrontierCode 2.0 comparison](https://www.anthropic.com/claude-fable-and-mythos-5-2), Fable 5.2 at High scored **45.3%**, versus **45.5%** for Opus 5.5 at Max, at roughly **half the cost per task**. That result is specific to this benchmark and these effort settings. For your own codebase, compare total cost per accepted change, including retries and review, before choosing a default.

For desktop agents, the reported OSWorld 2.1 scores favor Fable 5.2 over both alternatives, but the test covers a partial offline set. That is useful evidence for a pilot, not proof of better performance in every business application. Opus 5.5’s higher AA-Briefcase Elo in the earlier table also shows why coding, computer use, and document quality should be evaluated separately.

## What Safety Limits Should You Expect?

Fable 5.2 adds strong safeguards around cybersecurity and biology while remaining broadly available. Anthropic says these protections are as robust as Fable 5.1’s, with fewer unnecessary blocks. [The release announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2) describes the model’s safety positioning.

A capable model can still decline a request. [Anthropic’s refusal documentation](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) lists cybersecurity, biology, competing-model development, internal-reasoning extraction, and other usage-policy categories; some legitimate work can also be flagged. For an application, a refusal is a separate outcome to handle, not a completed answer. The API can return HTTP 200 with **stop\_reason: refusal**, and partial output from a refused response should be treated as incomplete.

Measure refusal rates on representative, permitted tasks before deployment. Where a supported fallback is appropriate, record which model actually answered and include its cost in your evaluation. A fallback can change the capability delivered to the user. Refusals also count toward rate limits, and some categories are billed even when no answer is produced. [The refusal and billing rules](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) explain the exceptions.

For sensitive workloads, check data handling as well as answer quality: [Fable 5.2 requires 30-day data retention unless Anthropic expressly authorizes an exception](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2).

## How Much Does Claude Fable 5.2 Cost?

Anthropic bills input and output separately. Cache writes, cache reads, batch processing, and fast mode have different rates, so choose the row that matches how your application sends requests.

Standard API input and output rates are each **20% lower than Fable 5.1**: input falls from $10 to $8 per million tokens, and output from $50 to $40. [These are Anthropic’s direct API rates](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2); the separate CometAPI comparison below uses a different baseline.

| Pricing item                | Anthropic direct API rate |
| --------------------------- | ------------------------- |
| Standard input              | $8.00 / MTok              |
| Standard output             | $40.00 / MTok             |
| 5-minute prompt-cache write | $10.00 / MTok             |
| 1-hour prompt-cache write   | $16.00 / MTok             |
| Prompt-cache read           | $0.20 / MTok              |
| Batch input                 | $4.00 / MTok              |
| Batch output                | $20.00 / MTok             |
| Fast-mode input             | $16.00 / MTok             |
| Fast-mode output            | $80.00 / MTok             |

*Pricing is based on the* [*official Fable 5.2 pricing documentation.*](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)

### Example: Cost for 1 Million Input Tokens and 100,000 Output Tokens

| Model / mode        | Input cost | Output cost | Total  |
| ------------------- | ---------- | ----------- | ------ |
| Fable 5.2 standard  | $8.00      | $4.00       | $12.00 |
| Fable 5.1 standard  | $10.00     | $5.00       | $15.00 |
| Opus 5.5 standard   | $4.00      | $2.00       | $6.00  |
| Fable 5.2 fast mode | $16.00     | $8.00       | $24.00 |

For this example, Fable 5.2 saves $3 compared with Fable 5.1. Prompt caching can reduce costs further when an application repeatedly sends the same system instructions, tool definitions, or repository context.

### Claude Fable 5.2 Pricing Through CometAPI

Standard token pricing for [Claude Fable 5.2 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-fable-5-2/) is 20% below Anthropic’s standard API token rates: **$6.40 per million input tokens and $32 per million output tokens**, compared with Anthropic’s $8 and $40, respectively.

For the same workload of 1 million input tokens and 100,000 output tokens, the standard token cost through CometAPI is **$9.60**: $6.40 for input plus $3.20 for output. That saves $2.40, or 20%, compared with the $12 direct-API example above. This calculation covers standard input and output tokens; cache, batch, fast-mode, and any tool charges are outside the example.

## What Should Developers Check Before Migrating to Claude Fable 5.2?

Review the [Fable 5.2 migration requirements](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide) before changing a working integration. Pay particular attention to the platform you use, how your application constructs conversation history, and whether it switches between models. When Fable 5.2 is the executor in an advisor-tool workflow, the advisor must be Fable 5.2 or Mythos 5.2. A Fable 5.1 advisor is not accepted for this pairing.

### Thinking-Block Prefix Validation

Fable 5.2 checks whether the prefix preceding a thinking block has changed. Editing the system prompt, tools, or earlier messages can cause a 400 error when an old block is resent and prefix-mismatch behavior is left unset. Preserve the prefix, or use the [documented block-dropping recovery behavior](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide) while fixing the history-editing logic.

For applications that manage conversation history manually, keep the system prompt and tool definitions stable throughout a session, and append new messages instead of modifying earlier turns. Preserve every returned thinking block in its original order. If context changes are unavoidable, use Anthropic's documented prefix-mismatch recovery mechanism rather than repeatedly retrying the same invalid request.

### Thinking Blocks Are Model-Bound

On the Claude API and Google-managed Claude Models on Google Cloud, only Fable 5.2 and Mythos 5.2 can read Fable 5.2 thinking blocks. Switching to another model can drop that reasoning while leaving the request successful. Test conversation continuity when routing between models rather than assuming preserved message text also preserves reasoning.

### Update the Computer-Use Tool

The older computer\_20251124 tool returns a 400 error with Fable 5.2 [except on Amazon Bedrock](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide), where it continues to work as on Fable 5.1. On other platforms, migrate to computer\_toolset\_20260801 and adapt the agent loop to the newer interface.

### Review Data Retention and Request Parameters

Fable 5.2 requires [30-day data retention unless Anthropic expressly authorizes an exception](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2). Forced tool choice with types any or tool returns a 400 error; use supported auto or none settings as appropriate. Omit temperature, top\_p, and top\_k, set effort deliberately, and measure token use and latency again after migration.

## Who Should Use Claude Fable 5.2?

| Use case                             | Why it fits                                                                    | Recommendation      |
| ------------------------------------ | ------------------------------------------------------------------------------ | ------------------- |
| Large-scale software engineering     | Repository-level reasoning, debugging, migrations, and multi-step code changes | Excellent fit       |
| Scientific research                  | Tool-assisted analysis, mathematical reasoning, and research workflows         | Excellent fit       |
| Hardware engineering                 | Circuit design, PCB routing, CAD, and firmware planning                        | Strong fit          |
| Long-running autonomous agents       | Planning, orchestration, progress review, and recovery across many steps       | Excellent fit       |
| Technical and financial analysis     | Ambiguous, data-heavy work requiring judgment and verification                 | Strong fit          |
| Visual document analysis             | Chart, diagram, and technical image interpretation                             | Strong fit          |
| Routine customer support             | High-volume, repeatable responses                                              | Use a lighter model |
| Simple classification and extraction | Predictable tasks with limited reasoning requirements                          | Use a lighter model |

For everyday coding and general knowledge work, [Claude Opus 5.5](https://www.cometapi.com/models/anthropic/claude-opus-5-5/) is a practical starting point. For faster or higher-volume workloads, [Claude Sonnet 5.5](https://www.cometapi.com/models/anthropic/claude-sonnet-5-5/) and [Claude Haiku 5.5](https://www.cometapi.com/models/anthropic/claude-haiku-5-5/) offer lower-cost alternatives. A model-routing strategy can reserve Fable 5.2 for tasks where its additional reasoning produces measurable value.

## Conclusion

Fable 5.2 makes the strongest case for difficult engineering and research work where repeated attempts are expensive. Its lower rates relative to Fable 5.1 strengthen the upgrade case, while the FrontierCode result shows why Opus 5.5’s lower token price is only part of the decision. Start with High effort, measure accepted results and total workflow cost, and increase effort only where it helps. Before deployment, test refusals and migration behavior alongside accuracy. Keep routine work on a less expensive model when the added capability does not improve the outcome.

## FAQ

### Can Claude Fable 5.2 fast mode accelerate every agent task?

No. Faster token generation affects only part of an agent run. Tool execution, network requests, external approvals, and repeated attempts also contribute to elapsed time. Measure the complete workflow before paying for fast mode; a task that spends most of its time waiting on tools may see a smaller improvement than a generation-heavy task.

### Does Claude Fable 5.2 need access to my entire repository?

Give the agent the context and permissions its task requires. Start with the relevant files, build instructions, and tests, then let it retrieve additional material when needed. A large context window does not make unrelated files useful, and it does not determine what the agent should be allowed to change. Keep secrets out of supplied context and define the boundaries for tool actions.

### How should I budget a multi-agent Claude Fable 5.2 workflow?

Track the whole workflow, including the coordinating model, delegated agents, repeated context, and retries. Set a budget for the task rather than for a single model response, and log where token use accumulates. Compare that total with the value of the accepted deliverable; a low-cost individual call can still belong to an expensive run.

### Can Claude Fable 5.2 benchmarks predict performance on my documents?

They provide evidence about the evaluated tasks, but your documents may have different layouts, terminology, scan quality, or answer requirements. Build a sample from the material your users actually submit, include difficult and incomplete inputs, and check results against known answers. This reveals whether the model’s published strengths transfer to your application.

### What is the difference between Claude Fable 5.2 and Claude Mythos 5.2?

They share the same underlying model. Fable 5.2 is broadly available with stronger cybersecurity and biology safeguards; Mythos 5.2 is available to organizations approved through Anthropic’s verification programs for relevant work. [The distinction is access and safeguards](https://www.anthropic.com/claude-fable-and-mythos-5-2), rather than a separate base model. [Anthropic’s model overview](https://platform.claude.com/docs/en/models/fable-5-2/overview) confirms their shared specifications and pricing.

### Claude Fable 5.2 vs Opus 5.5: which should I choose?

Start with Opus 5.5 for routine work and evaluate Fable 5.2 for the difficult cases. [Their standard API rates](https://platform.claude.com/docs/en/models/fable-5-2/overview) are $4/$20 and $8/$40 per million input/output tokens, respectively. For demanding coding tasks, use the High-versus-Max FrontierCode comparison above as a reason to test Fable, then choose based on accepted results, latency, and total task cost in your own workflow.

---

*Originally published at [https://www.cometapi.com/what-is-claude-fable-5-2/](https://www.cometapi.com/what-is-claude-fable-5-2/).*
