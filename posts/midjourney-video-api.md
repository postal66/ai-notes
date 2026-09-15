<!-- social-ops-fingerprint:b136f3f1750db2f01aac4775d2cff59055ca4e1962c01fb0bace62bbaa444760 -->
---
title: Midjourney Video API
---
# Midjourney Video API

![Midjourney Video API](https://resource.cometapi.com/blog/uploads/2025/07/20250702-145733-1024x518.webp)

The MidJourney Video API allows developers to programmatically generate, manipulate, and retrieve AI-generated video content using MidJourney’s models and prompts.

## Overview

Midjourney Video is the first video‐generation model (Video Model V1) released by Midjourney on June 18, 2025. It introduces an “Image‑to‑Video” workflow that transforms static AI‑generated or user‑uploaded images into short animated clips. This marks Midjourney’s expansion from still‑image creation into dynamic content, positioning it alongside other AI video tools from Google, OpenAI, and Meta .

## How MidJourney Video Works

- **Image‑to‑Video Workflow**: You supply either a Midjourney‑generated image or an external image, plus an optional motion prompt. Midjourney’s model then interprets “who’s moving,” “how they move,” and “what happens next” to animate the scene for about 5 seconds by default .
- **Automatic vs. Manual Animation**: In automatic mode, the system infers motion parameters and camera pathways. Manual mode lets you fine‑tune aspects like camera angle, subject path, and speed, giving more creative control .

## Technical Architecture

Midjourney Video is built on a **transformer architecture** enhanced to handle **temporal consistency** across frames. The pipeline works as follows:

1. **Feature Extraction**: The input image is processed through deep convolutional and transformer layers to capture spatial features.
2. **Keyframe Generation**: A small set of representative frames is synthesized.
3. **Frame Interpolation**: Specialized sub‑models generate intermediate frames, ensuring smooth **motion synthesis** between keyframes.
4. **Motion Conditioning**: Depending on **High** or **Low Motion** settings (and any manual prompts), the model adjusts object and camera trajectories.

## Model Versioning & Roadmap

**V1 Video Model (June 2025)**: Debut release focused on image‑to‑video conversion.

### Benchmark Performance

Early evaluations position the V1 model competitively:

- **Frame Quality (FID Score)**: Achieves a Fréchet Inception Distance of **22.4**, outperforming comparable open‑source video models by ~15% on standard video benchmarks.
- **Temporal Smoothness (TS Metric)**: Records a Temporal Smoothness score of **0.88** on the DAVIS dataset, indicating high visual continuity across frames.
- **Latency**: Average generation time of **12 seconds** per clip on a single NVIDIA A100 GPU, balancing performance with user expectations.
- **Quality Metrics**: Achieves an **SSIM** (Structural Similarity Index) above **0.85** on synthetic motion datasets when compared to ground‑truth clips, indicating **high fidelity** to natural movement patterns.

> **Note**: These figures reflect Midjourney’s internal tests; external performance may vary based on load and subscription tier.

### Key Features of V1

- **Clip Length**: Base clips run ~5 seconds; you can extend in 4‑second increments up to 21 seconds total.
- **Style Consistency**: Animations preserve the original image’s artistic style—brushstrokes, color palettes, and mood carry through the motion .
- **Performance & Speed**: A typical 4‑segment (≈17‑second) video renders in under 70 seconds, balancing quality with fast iteration.
- **Resolution**: Currently capped at 480p, which is clear for social‑media‑style clips but not targeted at large‑screen or high‑end commercial projects .

## How to call MidJourney Video API from CometAPI

### **`MidJourney Video`** API Pricing in CometAPI，lower than the official price:

|  |  |
| --- | --- |
| Model Name | Calculate price |
| **`mj_fast_video`** | 0.6 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### [API Usage](https://apidoc.cometapi.com/api-18581293)

1. send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

![Midjourney Video API](https://resource.cometapi.com/blog/uploads/2025/07/20250702-145733-1024x518.webp)

### API Integration of CometAPI

Currently, V1 is accessible **web‑only** via Midjourney’s **Discord bot**, but **Unofficial wrappers (e.g.,CometAPI**) provide endpoints,developers can integrate via:

Developers can integrate video generation via RESTful API. A typical request structure (illustrative):

```
curl --
location
--request POST 'https://api.cometapi.com/mj/submit/video' \
--header 'Authorization: Bearer {{api-key}}' \
--header 'Content-Type: application/json' \
--data-raw '{ "prompt": "https://cdn.midjourney.com/f9e3db60-f76c-48ca-a4e1-ce6545d9355d/0_0.png add a dog", "videoType": "vid_1.1_i2v_480", "mode": "fast", "animateMode": "manual" }'
```

**See Also [[How to Use Midjourney’s V1 Video Model?](https://www.cometapi.com/how-to-use-midjourneys-v1-video-model/)](<https://www.cometapi.com/midjourney-api/>)**

---

*Originally published at [https://www.cometapi.com/midjourney-video-api/](https://www.cometapi.com/midjourney-video-api/).*
