<!-- social-ops-fingerprint:e1155662ca9f42d8925d94a43cf04a2675c264f6d82212140e3ed5ce3a9b9506 -->
---
title: Google launches gemini-embedding-001: its first text embedding model
---
# Google launches gemini-embedding-001: its first text embedding model

![Google launches gemini-embedding-001: its first text embedding model](https://resource.cometapi.com/blog/uploads/2025/07/Google-launches-gemini-embedding-001-its-first-text-embedding-model-.webp)

Google officially unveiled its first production-grade text embedding model, **gemini-embedding-001**, marking a pivotal moment in the company’s efforts to advance natural language understanding and representation. Now broadly available to developers via the Gemini API, Google AI Studio, and Vertex AI, this state‑of‑the‑art model promises to redefine semantic search, recommendation systems, and a wide array of downstream AI applications .

## Key Features and Capabilities

- **Multilingual Support:** gemini-embedding-001 natively handles over 100 languages, enabling truly global deployments and cross‑lingual retrieval tasks.
- **Context Length:** The model accepts inputs up to 2,048 tokens, accommodating long-form documents, code snippets, and multi-sentence passages without truncation .
- **Dynamic Output Dimensions:** Leveraging Google’s proprietary Matryoshka Representation Learning (MRL) technique, developers can flexibly adjust the embedding size—3072 dimensions by default, with optional reductions to 1536 or 768—optimizing for storage and compute costs while maintaining high fidelity .

## Benchmark Performance

gemini-embedding-001 has already demonstrated top-tier results on the **Massive Text Embedding Benchmark (MTEB)**. In multilingual and monolingual evaluations, it achieved an average task score of **68.32**, surpassing leading competitors such as Mistral and Qwen-based embeddings. Notably, it scored 85.13 on pair classification tasks, 67.71 on retrieval, and 65.58 on reranking—metrics that underscore its versatility across diverse text-processing scenarios.

![Google launches gemini-embedding-001](https://resource.cometapi.com/blog/uploads/2025/07/gemini-embedding-001-1024x576.webp)

## How to Use

To encourage experimentation and adoption, Google provides both **free and paid tiers** for gemini-embedding-001. After exhausting free‑tier quotas, usage is billed at **$0.15 per one million input tokens**, making it competitively priced within the industry .Rate limits are designed to accommodate a range of use cases, from lightweight development prototypes to enterprise‑scale deployments.

Developers can access `gemini-embedding-001` today through the existing `embed_content` endpoint in the Gemini API. Integration with Google AI Studio and Vertex AI ensures a smooth onboarding experience. Example usage in Python is straightforward:

```
from google import genai

client = genai.Client()

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="What is the meaning of life?"
)
print(result.embeddings)
```

For those transitioning from the experimental `gemini-embedding-exp-03-07` or legacy embedding models (`embedding-001`, `text-embedding-004`), Google has announced deprecation timelines: the experimental version and legacy `embedding-001` will be retired on **August 14, 2025**, while `text-embedding-004` is slated for deprecation on **January 14, 2026**. Early migration to gemini-embedding-001 is advised to ensure uninterrupted service and access to the latest performance improvements.

Looking ahead, Google plans to expand Gemini Embedding’s capabilities with **Batch API** support for asynchronous, cost‑efficient processing, as well as future embedding models covering broader modalities. With its powerful multilingual coverage, adjustable dimensionality, and competitive pricing, gemini-embedding-001 stands ready to power the next generation of AI‑driven applications.

## Getting Started

CometAPI provides a unified REST interface that aggregates hundreds of AI models—under a consistent endpoint, with built-in API-key management, usage quotas, and billing dashboards. Instead of juggling multiple vendor URLs and credentials.

Developers can access [Gemini 2.5 Pro Preview](https://www.cometapi.com/gemini-2-5-pro-api/) and [Veo 3](https://www.cometapi.com/veo-3-api/) through [CometAPI](https://www.cometapi.com/), the latest models version listed are as of the article’s publication date. And Supercharge your terminal with **Google’s Gemini CLI** on CometAPI! To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

The latest integration gemini-embedding-001 will soon appear on CometAPI, so stay tuned！While we finalize gemini-embedding-001 Model upload, explore our other models on the Models page or try them in the AI Playground.

---

*Originally published at [https://www.cometapi.com/google-launches-gemini-embedding-001/](https://www.cometapi.com/google-launches-gemini-embedding-001/).*
