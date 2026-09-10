<!-- social-ops-fingerprint:c37f1673cff293ccf069207ac1e3647081afa234169d3bbbb2b74aa69f9a3521 -->
---
title: Grok 4.5 released: Architecture, release date, and other we know
---
# Grok 4.5 released: Architecture, release date, and other we know

![Grok 4.5 released: Architecture, release date, and other we know](https://resource.cometapi.com/grok-4.5%20leak.jpeg)

**TLDR** On June 28, 2026, Elon Musk announced that Grok 4.5 — built on xAI’s new 1.5-trillion-parameter V9 foundation model with supplemental training data from the Cursor AI coding platform — entered private beta at SpaceX and Tesla. Internal evaluations claim performance “close to, perhaps exceeding” Anthropic’s Claude Opus, with ongoing RLHF and Grok Build improvements.

For developers and businesses integrating frontier models today, **CometAPI** offers immediate, cost-effective access to Grok 4.3 (and other xAI models) via a single OpenAI-compatible endpoint alongside 500+ models from Anthropic, OpenAI, Google, and more — often at 20%+ savings versus direct pricing, with no prompt logging for privacy-focused workflows.

## Key Takeaways

- A quoted line attributed to Elon Musk says Grok 4.5 is in private beta at SpaceX and Tesla, [circulated by AshutoshShrivastava](https://x.com/ai_for_success/status/2071192465319858576).
- [TestingCatalog reports](https://x.com/testingcatalog/status/2071198330906878287) Grok 4.5 sits on a 1.5T V9 foundation model with Cursor data added in supplemental training.
- The only evidence-tagged signal is [Mark Kretschmann's June 28 screenshot](https://x.com/mark_k/status/2071119902841131380) showing the Grok / Cursor Composer 3 version number removed from xAI menus.
- No benchmark scores, pricing, context window, or API timing have been disclosed in this signal set.
- The Cursor training data story has been building since June 16 across at least three accounts, with [Mark Kretschmann tying Grok 5 to a 6T and 10T parameter pair](https://x.com/mark_k/status/2068745721386267133) in the Fable 5 weight class.

## Grok 4.5 release date

**Grok 4.5 entered private beta on June 28, 2026, and is scheduled for public release on July 9, 2026 (tomorrow, as of July 8).**

It builds on prior versions like Grok 4 (released around July 2025) and Grok 4.3. It should become accessible to eligible users (e.g., SuperGrok/Premium+ subscribers) shortly after the announcement. For API，CometAPI will be integrated with the grok 4.5 API immediately after its release, and will offer a cheaper acquisition price.

**Public Release**: Today (July 8, 2026), [Musk posted that](https://x.com/elonmusk/status/2074740539874775163), based on positive beta feedback, **SpaceXAI / xAI will make Grok 4.5 available to the public tomorrow** (July 9). It is described as an "Opus-class" model that is faster, more token-efficient, and lower cost than comparable models.

![Grok 4.5 released: Architecture, release date, and other we know](https://resource.cometapi.com/blog/uploads/2026/07/screenshot-20260708-161705.png)

*Source:* [*@*](https://x.com/mark_k/status/2071119902841131380)[*mark\_k*](https://x.com/elonmusk/status/2074740539874775163)

## Signals from the Architecture of grok 4.5: What we've seen

The primary source is [Elon Musk’s own X post](https://x.com/elonmusk/status/2071184354756477041) on June 28, 2026:

> “Grok 4.5, based on our 1.5T V9 foundation model, with Cursor data added in supplemental training, is now in private beta at SpaceX & Tesla. Early evals show performance close to, perhaps exceeding Opus. RL is continuing to significantly improve the model, and the Grok Build harness gets better every day…”

This was amplified by accounts like [@testingcatalog](https://x.com/testingcatalog/status/2074214554523816272) and @ai\_for\_success, with architectural details on the 1.5T V9 and Cursor integration, "Grok 4.5 is based on 1.5T V9 foundation model, with Cursor data added in supplemental training.".

**Cursor Signal**: xAI/SpaceX’s move toward acquiring or deeply partnering with Cursor (Anysphere) for ~$60B provides a rich source of real developer IDE traces, agentic workflows, and multi-file editing data. This supplemental training (post-pre-training) differentiates Grok 4.5 for coding tasks, though experts note initial pre-training integration would be even stronger.

![Grok 4.5 released: Architecture, release date, and other we know](https://pbs.twimg.com/media/HL4YkscWEAArDFf?format=jpg&name=900x900)

*Source:* [*@mark\_k*](https://x.com/mark_k/status/2071119902841131380)

The menu-state signal is narrower but more evidence-like. Per [Mark Kretschmann's June 28 post](https://x.com/mark_k/status/2071119902841131380), the version number for the Grok 1.5T / Cursor Composer 3 model was removed from xAI menus on the morning of June 28. He describes that as a pattern that can precede xAI releases. This is not a formal launch, but it is more concrete than a reposted performance claim because it is tied to a screenshot.

The later canary signal pushed the story forward. [TestingCatalog spotted](https://x.com/testingcatalog/status/2074214554523816272) a Grok web UI string reading "Unlock the full power of Chat with Grok 4.5." That kind of trace often appears before a product change, but it can also be abandoned, delayed, or hidden behind a limited rollout.

## What We Can Reasonably Expect from Grok 4.5

Given xAI’s trajectory and the leak details, here’s a grounded outlook:

1. **Enhanced Coding and Agentic Performance**: Supplemental Cursor data should boost SWE-Bench-like tasks, multi-file reasoning, and real-world developer workflows. Expect strengths in technical reasoning, debugging, and production-scale engineering — areas aligned with SpaceX/Tesla use cases.
2. **Scale and Efficiency**: At 1.5T parameters on optimized V9 (Blackwell-era GPUs via Colossus), it balances raw power with inference feasibility. RL improvements post-beta could narrow gaps in reasoning.
3. **Rapid Iteration**: Musk mentioned monthly new models from scratch. Grok 4.5 serves as a stepping stone, with a larger 2T+ run already incorporating Cursor data from pre-training.
4. **Multimodal and Tool-Use**: Building on prior Grok capabilities (vision, search, Grok Build), expect expanded agentic features.
5. **Public Rollout Timeline**: UI traces suggest days to weeks for broader access. Historical patterns indicate 1–2 weeks from teaser to preview.

**For Production Use Today**: While waiting, integrate via **CometAPI**’s Grok endpoints. Their OpenAI-compatible API supports seamless switching and offers cost savings (e.g., Grok 4 at reduced rates), perfect for building apps that will easily upgrade to Grok 4.5. Check [CometAPI Grok offerings](https://www.cometapi.com/) for details.

The hard facts come from official docs, and the official docs are quiet on Grok 4.5. xAI's [model page](https://docs.x.ai/developers/models) lists `grok-build-0.1` as a coding model trained specifically for agentic coding workflows, with a 256k context window and $1.00 / $2.00 per 1M input/output tokens in the [xAI pricing docs](https://docs.x.ai/developers/pricing). It lists `grok-4.3` for general usage, with a 1M-token context window and $1.25 / $2.50 per 1M input/output tokens. The [xAI rate-limit page](https://docs.x.ai/developers/rate-limits) includes Grok 4.3 and Grok Build 0.1, and the [xAI function-calling docs](https://docs.x.ai/developers/tools/function-calling) explain the current tool-use surface, but none of those pages list Grok 4.5.

That absence matters. A model can be real internally and still not be usable through the public API. Teams should separate "xAI may be testing this" from "developers can deploy this."

Public discussion is still useful for a narrower purpose: it tells us what builders should test first.

The follow-up questions are more useful than the hype:

- Does Cursor-style data reduce failed patch attempts?
- Does Grok 4.5 navigate repositories better than Grok 4.3 or Grok Build?
- Does it beat Claude Opus 4.8 on real multi-file tasks?
- Does it need fewer retries, fewer tool calls, or less human review?
- Does it remain competitive when latency and output length are measured?
- Does it generalize outside Cursor-like workflows?

Treat X threads as signals, not specs. The specs begin when xAI updates its model docs or release notes.

## Grok 4.5 vs Claude Opus: Expected Performance

The real routing question is not "Is Grok 4.5 exciting?" It is: Should a coding or agent workflow use Grok 4.5 instead of Claude Opus 4.8 once Grok 4.5 becomes available?

Claude Opus 4.8 is the clean baseline because Anthropic has public documentation and benchmark data. Anthropic's [model overview](https://platform.claude.com/docs/en/about-claude/models/overview) lists Claude Opus 4.8 with a 1M-token context window and 128k max output. Anthropic's [Opus 4.8 announcement](https://www.anthropic.com/news/claude-opus-4-8) positions it around complex agentic work, coding, and enterprise use cases, while the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing) gives the official API price baseline.

The Opus 4.8 system card gives actual numbers. In the evaluation summary, Opus 4.8 reports 88.6 on SWE-bench Verified, 69.2 on SWE-bench Pro, 74.6 on Terminal-Bench 2.1, 83.4 on OSWorld-Verified, and 1890 on GDPval-AA.

### Expected Strengths of Grok 4.5:

- **Coding Specialization**: Cursor data provides a unique edge in real-world developer traces that synthetic benchmarks undervalue. Prior Grok models were already competitive on coding; this could push it ahead on agentic tasks.
- **Scale & Speed**: 1.5T parameters + Colossus infrastructure may yield strong throughput and long-context handling.
- **Cost/Accessibility**: xAI models often price competitively; CometAPI further reduces costs (e.g., Grok 4 series at significant savings).

### Claude Opus Strengths (Current Flagship):

- Proven benchmarks: High SWE-Bench (~80%+ in recent versions), strong reasoning (GPQA, ARC-AGI), excellent instruction following and safety.
- Mature ecosystem: Robust tool use, artifacts, and enterprise features.

**Comparison Table (Projected/Reasoned Based on Available Data)**

| Aspect | Grok 4.5 (Expected) | Claude Opus (Current) |
| --- | --- | --- |
| Parameters | 1.5T (V9) | Undisclosed (dense/expert mix) |
| Coding (SWE-Bench est.) | Competitive/Leading (Cursor boost) | ~80%+ Verified |
| General Reasoning (GPQA/MMLU) | Close to/Above Opus | Leading |
| Context Window | Large (projected 200k+) | 200k+ |
| Price (via API) | Competitive (cheaper via CometAPI) | Premium |
| Data Specialization | Cursor IDE traces | Broad + curated |
| Availability | Private beta → soon? | Public API |
| Training Cadence | Monthly scratch models | Iterative |

*Table synthesized from leaks, prior benchmarks, and analyses. Actual results pending public evals.*

Treat the Opus comparison as a benchmark target, not a conclusion. If Grok 4.5 is truly close to or beyond Opus, it should show up in solved-task rate, fewer retries, lower reviewer edits, and better tool-loop recovery. If it only wins demos, it is not enough for production routing.

## Three Engineering Dark Corners

The migration risk is not only model quality. Three less-visible details can make a Grok 4.5 rollout expensive or fragile.

### 1. Cursor-shaped gains may not transfer to your coding stack

If the training signal comes from Cursor workflows, the model may be strongest in Cursor-like editing patterns. Your production system may be different: server-side agents, CI repair bots, GitHub issue triage, internal repo migration, or local developer assistants.

Evaluation checklist:

- Include real repositories, not toy prompts.
- Include tasks that require reading before editing.
- Include failed-test recovery tasks.
- Score final patch correctness, not only answer quality.
- Compare plain chat mode against agent mode.
- Measure whether Grok 4.5 reduces retries compared with Opus 4.8 and Grok 4.3.

### 2. Private beta performance may depend on internal harnesses

A model tested inside SpaceX or Tesla may benefit from internal tools, curated prompts, private evaluation tasks, or specialized retrieval. A public API version might behave differently.

Evaluation checklist:

- Record the exact model ID and release date.
- Record tool availability for every run.
- Separate model quality from harness quality.
- Track p50 and p95 latency.
- Track tool failures and invalid tool calls.
- Avoid comparing an internal-agent demo with a raw API call.

### 3. Pricing and context limits can erase benchmark wins

Even if Grok 4.5 is stronger, it may not be cheaper. Token price, context window, output cap, prompt caching, rate limits, and tool-call cost all matter.

Use this routing metric:

Effective cost per solved task = (primary model cost + retry cost + fallback cost + human review cost) / successful tasks

If Grok 4.5 solves more tasks with fewer retries, it can be worth a higher token price. If it uses more tokens, loops longer, or requires more review, the launch hype will not translate into lower workload cost.

## How To Evaluate Grok 4.5 Yourself

Use the leak window to prepare the eval before the model appears.

### 1. Build a 20-task coding-agent set

Include real tasks:

- bug fix in your own repo
- multi-file refactor
- dependency migration
- failing test repair
- code review with subtle regression
- documentation update tied to code
- UI bug from screenshot plus source
- SQL or data pipeline issue
- tool-calling workflow
- long-context repository question

### 2. Run the same tasks on available baselines

Do not wait for Grok 4.5 to start measuring. Run the same task set on:

- Grok 4.3 for current xAI general reasoning
- Grok Build 0.1 for the official xAI coding-model baseline where available
- Claude Opus 4.8 for high-capability coding and agentic work
- Claude Sonnet 5 for lower-cost production routing
- your current production model

### 3. Measure solved-task cost

Track:

- input tokens
- output tokens
- tool calls
- retries
- failed patches
- test pass rate
- latency
- reviewer edits
- final pass/fail score
- cost per accepted patch

Do not compare one-off outputs. Compare the same tasks, same instructions, same tools, and same scoring rubric.

### 4. Add Grok 4.5 only after public availability

When xAI or CometAPI exposes a stable Grok 4.5 model ID, add it to the same eval. Do not rewrite the eval around the new model. The whole point is to keep the benchmark stable enough that the comparison means something.

### 5. Decide by workload class

Use the winning model by task type, not by brand:

- Use the cheaper model when task success is similar.
- Use Opus 4.8 when failures are expensive and Grok 4.5 has not proven parity.
- Use Grok 4.5 only where it beats current baselines on your own tasks.
- Keep a fallback route until error rates, latency, and cost are stable.

## What We Know vs. What We Can't Yet Verify

**Confirmed / Strongly Signaled**:

- 1.5T V9 foundation + Cursor supplemental training.
- Private beta at SpaceX/Tesla (June 28, 2026).
- Musk-attributed “close to/beyond Opus” claim.
- Monthly new model roadmap.
- UI canary traces.

**Unverified / Open Questions**:

- Exact benchmarks (no system card).
- Public release date and API pricing.
- Full context window, multimodal capabilities.
- Precise Cursor data volume, license, and mixing ratio.
- Performance vs. specific Opus version or other frontiers (e.g., GPT-5.5, Gemini 3.x).
- Grok 4.5 vs. rumored larger Grok 5 variants.

Treat claims as vendor-directional. History shows internal evals can differ from public ones; independent verification is essential

## What To Watch Next

Watch five things over the next few weeks:

1. xAI model docs adding a Grok 4.5 model ID.
2. xAI release notes confirming public or preview availability.
3. Independent coding-agent benchmarks, especially [SWE-bench](https://www.swebench.com/), [Terminal-Bench](https://www.tbench.ai/), and Cursor-style coding-agent tasks.
4. Real developer reports on Cursor-like coding workflows.
5. CometAPI catalog or dashboard updates for Grok 4.5 availability.

The first reliable buying signal will not be a viral X post. It will be a model ID plus repeatable eval results.

## Future Outlook: Monthly Models and Beyond

xAI’s pace — new foundation models monthly — could redefine iteration speed. Grok 4.5 is an incremental leap; Grok 5 variants promise more. Expect continued emphasis on truth-seeking, humor, and real-world utility aligned with Musk’s vision.

**Call to Action**: Sign up for CometAPI today to access powerful Grok models affordably and stay ahead. Watch x.ai and X for official Grok 4.5 updates. The AI coding revolution is accelerating — position your workflows now.

---

*Originally published at [https://www.cometapi.com/grok-4-5-leak-xai-s-1-5t-v9-model-in-private-beta/](https://www.cometapi.com/grok-4-5-leak-xai-s-1-5t-v9-model-in-private-beta/).*
