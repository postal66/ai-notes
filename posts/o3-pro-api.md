<!-- social-ops-fingerprint:03538465df6ccd928fe3b8e7f854ab91b8447e8dd1319ac0a57ebe03164ba63a -->
---
title: o3-Pro API
---
# o3-Pro API

![o3-Pro API](https://resource.cometapi.com/blog/uploads/2025/06/o3-pro.jpg)

The o3-Pro API is a RESTful ChatCompletion endpoint that enables developers to invoke OpenAI’s advanced chain-of-thought reasoning, code execution, and data-analysis capabilities via configurable parameters (model=”o3-pro”, messages, temperature, max\_tokens, streaming, etc.) for seamless integration into complex workflows.

OpenAI o3‑pro is a “pro” variant of the o3 reasoning model engineered to think longer and deliver the most dependable responses by employing private chain‑of‑thought reinforcement learning and setting new state‑of‑the‑art benchmarks across domains like science, programming, and business—while autonomously integrating tools such as web search, file analysis, Python execution, and visual reasoning within API.

![o3-Pro](https://resource.cometapi.com/blog/uploads/2025/06/o3-pro-1024x573.jpg)

---

## Basic Information & **Features**

- **Model Class**: o3-Pro is part of OpenAI’s “reasoning models,” designed to **think step-by-step** rather than generate immediate responses.
- **Availability**: Accessible via ChatGPT Pro/Team interfaces and the OpenAI developer API as of June 10, 2025.
- **Access Tiers**: Replaces the previous o1-Pro edition; Enterprise and Edu users onboard in the week following launch.

---

## Technical Details

- **Architecture**: Builds on the o3 backbone with an enhanced **private chain of thought**, enabling multi-step reasoning at inference.
- **Tokenization**: Supports the same token schema as its predecessors—1 million input tokens ≈ 750,000 words.
- **Extended Capabilities**: Includes web search, Python code execution, file analysis, and visual reasoning; image generation remains unsupported in this release.

---

## Evolution of the o-Series

- **o1 → o3**: Initial jump from o1 to o3 in April 2025 introduced reasoning capabilities.
- **Pricing Strategy**: Alongside o3-Pro’s debut, OpenAI cut o3’s price by **80 percent**—from $2 to $0.40 per million input tokens—to accelerate adoption.
- **o3-Pro Release**: Premium compute and fine-tuned reasoning pathways deliver the highest reliability at a **premium tier**.

---

## Benchmark Performance

- **Math & Science**: Surpassed Google Gemini 2.5 Pro on the AIME 2024 contest, demonstrating superior problem-solving in advanced mathematics.
- **PhD-Level Science**: Outperformed Anthropic’s Claude 4 Opus on the GPQA Diamond benchmark, indicating robust expertise in scientific domains.
- **Enterprise Use**: Internal tests report consistent wins over predecessor models across coding, STEM, and business reasoning tasks.

---

## Technical Indicators

- **Latency**: Response times are higher than o1-Pro—reflecting the deeper reasoning chains—averaging **1.5×** the previous latency.
- **Throughput**: Sustained token-generation throughput of up to **10 tokens/sec** in burst mode.

---

With its enhanced reasoning chains, expanded feature set, and leading benchmark performance, **o3-Pro** represents a significant step forward in reliable, high-precision AI.

## How to call o3-Pro API from CometAPI

### **`o3-Pro`** API Pricing in CometAPI，20% off the official price:

- Input Tokens: $16/ M tokens
- Output Tokens: $64/ M tokens

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Useage Methods

1. Select the “**`o3-Pro`**“or”**`o3-pro-2025-06-10`**” endpoint to send the request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

For Model Access information in Comet API please see [API doc](https://apidoc.cometapi.com/).

This model adheres to the OpenAI v1/responses standard call format.  For specific reference:

```
curl --location
--request POST 'https://api.cometapi.com/v1/responses' \
--header 'Authorization: Bearer sk-xxxxxx' \
--header 'User-Agent: Apifox/1.0.0 (https://apifox.com)' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--header 'Host: api.cometapi.com' \
--header 'Connection: keep-alive' \
--data-raw '{ "model": "o3-pro", "input":  }'
```

If you have any questions about the call or have any suggestions for us, please contact us through social media and email address [support@cometapi.com](mailto:support@cometapi.com).

**See Also** :

- [O3 API](https://www.cometapi.com/o3-api/)
- [O4-Mini API](https://www.cometapi.com/o4-mini-api-cometapi/)
- [GPT-4.1 API](https://www.cometapi.com/gpt-4-1-api/)

---

*Originally published at [https://www.cometapi.com/o3-pro-api/](https://www.cometapi.com/o3-pro-api/).*
