<!-- social-ops-fingerprint:da83147e1827f018722100f3d2aa8de99549d825425ad1618a9b7c5484a70602 -->
---
title: How to get started with the Gemini 3 Pro Preview
---
# How to get started with the Gemini 3 Pro Preview

![How to get started with the Gemini 3 Pro Preview](https://resource.cometapi.com/blog/uploads/2025/11/How-to-get-started-with-the-Gemini-3-Pro-Preview.webp)

News about Gemini 3.0 has been the most talked-about topic among developers since August, with constant news reports confidently announcing its release date, only to find that it hasn’t happened. Hopes have been dashed time and again, yet anticipation remains high—because the performance of the Gemini 2.5 Pro has already fallen behind its competitors, Chatgpt and Claude. Now I’ll bring you the latest firsthand news, and I’m happy to announce that it’s now available on [CometAPI](https://www.cometapi.com/).

Google’s next-generation Gemini 3 wave has generated more leak-driven chatter than most product launches — community checkpoints appearing in public benchmarking sites, model names showing up in Google’s own tooling, and an active developer path for trying models via the Gemini CLI and the CometAPI.

## What is Gemini 3.0 — and why is it so highly anticipated?

At a high level, Gemini 3.0 is the **next major iteration** of the Gemini family of large, multimodal AI models developed by Google DeepMind (and its parent Google LLC). The Gemini series is positioned as Google’s flagship line of AI models — built for not just text understanding and generation, but for **multimodal tasks** (text + image + code + audio/video), reasoning, tool-use, and ultimately more agentic behavior.

The reason people are so excited about Gemini 3.0 is that it appears to represent a **major leap forward** — not just a small update — in the model’s capability, context length, reasoning, and real-world usefulness. Community leaks, code references, benchmarking signals and articles suggest that Gemini 3.0 will push into new territory of “thinking models”, longer context windows, deeper multimodal integration and agentic tool orchestration.

Below I’ll walk through exactly *why* it matters, *what we know so far*, and *what is still speculative*.

## What are “lithiumflow” and “orionmist”, and why did they appear on LMArena?

### What did LM Arena and the community find?

On October 19–23, Community investigators found two new LM Arena checkpoints named lithiumflow and orionmist . These names appear consistent with Google’s internal naming conventions (the “orion” family name has been used in past Gemini codenames), and community analysts interpret them as early identifiers or checkpoints for variants of Gemini 3.x — colloquially reported as Gemini 3 Pro / Flash checkpoints.

### Why does it matter?

If lithiumflow and orionmist are true Gemini 3 checkpoints, the split suggests Google may be preparing multiple sub-families( Flash and pro): e.g., a “lithiumflow” variant optimized for throughput and efficiency, and an “orionmist” variant tuned for up-to-date retrieval or multimodal capabilities. Lithiumflow appears (per community speculation) as the base generation model tuned for reasoning/generation (without search-grounding). Orionmist appears to be a variant with integration to external data/real-time search, possibly stronger in retrieval-augmented generation or “live” tasks.

### My test

LM Arena check-ins show *very strong* results for lithiumflow on classical language tasks (reasoning, code, and some SVG/layout tasks). Several community analysts also posted side-by-side comparisons claiming lithiumflow outperforms current public Gemini 2.x and other contemporaries on specific microbenchmarks.

Using Lithiumflow for writing results in better creativity and literary quality than Gemini 2.5, but the word count remains a weakness, only two to three thousand words. Combined with OrionMist, it can rival Claude 4.5 in performance and coding accuracy, but the difference isn’t significant.

Here’s how these models compare in the benchmarks so far:

| Benchmark | Gemini 3.0 (lithiumflow) | Gemini 3.0 (orionmist) | Gemini 2.5 Pro | Claude Opus 4.1 | Claude 3.7 Sonnet |
| --- | --- | --- | --- | --- | --- |
| SimpleBench | 80-100% | 80-100% | 62.4% | 60.0% | 46.4% |

Both models still exhibited illusions and instabilities in certain knowledge tasks—understandable for an early preview. This pattern (excelling in creative tasks and generating excellent structure/code, but occasionally exhibiting factual errors) is common when models are combined with novel multimodal or code generation capabilities.

> The testing of these two models has been closed at LM Arena, further confirming that they are indeed Gemini 3.0.

## Apple’s Involvement and Leaked Specifications

### Model differences

In mid-2025, **Apple** reportedly leaked code snippets in a beta iOS build showing identifiers such as `com.google.gemini_3_pro` and `gemini_3_ultra`.
Analysts inferred that Google and Apple were preparing **Gemini-powered “Apple Intelligence” integrations**, likely for Siri and on-device summarization:

- Gemini 3 Pro (cloud-based reasoning layer)
- Gemini 3 Nano (on-device variant)
- Real-time multimodal inference

This aligns with Google’s push for an **AI fabric** connecting mobile devices, cloud APIs, and the web ecosystem.

### Specification leak

Apple and Google negotiating deeper Gemini integration for Apple Intelligence/Siri — scoop describes Apple planning to use a custom Gemini variant in its AI stack. Apple and Google mentioned the 1.2T parameter in their collaborative plan for artificial intelligence models, which may be the specification of Gemini 3.0.

![How to get started with the Gemini 3 Pro Preview](https://resource.cometapi.com/blog/uploads/2025/11/20251106-202001-639x1024.jpg)

## How to get started with the Gemini 3 Pro Preview

 Based on available information and testing, I will provide three methods: Vertex, gemini CLI, and API. Developers can choose the method that best suits their needs and environment. The Gemini 3.0 pro model name is gemini-3-pro-preview-11-2025 and gemini-3-pro-preview-11-2025-thinking.

### Accoss Vertex

Gemini 3.0 pro (`gemini-3-pro-preview-11-2025)` has been added to Vertex’s model list, and some users in the community claim that they can test it directly, provided they have a paid Vertex account and can access it using their account credentials, Indeed, traces can be found in Vertex’s network logs:

![How to get started with the Gemini 3 Pro Preview](https://resource.cometapi.com/blog/uploads/2025/11/screenshot-20251106-211259-1024x513.webp)

### Accoss Gemini cli

Gemini 3.0 pro can also be called within the Gemini CLI, but the model needs to be manually specified when using it manually. Most of the latest reviews of Gemini 3.0 Pro currently come from the use of the Gemini CLI. However, it has some drawbacks: it only works with some North American nodes, requiring you to manually change your local IP address to try, and you may need to try multiple times. It’s not very stable and will return a 404 error when it fails.

You need to [install the Gemini CLI locally](https://www.cometapi.com/google-gemini-cli-tutorial-how-to-install-and-use-it-via-cometapi/), then authenticate with an account that has access permissions (google account / CometAPI account), and manually specify the model name “`gemini-3-pro-preview-11-2025`” to use Gemini 3.0 pro-preview, Example: install and run (shell)

```
```bash
# instant run (no install)

npx https://github.com/google-gemini/gemini-cli
```

or install globally:

```
npm install -g @google/gemini-cli
# or on macOS/Linux using Homebrew

brew install gemini-cli
```

```
The CLI accepts model identifiers the same way the API does. Practically: set your model identifier (for example `model: "gemini-3-pro-preview-11-2025"`) in a CLI request or configuration and invoke it — if your account has access, the request will succeed.

![](https://resource.cometapi.com/blog/uploads/2025/11/20251106-213209-1024x649.webp)

### Accoss CometAPI’s API

[CometAPI](https://www.cometapi.com/) is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling.

CometAPI has integrated the [Gemini 3 Pro Preview API](https://www.cometapi.com/gemini-3-pro-api/) , and the internal API call name is  `gemini-3-pro-preview`. When making the call, you only need to change the request address to `https://api.cometapi.com/v1/chat/completions`.

You can call Gemini 3.0 pro preview in the same way as calling the OpenAI API. In my tests, calling via CometAPI is more stable than using the Gemini CLI.

## What are the predicted characteristics of Gemini 3.0?

Below are the most-discussed capabilities (explicitly flagging which items are confirmed vs. community/analyst expectations).

### Core design & architecture (confirmed vs. expected)

- **Multimodal foundation:** Gemini is built as a multimodal family (text, images, code, audio/video), and Google has already published multimodal models and tools in the Gemini API. This is confirmed and will continue to be central.
- **Advanced reasoning / planning:** Expect deeper integration of planning and RL techniques informed by DeepMind research — a likely difference in design emphasis compared with some competitors. This is an expectation grounded in DeepMind’s history rather than a public spec.

### Context window and memory

Longer context windows: Gemini 3.0 to increase effective context capacity (discussions speculate in the millions of tokens), building on earlier large-context work. This is a prediction — Google has not published official Gemini 3.0 token limits yet.

### Performance, latency and model variants

- **High reasoning and coding accuracy:** Community LM Arena posts for “lithiumflow” (and “orionmist”) suggest strong performance on reasoning and code tasks. These are unverified community benchmarks but are the main reason for excitement. Treat them as early signals, not definitive proof.
- **Multiple variants:** Rumors and leak reports point to different flavors — a raw generation/“Pro” variant (often associated in posts with the lithiumflow tag) and a grounded/search-enabled variant (orionmist). Again, these are community inferences from model IDs and test behavior.

### Multimodality and new capabilities

- **Video and image integration:** Google has recently exposed video models (e.g., Veo 3) and image capabilities in the Gemini API; Gemini 3.0 is expected to leverage and unify these for richer multimodal workflows. This is supported by prior Google releases in the Gemini ecosystem.
- **On-device and privacy features (goal):**It expects more efficient, on-device or private-cloud options for sensitive data, because Google and partners emphasize privacy and lower latency. This is a prediction informed by ecosystem trends; specifics for Gemini 3.0 are not yet public.

## Bottom line

Gemini 3.0 pro-preview is widely expected to be a step-change for Google’s multimodal, reasoning-focused models — potentially offering longer context, stronger planning and richer multimodal capabilities. The current excitement is a mix of **confirmed developer tooling and Google product signals** (gemini API, CLI, Veo/video models) and **unofficial but noisy community signals** (LM Arena entries for lithiumflow/orionmist, leaks and analyst rumor timelines). Treat the community benchmarks as early indicators and prepare by learning the Gemini developer tools so you can evaluate the model objectively when Google releases official access.

I speculates that the most likely official release date is November 18th, which coincides with Google’s model migration plan on the 18th. Let’s look forward to more information about the Gemini 3 Pro Preview!

### Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access Gemini 3.0 pro- preview through CometAPI, [the latest model version](https://api.cometapi.com/pricing) is always updated with the official website. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://api.cometapi.com/doc) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://api.cometapi.com/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!
```

---

*Originally published at [https://www.cometapi.com/how-to-get-started-with-the-gemini-3-pro-preview/](https://www.cometapi.com/how-to-get-started-with-the-gemini-3-pro-preview/).*
