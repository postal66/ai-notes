<!-- social-ops-fingerprint:a0e326f81bcf8f65305b3d23994cbc947cfb96017e863cc17baf89a297ab520c -->
---
title: How to Use Claude Fable 5.1 API
---
# How to Use Claude Fable 5.1 API

![How to Use Claude Fable 5.1 API](https://resource.cometapi.com/How%20to%20Use%20the%20Claude%20Fable%205.1%20API.jpeg)

**Quick summary:** To use the [Claude Fable 5.1 API](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) in CometAPI, prepare an API key, set the model ID to `claude-fable-5-1`, and validate a small request before building a longer workflow. This guide covers access, effort, streaming, tools, caching, migration, and production checks. Treat deployment as more than changing a model string: confirm route compatibility, validate outputs, and measure accepted-task quality, latency, and cost before expanding usage.

## Key Takeaways

- **Get one request working first:** confirm credentials, model access, the chosen endpoint, and a usable response with non-sensitive test data.
- **Choose effort deliberately:** start at high, then compare other settings on representative tasks rather than using maximum effort for every request. Claude Code defaults to High. Claude Cowork / Claude.ai defaults to Medium
- **Review migration behavior:**[forced tool selection is rejected](https://platform.claude.com/docs/en/models/fable-5-1/overview); keep required workflow steps and tool-argument validation in application code.
- **Measure the complete workflow:** track cache usage, token cost, latency, refusals, fallback behavior, and whether the final result passes your acceptance checks.

For background, see CometAPI’s [earlier Fable 5.1 tracker](https://www.cometapi.com/what-is-claude-fable-5-1-what-is-confirmed/) and [Fable 5 API tutorial](https://www.cometapi.com/how-to-use-claude-fable-5-api/). This article concentrates on the current integration workflow.

## What Is Claude Fable 5.1?

[Claude Fable 5.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) is Anthropic's highest-capability generally available model for ambitious coding, multistep research, computer use, and document-heavy professional workflows. Anthropic recommends starting most workloads with Claude Opus 5 and escalating to Fable 5.1 when high-effort Opus evaluations still fall short.

The distinction is operational: Fable 5.1 is designed to keep working across dependent steps, recover after a failed tool call, verify results, and report progress during long runs. That can improve completion rates, but it also makes cost, latency, and observability central to deployment.

## Claude Fable 5.1 API Specifications

| Official specification | Claude Fable 5.1 |
| --- | --- |
| Provider | Anthropic |
| Model ID | claude-fable-5-1 |
| Release date | September 1, 2026 |
| Context window | 1,000,000 tokens |
| Maximum output | 128,000 tokens |
| Input and output | Text and images to text |
| Thinking | Adaptive, always on |
| Default effort | API is High, Claude Code defaults to High,Claude Cowork / Claude.ai defaults to Medium |
| Effort levels | low, medium, high, xhigh, max |
| Knowledge cutoff | June 2026 |
| Official price | $10 input / $50 output per million tokens |
| Cache read | $0.25 per million tokens |

The official overview confirms a [1M context window and 128K maximum output](https://platform.claude.com/docs/en/models/fable-5-1/overview). Adaptive thinking is always active; reasoning depth is controlled with effort rather than a traditional thinking-token budget.

## Claude Fable 5.1 API: Official Benchmark Performance

The benchmark summary is intentionally compact because the article's main purpose is implementation. The results below identify where the API premium is most likely to matter.

| Anthropic benchmark | Claude Fable 5.1 | Claude Fable 5 | Claude Opus 5 | GPT-5.6 Sol |
| --- | --- | --- | --- | --- |
| Terminal-Bench-Science 0.1 | 52.6% | 24.7% | 29.0% | 22.4% |
| Terminal-Bench 4.0 | 55.8% | 42.0% | 52.3% | 37.3% |
| GDPval-AA v2 | 1,853 Elo | 1,723 | 1,824 | 1,711 |
| OSWorld 2.0, partial | 77.9% | 72.9% | 75.4% | — |
| Humanity's Last Exam, no tools | 60.9% | 57.8% | 56.6% | — |
| AutomationBench | 31.4% | 17.1% | 26.9% | 19.6% |
| CursorBench 3.2.0 | 73.4% | 70.5% | 70.0% | 67.2% |

![How to Use Claude Fable 5.1 API](https://resource.cometapi.com/blog/uploads/2026/09/official_anthropic.png)

[*Anthropic's official Claude Fable 5.1 benchmark comparison*](https://www.anthropic.com/claude/fable)

The largest generational gain in this set is Terminal-Bench-Science: 52.6% versus 24.7%. AutomationBench rises from 17.1% to 31.4%, while Terminal-Bench 4.0 improves to 55.8%. The result is a strong case for testing Fable 5.1 on research agents, long-running coding, and business automation—not for routing every short request to the most expensive model.

## What Changed From Claude Fable 5 API?

| Dimension | Claude Fable 5.1 | Claude Fable 5 | Migration impact |
| --- | --- | --- | --- |
| Core role | Stronger long-running agents and research | Original public Mythos-class model | Re-evaluate hardest workflows |
| Forced tool choice | Returns an error | Previously supported | Remove any and named forcing |
| Thinking history | Stricter compatibility rules | Earlier behavior | Keep histories append-only |
| Progress updates | Readable updates between tool calls | Not available in this form | Expose long-run status |
| Per-message effort | Available in beta | Not available in this form | Tune depth within a conversation |
| Cache read price | $0.25 / MTok | $1.00 / MTok | Recalculate long-context economics |
| Input/output price | $10 / $50 per MTok | $10 / $50 per MTok | No list-rate change |

### Three Breaking Changes

#### Forced Tool Use Is No Longer Supported

Claude Fable 5.1 rejects `tool_choice` values that force any tool or a specifically named tool, returning a 400 invalid-request error. Keep automatic selection, use strict schemas or structured outputs for validation, and enforce mandatory workflow steps in application orchestration rather than by forcing a model tool call.

#### Earlier Models Cannot Read Fable 5.1 Thinking Blocks

Thinking compatibility is one-way: Fable 5.1 can consume thinking blocks created by earlier compatible Claude models, but earlier models cannot read blocks created by Fable 5.1. A router or fallback that moves to an earlier model may drop those blocks before inference, so integrations should log model switches and test fallback behavior explicitly.

#### Editing Earlier Turns Invalidates Preserved Thinking

Changing an earlier system prompt, tool definition, message, or referenced file bytes can invalidate later thinking blocks. Treat the conversation prefix as append-only, use mid-conversation instructions instead of rewriting history, and monitor prefix-mismatch transformations during migration.

### Five Additive API Capabilities

#### Per-Message Effort

Applications can change effort during a conversation without invalidating the prompt cache. This beta capability lets a workflow lower effort for routine follow-ups and raise it for difficult planning, debugging, or verification turns.

#### Turn-Scoped System Messages

A beta system message can apply to one turn and then stop rendering after the next user message while remaining unchanged in history. This is useful for temporary instructions in tool loops because it preserves both prompt-cache matching and the validity of later thinking blocks.

#### Readable Progress Updates Between Tool Calls

With the beta progress-display option, selected thinking blocks can carry short status updates that an application may show to users while private reasoning remains hidden. Long-running agents should treat these updates as operational status, not as final answers.

#### Lower Cache-Read Pricing

Cache reads cost $0.25 per million tokens, one quarter of the Fable 5 cache-read rate, while base input and output prices remain unchanged. This can materially reduce the cost of long sessions that repeatedly reuse a stable cached prefix.

#### Content Provenance

Generated text carries Anthropic's statistical watermark, while supported media retrieved through the Files API can include signed C2PA Content Credentials. These provenance mechanisms do not add prompt tokens or require request-format changes.

## What Do You Need Before Using the Claude Fable 5.1 API?

- **An account and API key:** sign in to CometAPI and generate a key in the [API key console](https://www.cometapi.com/console/token). Check model access and that your account is ready for usage-based billing before sending test calls.
- **A local runtime:** use a terminal with curl for the first HTTP example. For the Python examples, prepare Python and pip in an isolated environment, then install the SDK used by your chosen example.
- **A selected route:** the [Claude Fable 5.1 API](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) in CometAPI offers Messages and Chat Completions formats. Use the matching base URL and request format; do not mix their payloads.
- **Secure configuration:** set `COMETAPI_KEY` outside committed source files, use `claude-fable-5-1` as the model ID, and ensure your network can reach `https://api.cometapi.com.`
- **A safe test and acceptance check:** begin with a short, non-sensitive prompt. Confirm that the response contains usable content, inspect usage and completion status, and check your organization’s data-handling requirements before submitting real documents or logs.

## How to Access Claude Fable 5.1 Through CometAPI

CometAPI exposes [Claude Fable 5.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) through an Anthropic-compatible Messages route and an OpenAI-compatible Chat Completions route. Use Messages when you need native effort, thinking, caching, and Claude tool semantics; use Chat Completions when your application already standardizes on the OpenAI SDK.

### Step 1: Store the API key

```
export COMETAPI_KEY="your-cometapi-key"
```

```
$env:COMETAPI_KEY="your-cometapi-key"
```

### Step 2: Make the first Messages request

```
curl https://api.cometapi.com/v1/messages \
  --header "Authorization: Bearer $COMETAPI_KEY" \
  --header "content-type: application/json" \
  --data '{
    "model": "claude-fable-5-1",
    "max_tokens": 2048,
    "messages": [{
      "role": "user",
      "content": "Review this deployment architecture and list the three highest-risk failure modes."
    }]
  }'
```

### Step 3: Use the Anthropic Python SDK

```
pip install anthropic
```

```
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com",
)

response = client.messages.create(
    model="claude-fable-5-1",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "Find the root cause of this test failure and propose a verified patch.",
    }],
)

print(response.content[0].text)
```

### Step 4: Use the OpenAI Python SDK

```
pip install openai
```

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
)

response = client.chat.completions.create(
    model="claude-fable-5-1",
    messages=[{
        "role": "user",
        "content": "Design a migration plan for this service.",
    }],
)

print(response.choices[0].message.content)
```

## How does the reason for the Claude Fable 5.1 API work?

### Earlier Models Cannot Read Claude Fable 5.1 Thinking Blocks

Thinking blocks produced by Fable 5.1 are not backward-compatible with earlier Claude models. If a workflow changes models mid-conversation, remove incompatible thinking blocks or start a new branch while retaining only the user-visible messages and tool results required for the next request.

### Editing Earlier Turns Invalidates Preserved Thinking

A preserved thinking block is cryptographically bound to the preceding conversation state. Changing an earlier system prompt, tool definition, user message, assistant response, or tool result can break that binding and trigger a thinking-history error. Keep the replayed prefix byte-for-byte stable and append new turns instead of rewriting old ones.

### Preserved Thinking Across Turns

When the conversation prefix remains unchanged, preserved thinking can carry useful reasoning state into later turns. Store thinking blocks with their original message order, replay them only to a compatible model, and tre at a history edit as a new conversation branch rather than mutating the existing transcript.

### Control Reasoning With Effort

Start difficult production work at high effort, then test lower settings on routine turns and higher settings only where accepted-task quality improves enough to justify additional latency and tokens. Because effort can change between turns, one conversation no longer needs a single reasoning level throughout.

Fable 5.1 uses [adaptive thinking as its only thinking mode](https://platform.claude.com/docs/en/models/fable-5-1/overview). Begin at high effort, then measure lower settings for routine work and xhigh or max only when additional capability justifies cost and latency.

| Effort | Recommended role | Tradeoff |
| --- | --- | --- |
| low | Routine, well-specified work | Fastest and most economical |
| medium | Balanced production traffic | Moderate depth |
| high | Default difficult work | Best starting point |
| xhigh | Long-running coding and agents | More latency and tokens |
| max | Highest-value hardest tasks | Cost and latency secondary |

```
response = client.messages.create(
    model="claude-fable-5-1",
    max_tokens=8192,
    output_config={"effort": "high"},
    messages=[{
        "role": "user",
        "content": "Audit this repository migration plan.",
    }],
)
```

## Claude Fable 5.1 API: Stream Long Responses, Use Tools and Prompt Caching

Configure the following controls together: reasoning effort, streaming, tool execution, prompt caching, and the handling of safeguards and retained data. Each affects how a long-running request is observed, validated, and operated.

### Stream Long Responses

Streaming is the safer default for long, high-effort tasks because it avoids waiting for a large response to complete before the application receives any output.

```
with client.messages.stream(
    model="claude-fable-5-1",
    max_tokens=8192,
    output_config={"effort": "high"},
    messages=[{
        "role": "user",
        "content": "Analyze these logs and produce a remediation plan.",
    }],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### Use Tools Without Forced Tool Choice

Fable 5.1 [rejects forced tool selection](https://platform.claude.com/docs/en/models/fable-5-1/overview) using tool\_choice type any or a named tool. Use automatic selection, strict schemas, validate tool arguments in application code, and control mandatory workflow sequencing outside the model. If a workflow requires a specific tool to run, don't rely on `tool_choice` to enforce the sequence. Make the application invoke that tool or implement the required step in orchestration code.

```
tools = [{
    "name": "search_incidents",
    "description": "Search recent production incidents",
    "input_schema": {
        "type": "object",
        "properties": {
            "service": {"type": "string"},
            "days": {"type": "integer"},
        },
        "required": ["service", "days"],
    },
}]

response = client.messages.create(
    model="claude-fable-5-1",
    max_tokens=4096,
    tools=tools,
    tool_choice={"type": "auto"},
    messages=[{
        "role": "user",
        "content": "Review checkout incidents from the last 30 days.",
    }],
)
```

### Use Prompt Caching for Long Contexts

Anthropic lists [cache reads at $0.25 per million tokens](https://platform.claude.com/docs/en/models/fable-5-1/overview), one quarter of the Fable 5 rate. Put stable system instructions, tool schemas, and large reference material before dynamic user content, then verify cache hits in usage metadata.

```
messages = [{
    "role": "user",
    "content": [
        {
            "type": "text",
            "text": large_reference_document,
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": "Identify obligations that changed in this revision.",
        },
    ],
}]
```

### Handle Safeguards and Data Retention

Anthropic states that many flagged cybersecurity and biology requests [route to less capable models](https://www.anthropic.com/claude/fable). Treat a refusal or fallback as an application state: record the stop reason, show an appropriate user message, and route to an approved alternative where policy allows.

Fable also requires [30-day data retention by default](https://www.anthropic.com/claude/fable) for safety monitoring. Confirm organizational eligibility and retention settings before debugging a syntactically valid request as if it were only an API-format problem.

## Fable 5.1 vs Opus 5 vs Sonnet 5

| Decision dimension | Claude Fable 5.1 | Claude Opus 5 | Claude Sonnet 5 |
| --- | --- | --- | --- |
| Context / max output | 1M / 128K | 1M / 128K | 1M / 128K |
| Official input/output | $10 / $50 | $5 / $25 | $2 / $10 |
| Relative latency | Slower | Moderate | Fast |
| Default effort | high | high | high |
| Main strength | Maximum long-horizon capability | Premium general reasoning | Speed/cost balance |
| Best production role | Capability escalation | Default complex work | High-volume baseline |

Selection result: start routine traffic on Sonnet 5, use Opus 5 for complex general work, and escalate only the hardest or repeatedly failing tasks to Fable 5.1. This follows Anthropic's guidance and prevents premium reasoning from becoming the default cost of every request.

## Pricing Through CometAPI

| Route | Input / MTok | Output / MTok | Cache read / MTok |
| --- | --- | --- | --- |
| Anthropic list price | $10 | $50 | $0.25 |
| CometAPI listed price | $8 | $40 | Check live route |
| Nominal input/output difference | 20% lower | 20% lower | Varies by route |

The [live CometAPI model page](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) is the source of truth for current route availability and pricing. For a request with 100,000 uncached input tokens and 10,000 output tokens, the simple CometAPI estimate is $1.20; actual cost can change with caching, reasoning, batch behavior, and routing. Prices are subject to change; check the live model page before production budgeting.

## Migration Checklist From Fable 5

1. Change the model ID from claude-fable-5 to claude-fable-5-1.
2. Remove tool\_choice any and named-tool forcing; use auto.
3. Replace old thinking-budget assumptions with output\_config.effort.
4. Begin evaluation at high effort, then tune against real tasks.
5. Keep histories append-only when they contain preserved thinking blocks.
6. Increase max\_tokens for long high-effort runs.
7. Verify cache hits from usage metadata.
8. Handle refusals and fallbacks as explicit states.
9. Replay production traces and compare accepted-task rate, latency, and cost.

> **Safest migration strategy: keep histories append-only.** Fable 5.1 can preserve thinking blocks across turns, but replayed thinking blocks are bound to the preceding conversation state; changing earlier system prompts, tools, or messages can invalidate that binding.

## Common API Errors

### 400 error after changing tool calls

Likely cause: forced tool\_choice using any or a named tool. Use auto and enforce required sequence in application logic.

### claude-fable-5.1 does not work

The canonical ID uses hyphens: claude-fable-5-1.

### Output ends earlier than expected

`effort controls how much reasoning the model performs, while max_tokens limits the response token budget. Higher effort can require more output budget, so production applications should tune both independently. Raise max_tokens where justified and stream long responses.`

### Prompt cache never hits

Keep the cached prefix byte-for-byte stable; timestamps, reordered tools, and changing system messages prevent reuse.

### An HTTP-success response contains no normal answer

Inspect stop\_reason and fallback metadata instead of treating every refusal as a transport error.

### Replaying history produces a thinking error

Do not edit earlier turns before preserved Fable 5.1 thinking blocks. Use append-only history or current migration controls.

## How Should You Use the Claude Fable 5.1 API in Production?

Separate request routing, model execution, tool execution, validation, and evaluation. Log model ID, effort, latency, token usage, cache usage, stop reason, fallback behavior, and final task success.

Use Fable 5.1 for repository-wide migrations, difficult debugging, long-running agents, deep research, large-document synthesis, and high-value tasks where cheaper models repeatedly fail. Avoid it as the default for summaries, classification, extraction, and short customer-service responses.

### Example: Investigate a Checkout Incident

A team could provide sanitized checkout errors, recent deployment diffs, and relevant runbooks. The application retrieves matching incident records, then asks the model to rank possible causes and connect each hypothesis to evidence. An engineer reviews the proposed diagnostic steps and approves a test in a sandbox using synthetic transactions. The acceptance gate is reproducible behavior, traceable evidence, and passing regression checks; any production remediation requires separate human approval.

### Example: Analyze Changes to Operating Requirements

A team could supply an approved operating manual, supporting policies, and a revised draft. Keep the unchanged reference material as stable context, then ask the model to compare changed obligations, responsible teams, deadlines, and exceptions. Each proposed finding should reference the relevant passages in both versions and distinguish explicit changes from uncertain interpretations. The acceptance gate is a reviewer confirming every reported change against its cited evidence before updating procedures or notifying affected teams.

## Conclusion

Claude Fable 5.1 is not a drop-in model-string update. Its forced-tool behavior, thinking-history rules, effort controls, cache economics, and long-run progress features require deliberate migration.

The most effective deployment uses [Claude Sonnet 5](https://www.cometapi.com/models/anthropic/claude-sonnet-5/) for routine volume, [Claude Opus 5](https://www.cometapi.com/models/anthropic/claude-opus-5/) for complex default traffic, and [Claude Fable 5.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) as a measured capability escalation. Promote it only when accepted-task completion improves enough to justify total cost and latency.

---

*Originally published at [https://www.cometapi.com/how-to-use-claude-fable-5-1-api/](https://www.cometapi.com/how-to-use-claude-fable-5-1-api/).*
