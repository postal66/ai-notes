<!-- social-ops-fingerprint:128ee34b371179828eca21312ddfd7a83a98dc8778b2138a47ee5a0a5c97d6e2 -->
---
title: Minimax M2 API
---
# Minimax M2 API

![Minimax M2 API](https://resource.cometapi.com/blog/uploads/2025/10/Minmax-M2-2-1024x523.webp)

**MiniMax M2** is an **open-source, agent-native** large language model (LLM) released by MiniMax on **October 27, 2025**. It is explicitly engineered for **coding** and **agentic workflows** (tool calling, multi-step automation), prioritizing **low latency** and **cost-effective** serving while delivering strong reasoning and tool-use capabilities.

## Key features

**Highlights —** *coding specialization*, *agentic workflows*, *low active-parameter footprint*, *long context support*, *OpenAI-compatible API*. MiniMax positions Minimax M2 as a **fast, deployment-friendly MoE model** intended for multi-step agents, code generation & repair, terminal/IDE workflows, and tool calling.

**Notable bullets (quick):**

- **Architecture:** Mixture-of-Experts (MoE) with a very large total parameter count and a small *activated* parameter set per forward pass.
- **Activation footprint:** ~**10 billion active parameters** (per token).
- **Total parameters (reported):** reported between **~200B – 230B** depending on source/metric (see *Technical details*).
- **Context window:** enterprise-scale long context; **204,800 tokens** max context.
- **Primary modality:** text (tool calling / function calling supported).
- **Agent-native**: designed for multi-step tool calling (shell, browser, python interpreter, MCP tools).
- **Coding focus**: optimized for multi-file edits, run-fix loops and CI/IDE tasks.

## Technical details (architecture & specs)

**Architecture —** *Mixture-of-Experts (MoE)*: Minimax M2 API uses an MoE strategy so the model can have a **very large total parameter count** while only activating a fraction per inference step. This yields improved **compute efficiency**, **throughput**, and **cost per token** for interactive agent and coding loops.

**Precision & quantization —** model files and provider stacks list FP32/BF16 and FP8 formats and multiple quantized builds (safetensors, FP8/E4M3, etc.), enabling local deployment and efficiency trade-offs.

**Context & I/O —** deployed providers publish **204,800 token** context support and large maximum output settings. M2 is **text-only** for now (many open-weights releases from China have emphasized text/agent capabilities while multimodal remains the domain of other releases).

**Runtime recommendations / special instructions —** Minimax M2 API uses an **“interleaved thinking”** output format that wraps the model’s internal reasoning in `<think>...</think>` blocks. MiniMax’ request keeping that thinking content intact and passing it back in historical context to preserve performance for multi-turn agent workflows.

## Benchmark performance

**Composite intelligence & agent benchmarks —** independent benchmarking by Artificial Analysis reports that **MiniMax-M2 achieves a best-in-class Intelligence Index among open-weight models**, and ranks among the **top open-source models** on composite intelligence metrics, especially in **tool use, instruction following, and agentic tasks**. Artificial Analysis highlights the model’s **efficiency** (very few active parameters) as a key driver of its ranking.

![Minimax M2 API](https://resource.cometapi.com/blog/uploads/2025/10/Minmax-M2-2-1024x523.webp)

Minimax M2  shows **strong results on coding & agentic suites** (Terminal-Bench, SWE-Bench, BrowseComp, LiveCodeBench types of tasks), where its architecture and activation budget favor planning → act → verify loops (compilation/run/test cycles, multi-file edits, and tool chains).

![Minimax M2 API](https://resource.cometapi.com/blog/uploads/2025/10/Minmax-M2-1024x424.webp)

## Comparison: MiniMax M2 vs other contemporary models

**Against open-weights peers (DeepSeek, Qwen3, Kimi, etc.) —** Minimax M2  is presented as **particularly efficient** on active-parameter budget (≈10B) giving it strong intelligence-per-active-parameter ratios; other open models may have higher active parameter counts but similar or higher total parameters.

**Against commercial frontier models (OpenAI / Anthropic / Google / xAI) —** reporting places M2 **below the very top commercial models** on some generalist metrics but **competitive or ahead** on many agentic and coding benchmarks for its price point.

**Cost & speed tradeoffs —** Its cost per token is only 8% of Anthropic Claude Sonnet and its speed is about twice as fast.

## Limitations & risks

**Limitations —** *verbosity (high token usage)*, *text-only modality*, *task-specific weaknesses*, and the usual LLM risks (hallucination, overconfidence, dataset biases). Artificial Analysis and MiniMax both point out that M2 may underperform some large generalist models on certain open-ended tasks even while it excels at agentic and coding workflows. Because it is MoE-based, **deployment considerations** (expert routing, quantization, and inference frameworks) matter.

**Operational caveats —** Minimax M2 ’s *interleaved thinking* format requires retaining special `<think>...</think>` tokens across history for best performance; removing that content can degrade agent behavior. Also, because Minimax M2  is verbose, cost per task is a function of both **per-token price** and **total tokens generated**.

## Primary use cases

- **Agent orchestration & long workflows —** *multi-step tool chains*, *browse→retrieve→execute cycles*, *error recovery*, and *evidence traceability* in agent runs.
- **Developer productivity & coding assistants —** *compile-run-test loops*, *multi-file edits*, *test-validated repairs*, and *IDE integration* (Claude Code, Cursor, Codex, Grok CLI examples exist).
- **High-throughput agent fleets / production bots —** where *cost per inference* and *concurrency* matter, M2’s low activated parameter footprint can reduce infrastructure cost.

## How to call Minimax M2  API from CometAPI

### **`minimax-m2`** API Pricing in CometAPI，20% off the official price:

- Input Tokens: $0.24 M tokens
- Output Tokens: $0.96/ M tokens

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first.
- Sign into your [CometAPI console](https://www.cometapi.com/console/token).
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.

![Minimax M2 API](https://resource.cometapi.com/blog/uploads/2025/09/cometapi-key-guide-1024x527.webp)

### Use Method

1. Select the “minimax-m2” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to [API doc](https://apidoc.cometapi.com/):

- **Base URL:** `https://api.cometapi.com/v1/chat/completions`
- **Model Names:** “`minimax-m2`“
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

### API Integration & Examples

Below is a **Python** snippet demonstrating how to invoke GLM‑4.6 via CometAPI’s API. Replace `<API_KEY>` and `<PROMPT>` accordingly:

```
import requests

API_URL = "https://api.cometapi.com/v1/chat/completions"
headers = {
    "Authorization": "Bearer <API_KEY>",
    "Content-Type": "application/json"
}
payload = {
    "model": "minimax-m2",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "<PROMPT>"}
    ],
    "max_tokens": 512,
    "temperature": 0.7
}

response = requests.post(API_URL, json=payload, headers=headers)
print(response.json())
```

**See also [Claude Haiku 4.5 API](https://www.cometapi.com/claude-haiku-4-5-api/)**

---

*Originally published at [https://www.cometapi.com/minimax-m2-api/](https://www.cometapi.com/minimax-m2-api/).*
