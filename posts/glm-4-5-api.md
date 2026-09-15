<!-- social-ops-fingerprint:2529fea84a2d1509e1cce15b0dc4a092650359c990a49963f014f19ea465de3e -->
---
title: GLM‑4.5 API
---
# GLM‑4.5 API

![GLM‑4.5 API](https://resource.cometapi.com/blog/uploads/2025/07/zhipu-color.webp)

Zhipu’s GLM‑4.5 API is a unified RESTful service on the Z.ai (global) and Zhipu AI Open (Mainland China) platforms that exposes the 355 billion‑parameter, hybrid‑expert GLM‑4.5 model—capable of complex reasoning, coding, and agentic tasks—with configurable options (e.g., temperature, max tokens, streaming).

---

## Basic Features

GLM‑4.5 is designed as a **unified agentic model**, integrating **reasoning**, **coding**, and **autonomous decision‑making** capabilities within a single architecture. It natively supports two operational modes—**thinking** for complex reasoning and tool usage, and **non‑thinking** for rapid, on‑demand responses—making it ideal for versatile **agent** workflows.

---

## Technical Details

- **Parameter Scale**: The flagship GLM‑4.5 comprises **355 billion** total parameters with **32 billion active** parameters.
- **Hybrid Reasoning**: GLM‑4.5 employs a **hybrid FP8 quantization** strategy to optimize **inference efficiency** without substantially sacrificing accuracy.
- **Parameter Efficiency**: Uses **32 B active parameters** out of 355 B to minimize hardware load during inference .
- **Layer Optimization**: Components pruned and redistributed into deeper layers, enhancing **logical reasoning** without ballooning model size .

### Training Workflow

**Multi‑Stage Training**:

1. **Foundation Pre‑training** on ~15 trillion tokens.
2. **Reasoning Fine‑tuning** on >7 trillion curated tokens to sharpen decision‑making and code synthesis.

---

## Benchmark Performance

On a suite of **12 industry‑standard benchmarks** covering **agentic**, **reasoning**, and **coding** tasks, GLM‑4.5 achieved an overall score of **63.2**, ranking **third** globally behind proprietary titans such as **GPT‑4** and **Grok 4**. Highlights include:

| Benchmark | GLM‑4.5 Score | Top Proprietary Comparison |
| --- | --- | --- |
| **BrowseComp (web)** | 26.4 % | Claude 4 Opus: 18.8 % |
| **MATH 500** | 98.2 % | GPT‑4 Turbo |
| **AIME24** | 91.0 % | Claude 4 Sonnet |
| **GPQA** | 79.1 % | Gemini 2.5 Pro |

In a suite of 12 competitive tests—spanning **coding**, **reasoning**, and **agentic** benchmarks—GLM‑4.5 ranks **third overall**, matching or surpassing leading proprietary models such as Claude 4 Sonnet and Gemini 2.5 Pro on tasks like **SWE‑bench** and **AIME24** .

![GLM‑4.5](https://resource.cometapi.com/blog/uploads/2025/07/benchmark-glm4.5-1-1024x622.webp)

---

## Model Versions

The **GLM‑4.5 family** includes several specialized variants accessible via API:

- **GLM‑4.5** (355 B total parameters; 32 B active)
- **GLM‑4.5‑Air** (106 B total; lightweight, faster inference)
- **GLM‑4.5‑X**, **GLM‑4.5‑AirX** (ultra‑fast inference)
- **GLM‑4.5‑Flash** (free, optimized for coding & reasoning)

## How to call **GLM‑4.5** API from CometAPI

### **`GLM‑4.5`** Series API Pricing in CometAPI，20% off the official price:

|  |  |  |
| --- | --- | --- |
| Model | introduce | Price |
| `glm-4.5` | Our most powerful reasoning model, with 355 billion parameters | Input Tokens $0.48 Output Tokens $1.92 |
| **`glm-4.5-air`** | Cost-Effective Lightweight Strong Performance | Input Tokens $0.16 Output Tokens $1.07 |
| `glm-4.5-x` | High Performance Strong Reasoning Ultra-Fast Response | Input Tokens $1.60 Output Tokens $6.40 |
| **`glm-4.5-airx`** | Lightweight Strong Performance Ultra-Fast Response | Input Tokens $0.02 Output Tokens $0.06 |
| **`glm-4.5-flash`** | Strong Performance Excellent for Reasoning Coding & Agents | Input Tokens $3.20 Output Tokens $12.80 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`glm-4.5`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to [API doc](https://apidoc.cometapi.com/):

- **Base URL:** `https://api.cometapi.com/v1/chat/completions`
- **Model Names:** “`glm-4.5`“
- **Authentication:**  `Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

### API Integration & Examples

Below is a **Python** snippet demonstrating how to invoke GLM‑4.5 via CometAPI’s API. Replace `<API_KEY>` and `<PROMPT>` accordingly:

```
import requests

API_URL = "https://api.cometapi.com/v1/chat/completions"
headers = {
    "Authorization": "Bearer <API_KEY>",
    "Content-Type": "application/json"
}
payload = {
    "model": "glm-4.5",
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

**Key Parameters**:

- **model**: Specifies the GLM‑4.5 variant
- **max\_tokens**: Controls output length
- **temperature**: Adjusts creativity vs. determinism

**See Also [[GLM-4.5 Air API](https://www.cometapi.com/glm-4-5-air/)](<https://www.cometapi.com/grok-4-api/>)**

---

---

*Originally published at [https://www.cometapi.com/glm%E2%80%914-5-api/](https://www.cometapi.com/glm%E2%80%914-5-api/).*
