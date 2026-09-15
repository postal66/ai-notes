<!-- social-ops-fingerprint:08a9f19e66d43a467e5bca5a318ea90a2ca84ea1ee1c1e69b3abe8c2519f20bb -->
---
title: Alibaba Cloud releases Qwen‑VLo multimodal model，Image capability upgrade
---
# Alibaba Cloud releases Qwen‑VLo multimodal model，Image capability upgrade

![Alibaba Cloud releases Qwen‑VLo multimodal model，Image capability upgrade](https://resource.cometapi.com/blog/uploads/2025/06/vlo-1024x436.webp)

Alibaba Cloud’s AI division has officially launched **Qwen‑VLo**, the latest iteration in its Qwen multimodal model series, marking a significant advancement in unified vision‑and‑language capabilities. Announced on June 28, 2025, Qwen‑VLo offers both understanding and generation functionalities, extending well beyond its predecessors to include high‑resolution image creation and editing driven by natural‑language prompts and visual inputs.

Building on earlier releases such as Qwen‑VL and Qwen2.5‑VL, Qwen‑VLo represents what Alibaba describes as a “comprehensive upgrade” in multimodal AI. While Qwen‑VL focused primarily on interpreting visual information, and Qwen2.5‑VL enhanced long‑context comprehension, Qwen‑VLo integrates these strengths into a single framework capable of bidirectional vision‑language tasks. It accommodates open‑ended instructions, supports multiple languages—including Chinese and English—and refines its outputs to rival those of human artists .

## Key Features

### Progressive Image Generation

Qwen‑VLo constructs images in a stepwise fashion—from left to right and top to bottom—iteratively refining predicted content to ensure consistency and visual harmony. This mechanism enhances both generation efficiency and user control over the creative process.

### Dynamic Resolution Support

Utilizing dynamic resolution training, the model can handle arbitrary input/output resolutions and aspect ratios. Users can generate content tailored for diverse scenarios—such as web banners, social media covers, or high-resolution posters—without being constrained by fixed formats.

### Open-Ended Instruction Editing

Through natural language prompts, Qwen VLo can perform advanced edits such as style transfers (“Apply a Van Gogh style”), composite transformations (“Add a sunny sky”), and multi-faceted modifications in a single instruction. It also supports extracting and editing traditional visual signals like depth maps, segmentation masks, and edge outlines.

### Multilingual Interaction

The model accepts commands in multiple languages—currently supporting Chinese and English—thereby catering to a global user base and breaking down linguistic barriers in creative workflows.

## Availability and Access

Qwen‑VLo is currently available in **preview** via the Qwen Chat platform at [chat.qwen.ai](https://chat.qwen.ai/). Alibaba Cloud has noted that, as a preview release, users may encounter occasional inconsistencies or factual inaccuracies during generation. The development team is actively iterating to address these limitations before a broader rollout.

Under the hood, Alibaba’s AI engineers have optimized Qwen‑VLo for deployment across both cloud and edge environments. Leveraging mixed‑precision quantization and novel parameter‑efficient fine‑tuning techniques, the model maintains high performance on a compact compute footprint. Alibaba has also integrated adaptive inference pipelines to balance latency and quality, ensuring that Qwen‑VLo can serve latency‑sensitive applications—such as interactive design tools—while scaling to enterprise‑grade workloads on Alibaba Cloud.

## Compare to **Qwen-VL-Plus/Max**

| **Function Dimension** | **Qwen-VL-Plus/Max** | **Qwen VLo** |
| --- | --- | --- |
| Image Understanding | Basic classification, description | Multidimensional structure recognition, enhanced contextual understanding |
| Image Generation | Limited style support | High precision, progressive generation, strong style control capabilities |
| Multitasking Capability | Requires task-specific input | Unified multitasking, supports complex language instructions |
| Multilingual Interaction | Limited support | Native support for Chinese and English, smoother natural language control |
| Detail Preservation Ability | Possible detail loss in generation | Accurate identification and reconstruction of key structures and semantics |

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

To begin, explore models’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key.

The latest integration Qwen‑VLo API will soon appear on CometAPI, so stay tuned！While we finalize Qwen‑VLo Model upload, explore our other models on the [Models page](https://www.cometapi.com/model/) or try them in the [AI Playground](https://www.cometapi.com/console/playground). Qwen’s latest Model in CometAPI is [Qwen 3 API](https://www.cometapi.com/qwen-3-api/)(qwen3-235b-a22b;qwen3-30b-a3b;qwen3-8b) and qwen-vl-plus-latest.

![Alibaba Cloud releases Qwen‑VLo multimodal model，Image capability upgrade](https://resource.cometapi.com/blog/uploads/2025/06/qwenvl-1024x390.webp)

---

*Originally published at [https://www.cometapi.com/alibaba-cloud-releases-qwen%E2%80%91vlo/](https://www.cometapi.com/alibaba-cloud-releases-qwen%E2%80%91vlo/).*
