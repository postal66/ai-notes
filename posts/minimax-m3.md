<!-- social-ops-fingerprint:b5f300f46aeb74375f6104c0fdc99b6cb4a8aab8fe06365f77f2cbb6658fd1b3 -->
---
title: （20260903）MiniMax M3
---
# （20260903）MiniMax M3

## Product name

MiniMax M3 API on CometAPI

## Tagline

Build multimodal agents with up to 1M\-token context

## Short description

Access MiniMax M3 through CometAPI for coding, tool use, long\-context reasoning, and text, image, or video understanding through one API\.

## Maker post

Hey Product Hunt 👋

We’re the team behind CometAPI\.

Today we’re sharing API access and a developer\-focused guide to **MiniMax M3**, MiniMax’s open\-weight model for coding, agentic workflows, long\-context reasoning, and multimodal understanding\.

To be clear: **MiniMax develops MiniMax M3; CometAPI provides a third\-party API access and comparison layer\.**

### What MiniMax released

MiniMax officially released M3 on June 1, 2026\.

According to MiniMax’s announcement, API documentation, and public repository, M3 provides:

- Approximately 428B total parameters and 23B activated parameters

- Up to a one\-million\-token context window

- Native text, image, and video input

- Text output

- Function tools and configurable reasoning

- Open weights and local\-deployment instructions

- MiniMax Sparse Attention for more efficient long\-context processing

The large context window can accommodate repositories, research collections, tool histories, and long\-running agent sessions\. It does not guarantee perfect retrieval across every part of a one\-million\-token prompt\.

M3’s multimodal capability is for understanding image and video inputs; it should not be described as an image\- or video\-generation model\.

### Why we added it

M3 combines several capabilities that developers often have to evaluate separately:

- Repository\-scale coding

- Multi\-step tool use

- Long\-lived agent state

- Screenshot and diagram analysis

- Video understanding

- Open\-weight deployment

A practical workflow might give an agent code, documentation, screenshots, test output, and previous tool results in the same session\.

The important question is not only whether everything fits inside the context window\. It is whether the model can retrieve the right evidence, select valid tools, recover from failures, and continue acting reliably as the session grows\.

### Current CometAPI access

As of September 3, 2026, the current CometAPI implementation uses:

- Model ID: `minimax-m3`

- Endpoint: `POST /v1/chat/completions`

- Inputs: text, image, and video

- Output: text

- Usage\-based token billing

Current CometAPI pricing is divided into two context tiers:

- Up to 524,288 input tokens: **US$0\.24/M input and US$0\.96/M output**

- Long\-context tier: **US$0\.48/M input and US$1\.92/M output**

Pricing, routing, availability, and endpoint behavior can change\. Check the live model page before producing a production cost estimate\.

### What the benchmark results mean

MiniMax’s June 1 launch materials report:

- 59\.0% on SWE\-Bench Pro

- 66\.0% on Terminal\-Bench 2\.1

- 83\.5 on BrowseComp

- 75\.2 on OSWorld\-Verified

These are **vendor\-reported launch results**, not independent CometAPI reruns\.

They suggest that M3 is competitive across coding, browsing, and agent tasks, but they do not establish a permanent ranking or guarantee performance on a particular workload\. Scaffolding, reasoning settings, infrastructure, and evaluation limits can materially affect results\.

### Where system checks still matter

Maximum context capacity is not the same as dependable recall\. Very large requests can also increase latency and cost\.

Production evaluations should account for:

- Missed evidence in distant context

- Incorrect or unnecessary tool calls

- Multimodal interpretation errors

- Invalid structured output

- Failure recovery during long sessions

- Latency and cost as context accumulates

Computer\-use and business workflows should retain permission boundaries, logs, reversible actions, and human approval for consequential steps\.

### How we recommend evaluating M3

Start with 20–50 tasks taken from real work rather than polished demonstrations\.

For coding and agent workflows, test:

1. Repository navigation and multi\-file changes

2. Tool selection and argument correctness

3. Recovery after a tool or command fails

4. Structured\-output compliance

5. Long\-context evidence retrieval

6. Screenshot, chart, and video interpretation

7. Latency, retries, and total token usage

Record the exact model ID, prompt, settings, tool definitions, date, and output\. Compare the same tasks with the model already used in production\.

The most useful measures are task success rate, tool\-call reliability, failure\-recovery rate, and cost per accepted result—not the best score selected from one provider chart\.

### Where CometAPI fits

CometAPI provides one access and billing layer for evaluating MiniMax M3 alongside models from other providers\.

That can reduce integration work for comparative evaluations and fallback routing\. Model\-specific parameters, safety behavior, rate limits, and output formats can still differ, so teams should verify the exact schema before moving production traffic\.

Read the complete [MiniMax M3 guide](https://www.cometapi.com/what-is-minimax-m3/) for its specifications, architecture, benchmark context, current pricing, limitations, and implementation notes\.

What would you test first: repository\-scale coding, long\-context retrieval, multimodal analysis, or multi\-step tool reliability?

## SEO/GEO metadata

**Recommended H1:**
What Is MiniMax M3? Specs, Benchmarks, Pricing and API Access

**Meta title:**
MiniMax M3 API: Specs, Benchmarks \& Pricing \| CometAPI

**Meta description:**
Explore MiniMax M3’s 1M\-token context, 428B MoE architecture, multimodal inputs, vendor\-reported benchmarks, API pricing, model ID, and limitations\.

**Primary keyword:**
`MiniMax M3`

**Secondary keywords:**
`MiniMax M3 API`, `MiniMax M3 pricing`, `MiniMax M3 benchmarks`, `MiniMax M3 model ID`, `MiniMax M3 context window`, `MiniMax Sparse Attention`, `multimodal coding model`, `open-weight AI model`

**GEO entities:**
`MiniMax`, `MiniMax M3`, `CometAPI`, `MiniMax Sparse Attention`, `SWE-Bench Pro`, `Terminal-Bench 2.1`, `BrowseComp`, `OSWorld-Verified`, `long-context AI`, `agentic coding`

<!-- growth-republish-ping -->
