<!-- social-ops-fingerprint:e3c88047aa0c8914ff93995e3e4a93ed98ea9ed7dfbf2856499b24f317e6489b -->
---
title: Grok 4 API
---
# Grok 4 API

![Grok 4 API](https://resource.cometapi.com/blog/uploads/2025/07/grok4001-1024x535.webp)

The Grok 4 API is a developer-friendly, OpenAI-compatible interface that enables access to xAI’s latest large language model for advanced text generation, reasoning, and coding tasks via secure RESTful endpoints.

**Grok 4** positioning it as its most advanced large language model (LLM) to date. Billed as a “flagship model,” it aims to **rewrite human knowledge** through significantly enhanced reasoning, coding, and multimodal capabilities .

## Basic Information and Features

- **Release Date:** July 9, 2025
- **Modalities:** Primarily **text**, with upcoming support for **vision** and **image generation**

### Variants:

- **Grok 4** – general-purpose LLM for natural language, reasoning, and math
- **Grok 4 Code** – specialized for **code generation**, **debugging**, and **function calling**.

### Features

- **Generative Chatbot**: Grok 4 continues xAI’s lineage of chat-based LLMs (Grok‑1 through Grok‑3), now integrated deep across Musk’s X platform, standalone web app, and mobile application.
- **Multimodality**: In addition to **text**, Grok 4 introduces early support for **vision** inputs—paving the way for image understanding and generation.
- **Expressive Voice Assistant**: The “Eve” persona, introduced earlier, now benefits from its refined speech synthesis, offering **singing** and expressive dialogue.

## Technical Architecture and Model Versions

- **Architecture**: Grok 4 builds on a transformer-based backbone with significant architectural refinements geared toward **logical consistency** and **context retention** over extended dialogues.
- **Training Regimen**: Trained on a bespoke corpus scraped from publicly available X posts, open web sources, and licensed datasets. xAI emphasizes **data refinement** to filter “garbage data” and mitigate bias.

---

## Benchmark Performance

xAI highlights that Grok 4 outperforms most AI systems on key academic and coding benchmarks:

- **AIME:** 98.8 (Advanced Intelligence Math Exam)
- **GPQA:** 88 (Graduate-level Prompted QA)
- **SWE‑Bench:** 75 (Software Engineering tasks)
- **Humanity Last Exam (HLE):** 45% overall with advanced reasoning.
  In live demos, Elon Musk claimed Grok 4 is “smarter than almost all graduate students,” underscoring its leadership in **multi-disciplinary performance** .

![Grok 4 API](https://resource.cometapi.com/blog/uploads/2025/07/grok4001-1024x535.webp)

## How to call Grok 4 API from CometAPI

### **`Grok 4`** API Pricing in CometAPI，20% off the official price:

- Input Tokens: $2.4/ M tokens
- Output Tokens: $12/ M tokens

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`grok-4`”or “`grok-4-0709`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details:

- **Base URL:** `https://api.cometapi.com/v1/chat/completions`
- **Model Names:** “`grok-4`”or “`grok-4-0709`“
- **Authentication:** Bearer token via `Authorization: Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

Here’s a sample **cURL** snippet for invoking the Grok 4 API:

```
curl -X POST "https://api.cometapi.com/v1/chat/completions" \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "grok-4",
       "prompt": "Explain the benefits of renewable energy.",
       "max_tokens": 250,
       "temperature": 0.7
     }'
```

- **Authorization**: Replace `YOUR_API_KEY` with your CometAPI token.
- **Parameters**: Adjust `max_tokens` and `temperature` to control response length and creativity.

This snippet demonstrates how to make an **API call**, set the **model version**, and handle **chat completions**.

**See Also [o3-Pro API](https://www.cometapi.com/o3-pro-api/)** and [Gemini 2.5 Pro Preview API](https://www.cometapi.com/gemini-2-5-pro-api/) etc

---

*Originally published at [https://www.cometapi.com/grok-4-api/](https://www.cometapi.com/grok-4-api/).*
