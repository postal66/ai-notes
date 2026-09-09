<!-- social-ops-fingerprint:76245b2ed8ef15f162c5fed67def15aca162fca883add5c86bd3a360ac9e5bab -->
---
title: FLUX 3 API: Availability, Early Access, Video & Dev
---
# FLUX 3 API: Availability, Early Access, Video & Dev

![FLUX 3 API: Availability, Early Access, Video & Dev](https://resource.cometapi.com/flux-3-api-logo.png)

## TL;DR

The FLUX 3 API is not yet generally available as a public production API. Black Forest Labs has announced FLUX 3 and opened Early Access for FLUX 3 Video, while stable model IDs, complete public API specifications, and broader access are still pending.

Developers can apply for Early Access now or continue benchmarking available video APIs while preparing to evaluate FLUX 3 as access expands.

## What Is FLUX 3?

FLUX 3 is Black Forest Labs’ new multimodal foundation model for image, video, audio, and action-related tasks.

Unlike FLUX.2, which focuses primarily on image generation and editing, FLUX 3 is jointly trained across images, video, and audio. According to Black Forest Labs’ [official FLUX 3 announcement](https://bfl.ai/blog/flux-3), the goal is to model visual structure, motion, physical interactions, and sound within a shared architecture rather than treating each modality as a separate system.

For developers, the most important question is whether these capabilities can already be accessed through a production-ready API.

## Is the FLUX 3 API Available Now?

**No, the FLUX 3 API is not generally available as a public production API yet.**

As of July 24, 2026, Black Forest Labs offers an application-based Early Access program, beginning with FLUX 3 Video. Stable production model IDs, complete public API specifications, rate limits, and other production details have not yet been released for general use.

Developers interested in testing the model can apply through the [official FLUX 3 model page](https://bfl.ai/models/flux-3).

### FLUX 3 Availability at a Glance

| Item | Current Status |
| --- | --- |
| Official announcement | Released July 23, 2026 |
| Public FLUX 3 API | Not generally available |
| Stable production model IDs | Not published |
| FLUX 3 Video | Early Access |
| Maximum announced video length | Up to 20 seconds per generation |
| Native audio | Supported |
| FLUX 3 Image | Early Access planned in the following weeks |
| FLUX 3 Action | Selected research and commercial partners |
| FLUX 3 Dev | Open-weight multimodal backbone planned |

Black Forest Labs says the different FLUX 3 capabilities will roll out in phases over the following weeks and months.

The distinction matters: FLUX 3 has been announced and is available to selected Early Access users, but it is not yet a public endpoint that any developer can integrate into production.

## What Can FLUX 3 Video Do?

FLUX 3 Video is the first major FLUX 3 capability to enter Early Access.

According to BFL, it can generate clips with native audio up to 20 seconds long in a single generation. It supports both prompt-only generation and workflows that use images, videos, or audiovisual sequences as references.

### Watch FLUX 3 in Action

This preview offers an early look at FLUX 3’s multimodal capabilities across video, audio, image generation, and action prediction.

<https://www.youtube.com/watch?v=PCPhl8qMF_Y>

Announced capabilities include:

- text-to-video generation;
- image-to-video generation from a starting frame or visual reference;
- video-to-video transformation;
- video and audio continuation;
- keyframe-to-video generation;
- multilingual dialogue;
- audio synchronized with visual events;
- multiple aspect ratios and visual styles;
- chaining clips into longer multi-shot sequences;
- typography and animated design generation.

BFL’s preliminary evaluation used 10-second, 720p text-to-video clips with audio. However, complete production specifications covering supported resolutions, frame rates, codecs, queue behavior, latency, and output formats have not yet been published.

Those details will ultimately determine how practical FLUX 3 Video is for real production workloads.

## What Is FLUX 3 Dev?

FLUX 3 Dev is the planned open-weight version of the FLUX 3 multimodal backbone.

Black Forest Labs describes it as an open-weight backbone intended to support image, video, audio, content-creation, and action-prediction workloads. The company has not yet published its model weights, parameter sizes, hardware requirements, release date, or license terms.

For developers interested in local deployment, fine-tuning, research, or greater control over inference infrastructure, FLUX 3 Dev is the release to watch.

Teams should avoid making infrastructure or licensing plans until BFL publishes the final technical specifications and usage terms.

Follow the [official FLUX 3 page](https://bfl.ai/models/flux-3) for release updates.

## FLUX 3 vs FLUX.2: What Changed?

FLUX 3 represents a broader shift than simply adding video generation to FLUX.2.

| Feature / Dimension | FLUX.2 | FLUX 3 |
| --- | --- | --- |
| Primary focus | Image generation and editing | Multimodal generation and prediction |
| Main modalities | Image | Image, video, audio, and action prediction |
| Temporal modeling | Not a primary focus | Core capability |
| Native video audio | No | Yes |
| Video generation | No | Yes |
| Maximum video length | N/A | Up to 20 seconds per generation |
| Action prediction | Not a primary capability | Planned through FLUX 3 Action for selected partners |
| Open-weight version | FLUX.2 Dev is available | FLUX 3 Dev is planned; specifications are pending |
| Current availability | Released model family | Phased Early Access |

FLUX.2 remains a production image-generation and editing family with managed API variants and an available open-weight Dev version. FLUX 3 expands the architecture into temporal, audiovisual, and action-related workloads.

For teams focused on image generation today, FLUX.2 remains the more practical option.

See CometAPI’s [FLUX.2 overview](https://www.cometapi.com/what-is-flux-2-and-flux-2-is-now-available-on-cometapi/) or [FLUX.2 API integration guide](https://www.cometapi.com/how-to-use-flux-2-api) for current image-generation workflows.

FLUX 3 also extends into action prediction.

In the [FLUX 3 x mimic report](https://bfl.ai/blog/flux-3-mimic), BFL describes FLUX-mimic, a video-action model built on the FLUX 3 backbone in collaboration with mimic robotics. BFL says the system has been tested on production tasks at Audi.

The underlying idea is that a model capable of learning how physical scenes evolve over time may also develop representations useful for predicting robot actions.

This work should be viewed separately from the future content-generation API. FLUX 3 Action is initially intended for selected research and commercial partners.

## What Do the Early FLUX 3 Benchmarks Show?

Black Forest Labs has published preliminary preference evaluations for an early FLUX 3 Video candidate using 10-second, 720p text-to-video clips with audio.

In the published evaluation, FLUX 3 received:

- 52% preference against Seedance 2.0;
- 52% against Gemini Omni Flash;
- 57% against Happy Horse 1.1;
- 59% against Happy Horse v1;
- 60% against Kling v3 Pro;
- up to 69% against Grok Imagine Video;
- 77% against Runway Gen-4.5;
- 93% against Luma Ray 3.2.

![img](https://bfl.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2gpum2i6%2Fproduction%2F30bb456fef266f4b6115a9f209d4b907108ae09e-2880x1800.png&w=3840&q=75)

*Source*\*: Black Forest Labs,\* [FLUX 3: Real World Models](https://bfl.ai/blog/flux-3)*\*\*, July 23, 2026. Results are based on a preliminary evaluation of an early FLUX 3 candidate.*

These results are promising, but BFL notes that both the model and its evaluation harness are still in development. They should therefore be treated as preliminary vendor-run evaluations rather than independent production benchmarks.

Preference scores also do not show how the model performs on API latency, reliability, throughput, technical failures, or consistency across repeated generations.

Once broader FLUX 3 API access becomes available, teams should run the same prompts across FLUX 3 and their existing models under consistent test conditions.

## How Can Developers Access FLUX 3?

As of July 24, 2026, FLUX 3 is available through Black Forest Labs’ application-based Early Access program rather than general public API access.

Developers who want to test the model can apply through the [official FLUX 3 page](https://bfl.ai/models/flux-3).

CometAPI plans to support FLUX 3 after its API availability and integration specifications are officially confirmed. This would allow developers to access FLUX 3 alongside other AI models through the same API infrastructure without building a separate integration from scratch.

In the meantime, teams can continue building with models already available through CometAPI:

| Your Use Case | Recommended Models and Resources |
| --- | --- |
| AI video generation | Start with [Veo 3](https://www.cometapi.com/models/google/veo3/) or explore Seedance, Kling, Sora, Runway, and other models through the [CometAPI Video Generation API](https://apidoc.cometapi.com/api/video). |
| Video with native audio | Evaluate [Veo 3](https://www.cometapi.com/models/google/veo3/) for video generation with synchronized dialogue, sound effects, and ambient audio. |
| Image generation and editing | Use the released FLUX.2 family through the [FLUX.2 API integration guide](https://www.cometapi.com/how-to-use-flux-2-api/) or test [FLUX.2 Pro](https://www.cometapi.com/models/flux/flux-2-pro/). |
| Open-weight workflows | Explore [FLUX.2 Dev](https://www.cometapi.com/flux-2-dev-api/) while waiting for the FLUX 3 Dev weights, license, and hardware requirements. |
| Future FLUX 3 comparison | Build a reusable benchmark using the [evaluation framework below](#how-to-evaluate-the-flux-3-api-after-release), then run the same tests when FLUX 3 access expands. |

This approach lets developers continue shipping today with suitable alternatives while remaining ready to evaluate or integrate FLUX 3 when broader API access becomes available.

## How to Evaluate the FLUX 3 API After Release

Teams interested in FLUX 3 can prepare a benchmark before public API access arrives.

A representative test set should cover the workloads that matter most to the product:

| Test Group | What to Measure |
| --- | --- |
| Prompt adherence | Required objects, actions, camera instructions, and exclusions |
| Character consistency | Identity, clothing, proportions, and voice |
| Physical motion | Contact, weight, trajectories, and continuity |
| Native audio | Lip sync, dialogue accuracy, timing, and ambience |
| Editing and references | Image references, video transformations, keyframes, and continuation |
| Typography and multilingual output | Spelling, layout stability, animation, and language accuracy |

For each request, track:

- prompt and reference assets;
- model and endpoint version;
- resolution, duration, and aspect ratio;
- queue, generation, and delivery latency;
- technical failures and safety rejections;
- human acceptance score;
- common visual, motion, text, and audio failure patterns.

Running important prompts multiple times.

Generative video is stochastic, and one strong output does not necessarily mean a model is reliable enough for production. Repeated testing reveals consistency and failure patterns that polished demos may hide.

When FLUX 3 becomes publicly available, run the same workload against your existing models. This creates a more useful comparison than using different prompts or hand-picked examples for each model.

## What Should Developers Watch Next?

Before treating FLUX 3 as production-ready, watch for five key developments:

1. Stable public API endpoints and production model IDs.
2. Supported resolutions, durations, frame rates, codecs, and native-audio controls.
3. Rate limits, concurrency, queue behavior, and generation latency.
4. Commercial-use, content-moderation, privacy, and data-retention terms.
5. FLUX 3 Dev weights, parameter sizes, hardware requirements, and license details.

These details will determine whether FLUX 3 becomes not only an impressive model family, but also a practical option for production applications.

## FAQ

### Is the FLUX 3 API available?

As of July 24, 2026, FLUX 3 is not generally available as a public API. It is rolling out through a phased Early Access program, and developers can apply through the official [Black Forest Labs FLUX 3 page](https://bfl.ai/models/flux-3).

### How can I access FLUX 3 Video?

Developers and companies can apply for FLUX 3 Video Early Access through the official [FLUX 3 model page](https://bfl.ai/models/flux-3).

### Does FLUX 3 generate video with audio?

Yes. FLUX 3 Video generates native audio alongside video and supports capabilities such as multilingual dialogue, audiovisual continuation, and sounds synchronized with visual events. BFL says a single generation can be up to 20 seconds long.

### What is FLUX 3 Dev?

FLUX 3 Dev is the planned open-weight version of the FLUX 3 multimodal backbone. BFL has not yet published its model weights, parameter size, hardware requirements, release date, or license terms.

### What is the difference between FLUX 3 and FLUX.2?

FLUX.2 focuses on production image generation and editing. FLUX 3 expands into a multimodal architecture covering image, video, native audio, and action prediction.

## Final Thoughts

FLUX 3 is worth watching, particularly for developers interested in video generation with native audio and broader multimodal workflows.

For now, the practical approach is to continue building and benchmarking with available models while preparing a reusable evaluation set. When FLUX 3 API access expands, teams can run the same prompts across models and compare output quality, consistency, latency, reliability, and common failure patterns.

Ready to integrate video generation today? Explore the [CometAPI Video Generation API](https://apidoc.cometapi.com/api/video?) to work with currently available models.

---

*Originally published at [https://www.cometapi.com/flux-3-api/](https://www.cometapi.com/flux-3-api/).*
