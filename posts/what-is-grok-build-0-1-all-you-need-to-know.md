<!-- social-ops-fingerprint:575a8263fcd4618f01c6997447a493830dfa0a2931a3e6dbd78f39974edee279 -->
---
title: What Is Grok Build 0.1? All You Need to Know
---
# What Is Grok Build 0.1? All You Need to Know

![What Is Grok Build 0.1? All You Need to Know](https://resource.cometapi.com/grok-build-0-1-official.webp)

## TL;DR

[Grok Build 0.1](https://x.ai/news/grok-build-0-1) is xAI’s coding-specialized model for agentic software engineering rather than ordinary chatbot conversations. Released to the xAI API in public beta on May 29, 2026, it focuses on web development, debugging, tool calling, MCP workflows, and autonomous coding agents.

The model offers a [256,000-token context window](https://docs.x.ai/developers/models/grok-build-0.1), accepts text and image input, supports reasoning, structured outputs and function calling, and costs $1 per million input tokens and $2 per million output tokens at the standard rate. Its strongest case is not a single code completion, but a multi-step workflow in which an agent inspects a repository, edits files, calls tools, runs tests, and iterates toward a validated result.

The key distinction is simple: Grok Build is the coding-agent product, while `grok-build-0.1` is the API-accessible model that can run inside other agentic coding harnesses. The [Grok Build 0.1 API in CometAPI](https://www.cometapi.com/models/xai/grok-build-0-1/) is also live, providing the same model ID through an OpenAI-compatible gateway.

## Key Takeaways

- Grok Build 0.1 is optimized for agentic coding, repository work, debugging, and tool-driven software engineering.
- Its API model ID is `grok-build-0.1`, with a 256K context window and text-and-image input.
- Short-context xAI pricing is $1/M input, $0.20/M cached input, and $2/M output. The [Grok Build 0.1 API in CometAPI](https://www.cometapi.com/models/xai/grok-build-0-1/) is priced 20% lower at $0.80/M input, $0.16/M cached input, and $1.60/M output; requests at or above the 200K threshold use higher long-context rates.
- It supports reasoning, function calling, and structured outputs, but does not support the Batch API.
- Evaluate it by cost and time per successfully completed engineering task, not by raw token price or one benchmark alone.

## What Is Grok Build 0.1?

Grok Build 0.1 is a specialized xAI language model designed around [agentic software-engineering workflows](https://x.ai/news/grok-build-0-1). According to xAI, it was trained for tasks such as web development, debugging, and MCP-enabled coding agents, and it powered the original Grok Build coding environment.

That positioning separates it from a conventional general-purpose assistant. A coding agent must repeatedly inspect a repository, identify relevant files, call tools, edit code, run tests, read failures, and revise the implementation without losing task state.

For that reason, the meaningful unit of evaluation is an end-to-end engineering task: repository navigation → plan → edit → tool execution → failure recovery → validation.

## Is Grok Build 0.1 the Same as Grok Build?

No. [Grok Build](https://x.ai/news/grok-build-cli) is xAI’s terminal-based coding agent, while Grok Build 0.1 is an underlying model that developers can invoke through the API.

Grok Build includes plan review, code diffs, AGENTS.md support, plugins, hooks, skills, MCP servers, parallel subagents, worktree integration, and a headless mode for automation. The model can also be used outside that terminal product in compatible agent frameworks and gateways.

## What Are the Grok Build 0.1 Specifications?

| Specification | Grok Build 0.1 |
| --- | --- |
| Developer | xAI / SpaceXAI |
| Model ID | grok-build-0.1 |
| Primary focus | Agentic coding and software engineering |
| Input / output | Text and image input; text output |
| Context window | 256,000 tokens |
| Capabilities | Reasoning, function calling, structured outputs |
| Standard token pricing | $1.00/M input; $0.20/M cached input; $2.00/M output |
| Long-context threshold | 200K prompt tokens |
| Long-context pricing | $2.00/M input; $0.40/M cached input; $4.00/M output |
| Batch API | Not supported |
| Documented limits | 37 requests/s; 10,000,000 tokens/min |
| Regions | us-east-1, us-west-2 |

These specifications are documented on the [official xAI model page](https://docs.x.ai/developers/models/grok-build-0.1). The 256K context window can hold substantial repository context, while image input lets an agent interpret screenshots, mockups, architecture diagrams, and visual bug reports alongside source code.

Once a prompt reaches the long-context threshold, higher rates apply to all tokens in that request. Repository-heavy agents should therefore compact or retrieve context selectively instead of continually appending files and tool output.

## What Makes Grok Build 0.1 Different?

### Agentic coding as the primary optimization target

Grok Build 0.1 is not merely a model that can write Python or JavaScript. Its specialization is the interaction between reasoning, code generation, and tools. A useful coding agent must plan, inspect, edit, execute, recover from failures, and continue without losing task state.

### MCP-oriented tool workflows

MCP-oriented workflows can connect a coding agent to databases, deployment systems, documentation stores, issue trackers, observability systems, and internal developer tooling through standardized interfaces.

### Structured automation

Structured outputs are useful when an agent must return predictable objects rather than prose—for example, file-change plans, tool parameters, test results, review findings, or deployment decisions. This reduces brittle parsing between the model and the orchestration layer.

### Visual context for web and UI work

Because the model accepts image input, an agent can work with screenshots, rendered pages, interface references, error dialogs, and architecture diagrams in addition to source code.

### How Fast Is Grok Build 0.1?

xAI described Grok Build 0.1 as its fastest coding model at launch and advertised [more than 100 output tokens per second](https://x.ai/news/grok-build-0-1). That is an official service claim, not a guarantee for every prompt or endpoint.

Independent measurements should be treated as time-stamped observations. Artificial Analysis currently reports approximately 69.6 output tokens/s and 0.54 seconds time to first token for the SpaceXAI API. Provider infrastructure, prompt length, reasoning behavior, tool use, and server load can all change the result.

## How Should You Interpret the Benchmarks?

| Independent indicator | Current reported value | Interpretation |
| --- | --- | --- |
| Artificial Analysis Intelligence Index | 27, estimated | Composite estimate; independent evaluation is still indicated as forthcoming |
| Output speed | 69.6 tokens/s | Measured on the first-party SpaceXAI API after the first response chunk |
| Time to first token | 0.54 s | Endpoint latency measurement; not total task completion time |

These figures were checked against [Artificial Analysis on September 22, 2026](https://artificialanalysis.ai/models/grok-build-0-1-06-16/). Because the page is updated dynamically, future revisions should recheck the values and retain the verification date.

For autonomous coding systems, benchmark scores are only one part of the evaluation. Repository navigation, edit precision, tool selection, recovery behavior, test discipline, latency, and total token use can matter more to developer productivity.

## How Much Does Grok Build 0.1 Cost?

Grok Build 0.1 uses separate short- and long-context rates. The short-context tier applies when the prompt length is below 200,000 tokens; once the request reaches the threshold, the higher long-context rate applies to the request.

| Pricing tier | CometAPI | Official xAI |
| --- | --- | --- |
| Short-context input | $0.80/M | $1.00/M |
| Short-context cached input | $0.16/M | $0.20/M |
| Short-context output | $1.60/M | $2.00/M |
| Long-context input | $1.60/M | $2.00/M |
| Long-context cached input | $0.32/M | $0.40/M |
| Long-context output | $3.20/M | $4.00/M |

At short-context rates, one million input tokens plus one million output tokens costs $2.40 through CometAPI, compared with $3.00 through the official xAI API. At long-context rates, the same token mix costs $4.80 through CometAPI versus $6.00 through xAI. These figures cover model tokens only; production budgets should also include tool calls, retries, test execution, and orchestration overhead.

## Grok Build 0.1 vs Grok 4.7 vs Grok Code Fast 1

| Dimension | Grok Build 0.1 | Grok 4.7 | Grok Code Fast 1 |
| --- | --- | --- | --- |
| Lifecycle | Current coding-specialized model | Current frontier model | Previous-generation coding model; retired May 15, 2026 |
| Primary positioning | Specialized agentic coding model | Frontier coding, agentic tasks, and knowledge work | Fast coding model and predecessor in xAI's coding-model line |
| Context window | 256K | 500K | Legacy specification; do not use it as the basis for a new deployment |
| Reasoning and tools | Reasoning, function calling, structured outputs | Configurable reasoning; function calling, web search, X search, and code execution | Legacy coding workflows; migrate rather than expand new production use |
| Official short-context input / output | $1.00 / $2.00 per M tokens | $2.00 / $6.00 per M tokens | Retired; no current production rate should be assumed |
| CometAPI short-context input / output | $0.80 / $1.60 per M tokens | $1.60 / $4.80 per M tokens | Use the current catalog and replacement model rather than the retired slug |
| Official long-context input / output | $2.00 / $4.00 per M tokens | $4.00 / $12.00 per M tokens | Not applicable as a current model-selection rate |
| Typical fit | High-volume repository loops, debugging, and cost-sensitive coding agents | Harder, longer-running coding and professional workflows that need stronger frontier reasoning and more context | Migration reference only; pin grok-build-0.1 for current coding workloads |

Grok Build 0.1 is the more economical specialist when repeated repository inspection, editing, and testing dominate the workload. Grok 4.7 offers nearly twice the context and a broader frontier capability profile, but its output-token price is materially higher. The practical decision should be based on cost per successfully completed task, including retries, tool calls, and human correction time.

Both models are available in CometAPI, allowing teams to run the same coding tasks through one gateway and compare completion rate, latency, context use, and total cost under a consistent harness.

### How Is Grok Build 0.1 Related to Grok Code Fast 1?

The identifier `grok-code-fast-1` was included in xAI’s May 15, 2026 model retirement. The migration guide contains a broad statement that retired slugs redirect to `grok-4.3`, while its model-specific replacement table and “Code workloads” section recommend `grok-build-0.1` and state that the coding slug is routed to that model.

Because the same official guide describes the redirect at two levels, production users should not treat the retired slug as a stable model identifier. Pin `grok-build-0.1` explicitly for coding workloads and verify current routing before deployment.

The [Grok Build 0.1 API in CometAPI](https://www.cometapi.com/models/xai/grok-build-0-1/) provides direct access under the current model ID, avoiding dependence on the retired alias.

## Where Can You Use Grok Build 0.1?

This means the model is not tied to one IDE or provider endpoint. Through CometAPI, teams can use the same `grok-build-0.1` identifier in an OpenAI-compatible workflow and compare it with other coding models without rebuilding the surrounding agent controller.

Grok Build 0.1 can be called through xAI or through CometAPI. For CometAPI, send an authenticated `POST` request to `api.cometapi.com/v1/chat/completions` with `model: "grok-build-0.1"` and a standard `messages` array.

```
curl "https://api.cometapi.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $COMETAPI_KEY" \
  -d '{
    "model": "grok-build-0.1",
    "messages": [
      {
        "role": "user",
        "content": "Find the bug in this repository and propose a minimal fix."
      }
    ]
  }'
```

## When Should You Use Grok Build 0.1?

### IDE coding agents

The combination of coding specialization and low token pricing fits interactive workflows where an agent repeatedly reads, edits, and validates code.

### Automated debugging

Agents can inspect an error, search relevant files, generate a patch, execute tests, and refine the fix.

### Web and UI development

Image input creates a path for screenshot- and design-reference-driven workflows alongside source code.

### MCP-based software agents

Function calling and MCP-oriented workflows suit assistants that need controlled access to external development systems.

### CI and engineering automation

Headless workflows can support bug triage, automated repairs, test generation, refactoring, migrations, and pull-request preparation.

## Is Grok Build 0.1 Still Relevant in 2026?

Yes, but its role is specialized rather than “xAI’s newest model.” Its value lies in the combination of coding specialization, a 256K context window, reasoning, tool calling, structured outputs, image input, and relatively low standard token prices.

It is most compelling when teams need a responsive model for repeated software-agent loops and can evaluate it against their own repositories, tests, latency targets, and failure costs.

## Conclusion

Grok Build 0.1 is a focused coding-agent model rather than a universal frontier model. Its official specifications and pricing make it attractive for high-volume repository work, but the surrounding agent design determines whether that advantage survives in production.

Before adopting it, run a representative evaluation that measures successful task completion, human correction time, tool-call count, token use, test pass rate, and long-context exposure. Choose it when the complete workflow—not only the benchmark or token price—beats the alternatives.

---

*Originally published at [https://www.cometapi.com/what-is-grok-build-0-1/](https://www.cometapi.com/what-is-grok-build-0-1/).*
