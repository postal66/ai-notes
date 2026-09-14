<!-- social-ops-fingerprint:49f95562883df83b75621008bfa8f402de0a50a189798e1f216b67a71f4911ca -->
---
title: Managing Claude Code’s Context: a practical handbook
---
# Managing Claude Code’s Context: a practical handbook

![Managing Claude Code’s Context: a practical handbook](https://resource.cometapi.com/blog/uploads/2025/06/claude-code-1024x576.webp)

Anthropic’s Claude Code and the broader Claude family now give developers unprecedented control over *how much* the model sees and *how deeply* it reasons. Recent product updates (notably the Sonnet 4 1-million-token context window and Claude’s extended “thinking” controls) make context management both more powerful and more important: you can process whole repositories in a single session — but only if you structure prompts, files, and session state deliberately. This article explains how to reliably manage Claude Code’s context: commands & usage, thinking-budget control, CLAUDE.md patterns, subagent workflows, power-user tips, troubleshooting, and concrete code examples you can copy-paste.

## What is **Claude Code**?

Claude Code is Anthropic’s **agentic coding CLI** — a terminal-first tool that connects your development environment to Claude models so the assistant can read your repo, run commands, edit files, run tests, create commits, and execute multi-step workflows from the terminal. It’s built so the AI can “live” in your shell and act on your codebase, with features like repo scanning, slash-commands, subagents (specialized assistants with isolated context), and Model Context Protocol (MCP) integrations for external tools.

---

### Why should I manage the *context* of Claude Code?

Because context = relevance + cost + safety. Left unchecked, long histories cause:

- Higher token usage (more cost, slower responses).
- Context drift (old/irrelevant info confuses outputs).
- Information leakage (secrets or sensitive logs stuck in session).
  Managing context keeps outputs accurate, predictable, and cheaper.

## How does Claude Code organize and preserve project context?

Claude Code is an agentic CLI that treats your repo, tools and configuration as first-class context sources. It reads project files, `CLAUDE.md`, local tools and configured MCP servers; it also supports subagents that each get their own context window (helpful to avoid polluting the main conversation). Use this to keep main-level strategy separate from specialized agent memory (e.g., test runner, code reviewer).

### How does Claude Code ingest repo context and helper files?

- It scans the working directory and any extra directories you add (`--add-dir`).
- It looks for `.claude/` subfolders (commands, agents) and `CLAUDE.md`.
- You can wire Model Context Protocol (MCP) servers for external tool access; Claude Code can inherit those tools into its toolset.

### What methods can I take to manage context in Claude code?

1. Master the basic CLI commands for context. Store reusable prompts as slash commands in .claude/commands/ to avoid repeatedly pasting long prompts.
2. Design a CLAUDE.md file appropriately. Add CLAUDE.md to the repository root to define goals, allowed tools, style, escalation rules, and useful slash commands. (Claude Code reads this automatically and uses it as authoritative guidance.)
3. Use subagents for task isolation—each subagent gets its own context window and tool permissions, which keeps the main session from being polled. Store subagents in .claude/agents/ and version-control them.

## What are the basic context-management commands

Below are the commands you’ll use most often to manage conversational state in Claude Code. I list the behavior, example usage, recommended scenarios, and pointers to related CLI flags.

---

### `/clear` — “start fresh”

**What it does:** wipes the current conversation history from the session so subsequent prompts start from a clean slate. The REPL session continues, but the back-and-forth messages are removed from the model’s context. (Project files and `CLAUDE.md` remain accessible to Claude Code.)

**When to use**

- After finishing a feature or ticket and you want a clean session for an unrelated task.
- If the session has accumulated many exploratory turns and answers are degrading.
- Before handing the session to another user/agent to avoid leaking the prior conversational state.

**Usage**

```
# in the interactive REPL

/clear
```

**Notes & tips**

- `/clear` is destructive for that session’s conversation history; use `/resume`/`--continue` if you want to come back to old sessions saved on disk.

---

### `/compact` — “summarize & condense”

**What it does:** compresses the current conversation into a shorter summary that preserves salient facts and decisions, then replaces the verbose history with that summary so the session can continue without losing the important context. This reduces token usage while keeping continuity.

**When to use**

- When you want to keep the thread’s important state but reduce token footprint.
- Before a long new task that would otherwise push the context window toward limits.
- When you want a succinct session “memory” while retaining key decisions.

**Usage**

```
# in the interactive REPL

/compact
# or with an instruction to guide the summary

/compact Summarize decisions, open TODOs, and config changes only
```

**Notes & tips**

- `auto-compact`, `microcompact`, and other intelligent compaction behaviors may run automatically when conversation length approaches limits in some builds or setups; those features are rolling out and may appear in your installation or hosted environment. (Community and changelogs discuss microcompact and auto-compact behaviors.)

---

### `--continue`, `--resume`, and session controls (CLI level)

**What they do:** control session persistence and selection from the CLI.

- `claude --continue` (or `claude -c`) — re-open and continue the most recent conversation in the current project directory.
- `claude --resume` (or `claude -r <session-id>`) — show an interactive picker (or resume a specific session by ID). Useful when you’ve saved many sessions and want to pick one to continue.

**Usage examples**

```
# continue the most recent session

claude --continue

# open an interactive session picker

claude --resume

# resume by id (non-interactive)

claude --resume 550e8400-e29b-41d4-a716-446655440000
```

---

### Interactive-mode shortcuts that matter for context (terminal UX)

- `Ctrl+L` — clears the terminal screen (visual), but **keeps** conversation history. Use `/clear` to actually reset history.
- `Ctrl+D` — exit the session (EOF).
- `Ctrl+C` — cancel current generation.
  These are convenience controls; they affect only terminal behavior unless you explicitly run `/clear` or `--continue`/`--resume`.

---

### Other context-related controls & flags

- `--add-dir <path>` — include additional directories for Claude to read (good for scoping what Claude can access and reducing needless file reads).
- `--allowedTools` — pre-allow tools so Claude can run them without repeated permission prompts (reduces back-and-forth and noisy tool-permission dialogs).
- Slash-commands (`/.claude/commands/` or MCP-provided) — store frequently used, token-efficient prompts; invoking a slash-command is cheaper than pasting long prompts repeatedly.

## How should I design a CLAUDE.md file to control project context?

### What is CLAUDE.md and why it matters

`CLAUDE.md` is a preflight, project-level prompt that Claude Code reads automatically when starting in a repo. Use it to put short, actionable, stable facts about the project (nouns, architecture, standards). Because the model ingests CLAUDE.md into the prompt, a well-crafted file reduces the need to repeatedly paste the same information and preserves precious token budget.

### CLAUDE.md: practical template (recommended)

Keep these rules: short (100–200 lines where possible), hierarchical (global → project → subdir overrides), and machine-readable sections.

```
# CLAUDE.md — top of repository

Project: Acme Payment Gateway
Primary language: typescript
Build: pnpm build
Run tests: pnpm test
API routing: src/api/*
Database: Postgres via prisma (schema at prisma/schema.prisma)

# Conventions

- commit format: Conventional Commits
- test coverage threshold: 80%
- style: eslint + prettier (configs in .eslintrc, .prettierrc)

# What I'm asking Claude to do

- When asked to create a feature, always include tests and update the CHANGELOG.
- When modifying DB schema, present migration plan and migration files.
```

#### Notes:

- Put high-value items (APIs, important files, infra commands, test command) first.
- Use separate `CLAUDE.md` files in subdirs when different modules have different conventions; Claude will combine and prioritize more specific files.

## How do I assemble workflows and subagents to manage context and parallelize work?

### What are subagents?

Subagents are Claude Code patterns where the main agent delegates discrete tasks to subordinate agents (for example: `frontend-agent`, `backend-agent`, `qa-agent`) and then the main agent reconciles their outputs. Subagents let you work on different parts of the system in parallel without stuffing everything into a single chat.

### Sample workflow: feature implementation (parallel agents)

1. `main-agent` reads CLAUDE.md, creates plan.
2. `frontend-agent` (subagent) gets focused context: UI contracts, storybook, specific files.
3. `backend-agent` (subagent) gets DB schema, API contracts, and implements endpoints.
4. `qa-agent` runs tests, writes failing tests back to `main-agent`.
5. `main-agent` orchestrates commits, merge-requests, and updates CLAUDE.md.

CLI pattern:

```
# start main session

claude --session main

# spawn frontend subagent (conceptually: new session with scoped CLAUDE.md)

claude --session frontend --cwd frontend/
```

Tip: Create scoped `CLAUDE.md` files under subdirectories (`frontend/CLAUDE.md`, `backend/CLAUDE.md`) so each subagent starts with the minimal context it needs.

### Example subagent: `.claude/agents/code-reviewer.md`

```
---
name: code-reviewer
description: Focused code reviewer. Limited tools: Read, Grep, Bash
---

You are a code reviewer. When invoked:
1. Run `git diff --name-only` to see changed files.
2. Prioritize security, correctness, tests.
3. Return a patch (diff) and a 3-item actionable checklist.
```

---

## What are power user tips for keeping context healthy and costs down?

### 1) Keep CLAUDE.md lean and hierarchical

Avoid giant monolithic CLAUDE.md files. Use one global for a developer’s preferences and small module files for area specifics. See earlier template.

### 2) Use slash commands for verbs, CLAUDE.md for nouns

Make CLAUDE.md the place for *facts* (what files exist, architecture), and slash commands the place for *procedures* (create tests, run refactor). This prevents re-sending procedural logic every session. Community wisdom emphasizes this separation.

### 3) Verbose mode + plan mode as debugging tools

When Claude behaves unexpectedly, run verbose to see the exact context, and use plan mode to force an explicit plan you can approve before edits.

### 4) Budget thinking carefully

Start with default/minimum thinking tokens and only increase when tasks require multistep reasoning (complex refactors, formal verification). Use lower budgets for routine edits.

### 5) Instrument outputs & commits

Have hooks that automatically run tests and attach their output to the session (bash mode `!` to run a shell command and include output as context). Use commit hooks to create clear atomic commits with messages.

## How should I troubleshoot when context “drops” or Claude forgets instructions?

### Common symptoms and fixes

- **Symptom:** Claude ignores CLAUDE.md or previous instructions.
- **Fixes:** Confirm the file is in the session’s current working directory; check for more specific subdir CLAUDE.md overriding it; use verbose mode to see current prompt.
- **Symptom:** Performance degrades over long sessions (model “forgets” early parts).
- **Fixes:** Compact the session: extract stable facts into CLAUDE.md, or snapshot parts of the conversation into files and reference them instead of repeating. Also consider restarting short sessions and passing only concise context.
- **Symptom:** Extended thinking takes too long or times out.
- **Fixes:** Lower thinking\_budget, break the task into smaller subproblems, or run batch offline analysis if you need extremely large budgets. Anthropic recommends batching when optimal thinking budgets exceed ~32K tokens to avoid timeouts.

## Conclusion

Managing context in Claude Code is now a multi-dimensional problem: model choice, subagent design, `CLAUDE.md` discipline, thinking budgets, and tooling architecture all interact. Start by investing 1–2 hours to author a clear `CLAUDE.md`, scaffold 2–3 focused subagents, and add usage instrumentation for tokens and thinking budgets — you’ll see immediate gains in reliability, cost predictability, and team productivity.

## Use Claude Code via CometAPI

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

***We’re excited to announce that CometAPI now fully supports the powerful Claude Code.*** You only need to install Claude Code and authenticate with the obtained Comet API key and base address to use the Comet API model on Claude Code.

### Why to use claude code through CometAPI?

Top Artificial Intelligence features: Easily generate, debug and optimize code using models built specifically for developers.

- Flexible Model Selection: Our comprehensive range of models allows you to develop more seamlessly.
- Seamless Integration: APIs are always available. Integrate Claude Code directly into your existing workflow in minutes.
- **Using Claude Code via CometAPI will save more costs**. The API provided by CometAPI is 20% off the official price and is updated with the latest model by the official. The latest model is [Claude Opus 4.1](https://www.cometapi.com/claude-opus-4-1-api/).

Ready to use Claude Code? consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions.

**See Also [How to Install and Run Claude Code via CometAPI?](https://www.cometapi.com/how-to-install-and-run-claude-code-via-cometapi/)**

---

*Originally published at [https://www.cometapi.com/managing-claude-codes-context/](https://www.cometapi.com/managing-claude-codes-context/).*
