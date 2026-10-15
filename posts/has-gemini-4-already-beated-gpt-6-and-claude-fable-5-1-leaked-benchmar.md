<!-- social-ops-fingerprint:e7e6622ff468c4fbb0801446bc2e13b31f218e4ba257f907d45e0162c2a0f71d -->
---
title: Has Gemini 4 already beated GPT-6  and Claude Fable 5.1? Leaked benchmarks explained
---
# Has Gemini 4 already beated GPT-6  and Claude Fable 5.1? Leaked benchmarks explained

![Has Gemini 4 already beated GPT-6  and Claude Fable 5.1? Leaked benchmarks explained](https://resource.cometapi.com/Gemini%204-2.jpg)

**TLDR** Leaked benchmarks and Arena.ai stealth tests in mid-September 2026 position Google’s unreleased Gemini 4 Pro as the new frontier leader, topping GPT-6 Astra and Claude Fable 5.1 across software engineering, agentic tasks, knowledge work, reasoning, and multimodal benchmarks.

## Key Takeaways

- [Gemini 4 Pro](https://www.cometapi.com/en/models/google/gemini-4) leads leaked evaluations on DeepSWE v1.1 (88.7%), GDPval-AA v2 (2064 Elo), Terminal-bench 2.1 (95.3%), OSWorld-2.0 (86.8%), and multiple other agentic/reasoning suites.
- It undercuts GPT-6 Astra ($12/$60) and Claude Fable 5.1 ($10/$50) on list pricing while matching or exceeding their 1M-class context windows.
- Stealth testing on Arena.ai under placeholder names (e.g., gemini-3.8-flash) has produced standout SVG, Three.js, and agentic coding demos.
- RSI (recursive self-improvement) rumors circulate but lack public evidence of closed-loop autonomous model improvement for Gemini 4 itself.
- Google has confirmed heavy investment in a larger Gemini 4 base model; public launch timing remains unofficial.
- Platforms such as CometAPI already aggregate Gemini, [GPT-6 Astra](https://www.cometapi.com/en/models/anthropic/claude-fable-5-1), Claude Fable/Opus, and hundreds of other models behind one OpenAI-compatible endpoint at competitive rates—ideal for benchmarking the new frontier once it ships.

## What Do We Know About Gemini 4 ? (Leaks, Sources, and Verified Context)

As of September 20, 2026, Gemini 4 Pro has not received an official Google announcement, model card, or public API endpoint. Everything beyond Google’s earlier statements about investing in a “larger Gemini 4 base model” (July 2026 earnings) comes from community leaks, Arena.ai blind tests, and circulating benchmark tables.

Key sources and claims include:

- Leaker Pankaj Kumar and subsequent posts (around early-to-mid September) referenced an internal Pro checkpoint with an expected October public release and a possible Flash-Lite variant earlier.
- Multiple developers reported pulling a high-capability model labeled “gemini-3.8-flash” (or similar placeholders) on Arena.ai. Outputs included complex SVG generation (e.g., pelican on a bicycle, mechanical butterflies in Three.js), long non-repetitive JSON generation, and strong agentic behavior. Some users claimed backend details such as multi-million-token context, 256k output ceilings, cross-session memory, and native tool/internet capabilities.
- A widely shared comparison table lists Gemini 4 Pro against Gemini 4 Flash, Gemini 4 Flash-Lite, GPT-6 Astra, Claude Fable 5.1, Claude Opus 5, and GPT-5.6 Sol.
- Google has not confirmed the Arena tests or the table. Historical pattern shows the company often runs stealth evaluations on public platforms weeks before formal launches.

![Has Gemini 4 already beated GPT-6  and Claude Fable 5.1? Leaked benchmarks explained](https://resource.cometapi.com/blog/uploads/2026/09/Gemini-4%20pro%20.jpg)

### Context window

The leaked table shows 2M max input tokens for the Gemini 4 family—double the 1M of GPT-6 Astra and far above the 200k of the Claude Fable/Opus 5 line (some Claude variants have offered larger effective windows via other mechanisms). Separate ghost-routing claims floated 10M ceilings; these remain unverified.

## Price of Gemini 4 (Leaked Figures)

The circulating table lists:

- Gemini 4 Pro: $2.25 input / $11.25 output per 1M tokens (no caching).
- Gemini 4 Flash: $0.75 / $3.75.
- Gemini 4 Flash-Lite: $0.35 / $1.75.

These figures are substantially lower than GPT-6 Astra’s reported $12/$60 and Claude Fable 5.1’s $10/$50 list rates (Fable 5.1 offers aggressive cache-read discounts that can lower effective cost for agentic workloads). Current official Gemini 3.x Pro pricing sits in the $2–$4 input / $12–$18 output range depending on context length, so the leaked Pro numbers are plausible as a next-generation adjustment.

Actual public pricing will only be known at launch. Google has historically used competitive token rates and free tiers to drive adoption.

## Performance of Gemini 4 Pro: Leaked Benchmark Deep Dive

The circulating table places Gemini 4 Pro at the top of nearly every category. These numbers are **unofficial and unverified** by Google or independent third-party labs at the time of writing. They should be treated as directional signals rather than definitive rankings.

### Software engineering & agentic coding

- DeepSWE v1.1 (long-horizon software engineering): 88.7% (vs. GPT-6 Astra 86.9%, Claude Fable 5.1 69.1%, Claude Opus 5 75.0%).
- Terminal-bench 2.1 (agentic terminal coding): 95.3% (vs. Astra 94.1%, Fable 92.8%).
- Terminal-bench 4.0 (general agent capabilities): 69.7% (largest relative gap over Flash and competitors).

### Knowledge work & professional tasks

- GDPval-AA v2 (Elo, knowledge work): 2064 (only model above 2000; Astra 1994, Fable 1853).
- Vals Finance Agent v2: 74.2%.
- Harvey’s Legal Agent Benchmark (complex legal workflows, all-pass rate): 18.7%.

### Reasoning, multimodal & specialized

- CharXiv Reasoning (information synthesis from complex charts, no tools): 94.7%.
- LVBench (long video understanding): 95.8% agentic / 95.0% static.
- HLE-Verified (multidisciplinary expert reasoning): 72.1%.
- OSWorld-2.0 (agentic computer use, partial score, batch tool enabled): 86.8%.
- BioMysteryBench & LABBench2 (bioinformatics and biology research workflows): leading scores on both human-solvable and difficult subsets.

These results, if directionally accurate, show particular strength on long-horizon, multi-step, tool-using agentic workloads—the exact area where GPT-6 Astra and Claude Fable 5.1 were positioned as leaders after their early-September releases.

Arena qualitative tests reinforce the picture: complex SVG and Three.js generations from the stealth model have been judged superior or highly competitive against Astra in community side-by-side comparisons.

## How will Gemini 4 work?

**Gemini 4 (Pro) is not yet released**, so any description of “how it will work” is necessarily based on Google’s official statements, the limited leaked details about an early internal checkpoint, the trajectory of the Gemini 3.x series, and reasonable engineering inferences. Nothing below should be treated as confirmed specifications.

### Core Training and Scale Approach

Google has described Gemini 4 as its “most ambitious pre-training run yet,” built on a **significantly larger base model** than previous generations. The explicit goal is to remain competitive at the frontier, especially in coding and autonomous agents.

This implies:

- A larger parameter count or more effective capacity (via mixture-of-experts, better sparsity, or denser scaling).
- Heavier compute investment during pre-training.
- Continued emphasis on multimodal training data (text, image, video, audio, code, tool-use trajectories).

The model is expected to serve as a new high-capability baseline from which faster Flash-style variants can later be derived.

### Inference and Reasoning Style

Leaked descriptions of an early “argon” checkpoint mention a **High thinking-effort** mode that took roughly 2.4 minutes for a single generation and supported a dramatically higher output limit (reported at 256k tokens versus prior ~64k).

This points to:

- Optional compute-intensive reasoning paths (similar in spirit to extended-thinking or “max effort” modes in competing models).
- The ability to spend more internal computation on hard problems before producing an answer.
- Better support for long, coherent outputs such as complete codebases, multi-step plans, or lengthy reports.

Users will likely be able to control the trade-off between speed/cost and depth of reasoning, just as they can with current Gemini Flash models that offer low / medium / high thinking levels.

### Key Capability Focus Areas

Based on Sundar Pichai’s public remarks and the development trajectory:

1. **Coding and software engineering** Stronger long-horizon performance: multi-file refactors, debugging across repositories, self-correction loops, and higher completion rates on realistic software tasks.
2. **Autonomous / agentic behavior** Improved ability to plan, use tools, observe intermediate results, recover from errors, and continue toward a goal over many steps. This builds directly on the computer-use and agentic features already present in Gemini 3.5/3.8 Flash.
3. **Long-context reliability** Community reports mention targets in the 1.5-million-token range (or higher). The practical goal is not just larger windows but better retrieval fidelity and less degradation when working with very long documents, codebases, or multi-hour agent traces.
4. **Multimodal understanding and generation** Native handling of text + image + video + audio, with expected gains in spatial reasoning, video comprehension, and real-time voice/agent interactions (building on the September 2026 Gemini 3.8 Live models).
5. **Tool use and structured outputs** More robust function calling, code execution, search grounding, and structured JSON/XML-style outputs for reliable integration into applications and agents.

### How It Differs from Gemini 3.x

- **Scale**: Explicitly larger base model rather than incremental refinement.
- **Output capacity**: Leaked higher token limits enable longer single-pass generations.
- **Reasoning depth**: More pronounced high-effort modes for difficult problems.
- **Agentic focus**: Greater emphasis on sustained, multi-step autonomous work rather than single-turn or short-horizon tasks.
- **Positioning**: Intended as the new frontier Pro-tier model, while the Flash line continues rapid iteration for speed and cost efficiency.

### Relationship to Recursive Self-Improvement (RSI)

Google executives have publicly linked the company’s large AI capital expenditure to the longer-term goal of recursive self-improvement—systems that can meaningfully improve themselves or the processes that produce the next generation. Related research (such as the Dream-RSI paper) shows agents improving their own exploration strategies without changing model weights.

## Will Gemini 4 Pro outperform GPT-6 and Claude Fable 5.1?

| Category | Gemini 4 Pro | GPT-6 Astra | Claude Fable 5.1 | Notes |
| --- | --- | --- | --- | --- |
| Input / Output price | $2.25 / $11.25 | $12.00 / $60.00 | $10.00 / $50.00 | Gemini 4 Pro ~5× cheaper than Astra |
| Context window | 2M | 1M | 200k | Significant advantage for Gemini |
| DeepSWE v1.1 | 88.7% | 86.9% | 69.1% | Strong coding lead |
| GDPval-AA v2 (Elo) | 2064 | 1994 | 1853 | Knowledge work leader |
| Terminal-bench 4.0 | 69.7% | 66.4% | 57.9% | General agent capabilities |
| OSWorld-2.0 | 86.8% | 84.5% | 77.9% | Computer use |
| HLE-Verified | 72.1% | 67.3% | 62.1% | Expert reasoning |
| LVBench (video) | 95.8% / 95.0% | 93.8% | 90.4% | Multimodal strength |
| Bio / LAB research | Highest scores | Strong | Competitive | Scientific workflows |

Gemini 4 Pro tops **every major row** in the table, often by a meaningful margin, while its claimed pricing is far more aggressive than either GPT-6 Astra or [Claude Fable 5.1](https://www.cometapi.com/en/models/anthropic/claude-fable-5-1).

### Important Caveats

- **This table is not an official Google release.** As of September 20, 2026, Google has still not published a model card, API endpoint, pricing, or confirmed benchmarks for Gemini 4 Pro. The numbers originate from community sources / Arena sightings / internal checkpoint leaks (codename “argon” related).
- Some earlier circulating sheets were later flagged as predicted or partially copied. Treat every specific percentage and the pricing as **unverified** until Google confirms them.
- Claude Fable 5.1’s context window is listed here as 200k, which is lower than the 1M figure commonly reported in official Anthropic documentation. This may reflect a specific evaluation setting or an error in the leaked sheet.
- GPT-6 Astra and Claude Fable 5.1 remain the only fully public, independently evaluated frontier models right now. Artificial Analysis and other third-party trackers still show them as closely matched overall (with different strengths).

### Current Practical Reality (September 20, 2026)

| Model | Status | Best For | Price Level |
| --- | --- | --- | --- |
| Gemini 4 Pro | Unreleased (claimed strong) | Long-context, coding, agents, multimodality, cost | Very aggressive (claimed) |
| GPT-6 Astra | Released | Math, computer use, terminal, automation, cyber | Premium |
| Claude Fable 5.1 | Released | Long-horizon agents, reasoning, coding quality, cache efficiency | Premium |
| Gemini 4 Flash / Flash-Lite | Claimed siblings | Speed + cost-sensitive workloads | Extremely low |

### Quick Takeaways

- **Dominant across the board**: Gemini 4 Pro ranks #1 in every category listed, often by a clear margin.
- **Particular strengths**: Long-horizon coding/agents (DeepSWE, Terminal-bench), knowledge work, multimodal (video + charts), and specialized domains (finance, legal, biology, computer use).
- **Price positioning**: Roughly 1/5 the price of GPT-6 Astra and Claude Fable 5.1 on both input and output, while delivering higher scores.

Astra emphasizes computer use, cybersecurity thresholds, and scientific discovery; Fable 5.1 emphasizes long-running knowledge work and coding with refined safeguards and lower cache-read costs. Gemini 4 Pro’s leaked profile appears strongest on broad agentic software engineering and multimodal reasoning.

## How Developers Can Prepare: CometAPI Recommendations

While waiting for official Gemini 4 Pro access, teams benefit from a unified gateway that already supports the current frontier (Gemini 3.x series, GPT-6 Astra, Claude Fable 5.1 / Opus 5, and 500+ other models). [CometAPI](https://www.cometapi.com/) provides exactly that: a single OpenAI-compatible endpoint, one API key, pay-as-you-go billing typically 20–40% below direct vendor rates, and the ability to switch models with a single parameter change.

Practical workflow:

1. Prototype agentic pipelines on current Gemini Flash/Pro, GPT-6 Astra, and Claude Fable 5.1 via CometAPI.
2. Benchmark the same prompts across models to establish baselines.
3. When Gemini 4 Pro (and its Flash variants) appear in the CometAPI catalog—historically the platform adds new Google models rapidly—swap the model ID and re-run evaluations with minimal code changes.
4. Use the cost dashboard to track token spend across providers and route high-volume or latency-sensitive traffic to the most economical capable model.

This approach eliminates multi-key management, reduces vendor lock-in risk, and positions teams to adopt Gemini 4 Pro on day one of public availability.

Gemini 4 Pro, if the leaks prove directionally correct, represents Google’s strongest bid yet to reclaim the frontier on agentic software engineering and long-context multimodal reasoning. The combination of claimed performance, large context, and aggressive pricing would make it a default consideration for many production workloads. Until the official launch and independent evals arrive, the prudent path is continuous benchmarking across the existing frontier models—easily done through platforms that already unify access. Stay tuned for the formal announcement; the next few weeks are likely to clarify how much of the hype translates into production reality.

## FAQs

### Is Gemini 4 Pro released?

No. As of the latest catalog and Google statements (mid-to-late September 2026), it has not been publicly released or listed with an official model ID.

### When is the expected release date of Gemini 4 Pro?

Leakers point to October 2026 (with some late-September speculation). Google has given no official date. Treat it as a window pending confirmation via API catalog or blog post.

### Did Google achieve RSI with Gemini 4 Pro?

Public evidence shows advanced use of agentic loops for model refinement and research into strategy-level recursive improvement (e.g., Dream-RSI). Claims of full RSI producing the model are not supported by independent verification.

### How does it compare to GPT-6 Astra and Claude Fable 5.1 on benchmarks?

Leaked community charts claim leads on several agent/coding suites. Official independent scores for a released Gemini 4 Pro do not yet exist. Current public data favors evaluating the live models (Astra and Fable 5.1) on your tasks.

### Should I wait for Gemini 4 Pro before building?

No. Ship with today’s strongest available models (accessible via CometAPI or direct APIs), keep evaluation sets ready, and adopt the new model if and when independent and internal tests justify the switch.

### Where can I access current frontier models easily?

Unified providers such as CometAPI offer OpenAI-compatible access to GPT-6 Astra-class, Claude Fable 5.1, current Gemini models, and others with simplified billing and switching. Check the live model list and documentation for the latest IDs and pricing.

---

*Originally published at [https://www.cometapi.com/has-gemini-4-already-beated-gpt-6-and-claude-fable-5-1/](https://www.cometapi.com/has-gemini-4-already-beated-gpt-6-and-claude-fable-5-1/).*
