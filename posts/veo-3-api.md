<!-- social-ops-fingerprint:c69000ed39823e66ce3033e7529826c1e1728a121ab774557484a649f26b96ff -->
---
title: Veo 3 API
---
# Veo 3 API

![Veo 3 API](https://resource.cometapi.com/blog/uploads/2025/10/How-to-Use-Veo-3.1-API-710x373.webp)

The Veo 3 API is a RESTful endpoint on Google Vertex AI that enables developers to generate synchronized, high‑resolution video and audio clips from text or image prompts—complete with built‑in safety filters and imperceptible watermarking—in a single request.

Google DeepMind’s **Veo 3** represents the cutting edge of **text-to-video generation**, marking the first time a large-scale generative AI model seamlessly synchronizes **high-fidelity video** with **accompanying audio**—including dialogue, sound effects, and ambient soundscapes.

## Core **Features** and Capabilities

- **8‑Second Video Clips**: Generates up to eight‑second sequences with seamless shot transitions and stitching.
- **Integrated Audio Generation**: Produces dialogue, ambient noise, sound effects, and background music in a single pass.
- **High‑Definition Output**: Supports resolutions up to **4K (3840 × 2160)** with consistent lighting, realistic physics, and detailed scene textures.
- **Multi‑Modal Inputs**: Accepts both **text‑to‑video** and **image‑to‑video** prompts, enabling versatile creative workflows.

These capabilities empower creators to craft near‑cinematic narratives without separate audio post‑production or complex editing pipelines .

## Technical Details

Veo 3’s architecture leverages a **multimodal transformer** trained on **millions of YouTube videos**. Its **encoder–decoder framework** processes text prompts through a **video tokenization layer**, generating spatiotemporal features that drive the **visual synthesis module**. Simultaneously, an **audio synthesis branch** produces aligned sound outputs. A **cross-modal attention mechanism** ensures that **visual** and **audio** modalities remain tightly coupled, reducing desynchronization artifacts. Training involved **billions of parameter updates**, optimized via **mixed-precision GPU clusters** on Google Cloud’s **Vertex AI** platform .

## Benchmark Performance

In internal benchmarks, Veo 3 demonstrates:

- **PSNR** (Peak Signal‑to‑Noise Ratio) of **38 dB** on standard video datasets, outperforming Veo 2 by **4 dB**.
- **SSIM** (Structural Similarity Index) scores of **0.92**, indicating high visual fidelity.
- **Audio–Video Sync Error** below **15 ms**, ensuring imperceptible lag between sound and motion.
- **Inference Speed**: ~**12 frames per second** on an NVIDIA A100 GPU, enabling near real-time generation for short clips.
  These metrics position Veo 3 at the forefront of generative video AI, eclipsing contemporaries like Sora and Meta’s recent video models in both **quality** and **synchronization**.

## Model Versions and Evolution

- **Veo 1** (May 2024): Launched at Google I/O 2024, introduced **1080p silent video** generation over one minute.
- **Veo 2** (December 2024): Upgraded to **4K support** and improved **physical dynamics** understanding .
- **Veo 3** (May 2025): Added **audio synthesis**, **enhanced realism**, and **4K output**, marking a significant leap in **multimodal generation**.

## How to call Veo 3 API from CometAPI

### **`Veo 3`** API Pricing in CometAPI，lower than the official price:

| Model name | Price |
| --- | --- |
| veo3-pro | $2 |
| veo3-fast | $0.4 |
| veo3 | $2 |
| veo3-pro-frames | $0.4 |

**`veo3`**,**`veo3-pro`**,**`veo3-fast`**,**`veo3-pro-frames`**:It is the latest video generation model officially launched by Google. The generated videos have sound. It is the only video model with sound in the world. `veo3-pro-frames` supports the first frame mode. This model follows the openai chat standard format call

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Code Example

1. Select the “**`veo3-pro`**”etc endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Modify the **BASE\_URL** in your application to our interface address.***The URL is determined by your specific application needs.***
3. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.

If you have any questions about the call or have any suggestions for us, please contact us through social media and email address [support@cometapi.com](mailto:support@cometapi.com).

### Use Cases：

**Submit video generation task** (Doc: [available here](https://apidoc.cometapi.com/submit-video-generation-task-18941528e0)): <https://api.cometapi.com/veo/v1/video/create>

**Query video generation status**: [https://api.cometapi.com/veo/v1/video/query/{taskId}](https://api.cometapi.com/veo/v1/video/query/%7BtaskId%7D)

### API Code CometAPI Usage Example

```
import requests
def main():
url = " https://api.cometapi.com/veo/v1/video/create"
payload = {
"model": "veo3-pro",
"prompt": "A DJ on the stand is playing, around a World War II battlefield, lots of explosions, thousands of dancing soldiers, between tanks shooting, barbed wire fences, lots of smoke and fire, black and white old video: hyper realistic, photorealistic, photography, super detailed, very sharp, on a very white background",
}
headers = {"Authorization": "Bearer ", "Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
print("Generation:", response.json())
if name == "main":
main()
```

**See Also [3 Methods to Use Google Veo 3 in 2025](https://www.cometapi.com/3-methods-to-use-google-veo-3-in-2025/)**

---

*Originally published at [https://www.cometapi.com/veo-3-api/](https://www.cometapi.com/veo-3-api/).*
