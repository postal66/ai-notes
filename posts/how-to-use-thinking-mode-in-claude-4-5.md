<!-- social-ops-fingerprint:7d787a49ce568099cb9dd6ee1c741ef0367fdc3399e3330914efe8099300f8ed -->
---
title: How to use thinking mode in claude 4.5
---
# How to use thinking mode in claude 4.5

![How to use thinking mode in claude 4.5](https://resource.cometapi.com/blog/uploads/2026/01/How%2520to%2520use%2520thinking%2520mode%2520in%2520claude%25204.5.webp)

“Thinking mode” (also called *extended thinking*, *thinking*, or *thinking blocks*) in Claude 4.5 is an explicit, configurable operating mode that instructs the model to spend a separately budgeted number of tokens generating internal, step-by-step reasoning (a “chain-of-thought”) before emitting the final answer. It is designed to improve performance on multi-step reasoning, complex coding and agentic workflows, and research tasks by trading latency and token cost for deeper internal deliberation. Claude 4.5 exposes this capability at the Messages API level with explicit parameters (e.g., `thinking` / `budget_tokens` or an effort/“interleaved-thinking” header), preserves and optionally encrypts thinking blocks for later verification or tool use, and introduces cache and token-accounting behaviors you must manage when building production workloads.

## What is Claude 4.5? (And which models should I care about?)

Claude 4.5 is Anthropic’s latest set of Claude models released as incremental “4.5” updates (for example, *Sonnet 4.5* and *Opus 4.5*). Sonnet 4.5 is positioned as the best balance of intelligence, coding and agentic performance for most developers; Opus 4.5 focuses on very high-effort reasoning and preserves thinking blocks to improve multi-turn continuity. Both models support Claude’s extended thinking capabilities, though some behavior (e.g., summarized vs full thinking) differs by model.

The performance gains in Claude 4.5, particularly in Sonnet 4.5, are most visible in the **SWE-bench Verified** benchmark, which measures an AI's ability to solve real-world GitHub issues.

| Model | SWE-bench Verified Score | OSWorld (Computer Use) |
| --- | --- | --- |
| Claude 3.5 Sonnet | 49.0% | 42.2% |
| Claude 4.1 Opus | 67.6% | 55.0% |
| Claude 4.5 Sonnet (Thinking On) | 77.2% | 61.4% |
| GPT-5 (Medium Reasoning) | 65.0% | 52.0% |

These numbers indicate that Claude 4.5 is not just better at writing snippets; it is significantly more capable of navigating entire file systems and executing autonomous tasks without human intervention.

### Why this matters

- **Coding & agents:** Sonnet 4.5 shows strong gains on real-world software tasks and long-horizon coding work—making it a natural pick for code generation, code editing, and autonomous agent flows.
- **Extended thinking & context:** Claude 4.5 family models are built to reason with very large internal scratchpads (tens of thousands of tokens or more), enabling deeper multi-step reasoning. That changes how you design prompts, token budgets, and tool interactions.

## What is Thinking Mode in Claude 4.5?

Thinking Mode (officially termed "Extended Thinking") is a capability that allows the model to "show its work" to itself before delivering a final output. Unlike standard models that commit to an answer immediately, Claude 4.5 uses a dedicated reasoning space to explore multiple hypotheses, identify potential errors in its logic, and refine its strategy.

### The Anatomy of a Response

In a standard interaction, the model receives a prompt and begins generating the answer. In Thinking Mode, the response is split into two distinct blocks:

| Block Type | Visibility | Purpose |
| --- | --- | --- |
| Thinking Block | Hidden (via API) or Collapsed (UI) | The model’s internal monologue, planning, and self-critique. |
| Text Block | Visible | The final, refined answer provided to the user. |

### Key properties of thinking mode

- **Enable by request**: You pass a `thinking` object in the API call such as `{"type":"enabled","budget_tokens":10000}` to turn it on and give the model an internal token budget for reasoning.
- **Budgeting**: `budget_tokens` caps the model’s internal reasoning tokens. More budget => deeper reasoning potential but higher cost and latency. In Claude 4 models, thinking tokens are billed even if you receive only a summarized view.
- **Summarization & redaction**: For many Claude 4 models the user sees a summarized version of the thinking content; some internal reasoning may be redacted (encrypted) by safety systems and returned as `redacted_thinking`.
- **Signatures & verification**: Thinking blocks include an opaque `signature` used for verification when returning thinking blocks to the API (especially needed when using tools). You should treat the signature as opaque — don’t attempt to parse it.
- **Interleaved thinking with tools**: Claude 4 supports interleaving thinking blocks with tool executions (beta and flag-based in some cases). This is powerful for agentic work (run tool, think, run another tool, etc.).

For hands-on examples and the most up-to-date parameters, Anthropic’s Messages/Extended Thinking docs are the canonical reference.

## How does the Messages API return thinking content

### Summarized vs full thinking; encryption & signatures

Different Claude model versions handle thinking differently: more recent Claude 4 models (like Sonnet/Opus 4.5) often return a *summarized* public view of the internal reasoning while the full scratchpad may be encrypted and made available only via a `signature` field (or redacted blocks). When tools are used (or you need to preserve the internal state across tool calls), you must pass thinking blocks back to the API or use the signature mechanism the docs describe. This mechanism helps protect sensitive internal reasoning while allowing safe continuation of a thought process when needed.

### Practical handling pattern

**Tool use / continuation**: if your next request must continue the same internal state (e.g., tools ran based on the thinking), include the returned thinking block or signature when you call the API again so the model can decrypt and continue from where it left off.

**Request**: send `thinking: {type: "enabled", budget_tokens: N}`.

**Response**: you may receive (a) a summarized public output, (b) an encrypted `signature` or `redacted_thinking` block, or (c) both.

CometAPI offers the Claude 4.5 API at 20% of the official API price, and it can also be called using the [Anthropic Messages](https://apidoc.cometapi.com/anthropic-messages), You will need to obtain an API key before you begin.

### Example 1 — simple curl (non-streaming) enabling thinking

```
curl https://api.cometapi.com/v1/messages \
  -H "x-api-key: $CometAPI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 16000,
    "thinking": {
      "type": "enabled",
      "budget_tokens": 10000
    },
    "messages": [
      {"role": "user", "content": "Design a robust data validation strategy for CSV imports, show tests + code."}
    ]
  }'
```

The response will contain `content` blocks. Inspect each block and prefer the `text` blocks for final output; `thinking` blocks contain the model’s internal analysis summary.

### Example 2 — Python: request, parse thinking and text blocks

```
import os, requests

API_KEY = os.environ["CometAPI_API_KEY"]
URL = "https://api.cometapi.com/v1/messages"
HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

payload = {
    "model": "claude-sonnet-4-5",
    "max_tokens": 16000,
    "thinking": {"type": "enabled", "budget_tokens": 8000},
    "messages": [{"role": "user", "content": "Explain how to do property-based testing in Python; include example code."}]
}

r = requests.post(URL, headers=HEADERS, json=payload)
r.raise_for_status()
resp = r.json()

# Parse blocks
for block in resp.get("content", []):
    if block.get("type") == "thinking":
        thinking_summary = block.get("thinking")
        print("=== THINKING (summary) ===")
        print(thinking_summary[:1000])  # truncate for logs
        print("signature:", block.get("signature")[:64], "...")
    elif block.get("type") == "text":
        print("=== FINAL TEXT ===")
        print(block.get("text"))
```

This code extracts and prints the summarized thinking and final answer. If you need to preserve continuity in multi-turn agent flows, include the unmodified thinking blocks in the next request’s `messages` array (see next example).

### Example 3 — reusing thinking blocks in a multi-turn flow (Python pseudo)

```
# After initial response (resp above):
# Add the assistant message including the thinking block back into the conversation
assistant_message = {
  "role": "assistant",
  "content": resp["content"]  # include raw content array (contains thinking + text blocks)
}

# Next user turn: ask follow-up and include previous assistant message
payload2 = {
  "model": "claude-opus-4-5",  # Opus preserves thinking blocks better across turns
  "max_tokens": 20000,
  "thinking": {"type": "enabled", "budget_tokens": 12000},
  "messages": [
    {"role": "user", "content": "Now adapt the validation logic for an avro pipeline."},
    assistant_message
  ]
}
r2 = requests.post(URL, headers=HEADERS, json=payload2)
```

> Preserving exact unmodified thinking blocks is critical when doing tool-integrated or long agent workflows. Opus 4.5 has improved defaults for thinking block preservation and caching.

## How do I stream thinking outputs and show progress in a UI?

### Streaming best practices

- Use the SDK streaming endpoints (the Python/TypeScript SDKs have stream helpers). For long running or high budget reasoning jobs, streaming prevents HTTP timeouts and gives you partial text as the model computes. Typical code uses an iterator over `text_stream` (Python) or event parsing (JS).
- Expect two-phase streams sometimes: the model may first produce visible reasoning chunks, then finalize with the answer. Build your UI to handle chunked content and to show “thinking…” vs final answer states.
- If the API returns a `signature_delta` or `content_block_delta` when streaming, capture it and attach it to subsequent calls as required by the spec.

If you need to show intermediate reasoning progress in a UI, stream the response. The server will emit `thinking_delta` events followed by `text_delta` events.

```
curl https://api.cometapi.com/v1/messages \
  --header "x-api-key: $CometAPI_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 16000,
    "stream": true,
    "thinking": { "type": "enabled", "budget_tokens": 8000 },
    "messages": [ { "role": "user", "content": "Walk me through debugging this failing unit test and propose fixes." } ]
  }'
```

When streaming, handle `content_block_start`, `content_block_delta` (which includes `thinking_delta` and `text_delta`), and `content_block_stop` events in order. This is how you can display the model’s step-by-step reasoning as it happens.

## How does Claude Code interact with thinking mode?(terminal + VS Code)

Claude Code is the interactive, agentic coding terminal that integrates the Messages API and tool runners. The CLI/IDE experience exposes thinking in two ways:

- **Global / per-session settings:** Claude Code exposes a `/config` settings panel to adjust behavior (how the agent asks for permissions, whether to preserve thinking blocks, etc.). Use that UI rather than retyping raw JSON if you want a persistent behavior change.
- **Model selection & CLI commands:** You can choose `claude-sonnet-4-5` or `claude-opus-4-5` as the active model in the REPL; the tools and thinking behavior then follow the Messages API semantics. The CHANGELOG and release notes indicate thinking is now enabled by default for some Opus 4.5 deployments and that thinking configuration is surfaced through `/config`.

Practical flow in Claude Code:

1. Start a project in the REPL.
2. Use `/config` to inspect thinking-related flags (preservation, verbosity, etc.).
3. Ask the agent to run a long task — it will produce thinking content and, if needed, ask for permission to run particular bash steps. Preserve thinking blocks when you need to verify or re-run decisions later.

### Installation and Setup

Claude Code requires Node.js and can be installed globally.

```
# Install Claude Code CLI
npm install -g @anthropic/claude-code

# Authenticate
claude-code --init
```

### Activating Thinking in the Terminal

Claude Code supports various flags and natural language triggers to control its reasoning depth.

| Command/Trigger | Description |
| --- | --- |
| claude-code --think | Starts a session with extended thinking enabled by default. |
| claude-code --model sonnet-4.5 | Specifies the latest frontier model. |
| /think <task> | A slash command within the CLI to invoke a specific thinking-heavy task. |
| "ultrathink" | A natural language keyword that instructs Claude to use the maximum possible reasoning budget. |

Tips:

- Use `think`/`think harder` when you want the agent to explore alternative implementations.
- When Claude Code performs tool calls (run tests, git operations), preserve any `thinking` blocks if the CLI/agent returns them; otherwise the agent may lose context between steps.

## Benefits of Interleaved Thinking and Block Preservation

For advanced agentic workflows, Claude 4.5 introduces two beta features that significantly enhance multi-turn interactions and tool use: **Interleaved Thinking** and **Thinking Block Preservation**.

### Interleaved Thinking (Beta)

Standard reasoning occurs once before the output. **Interleaved Thinking** (enabled via the `interleaved-thinking-2025-05-14` header) allows Claude to "think" between tool calls.

Imagine Claude is debugging a server:

1. **Think:** "I should check the logs first."
2. **Tool Call:** `read_file(logs.txt)`
3. **Think:** "The logs show a database timeout. Now I need to check the connection pool settings."
4. **Tool Call:** `read_file(db_config.yml)`

This "continuous reflection" ensures that the model adapts its strategy based on the data it receives from tools, rather than following a rigid, pre-defined plan.

### Thinking Block Preservation

In multi-turn conversations, especially those involving tool use, it is critical to pass the previous `thinking` blocks back to the API.

- **Reasoning Continuity:** By receiving its previous thoughts, Claude maintains the logical context of its journey.
- **Opus 4.5 Optimization:** In Claude Opus 4.5, this behavior is automated. The model preserves all previous thinking blocks in its context by default, ensuring that even in sessions lasting 30+ hours, the model doesn't "forget" why it made certain architectural decisions ten turns ago.

## Best practices for using THINKING mode with Claude 4.5

### Choose the right model and budget for the task:

**Use Sonnet 4.5 for coding and agentic workflows** where you need the best trade-off of speed, cost, and strong coding abilities; use **Opus 4.5** for the deepest reasoning and the largest context windows or when you plan to run long autonomous sessions. Both support extended thinking. Pick `budget_tokens` proportionally to the complexity of the task (start small for experiments; raise budget only if you observe material quality improvements).

### Monitor and control cost & latency

You are *charged* for the full thinking tokens Claude produces, not the summarized output you receive. That means long internal deliberations increase cost even if you only see a short summary. Track token usage and consider gradual tuning (for example: 2k → 8k → 32k) when moving from exploration to production.

### Preserve thinking blocks only when necessary

Thinking blocks can be cryptographically signed and preserved for later verification and for interleaved tool use. Avoid echoing thinking blocks in every subsequent request unless your workflow requires the model to retain its prior internal deliberations (for example, when an agent will re-run steps and needs the preserved rationales). Preserving thinking all the time increases context volume and may complicate token accounting.

### When to stream thinking to users

Streamed thinking is excellent for developer tooling and educational UIs (showing “work in progress” while the model deliberates). Do **not** stream raw thinking to end users of production-facing consumer apps without considering safety and redaction: summarized thinking exists for precisely this reason. If you stream, provide UI affordances that label internal reasoning (e.g., “Assistant reasoning — internal”), and control whether the final user sees the summarized or the full reasoning.

### Tool use and interleaving

When combining thinking with tools (code execution, web fetch, local processes), use the *interleaved thinking* design when you need the model to select tools, run them, and reason on results within the same turn. Interleaving increases complexity (and may require feature flags) but is powerful for agentic automation. Be explicit about what thinking you preserve, and test how the model selects tools under a thinking enabled run.

## Practical troubleshooting and operational notes

### Common errors and what they mean

- **Invalid thinking + forced tool choice**: If you request thinking but also force particular tool-use modes that are incompatible with thinking, the API will return an error — do not mix forcing `tool_choice: {"type":"tool","name":"..."}` with thinking.
- **Budget > max\_tokens**: For interleaved thinking scenarios the effective token rules differ — the platform docs explain when `budget_tokens` can exceed `max_tokens`. Read the “interleaved thinking” section carefully before testing large budgets.
- **Signature validation**: If you preserve thinking blocks for later calls, include the returned `signature` so the API can verify they came from Claude; this prevents tampering and keeps the chain verifiable.

### Observability & instrumentation

Log: (1) `model` selection, (2) `thinking.budget_tokens`, (3) actual thinking token consumption (you are billed for it), (4) streaming latencies (time to first `thinking_delta`), and (5) final text tokens. Use these metrics to build budgets and SLOs for user-facing flows.

### Progressive rollout & human-in-the-loop

Roll out thinking-enabled models behind feature flags. Start with a percentage of developer or internal traffic, collect failures or redactions, and iterate prompts and budgets. For sensitive domains, require human review on outputs that include substantial internal reasoning before release.

### Debugging tips

- Start small: enable low `budget_tokens` and scale up to understand incremental improvements.
- Turn on streaming and log `content_block_delta` / signature events to understand when the model produces thinking blocks.
- If using Claude Code: check `/config` and the project-level settings; consult the Claude Code changelog if behavior doesn’t match expected defaults.

## Conclusion:

Claude 4.5, combined with the power of Extended Thinking and the Claude Code CLI, represents the most significant leap in developer productivity since the invention of the IDE. By allowing the model to "show its work" and deliberate over complex problems, Anthropic has moved beyond the "chatbot" era and into the "agentic" era.

Whether you are integrating the Messages API into a custom dev-tool or using Claude Code to manage your daily PRs, mastering Thinking Mode is essential. It provides the transparency needed for trust and the reasoning depth needed for excellence.

Developers can access Claude 4.5([**Claude Sonnet 4.5**](https://www.cometapi.com/models/anthropic/claude-sonnet-4-5) , [**Claude Haiku 4.5**](https://www.cometapi.com/models/anthropic/claude-haiku-4-5), [**Claude Opus 4.5**](https://www.cometapi.com/models/anthropic/claude-opus-4-5-20251101)) model through CometAPI. To begin, explore the model capabilities of [CometAPI](https://www.cometapi.com/) in the [Playground](https://www.cometapi.com/console/playground) and consult the API guide for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. CometAPI offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Free trial of Claude 4.5](https://www.cometapi.com/console/login)!

---

*Originally published at [https://www.cometapi.com/how-to-use-thinking-mode-in-claude-4-5/](https://www.cometapi.com/how-to-use-thinking-mode-in-claude-4-5/).*
