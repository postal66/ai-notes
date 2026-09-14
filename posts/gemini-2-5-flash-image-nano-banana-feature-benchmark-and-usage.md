<!-- social-ops-fingerprint:66522bc359faf8c9e5206b3251b9855e216d0cdaeed8e6c77687c0b5006c525b -->
---
title: Gemini 2.5 Flash Image(Nano Banana): Feature, Benchmark and Usage
---
# Gemini 2.5 Flash Image(Nano Banana): Feature, Benchmark and Usage

![Gemini 2.5 Flash Image(Nano Banana): Feature, Benchmark and Usage](https://resource.cometapi.com/blog/uploads/2025/09/Gemini-2.5-Flash-ImageNano-Banana-Feature-Benchmark-and-Usage.webp)

In late August 2025 Google (DeepMind) released *Gemini 2.5 Flash Image* — widely nicknamed **“nano-banana”** — a low-latency, high-quality image generation + editing model that’s been integrated into the Gemini app, Google AI Studio, the Gemini API and CometAPI. It’s designed to produce photorealistic images, preserve character consistency across edits, fuse multiple input images, and perform fine, localized edits through natural-language prompts. The model is available in preview / early GA and is already topping image leaderboards (LMArena) while shipping with safety mechanisms (SynthID watermarking and product-level filters).

## What is Gemini 2.5 Flash Image (aka “Nano Banana”)?

Gemini 2.5 Flash Image — playfully nicknamed **Nano Banana** — is Google DeepMind’s latest image generation and editing model in the Gemini family. Announced in late August 2025, the model is positioned as a preview release that brings higher-fidelity edits, multi-image fusion, better character consistency (keeping the same person/pet/object recognizable across multiple edits), and low-latency image generation into Gemini’s multimodal toolset. It’s available through the Gemini API, Google AI Studio, the Gemini mobile/web apps, and Vertex AI for enterprise customers.

### Origin and naming

The “nano banana” nickname became a viral shorthand on social feeds and community leaderboards after early testers and LMArena entries used a fruit-themed label; Google confirmed the connection and embraced the playful handle publicly in their developer and product posts. The official product name is **Gemini 2.5 Flash Image** and you’ll typically see the model identifier used in code and API calls (for preview usage it appears as e.g. `gemini-2.5-flash-image-preview`).

## What are the headline features of Gemini 2.5 Flash Image?

### What does “character consistency” actually mean?

One of the marquee capabilities is **character consistency**: you can ask the model to reuse the same subject (a person, pet, mascot, or product) across many edits or new scenes while preserving identifying visual features (face/shape, color palette, distinguishing marks). This addresses a common weakness in earlier image models where subsequent edits would produce visually plausible but noticeably different people/objects. Developers can therefore build workflows for product catalogs, episodic storytelling, or brand asset generation with less manual correction.

### What other editing controls are included?

Gemini 2.5 Flash Image supports:

- **Targeted local edits** via plain-language prompts (remove an object, change outfit, retouch skin, remove background element).
- **Multi-image fusion**: combine up to three input images into a single coherent composition (e.g., put a product from image A into scene B while preserving lighting).
- **Style and format controls**: photorealistic instructions, camera and lens attributes, aspect ratio, and stylized outputs (illustration, sticker, etc.).
- **Native world knowledge**: the model leverages the broader Gemini family’s knowledge to do semantically-aware edits (e.g., understand what “Renaissance lighting” or “Tokyo crosswalk” implies).

### What about speed, cost, and availability?

Gemini 2.5 Flash Image is part of the Flash tier of Gemini 2.5—optimized for low latency and cost while keeping strong quality. Google has previewed pricing for image output tokens and provided availability via API and AI Studio; enterprise customers can access it via Vertex AI.At announcement the published pricing for the Gemini 2.5 Flash Image tier was **$30 per 1M output tokens**, with an example per-image cost reported as **1290 output tokens ≈ $0.039 per image**.

## How does Gemini 2.5 Flash Image work under the hood?

### Architecture and training approach

Gemini 2.5 Flash Image inherits the Gemini 2.5 family architecture: a sparse mixture-of-experts (MoE) style backbone with multimodal training that combines text, image, audio, and other data. Google trained Flash Image on very large, filtered multimodal corpora and fine-tuned the model for the image tasks (generation, editing, fusion) and safety behavior. Training was run on Google’s TPU fabric and evaluated with both automatic and human judgement metrics.

### Conversation-driven editing

At a high level, the model uses contextual conditioning: when you provide an image (or multiple images) plus text prompts, the model encodes the visual identity of the subject into its internal representation. During subsequent edits or new scenes, it conditions generation on that representation so desired visual attributes (face geometry, key clothing or product identifiers, color palettes) are preserved. In practical terms this is implemented as part of the multimodal content pipeline exposed by the Gemini API: you send the reference images together with editing instructions and the model returns edited image outputs (or multiple candidate images) in one response.

### Watermarking & provenance

Google integrates safety and content-policy filters into Gemini 2.5 Flash Image. The release emphasizes evaluation and red-teaming, automated filtering steps, supervised fine-tuning and reinforcement learning for instruction following while minimizing harmful outputs. Outputs include an invisible SynthID watermark so images produced or edited by the model can be later identified as AI-generated.

## How well does it perform? (Benchmark data)

Gemini 2.5 Flash Image (marketed as “nano-banana” in some benchmarking contexts) reached **#1 on LMArena’s Image Edit and Text-to-Image leaderboards** as of late August 2025, with large Elo / preference leads over competitors in the reported comparisons. I reference LMArena and GenAI-Bench human evaluation results showing top preference scores for both text-to-image and image-editing tasks.

### Text-to-Image Comparision

| Capability Benchmark | Gemini Flash 2.5 Image | Imagen 4 Ultra 06-06 | ChatGPT 4o / GPT Image 1 (High) | FLUX.1 Kontext | Gemini Flash 2.0 Image |
| --- | --- | --- | --- | --- | --- |
| Overall Preference (LMArena) | 1147 | 1135 | 1129 | 1075 | 988 |
| Visual Quality (GenAI-Bench) | 1103 | 1094 | 1013 | 864 | 926 |
| Text-to-Image Alignment (GenAI-Bench) | 1042 | 1053 | 1046 | 937 | 922 |

### Image Editing

| Capability Benchmark | Gemini Flash 2.5 Image | ChatGPT 4o / GPT Image 1 (High) | FLUX.1 Kontext | Qwen Image Edit | Gemini Flash 2.0 Image |
| --- | --- | --- | --- | --- | --- |
| Overall Preference (LMArena) | 1362 | 1170 | 1191 | 1145 | 1093 |
| Character | 1170 | 1059 | 1010 | 911 | 850 |
| Creative | 1112 | 1057 | 968 | 983 | 879 |
| Infographics | 1067 | 1029 | 967 | 1012 | 925 |
| Object / Environment | 1064 | 1023 | 1002 | 1010 | 901 |
| Product Recontextualization | 1128 | 1032 | 943 | 1009 | 888 |
| Stylization | 1062 | 1165 | 949 | 1091 | 733 |

![Gemini 2.5 Flash Image(Nano Banana): Feature, Benchmark and Usage](https://resource.cometapi.com/blog/uploads/2025/08/gemini-image__image-editing__no_product-reconte.original-1024x576.webp)

### What do these benchmarks mean in practice?

Benchmarks tell us two things: (1) the model is competitive at photorealistic generation and (2) it stands out in **editing** tasks where character consistency and prompt adherence matter. Human preference rankings indicate that users viewing outputs rated Gemini’s outputs highly for realism and alignment with instructions in many evaluated prompts. However, explicit about known limitations (hallucination risk on fine factual details, long-form text rendering inside images, style transfer edge cases) — so benchmarks are a guide, not a guarantee.

Gemini 2.5 Flash Image is explicitly built for creative, productivity, and applied-imaging scenarios. Typical and emergent use cases include:

### Rapid product mockups and e-commerce

Drag product photos into scenes, generate consistent catalog imagery across environments, or swap colors/fabrics across a product line — all while preserving the product’s identity. The multi-image fusion features and character/product consistency make it attractive for catalog workflows.

### Photo retouching and targeted edits

Remove objects, fix blemishes, change clothing/accessories, or tweak lighting with natural-language prompts. The localized edit capability lets non-experts perform professional-style retouching using conversational commands.

### Storyboarding and visual storytelling

Place the same character across different scenes and keep their look consistent (useful for comics, storyboards, or pitch decks). Iterative edits let creators refine mood, framing, and narrative continuity without rebuilding assets from scratch.

### Education, diagrams, and design prototyping

Because it can combine text prompts and images and has “world knowledge,” the model can help generate annotated diagrams, educational visuals, or quick mockups for presentations. Google even highlights templates in AI Studio for use cases like real estate mockups and product design.

## How do you use Nano Banana API ?

Below are practical snippets adapted from [CometAPI API docs](https://apidoc.cometapi.com/guide-to-calling-gemini-2-5-flash-image-1425263m0) and Google’s API docs. They demonstrate the common flows: **text-to-image** and **image + text to image (editing)** using the official GenAI SDK or REST endpoint.

> Note: in CometAPI’s docs the preview model name appears as `gemini-2.5-flash-image-preview`. The examples below echo the official SDK examples (Python and JavaScript) and a REST curl example; adapt keys and file paths to your environment.

### REST curl example from CometAPI

Use Gemini’s official `generateContent` endpoint for text-to-image generation. Place the text prompt in `contents.parts[].text`.**Example (Windows shell, using `^` for line continuation):**

```
curl --location --request POST "https://api.cometapi.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent" ^
--header "Authorization: sk-xxxx" ^
--header "User-Agent: Apifox/1.0.0 (https://apifox.com)" ^
--header "Content-Type: application/json" ^
--header "Accept: */*" ^
--header "Host: api.cometapi.com" ^
--header "Connection: keep-alive" ^
--data-raw "{    "contents": [{
      "parts": [
        {"text": "A photorealistic macro shot of a nano-banana on a silver fork, shallow depth of field"}
      ]
    }]
  }'}"
| grep -o '"data": "*"' \
| cut -d'"' -f4 \
| base64 --decode > gemini-generated.png
```

The response contains base64 image bytes; the pipeline above extracts the `"data"` string and decodes it into `gemini-generated.png`.

This endpoint supports “image-to-image” generation: upload an input image (as Base64) and receive a modified new image (also in Base64 format).**Example:**

```
curl --location --request POST "https://api.cometapi.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent" ^
--header "Authorization: sk-xxxx" ^
--header "User-Agent: Apifox/1.0.0 (https://apifox.com)" ^
--header "Content-Type: application/json" ^
--header "Accept: */*" ^
--header "Host: api.cometapi.com" ^
--header "Connection: keep-alive" ^
--data-raw "{  \"contents\":     }  ],  \"generationConfig\": {    \"responseModalities\":   }}"
```

\*\*Description:\*\*First, convert your source image file into a Base64 string and place it in `inline_data.data`. Do not include prefixes like `data:image/jpeg;base64,`.The output is also located in `candidates.content.parts` and includes:An optional text part (description or prompt).The image part as `inline_data` (where `data` is the Base64 of the output image).For multiple images, you can append them directly, for example:

```
{
  "inline_data": {
    "mime_type": "image/jpeg",
    "data": "iVBORw0KGgo...",
    "data": "iVBORw0KGgo..."
  }
}
```

Below are developer examples adapted from Google’s official docs and blog. Replace credentials and file paths with your own.

### Python (official SDK style)

```
from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client()

prompt = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"

# Text-to-Image

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=,
)

for part in response.candidates.content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")
```

This is the canonical Python snippet from Google’s docs (preview model ID shown). The same SDK call pattern supports image + prompt editing (pass an image as one of the `contents`).More details refer to [gemini doc.](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)

## Conclusion

If your product needs robust, low-latency image generation and, especially, **reliable editing with subject consistency**, Gemini 2.5 Flash Image is now a production-grade option worth evaluating: it combines state-of-the-art image quality with APIs designed for developer integration (AI Studio, Gemini API, and Vertex AI). Carefully weigh the model’s current limitations (fine text in images, some stylization edge cases) and implement responsible-use safeguards.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access [Gemini 2.5 Flash Image](https://www.cometapi.com/gemini-2-5-flash-image/)(Nano Banana CometAPI list `gemini-2.5-flash-image-preview/gemini-2.5-flash-image` style entries in their catalog.) through CometAPI, the latest models version listed are as of the article’s publication date. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/gemini-generates-image-20873272e0) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

---

*Originally published at [https://www.cometapi.com/gemini-2-5-flash-imagenano-banana-feature-benchmark-and-usage/](https://www.cometapi.com/gemini-2-5-flash-imagenano-banana-feature-benchmark-and-usage/).*
