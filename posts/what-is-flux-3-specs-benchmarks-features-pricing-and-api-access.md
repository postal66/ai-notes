<!-- social-ops-fingerprint:f15b3712f0108cf72396227d1d8d2714d2b610bf30599828644dc4bb27456a72 -->
---
title: What Is FLUX 3? Specs, Benchmarks, Features, Pricing and API Access
---
# What Is FLUX 3? Specs, Benchmarks, Features, Pricing and API Access

![What Is FLUX 3? Specs, Benchmarks, Features, Pricing and API Access](https://resource.cometapi.com/1281b2003f8a62e07391c6085a69ed91eb574d08c-1900x1264.png)

**TL;DR:** FLUX 3 is Black Forest Labs’ unified multimodal foundation model. Its publicly available Video API generates clips of up to 20 seconds at 24 fps, with optional synchronized audio, from text, images, keyframes, or existing video. It supports resolutions from HD through UHD/4K, while FLUX 3 Image and the open-weight FLUX 3 Dev model remain separate rollout items.

## What Is FLUX 3?

[FLUX 3](https://www.cometapi.com/models/flux/flux-3/) is a frontier multimodal model from Black Forest Labs. Instead of independently training one model for images, another for video, and another for audio, BFL trains a shared representation across these modalities.

The central idea is that images, video, and sound are different observations of the same underlying world. A moving car has visual appearance, motion, sound, spatial relationships, material properties, and causal behavior. Learning these signals together gives the model more constraints than learning individual frames alone.

This is why Black Forest Labs describes FLUX 3 as a step toward a [reality model or world model](https://bfl.ai/blog/flux-3) rather than merely an image or video generator. The released video system already demonstrates that direction: synchronized audio, motion, scene structure, dialogue, camera behavior, and environmental sounds are handled in one generation workflow.

Not every announced FLUX 3 capability is publicly available yet. As of September 2026, FLUX 3 Video is available, while FLUX 3 Image and the open-weight FLUX 3 Dev model remain separate rollout items.

## FLUX 3 Specifications at a Glance

The following specifications reflect the current FLUX 3 developer documentation rather than the preliminary July launch configuration.

| Specification | Official FLUX 3 documentation |
| --- | --- |
| Developer | Black Forest Labs |
| Model family | FLUX 3 |
| Model type | Unified multimodal foundation / generative video model |
| Public video release | August 4, 2026 |
| Core training direction | Joint image, video, and audio representation learning |
| Research foundation | Self-Flow |
| Current primary API output | Video with synchronized audio |
| Text-to-video | Supported |
| Image-to-video | Supported |
| Keyframe-to-video | Supported |
| Video continuation | Supported |
| Maximum T2V/I2V duration | 20 seconds |
| Video continuation duration | 5–15 seconds |
| Frame rate | 24 fps |
| Resolution | HD, FHD, QHD/2K, and UHD/4K |
| FHD 16:9 resolution | 1920 × 1088 |
| Image references | Up to 10 for I2V/keyframe workflows |
| Native audio | Yes |
| Multilingual dialogue | Yes |
| Lip synchronization | Yes |
| Multi-shot generation | Yes |
| Draft Mode | Yes |
| Public still-image FLUX 3 endpoint | Not yet generally released by BFL |
| Open-weight FLUX 3 Dev | Planned |

Current BFL documentation specifies 5–20 seconds for text-to-video and image-to-video, while video continuation accepts a 5–15-second generation window. Supported aspect ratios include 21:9, 2:1, 16:9, 4:3, 1:1, 3:4, and 9:16.

## How Does FLUX 3 Work?

### Self-Flow

The key research foundation is [Self-Flow](https://black-forest-labs.github.io/Self-Flow/), Black Forest Labs’ self-supervised flow-matching approach. Traditional generative training pipelines often rely on separate pretrained representation models or auxiliary supervision. Self-Flow is designed to learn useful representations directly from the generative objective.

A major mechanism is [Dual-Timestep Scheduling](https://black-forest-labs.github.io/Self-Flow/). Different groups of tokens can be assigned different noise levels during training. This creates information asymmetry: some parts of the input contain more usable information than others, forcing the network to build representations that help infer what is missing.

In practical terms, FLUX 3 is encouraged to learn relationships between objects, frames, motion, sound, and temporal events rather than simply memorizing how individual frames should look.

![What Is FLUX 3? Specs, Benchmarks, Features, Pricing and API Access](https://resource.cometapi.com/6e1bc87-c966-4886-997b-fa8063a5f4e1.png)

*Self-Flow method architecture - official image source:* [Black Forest Labs Self-Flow project](https://black-forest-labs.github.io/Self-Flow/architecture.webp)

BFL also tested joint multimodal training using a FLUX.2-derived backbone with millions of videos and hundreds of millions of images. The experiments support the broader FLUX 3 hypothesis that representation learning and generation do not need to be separate systems.

### Why Video Is Central to FLUX 3

Video is particularly valuable for world modeling because it contains information that a still image cannot provide. A single frame can show a ball above the floor; a video can reveal that the ball is falling, bouncing, deforming on impact, making a sound, and changing direction afterward.

BFL disclosed that video prediction accounts for [more than 95%](https://bfl.ai/blog/flux-3-mimic) of FLUX 3’s training compute. Audio is comparatively inexpensive because it is a much lower-dimensional signal closely coupled to visible events. That allocation helps explain why video is the first FLUX 3 capability to reach general availability.

## What Can FLUX 3 Do?

### Text-to-Video

Users can generate a complete video from natural-language instructions. BFL says the released model handles simple and complex prompts while coordinating movement, scene logic, visual composition, and sound. This is especially useful for prompts that contain multiple sequential events rather than a single animated subject.

### Image-to-Video and Keyframes

FLUX 3 can animate an initial image, work toward an end frame, or use multiple images as timed keyframes. The current API supports [up to ten image references](https://docs.bfl.ai/flux_3/flux3_overview) in image-to-video workflows, allowing creators to control how a scene changes over time rather than asking the model to improvise the entire sequence.

### Video Continuation

An existing video and its audio can be supplied as context and FLUX 3 can generate what happens next. BFL describes continuation that preserves movement, camera behavior, dialogue, and sound across the transition, which is materially different from generating a second independent clip and joining both files afterward.

### Native Audio and Dialogue

FLUX 3 produces audio at generation time instead of requiring a separate speech or sound-generation pass. Its released audio capabilities include [dialogue](https://bfl.ai/blog/flux-3-video), sound effects, and ambient sound. Multilingual dialogue with lip synchronization is also supported.

### Multiple Shots in One Generation

A single prompt can contain [multiple scenes or camera angles](https://bfl.ai/blog/flux-3-video). This matters because many earlier video models are strongest when asked for one short, visually continuous shot; FLUX 3 is explicitly designed to support multi-shot sequences within one generation.

### Draft Mode

Draft Mode is one of the more practical additions for high-volume video generation. Instead of paying full price for every prompt experiment, developers can create a faster, lower-cost preview and then enhance the selected draft while preserving the chosen composition and motion. According to [current BFL pricing](https://docs.bfl.ai/flux_3/flux3_overview), a standard T2V/I2V draft costs $0.06 per second, versus $0.17 per second for regular HD generation.

## What Has Not Shipped Yet?

FLUX 3’s launch announcement described image, video, audio, and action capabilities under one architectural direction, but availability is staggered.

| Capability | Current BFL roadmap and availability |
| --- | --- |
| FLUX 3 Video generation | Generally available |
| Native video audio | Generally available |
| Text-to-video | Generally available |
| Image-to-video / keyframes | Generally available |
| Video continuation | Generally available |
| Richer image/video/audio reference combinations | Planned expansion |
| FLUX 3 Image generation and editing | Upcoming |
| FLUX 3 Dev open weights | Planned |
| Action-prediction deployment | Research / commercial partner track |

This distinction is especially important for users familiar with [FLUX.2 Max](https://www.cometapi.com/models/flux/flux-2-max/). FLUX.2 remains a current dedicated option for still-image generation, while the public FLUX 3 product is centered on video and audio.

## FLUX 3 Benchmark Performance

There are now two useful kinds of FLUX 3 benchmark evidence: BFL’s post-release internal evaluation and independent third-party evaluation. The first shows relative human preference under BFL’s protocol; the second checks whether those strengths remain visible under a separately designed benchmark.

### BFL Post-Release ELO Evaluation

The initial July announcement included preliminary win rates. The more relevant benchmark for current users is BFL’s August 4 [evaluation of the released model](https://bfl.ai/blog/flux-3-video). Black Forest Labs reports a text-to-video ELO score of 1135 in its internal all-vs-all evaluation.

![What Is FLUX 3? Specs, Benchmarks, Features, Pricing and API Access](https://resource.cometapi.com/04ece45b-48f7-442b-9df5-72004b6f8023.png)

*FLUX 3 released-model ELO evaluation - official image source:* [*Black Forest Labs*](https://bfl.ai/blog/flux-3-video)

| Metric | BFL released-model evaluation |
| --- | --- |
| Text-to-video ELO | 1135 |
| T2V position | Highest score in BFL’s tested group |
| Image-to-video result | Tied the strongest tested competitor and beat the remaining evaluated models |
| Evaluation type | Internal human-preference evaluation |
| Model stage | Generally available FLUX 3 Video release |

This is stronger evidence than the preliminary launch benchmark because it evaluates the released August model. It is still a vendor-run benchmark, however, and should not be interpreted as proof that FLUX 3 will outperform every competitor on every prompt category.

### Independent FLUX 3 Benchmark

Megaton’s v-benchmark v2 provides an independent check. FLUX 3 was evaluated in August 2026 and currently posts a 76.51/100 Megaton Index, ranking #3 in the published set at the time of evaluation.

| Benchmark dimension | Megaton FLUX 3 evaluation |
| --- | --- |
| Megaton Index | 76.51 |
| Prompt Adherence | 87.07 |
| Scene Consistency | 94.76 |
| Physics | 70.63 |
| Human Fidelity | 73.70 |
| Object & Product Fidelity | 83.82 |
| Causal & Semantic Coherence | 80.91 |
| Text Fidelity | 82.41 |
| Cinematography | 71.43 |
| Taste & Art Direction | 65.00 |

The profile is more informative than the overall score. Scene Consistency at 94.76 is the strongest major category, while Prompt Adherence, object fidelity, causal coherence, and text fidelity also exceed 80. Physics, Human Fidelity, and Taste & Art Direction are weaker, showing that stronger temporal representation does not eliminate synthetic motion or artistic-quality variation.

This also explains why benchmark conclusions can differ: BFL’s internal preference test puts FLUX 3 at the top of its comparison set, while Megaton’s independent leaderboard places it third. Different prompts, scoring dimensions, evaluator populations, and aggregation methods can produce different rankings.

## FLUX 3 vs Seedance 2.5 vs MiniMax H3 vs Wan 3.0

The AI video market moved quickly in 2026. FLUX 3 now competes with multimodal systems that increasingly combine long-form generation, synchronized audio, references, and editing.

| Dimension | FLUX 3 | Seedance 2.5 | MiniMax H3 | Wan 3.0 |
| --- | --- | --- | --- | --- |
| Developer | Black Forest Labs | ByteDance Seed | MiniMax | Alibaba |
| Maximum advertised clip | 20 s | 30 s | 15 s | 30 s |
| Video resolution | HD / FHD / QHD (2K) / UHD (4K) | API tier dependent | Up to 2K | Up to 1080p |
| Native audio | Yes | Yes | Yes, stereo | Yes |
| Text-to-video | Yes | Yes | Yes | Yes |
| Image/reference input | Yes | Yes | Yes | Yes |
| Keyframe/reference control | Strong timed keyframes | Strong multimodal reference control | Multimodal conditioning | Multimodal reference control |
| Video continuation/editing | Continuation available | Editing-oriented workflow | Omni generation focus | Editing and reference workflows |
| Multi-shot generation | Yes | Yes | Yes | Yes |
| Distinctive strength | Reality-model architecture, scene consistency, Self-Flow | Long-form storytelling and reference control | 2K audiovisual generation and omni-modal context | Long clips and lower starting cost |
| CometAPI starting/unit price\* | $0.136/s | $0.0824/s listed | $0.064/s | $0.040/s |

**\* Pricing is a rough comparison only.** Video APIs use different resolutions, durations, quality tiers, and billing rules, so the cheapest per-second number is not necessarily the cheapest equivalent-quality output.

### FLUX 3 vs Seedance 2.5

Seedance 2.5 has an obvious duration advantage, with up to 30-second generation compared with FLUX 3’s 20 seconds. It is also strongly oriented toward reference-driven generation, editing, and long-form storytelling. FLUX 3 differentiates through its shared world-model architecture, scene consistency, native audiovisual generation, timed keyframes, and broader image/action roadmap.

Independent testing reinforces that this is a genuine high-end competition: Megaton currently [places Seedance 2.5 above FLUX 3](https://megaton.ai/compare/seedance-2-5-vs-flux-3) overall.

### FLUX 3 vs MiniMax H3

MiniMax H3 offers up to 2K output and native stereo audio, giving it a strong technical specification for audiovisual content. FLUX 3 supports a longer maximum generation window—20 seconds versus H3’s 15 seconds—and its Draft Mode provides a cost-controlled iteration workflow.

### FLUX 3 vs Wan 3.0

Wan 3.0 emphasizes broad multimodal inputs, audiovisual generation, editing, and clips up to 30 seconds. It is also cheaper at CometAPI’s listed starting price. FLUX 3 is more expensive but differentiates through its reality-model positioning, scene consistency, Self-Flow research foundation, Draft Mode, and integration with action prediction.

## FLUX 3 Pricing

Black Forest Labs charges FLUX 3 by generated video duration.

| Mode | Official BFL FLUX 3 pricing |
| --- | --- |
| T2V / I2V Draft HD | $0.06/s |
| T2V / I2V HD | $0.17/s |
| T2V / I2V FHD | $0.29/s |
| T2V / I2V QHD (2K) | $0.40/s |
| T2V / I2V UHD (4K) | $0.80/s |
| Video continuation Draft | $0.12/s |
| Video continuation HD | $0.41/s |
| Video continuation FHD | $0.53/s |
| Video continuation QHD (2K) | $0.65/s |
| Video continuation UHD (4K) | $0.95/s |

A standard 10-second HD generation therefore costs approximately $1.70 at BFL’s listed rate, while a 10-second FHD generation costs approximately $2.90. Video continuation is substantially more expensive than ordinary generation, so applications that frequently extend clips should model those costs separately.

### FLUX 3 Price on CometAPI

CometAPI currently [lists FLUX 3 as available](https://www.cometapi.com/models/flux/flux-3/) with model ID flux-3.

| Resolution | CometAPI FLUX 3 pricing |
| --- | --- |
| 720p | $0.136/s |
| 1080p | $0.232/s |

For a 10-second generation, that corresponds to approximately $1.36 at 720p or $2.32 at 1080p. Compared with BFL’s listed $0.17/s and $0.29/s rates, the default CometAPI prices are about 20% lower for these two tiers.

*Availability note: some older descriptive copy on CometAPI still reflects the July Early Access period. The current* [*live model card*](https://www.cometapi.com/models/flux/flux-3/)*, pricing section, and API example list flux-3 as Available, with a CometAPI release date of August 13, 2026. For integration decisions, the live API and pricing fields are more relevant than the older availability copy.*

## Why FLUX 3 Matters Beyond AI Video

The most unusual part of FLUX 3 is not 20-second video generation. Several competitors can already generate equally long or longer clips. The larger technical bet is that a strong video representation can become a foundation for other forms of intelligence.

### From Video Prediction to Action Prediction

Robot-control signals are temporal predictions conditioned on visual observations, so BFL uses the FLUX 3 video representation as a foundation for action prediction. Its collaboration with mimic robotics produced FLUX-mimic, in which an action decoder reads representations from the video model instead of training an entirely independent perception stack.

BFL reports that the FLUX-mimic backbone can run in [under 80 ms](https://bfl.ai/blog/flux-3-mimic) on a single RTX 5090, while the complete robot system reaches a roughly 101 ms reaction loop. The company has also discussed industrial evaluation with Audi.

This does not make the public FLUX 3 Video API a robotics API. It does demonstrate why BFL invested heavily in multimodal video representation instead of treating video generation as an isolated media task.

## What Are FLUX 3’s Main Strengths?

- **Temporal and scene consistency.** Megaton’s 94.76 Scene Consistency score is the model’s strongest major benchmark category.
- **Native audiovisual generation.** Dialogue, effects, ambience, and visuals can be generated together rather than stitched together from separate models.
- **Strong prompt adherence.** The independent Prompt Adherence result of 87.07 suggests the model’s strengths extend beyond pure visual polish.
- **Keyframe control.** Up to ten images can participate in current image-to-video workflows, giving creators explicit temporal control.
- **Draft-to-final workflow.** Draft Mode addresses a real cost problem in AI video: many generations are discarded during prompt iteration.
- **Broad visual range.** BFL positions FLUX 3 as capable of raw, natural, cinematic, nostalgic, playful, stylized, and unusual outputs rather than one fixed house style.
- **World-model research direction.** Self-Flow and action prediction make FLUX 3 relevant beyond media generation.

## What Are FLUX 3’s Limitations?

- **The full multimodal roadmap has not shipped.** Public FLUX 3 Image and FLUX 3 Dev open weights should not be assumed from the family-level announcement.
- **20 seconds is no longer industry-leading duration.** Some 2026 competitors already support 30-second generations.
- **Physics is not solved.** Megaton gives FLUX 3 a Physics score of 70.63, considerably below its scene-consistency score.
- **Human fidelity still has room to improve.** A 73.70 independent score means difficult anatomy and realistic human motion can still fail.
- **Video continuation is expensive.** BFL’s continuation price is substantially higher per second than ordinary T2V/I2V.
- **BFL’s headline competitive benchmark is internal.** Production decisions should also include independent tests using the application’s own prompts, shot types, languages, and reference assets.

## How to Use FLUX 3 with CometAPI

CometAPI's [earlier FLUX 3 coverage](https://www.cometapi.com/flux-3-api/) explains the July Early Access phase, preliminary benchmarks, and planned rollout. This section focuses on the current production integration, pricing, and working API flow so it does not repeat that historical walkthrough. The [FLUX 3 production model](https://www.cometapi.com/models/flux/flux-3/) uses the model ID flux-3.

A basic 720p request uses the /v1/videos endpoint:

**Bash**

| curl --request POST "`https://api.cometapi.com/v1/videos`" \  --header "Authorization: Bearer $COMETAPI\_KEY" \  --form-string "model=flux-3" \  --form-string "prompt=A paper boat glides across a still pond in soft morning light" \  --form-string "seconds=5" \  --form-string "size=1280x720" |
| --- |

The video workflow is [asynchronous](https://www.cometapi.com/models/flux/flux-3/). After the initial request returns a task ID, the application checks the task until generation is complete and then retrieves the resulting video. For production applications, generation should normally be handled by a background job or task queue rather than holding an HTTP request open for the full render time.

## Who Should Use FLUX 3?

FLUX 3 is particularly compelling for applications that need more than visually attractive five-second clips: advertising systems with synchronized visuals and audio, automated short-form production, product demonstrations where object persistence matters, multilingual dialogue generation, storyboard-to-video workflows, keyframe-controlled animation, educational content, and experiments with longer multimodal pipelines.

It may be less attractive when the only requirement is the lowest possible cost per second, when more than 20 seconds must be generated in one pass, or when still-image generation is the primary task. For still images, an existing FLUX image model such as [FLUX.2 Max](https://www.cometapi.com/models/flux/flux-2-max/) may currently be a better fit.

## Is FLUX 3 Better Than Other AI Video Models?

There is no single defensible answer across every use case. BFL’s internal evaluation places the released FLUX 3 at the top of its text-to-video comparison, while independent Megaton evaluation places [FLUX 3](https://www.cometapi.com/models/flux/flux-3/) third overall behind newer competitors. Both results can be valid because the tests measure different prompt distributions and quality dimensions.

FLUX 3 appears particularly strong when scene consistency, prompt following, object fidelity, causal coherence, text rendering, synchronized sound, and controllable keyframes matter. Other models may win on maximum duration, resolution, artistic preferences, human fidelity, editing workflows, or cost. For developers, the correct comparison is workload-specific rather than leaderboard-specific.

## Frequently Asked Questions

### Is FLUX 3 available now?

Yes. FLUX 3 Video became generally available through BFL on August 4, 2026. [CometAPI also lists FLUX 3 as Available](https://www.cometapi.com/models/flux/flux-3/) under the model ID flux-3. The still-image FLUX 3 release and FLUX 3 Dev open weights remain separate roadmap items.

### Can FLUX 3 generate audio?

Yes. FLUX 3 Video generates synchronized native audio including dialogue, ambient sound, and effects. Multilingual dialogue and [lip synchronization](https://bfl.ai/blog/flux-3-video) are also supported.

### How long can FLUX 3 videos be?

Current text-to-video and image-to-video generation supports 5–20 seconds. Video continuation supports 5–15 seconds of newly generated content.

### What resolution does FLUX 3 support?

BFL supports HD (up to 1 megapixel per frame), FHD (up to 2 MP), QHD/2K (up to 4 MP), and UHD/4K (up to 8 MP). A 16:9 FHD output is 1920 × 1088. Resolution bands are based on total pixels per frame rather than aspect ratio; Draft Mode is HD only.

### Does FLUX 3 support image-to-video?

Yes. [Image-to-video and keyframe generation](https://docs.bfl.ai/flux_3/flux3_overview) are part of the generally available FLUX 3 Video feature set.

### Is FLUX 3 an image-generation model?

Architecturally, FLUX 3 is trained across images, video, and audio, and BFL has demonstrated image-generation and editing research. However, the FLUX 3 Image product remains an upcoming release; do not confuse the family roadmap with the currently public FLUX 3 Video API.

### Is FLUX 3 open source?

Not currently. BFL has announced [FLUX 3 Dev](https://bfl.ai/blog/flux-3), an open-weight multimodal variant, but has not yet provided a public release date.

### How much does FLUX 3 cost?

BFL prices text/image-to-video at $0.06/s for Draft HD, $0.17/s for HD, $0.29/s for FHD, $0.40/s for QHD, and $0.80/s for UHD. Video-to-video costs $0.12/s for Draft HD, then $0.41/s for HD, $0.53/s for FHD, $0.65/s for QHD, and $0.95/s for UHD. CometAPI currently lists $0.136/s for 720p and $0.232/s for 1080p.

### What is Self-Flow?

Self-Flow is BFL’s self-supervised flow-matching research approach. It is designed to let a generative model develop useful internal representations without depending on an external representation model. Its use of different noise levels across tokens encourages the network to infer missing information and learn relationships among multimodal observations.

### Is FLUX 3 a world model?

Black Forest Labs positions FLUX 3 as a reality-model foundation because its shared representations extend from audiovisual prediction toward physical action prediction. Calling it a complete general-purpose world model would be stronger than the evidence currently supports; a more precise description is a multimodal generative foundation model explicitly designed around world-modeling objectives.

## Conclusion

FLUX 3 represents a larger change for Black Forest Labs than a conventional upgrade from one FLUX image model to another. Its key idea is to train a shared multimodal representation of the world, then use that representation for video, sound, images, and eventually actions. Self-Flow provides the research foundation, while the released FLUX 3 Video model is the first production demonstration of that strategy.

As of September 2026, FLUX 3 Video supports clips up to 20 seconds, 24 fps, HD through UHD/4K output, synchronized audio, multilingual dialogue, image-to-video, keyframes, video continuation, multi-shot generation, and Draft Mode.

The benchmark picture is also more credible than it was at launch. BFL’s current released-model evaluation puts FLUX 3 first in its internal T2V ELO test, while independent Megaton testing ranks it third overall and highlights particularly strong scene consistency.

[FLUX 3](https://www.cometapi.com/models/flux/flux-3/) is therefore not automatically the best video model for every workload. [Seedance 2.5](https://www.cometapi.com/models/doubao/seedance-2-5/), [MiniMax H3](https://www.cometapi.com/models/minimax/minimax-h3/), and [Wan 3.0](https://www.cometapi.com/models/aliyun/wan3-0/) can offer longer generation, higher nominal resolution, lower pricing, or different reference and editing capabilities.

What makes FLUX 3 unusually interesting is the direction underneath the video generator: BFL is betting that the same representations required to predict convincing video can eventually support image generation, audio, physical reasoning, and robot actions. Developers can already test the first production step through FLUX 3 on CometAPI using the flux-3 model ID.

---

*Originally published at [https://www.cometapi.com/what-is-flux-3/](https://www.cometapi.com/what-is-flux-3/).*
