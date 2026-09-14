<!-- social-ops-fingerprint:349a98ae2b0dba33284789df149529d26c58038486b60430b3625a64f828c0d2 -->
---
title: Kimi K2 API
---
# Kimi K2 API

![Kimi K2 API](https://resource.cometapi.com/blog/uploads/2025/07/moonshot-2.png)

Kimi K2 API is an open‑source, trillion‑parameter Mixture‑of‑Experts language model with a 256K‑token context window, optimized for high‑performance coding, agentic reasoning, and efficient inference.

Kimi K2-0905 is the latest AI model released by Darkside of the Moon Technology Co., Ltd. It boasts powerful programming assistance capabilities, excelling in code generation and front-end development. Its context length is extended to 256KB, supporting complex tasks. The high-speed API output speed of the model reaches 60–100 tokens/second, ensuring fast response times.

The model is compatible with the Anthropic API, supports the WebSearch Tool, and offers an enhanced Claude Code experience. It also provides automatic context caching to reduce user costs. Users can now experience it through CometAPI (`kimi-k2-250905`).

## Basic Information & Features

- **Model Name:** Kimi K2
- **Architecture:** Mixture‑of‑Experts (MoE)
- **Total Parameters:** 1 trillion
- **Activated Parameters:** 32 billion per forward pass
- **Context Length:** 256 K tokens
- **Vocabulary Size:** 160 K tokens
- **Primary Use Cases:** Coding, tool integration, complex task decomposition, general reasoning.

### Technical Architecture

Kimi K2 employs a **384‑expert MoE** design, selecting **8 experts per token** to balance performance with inference efficiency. It comprises **61 layers**, including **1 dense layer**, and utilizes **Multi‑Layer Attention** (MLA) alongside the **SwiGLU** activation function. Training leveraged the **Muon optimizer** over **15.5 trillion tokens**, ensuring stability and high throughput across diverse benchmarks.

### Benchmark Performance

- **SWE‑bench Verified:** 65.8% single‑attempt accuracy—surpassing GPT‑4.1’s 54.6% and trailing only Claude Sonnet 4 among top models.
- **Multilingual SWE‑bench:** 47.3% accuracy, leading open‑source contenders.
- **LiveCodeBench:** 53.7%, the highest among non‑proprietary models.
- **EvalPlus:** 80.3, outperforming DeepSeek‑V3 and Qwen 2.5 series.

These results underscore Kimi K2’s **state‑of‑the‑art coding proficiency** and robust reasoning capabilities.

![kimi k2](https://resource.cometapi.com/blog/uploads/2025/07/Kimi-K2-1024x576.webp)

## How to call Kimi K2 API from CometAPI

### **`Kimi K2`** API Pricing in CometAPI，20% off the official price:

- Input Tokens: $0.11/ M tokens
- Output Tokens: $1.99/ M tokens

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`kimi-k2-0711-preview`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to [API doc](https://apidoc.cometapi.com/):

- **Base URL:** `https://api.cometapi.com/v1/chat/completions`
- **Model Names:** “`kimi-k2-250905`“
- **Authentication:** Bearer token via `Authorization: Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

### API Integration & Examples

Kimi K2 is accessible via **CometAPI** (OpenAI‑compatible) and the **Moonshot AI API**. Below is a Python snippet for a **ChatCompletion** call through CometAPI:

Python snippet for a **ChatCompletion** call through CometAPI:

```
pythonimport openai

openai.api_key = "YOUR_CometAPI_API_KEY"
openai.api_base = "https://api.cometapi.com/v1/chat/completions"

messages = [
    {"role": "system",  "content": "You are a helpful assistant."},
    {"role": "user",    "content": "Summarize Kimi K2's main features."}
]

response = openai.ChatCompletion.create(
    model="kimi-k2-250905",
    messages=messages,
    temperature=0.7,
    max_tokens=500
)

print(response.choices.message)
```

---

*Originally published at [https://www.cometapi.com/kimi-k2-api/](https://www.cometapi.com/kimi-k2-api/).*
