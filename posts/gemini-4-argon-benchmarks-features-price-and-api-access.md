<!-- social-ops-fingerprint:ee59f00f7c9af4814f4bd4ab751785942e5823c1ff38c0c0e4f8e29a2227ce62 -->
---
title: Gemini 4 Argon: Benchmarks, Features, Price and API Access
---
# Gemini 4 Argon: Benchmarks, Features, Price and API Access

![Gemini 4 Argon: Benchmarks, Features, Price and API Access](https://resource.cometapi.com/What%20is%20Gemini%204%20Argon.jpg)

**TLDR:** On September 30, 2026, Google DeepMind announced Gemini 4 Argon, its new frontier model and the start of the Gemini 4 series. It delivers state-of-the-art performance in long-horizon software engineering (77.9% on DeepSWE v1.1), enterprise knowledge work (leading the Vals Index at 68.9%), and defensive cybersecurity. Key upgrades include an industry-leading 1 million token output limit (up from 64K).

## Key Takeaways

- [Gemini 4 Argon](https://www.cometapi.com/models/google/gemini-4-argon/) is Google’s most capable model yet, optimized for complex, multi-step workflows in coding, legal/finance knowledge work, and cyber defense.
- Argon is designed for sustained reasoning across long, multi-step workflows rather than ordinary short-form chat. Google emphasizes real-world software engineering, legal and finance work, multimodal understanding, and cybersecurity defense.
- Google expanded the maximum output from the previous 64K-token level to 1 million tokens. Google has not yet published a complete public Gemini API specification for Argon's input context, modalities, endpoint behavior, or rate limits.
- On Google's comparison table, Argon scores 68.9% on the Vals Index, 77.9% on DeepSWE v1.1, 91.7% on LVBench, and 68% on CWE-bench v1. It does not lead every test: GPT-6 Astra wins FrontierSWE v2 and Terminal-Bench Science, while Claude Opus 5.5 leads Terminal-Bench 4.0 and PostTrainBench.
- Google's introductory API price is $2 per million input tokens and $10 per million output tokens. After the introductory period, pricing rises to $4 and $20, respectively. Cached input is advertised at 95% below the applicable input-token price.
- CometAPI's public catalog listed `gemini-4-argon` as available, rather than upcoming, on October 1, 2026.

Google has reclaimed a leading position in the frontier AI race with the launch of **Gemini 4 Argon**. Announced on September 30, 2026, this model marks the beginning of the Gemini 4 era and is explicitly positioned as Google’s “next era of frontier intelligence.” It targets the hardest real-world workloads: sustained agentic coding, high-stakes enterprise knowledge work (legal, finance, tax), and defensive cybersecurity.

Unlike previous incremental updates, Argon introduces a fundamental shift in capability depth through dramatically expanded output length and specialized training for long-horizon tasks. Thousands of Google employees are already using it internally for production engineering work, while external access begins narrowly with vetted cybersecurity partners.

## What Is Gemini 4 Argon?

Gemini 4 Argon is Google DeepMind’s latest frontier large language model and the first release in the Gemini 4 family. It is designed specifically to sustain deep reasoning across complex, multi-step, long-horizon workflows that previous models struggled to complete reliably in a single trajectory.

According to Google, Argon “delivers frontier performance in complex workflows across real-world software engineering, enterprise knowledge work like legal and finance, and cybersecurity defense.” It builds on lessons from the delayed or canceled Gemini 3.5 Pro efforts earlier in 2026 and the subsequent focus on the Gemini 3.8 Flash series.

The model emphasizes agentic capabilities—autonomous planning, tool use, code generation and editing, vulnerability discovery and remediation, multi-document analysis, and long-video understanding—while incorporating stronger safety systems for frontier-level power.

Internally, Argon is already [delivering measurable impact at Google scale](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/):

- Quantum computing teams used it to optimize spacetime resources (qubits × gates), beating published baselines by 40% in minutes.
- Agent teams analyzed fleet-wide telemetry and autonomously applied memory optimizations, freeing over 300 TiB of memory across data centers (with estimated total savings of 500 TiB to 1 PiB).
- Large-scale code migrations from C/C++ to Rust are underway, including tens of thousands of lines in core libraries (re2, libgav1) and over 800,000 lines in the Fuchsia Zircon kernel. One notable result: a memory-safe video decoder (libgav1) that runs 2.7× faster than the prior Rust port after profile-guided optimization.

These real-world deployments underscore that Argon is not just a benchmark champion but a practical productivity multiplier for complex engineering organizations.

## Gemini 4 Argon Accessibility as of October 1st

Google is taking a deliberately phased approach to release because of the model’s advanced capabilities. It is currently rolling out to a set of trusted cyber defenders through the Fairwind Program (which has enrolled more than 650 organizations, including major security firms). Google is also participating in the U.S. government’s voluntary pre-release model access process. Broader availability to developers, enterprises, and consumers—starting with paid API customers and Google AI Ultra subscribers—is expected “as soon as possible” after further guardrail iteration based on early feedback.

## Gemini 4 Argon Key Features

### 1. Long-Horizon Reasoning With Up to 1M Output Tokens

Google says Argon's maximum output is 1 million tokens, up from 64,000 tokens in the previous generation. That is a maximum generation limit, not a statement that every response should be enormous. It gives the model room for long reasoning trajectories, multi-file code generation, detailed research, or extended agent work without forcing a new request every few steps.

![Gemini 4 Argon: Benchmarks, Features, Price and API Access](https://pbs.twimg.com/media/HTfdN2Ka4AA3Jdk?format=jpg&name=4096x4096)

### 2. Real-World Software Engineering

Argon's 77.9% score on DeepSWE v1.1 is the highest value in Google's comparison table. DeepSWE focuses on long-horizon software-engineering work, which better matches autonomous coding agents than short code-completion tests. The model also reaches 91.9% on Vibe Code Bench.

The picture is not one-sided. GPT-6 Astra scores 65.5% on FrontierSWE v2 versus Argon's 55.0%, and Claude Opus 5.5 scores 66.4% on Terminal-Bench 4.0 versus Argon's 57.4%. Buyers should therefore test repository editing, shell use, debugging, and migration work separately rather than relying on one "coding" score.

![Gemini 4 Argon: Benchmarks, Features, Price and API Access](https://pbs.twimg.com/media/HTfdNJTbUAAo-l6?format=jpg&name=4096x4096)

### 3. Enterprise Knowledge Work

Google reports Argon at 68.9% on the Vals Index, which weights finance, coding, legal, and tax work by contribution to U.S. GDP. It also leads the compared models on Vals Finance Agent v2, Harvey's Legal Agent Benchmark, and AutomationBench.

These evaluations make Argon especially relevant to research-heavy workflows: due diligence, contract review, financial analysis, tax research, and cross-document synthesis. They do not remove the need for source verification or professional review. A benchmark lead measures performance under a specific harness; it does not establish suitability for unsupervised legal or financial decisions.

### 4. Multimodal and Long-Video Understanding

Argon scores 71.6% on Chartography and 91.7% on LVBench, narrowly leading GPT-6 Astra on chart understanding and more clearly leading on long-video understanding. Google also describes workflows in which Argon interprets a sequence of documents and acts onthe result.

This combination is useful when text alone is insufficient: analyzing earnings charts alongside filings, extracting evidence from hours of video, reviewing product screenshots with written requirements, or reconciling data across PDFs and visual reports.

### 5. Defensive Cybersecurity

Google trained Argon to discover, validate, and patch critical vulnerabilities. On CWE-bench v1, Argon and GPT-6 Astra both score 68%, while Claude Opus 5.5 scores 67%. Google says Argon also outperforms Gemini 3.8 Flash Cyber in internal vulnerability-discovery and black-box penetration-testing evaluations.

Initial access reflects the risk. Trusted cyber defenders can use the model through Google's Fairwind Program, and Google says Wiz used Argon in its Scan for Good initiative to identify a critical vulnerability affecting health-care software. Restricted distribution gives Google time to gather evidence before exposing advanced cyber capability more broadly.

### 6. The hallucination rate dropped to 10%.

Gemini 4 Argon has an insanely low hallucination rate on Artificial Analysis. 15%. Arena reports a **0.10% +/- 0.48% tool-hallucination estimate** for Gemini 4 Argon High, compared with **0.16% +/- 0.09%** for Gemini 3.8 Flash High. The point estimate is lower, which suggests improvement. However, the uncertainty intervals overlap substantially, and Argon's interval is much wider.

![Gemini 4 Argon: Benchmarks, Features, Price and API Access](https://pbs.twimg.com/media/HTfc3V5XgAAwuG8?format=jpg&name=900x900)

## Gemini 4 Argon Benchmark Performance

The following figures come from [Google DeepMind's comparison table.](https://deepmind.google/models/gemini/) Google links a separate methodology document and states that scores are pass@1 unless noted. Treat these as vendor-published results and validate them against private workloads.

| Benchmark | Workload | Gemini 4 Argon | GPT-6 Astra | Claude Opus 5.5 | Leader |
| --- | --- | --- | --- | --- | --- |
| Vals Index | GDP-weighted knowledge work | 68.9% | 63.1% | 67.0% | Argon |
| AutomationBench | End-to-end business automation | 51.3% | 41.4% | 42.5% | Argon |
| Vals Finance Agent v2 | Multi-step finance research | 65.4% | 53.5% | 58.6% | Argon |
| Harvey Legal Agent | Legal research and drafting | 19.6% | 5.4% | 3.8% | Argon |
| DeepSWE v1.1 | Long-horizon software engineering | 77.9% | 74.1% | 74.2% | Argon |
| FrontierSWE v2 | Agentic coding | 55.0% | 65.5% | 62.3% | Astra |
| Terminal-Bench 4.0 | Terminal-based agent work | 57.4% | 58.2% | 66.4% | Opus |
| Terminal-Bench Science 0.1 | Science and math agents | 57.6% | 68.1% | 63.3% | Astra |
| GraphWalks, 256K-1M | Long-context graph traversal, F1 | 84.2% | 71.8% | 66.8% | Argon |
| Agent's Last Exam | Computer use | 39.5% | 34.2% | 38.2% | Argon |
| OSWorld 2.0 offline subset | Computer use, partial score | 69.2% | 72.6% | Not reported | Astra |
| Chartography | Chart understanding | 71.6% | 71.0% | 66.3% | Argon |
| LVBench | Long-video understanding | 91.7% | 87.5% | 83.7% | Argon |
| CWE-bench v1 | Vulnerability remediation | 68.0% | 68.0% | 67.0% | Tie |

### How to Read the Results

Argon's clearest advantage is breadth across professional knowledge work, long context, chart analysis, and long video. Its 19.6% legal-agent result is more than three times Astra's 5.4%, although all three absolute scores show that the benchmark remains difficult. Argon also leads AutomationBench by 8.8 percentage points over Opus 5.5.

Coding requires a more nuanced conclusion. Argon leads DeepSWE and Vibe Code Bench, but Astra leads FrontierSWE, and Opus leads Terminal-Bench 4.0. For science-oriented terminal work, Astra leads Argon by 10.5 points. The correct headline is not "Argon wins every benchmark." It is that Argon is exceptionally strong across long-horizon enterprise workflows while competitors retain important task-specific advantages.

![Gemini 4 Argon: Benchmarks, Features, Price and API Access](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-4-argon_table_blog.gif)

The benchmark evidence is strong but not universal. GPT-6 Astra remains ahead on several science, coding, and computer-use measures, while Claude Opus 5.5 leads important terminal and ML-engineering tests. [Independent evidence is similarly nuanced](https://artificialanalysis.ai/models/gemini-4-argon): Artificial Analysis ranks Argon #8 of 223 models in its comparison class, and Arena ranks Gemini 4 Argon High #8 of 46 agent models while placing it first on steerability. Argon's biggest advantage is the combination of long-horizon reasoning, enterprise-domain performance, and multimodal depth at an aggressive announced price.

## Is Gemini 4 Argon Available?

As of the announcement (September 30, 2026) and subsequent coverage, **no**—not to the general public or standard developers. Access is restricted to:

- Trusted members of the Fairwind Program (cyber defenders, governments, critical infrastructure partners).
- Internal Google teams.
- Participants in the U.S. government’s voluntary pre-release process.

Google states it will expand “as soon as possible” after gathering feedback and iterating on guardrails, beginning with paid API customers and Google AI Ultra subscribers, then broader developer, enterprise, and consumer access. No fixed public date has been given

## Gemini 4 Argon API Pricing

Google's introductory price is $2 per million input tokens and $10 per million output tokens. The post-introductory rate is $4 input and $20 output. Cached input is priced at a 95% discount to the applicable input rate, which implies $0.10 per million during the introductory period and $0.20 afterward if the policy is applied exactly as announced.

The price is attractive relative to other premium frontier models, but cost per token is not cost per completed task. A model that generates hundreds of thousands of output tokens or performs many tool calls can still create a large bill. Set output caps, monitor tool loops, and measure cost per accepted result.

## How to Access Gemini 4 Argon API Through CometAPI

Once Google opens broader API access, platforms that aggregate frontier models become the fastest and often most cost-effective way for developers to experiment and productionize.

**CometAPI** provides a unified, OpenAI-compatible endpoint to 500+ models from OpenAI, Anthropic, Google, and others. This means you can switch between Gemini models, GPT-6 variants, and Claude models by changing only the model parameter—without managing multiple accounts, billing systems, or SDKs.

**Recommended steps to prepare and access via CometAPI:**

1. Sign up at cometapi.com and generate an API key from the dashboard (starts with `sk-`).
2. Use the base URL `https://api.cometapi.com/v1.`
3. Call models with the standard OpenAI SDK or native Gemini format.

CometAPI already supports the Gemini family (including prior Pro and Flash models) with competitive pricing, free trial credits, and seamless switching. Check the CometAPI Models page regularly for Gemini 4 Argon availability. This approach avoids Google Cloud onboarding friction and enables easy A/B testing against Claude Opus 5.5 or GPT-6 Astra in the same codebase.

## Gemini 4 Argon vs GPT-6 Astra vs Claude Opus 5.5

| Category | Gemini 4 Argon | GPT-6 Astra | Claude Opus 5.5 |
| --- | --- | --- | --- |
| Provider | Google | OpenAI | Anthropic |
| Release status on Oct. 1, 2026 | Limited trusted-tester rollout; broader access coming | Active API model | Active latest model; released Sept. 22, 2026 |
| Best fit | Long-horizon knowledge work, multimodal analysis, defensive cyber, large outputs | Complex reasoning, science, computer use, broad tool ecosystem | Long-running agentic coding and knowledge work |
| Input context | Not yet published as a final public API specification | 1,050,000 tokens | 1,000,000 tokens |
| Max output | 1,000,000 tokens | 128,000 tokens | 128,000 synchronous; 300,000 Batch beta |
| Inputs and outputs | Multimodal capabilities stated; detailed public API matrix pending | Text and image in; text out | Text and images in; text out |
| Reasoning control | Long-horizon reasoning; public API controls pending | low through max reasoning effort | Adaptive thinking always on; default effort medium |
| Standard price per 1M tokens | Intro: $2 input / $10 output; later $4 / $20 | $10 input / $50 output | $4 input / $20 output |
| Standout wins in Google's table | Vals, AutomationBench, DeepSWE, long context, LVBench | FrontierSWE, science terminal work, OSWorld subset | Terminal-Bench 4.0, PostTrainBench |
| Main caveat | Broad API availability and full specifications are still rolling out | Highest list price of the three | Does not lead Google's knowledge-work table; adaptive thinking cannot be disabled |

### Which Model Is Best?

Choose Gemini 4 Argon when long-context knowledge work, multimodal evidence, defensive cybersecurity, or unusually large generated artifacts dominate the workload. Choose GPT-6 Astra when you need a mature OpenAI tool surface, strong science-agent performance, or its specific computer-use strengths. Choose Claude Opus 5.5 for Claude-native agentic coding and terminal workflows, especially when its behavior already performs well in your evaluation harness.

For most businesses, the better strategy is not a permanent single-model decision. Route routine requests to a lower-cost model, evaluate Argon, Astra, and Opus on the difficult tail, and preserve a fallback. CometAPI is useful here because one integration layer can make cross-model testing and controlled routing easier.

## Conclusion

Gemini 4 Argon marks Google’s strongest re-entry into the absolute frontier, reclaiming leadership on several enterprise-critical and long-horizon benchmarks while introducing practical advances such as 1M output tokens and aggressive introductory pricing. Its phased, security-first rollout prioritizes responsible deployment of powerful cyber-defense capabilities.

---

*Originally published at [https://www.cometapi.com/what-is-gemini-4-argon/](https://www.cometapi.com/what-is-gemini-4-argon/).*
