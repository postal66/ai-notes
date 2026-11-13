<!-- social-ops-fingerprint:cd1e83f723746409b0f815757525243d1f78b3081eea016d50005cc9cb36d259 -->
---
title: What is Gemini Omni 1.2 Flash? All You need to know
---
# What is Gemini Omni 1.2 Flash? All You need to know

![What is Gemini Omni 1.2 Flash? All You need to know](https://resource.cometapi.com/console/blog-banner/2026/11/2a326bb8f3344a97812e719279cc73ff.jpg)

## TL;DR

Gemini Omni 1.2 Flash is Google’s video generation and conversational editing model, [released on November 5, 2026](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/). It creates and edits clips up to 15 seconds long and brings the advertised 720p price down by 30%, to about $0.07 per second. For teams making product videos and ads, that means more room to tell a story and a lower cost for trying different versions. You can refine a clip through conversation, then use standalone upscaling to prepare the selected version for delivery.

## What is Gemini Omni 1.2 Flash?

Google describes the model as supporting [video creation and editing through conversation](https://deepmind.google/models/model-cards/gemini-omni-1-2-flash/). Its output includes video with audio, while the broader model description covers text, image, audio, and video inputs.

For reference-driven work, check which inputs your chosen service accepts. Google Cloud makes [audio references available through allowlisting](https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available).

Imagine turning a product photograph into a short ad. Start with a clear view of the product, generate a scene, then ask for a different setting or lighting while keeping the product recognizable. This is where conversational editing becomes useful: you can develop an approved idea over several turns instead of describing the whole scene again for every variation.

### Gemini Omni 1.2 Flash specifications

The following details refer to Google’s enterprise developer documentation. Consumer applications may impose different limits.

| Specification                        | Gemini Omni 1.2 Flash technical details                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| Model ID                             | gemini-omni-1.2-flash                                                                                          |
| Release stage                        | Generally available                                                                                            |
| Release date                         | November 5, 2026                                                                                               |
| Maximum input tokens                 | 131,072                                                                                                        |
| Maximum output tokens                | 260,640                                                                                                        |
| Generation and editing duration      | 3–15 seconds                                                                                                   |
| First-and-last-frame generation      | 3–10 seconds                                                                                                   |
| Extension output per turn            | 3–10 seconds                                                                                                   |
| Aspect ratios                        | 16:9 and 9:16                                                                                                  |
| Resolution options                   | 360p, 720p, 1080p, and 4K                                                                                      |
| Sound generation                     | Speech, music, and sound effects                                                                               |
| Supported generation interface       | Interactions API                                                                                               |
| Chat Completions and GenerateContent | Not supported on this documented surface                                                                       |
| Reference images per prompt          | Up to 10                                                                                                       |
| Image files                          | PNG, JPEG, WebP, HEIC, HEIF; up to 20 MB inline or via console upload, or 30 MB from Cloud Storage             |
| Videos per prompt                    | Up to 3                                                                                                        |
| Video input for editing or upscaling | Up to 15 seconds                                                                                               |
| Video input for extension            | Any duration; uses up to the final 10 seconds                                                                  |
| Video understanding input            | Up to 10 minutes; this does not extend the editing limit                                                       |
| Video input MIME types               | video/x-flv, video/quicktime, video/mpeg, video/mpegs, video/mpg, video/mp4, video/webm, video/wmv, video/3gpp |
| Content provenance                   | SynthID watermarking and C2PA Content Credentials                                                              |

Use the limit for the operation you are requesting. A longer video accepted for understanding is not automatically valid for editing. The [technical specifications](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-2-flash) list the input limits above; [Google’s Content Credentials guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/content-credentials) explains the provenance metadata.

Two distinctions matter when designing an application.

First, a duration selector should depend on the operation. A valid 15-second generation request does not mean a 15-second first-and-last-frame request is valid.

Second, token capacity is not a quality score. It describes an interface limit; it does not establish better motion, stronger prompt adherence, or faster rendering.

## How does Gemini Omni 1.2 Flash rank in independent comparisons?

In Arena’s November 8, 2026 snapshots, Gemini Omni 1.2 Flash ranks first on both the [text-to-video](https://arena.ai/leaderboard/video/text-to-video) and [image-to-video](https://arena.ai/leaderboard/video/image-to-video) leaderboards. Both entries are marked preliminary, so read the scores together with their uncertainty and vote counts.

| Arena category | Score     | Votes | Displayed rank range |
| -------------- | --------- | ----- | -------------------- |
| Text-to-video  | 1540 ± 16 | 1,714 | 1–2                  |
| Image-to-video | 1503 ± 12 | 2,667 | 1–6                  |

These results make the model worth testing, especially for turning prompts or product images into short clips. They do not establish that it will win every production task. The image-to-video rank range is particularly broad: compare your own product details, motion and editing results before choosing a model for a campaign. Rankings can change as more votes arrive.

## **Gemini Omni 1.2 Flash vs Omni 1.1 Flash: what changes?**

The clearest changes are longer clips and lower output pricing. The workflow also deserves attention: reference-based generation, conversational edits and standalone upscaling help you take a useful first draft through to delivery. The table separates explicit version comparisons from capabilities you can use in 1.2.

| Dimension                         | Previous generation: Omni 1.1 Flash                       | Gemini Omni 1.2 Flash launch comparison                           | Practical implication                                                               |
| --------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Maximum native clip               | 10 seconds                                                | 15 seconds                                                        | 50% more duration per clip                                                          |
| Approximate 720p price            | $0.10/second, implied by the announced reduction          | $0.07/second                                                      | Lower output cost at equal duration                                                 |
| Reference adherence               | Comparison baseline                                       | Google reports improvement                                        | Test product identity and fine details                                              |
| Temporal consistency              | Comparison baseline                                       | Google reports less drift                                         | Review intermediate frames, not just endpoints                                      |
| Conversational revisions          | Earlier workflow                                          | Multi-turn editing across full 15-second clips                    | Test whether unrelated details remain stable                                        |
| Independent preference comparison | Arena text-to-video: 1513 ± 15 in the November 8 snapshot | Arena text-to-video: 1540 ± 16, preliminary, in the same snapshot | A higher preference score in this snapshot; not a percentage improvement in quality |
| Standalone upscaling              | Not listed in the current standalone upscaling guide      | Documented separate upscale operation                             | Approve a draft, then upscale the selected video                                    |
| Reference workflow                | Reference-based generation already existed                | Stronger reference adherence reported                             | Build variants around the same product or character                                 |

For teams producing 15-second advertisements, the extra five seconds can fit a hook, demonstration, and closing message into one generation. At equal duration, the lower 720p rate also makes additional creative variations less expensive. The quality improvements are most relevant when the same product or character must remain recognizable throughout the clip.

### Duration and Editing Capabilities

Gemini Omni 1.2 Flash increases the native generation and editing length from **3–10 seconds** in 1.1 to **3–15 seconds** (selectable in 1-second increments). Video input for editing is also extended from 10 seconds to 15 seconds. Multi-turn conversational editing is enhanced, allowing direct modifications to the entire clip (including aspect ratio changes) without full regeneration. Video extension remains 3–10 seconds per turn, with a total length of up to about 30 seconds. First-and-last-frame interpolation is still limited to 3–10 seconds.

### Quality and Consistency Improvements

Version 1.2 offers noticeably better stability for characters, products, clothing, brand colors, faces, and object locking, with reduced drift and fewer jump cuts. Camera movement is smoother and more controllable, lip-sync and speech sound more natural, and multi-speaker conditioning is supported. It follows reference images, short motion clips, and audio cues more reliably. Independent evaluations (such as Arena scores) show 1.2 slightly ahead of 1.1 on both text-to-video and image-to-video.

### Output and Spec Details

Both models support the same resolutions: native 360p / 720p, with upscaling to 1080p / 4K at 24 FPS. Aspect ratios remain 16:9 and 9:16. 1.2 additionally supports text output alongside video with native audio and strengthens standalone upscaling as a dedicated task. Input modalities (text, image, video) and context window size are essentially unchanged.

### Standalone Video Upscaling

Gemini Omni 1.2 Flash can upscale previously generated videos without requiring a new text-to-video generation request. Supported paths include 360p to 720p or 1080p, and 720p to 1080p or 4K. This allows teams to approve composition and motion at a lower resolution before preparing a delivery-ready version.

## How much does Gemini Omni 1.2 Flash cost?

At 720p output, 1.2 Flash is priced at approximately **$0.07 per second** (about $12.00 per million video tokens), which is roughly **30% lower** than 1.1’s \~$0.10 per second ($17.50 per million tokens). 360p drafts are cheaper, and 1080p / 4K upscaled outputs follow the same price reduction. The recommended workflow is to iterate quickly at lower resolutions and upscale only the final keepers to control costs.

| Scenario           | Generations per accepted clip | 15-second 720p output spend |
| ------------------ | ----------------------------- | --------------------------- |
| Efficient workflow | 1                             | $1.05                       |
| Moderate revisions | 2                             | $2.10                       |
| Heavy revisions    | 4                             | $4.20                       |

At the implied previous rate of about $0.10 per second, 100 clips of 15 seconds would cost roughly $150 in output charges. The new rounded rate brings that estimate to $105, a saving of about $45 for the same total duration. These are planning calculations, not a quote for a complete project.

Standalone upscaling has its own output-token usage and reports zero input tokens. Its charge depends on the source and target resolutions, so do not reuse the $0.07-per-second generation estimate for every upscale. See the [upscaling billing rules](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/upscale-videos).

The more useful business metric is **cost per accepted clip**.

For example, if each approved 15-second video requires four separately billed generations, the estimated output spend becomes $4.20 before other costs. A lower retry rate can therefore matter more than a small difference in advertised unit pricing.

## How can developers use Gemini Omni 1.2 Flash?

Use [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-2-flash) for generation and editing on the documented enterprise service. GenerateContent and Chat Completions cannot be used for those operations. Start with a short clip and a simple revision before adding the workflow to a production application.

A straightforward first project is a short product video:

1. Prepare a clear product image and a brief describing the shot, movement, and sound.
2. Generate a short draft through the Interactions API.
3. Request one focused revision, such as a new background, while preserving the product and framing.
4. Review the result before selecting the delivery resolution.
5. Record the request settings and usage so the approved workflow can be repeated.

| Dimension         | Google Cloud native                | CometAPI                                |
| ----------------- | ---------------------------------- | --------------------------------------- |
| Model ID          | gemini-omni-1.2-flash              | omni-fast                               |
| API endpoint      | Interactions API                   | POST /v1/videos                         |
| Billing basis     | Approximately $0.07/second at 720p | $0.40/request in current catalog        |
| Request format    | Interactions API JSON              | Multipart form / JSON depending on task |
| Task handling     | Sync, stateful, streaming, async   | Submit, poll, download                  |
| Version certainty | Explicit 1.2 Flash                 | Published ID does not identify 1.2      |
| API status        | GA                                 | CometAPI endpoint marked Beta           |

The [Gemini Omni Fast API in CometAPI](https://www.cometapi.com/models/google/gemini-omni-fast/) provides a separate integration route under `omni-fast`. Its published identifier does not specify version 1.2 Flash, so use the provider’s documented settings and pricing for that route.

Generated videos include SynthID watermarking, and the documented Google Cloud model surface also supports Content Credentials (C2PA). These provenance mechanisms are useful when publishing AI-generated marketing assets or managing internal content-review workflows.

## What happens to existing Omni 1.1 Flash requests?

1.2 became generally available on November 5, 2026 (model ID: `gemini-omni-1.2-flash`). Starting **December 3, 2026**, requests to `gemini-omni-1.1-flash` will automatically route to 1.2 and be billed at the new lower rates, with no code changes required. Paid-tier rate limits have also been increased.

Test a few representative prompts before that date if your application depends on the earlier model’s behavior. Automatic routing keeps the request path working, but you should still review the resulting videos. For other platforms, use that service’s migration and billing documentation.

## Conclusion

Choose Gemini Omni 1.2 Flash for projects where the creative work continues after the first generation: product variations, seasonal scenes, and short advertisements built around a consistent subject.

Start with one repeatable campaign brief and a small set of reference assets. Once the composition and editing behavior work for that brief, expand to more products or placements. This turns a promising demo into a production process your team can reuse.

## FAQ

### How many reference images can I use with Gemini Omni 1.2 Flash?

The enterprise API accepts up to 10 images per prompt. Use that allowance for distinct views or details that matter to the shot; adding near-duplicate images can make the brief harder to manage. These answers follow Google’s [enterprise technical specifications](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-2-flash); limits in consumer apps may differ.

### How does Gemini Omni 1.2 Flash extend a longer video?

For extension, the model uses up to the last 10 seconds of the input, even when the source video is longer. It generates a 3–10-second continuation, concatenated onto up to the last 30 seconds of the input. Keep the full original in your editing timeline if you need to preserve an earlier sequence; the returned extension should not be treated as a replacement for the complete source.

### Which reference image files does Gemini Omni 1.2 Flash accept?

Supported image formats are PNG, JPEG, WebP, HEIC, and HEIF. Each image can be up to 20 MB for inline data or direct console uploads, or 30 MB when supplied from Google Cloud Storage. Check both format and file size before submitting a request, especially when your source assets are high-resolution product photographs.

---

*Originally published at [https://www.cometapi.com/what-is-gemini-omni-1-2-flash/](https://www.cometapi.com/what-is-gemini-omni-1-2-flash/).*
