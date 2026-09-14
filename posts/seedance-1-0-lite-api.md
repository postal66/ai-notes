<!-- social-ops-fingerprint:3b62ab332cc5f35f06875b9bb3408b4690002fd08ae91c938decd2b63f02cf8e -->
---
title: Seedance 1.0 Lite API
---
# Seedance 1.0 Lite API

![Seedance 1.0 Lite API](https://resource.cometapi.com/blog/uploads/2025/08/bytedance-logo-png_seeklogo-471468-1.webp)

ByteDance has officially rolled out **Seedance 1.0 Lite**, a streamlined edition of its flagship video‐generation framework. this new model balances speed, cost-efficiency, and quality—making advanced AI‐powered video creation accessible to a broader audience.

## Introduction to Seedance 1.0 Lite

**Seedance 1.0 Lite** is a **diffusion-based** Text-to-Video and Image-to-Video model optimized for **rapid**, **flexible**, and **budget-friendly** workflows. Built by ByteDance—the team behind TikTok and CapCut—it inherits core breakthroughs in **semantic understanding** and **prompt fidelity** from the full Seedance 1.0 framework while operating at a fraction of the compute cost.

### Features

**Seedance 1.0 Lite** is engineered for **short-form** video clips (5–10 seconds) with support for both **text → video** and **image → video** workflows. Key **features** include:

- **Dual-mode Generation**: Supports both **Text-to-Video** and **Image-to-Video** pipelines, enabling users to transform prompts or still images into dynamic clips .
- **Aspect-Ratio Adaptivity**: Automatically adjusts to **16:9**, **9:16**, and square formats for social media, presentations, or web embeds.
- **Multi-Resolution Support**: Offers **480p**, **720p**, and **1080p** output, with durations of **5s** or **10s** per generation cycle .**Stable Motion**: Delivers **coherent spatiotemporal fluidity**, reducing frame jitter even in dynamic scenes.
- **Stylized Outputs**: Accurately interprets prompts ranging from **anime** and **claymation** to **cyberpunk** and **oil painting**, without extensive fine-tuning .
- **Cost-Effective**: Optimized inference stack means **lower compute costs**, ideal for A/B testing and social media content creation.

### Model Version:

Text video: bytedance-seedance-1-0-lite-t2v-250428

Photo video: bytedance-seedance-1-0-lite-i2v-250428

## Technical Details

- **Model Architecture**: Leverages a **diffusion backbone** tailored for **fast sampling**, with optimizations that reduce jitter and maintain **smooth motion** across complex scenes .
- **Lite-Scale Optimizations**: Prunes non-critical layers and quantizes weights to achieve up to **2× faster** inference compared to the full Seedance 1.0, trading minimal quality for significant speed gains .
- **Prompt Parsing**: Implements ByteDance’s proprietary **DiT**-inspired encoder to parse **natural language** prompts, supporting **multi-agent interactions**, dynamic camera cues, and style modifiers.

## Benchmark Performance

Empirical evaluations position Seedance 1.0 Lite as a **top contender** among lightweight video models:

- **Inference speed**: ~3 seconds per frame at 720 p on a single NVIDIA L20 GPU (≈0.18 s per 24 fps frame).
- **Visual fidelity**: Achieves **Structural Similarity Index (SSIM)** scores of 0.87 on standard video testsets, outperforming comparable models like RunwayML’s Gen-V2 and Synthesia’s V-Lite by 5–7% .
- **Prompt adherence**: Scored 4.3/5.0 in human evaluations for semantic alignment, indicating strong **prompt comprehension** even in multi-subject scenes.
- **Cost-efficiency**: With per-clip pricing at $0.18, Seedance 1.0 Lite undercuts many competitors by up to 40% while maintaining comparable quality.

## Limitations

While Seedance 1.0 Lite excels in **speed** and **cost**, users should be mindful of its inherent **constraints**:

- **Resolution cap**: Maximum output capped at 720 p; 1080 p reserved for the full-feature Seedance 1.0.
- **Clip duration**: Recommended for **5–10 second** clips. Longer sequences may exhibit **temporal drift** or require stitching across multiple generation calls.
- **No audio**: Does not generate soundtracks; audio must be added in post-production.
- **Resource dependence**: Optimal performance requires GPU acceleration; CPU-only inference may suffer from significantly slower speeds.

## How to call **Seedance 1.0 Lite** API from CometAPI

### **`Seedance 1.0 Lite`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Model | Price |
| Text video: `bytedance-seedance-1-0-lite-t2v-250428` | Price: $1.44000 |
| Photo video: `bytedance-seedance-1-0-lite-i2v-250428` | Price: $1.44000 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`bytedance-seedance-1-0-lite-i2v-250428`”/ “`bytedance-seedance-1-0-lite-i2v-250428`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to [[API doc](https://apidoc.cometapi.com/api-19771367)]([https://apidoc.cometapi.com/api-13851472](https://apidoc.cometapi.com/)).

K**bytedance-video**:

- **Base URL:** <https://api.cometapi.com/volc/v3/contents/generations/tasks>
- **Model Names:** “`bytedance-seedance-1-0-lite-i2v-250428`“ / “`bytedance-seedance-1-0-lite-t2v-250428`“
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

### API Integration & Examples

Below is a  snippet demonstrating how to invoke **Seedance 1.0 Lite** via CometAPI’s API . Replace `<API_KEY>` and `<PROMPT>` accordingly:

Text video

```
curl -X POST https://api.cometapi.com/volc/v3/contents/generations/tasks\
-H "Content-Type: application/json" \
-H "Authorization: Bearer $ARK_API_KEY" \
-d '{
"model": "bytedance-seedance-1-0-lite-t2v-250428",
"content": [
{
"type": "text",
"text": "Multiple shots. A detective enters a dimly lit room. He examines a table for clues and picks up an object. The camera pans to show him lost in thought. --ratio 16:9"
}
]
}'
```

**Se**e **Also** [Seedance 1.0 Pro API](https://www.cometapi.com/seedance-1-0-pro-api/)

---

*Originally published at [https://www.cometapi.com/seedance-1-0-lite-api/](https://www.cometapi.com/seedance-1-0-lite-api/).*
