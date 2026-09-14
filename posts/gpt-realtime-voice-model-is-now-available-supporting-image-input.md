<!-- social-ops-fingerprint:e9dfdb9b0aa2ff75ca1bf5c873eb8c35890282a4bb7ba2e9de7bc2a1c9342b01 -->
---
title: GPT-Realtime voice model is now available, supporting image input
---
# GPT-Realtime voice model is now available, supporting image input

![GPT-Realtime voice model is now available, supporting image input](https://resource.cometapi.com/blog/uploads/2025/08/GPT-Realtime.webp)

OpenAI today announced that **GPT-Realtime voice model is now available, supporting image input**, marking the Realtime API’s move from beta to general availability for production voice agents. The release positions GPT-Realtime as a low-latency, speech-to-speech model that can run two-way voice conversations while also grounding responses in images supplied during a session.

OpenAI describes *gpt-realtime* as its most advanced speech-to-speech model to date: it processes audio end-to-end (rather than chaining separate speech-to-text and text-to-speech steps), produces more natural and expressive speech, and shows measurable gains in comprehension, instruction following, and function calling. The company highlights improvements on internal benchmarks and says the model captures subtleties such as laughter, mid-sentence language switching, and higher accuracy on alphanumeric content.

## What’s new

- **Image inputs in live voice sessions.** Developers can attach photos, screenshots or other images alongside audio or text; the model can answer visual questions, read text in screenshots (OCR-style), and incorporate scene understanding into the spoken reply. This enables workflows such as visual Q&A during a call or multimodal support for customer service.
- **Speech-to-speech, lower latency, more expressive voices.** GPT-Realtime delivers native audio output with reduced round-trip latency compared with older STT→LLM→TTS chains and ships with expressive voice options (reported as “Cedar” and “Marine” in coverage). The model is tuned for instruction following and conversational nuance.
- **Enterprise integration features.** The Realtime API update adds enterprise-oriented capabilities such as MCP server support and SIP phone calling so voice agents can connect to phone networks and PBX systems directly. These additions are aimed at customer-support and contact-center deployments.

## Benchmarks

**BigBench Audio (reasoning): 82.8%** — up from **65.6%** on OpenAI’s December 2024 realtime model. This is the headline reasoning benchmark reported for audio-capable reasoning tasks.

**MultiChallenge (instruction following, audio): ~30.5%** vs **~20.6%** previously — shows improved adherence to multi-step or complex spoken instructions.

**ComplexFuncBench (function-calling success): ~66.5%** vs **~49.7%** previously — better reliability when the model must call tools/functions during an audio session.

**Cost & latency:** OpenAI states the new model reduces per-token audio cost (≈20% lower than the prior realtime preview) and operates as a single end-to-end model (no separate STT → LM → TTS chain), which lowers end-to-end latency in real-time interactive flows.

OpenAI says the `gpt-realtime` model demonstrates material improvements in a range of objective benchmarks and real-world behaviors — higher scores on BigBench Audio and on instruction-following/function-calling evaluations — and better handling of alphanumerics, codewords and language switching in live audio. The company also introduced two new voices (Cedar and Marin) and reports a 20% price reduction compared with the earlier realtime preview model.

The Realtime API and `gpt-realtime` model are now available to developers (GA),OpenAI also lowered the price of its Realtime API with this update, reducing audio input to $32 per million tokens and audio output to $64 per million tokens, a 20% reduction from the previous price, providing developers with a more economical solution.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access  [GPT-5](https://www.cometapi.com/gpt-5-api/) through CometAPI, the latest models version listed are as of the article’s publication date. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

The latest integration ***`gpt-realtime`*** will soon appear on CometAPI, so stay tuned！

---

*Originally published at [https://www.cometapi.com/gpt-realtime-voice-model-is-now-available-supporting-image-input/](https://www.cometapi.com/gpt-realtime-voice-model-is-now-available-supporting-image-input/).*
