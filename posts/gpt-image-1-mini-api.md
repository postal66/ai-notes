<!-- social-ops-fingerprint:7af1914b84aaaf337ae463ab5af69af0688e3a4a0d14f6b4149e351a558058df -->
---
title: gpt-image-1-mini API
---
# gpt-image-1-mini API

![gpt-image-1-mini API](https://resource.cometapi.com/blog/uploads/2025/09/cometapi-key-guide-1024x527.webp)

**gpt-image-1-mini** is a *cost-optimized, multimodal image model* from OpenAI that accepts **text and image inputs** and produces **image outputs**. It is positioned as a smaller, cheaper sibling to OpenAI’s full GPT-Image-1 family — designed for high-throughput production use where cost and latency are important constraints. The model is intended for tasks such as **text-to-image generation**, **image editing / inpainting**, and workflows that incorporate reference imagery.

## Key features

- **Text→Image generation:** converts natural-language prompts into images with strong instruction following.
- **Image editing / inpainting:** accepts reference images and masks to perform targeted edits.
- **Cost-optimized (“mini”) design:** a smaller footprint that OpenAI and observers describe as much cheaper per image than the large model (OpenAI/DevDay messaging and early reports say ~80% less expensive).
- **Flexible output controls:** supports size, output format (JPEG/PNG/WEBP), compression and a quality knob (low/medium/high/auto in the cookbook).

## Technical details (architecture & capabilities)

- **Model family & input/output:** member of the **gpt-image-1** family; accepts **text prompts** and **image inputs** (for edits) and returns generated image outputs. **Quality/size** parameters control resolution (typical max ~1536×1024 in this family—see docs for exact supported sizes).
- **Operational tradeoffs:** engineered as a smaller footprint model—trades some top-end fidelity for **throughput and cost** improvements while preserving robust prompt-following and edit features.
- **Safety & metadata:** follows OpenAI’s image safety guardrails and embeds C2PA metadata options for provenance when available.

**Inputs & outputs** — canonical usage supports:

- **Text prompt** (string) to generate a new image.
- **Image + mask** to perform targeted edits/inpainting.
- **Reference images** to control style or composition.
  These are exposed via the Images API (model name `gpt-image-1-mini`).

## Limitations

- **Lower peak fidelity:** compared with the large gpt-image-1 model, mini may **lose some micro-detail and top-end photorealism** (expected tradeoff for cost).
- **Text rendering & tiny details:** like many image models, it can **struggle with small legible text**, dense charts, or micro-fine textures; expect to post-process or use higher-capacity models for those needs.
- **Edit scope:** image edit/inpainting features are available but suggest some **editing limitations** relative to interactive ChatGPT web tools—edits are effective for many tasks but may require iterative refinement.
- **Safety & policy constraints:** outputs are subject to OpenAI moderation/safety guardrails (explicit content, copyrighted content restrictions, disallowed outputs). Developers can control moderation sensitivity via API parameters where offered.

---

## Recommended use cases

- **High-volume content generation** (marketing assets, thumbnails, rapid concept art) — where **cost per image** is primary.
- **Programmatic editing / templating** — bulk inpainting or variant generation from a base asset.
- **Interactive applications with budget constraints** — chat interfaces or integrated design tools where response speed and cost matter more than absolute top fidelity.
- **Prototyping & A/B image generation** — generate many candidate images quickly and selectively upscale or re-run on larger models for finalists.

## How to call gpt-image-1-mini API from CometAPI

### **`gpt-image-1-mini`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Input Tokens | $2.00 |
| Output Tokens | $6.40 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first.
- Sign into your [CometAPI console](https://www.cometapi.com/console/token).
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.

![gpt-image-1-mini API](https://resource.cometapi.com/blog/uploads/2025/09/cometapi-key-guide-1024x527.webp)

### Use Method

1. Select the “gpt-image-1-mini” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to [image generation](https://apidoc.cometapi.com/images-generations):

- **Base URL:** `https://api.cometapi.com/v1/images/generations`
- **Model Names:** gpt-image-1-mini
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

`https://apidoc.cometapi.com/image-edits`: `https://api.cometapi.com/v1/images/edits`

**See Also** [GPT-image-1 API](https://www.cometapi.com/gpt-image-1-api/)

---

*Originally published at [https://www.cometapi.com/gpt-image-1-mini-api/](https://www.cometapi.com/gpt-image-1-mini-api/).*
