<!-- social-ops-fingerprint:e79f156c8b0763ed89ddf9c52ca566c96e4e2960d78e72daef8301a42d6f86fd -->
---
title: What Is Qwen3.8-Omni-Flash and How to access
---
# What Is Qwen3.8-Omni-Flash and How to access

![What Is Qwen3.8-Omni-Flash and How to access](https://resource.cometapi.com/Qwen3.8-Omni-Flash.jpeg)

## TL;DR

**Qwen3.8-Omni-Flash** is Alibaba Qwen’s native omni-modal model for text, image, audio, and video understanding, with text as its output modality. Announced on September 18, 2026, it combines a [1M-token context window](https://www.qwencloud.com/models/qwen3.8-omni-flash), native audio-video reasoning, adjustable thinking, function calling, web search, spatial audio understanding, and tool use.

The most important change is not simply better video understanding. Qwen describes the model as its first omni-modal model built around [agentic capabilities](https://x.com/Alibaba_Qwen/status/2100785962414702599): it can understand what it sees and hears, plan what to do next, invoke tools, and work through longer tasks such as vlog editing, video translation, movie recap production, meeting analysis, and multimedia research.

At launch, Qwen reported an [average improvement of more than 25% across 29 evaluations](https://qwen.ai/blog?id=qwen3.8-omni-flash) over Qwen3.5-Omni-Plus. These are vendor-reported launch results rather than independent evaluations.

## Key Takeaways

- **Native omni-modal input:** Qwen3.8-Omni-Flash accepts text, image, audio, and video, while currently returning text.
- **Agentic media workflows:** It can combine media understanding with planning, function calling, and web search.
- **Long context and audio depth:** The hosted model provides a 1M-token context window and supports multilingual, stereo, and first-order ambisonic audio.
- **Vendor-reported benchmark gains:** The largest improvements appear in multimodal agents, long-audio understanding, speaker diarization, and audio grounding.
- **Hosted availability:** The model is available through hosted APIs; Qwen-MM-Plugins is separately open source for multimodal agent workflows.

Developers can access the [Qwen3.8-Omni-Flash API in CometAPI](https://www.cometapi.com/models/aliyun/qwen3-8-omni-flash/) through a unified API workflow.

## What Is Qwen3.8-Omni-Flash?

Qwen3.8-Omni-Flash is Qwen’s next-generation native omni-modal model. Instead of treating audio or video only as preprocessing artifacts, it reasons over text, visual frames, speech, environmental sound, and temporal relationships inside one workflow. Its supported inputs are text, images, audio, and video; its current output is text.

That output distinction matters. The [official Alibaba Cloud documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-8-omni-flash) positions Qwen3.8-Omni-Flash for multimodal understanding and agent execution, while speech-output use cases remain better matched to Qwen Omni variants that explicitly support generated audio.

The launch framing moves from “perceive the media” toward “understand, plan, execute, and deliver.” That makes the model relevant to video editing, multimedia research, meeting analysis, instructional-video processing, and other workflows where the model must do something with media rather than merely summarize it.

### Qwen3.8-Omni-Flash specifications

The specification table below is based on the official Alibaba Cloud and QwenCloud model pages; limits and prices may vary by region and should be rechecked before publication or deployment.

| Specification | Qwen3.8-Omni-Flash — official model page |
| --- | --- |
| Developer | Alibaba Qwen |
| Release | September 18, 2026 |
| Model type | Native omni-modal model |
| Input / output | Text, image, audio, video / text |
| Context window | 1,000,000 tokens |
| Maximum input | 991,808 tokens normal; 983,616 tokens in thinking mode |
| Maximum output | 131,072 tokens |
| Maximum reasoning allowance | Up to 262K tokens on QwenCloud |
| Thinking | Enabled by default; configurable reasoning effort |
| Tools and caching | Function calling, web search, implicit cache, and session cache |
| Audio | 113 languages and dialects; stereo and four-channel FOA |
| API styles | Chat Completions and Responses |
| QwenCloud price | $0.15 input, $0.47 output, and $0.016 implicit-cache input per 1M tokens |
| Open weights | Not announced for this model at launch |

## How Does Qwen3.8-Omni-Flash Work?

QwenCloud states that Qwen3.8-Omni-Flash is built on the [Qwen3.8-Flash-Next architecture](https://github.com/QwenLM/Qwen3.8-Flash-Next). That gives architectural context, but the parameter counts published for Flash-Next should not automatically be presented as the exact parameter specification of the Omni model unless Qwen confirms that mapping.

### Gated DeltaNet + Qwen Sparse Attention

The Flash-Next foundation combines Gated DeltaNet with Qwen Sparse Attention. In simplified terms, the recurrent component compresses historical information into a compact state, while sparse attention retrieves selected long-range context instead of applying dense full attention to every token pair. This is especially relevant for long audio and video streams, where sequence length can dominate computational cost.

### Agentic perception instead of static perception

The larger change is at the system level. Qwen says the model can actively explore long videos and focus on relevant moments rather than spending equal compute on every segment. Conceptually, the agent identifies where evidence is likely to be, inspects those moments more deeply, reasons about them, and then decides which tool or operation should happen next.

## What Are the Main Qwen3.8-Omni-Flash Features?

### Native audio-video reasoning

Qwen3.8-Omni-Flash reasons jointly over the visual and audio streams of a video. That matters when the answer depends on both modalities: identifying who said something, deciding whether a sound happened before or after an action, interpreting music or ambient audio, or connecting spoken instructions to what appears on screen.

### Multi-speaker and spatial audio understanding

The API supports multichannel audio, including two-channel stereo and four-channel first-order ambisonics. Preserving directional information can help with meeting analysis, embodied agents, recorded events, multi-speaker environments, and audio grounding.

### Adjustable reasoning effort

Thinking is enabled by default. Developers can configure reasoning effort to trade latency and token consumption against deeper reasoning for complex multimedia tasks.

### Function calling and web search

Function calling and web search are central to the agentic positioning. After understanding a video, image, or audio file, the model can pass structured arguments to an external tool, retrieve additional information, or continue a workflow outside the model.

### Qwen-MM-Plugins

Qwen also released [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins), an Apache-2.0 toolkit for multimodal-native agent harnesses. Its workflows include video production, video-to-note conversion, learning reusable skills from demonstration videos, and audiovisual memory.

## How Good Is Qwen3.8-Omni-Flash on Benchmarks?

### Is Qwen3.8-Omni-Flash Still Good at Text and Coding?

Qwen’s launch results indicate that the Omni model stays close to the related Flash text model on several coding and reasoning evaluations. Qwen reports 92.6 on LiveCodeBench v6, 63.3 on SWE-bench Pro, and 91.0 on GPQA Diamond. These are vendor-reported results under Qwen’s launch setup and should be validated against the coding tasks and agent harness used in production.

Qwen reports more than a 25% average improvement across 29 evaluations compared with Qwen3.5-Omni-Plus. The following tables summarize the [official launch benchmark results](https://qwen.ai/blog?id=qwen3.8-omni-flash). They are first-party results and had not yet been independently reproduced at publication.

**Evaluation conditions:** Static rows measure a single model run under Qwen’s launch setup. Rows labelled “+ agent” include a surrounding agent harness, retrieval or iterative media inspection. The official launch materials should be consulted for prompt templates, sampling settings, media preprocessing and harness versions; where those details are not disclosed, the result should be treated as vendor-reported rather than independently reproducible.

The larger significance is the shift from multimodal understanding to multimodal execution. Earlier pipelines often transcribed audio, sampled video frames, sent those artifacts to an LLM, produced an answer, and then relied on separate application logic for the actual task. Qwen3.8-Omni-Flash is designed to compress more of that loop into one agent system.

A media-production agent can inspect footage and audio before planning edits. A meeting agent can combine speaker identity with spoken content and presentation visuals. A research agent can locate relevant moments in hours of audiovisual material and then search for external context. In this framing, audio and video become working context for an agent rather than passive attachments.

### Audio-video agents

| Benchmark — official launch source | Qwen3.8-Omni-Flash | Qwen3.5-Omni-Plus | Gemini 3.8 Flash |
| --- | --- | --- | --- |
| WildClawBench-MM | 71.0 | 34.5 | 58.9 |
| UniClawBench | 69.6 | 67.1 | 69.0 |
| AgenticVBench | 36.8 | 14.5 | 45.0 |
| OmniGAIA | 74.0 | — | 78.6 |
| StreamingBench | 80.8 | 57.1 | 79.9 |

The largest generational jump is WildClawBench-MM, where Qwen reports a rise from 34.5 to 71.0. AgenticVBench also improves sharply, while Gemini 3.8 Flash remains ahead on that benchmark. The pattern is therefore not a universal “one model wins everything” result.

### Audio-video understanding and reasoning

| Benchmark | Qwen3.8-Omni-Flash | Qwen3.5-Omni-Plus | Gemini 3.8 Flash |
| --- | --- | --- | --- |
| OmniVideoBench | 63.4 | 53.8 | 65.2 |
| OmniVideoBench + Qwen Code agent | 67.8 | — | 65.2 |
| Video-MME-v2 | 65.0 | — | 71.0 |
| Video-MME-v2 + agent | 71.3 | — | 71.0 |
| LVOmniBench | 63.3 | — | 70.7 |
| LVOmniBench + agent | 73.6 | — | 70.7 |
| JointAVBench | 75.9 | — | 70.4 |

The static rows are mixed. Gemini leads several conventional video-reasoning tests, but Qwen’s result often rises inside an agent loop. That distinction matters only when the production application uses comparable retrieval, tools or iterative inspection.

### Audio and multi-speaker understanding

| Benchmark | Qwen3.8-Omni-Flash | Qwen3.5-Omni-Plus | Gemini 3.8 Flash |
| --- | --- | --- | --- |
| LongAudioSpan | 82.7 | 74.4 | 79.3 |
| AliMeeting DER ↓ | 3.4 | 88.1 | 72.6 |
| AliMeeting cpWER ↓ | 17.2 | 89.6 | 53.1 |
| FLEURS-ASR WER ↓ | 9.3 | 7.2 | 7.9 |
| VoiceBench | 91.6 | 92.9 | 92.3 |

The meeting rows are the standout, while FLEURS-ASR and VoiceBench do not improve over the predecessor. The launch results therefore point to richer multi-speaker, spatial and long-context audio understanding rather than a uniform speech-recognition win.

## Qwen3.8-Omni-Flash vs Qwen3.5-Omni-Plus vs Gemini 3.8 Flash

The table combines Qwen’s official product information with Google’s [official Gemini 3.8 Flash specification](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash). Benchmark comparisons remain Qwen-run and should not be treated as neutral third-party rankings.

| Dimension | Qwen3.8-Omni-Flash | Qwen3.5-Omni-Plus | Gemini 3.8 Flash |
| --- | --- | --- | --- |
| Architecture | Qwen3.8-Flash-Next foundation; exact Omni parameter mapping not disclosed | Previous Qwen Omni generation | Google proprietary Gemini architecture |
| Context window | 1M tokens | Smaller deployment limits | 1,048,576 input tokens |
| Reasoning | Adjustable reasoning effort; thinking enabled by default | No equivalent default-on reasoning mode in the cited deployment | Low, medium and high thinking levels |
| Multimodal input | Text, image, audio, video | Text, image, audio, video | Text, image, video, audio and PDF |
| Output | Text | Text and supported speech workflows | Text |
| Coding | Strong vendor-reported coding scores; not its primary differentiator | Not the main positioning | Designed for long-horizon software engineering and agents |
| API availability | Chat Completions and Responses; hosted API | Hosted Qwen APIs | Gemini API; generally available |
| Tools | Function calling and web search | Function calling and web search | Function calling, search grounding, code execution and other built-in tools |
| Published API pricing | QwenCloud: $0.15 input / $0.47 output per 1M tokens | Region and endpoint dependent | Google introductory price: $0.75 input / $3.75 output per 1M tokens through December 31, 2026 |
| Best fit | Media agents and analysis | Omni conversation and speech output | Broad multimodal, coding and autonomous-agent workflows |

Qwen3.5-Omni-Plus remains relevant when generated speech is required. Qwen3.8-Omni-Flash is more clearly optimized around efficient audio-video understanding plus tool-oriented execution.

Against Gemini 3.8 Flash, Qwen’s evaluation is mixed: Qwen3.8-Omni-Flash is competitive in audio, multi-speaker processing, grounding and several agent workflows, while Gemini leads some static video-reasoning tests. The sensible comparison is workload-specific.

Developers evaluating unified access can compare the [Gemini 3.8 Flash API in CometAPI](https://www.cometapi.com/models/google/gemini-3-8-flash/), [Qwen3.8-Flash API in CometAPI](https://www.cometapi.com/models/aliyun/qwen3-8-flash/), and [Qwen3.8-Flash-Next API in CometAPI](https://www.cometapi.com/models/aliyun/qwen3-8-flash-next/) outside the table so that technical-source links and product-access links remain distinct.

## Limitations of Qwen3.8-Omni-Flash

- **Text-only output:** It understands audio and video but does not generate speech as its response modality.
- **Hosted deployment:** Open weights were not announced for Qwen3.8-Omni-Flash at launch.
- **Fresh benchmarks:** The headline comparisons are primarily first-party results and need independent replication.
- **Agent harness effects:** Some scores include retrieval, tool environments or iterative inspection and should not be confused with raw-model-only results.
- **Workflow-dependent cost:** Long videos can still become expensive if the application repeatedly reprocesses large segments instead of using retrieval, caching or targeted inspection.

## Who Should Use Qwen3.8-Omni-Flash?

Qwen3.8-Omni-Flash is most interesting when audio or video is part of the task itself rather than an attachment that merely needs summarizing. Suitable use cases include meeting intelligence, long-form media search, video translation pipelines, tutorial-to-notes workflows, media-production agents and audiovisual archives.

For conventional text chat, a dedicated Flash text model may remain simpler. For speech-output applications, an Omni model with explicit audio generation may be a better fit. For workflows that combine seeing, hearing, reasoning and acting, Qwen3.8-Omni-Flash is the more distinctive option in the Qwen lineup.

## Conclusion

Qwen3.8-Omni-Flash is best understood as an agentic audio-video model, not simply another multimodal Flash release. Its 1M context, native audio-video reasoning, multi-speaker and spatial-audio capabilities, adjustable reasoning, function calling, search and Qwen-MM-Plugins ecosystem are aimed at the same transition: letting an AI system move from understanding multimedia to doing work with multimedia.

The launch data indicates a substantial generational improvement over Qwen3.5-Omni-Plus, particularly in agentic workflows and complex audio scenarios. Against Gemini 3.8 Flash, Qwen’s own numbers are more balanced. The important question is therefore not which model wins one table, but which model-and-harness combination completes the target workflow accurately and economically.

---

*Originally published at [https://www.cometapi.com/what-is-qwen3-8-omni-flash-and-how-to-access/](https://www.cometapi.com/what-is-qwen3-8-omni-flash-and-how-to-access/).*
