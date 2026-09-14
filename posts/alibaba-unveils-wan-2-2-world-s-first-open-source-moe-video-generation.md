<!-- social-ops-fingerprint:b6834b5feeb92cbe85270162db097882e2204957e4abdd938cf1b94dd94d9f05 -->
---
title: Alibaba Unveils Wan 2.2: World’s First Open‑Source MoE Video Generation Model
---
# Alibaba Unveils Wan 2.2: World’s First Open‑Source MoE Video Generation Model

![Alibaba Unveils Wan 2.2: World’s First Open‑Source MoE Video Generation Model](https://resource.cometapi.com/blog/uploads/2025/07/Alibaba-Unveils-Wan-2.2.webp)

Alibaba’s DAMO Academy today officially released **Wan 2.2**, a next‑generation suite of open‑source video generation models built on a **Mixture‑of‑Experts (MoE)** architecture. Wan 2.2 promises breakthrough improvements in computational efficiency, motion fidelity, and cinematic expressiveness—enabling developers and creators to generate high‑quality 1080p videos from text or image prompts with unprecedented control and flexibility .Wan 2.2 delivers significant gains in motion quality, visual detail, and computational efficiency compared to its predecessor, Wan 2.1.

## Key Innovations in Wan 2.2

### 1. MoE‑Driven Denoising Pipeline

subnetworks, the system can allocate resources where they matter most—broad strokes for scene layout followed by fine‑grained detail refinement. This design enables Wan 2.2’s flagship model to boast 27 billion total parameters while activating only 14 billion per inference pass, effectively halving the compute resources required for high‑quality video synthesis.

- **High-Noise Expert** focuses on establishing the overall motion trajectories and scene composition.
- **Low-Noise Expert** applies meticulous texture, facial detail, and lighting nuances.

This dual‑expert framework ensures that creators can generate longer, more complex sequences with professional cinematic fidelity—all without proportionally increasing GPU memory demands compared to Wan 2.1 .

### 2. Cinematic Aesthetic Control System

Building on its architectural innovations, it introduces an unprecedented “Film Aesthetics Control System” that allows users to steer lighting, color grading, camera angles, and composition through intuitive keyword prompts. By combining descriptors such as “sunset glow,” “soft rim light,” or “low‑angle balanced composition,” creators can automatically generate scenes reminiscent of Hollywood blockbusters or indie art films alike. Conversely, inputs like “cool tones,” “hard lighting,” and “dynamic framing” produce science‑fiction or noir‑style visuals on demand .

For the first time in open‑source AI video models, Wan 2.2 integrates a **film‑grade control interface**:

- **60+ adjustable parameters** covering lighting, color grading, framing, lens effects, and depth of field.
- **Smart style linking**, allowing users to describe moods (e.g., “noir lighting at twilight”) and have the system automatically configure complex camera and color setups.
- **Predefined cinematic presets**, such as “vintage Western,” “neo‑Tokyo sci‑fi,” and “documentary reportage,” streamline creative workflows.

### 3. Enhanced Physics and Emotional Realism

Wan 2.2 demonstrates marked improvements in simulating real‑world phenomena and human micro‑expressions:

- **Physics simulation** for natural fluid dynamics, volumetric lighting, and collision effects.
- **Facial micro‑expression capture**, rendering subtle cues like trembling lips, eyebrow shifts, and suppressed tears with high fidelity.
- **Multi‑person scene handling**, ensuring coherent interactions and consistent lighting across moving characters .

## Model Variants and Performance

The Wan 2.2 release includes:

- **Wan 2.2‑T2V‑A14B**: Text‑to‑Video
- **Wan 2.2‑I2V‑A14B**: Image‑to‑Video
- **Wan 2.2‑IT2V‑5B**: A compact 5 billion‑parameter unified model that fits on consumer‑grade GPUs,Unified Generation

The 5B variant leverages a high‑compression 3D VAE for 4×16×16 time‑space token reduction—enabling smooth 1080p output even on modest hardware.

The Wan 2.2 suite includes two core offerings designed for different use cases:

### 14B-Parameter MoE Model (Wan 2.2-T2V-A14B & Wan 2.2-I2V-A14B)

- Employs the full MoE architecture for maximum quality.
- Supports both text‑to‑video and image‑to‑video workflows at up to 1080p resolution.
- Ideal for studio‐level production and research .

### 5B-Parameter Dense Unified Model (Wan 2.2-IT2V-5B)

- A compact, performance‐oriented model deployable on a single consumer‑grade GPU (e.g., NVIDIA RTX 4090).
- Generates 720p, 24 fps videos in minutes, leveraging a high‑compression 3D VAE to achieve 4×16×16 temporal and spatial downsampling with minimal quality loss.
- Lowers the barrier for hobbyists and small teams to experiment with AI video generation .

Benchmarks indicate that the smaller model can deliver a 5‑second high‑definition clip in under five minutes on standard gaming hardware, making Wan 2.2 one of the fastest open‑source solutions in its class.

## Accessibility and Open‑Source Commitment

In line with Alibaba’s pledge to democratize AI, Wan 2.2 is fully open‑source and freely accessible through multiple platforms:

- **GitHub & Hugging Face** for direct model and code downloads.
- **Moda Community** for community‑driven extensions and integrations.
- **Alibaba Cloud BaiLian API** for enterprise‑grade, on‑demand model hosting.
- **Tongyi Wanxiang Website & App** for no‑code, browser‑based experimentation.

Since early 2025, the Wan series has amassed over 5 million downloads across the open‑source community, underscoring its role in fostering collaborative innovation and skill development among AI practitioners globally.

## Industry Implications

The release of Wan 2.2 marks a pivotal moment in AI‑assisted filmmaking and content creation:

**Commercial Potential:** Brands, advertisers, and social media platforms stand to benefit from rapid prototyping of video assets, personalized ad creatives, and dynamic storytelling formats.

**Lowering Barriers:** Professionals and independent creators can now achieve near‑studio‑level video production without expensive hardware or software licenses.

**Innovation Catalyst:** Open‑sourcing a MoE‑based generative video model accelerates research collaboration, potentially spawning new architectures and artistic tools.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

The latest integration Wan 2.2 will soon appear on CometAPI, so stay tuned！While we finalize Gemini 2.5 Flash‑Lite Model upload, explore our other models on the Models page or try them in the AI Playground.

While waiting,developers can access [Veo 3 API](https://www.cometapi.com/veo-3-api/) and [Midjourney Video API](https://www.cometapi.com/midjourney-video-api/) through [CometAPI](https://www.cometapi.com/) to generate video instead of wan 2.2, the latest claude models version listed are as of the article’s publication date. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

In summary, Alibaba’s Wan 2.2 not only advances the state of the art in video AI but also exemplifies how open‑source ecosystems can accelerate progress and diversify use cases. As developers begin to experiment with its MoE backbone and cinematic controls, the next wave of AI‑generated video content may well emerge from the very communities that Alibaba has helped empower.

---

*Originally published at [https://www.cometapi.com/alibaba-unveils-wan-2-2/](https://www.cometapi.com/alibaba-unveils-wan-2-2/).*
