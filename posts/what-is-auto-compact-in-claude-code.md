<!-- social-ops-fingerprint:2c6df813e4c9e5ab30bf683bc17e16e584cadb6e8b94a1f67986bd825c78d48b -->
---
title: What Is Auto Compact in Claude Code
---
# What Is Auto Compact in Claude Code

![What Is Auto Compact in Claude Code](https://resource.cometapi.com/auto%20compact%20in%20claude%20code.webp)

Claude Code is Anthropic’s agentic coding assistant that can read a codebase, edit files, run commands, and integrate with tools across terminal, IDE, desktop app, and browser workflows. Because it works inside a shared context window, long sessions eventually fill up with chat history, file output, and tool chatter.Claude Code manages this automatically by compacting conversation history as you approach the limit, and that early instructions can be lost if they are only present in chat history.

That matters even more in 2026 because Anthropic continues to push Claude Code toward longer, more autonomous work. On March 25, 2026, Anthropic published “Claude Code auto mode: a safer way to skip permissions,” saying users approve 93% of permission prompts and describing auto mode as a classifier-based middle ground between manual approval and unsafe permission skipping. On February 5, 2026, Anthropic also launched Claude Opus 4.6, highlighting stronger coding, better debugging, and longer agentic sessions. Those updates are not the same as auto compact, but they show the product direction clearly: fewer interruptions, longer sessions, and more reliable continuity.

CometAPI currently offers access to the Claude API at a lower price than the official API, for example  [Claude Sonnet 4.6](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/),[Claude Opus 4.6](https://www.cometapi.com/models/anthropic/Claude-Opus-4-6/), and the Claude 5.

## What auto-compact actually means in Claude Code

Auto Compact is a built-in context optimization mechanism in Claude Code (the CLI/desktop tool from Anthropic) and the broader Claude API ecosystem. It automatically intervenes when your conversation nears the model’s context window ceiling—typically around 200,000 tokens for flagship models like Claude Opus 4 or Sonnet 4. The hooks documentation is explicit: `PreCompact` fires before a compact operation, and the `auto` matcher means “auto-compact when the context window is full.” The matching `PostCompact` hook fires after compaction completes, and it receives the generated `compact_summary`.

That matters because compaction is not the same thing as “memory.” Auto memory is Claude’s own note-taking system, while compaction is a session-management mechanism that compresses the live conversation state. The memory docs are clear that `CLAUDE.md` is persistent, auto memory is written by Claude, and compaction is the moment when the session’s conversational history gets reduced so the model can keep working.

Instead of forcing a new chat (and losing history) or letting the model “forget” critical details, Auto Compact:

1. **Analyzes the full history** — identifying core elements worth keeping.
2. **Generates a concise summary** — of decisions, code architecture, resolved bugs, file states, and next steps.
3. **Replaces older messages** — with this summary (a “compaction block” in API terms).
4. **Resumes seamlessly** — with the preserved context.

**Key Data Points (2026):**

- **Trigger threshold**: Defaults to ~95% capacity (or ~25% remaining). Some users report an internal buffer reserving 20–45k tokens (~22.5% of context) for the compaction process itself.
- **Performance improvement**: Since Claude Code v2.0.64, compaction is “instant” rather than taking minutes.
- **Token savings example** (from Claude Agent SDK benchmarks): A 5-ticket workflow dropped from 204k to 82k input tokens (58.6% reduction) with two compaction events.

Auto Compact is **not** the same as `/clear` (which wipes everything) or simple truncation. It intelligently preserves what matters—recent code diffs, architectural choices, naming conventions—while condensing resolved debugging loops and exploratory tangents.

## Why Use Auto Compact in Claude Code?

**Long coding sessions are the norm.** A single feature implementation might span 50+ turns: planning, debugging, refactoring, testing. Without compaction, token usage grows linearly, response quality degrades, and costs skyrocket.

For developers, the payoff is less restart fatigue. Instead of manually copying a summary into a new session, you let Claude compact the session and keep moving. That is especially useful in bug-fixing, multi-file refactors, test-driven changes, and review-heavy workflows where the conversation can get very long. Claude Code sessions start with a fresh context window, so compaction is one of the key mechanisms that makes long-running work practical.

### Core Benefits

- **Unlimited session length**: Continue indefinitely without starting over.
- **Cost & performance efficiency**: Reduces input tokens dramatically. Real-world reports show 50–60% savings in multi-phase workflows.
- **Better focus and stability**: Prevents “context overload” where the model hallucinates or forgets earlier constraints.
- **Preserves institutional knowledge**: Key decisions stay in context even after hundreds of messages.
- **Seamless for agentic workflows**: Critical when using tools, MCP servers, or multi-agent setups in Claude Code.

### When should you rely on auto compact?

Use auto compact when the task is naturally long-running: multi-file refactors, debugging sessions that bounce between logs and source files, feature implementation with repeated verification, or research that requires many tool calls. Anthropic’s documentation explicitly points to long sessions where the context window fills with irrelevant conversation, file contents, and commands, and says auto compaction preserves key code and decisions while freeing space.

It is less suitable when the task is short, isolated, or requires precise, permanently retained instructions. That instructions from early in the conversation may get lost after compaction, which is why project rules belong in `CLAUDE.md`, not in a throwaway prompt that might be compressed away later.

### When to use (or enable) it:

- **Always on by default** for most users — ideal for daily coding, large refactors, or exploratory projects.
- **Long-running tasks** — processing queues, data pipelines, or multi-file codebases.
- **Team/enterprise environments** — where context continuity across sessions matters.
- **High-stakes projects** — where losing a single architectural decision could cost hours.

### When to consider disabling (via `/config`):

- You want every single token of context for ultra-precise control.
- You prefer fully manual management (power users who save/restore plans via files).

**Latest news (2025–2026):** In March 2025, Anthropic improved Auto Compact’s preservation logic, making summaries smarter at retaining “important info while reducing token usage.” By late 2025, triggering was refined (sometimes earlier at 64–75% usage to avoid failed compactions). Early 2026 saw temporary bugs in the web/desktop interfaces (marked fixed mid-January but with lingering reports), while the CLI remained stable. Version 2.0.64 (Feb 2026) made compaction instant, a major win for developer experience.

## How to Use Auto Compact in Claude Code: Step-by-Step Guide

Claude Code is designed so that each session begins with a fresh context window. That is useful because every new task starts cleanly, and it also makes it easier to spot when a session is getting noisy. Recommending `/clear` between unrelated tasks so stale context does not keep consuming space.

### Step 1: Check Current Context Status

Use `/context` to visualize the current context load. Claude Code’s built-in command list says `/context` shows a colored grid and highlights memory bloat, optimization suggestions, and capacity warnings. That makes it the quickest way to tell whether you are approaching the point where auto compaction is likely to kick in.

In your Claude Code session, type:

```
/context
```

This shows “Context left until auto-compact: XX%” — your real-time progress bar.

### Step 2: Configure Auto-Compact (Optional)

When the context window gets full, Claude Code automatically compacts the conversation. The hooks reference labels this event as `auto`, and it fires when the context window is full. In practice, you do not “turn on” auto compact so much as let Claude Code do it when needed.

```
/config
```

Navigate to “Auto-compact enabled” and toggle true/false. Default is **enabled**. You can also adjust related settings like MCP server usage to free tokens proactively.

### Step 3: Let Auto-Compact Run Automatically

When you hit ~95%:

- Claude displays “Compacting our conversation so we can keep chatting…” (or similar).
- It runs in the background and resumes.
- You’ll see the new summary at the top of context.

**Pro tip:** Do **not** wait for 0%. Manually compact earlier for better results (see best practices below).

### Step 4: Use hooks if you want to automate what happens around compaction

Claude Code exposes both `PreCompact` and `PostCompact` hooks. The hook reference shows that `PreCompact` can detect whether compaction is manual or automatic, and `PostCompact` receives the generated `compact_summary`. That makes hooks a strong fit for logging, audit trails, post-compaction notes, or external automation.

A simple hook pattern looks like this:

```
{  "hooks": {    "PostCompact": [      {        "matcher": "auto",        "hooks": [          {            "type": "command",            "command": "./scripts/save-compact-summary.sh"          }        ]      }    ]  }}
```

And the matching shell script can read the JSON input from stdin, because Claude Code command hooks receive JSON that way:

```
#!/usr/bin/env bashset -euo pipefailjq -r '.compact_summary // empty' \  | sed 's/^/[compact] /' \  >> .claude/compact-log.txt
```

The docs confirm that command hooks receive JSON via stdin, and that `PostCompact` includes `compact_summary`, so this pattern is aligned with the current hook model.

### Step 5: Manual Compact with Precision (Recommended)

Use `/compact` when you want the assistant to compress the thread right now. You can include instructions that shape the summary you want preserved. Anthropic’s built-in commands page lists `/compact [instructions]` as “Compact conversation with optional focus instructions,”

```
/compact keep the auth flow decisions, the current test plan, and the open TODOs
```

That pattern is useful right before a handoff, before a branch switch, or before you ask Claude to start a new phase of work.

Examples from real usage:

- After debugging: /compact keep the solution we found, remove debugging steps
- Project milestone: /compact focus on the new feature requirements

### API-Level Compaction (Advanced – Python SDK & Messages API)

For custom agents or scripts, use the official compaction tools.

**Claude Agent Python SDK example** (automatic for tool-using workflows):

```
from anthropic import Anthropic

client = Anthropic()

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-6",
    max_tokens=4096,
    tools=your_tools,
    messages=messages,
    compaction_control={
        "enabled": True,
        "context_token_threshold": 100000,  # or lower for aggressive compaction
        "model": "claude-haiku-4-5",        # cheaper summarizer
        "summary_prompt": """Create a focused summary preserving:
1. COMPLETED TASKS and key outcomes
2. CURRENT STATE and open items
3. NEXT STEPS
Wrap in <summary></summary> tags."""
    }
)
```

Detect compaction events:

```
if curr_msg_count < prev_msg_count:
    print(f"Compaction occurred! Messages reduced from {prev_msg_count} to {curr_msg_count}")
```<grok-card data-id="f4afb5" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

**Full Messages API (beta, 2026)** – requires header:
```bash
curl https://api.anthropic.com/v1/messages \
  --header "anthropic-beta: compact-2026-01-12" \
  --data '{
    "model": "claude-opus-4-6",
    "messages": [...],
    "context_management": {
      "edits": [{
        "type": "compact_20260112",
        "trigger": {"type": "input_tokens", "value": 150000},
        "pause_after_compaction": true
      }]
    }
  }'
```

The API returns a compaction block you must pass back in future calls. Custom instructions and pausing give full control over budgeting (e.g., enforce a 3M total token cap across sessions).

> If you are using the Claude API of CometAPI, change the message header to "[https://api.cometapi.com/v1/messages\\](https://api.cometapi.com/v1/messages%5C%5C)".

## Auto-Compact vs Manual Compact vs Clear: Comparison Table

| Feature | Auto-Compact | Manual /compact | /clear |
| --- | --- | --- | --- |
| Trigger | Automatic (~95% context) | User-initiated | User-initiated |
| Control | Low (system decides) | High (custom instructions) | None (full reset) |
| Context Preservation | Good (recent + key items) | Excellent (you guide exactly) | None |
| Token Savings | High (58%+ in benchmarks) | High + predictable | Maximum (but loses history) |
| Workflow Disruption | Minimal if instant; can be jarring | None (you choose timing) | Complete reset |
| Best For | Hands-off long sessions | Strategic milestones & power users | Starting fresh projects |
| Risk | Occasional loss of nuance (early bugs) | None | Total loss of prior work |
| 2026 Maturity | Stable & instant (v2.0.64+) | Highly recommended by community | Always available |

## Best Practices for Claude Code Auto Compact (Pro Tips from Developers)

### Compact proactively

The third rule is to use compaction as a reset, not a crutch. If the thread is full of dead ends, ask Claude to compact with a clear instruction about what matters: current objective, chosen approach, failing tests, and unresolved questions. In practice, that makes the summary far more useful than letting the system compact blindly and hoping for the best.

### Keep your durable instructions short.

Anthropic says files over 200 lines can reduce adherence, so large policy blobs are usually worse than concise, well-scoped rules. Use `.claude/rules/` for file-type or path-specific behavior, and use `@path` imports when you need richer supporting detail without bloating the main instruction file.
**Free tokens first** — Disable unused MCP servers with /mcp or @server-name disable before compacting.

### Combine with CLAUDE.md

Treat `CLAUDE.md` as the source of truth for anything you want to survive a long session`CLAUDE.md` is re-read after `/compact`, which makes it the right place for build commands, coding conventions, and the persistent rules you never want to lose. Auto memory is useful too, but it is a different system with a different purpose.

## Other tips

**Monitor via /context** — Keep usage under 70–80% when possible.

**For API users** — Set lower thresholds (e.g., 50k–100k) and use cheaper summarizer models like Haiku.

**Disable only when needed** — Most developers now recommend keeping Auto-Compact on after 2025 improvements.

**Test compaction** — In non-critical sessions first to see how your specific workflow is summarized.

**Real-world impact**: Developers report 2–3x longer productive sessions and fewer “Claude forgot what we were doing” moments.

## Common Issues & Troubleshooting (2026 Edition)

- **Auto-compact not triggering**: Check web/desktop vs CLI; some Jan 2026 bugs were fixed but verify version.
- **Lost context after compaction**: Use manual /compact with explicit instructions next time.
- **Infinite loops or 102% usage**: Rare; restart session or use /clear as last resort.
- **Slow compaction**: Pre-v2.0.64 issue—update Claude Code.
- **API compaction block errors**: Always append the full compaction content block in follow-up calls.

## Conclusion

Auto compact is one of the most important hidden mechanics in Claude Code because it keeps long coding sessions usable without forcing you to restart every time the context window fills. The practical rule is simple: let auto compact handle overflow, use `/compact` when you want control, store durable guidance in `CLAUDE.md`, and use `/clear` or `/rewind` when the session structure changes. That combination gives you the best balance of continuity, control, and speed in long Claude Code workflows.

Auto Compact in Claude Code represents a leap in practical AI-assisted development. By intelligently managing the 200k-token context window, it eliminates the biggest friction point in long-form coding: running out of memory. With instant performance (2026), rich configuration options, and powerful API extensions, it’s now a mature, battle-tested feature used by thousands of developers daily.

**Action steps today**:

1. Open Claude Code and run `/config` — confirm Auto-Compact is enabled.
2. Try a manual `/compact` with instructions on your current project.
3. Explore the Python SDK or Messages API for automated agents in [CometAPI.](https://www.cometapi.com/)

---

*Originally published at [https://www.cometapi.com/what-is-auto-compact-in-claude-code/](https://www.cometapi.com/what-is-auto-compact-in-claude-code/).*
