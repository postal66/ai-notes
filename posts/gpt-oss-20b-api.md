<!-- social-ops-fingerprint:290d00989a425940229badd7e47143202505a05dd0af09ed62cbad70408d07d1 -->
---
title: GPT-OSS-20B API
---
# GPT-OSS-20B API

![GPT-OSS-20B API](https://resource.cometapi.com/blog/uploads/2025/10/How-much-computing-power-is-required-for-GPT-OSS-deployment-710x373.webp)

`gpt-oss-20b` is a **portable, open‑weight reasoning model** offering **o3‑mini‑level performance**, **agent-friendly tool use**, and full **chain-of-thought support** under a permissive license. While it’s not as powerful as its 120 B counterpart, it’s uniquely suited for **on-device, low-latency, and privacy-sensitive deployments**. Developers should weigh its known **compositional limitations**, especially on knowledge-heavy tasks, and tailor safety precautions accordingly.

## Basic Information

`gpt-oss-20b` is a **21‑billion‑parameter open‑weight reasoning model** released by OpenAI under the **Apache 2.0 license**, enabling **full weight access for download, fine‑tuning, and redistribution**. It marks OpenAI’s first open‑weight model release since **GPT‑2 in 2019** and is optimized for **edge deployment and local inference** on systems with **≥ 16 GB VRAM**.

- **Parameters:** 21 billion total, of which 3.6 billion are active per token
- **Architecture:** Transformer with **mixture-of-experts (MoE)**
- **Context Window:** Up to 128 000 tokens for long-form understanding
- **License:** Apache 2.0, enabling unrestricted academic and commercial use ().

---

## Features & Technical Architecture

### Model Specifications

- **Parameters**: 21 B total, **3.6 B active per token** via Mixture-of-Experts (MoE) architecture with **32 experts per layer**, **4 active per token** .
- **Layers**: 24, context window up to **128K tokens**, max output tokens up to **32K** in some deployments .
- **Attention & Memory**: Alternating dense + sparse attention patterns; grouped multi-query attention (group size = 8) for inference efficiency .

### Training & Reasoning Controls

- Trained on English‑dominant text focusing STEM, coding, general knowledge.
- Supports **chain‑of‑thought (CoT)** reasoning and adjustable **reasoning levels** (Low, Medium, High) depending on task complexity .

---

## Benchmark Performance

- Matches or **exceeds performance of OpenAI’s o3‑mini model** on benchmarks like **MMLU, AIME, HLE, HealthBench, Codeforces, Tau‑Bench** even in its smaller size.
- Outperforms proprietary models such as **OpenAI o1, GPT‑4o, and o4‑mini in health and math reasoning** tasks at high reasoning levels .
- Compared to larger GPT‑OSS‑120B (117 B), it trails in tasks relying on deep symbolic reasoning or extensive knowledge (e.g. GPQA), but remains efficient in coding and health domains.

The **20 B** variant also impresses: it rivals **o3-mini** across the same suite despite its smaller footprint, showcasing efficient scaling of reasoning capabilities with MoE.

- **MMLU (Massive Multitask Language Understanding)**: ~88% accuracy
- **Codeforces Elo (coding reasoning)**: ~2205
- **AIME (math competition with tools)**: ~87.9%
- **HealthBench**: Significantly outperforms o4-mini in clinical QA and diagnosis tasks
- **Tau-Bench (Retail + Reasoning tasks)**: ~62% on average

---

## Model Version & Comparison

| Model | Params | Active Params | Hardware Need | Benchmark Performance |
| --- | --- | --- | --- | --- |
| **`gpt-oss-20b`** | 21 B | 3.6 B | ≥ 16 GB GPU or on-device | Comparable to **o3‑mini** |
| **gpt‑oss‑120**b | 117 B | 5.1 B | 80 GB+ GPU | Matches or exceeds **o4‑mini** |

Designed as a lightweight counterpart to **gpt‑oss‑120B**, GPT‑OSS‑20B offers portability while maintaining strong task performance where resource is constrained. It stands out against proprietary OpenAI models for being openly accessible and tunable.

---

## Limitations

- **Lower knowledge recall** on complex tasks like GPQA compared to larger models .
- **Reports from users** indicate variability in real‑world performance, especially for coding or general‑knowledge prompts; some attribute this to early implementation or prompt misuse.
- **Safety & misuse risks**: While OpenAI evaluated adversarial fine‑tuned gpt‑oss variants, even those did not reach high capability in biorisk or cyber domains; still, users deploying large-scale use cases may require extra safeguards.

---

## Use Cases

OpenAI has engineered GPT‑OSS to support a **wide spectrum of use cases**, ranging from consumer apps to enterprise-grade analytics. The 20B variant is optimized for local execution, capable of running on devices with as little as **16GB of RAM**, such as **high-end laptops or MacBooks with M-series chips**. GPT‑OSS‑20B is ideal for:

- **Local/offline inference** on Windows PCs (via Windows AI Foundry), macOS, or Snapdragon-based edge devices.
- **Agentic workflows**: code execution, tool use, browser-based agents, or autonomous assistants in constrained bandwidth settings.
- **Rapid prototyping and fine-tuning**, especially for developers working without cloud infrastructure or with privacy constraints.

## Other Model Comparisons

- `gpt-oss-20b`**vs. o3‑mini / o4‑mini**: GPT‑OSS‑20B rivals o3‑mini in accuracy and co‑thought reasoning; it is more efficient and open than o4‑mini but underperforms compared to **gpt‑oss‑120B** on demanding reasoning tasks.
- `gpt-oss-20b` **vs. LLaMA 4, GLM‑4.5, DeepSeek**: GPT‑OSS‑20B brings full open‑weight transparency under Apache 2.0, unlike semi‑open models; but users report in some cases preferring GLM‑4.5‑AIR on reasoning quality .

## How to call **gpt-oss-20b** API from CometAPI

### **`gpt-oss-20b`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Input Tokens | $0.08 |
| Output Tokens | $0.32 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`gpt-oss-20b`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to  [API doc](https://apidoc.cometapi.com/):

- **Core Parameters**: `prompt`, `max_tokens_to_sample`, `temperature`, `stop_sequences`
- **Endpoint:** `https://api.cometapi.com/v1/chat/completions`
- **Model Parameter:** “`gpt-oss-20b`“
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY`
- **Content-Type:** `application/json` .

### API Call Example

Although open-weight, GPT‑OSS models can be accessed via APIs such as CometAPI, and others. For **gpt‑oss‑20B**, a typical call to CometAPI look like:

```
POST  https://api.cometapi.com/v1/chat/completions
{
  "model": "gpt-oss-20b",
  "messages": [{ "role": "system", "content": "Reasoning: high" },
               { "role": "user", "content": "Solve bilateral integral…" }],
  "max_tokens": 2048,
  "temperature": 0.0
}
```

This supports function‑calling, structured output schemas, tool integrations, and reasoning control via system prompts.

**See Also [GPT-OSS-120B](https://www.cometapi.com/gpt-oss-120b/)**

---

*Originally published at [https://www.cometapi.com/gpt-oss-20b/](https://www.cometapi.com/gpt-oss-20b/).*
