<!-- social-ops-fingerprint:bfed1cd40d75c5313b7839c89b4f2fed58c85226c1f011e3e2464e0132db581b -->
---
title: Gemini 3 Pro Image( Nano Banana Pro) API
---
# Gemini 3 Pro Image( Nano Banana Pro) API

![Gemini 3 Pro Image( Nano Banana Pro) API](https://resource.cometapi.com/blog/uploads/2025/11/7-Nano-Banana-Pro-Prompts-that-You-Should-to-Try-710x399.webp)

Google’s *Nano Banana Pro* (official model id **`gemini-3-pro-image-preview`**) is the image-generation / image-editing variant of Gemini 3 Pro. It’s a preview-stage, professional-grade image model that adds 2K/4K output, high-fidelity multi-image composition (up to **14 reference images**, character consistency for **up to 5 people**), stronger text-in-image rendering, and search grounding for real-world factuality.

## Basic features

- **Text → Image**: full prompt-driven generation with strong prompt adherence.
- **Image → Image (edits)**: fine, targeted edits with maintained subject/character consistency across multiple edits.
- **Maximum output resolution:** up to **4K** (examples and supported exact pixel sizes depend on aspect ratio; the API exposes 1K/2K/4K presets)
- **Iterative planning & self-correction**: an internal “multi-stage” pipeline that detects and corrects common visual mistakes (perspective, text, fine geometry).
- **Advanced in-image text rendering**: clear, legible multi-language text (short captions to long paragraphs) suitable for posters, mockups, and infographics.
- **5 characters** and fidelity for up to **14 objects/reference images** in a single workflow.
- **Watermarking / provenance:** all generated images include a SynthID watermark; model embeds C2PA metadata for provenance in some product integrations.

## Gemini 3 Pro Image versions & naming

- `gemini-3-pro-image-preview`
- `gemini-3-pro-image`

---

## Technical details

### Architecture

- **Lineage / backbone**: Nano Banana Pro be built on Google’s evolving Gemini image stack — specifically the new **Gemini 3 Pro Image / GEMPIX 2** architecture (a higher-capacity multimodal image+text framework). That is an evolution from **Gemini 2.5 Flash Image** (the original “nano-banana”) into a natively multimodal image model with expanded vision-language reasoning capabilities.
- **Model behavior**: native multimodality (image + text + world knowledge), explicit pipelines for multi-image fusion, and an internal staged planner that refines outputs over multiple passes rather than producing a single static sample. Early reports indicate stronger geometric/optical reasoning (glass, refraction) versus prior versions.
- **Thinking / internal refinement**: The model uses a visible “thinking” process internally to refine composition (the API documents this behavior and notes those internal steps are not charged as final image tokens).
- **Grounding & tools**: Supports **Search grounding** (can incorporate web facts into diagram/infographic generation). It also supports system instructions for more deterministic control.

### Key API parameters:

- *`thinking_level`* (low / high) to trade latency vs reasoning depth;
- *`media_resolution`* (low/medium/high) to control image OCR/detail reading tokens;
- *`generationConfig.imageConfig`* to control aspect ratio/resolution in image outputs.

### Image limits:

- **Input modalities supported:** Text and images (the model does not accept audio or video as image-generation inputs).
- **Max images per prompt:** 14 (for the Gemini 3 Pro Image preview).
- **Max image size (upload):** 7 MB per input image.
- **Supported aspect ratios:** 1:1, 3:2, 16:9, 9:16, 21:9, etc.

**Output images / tokens:** high limits, with 4K/4096px supported.

## Benchmark performance

> **Short summary:** public/early benchmarks so far are mostly qualitative / community-driven, but consistently report substantial improvements in resolution, artifact reduction, and physical fidelity versus the original nano-banana (Gemini 2.5 Flash Image). Specific named “challenges” have shown clear visual gains, but there are not yet (public) standardized numeric benchmark tables from Google comparing v1 → v2 across standard image-generation metrics.

- **Qualitative community tests**: Cleaner edges, sharper micro-details, truer colors, and more faithful prompt adherence (fewer hallucinated props, more consistent characters). Popular informal tests include the so-called “Wine Glass Test” and “Glass Burger Challenge”, where GEMPIX2 (Nano Banana Pro) handles transparency and refraction markedly better than earlier builds.
- **Text handling**: Nano Banana Pro shows visibly improved typography and text placement inside images (a persistent weakness for many image models). Community comparisons indicate fewer garbled rendered glyphs.
- **Throughput / UX**: faster iteration speed and a UX that performs multi-stage refinement on the back end so users see more reliable first-pass results (reducing manual re-rolls).

## Limitations & risks

- **Content filters & detection**: Platforms integrating the model (e.g., Whisk/third-party apps) may enable strict celebrity or likeness detection and block certain outputs, which affects creative workflows that rely on realistic celebrity likenesses.
- **Hallucination / reasoning edge cases**: while improved, the model can still produce physically unrealistic artifacts, especially with dense symbolic text inside images or highly technical diagrams — though NB2 appears to reduce these errors versus earlier versions.
- **Safety & misuse:** generative image models can be used to create problematic or harmful content. Google applies constraints, content filters, and the SynthID watermark to help with provenance; nevertheless, misuse has occurred (high-profile controversy tied to a Nano Banana generated image in a politically sensitive setting).

## How Nano Banana Pro stacks up vs other models

- **Nano Banana Pro (GEMPIX 2 / Gemini 3 Pro Image)** — strong mobile integration, multi-image fusion, iterative self-correction, 2K native/4K upscaling, tightly integrated into Google apps (Search, Photos, Workspace/Gemini). Best for workflows that need reliable edits, continuity, and integration with Google services.
- **Midjourney** — excels at stylized artistic outputs and community-driven prompt engineering; not typically targeted at photo-accurate multi-image fusion or deep multimodal editing pipelines.
- **Stable Diffusion / open weights** — fully open, highly customizable, and hostable locally; ecosystem of checkpoints and fine-tuning is a decisive advantage for research and offline usage. Less “one-click” mobile integration and less consistent multi-image editing coherence out-of-the-box than Nano Banana Pro.
- **Seedream 4.0 (ByteDance)** — recently positioned explicitly as a Nano Banana competitor, emphasizing ultra-fast rendering, 2K output, and support for many reference images (up to six). Positioned as a pro/creator alternative.

(These comparisons are high level; pick a winner by matching the tool to your workflow: openness/customizability → Stable Diffusion; stylized art → Midjourney; integrated, consistent mobile editing with aggressive iteration → Nano Banana Pro/ Gemini 3 Pro image family.)

---

## Real-world use cases

- **Mobile photo editing & creative filters** (Google Photos integrations — restyling, background fusion, portrait recomposition).
- **Marketing & ad assets** — fast concept generation, consistent brand characters across multiple frames/angles.
- **Concept art & storyboarding** — multi-image fusion helps keep character continuity across panels.
- **E-commerce / product mockups** — generate consistent product shots in different contexts/lighting conditions.
- **Rapid prototyping for AR/VR assets** — high quality 2K/4K outputs that can be upscaled for immersive uses.

## How to call gemini-3-pro-image(**Nano Banana Pro)**  API

### Nano Banana API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Price | $0.19200 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`gemini-3-pro-image`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details  :

- **Base URL:** <https://api.cometapi.com/v1beta/models/gemini-3-pro-image-preview:generateContent>
- **Model Names:** `gemini-3-pro-image`
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

**See also [Gemini 2.5 Flash Image API (Nano-Banana)](https://www.cometapi.com/gemini-2-5-flash-image/)**

---

*Originally published at [https://www.cometapi.com/gemini-3-pro-image-nano-banana-2-api/](https://www.cometapi.com/gemini-3-pro-image-nano-banana-2-api/).*
