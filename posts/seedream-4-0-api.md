<!-- social-ops-fingerprint:1771ce61594cb2d971a728902d980e169f8e23e5d7f7298e6e697faef8d3d8ac -->
---
title: Seedream 4.0 API
---
# Seedream 4.0 API

![Seedream 4.0 API](https://resource.cometapi.com/blog/uploads/2025/08/bytedance-logo-png_seeklogo-471468-1.webp)

Seedream 4.0 (model identifier **bytedance-seedream-4-0-250828**) is ByteDance’s newest *image-creation* foundation model that unifies **text→image generation** and **image editing** in a single architecture. The model was announced in early September 2025 and is positioned for high-resolution (up to **4K**) generation, multi-reference workflows, and fast inference for production use.

## Key features

- **Unified generation + editing** — one model handles both *text-to-image* and *image-to-image* ,Image editing, multi-image editing, group image generation and other creative modes workflows.
- **High resolution** — supports outputs up to **4K** and multiple aspect ratios.
- **Multi-reference / group generation** — accepts multiple reference images and can create consistent sets of images.
- **Faster inference** — ByteDance claims substantially faster inference than prior Seedream versions (and improved latency for editing tasks).
- **Production ergonomics** — features such as text rendering, layout/diagram generation, and prompt-based fine edits (change text, remove objects) are emphasized for real workflows.

## Technical details

- Architecture: Seedream 4.0 using a *Mixture-of-Experts (MoE)* style architecture and other efficiency optimizations to boost throughput and lower per-image cost in production deployments. This change is framed as the principal reason for the model’s claimed ten-fold speed-up vs prior releases.
- **Inputs & formats:** supports standard image formats (JPEG/PNG), aspect ratios across square/portrait/landscape and both **text prompt** and **one-or-multi-image references** as input.

## Benchmark performance

ByteDance reports high scores on **prompt adherence**, **alignment (editing fidelity)** and **aesthetics** in its internal benchmark called **MagicBench**; the company says Seedream 4.0 outperformed earlier Seedream releases and—by their internal ELO comparisons—competes favorably with Google’s Gemini 2.5 Flash Image (“Nano Banana”). Seedream 4.0 is particularly strong at **prompt-following** and **edit fidelity** (i.e., it tends to respect user edit instructions and preserve reference content)

![Seedream 4.0](https://resource.cometapi.com/blog/uploads/2025/09/seedream-4.0-data-1024x428.webp)

## Typical use cases

- **Marketing & creative production** — posters, banners, social graphics where layout, typography, and repeatable edits matter.
- **Rapid prototyping for design** — multi-reference conditioning allows designers to fuse brand assets with new compositions.
- **Batch content generation** — product imagery variants, campaign A/B assets, and multi-shot consistent scenes.
- **Image editing workflows** — precise “change X but keep Y” natural language edits for localization or last-mile creative adjustments.

## How to call Seedream 4.0 API from CometAPI

### **`Seedream 4.0`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Price | $0.02400 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`bytedance-seedream-4-0-250828`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to `seedream image`  [API doc](https://apidoc.cometapi.com/bytedance-image-generationseedream-19773064e0):

- **Endpoint:** `https://api.cometapi.com/v1/images/generations`
- **Model Parameter:** `bytedance-seedream-4-0-250828`
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY`
- **Content-Type:** `application/json` .

```
curl
--location
--request POST 'https://api.cometapi.com/v1/images/generations' \
--header 'Authorization: Bearer {{api-key}}' \ --header 'Content-Type: application/json' \
--data-raw
'{
"model": "bytedance-seedream-4-0-250828",
"prompt": "Generate a close-up image of a dog lying on lush grass.",
"image":"https://filesystem.site/cdn/20250414/chxiLc2O45zoLT8BCrQ6WQlTvGDDnK.png",
"sequential_image_generation": "disabled", "response_format": "url", "size": "2K", "stream": false, "watermark": true }'
```

**See Also [Gemini 2.5 Flash Image API (Nano-Banana)](https://www.cometapi.com/gemini-2-5-flash-image/)**

---

*Originally published at [https://www.cometapi.com/seedream-4-0-api/](https://www.cometapi.com/seedream-4-0-api/).*
