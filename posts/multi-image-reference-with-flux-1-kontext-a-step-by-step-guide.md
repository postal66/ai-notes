<!-- social-ops-fingerprint:829571334ca5401949569e541dc2cb74e40de5ef8063558591f34da811649ca1 -->
---
title: Multi-Image Reference With Flux.1 Kontext: A Step-by-step Guide
---
# Multi-Image Reference With Flux.1 Kontext: A Step-by-step Guide

![Multi-Image Reference With Flux.1 Kontext: A Step-by-step Guide](https://resource.cometapi.com/blog/uploads/2025/08/FLUX.1-Kontext-Dev.webp)

Flux.1 Kontext’s “multi-image reference” capability represents a paradigm shift in how AI-driven image editing and generation workflows handle multiple visual inputs. By allowing creators to feed several reference images simultaneously, Flux.1 Kontext can maintain coherent style, pose, and lighting across all inputs—enabling unified batch edits, consistent style transfers, and complex scene compositions. Below, we explore the foundations, recent breakthroughs, and best practices for mastering multi-image reference processing with Flux Kontext.

## What is Flux.1 Kontext and why is it transforming image editing?

Flux.1 Kontext represents the latest advancement in multimodal image generation and editing, built upon the Flux series of flow-based transformer models. Flux models—developed by Black Forest Labs—are based on rectified flow transformer blocks, scaling up to 12 billion parameters to deliver high-fidelity text-to-image synthesis and editing capabilities. Unlike traditional text-to-image pipelines, Flux.1 Kontext extends these foundations by enabling **in-context** editing: users can supply not only text prompts but also one or more reference images, allowing the model to semantically understand visual concepts and apply them to novel outputs .

The significance of Flux.1 Kontext lies in its unified architecture—dubbed **generative flow matching**—which handles both **local edits** (e.g., changing the color of an object in a photo) and **global transformations** (e.g., generating new views of a scene) within a single model. This removes the need for separate editing and generation models, streamlining workflows and reducing context-switching for creative professionals .

---

### What are the different Flux.1 Kontext variants?

Flux.1 Kontext comes in three main variants, each catering to distinct use cases and licensing models:

1. **Flux.1Kontext Dev**: A source-available model under a non-commercial license, primarily designed for experimentation and integration into local GPU-powered workflows.
2. **Flux.1 Kontext Pro**: A proprietary, API-accessible model offering industry-grade performance, consistent results, and commercial support.
3. **Flux.1 Kontext Max**: The premium tier with enhanced typography handling, maximum throughput, and improved edge-case fidelity.

Together, these variants ensure that both researchers and enterprise users can leverage multimodal editing, whether they prioritize customizability or production stability .

## What is “multi-image reference” in Flux.1 Kontext?

Multi-image reference refers to the process of supplying multiple example images to an AI model so that it can infer shared characteristics—such as style, lighting, or subject identity—and apply consistent edits or generate novel content that respects those attributes across all inputs. Unlike single-image conditioning, this approach empowers creators to enforce uniformity in batch outputs, reducing manual touch-ups and ensuring visual coherence.

### How does Flux.1Kontext implement multi-image reference?

At the core of Flux.1 Kontext’s multi-image capability is its **flow matching** framework. Rather than treating each reference image in isolation, Flux.1 Kontext concatenates image embeddings and text tokens into a unified sequence. A transformer-based flow matcher then learns to align and merge these embeddings in latent space, effectively capturing both individual and joint visual semantics.

Conventional multi-reference approaches often average embeddings or rely on heavy fine-tuning (e.g., LoRA). Flux.1 Kontext’s flow matching approach:

- **Preserves consistency** across multiple turns, maintaining object identities and styles.
- **Reduces degradation**, which is common in iterative editing pipelines.
- **Supports interactive rates**, enabling near-real-time previews in applications.

## What workflows enable multi-image integration with Flux.1 Kontext?

Flux.1 Kontext’s design ensures seamless integration into both GUI-based and code-driven pipelines:

### ComfyUI Integration

By leveraging ComfyUI’s node-based interface, users can feed multiple reference images directly into a dedicated “Flux.1 Kontext Dev” node. This node accepts a list of images alongside a text prompt, outputting a unified diffusion graph result. Two primary modes exist:

- **Concatenation Mode**: Sequentially appends embeddings, ideal for simple composite tasks.
- **Cross-Attention Mode**: Interleaves attention maps for deeper semantic blending, preferable for complex style merges.
  Prompt tricks—such as specifying per-image weights and seam-blending tokens—help prevent color shifts and visible joins ().

### API-First Approach (Replicate, CometAPI)

Developers can interact with Flux.1 Kontext Max or Pro via RESTful endpoints. The API schema typically includes:

```
   {
     "input_images": ,
     "prompt": "Describe the desired transformation",
     "options": { "blend_strength": 0.8, "seed": 42 }
   }
```

Playground and SDK support in JavaScript, Python, and Go make it straightforward to incorporate multi-image conditioning into web or mobile apps .

## Multi-Image Reference With CometAPI’s Flux.Kontext api

Below is a step-by-step guide to submitting multi-image reference requests to the FLUX 1 Kontext API. It covers authentication, request construction (with two reference images), result handling, and best practices.

---

### 1. How do I authenticate with the FLUX.1 Kontext API?

If you’re using Replicate’s hosted FLUX 1 Kontext apps, log in at Replicate → your account → API Tokens.

**Obtain your API key**: Register and Login [CometAPI](https://www.cometapi.com/), retrieve your bearer token from your dashboard.

**Include the key in your header** `Authorization: Token YOUR_API_TOKEN` or, for bearer-style APIs: `Authorization: Bearer YOUR_API_TOKEN`

---

### 2. Which endpoint handles two-image fusion?

For the “combine two images” model on Replicate (`flux-kontext-apps/multi-image-kontext-pro`), send your POSTs to:

```
https://api.replicate.com/v1/predictions
```

For CometAPI’s managed API, it will be:

```
https://api.cometapi.com/replicate/v1/models/black-forest-labs/flux-kontext-max/predictions
```

> Note: In CometAPI, Only flux-kontext supports multiple image references，To call the following different models you need to switch the model name after the model in the url:
> `black-forest-labs/flux-kontext-max`
> `black-forest-labs/flux-kontext-pro`

Both endpoints expect a JSON payload containing `prompt`, `input_image_1`, and `input_image_2` .

---

### 3. What does the request payload look like?

Below is the minimal JSON schema as documented for `multi-image-kontext-pro`:

| Field | Type | Description |
| --- | --- | --- |
| `prompt` | string | Text description of how to combine or transform the two input images |
| `input_image_1` | string | URL or Base64 data URI of first image (JPEG/PNG/WebP/GIF) |
| `input_image_2` | string | URL or Base64 data URI of second image |
| `aspect_ratio` | enum | (optional) `match_input`, `1:1`, `16:9`, etc. Defaults to `match_input` |

> **Tip:** You can pass publicly-hosted URLs or inline Base64 data URIs—Base64 is convenient for one-off scripts but may slow down very large files .

> Now CometAPI supports uploading up to 4 reference images (previously only single image supported)

---

### 4. How do I send a multi-image request with cURL?

```
curl https://api.replicate.com/v1/predictions \
  -H "Authorization: Token $REPLICATE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "version": "multi-image-kontext-pro:f3545943bdffdf06420f0d8ececf86a36ce401b9df0ad5ec0124234c0665cfed",
    "input": {
      "prompt": "Blend the lighting from image1 with the background of image2, preserving color harmony",
      "input_image_1": "https://example.com/portrait1.png",
      "input_image_2": "https://example.com/background2.jpg",
      "aspect_ratio": "match_input"
    }
  }'
```

- Replace the `version` field with the latest model version ID from Replicate.
- On CometAPI, swap in their `/predict` endpoint and use `"file": { ... }` per their docs.

---

### 5. How can I do the same in Python?

```
import requests

API_TOKEN = "YOUR_API_TOKEN"
headers = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json",
}

payload = {
    "version": "multi-image-kontext-pro:f3545943bdffdf06420f0d8ececf86a36ce401b9df0ad5ec0124234c0665cfed",
    "input": {
        "prompt": "Combine the style of image1 with the content of image2, matching lighting and mood",
        "input_image_1": "https://my-bucket.s3.amazonaws.com/imgA.png",
        "input_image_2": "https://my-bucket.s3.amazonaws.com/imgB.png",
        "aspect_ratio": "match_input"
    },
}

resp = requests.post("https://api.replicate.com/v1/predictions", json=payload, headers=headers)
resp.raise_for_status()
data = resp.json()
print("🖼️ Output URL:", data)
```

- Check `data` (“starting” → “processing” → “succeeded”) to poll until ready.

---

### 6. How do I handle and display the result?

When prediction completes, the model returns a URI to the fused image:

```
{
  "id": "...",
  "status": "succeeded",
  "output": "https://.../result.png"
}
```

Fetch that URL (or embed it directly in your application/UI).

## How to maximize results: best practices?

### Which reference images should you select?

- **Homogeneity**: Choose images with consistent style, subject scale, and lighting for optimal uniformity.
- **Diversity for Style Transfer**: When applying a new style, include a variety of examples showcasing the full range of desired effects.
- **High-Resolution Inputs**: Better quality references yield sharper generative outputs, especially for fine details like textures and facial features.
- **Image size limits:** Keep each input under 10 MB (Replicate standard) to avoid timeouts.
- **Formats:** JPEG, PNG, GIF, and WebP work best; avoid exotic formats.

**Prompt engineering:**

- Be explicit: “preserve facial features from image1”
- Use weighting: “image1 priority high, image2 priority low”
- **Rate limits:** Check your plan’s QPS limits; batch requests carefully.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access [FLUX.1 Kontext](https://www.cometapi.com/flux-1-kontext/) (Model: `flux-kontext-pro ; flux-kontext-max`) through [CometAPI](https://www.cometapi.com/), the latest models version listed are as of the article’s publication date. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

---

## Conclusion

Multi-image referencing with FLUX 1 Kontext represents a paradigm shift in generative AI workflows. By unifying text and multiple visual inputs within a single flow matching architecture, it empowers creators to achieve complex, consistent outputs in fewer steps. Recent breakthroughs—ranging from the Image Stitch Node in ComfyUI to low-precision quantization optimizations and the CometAPI API—have dramatically expanded the accessibility, performance, and creative potential of multi-image processing.

---

*Originally published at [https://www.cometapi.com/multi-image-reference-with-flux-1-kontext/](https://www.cometapi.com/multi-image-reference-with-flux-1-kontext/).*
