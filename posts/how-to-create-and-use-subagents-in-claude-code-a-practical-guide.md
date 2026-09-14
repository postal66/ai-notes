<!-- social-ops-fingerprint:883e3540a2e818b9c6f3ee281811e13763955e1a474192e9ed2cf9877041a348 -->
---
title: How to create and use Subagents in Claude Code— a practical guide
---
# How to create and use Subagents in Claude Code— a practical guide

![How to create and use Subagents in Claude Code— a practical guide](https://resource.cometapi.com/blog/uploads/2025/10/How-to-create-and-use-Subagents-in-Claude-Code.webp)

Subagents are one of the most useful additions to the Claude Code / Claude Agent ecosystem: they let you break complex workflows into smaller, specialist AI “teammates”, preserve main-thread context, and safely limit tool access. This article explains **what subagents are**, **how to create and invoke them** (CLI, filesystem, and SDK), the **design principles** you should follow when building them, and **concrete sample code** you can copy and adapt.

## What are Subagents?

A **subagent** is a pre-configured, narrowly scoped AI assistant that Claude Code (or the Claude Agent SDK) can delegate work to. Each subagent:

- Has a unique name and a clear description of purpose.
- Runs in its **own context window** separate from the main conversation (so long chains of detail don’t pollute the orchestrator’s context).
- Can be configured with a limited set of **tools** (file read/write, bash, grep, MCP tools, etc.), and with a specific model choice.
- Contains a system prompt (the subagent’s personality and instructions) that guides behavior and constraints.

These properties make subagents ideal for tasks that are token-heavy (research, searching big logs), security-sensitive (scanning or potentially destructive tools), or repetitive and well-specified (style checking, test running).

Anthropic has been iterating quickly: the Claude Code CLI and Agent SDK have been refactored and extended into the **Claude Agent SDK**, plugin support has been introduced for bundling agents and related customizations (slash commands, MCP servers, hooks), and **Skills** provide a way to package domain workflows for reuse across Claude.ai, Claude Code, and the Agent SDK. These updates make it easier to **share, install, and version** subagents across teams and projects. If you plan to build production workflows you should evaluate plugin / skills packaging and the SDK-based deployment patterns.

### Why Subagents matter

Three reasons they’re immediately useful:

1. **Context preservation** — long or noisy searches, test runs, or scans live inside a subagent instead of overwhelming the primary context. That reduces token waste and makes results easier to reason about.
2. **Specialized expertise** — you can encode domain knowledge and behavior in a system prompt tailored to the task (e.g., a `security-auditor` that focuses on secrets, dependency issues, and unsafe shell usage).
3. **Safer permissions** — limiting tools per subagent reduces blast radius (a doc-reviewer might have read-only tools; a test-runner has `Bash` but no `Edit`).
4. **Parallelization:** You can spin up multiple subagents to run concurrently (for instance: `style-checker`, `security-scanner`, `test-runner`) and then collect their brief results — a huge win for expensive, independent checks.

## Prerequisites for using Subagents in Claude Code

Before you start building Subagents, make sure you have the following in place:

### 1) Claude Code installed and authenticated

Install the Claude Code CLI or use the web/IDE integrations. CometAPI‘s Quickstart and setup docs list supported install methods (npm global package or native installers) and show how to verify your install with `claude --version` / `claude doctor`. You’ll also need a [CometAPI](https://www.cometapi.com/) account (Using CometAPI’s key to access Claude code is cheaper and more convenient than the official model.) as noted in the Quickstart.

### 2) Node / environment (for some install paths) and basic shell tooling

If you install via the npm package you should have Node.js (Node 18+ is common in examples). If you intend to use the Agent SDK (JavaScript/TypeScript or Python) you’ll need a project with the SDK dependency installed. Many tutorials assume standard developer tooling (git, bash, optional `gh` CLI for GitHub workflows).

### 3) Project layout & CLAUDE.md

Best practice is to keep repo-level helper docs (`CLAUDE.md`) and to put project-scoped agents in `.claude/agents/` so teammates inherit them. CLAUDE.md files are pulled into Claude’s context automatically and help guide behavior consistently across sessions, each subagent is a Markdown file with YAML frontmatter. Minimal example:

```
---
name: code-reviewer
description: Expert code review specialist. Use PROACTIVELY after code changes to check security, style, and maintainability.
tools: Read, Grep, Glob, Bash
model: inherit
---
You are a senior code reviewer. When invoked:
1. Run `git diff` to identify modified files.
2. Focus review on changed code paths.
3. List security issues, probable false positives, and suggested fixes.
4. Provide a short, prioritized action list.

Return results in JSON with fields: summary, issues.
```

- `name` is a lowercase identifier.
- `description` guides automatic invocation and matching.
- `tools` restricts tool access (omit to inherit everything).
- `model` can be `sonnet`, `opus`, `haiku`, or `inherit`.

### 4) Permissions & MCP servers (optional but common)

If your workflows use Model Context Protocol (MCP) servers or external tools (Puppeteer, Sentry, custom REST tools), ensure your MCP servers are configured and reachable. For sensitive operations (write, bash, git commit) be deliberate about the allowlist and per-agent `tools` scoping.

## How to create Subagents in Claude Code

You can create subagents in three main ways: via the interactive CLI (`/agents`), as filesystem markdown files, or programmatically through the Agent SDK. Below are the step-by-step options：

Claude Code supports three practical ways to create subagents:

1. **Interactive CLI `/agents` UI** — fastest for iterative creation inside a session.
2. **Filesystem-based** — create Markdown files with YAML frontmatter in `.claude/agents/` (project-level) or `~/.claude/agents/` (user-level). Project agents have higher priority.
3. **Programmatic (Agent SDK)** — define subagents in code via the `agents` parameter when you call `query()`; recommended for SDK-driven apps. This approach is ideal when subagents must be created dynamically or embedded in an application.

### Quick interactive flow (recommended first step)

1. Start Claude Code in your terminal or open the command palette in VS Code.
2. Run the subagents interface with the slash command:

```
/agents
```

3. Choose **Create New Agent**, pick project-level or user-level scope, fill in name/description/tools/system prompt, and save. You can generate a draft with Claude and then refine it. Once saved the agent is available in `/agents` and can be invoked explicitly or automatically.

### Filesystem-based subagents (Markdown + YAML frontmatter)

Subagents are stored as Markdown files with YAML frontmatter. Place them in:

- Project scope: `.claude/agents/*.md` (highest priority)
- User scope: `~/.claude/agents/*.md`

Basic file structure:

```
---
name: code-reviewer
description: "Review recent code changes for security and style."
tools: Read, Grep, Glob, Bash  # optional; omit to inherit

model: sonnet  # optional; or 'inherit'

---
You are a senior code reviewer with expertise in security, performance, and best practices.
When reviewing:
- Identify security vulnerabilities
- Prioritize clarity and maintainability
- Always provide concise examples and suggested fixes
- If unsure, ask for the minimal reproducible snippet
```

A few implementation notes:

- `name` must be lowercase with hyphens.
- Omitting `tools` will let the subagent inherit all the main thread’s tools; explicitly listing tools enforces a least-privilege model.
- Use `model: 'inherit'` for consistent behavior with the main thread, or specify a model alias (e.g., `sonnet`, `opus`, `haiku`).

### CLI JSON definition (ad hoc/session usage)

You can define temporary subagents inline when launching a session:

```
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer.",
    "prompt": "You are a senior code reviewer. Focus on security and best practices.",
    "tools": ,
    "model": "sonnet"
  }
}'
```

CLI-defined agents are useful for scripted runs or experiments; they have lower priority than project agents but higher than user agents.

### Programmatic definition (Agent SDK — recommended for apps)

If you’re building an application or automation, define subagents programmatically via the Agent SDK’s `agents` parameter (this is the most integrated option). Example (TypeScript):

```
import { query } from '@anthropic-ai/claude-agent-sdk';

async function runReview() {
  const result = await query({
    prompt: "Assess the authentication module for security issues",
    options: {
      agents: {
        "code-reviewer": {
          description: "Expert code review specialist",
          prompt: `You are a code review specialist...`,
          tools: ,
          model: "sonnet"
        },
        "test-runner": {
          description: "Runs the test suite and analyzes failures",
          prompt: `You run tests and summarize failures...`,
          tools: ,
          model: "sonnet"
        }
      }
    }
  });

  console.log(result);
}
```

The SDK also accepts filesystem-based agents (it will load `.claude/agents/` files) if you prefer that pattern. Programmatic agents are powerful for dynamic workflows and CI integration.

For Python, the `claude-agent-sdk` package supports similar patterns: you can use `query()` or `ClaudeSDKClient` and configure options, tools, and MCP servers programmatically. See the Python SDK repo for quick start samples.

---

## How to invoke subagents

### Automatic delegation

Claude Code can **automatically** choose a subagent when a user prompt matches a subagent’s purpose. This is useful for background orchestration where the main agent routes tasks to the right specialist automatically. Rely on clear subagent descriptions and focused system prompts to improve automatic selection accuracy.

### Explicit invocation (recommended for clarity)

You can explicitly invoke an agent in conversation:

```
> Use the code-reviewer subagent to check my recent changes
```

Explicit invocation is deterministic and recommended for production flows where you want to avoid unexpected delegation.

### SDK orchestrator patterns

Common patterns in SDK apps:

- **Fork + gather**: Launch multiple subagents in parallel, collect each agent’s concise answer, then summarize/merge results in the main agent.
- **Supervisor loop**: The orchestrator assigns tasks to subagents, inspects results, and either accepts them or requests recalculation/clarification.
- **Sandboxed execution**: Give potentially dangerous capabilities (deploy, run scripts) to a tightly constrained agent and require explicit human approval hooks before executing.

These patterns map to practical implementations using the Agent SDK’s session management, hooks, and MCP tools.

---

## How to make subagents that are useful, safe, and composable

### 1) Single responsibility and clear prompts

Each subagent should have one clear purpose and a system prompt that specifies boundaries, success criteria, and output format. If the desired output is structured (JSON, bullet list, code patch), instruct the subagent precisely to reduce parsing errors.

### 2) Least privilege for tools

Grant only the tools a subagent needs. For example, a doc-reviewer does not need `Write` or `Bash`. Default to read-only where possible and escalate tool permissions explicitly when needed. This reduces risk and simplifies auditing.

### 3) Return compact, structured outputs

Subagents should return **concise, final answers** rather than long-running thought traces. A common pattern is: do heavy work within the subagent’s context, then return a short summary with attachments (patches, file references, JSON). This maximizes context efficiency for the orchestrator.

### 4) Testability and versioning

Store subagent files in version control, create CI tests that exercise real runs against small inputs, and pin models/toolsets. If you rely on Skills and plugins, adopt the plugin marketplace/versioning patterns to manage upgrades and rollbacks.

### 5) Audit hooks and human-in-the-loop checkpoints

Use SDK hooks to intercept tool invocations (PreToolUse hooks) and require human approval for destructive actions. Log all tool calls for replayable audits. The SDK provides hook and permission machinery to support this pattern.

## Application sample — a small, production-like pipeline

Below is a compact example that shows the typical pieces: a filesystem agent, an SDK invocation that uses two agents (one for review, one for tests), and a simple orchestration.

### 1) Filesystem agent: `.claude/agents/code-reviewer.md`

```
---
name: code-reviewer
description: Use PROACTIVELY after code changes. Perform security, style, and maintainability review on modified files.
tools: Read, Grep, Glob
model: inherit
---
You are a meticulous senior code reviewer. When invoked:
1. Run `git diff --name-only` to find modified files.
2. For each modified file, read and look for security issues, suspicious patterns, or maintainability problems.
3. Return JSON:
{
  "summary": "one-line summary",
  "issues": ,
  "recommended_changes":
}
```

### 2) Programmatic orchestration (Node.js)

```
import { query } from '@anthropic-ai/claude-agent-sdk';
import fs from 'fs';

async function runPipeline() {
  const result = query({
    prompt: 'Run PR checks: security review then unit tests.',
    options: {
      agents: {
        'code-reviewer': {
          description: 'Use PROACTIVELY after code changes; output JSON with issues.',
          prompt: fs.readFileSync('./.claude/agents/code-reviewer.md', 'utf8'),
          tools: ,
          model: 'sonnet'
        },
        'test-runner': {
          description: 'Run test suite and summarize failing tests.',
          prompt: `You are a test-runner. Execute tests and return JSON { summary, failing_tests[] }`,
          tools:
        }
      }
    }
  });

  for await (const message of result) {
    // Implement streaming logic: messages may include subagent outputs
    console.log(message);
  }
}

runPipeline().catch(console.error);
```

**Notes:** the `code-reviewer` is stored in the repo for team reuse; the SDK call demonstrates programmatic agents taking precedence and the `tools` scoping prevents accidental writes.

---

## Advanced topics & patterns

### Dynamic agent configuration

Create parameterized agent factories that choose model and toolsets depending on environment (dev vs. prod) or severity levels (e.g., `strict` vs `balanced` security modes). The SDK examples show how to generate agent definitions at runtime.

### Parallelization

Spin off multiple read-only analysis agents in parallel (style, security, test coverage) and aggregate their JSON outputs in the main thread. This greatly reduces wall-clock time for large repos.

### Plugin-supplied agents

Plugins can provide subagents packaged with the plugin manifest; they appear in `/agents` alongside custom agents and can be invoked explicitly. Use this to distribute standardized agents across teams.

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

## Final thoughts

Treat Subagents as **reusable, versioned micro-personas**. Start small: make a `doc-reviewer` and a `test-runner` for a repo, check them into `.claude/agents/`, and automate them in CI using headless `claude -p`. Iterate your prompts, add structured outputs, and tighten tool permissions.

The mental model that helps most: imagine Claude as a project manager and subagents as specialists on the team. The manager delegates clearly-worded tasks, aggregates the specialists’ deliverables, and writes the final report. Over time you’ll see improvements in reliability, testability, and the ability to automate large chunks of developer workflows.

---

*Originally published at [https://www.cometapi.com/how-to-create-and-use-subagents-in-claude-code/](https://www.cometapi.com/how-to-create-and-use-subagents-in-claude-code/).*
