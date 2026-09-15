<!-- social-ops-fingerprint:62ba2f87e9b1b78cd500da5c973daad3153263649184c742ee68fb3a5dc4b6c6 -->
---
title: Alibaba Releases Qwen3‑Coder and Qwen Code: A Breakthrough in Agentic AI Coding
---
# Alibaba Releases Qwen3‑Coder and Qwen Code: A Breakthrough in Agentic AI Coding

![Alibaba Releases Qwen3‑Coder and Qwen Code: A Breakthrough in Agentic AI Coding](https://resource.cometapi.com/blog/uploads/2025/07/Qwen3-Coder.webp)

On July 23, 2025, Alibaba Group officially launched Qwen3‑Coder, an open‑source artificial intelligence model tailored for software development and autonomous coding tasks. The announcement positions Qwen3‑Coder as the company’s most advanced coding model to date, boasting unprecedented scale and performance capabilities designed to meet the complex needs of modern software engineering teams .

The flagship variant, **Qwen3‑Coder‑480B‑A35B‑Instruct**, comprises a 480 billion‑parameter MoE model with 35 billion active parameters, natively supporting context windows up to 256 K tokens and extendable to 1 million tokens via extrapolation techniques. This expansive context length allows the model to maintain coherence over large codebases, documentation, and multi‑file projects without losing track of dependencies.

## Model Specifications and Capabilities of Qwen3‑Coder

Key technical highlights include:

**Extensive Benchmarks**: According to Alibaba, Qwen3‑Coder outperforms all existing open‑source coding models on benchmarks such as SWE‑Bench‑Verified and agentic coding evaluations, demonstrating superior accuracy, efficiency, and code quality .

**Agentic Coding Framework**: Leveraging long‑horizon reinforcement learning (Agent RL), Qwen3‑Coder can autonomously plan coding tasks, invoke external developer tools, and self‑correct based on feedback loops, mirroring real‑world software engineering processes .

**Dual Thinking Modes**: A unified thinking and non‑thinking mode enables the model to adapt computational budgets dynamically, toggling between rapid response for straightforward scripts and deeper reasoning for intricate algorithmic challenges .

### Performance Benchmarks

In internal benchmarks, Qwen3‑Coder outperformed leading domestic competitors including DeepSeek and Moonshot AI’s K2 on key coding metrics, such as code generation accuracy and multi‑file debugging. Moreover, Alibaba claims parity with top U.S. models—namely OpenAI’s GPT‑4 and Anthropic’s Claude—on standard coding challenges, underscoring its competitiveness on a global scale .

| Model | Runtime Failures (%) | Grammar Errors (%) | Zero-Score Rate (%) | Total Failures (%) | Max Score | Median Score | Median Gap (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OpenAI o4 mini (high) | 1.11 | 3.33 | 6.67 | 11.11 | 77.75 | 66.75 | 14.16 |
| Claude Sonnet 4 (Think) | 1.11 | 5.56 | 3.33 | 10.00 | 75.67 | 66.98 | 11.49 |
| Qwen3-Coder-480B-A35B | 5.56 | 4.44 | 10.00 | 20.00 | 72.85 | 52.04 | 28.57 |
| Gemini 2.5 Pro | 2.22 | 7.78 | 8.89 | 18.89 | 72.24 | 58.05 | 19.65 |
| DeepSeek R1 0528 | 3.33 | 5.56 | 13.33 | 22.22 | 69.36 | 49.25 | 29.00 |
| Claude Sonnet 4 | 3.33 | 4.44 | 7.78 | 15.55 | 68.26 | 61.02 | 10.60 |
| GPT-4.1 mini | 2.22 | 7.78 | 3.33 | 13.33 | 64.39 | 50.87 | 20.99 |
| Qwen3-235B-A22B-Instruct-2507 | 4.44 | 16.67 | 13.33 | 34.44 | 63.24 | 42.44 | 32.89 |

Trained on a massive **7.5 trillion token dataset**, with over **70%** of the data sourced from high-quality code repositories, Qwen3-Coder was further refined using reinforcement learning based on real-world development scenarios. This post-training fine-tuning significantly improved the model’s execution success rate and robustness in generating correct and efficient code.

Qwen3-Coder is now available on **Hugging Face** and **GitHub**, and developers can access it via the **Alibaba Cloud Model Studio** API. It has also been integrated into **Tongyi Lingma (Qwen Code)**, Alibaba’s AI coding assistant, providing seamless deployment for enterprise and individual developers alike.

## Qwen Code

To facilitate broad adoption, Alibaba is concurrently releasing **Qwen Code**, a command‑line interface built on top of Gemini Cli that seamlessly connects Qwen3‑Coder to popular development environments, version control systems, and CI/CD pipelines . This tool features:

- **Custom Prompts & Function Calling**: Preconfigured interaction patterns that guide developers through test generation, code review, and deployment tasks.
- **Plugin Architecture**: Extensible modules for integrating third‑party debuggers, linters, and performance profilers.
- **Alibaba Cloud Model Studio Access**: One‑click API provisioning, monitoring dashboards, and fine‑tuning options within the Alibaba Cloud ecosystem .

Developers can install Qwen Code through the npm manager or use the source code from GitHub，Qwen Code supports OpenAI SDK calling LLM.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can interact with [Qwen3-Coder](https://www.cometapi.com/qwen3-coder-api/) through a compatible OpenAI‐style API, available via CometAPI . **CometAPI**, which offer Open source(`qwen3-coder-480b-a35b-instruct`) and commercial versions(`qwen3-coder-plus; qwen3-coder-plus-2025-07-22`)at the same price.The commercial version is 1M long. Sample code for Python (using the OpenAI‐compatible client) with best practices recommending sampling settings of temperature = 0.7, top\_p = 0.8, top\_k = 20, and a repetition\_penalty = 1.05. Output lengths can extend up to 65,536 tokens, making it suitable for large code generation tasks.

To begin, explore models’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key.

---

*Originally published at [https://www.cometapi.com/alibaba-releases-qwen3%E2%80%91coder-and-qwen-code/](https://www.cometapi.com/alibaba-releases-qwen3%E2%80%91coder-and-qwen-code/).*
