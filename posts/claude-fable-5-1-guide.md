<!-- growth-fingerprint:5df79c6522ef7360f5c221b6c9abc5d2f32c940ab92d3c87697977a548c47729 -->
---
title: What Is Claude Fable 5.1? Features, Benchmarks, Pricing, and Access
---

# What Is Claude Fable 5\.1? Features, Benchmarks, Pricing, and Access

Anthropic [released Fable 5\.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) on September 1, 2026 as its most capable generally available model for coding and knowledge work\. The model targets long\-horizon jobs: multi\-hour coding, multi\-step research, document\-heavy professional work, and agents that repeatedly use tools while retaining large amounts of context\.

[Claude Fable 5\.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) combines a [1M\-token context window](https://platform.claude.com/docs/en/models/fable-5-1/overview), up to 128K output tokens, text\-and\-image input, and always\-on adaptive thinking\. Base pricing remains [$10 input and $50 output per MTok](https://platform.claude.com/docs/en/models/fable-5-1/overview); the important cost change is [$0\.25 per MTok for cache reads](https://platform.claude.com/docs/en/models/fable-5-1/overview)\.

## At glance Claude Fable 5\.1 Specifications

The specifications below come from [Anthropic’s model documentation](https://platform.claude.com/docs/en/models/fable-5-1/overview)\. Prices are Anthropic list prices and should be kept separate from any CometAPI price\.

|[Official specification](https://platform.claude.com/docs/en/models/fable-5-1/overview)|[Claude Fable 5\.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/)|
|---|---|
|Release and model ID|September 1, 2026 — claude\-fable\-5\-1|
|Primary role|Demanding reasoning and long\-horizon agentic work|
|Context and maximum output|1M\-token context — up to 128K output|
|Input → output|Text and images → text|
|Thinking and default API effort|Adaptive thinking, always on — High effort|
|Reliable knowledge cutoff|June 2026|
|List pricing|$10 input — $50 output — $0\.25 cache read per MTok|

Two details matter beyond the raw numbers\. The 1M context window is available by default rather than as a special long\-context tier\. Adaptive thinking is always on, while effort controls how much work the model performs; Anthropic says the default is High in Claude Code and Medium in Claude Cowork and Claude\.ai\.

## What is Claude Fable 5\.1

[Claude Fable 5\.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) is Anthropic's frontier model for jobs where a system must keep reasoning, using tools, and preserving context over many steps\. Rather than targeting short question\-and\-answer exchanges, it is designed for sustained execution: exploring a codebase, running terminal workflows, synthesizing large document sets, and completing professional tasks that may take hours\.

Its defining package is a [1M\-token context window with up to 128K output](https://platform.claude.com/docs/en/models/fable-5-1/overview), text\-and\-image input, and adaptive thinking that remains enabled throughout a request\. This lets an agent keep lengthy instructions, source material, tool results, and intermediate decisions in one working context while adjusting reasoning effort to the difficulty of each step\.

The best fit is a high\-value workflow in which failure, rework, or lost context costs more than premium token pricing\. Examples include repository\-scale engineering, multi\-stage research, computer\-use agents, compliance\-heavy document analysis, and business automation with repeated tool calls\. For routine classification, high\-volume extraction, or latency\-sensitive chat, a lower\-cost Claude tier may remain the better starting point\.

Default Fable use requires 30\-day retention for safety monitoring\. Eligible enterprise customers can use zero data retention while Enterprise Frontier Safeguards roll out; Anthropic says the planned architecture stores monitored data in customer\-controlled cloud infrastructure\. Regulated teams should verify account\-specific terms before deployment\.

## Claude Fable 5\.1 vs\. Fable 5: What Changed?

The 5\.1 release is not a uniform capability jump\. The clearest changes are lower repeated\-context cost and much stronger execution on agentic research, terminal coding, and business workflows, while general tool\-assisted reasoning moves only slightly\.

|[Dimension](https://www.anthropic.com/claude-fable-and-mythos-5-1)|[Claude Fable 5](https://www.cometapi.com/models/anthropic/claude-fable-5/)|[Claude Fable 5\.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/)|Change|
|---|---|---|---|
|Base input / output|$10 / $50 per MTok|$10 / $50 per MTok|No change|
|Cache read|$1\.00 per MTok|$0\.25 per MTok|75% lower|
|Terminal\-Bench\-Science 0\.1|24\.7%|52\.6%|\+27\.9 points|
|Terminal\-Bench 4\.0|42\.0%|55\.8%|\+13\.8 points|
|AutomationBench|17\.1%|31\.4%|\+14\.3 points|
|HLE with tools|63\.8%|65\.0%|\+1\.2 points|

### Cache reads are 75% cheaper while base prices stay flat

Input remains $10 per MTok and output remains $50 per MTok, so the headline rate did not fall\. The material change is the [cache\-read price dropping from $1\.00 to $0\.25 per MTok](https://www.anthropic.com/claude-fable-and-mythos-5-1)\. This matters most for agents that repeatedly reload a long prefix containing repositories, policies, documents, tool definitions, and prior state\. Their cost per completed workflow can decline even when fresh\-input and output rates do not\.

### Agentic scientific research shows the largest gain

Terminal\-Bench\-Science 0\.1 rises from 24\.7% to 52\.6%, a gain of 27\.9 percentage points and more than double the previous score\. This is the strongest evidence that Fable 5\.1 improves long\-horizon execution: planning an investigation, operating tools, interpreting results, and recovering from intermediate errors\.

### Terminal coding and business automation improve materially

Terminal\-Bench 4\.0 increases from 42\.0% to 55\.8%, while AutomationBench rises from 17\.1% to 31\.4%\. These results point to better end\-to\-end task completion, not merely better code generation\. Teams should expect the greatest benefit in workflows that require the model to inspect an environment, choose actions, use tools, and verify outcomes across multiple steps\.

### General reasoning improves less than execution

Humanity?s Last Exam with tools moves from 63\.8% to 65\.0%, only 1\.2 points, and CursorBench increases by 2\.9 points\. The comparison therefore does not support a blanket claim that every capability improved equally\. Fable 5\.1 is better understood as an execution\-focused upgrade whose strongest gains appear when reasoning must be sustained through tools and long task chains\.

**Comparison result:** Existing Fable 5 users running long, tool\-heavy agents have the clearest reason to upgrade: substantially cheaper cache reads and fewer failures on execution\-oriented benchmarks\. Teams using short prompts or general knowledge tasks should validate the smaller gains against latency and total cost before migrating\.

## Benchmark performance of Claude Fable 5\.1

Anthropic’s [official benchmark table](https://www.anthropic.com/claude-fable-and-mythos-5-1) compares the new model with its predecessor, [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/), and [GPT\-5\.6 Sol](https://www.cometapi.com/models/openai/gpt-5-6/)\. The selected rows below cover research, coding, knowledge work, computer use, and automation\.

|[Official benchmark](https://www.anthropic.com/claude-fable-and-mythos-5-1)|[Claude Fable 5\.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/)|[Claude Fable 5](https://www.cometapi.com/models/anthropic/claude-fable-5/)|[Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/)|[GPT\-5\.6 Sol](https://www.cometapi.com/models/openai/gpt-5-6/)|
|---|---|---|---|---|
|Terminal\-Bench\-Science 0\.1|52\.6%|24\.7%|29\.0%|22\.4%|
|Terminal\-Bench 4\.0|55\.8%|42\.0%|52\.3%|37\.3%|
|GDPval\-AA v2|1853|1723|1824|1711|
|OSWorld 2\.0 partial|77\.9%|72\.9%|75\.4%|—|
|OSWorld 2\.0 strict|41\.7%|36\.1%|39\.6%|—|
|AutomationBench|31\.4%|17\.1%|26\.9%|19\.6%|
|CursorBench 3\.2\.0|73\.4%|70\.5%|70\.0%|67\.2%|

The graphic above is the official Anthropic benchmark image copied from the source document, not a locally redrawn chart\. Anthropic notes a [±3\.5–4\.5 point standard error](https://www.anthropic.com/claude-fable-and-mythos-5-1) for Terminal\-Bench\-Science and says production safeguards were enabled during evaluation\. Small differences should therefore be treated cautiously\.

![test\.jpg](Images_attachments/test.jpg)

*Source:*[*Official Anthropic Fable 5\.1 benchmark graphic*](https://www.anthropic.com/claude/fable)

### How to read the benchmark results

These scores should not be interpreted as universal measures of model quality\. Anthropic evaluated Claude Fable 5\.1 with production safeguards enabled, and some benchmark tasks may be affected by safeguard interventions\. Terminal\-Bench\-Science also reports a standard error of approximately ±3\.5–4\.5 percentage points per model\.

OSWorld 2\.0 results use the benchmark authors' August 2026 task release, so they should not be directly compared with scores from earlier task releases\.

## Claude Fable 5\.1 Pricing

### Input and output pricing

~~Anthropic lists Claude Fable 5\.1 at ~~[~~$10 per MTok of input and $50 per MTok of output~~](https://platform.claude.com/docs/en/models/fable-5-1/overview)~~\.~~~~ CometAPI currently lists the same model~~~~ at ~~[~~$8 per MTok of input and $40 per MTok of output~~](https://www.cometapi.com/models/anthropic/claude-fable-5-1/)~~, a 20% reduction from the official list rates\. These are usage\-based rates; check the live model page before production because platform prices and billing rules can change\.~~

Developers can access Claude Fable 5\.1 API through CometAPI with usage\-based pricing of $8 per MTok of input and $40 per MTok of output\. Compared with [Anthropic’s official Claude Fable 5\.1 API pricing](https://platform.claude.com/docs/en/models/fable-5-1/overview?utm_source=chatgpt.com) of $10 per MTok of input and $50 per MTok of output, CometAPI provides a 20% lower entry cost while maintaining access to the same Claude Fable 5\.1 model capabilities through its API infrastructure\. [Claude Fable 5\.1 API on CometAPI](https://www.cometapi.com/models/anthropic/claude-fable-5-1/?utm_source=chatgpt.com) supports usage\-based billing, and developers should verify the latest API configuration, supported features, and pricing before production deployment\.

### Prompt cache pricing

Anthropic prices a 5\-minute cache write at $12\.50 per MTok, a 1\-hour cache write at $20 per MTok, and a [cache read at $0\.25 per MTok](https://platform.claude.com/docs/en/models/fable-5-1/overview)\. The read rate is 75% below Fable 5's $1 per MTok, so long\-running agents that reuse repositories, policies, tool definitions, or prior state benefit more than short, one\-off prompts\.

### Example agent workflow cost

An agent that reads 150K cached tokens on each of 1,000 steps consumes 150 MTok of cache reads\. At Fable 5\.1's $0\.25 rate, that component costs $37\.50; at Fable 5's $1 rate, it would cost $150—a $112\.50 saving\. Fresh input, output, cache writes, and platform charges remain additional, so teams should compare total cost per successful workflow rather than cache cost alone\.

### Why cache pricing changes agent economics

A conventional request may spend most of its bill on fresh input and output\. An agent is different: every tool step can re\-read a large cached prefix containing policy, code, documents, tool definitions, and earlier state\. Anthropic’s [75% cache\-read reduction](https://www.anthropic.com/claude-fable-and-mythos-5-1) disproportionately benefits long loops\.

For example, an agent that re\-reads 150K cached tokens across 1,000 steps consumes 150 million cache\-read tokens\. At $1 per MTok, that component costs $150; at $0\.25 per MTok, it costs $37\.50\. This example excludes fresh input, output, cache writes, and platform charges, but it shows why unchanged base prices can still produce a lower cost per completed task\.

Anthropic estimates [about 25% lower cost](https://www.anthropic.com/claude-fable-and-mythos-5-1) for typical token\-billed workloads and up to approximately 45% for highly agentic workloads\. These are workload\-mix estimates, not a universal discount on every token\.

## Claude Fable 5\.1 vs Opus 5 vs Sonnet 5

The frontier model is the capability ceiling, but Anthropic recommends the Opus tier as the starting point for most workloads\. The Sonnet tier remains the faster, lower\-cost choice when throughput and latency matter more than maximum long\-horizon reliability\. For a deeper two\-model analysis, see CometAPI’s [Fable vs Sonnet comparison](https://www.cometapi.com/claude-fable-5-vs-claude-sonnet-5-which-is-better/)\.

|Dimension|[Claude Fable 5\.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/)|[Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/)|[Claude Sonnet 5](https://www.cometapi.com/models/anthropic/claude-sonnet-5/)|
|---|---|---|---|
|Context window|1M|1M|1M|
|Maximum output|128K|128K|128K|
|Input / output list price|$10 / $50|$5 / $25|$2 / $10|
|Comparative latency|Slower|Moderate|Fast|
|Best fit|Hardest long\-horizon agents and reasoning|Default premium starting point|High\-volume work prioritizing speed and cost|

**Selection result:** Start with the lower\-cost tier that meets the task\. Escalate only when production evaluations show that the frontier model raises accepted\-result rate, reduces retries, or lowers total cost per successful workflow\.

## Migration changes developers must test

The new model is mostly a drop\-in successor, but Anthropic documents [three breaking changes](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) that affect agent frameworks and long conversations\.

|[Migration change](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)|What happens|Required developer action|
|---|---|---|
|Forced tool choice|tool\_choice = any or a named tool returns HTTP 400|Use auto, instruct the model, and enforce strict schemas when needed|
|Thinking blocks across model switches|Older models cannot read the new thinking blocks|Test routers and expect reasoning blocks to be dropped when routing backward|
|Editing earlier turns|Changed history can invalidate thinking blocks|Keep histories append\-only or use supported compaction patterns|

Also test per\-message effort, turn\-scoped system messages, progress updates between tool calls, cache behavior, and content provenance before moving production traffic\. The existing [Fable API tutorial](https://www.cometapi.com/how-to-use-claude-fable-5-api/) remains the better place for generic SDK setup and request examples\.

## Who Should Use Claude Fable 5\.1?

[Claude Fable 5\.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) is best for workloads where sustained reasoning and successful completion matter more than minimum latency or token price\. Choose it when the task spans many steps, repeatedly uses tools, or carries enough business value that avoiding failed runs and rework can offset premium model costs\.

- **Repository\-scale engineering:** debugging, migrations, multi\-file refactoring, test execution, and unattended coding agents\.
- **Multi\-step research:** searching, evaluating evidence, running analyses, and producing a grounded final report\.
- **Large\-document and professional work:** contracts, technical documentation, financial material, spreadsheets, and presentation workflows\.
- **Computer\-use and automation:** tasks that require repeated tool calls, interface navigation, verification, and recovery from intermediate errors\.

For routine classification, high\-volume extraction, or latency\-sensitive chat, start with [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/) or [Claude Sonnet 5](https://www.cometapi.com/models/anthropic/claude-sonnet-5/)

## Availability through CometAPI

As of September 4, 2026,  the [CometAPI model page lists Claude Fable 5\.1 as live and operational](https://www.cometapi.com/models/anthropic/claude-fable-5-1/)\. The model ID is `claude-fable-5-1`\.

1. Create or sign in to a CometAPI account and generate an API key in the dashboard\.
2. Select Claude Fable 5\.1 and pass `claude-fable-5-1` as the model ID\.
3. Send requests through the Anthropic\-compatible `/v1/messages` endpoint or the OpenAI\-compatible `/v1/chat/completions` endpoint\.
4. Run a production\-style evaluation to confirm latency, context handling, tool behavior, and billing before migrating traffic\.

Developers can also access the model directly through the [Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS](https://platform.claude.com/docs/en/models/fable-5-1/overview)\.

## Conclusion

[Claude Fable 5\.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) is best understood as an execution upgrade\. The most convincing evidence is not the unchanged 1M context window or premium $10/$50 base price; it is the large improvement on agentic research, terminal coding, and automation, combined with substantially cheaper cache reads\.

Use it when a task is difficult, long\-running, and valuable enough that fewer failed runs can justify premium pricing\. For routine, high\-volume, or latency\-sensitive work, begin with a lower\-cost tier and escalate only when your own evaluation shows a measurable improvement in completed outcomes\.

## FAQs

### Is Claude Fable 5\.1 available through an API?

Yes\. Anthropic lists Claude Fable 5\.1 as [active since September 1, 2026](https://platform.claude.com/docs/en/models/fable-5-1/overview)\. It is available through the Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS\.

### How much does Claude Fable 5\.1 API cost?

Anthropic's official list price is $10 per MTok of input and $50 per MTok of output\. [CometAPI currently lists $8 input and $40 output per MTok](https://www.cometapi.com/models/anthropic/claude-fable-5-1/)\. Check the live route price before deployment\.

### How large is Claude Fable 5\.1's context window?

The model supports a [1M\-token context window and up to 128K output tokens](https://platform.claude.com/docs/en/models/fable-5-1/overview)\. Large capacity does not remove the need to test retrieval quality, latency, and cost with production documents\.

### What changed from Claude Fable 5 to 5\.1?

The largest practical changes are stronger agentic research and terminal execution, a cache\-read price reduction from $1 to $0\.25 per MTok, per\-message effort controls, progress updates, and content provenance\. Migration also requires testing forced tool choice, thinking blocks across model switches, and edited conversation histories\.

### Is Claude Fable 5\.1 better than Claude Opus 5?

Not for every workload\. Fable 5\.1 is the higher\-capability option for demanding long\-horizon work, but it is slower and more expensive\. Anthropic recommends starting most workloads with [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/) and moving up when higher\-effort evaluations still fall short\.

### Can I use Claude Fable 5\.1 through CometAPI?

Yes\. CometAPI currently lists [Claude Fable 5\.1 as live](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) under model ID `claude-fable-5-1`, with Anthropic\-compatible and OpenAI\-compatible endpoints\.

### Does Claude Fable 5\.1 support forced tool use?

No\. Anthropic documents that [tool\_choice set to any or a named tool returns HTTP 400](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)\. Use `auto` or `none`, then guide tool selection with instructions and strict input schemas when required\.

## SEO Metadata

**Meta title:** What Is Claude Fable 5\.1? Specs, Benchmarks \& Pricing

**Meta description:** Explore Specifications at a glance, official benchmarks, cache pricing, migration changes, safeguards, and comparisons with Opus 5 and Sonnet 5\.

**Keywords:** Claude Fable 5\.1, Fable 5\.1 benchmarks, Claude Fable 5\.1 pricing, Claude Fable 5\.1 API, Fable 5\.1 vs Fable 5, Fable 5\.1 vs Opus 5, Claude Mythos 5\.1

**URL slug:** what\-is\-claude\-fable\-5\-1
