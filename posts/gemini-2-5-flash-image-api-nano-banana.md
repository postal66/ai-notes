<!-- social-ops-fingerprint:935b0e87790f1e5d803eed28d02493f6b028659e14ee086cc9f214548164439a -->
---
title: Gemini 2.5 Flash Image API (Nano-Banana)
---
# Gemini 2.5 Flash Image API (Nano-Banana)

![Gemini 2.5 Flash Image API (Nano-Banana)](https://resource.cometapi.com/blog/uploads/2025/08/gemini-image__image-editing__no_product-reconte.original-1024x576.webp)

Gemini 2.5 Flash Image (aka “Nano banana” ) is Google’s newest native image generation + editing model in the Gemini 2.5 family. It focuses on multi-image fusion, precise natural-language edits, and fast multimodal workflows.

## Introduction to the model

**What it is —** *Gemini 2.5 Flash Image* is a multimodal image generation and editing model built on the Gemini 2.5 family. It’s designed to produce **photorealistic images**, perform **targeted edits** (inpainting, style transfer, object swaps), and **blend multiple source images** into a single coherent output — while applying Gemini’s improved language reasoning to control composition and semantics.

## Key features

- **Native image generation & editing** — generate images or edit existing photos via natural-language prompts. **(Generate / Edit)**.
- **Multi-image fusion** — combine multiple input images into one photorealistic scene.
- **Character consistency** — keep the same subject or character appearance across edits and prompts. **(Consistency)**.
- **SynthID watermarking** — all outputs include an **invisible SynthID** to identify AI-generated content. **(Watermark)**.

## Technical details

- **Architecture & positioning:** built on the Gemini 2.5 Flash family — designed as a **low-latency** “Flash” variant that trades a little model size/throughput for much faster per-call response and cost efficiency while retaining stronger reasoning than earlier Flash tiers.
- **Input formats & limits:** accepts **inline base64 images** for small inputs and **file uploads** via the File API for larger images (recommended for >20 MB). Supports common MIME types (JPEG, PNG).
- **Modes of operation:** text-to-image, image editing (inpainting / semantic masking), style transfer, multi-image composition, and **interleaved** text+image responses (useful for illustrated instructions, recipes, or mixed content).
- **Provenance & safety mechanisms:** visible watermarks on AI outputs plus hidden SynthID markers and policy enforcement layers to limit explicit disallowed content.

## Benchmark performance

![Gemini 2.5 Flash Image API (Nano-Banana)](https://resource.cometapi.com/blog/uploads/2025/08/gemini-image__image-editing__no_product-reconte.original-1024x576.webp)

## Limitations & known risks

- **Content policy constraints:** models enforce content policies (e.g., disallowing explicit sexual content and some illicit content), but enforcement is not perfect — generating images of public figures or controversial icons may still be possible in some scenarios, so **policy checks are essential**. )
- **Failure modes:** possible **identity drift** in extreme edits, occasional semantic misalignment (when prompts are under-specified), and artifacts in very complex scenes or extreme viewpoint changes.
- **Provenance & misuse:** while watermarks and SynthID are present, these do not prevent misuse — they assist detection and attribution but are not a substitute for human review in sensitive workflows.

## Typical use cases

- **Product & ecommerce:** *place/catalog products into lifestyle shots* via multi-image fusion.
- **Creative tooling / design:** *fast iterations* in design apps (Adobe Firefly integration cited).
- **Photo editing & retouching:** *localized edits from natural language* (remove objects, change color/lighting, restyle).
- **Storytelling / character assets:** *keep characters consistent* across panels and scenes.

## How to call **Gemini 2.5 Flash Image** API from CometAPI

### **`Gemini 2.5 Flash Image`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Price | $0.3120 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`Gemini-2.5 Flash-Image`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to  [API doc](https://apidoc.cometapi.com/chat-13851472e0):

- **Endpoint:** `https://api.cometapi.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent`
- **Model Parameter:** gemini-2.5-flash-image-preview / gemini-2.5-flash-image
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY`
- **Content-Type:** `application/json` .

Note: When invoking the API, set the parameter “stream”: true.

```
curl --location --request POST 'https://api.cometapi.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent' \
--header 'Authorization: sk-xxx' \
--header 'User-Agent: Apidog/1.0.0 (https://apidog.com)' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--header 'Host: api.cometapi.com' \
--header 'Connection: keep-alive' \
--data-raw '{
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": "cat"
                },
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
						"data": "iVBORw0KGgoA Note: Base64 data here"
						}

            ]
        }
    ],
    "generationConfig": {
        "responseModalities": [
            "TEXT",
            "IMAGE"
        ]
    }
}'
```

**See Also** **[GPT-image-1 API](https://www.cometapi.com/gpt-image-1-api/)**

---

*Originally published at [https://www.cometapi.com/gemini-2-5-flash-image/](https://www.cometapi.com/gemini-2-5-flash-image/).*
