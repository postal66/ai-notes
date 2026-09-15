<!-- social-ops-fingerprint:8862f3b4dde22b2c0a57756572e501fa3f97dc5c759b879b7eff5cae5afd0c4a -->
---
title: Alibaba Cloud Unveils Qwen‑TTS: A High‑Fidelity, Streaming Speech Synthesis Model
---
# Alibaba Cloud Unveils Qwen‑TTS: A High‑Fidelity, Streaming Speech Synthesis Model

![Alibaba Cloud Unveils Qwen‑TTS: A High‑Fidelity, Streaming Speech Synthesis Model](https://resource.cometapi.com/blog/uploads/2025/07/Qwen-TTS-Image-784x441-discover.webp)

On **June 26, 2025**, Alibaba Cloud launched **Qwen‑TTS**, the latest addition to its Tongyi Qianwen (Qwen) family of large AI models. Designed for versatile, high‑quality text‑to‑speech applications, Qwen‑TTS supports Chinese, English, and mixed‑language input and offers both batch and streaming audio outputs, catering to diverse use cases from intelligent voice assistants to multimedia content production.

## Key Technical Features

- **Multilingual Input**: Processes pure Chinese, pure English, or code‑switched Chinese‑English text, enabling seamless voice synthesis across global applications.In addition, the model offers seven bilingual Chinese‑English voice profiles (e.g., Cherry, Ethan, Chelsie, Serena), facilitating seamless cross‑language applications such as global customer support, educational tutoring, and multimedia content targeting international audiences.
- **Streaming Output**: Delivers audio in real time via Base64‑encoded segments, with a final package providing a full audio URL—ideal for low‑latency interactive scenarios.
- **Token‑Based Audio Encoding**: Internally maps every 1 second of audio to 50 tokens (with any partial second rounded up), ensuring predictable performance and granularity for developers .
- **Multiple Voice Styles**: Offers a palette of preset voices—**Cherry, Serena, Ethan, Chelsie**, as well as **Dylan, Jada, Sunny**—allowing for tailored emotional tones and branding consistency.
- **High Throughput & Low Latency**: Optimized for real‑time streaming, Qwen‑TTS can generate audio outputs with end‑to‑end latencies under 100 ms on standard GPU instances, making it ideal for interactive voice assistants and live broadcasting.

## Seamless Integration via DashScope SDK

Qwen‑TTS is immediately accessible through Alibaba Cloud’s Model Studio and the Qwen API endpoint. Developers can deploy the model via PAI‑EAS with just a few clicks, integrate it into workflows through SDKs and OpenAPI‑compliant calls, or fine‑tune it using proprietary voice datasets hosted on Alibaba Cloud . Its scalable architecture supports batch audio generation as well as on‑the‑fly synthesis in virtual call centers and conversational AI platforms.

Alibaba Cloud has prioritized ease of integration for Qwen‑TTS, offering a **straightforward RESTful API** and SDKs in multiple languages. Sample Python code illustrates how minimal configuration—simply setting an environment variable for the API key—enables developers to invoke Qwen‑TTS with a single function call. For example:

```
pythonimport os
from qwen_sdk import SpeechSynthesizer

# Configure API key

os.environ = "your-api-key"

# Synthesize Beijing dialect speech

synthesizer = SpeechSynthesizer(model="qwen-tts-latest", voice="Dylan")
audio_url = synthesizer.synthesize(text="你好，欢迎使用 Qwen‑TTS！")
print(f"Audio available at: {audio_url}")
```

This simplicity accelerates time‑to‑market for applications in education, media production, smart devices, and beyond.

## Use Cases and Industry Impact

- **Customer Service Automation**: Companies can deploy empathetic, regionally accented voice agents to handle high volumes of inbound calls, reducing labor costs while enhancing user satisfaction.
- **Content Creation & Media**: Publishers and broadcasters can generate multilingual audiobooks, podcasts, and on‑demand announcements with professional‑grade quality.
- **Accessibility**: Educational platforms and assistive devices stand to benefit from clear, engaging voice outputs for learners and users with visual impairments.
- **Smart Devices & IoT**: OEMs can embed Qwen‑TTS into wearables, home assistants, and in‑vehicle infotainment systems to deliver personalized, context‑aware voice interactions.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

To begin, explore models’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key.

The latest integration **Qwen‑TTS** API will soon appear on CometAPI, so stay tuned！While we finalize Qwen‑VLo Model upload, explore our other models on the [Models page](https://www.cometapi.com/model/) or try them in the [AI Playground](https://www.cometapi.com/console/playground). Qwen’s latest Model in CometAPI is [Qwen 3 API](https://www.cometapi.com/qwen-3-api/)(qwen3-235b-a22b;qwen3-30b-a3b;qwen3-8b)

---

*Originally published at [https://www.cometapi.com/alibaba-cloud-unveils-qwen%E2%80%91tts/](https://www.cometapi.com/alibaba-cloud-unveils-qwen%E2%80%91tts/).*
