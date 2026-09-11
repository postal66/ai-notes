<!-- social-ops-fingerprint:f9d8232d429d414eaee30e132fbc2ddacc4093e3997614a44c5c10681d95fe67 -->
---
title: Qwen-image-edit API
---
# Qwen-image-edit API

![Qwen-image-edit API](https://resource.cometapi.com/blog/uploads/2025/11/qwen-image-1024x589.webp)

Qwen-Image-Edit is the editing branch of the Qwen image family developed by the Qwen team (Alibaba / QwenLM ecosystem). It is built on a 20-billion-parameter MMDiT backbone and explicitly extends Qwen-Image’s advanced text-rendering capabilities into robust image-editing workflows. The model is intended for tasks where editing fidelity matters — e.g., directly changing text on signs, preserving fonts and layout, adding/removing objects while keeping semantic consistency, viewpoint/pose transforms, and fine-grained style transfers.

## Key features

- **Precise in-image text editing (bilingual: Chinese & English)** — add, remove or replace text while preserving font/size/style as much as possible.
- **Dual editing modes: semantic + appearance** — supports high-level semantic changes (repose, object replacement, viewpoint) and low-level appearance edits (style transfer, texture, local retouching).
- **Mask / region / multi-turn edits** — supports masked inpainting, region prompts and chained edits for iterative refinement workflows.
- **Multi-image inputs (latest version):** the 2509 iteration adds multi-image editing support (e.g., person+person, person+product), improved identity/product/text consistency and native ControlNet-style inputs.

## Technical details

- **Base scale / family:** built on the **20B parameter** Qwen-Image foundation model (MMDiT style diffusion / multimodal design).
- **Dual-encoding editing pipeline:** the edit module receives (1) a semantic representation via a Qwen2.5-VL visual encoder and (2) a reconstructive representation via a VAE encoder. Feeding both representations in parallel enables the edit head to trade off semantic change vs. pixel fidelity. This dual-encoding is a core engineering choice for robust edits.
- **Progressive / curriculum training:** training progressed from simpler text rendering and generation tasks to complex paragraph-level text rendering and multi-task editing objectives (T2I, TI2I, I2I reconstruction). This curriculum is reported to be a central factor in the model’s improved text fidelity and editing stability.
- **Model flavor / modules:** Qwen-Image-Edit is described as an MMDiT-style 20B model that integrates Qwen2.5-VL components, a diffusion editing head, and VAE components for appearance control.

## Benchmark performance

**Claimed cross-benchmark SOTA:** the Qwen team reports state-of-the-art (SOTA) or top-tier results on multiple public image generation and editing benchmarks — including *GenEval, DPG, OneIG-Bench* (generation) and *GEdit, ImgEdit, GSO* (editing).

![Qwen-image-edit API](https://resource.cometapi.com/blog/uploads/2025/11/qwen-image-1024x589.webp)

## Limitations & caveats (practical)

1. **Artifacts & edge cases:** community testing shows occasional over-saturation, skin texture artifacts, or compositing seams in some high-detail edits; community lightning forks aim to mitigate these.
2. **Compute / memory:** the 20B model and full-precision editing pipelines are GPU-intensive. Local deployment benefits from bfloat16/FP8 and optimized sampling workflows (4/8 step “lightning” variants exist to reduce VRAM and latency).
3. **Safety & IP:** as with all general-purpose imagers, Qwen-Image-Edit can generate copyrighted characters or sensitive content — production use requires moderation controls and rights clearance. (Typical enterprise best practice.)
4. **Failure modes:** obscure or very rare characters/words may still be rendered incorrectly or require iterative (“chained”) edits to converge (authors note examples like rare Chinese glyphs requiring stepwise corrections).

## How Qwen-Image-Edit compares with other options

- **Stable Diffusion / SDXL (inpainting):** SDXL plus ControlNet and dedicated inpainting pipelines are fast, have broad community tool support and many LoRAs; they excel at general inpainting workflows and speed/efficiency. Qwen-Image-Edit’s strengths are *native bilingual text editing*, tighter identity/product consistency in some cases, and integrated semantic+appearance tradeoffs. Community comparisons show Qwen often ranks higher in editing fidelity and text adherence but at higher compute cost.
- **Closed-source editors (Adobe Firefly / DALL·E / Runway):** closed APIs can be very polished (UI, integrated moderation, latency guarantees), but Qwen-Image-Edit stands out as a fully open alternative that specifically targets robust bilingual text editing and offers local deployment. Practical choice often depends on whether you need local control / open licensing or polished cloud UX.

## Practical use cases

- **Poster & signage edits** — change text on posters while preserving font/texture.
- **Product marketing / poster generation** — add/remove items, maintain product identity for e-commerce images.
- **Portrait identity-preserving edits** — pose changes, style transfers while keeping identity consistent (improved in 2509).
- **Restoration & calligraphy correction** — old photo restoration and stepwise correction of handwritten/printed characters.
- **Creative/Design workflows** — multi-image composition edits, meme generation, avatar styling where bilingual text may be involved.

## How to call qwen-image-edit API from CometAPI

### **`qwen-image-edit`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Input Tokens | $2.00 |
| Output Tokens | $6.40 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first.
- Sign into your [CometAPI console](https://www.cometapi.com/console/token).
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.

![Qwen-image-edit API](https://resource.cometapi.com/blog/uploads/2025/09/cometapi-key-guide-1024x527.webp)

### Use Method

1. Select the “qwen-image-edit” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to `https://apidoc.cometapi.com/image-edits`:

- **Base URL:** `https://api.cometapi.com/v1/images/edits`
- **Model Names:** qwen-image-edit
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

**See also [Qwen-image API](https://www.cometapi.com/qwen-image-api/)**

---

*Originally published at [https://www.cometapi.com/qwen-image-edit-api/](https://www.cometapi.com/qwen-image-edit-api/).*
