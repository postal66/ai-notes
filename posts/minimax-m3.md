<!-- growth-fingerprint:c4c5f789e461b32b44778ad9f60bce3311de9b37917652cac8ddb7f413afe250 -->
---
title: MiniMax M3 Is Live: 1M Context, 428B MoE, and What the Benchmarks Really Mean
---

# MiniMax M3 Is Live: 1M Context, 428B MoE, and What the Benchmarks Really Mean

*A developer-focused look at MiniMax M3's specifications, CometAPI access and pricing, the vendor-reported benchmark results, and the checks that still matter before you route production traffic to it.*

## TL;DR

[**MiniMax M3**](https://www.cometapi.com/what-is-minimax-m3/) is a released, open-weight model from MiniMax, available through CometAPI today. It is built for coding, agentic workflows, long-context reasoning, and multimodal understanding — not image or video generation.

The headline is the context and architecture: up to a one-million-token context window, roughly 428B total parameters with about 23B activated, MiniMax Sparse Attention for long-context efficiency, and native text, image, and video input. MiniMax reports a 59.0% on SWE-Bench Pro, 66.0% on Terminal-Bench 2.1, 83.5 on BrowseComp, and 75.2 on OSWorld-Verified.

Those scores are **vendor-reported launch results**, not independent CometAPI reruns. They suggest M3 is competitive across coding, browsing, and agent tasks, but they do not establish a permanent ranking or guarantee performance on your specific workload.

A large context window is a capacity, not a recall guarantee. Retrieval quality, tool correctness, multimodal interpretation, and failure recovery are what determine whether a long agent session actually succeeds.

## Key Takeaways

- MiniMax M3 is a released model, not an announcement: it launched on June 1, 2026.
- The model ID on CometAPI is `minimax-m3`, served at `POST /v1/chat/completions` with usage-based token billing.
- It supports native text, image, and video **input** with text output. Do not describe it as an image- or video-generation model.
- CometAPI pricing splits into a standard tier (up to 524,288 input tokens) and a long-context tier. Standard is **$0.24/M input and $0.96/M output**; long-context is **$0.48/M input and $1.92/M output**.
- The benchmark figures are vendor-reported launch numbers, not independent measurements. Scaffolding, reasoning settings, infrastructure, and evaluation limits can materially change results.
- Maximum context is not the same as dependable recall, and very large requests increase latency and cost.

## Status at a Glance

A quick reference for the confirmed, on-record facts before the deeper discussion.

|Dimension|Confirmed detail|
|---|---|
|Release status|Released (June 1, 2026), open weights, local deployment supported|
|Architecture|Sparse mixture-of-experts, ~428B total / ~23B activated parameters|
|Context window|Up to 1,000,000 tokens|
|Inputs|Text, image, video|
|Output|Text|
|Tool use|Function tools with configurable reasoning|
|Long-context mechanism|MiniMax Sparse Attention|
|CometAPI model ID|`minimax-m3`|
|CometAPI endpoint|`POST /v1/chat/completions`|
|Standard tier price|$0.24/M input; $0.96/M output (≤ 524,288 input tokens)|
|Long-context tier price|$0.48/M input; $1.92/M output|
|Billing|Usage-based token billing|

## What MiniMax Released

MiniMax officially released M3 on June 1, 2026. According to MiniMax's announcement, API documentation, and public repository, M3 provides:

- Approximately 428B total parameters and 23B activated parameters
- Up to a one-million-token context window
- Native text, image, and video input
- Text output
- Function tools and configurable reasoning
- Open weights and local-deployment instructions
- MiniMax Sparse Attention for more efficient long-context processing

The large context window can accommodate repositories, research collections, tool histories, and long-running agent sessions. It does not guarantee perfect retrieval across every part of a one-million-token prompt.

M3's multimodal capability is for **understanding** image and video inputs. It should not be described as an image- or video-generation model.

## Why It Was Added to CometAPI

M3 combines several capabilities that developers often have to evaluate separately:

- Repository-scale coding
- Multi-step tool use
- Long-lived agent state
- Screenshot and diagram analysis
- Video understanding
- Open-weight deployment

A practical workflow might give an agent code, documentation, screenshots, test output, and previous tool results in the same session.

The important question is not only whether everything fits inside the context window. It is whether the model can retrieve the right evidence, select valid tools, recover from failures, and continue acting reliably as the session grows.

## Current CometAPI Access

As of September 3, 2026, the current CometAPI implementation uses:

- Model ID: `minimax-m3`
- Endpoint: `POST /v1/chat/completions`
- Inputs: text, image, and video
- Output: text
- Usage-based token billing

Current CometAPI pricing is divided into two context tiers:

- Up to 524,288 input tokens: **US$0.24/M input and US$0.96/M output**
- Long-context tier: **US$0.48/M input and US$1.92/M output**

Pricing, routing, availability, and endpoint behavior can change. Check the live model page before producing a production cost estimate.

## What the Benchmark Results Mean

MiniMax's June 1 launch materials report:

- 59.0% on SWE-Bench Pro
- 66.0% on Terminal-Bench 2.1
- 83.5 on BrowseComp
- 75.2 on OSWorld-Verified

These are **vendor-reported launch results**, not independent CometAPI reruns.

They suggest that M3 is competitive across coding, browsing, and agent tasks, but they do not establish a permanent ranking or guarantee performance on a particular workload. Scaffolding, reasoning settings, infrastructure, and evaluation limits can materially affect results.

## Where System Checks Still Matter

Maximum context capacity is not the same as dependable recall. Very large requests can also increase latency and cost.

Production evaluations should account for:

- Missed evidence in distant context
- Incorrect or unnecessary tool calls
- Multimodal interpretation errors
- Invalid structured output
- Failure recovery during long sessions
- Latency and cost as context accumulates

Computer-use and business workflows should retain permission boundaries, logs, reversible actions, and human approval for consequential steps.

## How We Recommend Evaluating M3

Start with 20–50 tasks taken from real work rather than polished demonstrations.

For coding and agent workflows, test:

1. Repository navigation and multi-file changes
2. Tool selection and argument correctness
3. Recovery after a tool or command fails
4. Structured-output compliance
5. Long-context evidence retrieval
6. Screenshot, chart, and video interpretation
7. Latency, retries, and total token usage

Record the exact model ID, prompt, settings, tool definitions, date, and output. Compare the same tasks with the model already used in production.

The most useful measures are task success rate, tool-call reliability, failure-recovery rate, and cost per accepted result — not the best score selected from one provider chart.

## Where CometAPI Fits

CometAPI provides one access and billing layer for evaluating MiniMax M3 alongside models from other providers.

That can reduce integration work for comparative evaluations and fallback routing. Model-specific parameters, safety behavior, rate limits, and output formats can still differ, so teams should verify the exact schema before moving production traffic.

Read the complete [MiniMax M3 guide](https://www.cometapi.com/what-is-minimax-m3/) for its specifications, architecture, benchmark context, current pricing, limitations, and implementation notes.

## FAQ

### Is MiniMax M3 released?

Yes. MiniMax released M3 on June 1, 2026, and it is available through CometAPI today with the model ID `minimax-m3`.

### Can MiniMax M3 generate images or video?

No. M3 accepts text, image, and video as input for understanding, but it produces text output. It should not be described as an image- or video-generation model.

### What is the MiniMax M3 context window?

Up to one million tokens. That is capacity, not a guarantee of recall across the whole prompt.

### How much does MiniMax M3 cost on CometAPI?

For up to 524,288 input tokens it is US$0.24/M input and US$0.96/M output. The long-context tier is US$0.48/M input and US$1.92/M output. Check the live model page for current pricing.

### Are the M3 benchmark scores independent?

No. The published results are vendor-reported launch numbers from MiniMax. They are useful directional signals, not independent measurements of your workload.

### Can I deploy MiniMax M3 locally?

Yes. MiniMax published open weights and local-deployment instructions.

## Conclusion

MiniMax M3 is a real, usable model rather than a rumor: a 1M-token context window, a 428B-parameter spatial MoE architecture, multimodal input, function tools, and open weights. The CometAPI path makes it easy to benchmark alongside models from other providers through one interface and one billing model.

The discipline is still the same as evaluating any production model. Treat the vendor-reported benchmarks as evidence of competitiveness, not as a guarantee. Measure task success, tool reliability, failure recovery, and cost per accepted result on real work. Verify the exact schema and parameters before moving traffic. A large context window earns its keep only when the model reliably retrieves the right evidence and keeps acting correctly as the session grows.
