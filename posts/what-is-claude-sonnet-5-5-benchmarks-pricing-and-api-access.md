<!-- social-ops-fingerprint:5fef8339765fd55023fd81550e79fa34b93cfdad64725ee9490e75f6056a0897 -->
---
title: What Is Claude Sonnet 5.5?Benchmarks, Pricing, and API Access
---
# What Is Claude Sonnet 5.5?Benchmarks, Pricing, and API Access

![What Is Claude Sonnet 5.5?Benchmarks, Pricing, and API Access](https://resource.cometapi.com/official-8.jpg)

## TL;DR

[Claude Sonnet 5.5 is Anthropic's newest Sonnet-class model, released on September 28, 2026](https://www.anthropic.com/claude-sonnet-5-5). It is positioned as the faster, lower-cost complement to Claude Opus 5.5 for coding, well-scoped agentic work, document production, computer use, and multimodal analysis.

The model keeps standard pricing at $2 per million input tokens and $10 per million output tokens. Anthropic reports output generation that is more than 30% faster than Sonnet 5 and task-level costs that can be up to 30% lower because the newer model often completes work with fewer tokens and steps.

Published results include 70.6% on Terminal-Bench 4.0, 55.5% on CursorBench 4.0, 1844 on GDPval-AA v2.1, and 80.1% on OSWorld 2.1. The practical value is not one isolated score: Sonnet 5.5 approaches Opus 5.5 on several professional-work evaluations while retaining lower standard token prices.

## Key Takeaways

- Claude Sonnet 5.5 is the second model in Anthropic's Claude 5.5 family and is optimized for fast production work rather than the most ambiguous, open-ended tasks.
- It supports a 1M-token context window, up to 128K output tokens, text and image input, adaptive thinking, tool use, and structured responses.
- Standard Claude API pricing is $2/M input, $10/M output, $0.20/M cache reads, and $2.50/M five-minute cache writes.
- Anthropic reports 30%+ faster output than Sonnet 5 and strong gains in coding, computer use, chart understanding, and long-horizon knowledge work.
- The Claude API model ID is **claude-sonnet-5-5**; developers can also access [Claude Sonnet 5.5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-sonnet-5-5/).

## What Is Claude Sonnet 5.5?

Claude Sonnet 5.5 is Anthropic's newest general-purpose Sonnet model and the second release in the Claude 5.5 family after Claude Opus 5.5. Anthropic positions it as a faster and lower-cost complement to Opus rather than as a direct replacement for the flagship.

The distinction is practical: Opus 5.5 is aimed at complex, ambiguous work requiring sustained judgment, while Sonnet 5.5 is optimized for well-scoped tasks, bug fixing, rapid iteration, coding, document production, and high-volume professional workflows.

### What Are the Most Important Claude Sonnet 5.5 Features?

The model combines a 1M-token context window, up to 128K output tokens, text-and-image input, adaptive thinking, adjustable effort, tool use, structured outputs, prompt caching, batch processing, and support across the Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS. For production teams, the defining combination is not a single feature but fast generation, lower task-level token use, and near-Opus performance on several well-scoped professional workloads.

## Claude Sonnet 5.5 benchmarks

Anthropic reports substantial gains across coding, long-horizon professional work, computer use, and visual understanding. The table below summarizes the company's published evaluation results.

| Benchmark and official source | Claude Sonnet 5.5 | Claude Sonnet 5 | Claude Opus 5.5 | GPT-6 Sol |
| --- | --- | --- | --- | --- |
| Terminal-Bench 4.0 | 70.6% | 10.3% | 66.4% at Xhigh | Not publicly reported |
| FrontierCode 1.1 Main | 46.2% at Max | 42.4% | 54.4% | 49.3% / 52.1% at Xhigh |
| CursorBench 4.0 | 55.5% | 34.1% | 57.8% | Not publicly reported |
| GDPval-AA v2.1 | 1844 | 1449 | 1846 | 1487 |
| AA-Briefcase v1.1 | 1811 | 1359 | 1822 | 1483 |
| Humanity's Last Exam | 64.5% with tools | 54.9% | 67.7% | Not reported in the source table |
| OSWorld 2.1 | 80.1% | 57.0% | 81.8% | Not reported in the source table |
| Chartography | 61.6% | 15.6% | 64.4% | 53.6% |

**Evaluation conditions and caveats:** Scores are not all measured at the same effort setting. The 66.4% Opus 5.5 Terminal-Bench result is reported at Xhigh. Anthropic notes that Sonnet 5.5 can score lower at Max than at Xhigh on FrontierCode because extra review steps can introduce timeouts or out-of-scope edits. Artificial Analysis ran GDPval-AA and AA-Briefcase on a pre-release Sonnet 5.5 deployment affected by a structured-output bug that Anthropic says has since been fixed. Cross-vendor GPT-6 Sol figures should also be treated as dated observations because OpenAI corrected an image-encoding issue on September 25, 2026.

**What the results mean:** Sonnet 5.5 is not simply ahead of Sonnet 5 on isolated scores. It moves much closer to Opus 5.5 on coding, professional work, computer use, and chart recognition while keeping Sonnet-tier pricing. Anthropic also reports that, at Low or Medium effort, Sonnet 5.5 can exceed Sonnet 5's best score on several evaluations at roughly one-tenth of the cost per task. That combination of capability, speed, and task-level efficiency is its main competitive advantage.

## How Good Is Claude Sonnet 5.5?

### Coding

The improvement is also operational. Anthropic reports that Sonnet 5.5 understands codebases faster, batches tool calls more efficiently, uses fewer steps, and lowers cost per completed task. FrontierCode tests whether proposed code changes are mergeable, while CursorBench uses ambiguous, multi-file tasks drawn from real coding sessions; the gains therefore reflect repository-level execution and judgment, not only short code generation. These changes matter for bug fixing, code review, test execution, and long-running coding agents.

![What Is Claude Sonnet 5.5?Benchmarks, Pricing, and API Access](https://resource.cometapi.com/blog/uploads/2026/09/official-1.png)

### Knowledge Work

The improvements extend beyond programming. GDPval-AA tests real-world professional tasks across 44 occupations and nine major industries, so Sonnet 5.5's score of 1844—versus 1449 for Sonnet 5 and 1846 for Opus 5.5—suggests that its gains transfer to practical analysis, document production, and decision-support work rather than remaining confined to laboratory reasoning tests.

Anthropic highlights financial analysis, document synthesis, slide creation, spreadsheet work, chart interpretation, source checking, information retrieval, and professional writing as areas where the model improves.

Early testers also reported less quantifiable improvements: clearer collaboration, more natural conversational judgment, and a stronger eye for design. Anthropic says the model can add polish to user interfaces and follow slide templates closely enough to produce decks requiring minimal editing; in one internal operating-review test, two experts judged the first draft ready to send without changes.

The broader implication is that Sonnet 5.5 is best understood as a professional work model, not merely a cheaper coding model.

### Computer Use

Sonnet 5.5 scores 80.1% on OSWorld 2.1, compared with 57.0% for Sonnet 5 and 81.8% for Opus 5.5. OSWorld evaluates the ability to operate graphical computer environments, so the result indicates a large generational improvement and near-Opus performance for workflows involving browsers, desktop tools, and multimodal interface understanding. Chartography results show a similar pattern in visual chart recognition: 61.6% for Sonnet 5.5 versus 15.6% for Sonnet 5.

### Speed

Anthropic reports that Sonnet 5.5 generates output more than 30% faster than Sonnet 5, making it the fastest Sonnet model at launch. Faster output combines with fewer tool calls and lower token use to shorten agent loops, reduce waiting time during iterative coding, and improve throughput in support and other high-volume workflows.

## How Much Does Claude Sonnet 5.5 Cost?

| Pricing and official source | Claude Sonnet 5.5 | CometAPI: Sonnet 5.5 | Claude Opus 5.5 |
| --- | --- | --- | --- |
| Cache reads | $0.20 / 1M | $0.16 / 1M | $0.20 / 1M |
| Five-minute cache writes | $2.50 / 1M | $2 / 1M | $5 / 1M |
| Input tokens | $2 / 1M | $1.60/M | $4 / 1M |
| Output tokens | $10 / 1M | $8.00/M | $20 / 1M |

At standard token rates, Sonnet 5.5 costs half as much as Opus 5.5 for input and output. Anthropic also says the newer Sonnet often needs fewer tokens to finish the same work than Sonnet 5, reducing cost per completed task.

These are standard Claude API prices. Cloud-provider pricing, regional processing, cache duration, batch discounts, and long-context rules can change the effective cost.

## What Safety Changes Does Claude Sonnet 5.5 Introduce?

[Anthropic says its automated behavioral audit covered roughly 1,850 scenarios](https://www.anthropic.com/claude-sonnet-5-5#safety) and found Sonnet 5.5 improved on or matched Sonnet 5 on most tested measures of alignment, resistance to misuse, and honesty.

### Cybersecurity Safeguards

Because Sonnet 5.5 has stronger cyber capabilities than its predecessor, Anthropic is deploying safeguards similar to those used for more capable models. Routine software development and ordinary bug fixing remain supported, while some higher-risk cybersecurity tasks can fall back to a safer model path.

### Biology Safeguards

The model uses the same biology safeguards as Sonnet 5, targeting a narrow set of potentially harmful requests while leaving most research, education, and clinical work unaffected.

### Anti-Distillation Protections

Anthropic says Sonnet 5.5 is the first Sonnet model to launch with safety classifiers designed to prevent reasoning extraction through industrial-scale distillation attacks. It also expands preserved thinking, tying thinking content to the account and conversation that created it so the reasoning cannot be freely detached and replayed elsewhere. Most developers will not notice this change, but systems that move conversations between accounts or alter earlier conversation state should review the migration guidance.

These statements describe Anthropic's reported safeguards, not an independent guarantee of safety for every deployment. Teams should evaluate the model against their own threat model, policies, and high-risk workflows.

## Claude Sonnet 5.5 vs Claude Sonnet 5 vs Claude Opus 5.5 vs GPT-6 Sol

Claude Sonnet 5.5 is positioned as the fast, efficient production model in this group. Anthropic reports that it generates outputs more than 30% faster than Claude Sonnet 5 while keeping the same headline token price. Claude Opus 5.5 targets harder and more ambiguous work, while GPT-6 Sol is the closest OpenAI comparison for long-context coding and agentic workflows.

| Dimension | Claude Sonnet 5 | Claude Sonnet 5.5 | Claude Opus 5.5 | GPT-6 Sol |
| --- | --- | --- | --- | --- |
| Positioning | Previous Sonnet production model | Fast, efficient production workhorse | Higher-end complex reasoning | Complex coding and agentic workflows |
| Context window | 1M | 1M | 1M | 1.05M |
| Maximum output | 128K | 128K | 128K | 128K |
| Reasoning controls | Adaptive effort | Adaptive effort | Adaptive thinking, always on | none, low, medium, high, xhigh, and max |
| Multimodal input | Text and images | Text and images | Text and images | Text and images |
| API availability | Claude API and major cloud platforms | Claude API and major cloud platforms | Claude API and major cloud platforms | Responses API and Chat Completions |
| Standard input / output price per 1M | $2 / $10 | $2 / $10 | $4 / $20 | $2 / $10 for prompts up to 272K input tokens |
| Speed | Baseline | More than 30% faster than Sonnet 5 | Optimized for harder, longer-running work | Varies by reasoning effort |
| FrontierCode 1.1 | 42.4% | 46.2% at Max | 54.4% | 49.3% / 52.1% at Xhigh |
| GDPval-AA v2.1 | 1449 | 1844 | 1846 | 1487 |
| Best suited to | Existing Sonnet workloads | High-volume coding and professional agents | Hard, ambiguous, long-running tasks | OpenAI-native coding, agents, tools, and long-context workflows |

These benchmark figures are reported cross-vendor observations rather than controlled, permanent rankings. Results depend on effort settings and deployment conditions.

## How Do You Access and Call Claude Sonnet 5.5 Through CometAPI?

Claude Sonnet 5.5 is available through Claude, the Claude Platform, Amazon Web Services, Google Cloud, and Microsoft Azure. Developers who want one OpenAI-compatible interface for multiple providers can call the model through [Claude Sonnet 5.5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-sonnet-5-5/) with the model identifier **claude-sonnet-5-5**.

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
)

response = client.chat.completions.create(
    model="claude-sonnet-5-5",
    messages=[
        {
            "role": "user",
            "content": "Analyze this codebase and identify the three highest-impact bugs.",
        }
    ],
    max_tokens=2048,
)

print(response.choices[0].message.content)
```

For production use, store the API key in an environment variable and evaluate effort settings, caching, tool calling, retry behavior, and task-level token consumption.

### What Is the Effort Setting in Claude Sonnet 5.5?

Claude Sonnet 5.5 supports adjustable effort levels that trade speed and token use against reasoning depth. Anthropic sets Medium effort by default in Claude apps and Claude Code, while the Claude Platform defaults to High.

Lower effort settings suit routine or highly structured work. Higher settings allow more reasoning and checking for harder coding, analysis, and agentic tasks. Production budgeting should therefore consider effort, tool usage, and total task completion cost rather than token price alone.

### API: What’s new compared with Sonnet 5

Five changes can break or alter existing Sonnet 5 integrations:

1. **Thinking-off migrations:** integrations that disabled thinking should switch to **thinking: {"type": "between\_tools"}**. This setting turns off up-front thinking while preserving between-tool reasoning behavior.
2. **Forced tool use:** forced tool choices now return an error; use automatic tool selection with strict schemas where appropriate.
3. **Thinking-block preservation:** thinking blocks are tied to the model and conversation. Pass them back unchanged, and do not assume they can be replayed after changing earlier system messages, tools, or account context.
4. **Computer-use tool version:** on the Claude API and Google Cloud, the older **computer\_20251124** tool is no longer accepted; migrate to the currently documented computer toolset.
5. **Advisor compatibility:** the advisor tool rejects Claude Opus 4.8, Opus 4.7, and Sonnet 5 as advisors.

One additional response-shape change may fail silently: text generated between tool calls can appear in thinking blocks instead of text blocks. Applications that stream progress messages should process responses by block type and set an appropriate display mode. Sonnet 5.5 also adds per-message effort in beta, mid-conversation system messages, mid-conversation tool changes in beta, a 512-token minimum cacheable prompt length, batch processing, Files API support, PDF and vision input, and both server-side and client-side tools.

## What Does Claude Sonnet 5.5 Mean for the Claude 5.5 Family?

- Claude Opus 5.5: complex, high-judgment, long-horizon work.
- Claude Sonnet 5.5: efficient production, coding, agents, and professional work.
- Claude Haiku 5.5: announced as the upcoming high-throughput, cost-sensitive member of the family.

The broader shift is toward measuring cost per successful task, inference speed, and model routing rather than focusing only on raw token price or a single benchmark.

## Conclusion

Claude Sonnet 5.5 is an efficiency-focused upgrade to Anthropic's production tier. It keeps Sonnet 5's $2/$10 standard token pricing while adding a 1M-token context window, up to 128K output tokens, substantially faster generation, and strong gains across coding, computer use, visual understanding, and knowledge work.

The strongest case for the model is workload economics: how reliably and quickly it completes a task, how many tool calls and tokens it consumes, and how often a workflow still needs escalation to Opus 5.5. Teams should validate those factors on their own tasks and treat cross-vendor benchmarks as dated observations rather than permanent rankings.

---

*Originally published at [https://www.cometapi.com/what-is-claude-sonnet-5-5/](https://www.cometapi.com/what-is-claude-sonnet-5-5/).*
