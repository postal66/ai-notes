<!-- social-ops-fingerprint:480c1cf1ed089deba2f2fd0c5603c1a3d1ba3978f377194ea9c31004f2e07e1f -->
---
title: ByteDance open-sources Seed-OSS-36B, a 36B-parameter LLM
---
# ByteDance open-sources Seed-OSS-36B, a 36B-parameter LLM

![ByteDance open-sources Seed-OSS-36B, a 36B-parameter LLM](https://resource.cometapi.com/blog/uploads/2025/08/seed-oss-68a609f4201e788db05b5dcd.webp)

ByteDance’s Seed team has released **Seed-OSS**, a family of open-source large language models led by **Seed-OSS-36B**, a 36-billion-parameter model that supports exceptionally long input windows and is being distributed under an Apache-2.0 license. The code and model cards were published on GitHub and Hugging Face on Aug. 20, 2025, and multiple variants — including a Base and an Instruct flavor (plus versions trained with synthetic data) — are immediately available to developers.

## What Seed-OSS was released

ByteDance Seed released three Seed-OSS variants: `Seed-OSS-36B-Base` (published in versions with and without synthetic data) and `Seed-OSS-36B-Instruct`

### Key technical highlights of Seed-OSS

- **Parameter count:** The headline model is described as a **36-billion-parameter** model. \
- **Very long context window:** ByteDance advertises an extremely large context length — **up to 512,000 tokens** — aimed at long-document reasoning, codebases, and multi-document agent workflows. \
- **Training scale:** Seed-OSS reportedly reached strong benchmark performance despite being trained on roughly **12 trillion tokens**, per the model documentation.

The Seed-OSS model series is based on the popular causal language model architecture and utilizes RoPE, the GQA attention mechanism, RMS Norm, and the SwiGLU activation function. The newly released Seed-OSS-36B model boasts 36 billion parameters and is capable of handling 512KB of long context. Despite using only 12 trillion training data, it achieves impressive performance on multiple popular benchmarks.

The Seed-OSS model series includes two versions: Seed-OSS-36B-Base with synthetic instruction data and Seed-OSS-36B-Base-woSyn without synthetic instruction data. This design not only provides developers with a high-performance base model but also offers researchers a wider range of options, ensuring that the validity of their research is not compromised by synthetic data.

A key feature of this model is the flexible “thinking budget,” allowing users to dynamically adjust the length of inference as needed. This capability significantly improves inference efficiency in real-world applications. Furthermore, Seed-OSS is specifically optimized for inference tasks, ensuring enhanced reasoning capabilities while maintaining good general performance.

At the launch event, the Seed team emphasized that the Seed-OSS model is not only suitable for academic research but also widely applicable to various development tasks, such as agent-based intelligence tasks like tool usage and problem solving. Model training and evaluation results demonstrate that Seed-OSS achieves leading performance in open source across tasks such as knowledge question answering, mathematical reasoning, and programming.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

The latest integration Seed-OSS will soon appear on CometAPI, so stay tuned！While we finalize Seed-OSS Model upload, explore our other image models that such as [DeepSeek V3.1](https://www.cometapi.com/deepseek-v3-1/) on the your workflow or try them in the AI Playground. You can explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the API guide for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. CometAPI offer a price far lower than the official price to help you integrate.

---

*Originally published at [https://www.cometapi.com/bytedance-open-sources-seed-oss-36b/](https://www.cometapi.com/bytedance-open-sources-seed-oss-36b/).*
