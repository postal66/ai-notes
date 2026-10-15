<!-- social-ops-fingerprint:acb9300dd2183157bb8c17b867edf596df225c4c289109088d104f5de32eaa40 -->
---
title: Gemini 4 Pro Is Coming: Everything We Know From test, leaks & RSI Rumors
---
# Gemini 4 Pro Is Coming: Everything We Know From test, leaks & RSI Rumors

![Gemini 4 Pro Is Coming: Everything We Know From test, leaks & RSI Rumors](https://resource.cometapi.com/Gemini%204%20Pro.jpg)

**TLDR:** Google has confirmed Gemini 4 as its “most ambitious pre-training run yet.” Community leaks in mid-September 2026 point to an early internal checkpoint of **Gemini 4 Pro** (codenamed “argon”) featuring a reported 256k output token limit, possible multi-million-token context, and high-effort reasoning modes.Unofficial timelines cluster around October 2026 after pre-training delays. RSI (recursive self-improvement) links remain speculative. Until official release, developers can access current frontier models—including [GPT-6 Astra](https://www.cometapi.com/en/models/openai/gpt-6-astra), [Gemini 3.8 Flash](https://www.cometapi.com/en/models/google/gemini-3-8-flash), and [Claude Fable 5.1](https://www.cometapi.com/en/models/anthropic/claude-fable-5-1)—through unified, discounted APIs such as [CometAPI](https://www.cometapi.com/).

## Key Takeaways

- **Gemini 4 is real and in training.** Google said in July 2026 that it had started its "most ambitious pre-training run yet" for Gemini 4.
- **Gemini 4 Pro has not been officially announced.** The name, model ID, pricing, API availability, context window, and final specifications remain unconfirmed. [Leaked screenshots and community reports](https://x.com/Lentils80/status/2099601296516960580) describe a Gemini 4 Pro checkpoint with a 256k output token limit (vs. prior ~64k), high-effort compute, and possible 1.5M+ context ambitions.
- [Gemini 4.0 appears to have quietly surfaced on Arena.ai](https://x.com/TimJayas/status/2100490854272225445) (apparently, Gemini 3.8 Flash is being routed to the new Gemini Pro within Arena)
- Most credible unofficial targets now point to an October 2026 public rollout after pre-training refinements.
- Claims of strong RSI for Gemini 4 remain unverified; related research (Dream-RSI) improves exploration strategies without weight updates.
- Until Gemini 4 Pro is officially released, developers can already experiment with current frontier models through platforms such as CometAPI, including Gemini 3.8 Flash, GPT-6 Astra, and Claude Fable 5.1.

## What Is Gemini 4 Pro?

Gemini 4 Pro is the rumored flagship “Pro”-tier model in Google DeepMind’s next major Gemini generation. It sits above the lighter Flash variants and is positioned for high-complexity work: advanced coding, multi-step reasoning, long-horizon agentic tasks, multimodal understanding, and enterprise-scale document or codebase analysis.

Unlike the iterative 3.x Flash releases that have continued through 2026, Gemini 4 is described by Google leadership as requiring substantially larger base models to remain competitive at the frontier. [Sundar Pichai stated on the Alphabet Q2 2026](https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf) earnings call: “For the next generation of frontier, you’re going to need much larger base models. We are now training Gemini 4, and we’re being very ambitious with it.”

The “Pro” designation historically signals the highest-capability publicly available tier optimized for quality over pure speed or cost—similar to earlier Gemini Pro and 2.5 Pro models that led coding and reasoning leaderboards for extended periods.

## What We Know About Gemini 4 Pro(As of September 17)

### Confirmed Official Signals

Google publicly acknowledged Gemini 4 in July 2026. In the launch post for Gemini 3.6 Flash (and related Flash variants), the team stated they had “already started our most ambitious pre-training run yet, for Gemini 4.” [Alphabet CEO Sundar Pichai reinforced this on the Q2 earnings call](https://9to5google.com/2026/07/26/google-gemini-4-teases/), describing Gemini 4 as requiring “much larger base models” to stay at the frontier, with explicit emphasis on coding and autonomous agents. He expressed internal excitement about progress and confidence that the results would please external users when released.

No official model card, parameter count, context window, benchmarks, pricing, or API endpoint for Gemini 4 or Gemini 4 Pro has been published. The Flash series (including the September 2026 Gemini 3.8 Flash and 3.8 Live variants) continues to receive frequent updates while the larger Pro-tier work proceeds.

### Leaked Checkpoint and Specs

[Community reporting](https://nokiapoweruser.com/google-gemini-4-pro-first-leaked-image-specs/#google_vignette) indicates Google has produced an early internal checkpoint of the upcoming Pro model. [one zero-shot peacock svg demo](https://x.com/letdarky) is making the rounds. previous checkpoint was Argon 160 / Gemini 3.8 Flash on arena.Reported details include:

- A 256k-token output limit (a large increase over the ~64k of prior Gemini models).
- Generation under a “High” thinking-effort setting that took approximately 2.4 minutes.
- Association with the Gemini 4 Pro tier rather than another Flash iteration.

### Capital Expenditure and the RSI Connection

In early August 2026, Google DeepMind executive [Jasjeet Sekhon (chief strategy officer) publicly described](https://seekingalpha.com/news/4623658-google-exec-says-heavy-ai-capex-spending-is-a-precursor-to-rsi) the industry’s massive capital expenditures on AI as a bet on recursive self-improvement (RSI)—systems that can improve themselves or the processes that produce the next generation of models. He noted that current revenues do not yet justify the scale of spending and that RSI is becoming a central part of the investment thesis, while acknowledging it has not yet been achieved.

Separately, Google researchers published the [Dream-RSI paper in mid-September 2026](https://cellcog.ai/blog/dream-rsi-recursive-self-improvement/), demonstrating recursive improvement of an agent’s exploration strategies (without updating model weights) using Gemini 3.x models. This is related research but not evidence that Gemini 4 itself incorporates strong weight-space RSI.
The RSI framing underscores the strategic scale of the Gemini 4 effort: Google is investing at a level consistent with a generational leap rather than an incremental upgrade.

### Arena.ai / LM Arena Mentions and Routing Claims

Arena.ai (the crowdsourced human-preference platform formerly known as LMSYS Chatbot Arena / LMArena) is a frequent early-testing venue for Google models. New anonymous or labeled Gemini entries often appear there before official announcements, and the community treats them as signals of near-term releases.

Gemini 4.0 has “quietly surfaced” and that traffic labeled as Gemini 3.8 Flash is sometimes being routed to a new Gemini Pro checkpoint inside Arena battles.:

- [http://Arena.ai](https://t.co/y8UaaBI8Lm) Suddenly Launched a New Variant "gemini-3.8-flash" This Morning on September 17
- Official 3.8 Flash Was Released on September 2, Reappearance of the Same Name Is Extremely Unusual.

![Gemini 4 Pro Is Coming: Everything We Know From test, leaks & RSI Rumors](https://resource.cometapi.com/blog/uploads/2026/09/Gemini%203.5%20pro%20is%20Come%20soon.jpg)

### What remains unconfirmed

As of September 17, 2026, there is no authoritative Google announcement confirming:

| Gemini 4 Pro attribute | Current status |
| --- | --- |
| Gemini 4 training | Confirmed |
| Gemini 4 Pro name | Unconfirmed |
| First Pro checkpoint | Leak/rumor |
| October release | Leak/estimate |
| November–December release | External estimate |
| 1.5M context | Unverified leak |
| 10M context | Unverified claim |
| Specific benchmark scores | Unverified |
| GPT-6 Astra comparison | Unverified |
| Claude Fable 5.1 comparison | Unverified |
| RSI achievement | Unverified |
| API model ID | Not announced |
| Official pricing | Not announced |

## The Relationship Between Gemini 4 Pro and RSI

Recursive self-improvement (RSI)—systems that can meaningfully improve their own capabilities or the processes that produce the next generation—has become a frequent topic of speculation around every major frontier training run.

- The claim that "Google has achieved RSI, making its new model more powerful" originates [from posts on X](https://x.com/Mr_Salio/status/2098743835681513612), but it has not yet been confirmed by testing or official reports.
- Separately, Google researchers (with collaborators) published Dream-RSI in September 2026. The system allows an agent to recursively improve its own *exploration and search strategies* by “dreaming” alternative policies and retaining the best, without ever updating the underlying model weights. Experiments used Gemini 3.1 Pro and Gemini 3.7 Flash. This is meta-level improvement of the orchestration layer, not full weight-space RSI that would automatically produce a stronger Gemini 4 from Gemini 3.
- Broader 2026 research (AIDE², various agent-loop papers, and economic analyses) shows bounded or component-level self-improvement—better prompts, skills, memory retrieval, or evaluation harnesses—but not full closed-loop weight-level RSI that produces successively stronger base models without human intervention.

In short: Google is clearly investing in self-improving agent systems, and the Gemini 4 training run is described as unusually ambitious. Strong claims that the model itself embodies solved RSI remain unproven and should be treated as rumor.

## What Features are confirmed or expected for Gemini 4 Pro?

Building on the trajectory from Gemini 1.5 → 2.5 → 3.x and the leaked argon details, the following areas are the most plausible sites of meaningful progress. Each is framed as an H3-level expectation grounded in either leak data or reasonable extrapolation from prior generations.

### Dramatically Expanded Output Capacity

The leaked 256k output token limit would allow generation of entire multi-file codebases, long research reports, or complex structured documents in a single pass. Prior Gemini models were more constrained on output length, often requiring iterative continuation. This change alone would simplify agentic coding pipelines.

### Longer Context Windows and Better Retrieval

Reports of a possible 1.5M–2M token context (still undecided) would extend Google’s traditional strength in long-context handling. Combined with improved retrieval and reduced “lost-in-the-middle” effects, this would benefit legal, scientific, and large-codebase analysis.

### Stronger Coding and Agentic Performance

Pichai explicitly called out coding and agentic coding as focus areas. Gemini 2.5 and 3.x already delivered large jumps on SWE-bench, LiveCodeBench, and WebDev Arena. Gemini 4 Pro is expected to push further on multi-file refactoring, autonomous bug fixing, tool-use reliability, and long-horizon planning.

### Deeper Reasoning / Adaptive Compute

The “High thinking effort” mode that consumed 2.4 minutes on the argon checkpoint suggests continued investment in inference-time compute scaling (similar to Deep Think or extended thinking modes in the 3.x series). Expect more reliable multi-step logic, lower hallucination rates on hard problems, and configurable effort levels.

### Multimodal and Native Tool Improvements

Gemini has long been natively multimodal. Further gains in video understanding, real-time visual reasoning, and seamless tool calling (background tools without breaking conversation flow) are consistent with the direction of 3.8 Live and related releases.

### Efficiency and Serving Optimizations

Even with larger base models, Google typically pairs frontier Pro models with efficient Flash variants and speculative decoding. Expect continued progress on tokens-per-second and cost-per-quality.

## What assistance can CometAPI provide while waiting?

Until Gemini 4 Pro ships, developers can already access current state-of-the-art models through CometAPI’s unified, OpenAI-compatible endpoint. Notable options include:

- **GPT-6 Astra** – OpenAI’s flagship for complex reasoning, coding, computer use, and long-horizon agentic work (1,050,000-token context, up to 128k output). Available on CometAPI at a permanent discount versus list pricing.
  Model page: <https://www.cometapi.com/models/openai/gpt-6-astra/>
  Usage guide: <https://www.cometapi.com/how-to-use-gpt-6-astra-api/>
- Latest Gemini 3.x Flash and Pro-class models (including 3.8 variants) for multimodal and agentic workloads.
- Seamless switching between providers with a single API key and OpenAI SDK compatibility.
- Gemini CLI integration documentation for local agentic coding workflows.

CometAPI’s catalog also surfaces emerging models quickly, so Gemini 4 Pro (once released) can be expected to appear alongside the existing lineup under the same endpoint.

## How Gemini 4 Pro Compares (Projected vs. Current Frontier)

| Capability | Gemini 3.x / 2.5 Pro (Public) | GPT-6 Astra (Public) | Gemini 4 Pro (Leaked / Expected) |
| --- | --- | --- | --- |
| Context window | Up to ~1–2M tokens | 1,050,000 tokens | Rumored 1.5M–2M |
| Max output tokens | ~64k | 128,000 | Leaked 256k |
| Reasoning / thinking modes | Deep Think / Extended | low → max effort levels | High-effort (2.4 min observed) |
| Coding / agentic focus | Strong (SWE-bench gains) | Flagship strength | Explicit priority + leak claims |
| Multimodality | Native (text/image/video/audio) | Text + image input | Expected continuation + improvement |
| Status | Production | Production (Sep 2026) | Internal checkpoint, not released |

Table notes: Gemini 4 Pro figures are drawn from the argon leak and community reports; they are not official Google specifications. GPT-6 Astra specs are from public documentation.

## Conclusion

Gemini 4 Pro represents Google’s stated next step at the frontier: a larger-scale pre-training effort explicitly aimed at keeping pace with—and ideally surpassing—contemporaneous models from OpenAI, Anthropic, and others. The September 2026 argon checkpoint provides the first concrete (if still unofficial) glimpse of expanded output capacity and high-effort reasoning. Release timing appears to be tightening around October 2026, though post-training and evaluation remain variables.

RSI remains an active research direction rather than a confirmed feature of the model. In the meantime, the practical path for developers is clear: continue shipping with the strongest available systems—GPT-6 Astra, current Gemini 3.x models, and peers—while monitoring official Google channels for the Gemini 4 announcement. Platforms such as CometAPI already aggregate these models under one key and one billing relationship, reducing friction both today and when Gemini 4 Pro eventually arrives.

---

*Originally published at [https://www.cometapi.com/gemini-4-pro-is-coming/](https://www.cometapi.com/gemini-4-pro-is-coming/).*
