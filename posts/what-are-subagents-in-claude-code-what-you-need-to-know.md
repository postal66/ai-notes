<!-- social-ops-fingerprint:8e7b251a772204d51b06be6d91be767e1768132bb3bc6d04bde7e665840456c4 -->
---
title: What are SubAgents in Claude Code? What You Need to Know
---
# What are SubAgents in Claude Code? What You Need to Know

![What are SubAgents in Claude Code? What You Need to Know](https://resource.cometapi.com/blog/uploads/2025/10/What-are-SubAgents-in-Claude-Code-What-You-Need-to-Know.webp)

Sub-agents (often written *subagents* or *sub-agents*) are one of the clearest practical advances in agentic developer tooling: they let you compose a small team of specialized AI assistants inside **Claude Code**, each with its own role, tools, and context window. The idea is simple but powerful — instead of asking one generalist model to do everything, you define compact, single-purpose agents that the main orchestrator delegates work to (either automatically or when you explicitly request them). This changes how you manage context, tools, and the cost/latency tradeoffs of complex workflows.

## What are subagents?

**Short definition.** A subagent is a pre-configured, task-specialized AI “personality” that Claude Code can delegate a task to. Each subagent has its own system prompt, its own (isolated) context window, explicitly granted tools, and optionally a model selection. Subagents can be created at the project or user level and invoked automatically by Claude or explicitly by the user.

### Key properties of a subagent

- **Specialized purpose and system prompt.** You describe the subagent’s role, constraints, and approach in its system prompt so it behaves predictably for its narrow domain (for example, *code-reviewer*, *debugger*, *data-scientist*).
- **Isolated context window.** Each subagent keeps its own conversation history and context, preventing the main thread’s context from becoming polluted with low-level details. This is central to scaling workflows that otherwise exhaust a single conversation’s context.
- **Tool scoping and permissions.** You can grant or restrict which internal tools or external Model Context Protocol (MCP) tools a subagent may use. This is a crucial safety and governance feature.
- **Config as code.** Subagents are defined as Markdown files with YAML front matter (name, description, tools, model) and stored either at the project level (`.claude/agents/`) or user level (`~/.claude/agents/`). Project definitions take precedence.

## What are Automatic delegation and Explicit invocation

Claude Code can *automatically* delegate tasks to subagents when your prompt or the subagent `description` matches the task — or you can *explicitly* request an agent (e.g., `> Use the code-reviewer subagent to check my recent changes`). Make the `description` action-oriented (`"Use PROACTIVELY"`, `"MUST BE USED"`) to nudge automatic delegation, two complementary ways to use subagents in Claude Code:

1. **Automatic delegation** — Claude inspects the request and delegates matched work to a subagent proactively.
2. **Explicit invocation** — you call out a subagent by name in your prompt/command (for example, `Use the code-reviewer subagent to check my changes`).

Both approaches have different UX and engineering tradeoffs. Below I unpack each.

### Automatic delegation

**How it looks to users.** You issue a high-level command (e.g., “Prepare a security audit for this new library”), and Claude detects that one or more subagents are a good fit based on the `description` field in their configs. If configured for proactive use, the subagent is dispatched automatically and returns results as structured outputs.

**Why teams use it.**

- It lowers cognitive load — you don’t need to remember or type every subagent name.
- It creates smoother onboarding for shared workflows where particular tasks should always be handled by the same specialist.

**Caveats.**

- You must engineer the `description` and system prompt deliberately so Claude reliably selects the correct subagent.
- Over-eager delegation can increase token usage and noise if many subagents activate for similar tasks; design your descriptions conservatively.

### Explicit invocation

**How it looks to users.** You explicitly call a subagent: `> Use the test-runner subagent to run the project tests`. The orchestration is deterministic: Claude invokes that named subagent with its preconfigured permissions and prompt.

**Why teams use it.**

- Full control: you decide exactly which specialist will run, which simplifies debugging and reproducibility.
- Easier to reason about costs and tool access in CI or automated scripts.

**Caveats.**

- More typing and discipline: developers or automation must know the right subagent names.
- Less opportunistic: you lose some convenience where the main agent would have detected a good subagent automatically.

## How subagents work — the technical overview

Below is a practical, implementation-oriented look at what happens when you create and use a subagent.

### Defining a subagent (config as code)

A subagent is a Markdown file with YAML front matter. Important fields include:

- `name` — a unique lowercase id (hyphenated)
- `description` — natural-language description used for automatic delegation matching
- `tools` — optional comma list of allowed tools (or omitted to inherit all tools)
- `model` — optional alias (`sonnet`, `opus`, `haiku`) or `inherit` to use the main conversation’s model

A small example (conceptual, not verbatim from the docs):

```
---
name: code-reviewer
description: Expert code reviewer. Proactively reviews code for quality, security, and maintainability.
tools: Read, Grep, Bash
model: inherit
---
You are a senior code reviewer. Focus on security, correctness, and maintainability.
```

These files live in either `.claude/agents/` (project scope) or `~/.claude/agents/` (user scope). Project files take precedence, which makes sharing and version-controlling subagents straightforward.

### Model selection and tools

- **Model field:** you can pick a specific model alias for the subagent or let it inherit the main conversation’s model. That lets you mix cost/quality tradeoffs (for example, use a cheaper model for large data-scanning subagents and a higher-quality model for final synthesis).
- **Tool scoping:** giving each subagent a minimal set of tools reduces blast radius and simplifies reasoning about safety. Tools include the standard Claude Code primitives (Read, Grep, Bash, Edit, etc.) and MCP-provided integrations.

### Runtime behavior and context handling

When Claude delegates to a subagent, that subagent receives:

1. Its system prompt (the YAML/Markdown contents).
2. Only the context it needs (its own context window).
3. Tool access as allowed in its config.

Because each subagent keeps an isolated context, long investigations or large file analyses can be decomposed into many small contexts instead of forcing one single context to hold everything — a major win for both reliability and interpretability.

## Architectural patterns for subagent

The most common architecture is an *orchestrator* (main agent) that decomposes a high-level task, spins up multiple sub-agents, and then synthesizes or verifies their outputs. Two canonical patterns appear in the wild:

### 1) Orchestrator + Specialists

One agent (the *orchestrator*) coordinates multiple subagents in parallel or serially. The orchestrator decides which specialist to call, aggregates outputs, verifies consistency, and performs final integration. This is the common “manager delegates to team members” approach and matches many examples and recommended designs in Claude Code materials. Benefits include parallelism, clearer separation of concerns, and easier error containment (a buggy subagent affects only its scope).

**When to use it:** complex tasks with independent subproblems (e.g., “generate tests”, “run static analysis”, “rewrite a module”, then “integrate and run end-to-end tests”).

**Trade-offs:** orchestration logic can become complex; extra round-trips may slightly increase latency.

### 2) Pipeline / Chained Specialists

Here subagents are arranged in a sequence where the output of one becomes the input of the next (e.g., spec → scaffold → implement → test → optimize). This is essentially function composition expressed as agents — handy when you need stepwise transformations and strict guarantees about how data flows between stages. It’s conceptually simpler for linear workflows and sometimes easier to debug.

**When to use it:** deterministic multi-step transformations (for example, translating a design doc into scaffolded code, then tests, then optimizations).

**Trade-offs:** less natural for tasks requiring broad exploration (research, brainstorming), and a single broken link can stall the whole pipeline.

## What makes a subagent different from a mere role-based prompt?

### 1) Separate context windows

Each subagent gets its own context buffer that stores exchanges, files, and metadata relevant to its role. That prevents the main session’s context from being polluted by noisy intermediate messages, and it also means you can preserve — or limit — history for each capability. This is how Claude Code lets you keep long-lived, high-signal contexts for specialized tasks without paying the token cost or cognitive overhead of stuffing everything into one prompt.

### 2) System prompts and personas

Subagents are created with system-level instructions that define their role, tone, and constraints (e.g., “Act only as a refactoring specialist; do not execute shell commands” or “Generate unit tests in pytest style; only use public interfaces”). These prompts act like job descriptions for the subagent and are enforced at run-time by Claude Code’s runtime.

### 3) Tool bindings and permission scoping

A critical practical difference: subagents can be granted or denied access to specific tools — filesystem, process execution, external APIs, or privileged datasets. That makes subagents powerful for **least-privilege** designs: a documentation generator can be blocked from running arbitrary commands, while a CI subagent is granted an isolated sandbox. Many community posts advocate pairing subagents with Model Context Protocol (MCP) or a hooks-based MCP server to manage secure access to secrets and I/O.

### 4) Model choice and cost-performance tradeoffs

Because subagents are modular, you can assign different underlying models depending on task complexity. Use a high-capability Sonnet model for deep reasoning or a lightweight Haiku model for fast, repetitive tasks. This heterogeneous deployment helps balance latency, token cost, and capability. Anthropic’s product updates and community articles emphasize parallel deployment of smaller models for cost-effective scaling.

### 5) Communication patterns

Subagents communicate with the orchestrator (or each other) via structured messages or files. Typical patterns include:

- returning a structured JSON payload (preferred for programmatic orchestration),
- writing to a scoped file in a shared workspace,
- or sending a final formatted message back to the orchestrator that includes a confidence score and rationale.
  Community experiments show teams prefer explicit, machine-readable handoffs to avoid ambiguity.

## Performance Benefits

Sub-agents aren’t just a design neatness — they deliver practical performance and quality benefits when used correctly.

### 1) Reduced wall-clock time via parallelism

By dispatching multiple workers concurrently (for example, one worker per repository folder, per microservice, or per data chunk), the orchestrator reduces the elapsed time needed to complete large composite tasks. Use-cases like triaging bug reports, generating documentation for many modules, or auditing multiple services are natural fits. Significant speedups in developer workflows when workloads are truly parallelizable.

By giving each role its own context, you avoid prompt bloat and reduce hallucination risk caused by irrelevant historical noise. That means fewer context-related failures and more consistent outputs for specialized tasks. Community write-ups and Anthropic’s own research show that multi-agent setups often outperform monolithic agents on breadth-first tasks. One Anthropic internal evaluation reported dramatic improvements for research-style tasks using a lead agent + subagents architecture.

> Caveat: parallelism yields the best gains when sub-tasks are independent. If workers must constantly wait on each other or share heavy state, you’ll see diminishing returns.

### 2) Better context utilization and lower token waste

Instead of stuffing every intermediate search result into a single global context, workers keep only what’s relevant inside their own window and return distilled outputs. That reduces token consumption for the orchestrator and reduces the risk of hitting context limits — a practical win when you’re working with large codebases, long logs, or big document repositories. The SDK’s compaction/summarization further extends long-running agents’ effective memory.

### 3) Improved accuracy from specialist prompts

A sub-agent constructed as a narrowly-scoped specialist can be tuned (via its system prompt and toolset) to optimize for precision in its domain: security checks, code style, or compliance extraction. Narrowly scoped prompts tend to reduce hallucination because the agent’s allowable action space and expected outputs are constrained. Organizations report higher-quality outputs for tasks like automated code review when they use domain-specific sub-agents instead of asking a generalist to do everything.

## How teams actually use subagents — example workflows

Below are concrete examples to make this less abstract.

### Example A — Refactor pipeline (Orchestrator + Specialists)

1. Orchestrator receives a “refactor component X” request.
2. Orchestrator calls `analysis-subagent` (no write perms) to identify complexity hotspots and risky dependencies.
3. Orchestrator calls `refactor-subagent` (write perms to a branch-like sandbox) to produce refactored files.
4. Orchestrator calls `test-gen-subagent` (read-only on code) to produce unit tests.
5. Orchestrator runs CI with `ci-runner-subagent` (sandboxed execution) and aggregates results for a human review.
   This pattern isolates each phase, contains risk, and keeps audit trails tidy.

### Example B — Research + prototype (Pipeline)

1. `literature-subagent` scrapes and summarizes references (no file write, regulated web access).
2. `prototype-subagent` scaffolds a minimal PoC from the summary.
3. `benchmark-subagent` runs microbenchmarks in a sandbox and reports results.
   This chain enforces the sequential nature of research tasks while keeping responsibilities clear.

## Best practices and patterns

### Design and configuration

- **Start with small, narrow roles.** Make each subagent responsible for one clear job. Narrow responsibilities make debugging far easier.
- **Version control your `.claude/agents/` folder.** Treat subagent definitions like code — review, test, and pin versions. This reduces drift and eases audits.
- **Pin tools and models purposely.** Use `model: inherit` when you want consistent behavior with the main conversation; specify a lower-cost model alias for background scans. Lock down tools to minimize the attack surface.

### Operational patterns

- **Use explicit invocation for deterministic automation.** If you’re running CI jobs or hooks, call specific subagents to ensure predictable results.
- **Use automatic delegation in interactive sessions.** For exploratory work, let Claude pick subagents to lower friction — but make `description` fields deliberate so automation doesn’t trigger unexpectedly.
- **Design structured outputs for synthesis.** Force subagents to write to files or produce JSON that the orchestrator can read; that simplifies the reduce step and auditing.

### Testing, monitoring, and governance

- **Build representative evals.** Track where subagents fail and build tests that exercise those failure modes. Anthropic recommends representative test sets and iterative improvement.
- **Monitor token and tool usage.** Instrument each subagent’s usage and add alerts to detect runaway cost or rate-limit conditions.

## When NOT to use subagents

Subagents are powerful but not always the right tool.

- **Simple tasks:** For short, one-off prompts or trivial transformations, subagents add unnecessary complexity.
- **Tight latency constraints:** Orchestration round-trips add overhead; if you need single-turn, extremely low-latency responses, a monolithic approach may be simpler.
- **Small teams with little infra:** Without tooling for secrets, observability, and sandboxes, subagents can increase operational risk. Community articles emphasize starting small and adding subagents when you need modularity.

## Where to use Claude code cli is most recommended

***It was excited announce that CometAPI now fully supports the powerful Claude Code cli.*** You only need to install Claude Code and authenticate with the obtained Comet API key and base address to use the Comet API model on Claude Code.

### Why to use claude code through CometAPI?

Top Artificial Intelligence features: Easily generate, debug and optimize code using models built specifically for developers.

- Flexible Model Selection: Our comprehensive range of models allows you to develop more seamlessly.
- Seamless Integration: APIs are always available. Integrate Claude Code directly into your existing workflow in minutes.
- **Using Claude Code via CometAPI will save more costs**. The Claude API provided by CometAPI is 20% off the official price and is updated with the latest model by the official.

Ready to use Claude Code cli? consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions.

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

**See Also [How to Install and Run Claude Code via CometAPI?](https://www.cometapi.com/how-to-install-and-run-claude-code-via-cometapi/)**

## Conclusion — why subagents matter now

Subagents make the promise of agentic workflows practical for teams: they let you reason about roles, permissions, context, cost, and parallelization explicitly and as first-class objects. When used judiciously, subagents unlock higher developer velocity, better quality on multi-step tasks, and more predictable governance. The flipside is that you must design, test, and monitor these subagents just like production software — but that investment turns prompt engineering into reliable engineering practice.

---

*Originally published at [https://www.cometapi.com/what-are-subagents-in-claude-code/](https://www.cometapi.com/what-are-subagents-in-claude-code/).*
