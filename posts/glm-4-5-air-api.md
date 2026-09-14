<!-- social-ops-fingerprint:1b2c648c67baacac40e17f58664e797e11246b532e2493a38eb0661d1d5be5fd -->
---
title: GLM-4.5 Air API
---
# GLM-4.5 Air API

![GLM-4.5 Air API](https://resource.cometapi.com/blog/uploads/2025/07/zhipu-color.webp)

Zhipu’s GLM-4.5 Air API is a RESTful endpoint on the Z.ai (global) and Zhipu AI Open (Mainland China) platforms that provides access to the compact 106 billion‑parameter (12 billion active) GLM‑4.5 Air model—featuring hybrid “thinking” and “non‑thinking” modes and full configurability of inference settings (e.g., temperature, max tokens, streaming) for efficient, high‑throughput intelligent‑agent applications .

## Basic Features

- **Parameter Efficiency**: 106 billion **total parameters**, 12 billion **active parameters**, enabling a high performance-to-size ratio .
- **Hybrid Reasoning Modes**:
- **Thinking Mode** for **complex reasoning** and **tool usage**.
- **Non‑thinking Mode** for **instant responses**.
- **Open‑Source License**: Released under the **MIT license**, permitting **commercial use** and **secondary development** .

## Technical Architecture

- **Mixture-of‑Experts (MoE)** design, GLM-4.5 Air share the same core approach as the full GLM‑4.5 (355 B total / 32 B active) but optimized for a **compact footprint**.
- **128K Context Window**: Supports **long-horizon tasks** such as multi‑turn dialogue and document understanding.
- **Native Function Calling**: Allows seamless integration with external **APIs**, **databases**, or **tool chains** for agentic workflows .

## Benchmark Performance

Across **12 industry-standard benchmarks** spanning **agentic**, **reasoning**, and **coding** tasks:

- **Overall Score**: 59.8 (against 63.2 for GLM‑4.5), ranking **6th** among leading open‑source and proprietary models.
- **Agentic Benchmarks** (e.g., **BFCL v3**, **BrowseComp**): achieves **21.3%** on BrowseComp, demonstrating competitive **tool‑use capabilities**.
- **Reasoning & Coding** (e.g., **MMLU Pro**, **SWE‑Bench**): scores up to **81.4** on MMLU Pro and **57.6** on SWE‑Bench Verified.

![GLM-4.5 Air](https://resource.cometapi.com/blog/uploads/2025/07/benchmark-glm4.5-1024x622.webp)

## Model Version comparison

- **GLM‑4.5**: 355 B total / 32 B active — the **flagship** for **maximum capability**.
- **GLM-4.5 Air**: 106 B total / 12 B active — the **efficiency‑optimized** sibling for **resource‑sensitive deployments** .

## How to call **GLM-4.5 Air** API from CometAPI

### **`GLM-4.5 Air`** API Pricing in CometAPI，20% off the official price:

- Input Tokens: $0.16/ M tokens
- Output Tokens: $1.07/ M tokens

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`glm-4.5-air`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to [API doc](https://apidoc.cometapi.com/):

- **Base URL:** `https://api.cometapi.com/v1/chat/completions`
- **Model Names:** “`glm-4.5-air`“
- **Authentication:**  `Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

**See Also [GLM‑4.5 API](https://www.cometapi.com/glm%e2%80%914-5-api/)**

---

*Originally published at [https://www.cometapi.com/glm-4-5-air/](https://www.cometapi.com/glm-4-5-air/).*
