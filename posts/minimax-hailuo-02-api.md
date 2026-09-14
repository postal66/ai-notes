<!-- social-ops-fingerprint:55228e2ebd7ad9a4d1351b9a35490b4c795d59a6278af60a4cdd492996defcce -->
---
title: MiniMax‑Hailuo‑02 API
---
# MiniMax‑Hailuo‑02 API

![MiniMax‑Hailuo‑02 API](https://resource.cometapi.com/blog/uploads/2025/06/MiniMax-Unveils-Hailuo%E2%80%AF02-%E2%80%93-A-New-Era-in-AI-Video-Generation-2-710x373.webp)

MiniMax‑Hailuo‑02 API is an asynchronous, HTTP‑based service from MiniMax that lets developers generate professional‑grade, cinematic videos from either text or image prompts.Built on a diffusion‑transformer backbone, MiniMax‑Hailuo‑02 delivers photorealistic visuals, advanced physics simulation, and director‑level camera controls with consistent character rendering, and it ranks #2 globally on the Artificial Analysis benchmark.

## Basic Information & Features

| Feature Category | Performance Description |
| --- | --- |
| Native Resolution | Natively outputs 1080 p (no frame interpolation) |
| Physics-Engine Comprehension | Supports realistic physical logic such as gravity, inertia, and acceleration |
| Complex Motion Processing | Can generate highly dynamic scenes (e.g., gymnastics, dance, combat) |
| Instruction-Parsing Ability | Accurately responds to combined prompts of scene settings + style constraints + motion trajectories |
| Stability | Significantly reduces clipping, tearing, and abnormal frame jumps |

## Technical Architecture

At its core, MiniMax‑Hailuo‑02 is powered by the **Noise‑aware Compute Redistribution (NCR)** architecture, which redistributes computational resources based on scene complexity to boost efficiency and fidelity . This design achieves a **2.5× improvement** in both **training** and **inference efficiency** compared to its predecessor, Hailuo‑01 . Additionally, the model incorporates a **Mixture‑of‑Experts (MoE)** framework, enabling dynamic specialization across diverse visual and motion sub‑tasks.

## Technical details

- **Model architecture & scale:** MiniMax reports Hailuo-02 is a substantial upgrade over Hailuo-01 — **roughly triple the parameter count** and re-engineered for native 1080p generation (model scale + training improvements).
- **Physics & temporal consistency:** explicit design for *physics simulation* (fluid dynamics, object interactions, realistic motion), and *frame-to-frame consistency* for characters and props. These subsystems improve perceived realism versus earlier short-clip generators.
- **Camera & cinematography controls:** supports complex *camera motion* (pans, tracking, zooms) and director-style presets (e.g., “reel”, “tracking shot”) to help creators get professional staging without manual keyframing.
- **Input modes:** text prompts (full scenes), image→video (animate a provided still), and presets/“director” controls in higher tiers.

## Benchmark Performance

- **Global Ranking**: Secured **#2** on the Artificial Analysis Video Arena leaderboard, trailing only ByteDance’s Seedance but surpassing Google’s Veo 3 in quality‑per‑cost metrics.
- **Comparative Fidelity**: Demonstrated **sharper detail** and **more vibrant color** reproduction in natural scenes compared to Veo 3, making it ideal for documentaries and artistic visualizations.
- **Throughput**: Achieves up to **60 FPS equivalent** rendering on standard A100 hardware, enabling rapid iteration for creative teams.

## Model Versioning and Updates

**Codename**: Internally referred to as **“Kangaroo”** to signify its large leap in generative “jumps” of quality.

MiniMax‑Hailuo‑02 is offered in two **operational modes**:

- **Standard**: Prioritizes **faster renders** and lower cost, suitable for rapid prototyping and high‑throughput applications .
- **Pro**: Unlocks **advanced physics simulations** and **higher detail**, tailored for demanding cinematic and VFX workflows .

Both versions support **customizable resolution** and **duration parameters**, allowing developers to fine‑tune outputs to project requirements.

## Limitations & known caveats

- **Duration constraint:** optimized for short clips (~5–10s). Long continuous sequences are not yet its strength.
- **Audio & synchronization:** current public builds and demos focus on visual fidelity; fully integrated, *synchronized audio/voiceover* pipelines were described as planned enhancements rather than built-in features in early releases.
- **Artifact/edge cases:** complex scenes with dense occlusion, high-frequency textures, or extreme low-light may still show artifacts; rigorous editorial oversight is recommended.
- **Ethics & content policy risks:** high realism raises **deepfake** and copyright concerns — production workflows must include provenance, consent checks, and moderation. (This is a general industry risk that applies strongly here.)

## How to call **minimax-hailuo-02** API from CometAPI

### **`minimax-hailuo-02`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Price | $2.88 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`minimax-hailuo-02`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to  [API doc](https://apidoc.cometapi.com/minimax-conch-generation-14660582e0):

- **Endpoint:** `https://api.cometapi.com/v1/images/generations`
- **Model Parameter:** `minimax-hailuo-02`
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY`
- **Content-Type:** `application/json` .

### API Integration

Developers can access MiniMax‑Hailuo‑02 via a **RESTful API**, submitting asynchronous tasks for generation and retrieving results by **task\_id**. Below is a **cURL example**:

```
bashcurl -X POST https://api.cometapi.com/v1/video_generation \
  -H "Authorization: Bearer $YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-hailuo-02",
    "prompt": "A futuristic cityscape at dawn with flying vehicles, dynamic camera pan",
  }'
```

Upon success, the API returns a **task\_id**, which can be used to poll the **task-result** endpoint and obtain the **video\_url** once rendering is complete.

**see also  [Veo 3](https://www.cometapi.com/veo-3-api/)**

---

*Originally published at [https://www.cometapi.com/minimax%E2%80%91hailuo%E2%80%9102/](https://www.cometapi.com/minimax%E2%80%91hailuo%E2%80%9102/).*
