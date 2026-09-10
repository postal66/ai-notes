<!-- social-ops-fingerprint:3a2fac11bf11e51be47216d5695fadf5ae50eb64a6e194815364f25e989b5f86 -->
---
title: Claude Sonnet 5: Features, Benchmarks, Pricing & Use Cases  in 2026
---
# Claude Sonnet 5: Features, Benchmarks, Pricing & Use Cases  in 2026

![Claude Sonnet 5: Features, Benchmarks, Pricing & Use Cases  in 2026](https://resource.cometapi.com/What%20is%20claude%20sonnet%205.jpg)

## Quick Answer: What Is Claude Sonnet 5?

[Claude Sonnet 5](https://www.cometapi.com/models/anthropic/claude-sonnet-5/) is Anthropic’s next-generation Sonnet-class AI model, released on June 30, 2026. It is designed for coding agents, tool use, long-context reasoning, document analysis, and professional automation. It supports a 1M-token context window, 128k max output tokens, adaptive thinking by default, and API access through Claude Platform and CometAPI.

## Quick Facts About Claude Sonnet 5

| Item | Claude Sonnet 5 Details |
| --- | --- |
| Provider | Anthropic |
| Release date | June 30, 2026 |
| API model ID | claude-sonnet-5 |
| Context window | 1M tokens |
| Max output | 128k tokens on synchronous Messages API |
| Official launch pricing | $2 / million input tokens and $10 / million output tokens through August 31, 2026 |
| Official standard pricing | $3 / million input tokens and $15 / million output tokens from September 1, 2026 |
| CometAPI listed pricing | $1.6 / million input tokens and $8 / million output tokens at the time of writing |
| Best for | Coding agents, tool use, document reasoning, long-context workflows, business automation |
| Important migration note | New tokenizer produces about 30% more tokens for the same text compared with Sonnet 4.6 |

## What Is Claude Sonnet 5?

Claude Sonnet 5 is Anthropic’s latest Sonnet-class model and a direct upgrade from Claude Sonnet 4.6. Anthropic describes it as the most agentic Sonnet model yet, built to make plans, use tools such as browsers and terminals, and run longer workflows that previously required larger and more expensive models. According to Anthropic’s launch announcement, Sonnet 5 narrows the gap with Opus 4.8 while keeping the speed and price profile expected from the Sonnet family.

For API users, Claude Sonnet 5 also brings important behavior changes. Adaptive thinking is now on by default. Manual extended-thinking budgets are removed. Non-default `temperature`, `top_p`, and `top_k` settings return a 400 error. Anthropic also notes that the model uses a new tokenizer, meaning teams should retest prompt sizes, output limits, and cost assumptions before migrating production traffic.

Unlike purely scaled-up models, Sonnet 5 emphasizes practical agentic reliability—finishing tasks, checking outputs unprompted, and operating in “brownfield” (messy real-world) codebases. Early testers noted it compresses multi-day projects into hours.

## Key Features of Claude Sonnet 5

### 1. Stronger Agentic Coding

Claude Sonnet 5 is built for agentic coding workflows: debugging, refactoring, test generation, code migration, repository analysis, and multi-step engineering tasks. Anthropic’s system card reports 85.2% on SWE-bench Verified, 63.2% on SWE-bench Pro, 78.3% on SWE-bench Multilingual, and 80.4% on Terminal-Bench 2.1.

This matters because coding agents rarely fail only on syntax. They fail when they lose context, skip tests, misunderstand repo conventions, or stop halfway through a multi-step task. Sonnet 5’s improvements are aimed directly at follow-through.

![Claude Sonnet 5: Features, Benchmarks, Pricing & Use Cases  in 2026](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F9941d610909f28a504e16dd5af823df172ec6035-2600x1234.png&w=3840&q=75)

### 2. 1M-Token Long Context

Claude Sonnet 5 supports a 1M-token context window. That makes it suitable for repository-scale coding, multi-document review, long customer-support histories, legal packets, financial documents, technical manuals, and research workflows.

However, developers should not assume that 1M tokens in Sonnet 5 holds exactly the same amount of text as Sonnet 4.6. Anthropic says the updated tokenizer produces roughly 30% more tokens for the same text. That means the effective text capacity may be lower for the same token budget, even though the context window remains 1M tokens.

### 3. Adaptive Thinking by Default

Claude Sonnet 5 uses adaptive thinking by default. Instead of requiring a manually assigned thinking budget, the model decides when and how much reasoning to use. Developers can control cost and depth through the `effort` parameter.

Anthropic recommends high effort by default for complex reasoning, coding, and agentic tasks; medium effort for balanced cost-performance; low effort for latency-sensitive tasks; xhigh for harder long-running coding and agentic work; and max for the highest-capability runs.

### 4. Better Tool Use and Automation

Sonnet 5 is designed to use tools such as browsers, terminals, file systems, code execution, and structured APIs. This makes it valuable for AI agents that need to inspect information, call tools, revise plans, and complete tasks across several steps.

For CometAPI users, the recommended approach is to use the native `/v1/messages` endpoint when you need Claude-specific capabilities such as adaptive thinking, effort control, prompt caching, and Claude-style response blocks. Use the OpenAI-compatible endpoint when you want easier multi-model routing across Claude, GPT, Gemini, and other models.

### 5. Improved Safety for Agentic Contexts

Anthropic reports that Sonnet 5 has a lower overall rate of undesirable behaviors than Sonnet 4.6 and performs better in agentic safety evaluations, including resistance to certain prompt-injection attacks. It also ships with real-time cybersecurity safeguards.

This is important for production agents. A model that can use tools and act over long horizons needs stronger guardrails, especially when workflows involve code, credentials, customer data, internal tools, or external web content.

![Claude Sonnet 5: Features, Benchmarks, Pricing & Use Cases  in 2026](https://resource.cometapi.com/blog/uploads/2026/07/claude-sonnet-5-safety.webp)

## Benchmark Performance of Claude Sonnet 5

The benchmark data below comes from Anthropic’s Claude Sonnet 5 system card and launch materials.

| Benchmark | What It Measures | Claude Sonnet 5 | Claude Sonnet 4.6 | Why It Matters |
| --- | --- | --- | --- | --- |
| SWE-bench Verified | Real GitHub issue resolution | 85.2% | Not in summary table | Strong signal for coding agents |
| SWE-bench Pro | Harder multi-file repo issues | 63.2% | 58.1% | Better on complex engineering tasks |
| SWE-bench Multilingual | Coding across 9 languages | 78.3% | Not in summary table | Useful for global engineering teams |
| Terminal-Bench 2.1 | Terminal-based coding tasks | 80.4% | 67.0% | Strong command-line agent performance |
| BrowseComp | Agentic web search | 84.7% single-agent / 86.6% multi-agent | 76.2% | Better web research and information retrieval |
| Humanity’s Last Exam, no tools | Frontier knowledge/reasoning | 43.2% | 34.6% | Stronger broad reasoning |
| Humanity’s Last Exam, with tools | Reasoning plus tools | 57.4% | 46.8% | Better tool-augmented problem solving |
| OSWorld-Verified | Computer-use tasks | 81.2% | 78.5% | Useful for GUI and desktop-style agents |
| FrontierCode v1 | Agentic software engineering | 38.8% | 15.1% | Large improvement in real coding workflows |
| GDPval-AA v2 | Professional work tasks, ELO | 1609 | 1381 | Stronger business deliverables |
| AutomationBench | Business automation | 13.5% | 5.3% | Better workflow automation |
| HealthBench Professional | Clinical-task benchmark | 57.8% | 44.2% | Stronger expert-domain reasoning, with review needed |

Key highlights:

- **Coding Benchmarks**: Notable gains on SWE-bench variants, Terminal-Bench, and FrontierCode. Sonnet 5 shines in agentic loops where sustained execution matters.
- **Reasoning**: Improvements on GPQA Diamond, MMMU, MathVista, and Humanity’s Last Exam (with/without tools).
- **Agentic Search & Computer Use**: Cost-performance curves favor Sonnet 5 at medium effort levels; high effort approaches Opus.
- **Multimodal & Professional**: Gains in OfficeQA, Legal Agent Benchmark, GDPval-AA, and health-related tasks.
- **Safety Data**: Lower overall misaligned behavior; 0% full exploit success on Firefox 147 cyber eval (safer by design).

Independent reports and user tests confirm real-world uplift, though some note variability vs. Opus on maximum-effort creative or edge-case tasks. For most production coding and automation, the speed and cost advantages win.

The biggest story is not one isolated score. It is the pattern: Sonnet 5 improves across coding, terminal work, agentic search, professional document tasks, and tool-heavy workflows. That makes it a strong default candidate for production AI applications where Sonnet 4.6 was close but not reliable enough.

## Claude Sonnet 5 Pricing

### Official Anthropic Pricing

Through August 31, 2026, Claude Sonnet 5 costs:

| Token Type | Price |
| --- | --- |
| Input tokens | $2 / million tokens |
| Output tokens | $10 / million tokens |
| 5-minute cache writes | $2.50 / million tokens |
| 1-hour cache writes | $4 / million tokens |
| Cache hits and refreshes | $0.20 / million tokens |

Starting September 1, 2026, official standard pricing becomes:

| Token Type | Price |
| --- | --- |
| Input tokens | $3 / million tokens |
| Output tokens | $15 / million tokens |
| 5-minute cache writes | $3.75 / million tokens |
| 1-hour cache writes | $6 / million tokens |
| Cache hits and refreshes | $0.30 / million tokens |

**Access Options**:

- **Claude.ai / Apps**: Default for Free/Pro; selectable on higher plans.
- **Claude Code**: Excellent for agentic coding workflows.
- **API**: Direct via Anthropic (`claude-sonnet-5`), CometAPI, Google Vertex.

### Recommended: Access via CometAPI for Unified, Cost-Effective Integration

For developers managing multiple models or seeking simplicity, **CometAPI** (cometapi.com) is an outstanding choice. It provides unified OpenAI-compatible access to 500+ models, including the full Claude family, with one API key, 20% lower than official pricing, failover, and centralized billing.

## How to Access Claude Sonnet 5

### 1. Claude.ai and Claude Code

Claude Sonnet 5 is available in Claude.ai and Claude Code. Anthropic says it is the default model for Free and Pro users and available to Max, Team, and Enterprise users.

### 2. Claude API

Developers can call the model directly through the Claude API using:

```
claude-sonnet-5
```

### 3. CometAPI

CometAPI exposes Claude Sonnet 5 through two integration styles:

| Endpoint | Best For |
| --- | --- |
| /v1/messages | Claude-native features, adaptive thinking, effort control, prompt caching, server tools |
| /v1/chat/completions | OpenAI-compatible apps, model routing, quick A/B testing across providers |

For CometAPI users, the strongest recommendation is to start with `/v1/messages` for serious Claude-native workloads, especially coding agents and long-context document tasks. Use `/v1/chat/completions` when portability across models is more important than Claude-specific controls.

## Code Example: Calling Claude Sonnet 5 Through CometAPI

Here is a Python example using the Anthropic SDK with CometAPI’s base URL. Notice that it does not set `temperature`, `top_p`, or `top_k`, because Claude Sonnet 5 rejects non-default sampling parameters.

```
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com",
)

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=4096,
    output_config={"effort": "medium"},
    messages=[
        {
            "role": "user",
            "content": (
                "You are a senior backend engineer. Review this API design, "
                "identify reliability risks, and suggest production-ready fixes."
            ),
        }
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

For harder coding-agent tasks, you can raise effort:

```
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=16000,
    output_config={"effort": "xhigh"},
    messages=[
        {
            "role": "user",
            "content": "Analyze this repository migration plan and produce a step-by-step implementation checklist.",
        }
    ],
)
```

Avoid this old pattern:

```
# Not recommended for Claude Sonnet 5
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=4096,
    temperature=0.2,
    thinking={"type": "enabled", "budget_tokens": 8000},
    messages=[{"role": "user", "content": "Solve this problem."}],
)
```

Manual thinking budgets return an error, and non-default sampling parameters return an error.

## Best Use Cases for Claude Sonnet 5

### Coding Agents and Software Engineering

Claude Sonnet 5 is one of the best fits for AI coding agents. Use it for debugging, test generation, refactoring, pull request analysis, repository migration, dependency updates, and codebase Q&A.

### Long-Context Document Reasoning

The 1M-token context window makes Sonnet 5 useful for reviewing long policies, contracts, technical documentation, financial reports, customer histories, and multi-file project archives.

### Business Workflow Automation

Sonnet 5 can support agents that update CRM records, draft customer responses, analyze spreadsheets, summarize meetings, produce reports, and coordinate multi-step operations.

### Research and Knowledge Work

Its BrowseComp, HLE, GDP.pdf, and GDPval-AA performance suggest strong use in research workflows where the model must combine tool use, document reading, and structured reasoning.

### Customer Support and Internal Assistants

For support teams, Sonnet 5 can analyze long conversation histories, match policies, draft replies, and escalate uncertain cases. Use lower effort for simple routing and higher effort for complex cases.

## CometAPI Recommendations

For developers building on CometAPI, Claude Sonnet 5 works best as a high-performance default model for serious production workflows.

Use `claude-sonnet-5` when you need strong reasoning, coding, long-context analysis, and agentic follow-through. Pair it with cheaper models for simple tasks such as classification, tagging, and short summarization. For the hardest reasoning tasks, route selectively to Claude Opus 4.8 or Claude Fable 5.

A practical routing setup:

| Task Type | Recommended Model Strategy |
| --- | --- |
| Simple classification | Lower-cost fast model |
| Customer support draft | Claude Sonnet 5 at low or medium effort |
| Code review or bug investigation | Claude Sonnet 5 at high or xhigh effort |
| Long document analysis | Claude Sonnet 5 with prompt caching |
| Hard enterprise reasoning | Escalate to Opus 4.8 or Fable 5 |
| Multi-provider testing | Use CometAPI OpenAI-compatible endpoint |

The biggest production tip: retest token counts before migration. Because Sonnet 5’s tokenizer can produce about 30% more tokens for the same text, your old Sonnet 4.6 cost and context assumptions may not hold.

## FAQ

### Is Claude Sonnet 5 available now?

Yes. Anthropic released Claude Sonnet 5 on June 30, 2026. It is available through Claude.ai, Claude Code, Claude Platform, and CometAPI.

### What is the Claude Sonnet 5 API model ID?

The API model ID is `claude-sonnet-5`.

### How much does Claude Sonnet 5 cost?

Official Anthropic launch pricing is $2 per million input tokens and $10 per million output tokens through August 31, 2026. Standard pricing becomes $3 per million input tokens and $15 per million output tokens from September 1, 2026. CometAPI currently lists $1.6 input and $8 output per million tokens.

### Is Claude Sonnet 5 better than Claude Sonnet 4.6?

Yes, especially for coding, agentic search, terminal work, professional tasks, and long-context workflows. Anthropic’s system card reports major improvements on Terminal-Bench, FrontierCode, BrowseComp, HLE, GDPval-AA, AutomationBench, and HealthBench Professional.

### Should I use Claude Sonnet 5 or Claude Opus 4.8?

Use Claude Sonnet 5 for strong cost-performance in coding agents, document reasoning, and production automation. Use Claude Opus 4.8 when your task requires higher peak reasoning, harder agentic work, or cybersecurity workflows that require reduced guardrails.

## Conclusion

Claude Sonnet 5 is a major upgrade for developers building coding agents, automation systems, document workflows, and long-context AI applications. Its strongest value is not just higher benchmark scores; it is the combination of stronger agentic behavior, 1M-token context, adaptive thinking, improved tool use, and lower cost than Opus-tier models.

**Next Steps:**

- Test on Claude.ai or via API.
- Integrate via CometAPI for multi-model flexibility.
- Monitor Anthropic’s Transparency Hub for ongoing benchmarks.

---

*Originally published at [https://www.cometapi.com/what-is-claude-sonnet-5/](https://www.cometapi.com/what-is-claude-sonnet-5/).*
