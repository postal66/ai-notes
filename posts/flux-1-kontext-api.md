<!-- social-ops-fingerprint:6822508135249cbebc2bf0d227d5332aefe23980d3175c725d55e584e217ccae -->
---
title: FLUX.1 Kontext API
---
# FLUX.1 Kontext API

![FLUX.1 Kontext API](https://resource.cometapi.com/blog/uploads/2025/08/Which-is-the-best-image-generation-and-image-editing-AI-in-2025-710x373.webp)

The Flux.1 Kontext API offers a unified, RESTful and SDK-accessible interface for seamless multimodal image generation and iterative in-context editing, allowing developers to combine text and visual prompts into a single flow-matching workflow.

FLUX.1 Kontext is **Black Forest Labs**’ latest **in-context generative flow matching** model, designed to revolutionize how creators generate and edit images. Unlike traditional text-to-image systems, it natively accepts both **text** and **image** inputs, enabling seamless **context-aware** generation and precise **local edits** within a unified framework.

## Basic Information & Features

- **Multimodal Inputs**: Accepts **text** and **image** prompts simultaneously for richer context understanding.
- **Character Consistency**: Maintains fidelity of subjects across multiple editing turns.
- **Local Editing**: Targets specific regions without affecting the rest of the image.
- **Style Reference**: Replicates existing visual styles for coherent scene generation.
- **Minimal Latency**: Inference times of **3–5 seconds** at 1 MP resolution, up to **8× faster** than leading alternatives .

## Model Versions & Availability

- **FLUX.1 Kontext** : Balanced performance for **iterative editing**; up to an order of magnitude faster than previous state-of-the-art models.
- **FLUX.1 Kontext** : Prioritizes **prompt fidelity**, **typography readability**, and **maximized speed**.
- **FLUX.1 Kontext** : A **12 B-parameter** open-weight variant, currently in private beta.

## Technical Architecture

Flux.1 Kontext leverages **rectified flow transformer blocks** scaled to 12 billion parameters, operating in a latent space for high-fidelity outputs. It concatenates text and encoded image tokens into a unified sequence, enabling both **local editing** (targeted modifications) and **global generation** within one model . This design achieves:

- **Semantic Context Integration:** Joint processing of visual and textual modalities.
- **Unified Workflow:** No need for separate inpainting or text-to-image pipelines.
- **Latent-space Efficiency:** Reduced memory footprint and faster inference on a variety of GPUs.

## Benchmark Performance

| Metric | FLUX.1 Kontext | OpenAI 4o/gpt-image-1 |
| --- | --- | --- |
| Prompt Adherence Rate | 98.7 % | 93.2 % |
| Average Generation Latency | 2.3 s | 3.1 s |
| Color Accuracy (ΔE₀₀) | 1.2 | 2.8 |
| Multi-Scene Consistency | High | Medium |

- **Superior Prompt Following**: Outperforms competitors with **accurate semantic interpretation** and **stable stylization**.
- **Reduced Artifacts**: Eliminates common issues like **yellow tint** and **banding**, ensuring **professional-quality** outputs.

## How to call **`FLUX.1 Kontext`** API from CometAPI

### **`FLUX.1 Kontext`** API Pricing in CometAPI，lower than official price:

|  |  |  |
| --- | --- | --- |
| Model Variants | Kontext | Kontext |
| Price in CometAPI | Pricing:$0.096 | Pricing:$0.192 |
|  | pay per view | pay per view |
| model name | **`flux-kontext-pro`**; `black-forest-labs/flux-kontext-pro` | **`flux-kontext-max`**； `black-forest-labs/flux-kontext-max` |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Useage Methods

1. Select the “**`flux-kontext-pro`**”or “`black-forest-labs/flux-kontext-pro`”endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_AIMLAPI\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

For Model lunched information in Comet API please see [https://api.cometapi.com/new-model.](https://www.cometapi.com/changelog/)

For Model Price information in Comet API please see [https://api.cometapi.com/pricing](https://www.cometapi.com/pricing/).

### Code Usage:

Method 1: **`black-forest-labs/flux-kontext-pro`**, **`black-forest-labs/flux-kontext-max`**

The above two models follow the replicate call format,Here’s a simplified example of a JSON request :

```
curl --location
--request POST 'https://api.cometapi.com/replicate/v1/predictions' \
--header 'Authorization: Bearer sk-' \
--header 'Prefer: wait=10' \
--header 'User-Agent: Apifox/1.0.0 (https://apifox.com)' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--header 'Host: api.cometapi.com' \
--header 'Connection: keep-alive' \
--data-raw '{ "model": "black-forest-labs/flux-kontext-max", "input": { "prompt": "black forest gateau cake spelling out the words \"FLUX SCHNELL\", tasty, food photography, dynamic shot" } }'
```

Method 2: **`flux-kontext-pro`**, **`flux-kontext-max`**

The above two models follow the OpenAI chat standard call format and Calling through technical means. Here’s a simplified example of a JSON request:

```
curl --
location
--request POST 'https://api.cometapi.com/v1/chat/completions' \
--header 'Authorization: sk-' \
--header 'User-Agent: Apifox/1.0.0 (https://apifox.com)' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--header 'Host: api.cometapi.com' \
--header 'Connection: keep-alive' \ --data-raw '{ "model": "flux-kontext-pro", "messages":  }'
```

**See Also [GPT-image-1 API](https://www.cometapi.com/gpt-image-1-api/)**

---

*Originally published at [https://www.cometapi.com/flux-1-kontext/](https://www.cometapi.com/flux-1-kontext/).*
