<!-- social-ops-fingerprint:06d76b37ba9e44de59da1fa7150c5fc24a4664aea63f3917576d52606d1f06cd -->
---
title: GPT-5 mini API
---
# GPT-5 mini API

![GPT-5 mini API](https://resource.cometapi.com//images/logo.svg)

GPT-5 mini is a **lightweight**, cost-optimized variant of OpenAI’s flagship GPT-5 model, designed to deliver **high-quality** reasoning and multimodal capabilities at reduced latency and expense.

## Basic information & key features

**GPT-5 mini** is OpenAI’s **cost- and latency-optimized** member of the GPT-5 family, intended to deliver much of GPT-5’s multimodal and instruction-following strengths at **substantially lower cost** for large-scale production use. It targets environments where **throughput**, **predictable per-token pricing**, and **fast responses** are the primary constraints while still providing strong general-purpose capabilities.

- **Model Name**: `gpt-5-mini`
- **Context Window**: 400 000 tokens
- **Max Output Tokens**: 128 000
- **Key features:** speed, throughput, cost-efficiency, deterministic outputs for concise prompts

## Technical details — architecture, inference, and controls

**Optimized inference path & deployment.** Practical speedups come from **kernel fusion**, **tensor parallelism tuned for a smaller graph**, and an inference runtime that prefers **shorter internal “thinking” loops** unless the developer requests deeper reasoning. That is why mini achieves noticeably lower compute per call and predictable latency for high-volume traffic. This tradeoff is deliberate: **lower compute per forward pass → lower cost and lower average latency**.

**Developer controls.** GPT-5 mini exposes parameters such as **`verbosity`** (controls detail/length) and **`reasoning_effort`** (trade speed vs. depth), plus robust **tool-calling** support (function calls, parallel tool chains, and structured error handling), which lets production systems tune accuracy vs. cost precisely.

## Benchmark performance — headline numbers and interpretation

GPT-5 mini typically sits **within ~85–95%** of GPT-5 high on general benchmarks while substantially improving latency/price. The platform launch materials indicate **very high absolute scores** for GPT-5 high (AIME ≈ **94.6%** reported for the top variant), with mini somewhat lower but still industry-leading for its price point.

Across a range of standardized and internal benchmarks, **GPT-5 mini** achieves:

- **Intelligence** (AIME ’25): 91.1% (vs. 94.6% for GPT-5 high)
- **Multimodal** (MMMU): 81.6% (vs. 84.2% for GPT-5 high)
- **Coding** (SWE-bench Verified): 71.0% (vs. 74.9% for GPT-5 high)
- **Instruction Following** (Scale MultiChallenge): 62.3% (vs. 69.6%)
- **Function Calling** (τ²-bench telecom): 74.1% (vs. 96.7%)
- **Hallucination Rates** (LongFact-Concepts): 0.7% (lower is better)()

These results demonstrate GPT-5 mini’s **robust** trade-offs between performance, cost, and speed.

## Limitations

**Known limitations:** GPT-5 mini *reduced deep-reasoning capacity vs full GPT-5, higher sensitivity to ambiguous prompts, and remaining risks of hallucination.*

- **Reduced deep reasoning:** For multi-step, long-horizon reasoning tasks the full reasoning model or “thinking” variants outperform mini.
- **Hallucinations & overconfidence:** Mini reduces hallucination relative to very small models but does not eliminate it; outputs should be validated in high-stakes flows (legal, clinical, compliance).
- **Context sensitivity:** Very long, highly interdependent context chains are better served by the full GPT-5 variants with larger context windows or the “thinking” model.
- **Safety & policy limits:** Same safety guardrails and rate/usage limits that apply to other GPT-5 models apply to mini; sensitive tasks require human oversight.

## Recommended use cases (where mini excels)

- **High-volume conversational agents:** low latency, predictable cost. **Keyword:** *throughput*.
- **Document & multimodal summarization:** long-context summarization, image+text reports. **Keyword:** *long context*.
- **Developer tooling at scale:** CI code checks, auto-review, lightweight code generation. **Keyword:** *cost-efficient coding*.
- **Agent orchestration:** tool-calling with parallel chains when deep reasoning is not required. **Keyword:** *tool calling*.

## How to call ****`gpt-5-mini`**** API from CometAPI

### **`gpt-5-mini`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Input Tokens | $0.20 |
| Output Tokens | $1.60 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`gpt-5-mini`“ / “`gpt-5-mini-2025-08-07`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to  [API doc](https://apidoc.cometapi.com/):

- **Core Parameters**: `prompt`, `max_tokens_to_sample`, `temperature`, `stop_sequences`
- **Endpoint:** `https://api.cometapi.com/v1/chat/completions`
- **Model Parameter:** “`gpt-5-mini`“ / “`gpt-5-mini-2025-08-07`“
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY`
- **Content-Type:** `application/json` .

API Call Instructions: gpt-5-chat-latest should be called using the standard `/v1/chat/completions forma`t. For other models (gpt-5, gpt-5-mini, gpt-5-nano, and their dated versions), using `the /v1/responses format` [is recommended](https://apidoc.cometapi.com/). Currently two modes are available.

**See Also [GPT-5](https://www.cometapi.com/gpt-5-api/)** Model

---

*Originally published at [https://www.cometapi.com/gpt-5-mini-api/](https://www.cometapi.com/gpt-5-mini-api/).*
