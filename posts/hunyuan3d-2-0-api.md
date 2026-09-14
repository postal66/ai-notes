<!-- social-ops-fingerprint:07db8ee0d0a98f0dc8b27890ea78a3476e9cfebdd7f0500016b01e13b9df69c3 -->
---
title: Hunyuan3D 2.0 API
---
# Hunyuan3D 2.0 API

![Hunyuan3D 2.0 API](https://resource.cometapi.com/blog/uploads/2025/08/Hunyuan3D-.webp)

**`Hunyuan3D`** 2.0 is Tencent’s advanced large-scale 3D generative AI system. Leveraging diffusion-based architectures, it transforms text descriptions or images into richly detailed 3D assets—meshes enriched with high-quality textures—via a two-stage pipeline of **shape generation** and **texture synthesis**.

## Key features (what it does)

- **Two-stage generation:** decouples **geometry** (bare mesh) from **texture synthesis** (UV maps / PBR textures), improving control and quality.
- **Image-conditioned and text-conditioned modes:** accepts **single or multi-view images** and/or **text prompts** to guide shape and texture.
- **High-resolution textures:** supports large texture outputs (configs for 2K–6K+ workflows) and SR/enhancement steps. **Keywords:** *texture resolution, super-resolution, baking*.

---

## Technical Details

- **Shape generator (Hunyuan3D-DiT)**: a diffusion-transformer style module trained to produce geometry (octree / octree-like or lattice representations depending on version), optimized to align geometry with a conditioning image or text prompt.
- **Texture synthesizer (Hunyuan3D-Paint / PBR synthesizer)**: a second model that generates UV-mapped texture atlases with **physically-based rendering** outputs (albedo, roughness, metallic maps) so generated assets are immediately usable in renderers and game engines.
- **Decoding & resolution**: later versions raise geometric resolution (e.g., higher octree/lattice resolution) and texture sizes (common community settings produce up to multi-k textures for export).
- **Scaling & model sizes**: v2.5 reporting indicates considerable scale-up (parameter counts and dataset scale) from 2.0 to 2.5 to improve geometry precision and texture fidelity.
- **Hunyuan3D-2.5 upgrades:** **LATTICE** (10B parameters max) for sharper, clean geometry; **PBR texture pipeline** with improved **multi-view** consistency; 4K-class textures reported in community notes.

**Compute & VRAM:** reference repo notes **~6 GB VRAM** for shape generation and **~16 GB** for full shape+texture inference (typical desktop GPUs).

## Benchmark Performance (v2.0 vs Others)

| Model | CMMD ⬇ | FID\_CLIP ⬇ | FID ⬇ | CLIP-score ⬆ |
| --- | --- | --- | --- | --- |
| Top Open-source | 3.591 | 54.639 | 289.287 | 0.787 |
| Top Closed-source 1 | 3.600 | 55.866 | 305.922 | 0.779 |
| Closed-source 2 | 3.368 | 49.744 | 294.628 | 0.806 |
| Closed-source 3 | 3.218 | 51.574 | 295.691 | 0.799 |
| **Hunyuan3D 2.0** | **3.193** | **49.165** | **282.429** | **0.809** |

*Results confirm notable superiority in geometric detail and texture realism.*

## Use Cases

- **Input Modes**: Text-to-3D, Image-to-3D, Multi-view input (in advanced versions).
- **Outputs**: High-resolution mesh + high-quality textures (PBR in later versions).

**Game prototyping & asset pipelines:** rapid concept → textured mesh turnaround; reduces artist iteration time for props/characters. **Keywords:** prototyping, game assets.

**AR/VR / virtual production:** PBR textures + engine-compatible exports allow fast integration into interactive scenes and previsualization. **Keywords:** AR/VR, PBR, engine-ready.

**Architecture & product visualization:** stylized or realistic 3D prototypes from sketches or mood images. **Keywords:** visualization, rapid iteration.

**Education / creative tooling:** accessible way to teach 3D concepts and let creators generate base meshes for refinement. **Keywords:** education, creative tooling. (Community examples and tutorials.)

---

## Limitations & Challenges

- **Mesh Density**: High triangle counts (up to ~600k) require retopology for production pipelines.
- **Texture Detail**: Fine details (e.g. fabrics) may blur when input resolution is low.
- **Region Restrictions**: EU/GDPR concerns limit usage; compliant versions are in progress.
- **Seams & lighting inconsistency:** texture baking can produce **seams or lighting artifacts**, particularly with single-image inputs; multi-view inputs and SR/inpainting mitigate but do not eliminate these issues.
- Prompt/conditioning sensitivity:\*\* as with other generative models, **prompt phrasing and input framing** substantially affect results; edge cases and fine geometric constraints may need iterative refinement.

## How to call **`Hunyuan3D`** API from CometAPI

### **`Hunyuan3D-2`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Price | $0.08000 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`Hunyuan3D-2`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to  [API doc](https://apidoc.cometapi.com/hunyuan3d-20073774e0):

- **Endpoint:** `https://api.cometapi.com/v1/images/generations`
- **Model Parameter:** `Hunyuan3D-2`
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY`
- **Content-Type:** `application/json` .

```
curl --location
--request POST 'https://api.cometapi.com/v1/images/generations' \
--header 'Authorization: Bearer {{api-key}}' \
--header 'Content-Type: application/json' \
--data-raw '{ "model": "Hunyuan3D-2", "prompt": "A cute baby sea otter", "image": "https://filesystem.site/cdn/20250414/chxiLc2O45zoLT8BCrQ6WQlTvGDDnK.png" }'
```

---

*Originally published at [https://www.cometapi.com/hunyuan3d-2-0/](https://www.cometapi.com/hunyuan3d-2-0/).*
