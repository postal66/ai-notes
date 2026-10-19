<!-- social-ops-fingerprint:a6892de79dee3a0ce8c8ee40ba0a0aab2971c84118cf432c84117b899200b935 -->
---
title: Vidu Q4 Preview Launches: What Is It and how to access
---
# Vidu Q4 Preview Launches: What Is It and how to access

![Vidu Q4 Preview Launches: What Is It and how to access](https://resource.cometapi.com/Vidu%20Q4.png)

**TLDR:** Vidu Q4 Preview is ShengShu Technology's public preview of its next-generation video model, announced on October 7, 2026. It supports image-to-video and reference-to-video workflows, outputs up to 4K, , support for up to 15 image references + 3 voice references, and dramatically stronger character performance, camera work, and VFX. Its main differentiator is the combination of high-resolution output with multiple visual and audio references

It debuted at #3 on the Artificial Analysis AA-Video-I2V leaderboard (1,179 Elo, jumping 16 places from Vidu Q3 Pro). Pricing starts as low as ~$0.014/sec (with launch discounts), available via the official Vidu web app, API, and platforms including CometAPI. Ideal for short drama, advertising, social content, and cinematic production.

### Key Takeaways

- Vidu Q4 Preview is Shengshu’s most advanced video model to date, focusing on “expressive performance” with lifelike emotions, natural voices, fluid motion, and high-impact VFX.
- Core capabilities: Image-to-Video and Reference-to-Video only (no text-to-video in Preview); max 16s; resolutions 540p–4K; up to 15 reference images and 3 audio references; native audio generation.
- Benchmark win: #3 on Artificial Analysis image-to-video leaderboard (1,179 Elo) vs. Vidu Q3 Pro at #19; better quality at similar or lower cost in many comparisons.
- Pricing: Launch rates from ~$0.014–$0.045/sec at lower resolutions, scaling to higher for 4K; 30% discount on image/reference-to-video through November 30, 2026 on official channels.
- Access: Official Vidu website and platform.vidu.com API; also available on third-party platforms and unified APIs such as CometAPI.
- Best for professional workflows needing character/product consistency across multi-shot scenes with audio.

## What Is Vidu Q4 Preview?

Vidu Q4 Preview is the public early-access version of Shengshu Technology’s (also referred to as ShengShu or Vidu AI) next-generation flagship AI video generation model. Launched on October 7, 2026, it builds on the earlier Vidu Q series (notably Q3) with a strong emphasis on “传神表现力” — lifelike, expressive performance.

Shengshu Technology originated from Tsinghua University’s AI research labs and has positioned Vidu as a production-oriented video model for short dramas, advertising agencies, social content creators, independent studios, and film production teams. The Preview version was released intentionally ahead of the full Q4 so creators can test it in real projects and provide feedback that will shape the final release.

Unlike pure text-to-video models, Q4 Preview is reference-driven. It prioritizes consistency of characters, styles, scenes, products, and voices when multiple references are supplied. Output includes native synchronized audio (dialogue, sound effects, and ambience generated together with the video), eliminating or reducing the need for separate audio post-production in many cases.

Official highlights include maximum 4K resolution, up to 16-second clips, up to 15 reference images, and up to 3 reference audio tracks.

## Key Features and Technical Specifications

| Specification | Vidu Q4 Preview |
| --- | --- |
| Model ID | viduq4-preview |
| Mode | Image-to-Video; Reference-to-Video |
| Resolution | 540p; 720p; 1080p; 2K; 4K |
| Frame rate | 24 fps |
| Maximum video duration | 16 seconds |
| Image-to-Video duration | 3–16 seconds |
| Image references | Up to 15 |
| Audio references | Up to 3 |
| Audio-video generation | Supported |
| Reference-to-Video aspect ratios | 16:9, 9:16, 1:1, 4:3, 3:4 |

Vidu Q4 Preview operates in two primary modes:

### Image-to-Video (I2V)

Upload a single image (which becomes the first frame), add a text prompt describing motion, camera movement, dialogue, or effects, and generate a 3–16 second video. The output preserves the original aspect ratio of the source image. Supports resolutions from 540p to 4K.

### Reference-to-Video (R2V)

Combine 1–15 reference images (characters, products, objects, locations, styles) plus optional 0–3 voice/audio references (typically short MP3 clips). The model maintains visual and vocal consistency across the generated multi-shot sequence. Durations range from 1–16 seconds. This mode enables complex, one-take storytelling with multiple subjects.

### Additional technical details :

- Frame rate: 24 fps
- Color: Up to 10-bit at higher resolutions (2K/4K) for professional workflows
- Audio: Native generation of synchronized speech, emotional delivery, lip-sync, and sound effects
- Camera & motion: Improved stability, smoother multi-shot transitions, better large-motion handling (martial arts, combat, running), and stronger cinematic camera language
- VFX: Enhanced explosions, smoke, particles, energy effects, and complex scene dynamics
- Prompting: Stronger instruction following; users are advised to reference images by order (e.g., “image 1”, “image 2”) and include timed beats for multi-shot control

These upgrades deliver more nuanced facial expressions, natural emotional delivery in voices, coherent lighting/texture, and reduced artifacts compared with prior generations.

### Performance Benchmarks and Supporting Data

Independent evaluation from Artificial Analysis placed Vidu Q4 Preview at #3 on the AA-Video-I2V v1.0 leaderboard with an Elo score of 1,179. This represents a jump of 16 places from Vidu Q3 Pro (previously around #19 with ~1,056 Elo). At the time of the snapshot (early October 2026), MiniMax H3 Max led at ~1,195 Elo, followed closely by MiniMax H3 and then Vidu Q4 Preview.

Shengshu and third-party reports note that Q4 Preview achieves higher quality at the same or lower effective cost than Q3 Pro in comparable setups (e.g., around $7.20 per minute at 1080p with audio in one tested configuration, sometimes cited as 25% more cost-efficient). Launch messaging claims up to 5× more output for the same budget under similar specifications.

Early testing (including beta on platforms like SelfyzAI and RunningHub) highlights stronger character consistency, more authentic acting/lip-sync, steadier camera work, and impactful large-scale effects (disaster, sci-fi, fantasy sequences). Chinese text rendering and on-screen text handling have also been praised as production-ready .

Note that as a Preview, specific scores, limits, and pricing can still evolve before the full Q4 release.

## Vidu Q4 vs Vidu Q3: Similarities and Differences

This comparison is specifically against **Q3 Pro**, not every model in the Q3 family. Q3 Mix, Q3 Turbo, and other Q3 variants have different workflows and limits.

| Dimension | Vidu Q4 Preview | Vidu Q3 Pro |
| --- | --- | --- |
| Maximum listed resolution | 4K | 1080p |
| API duration | 3–16 seconds on Q4 endpoints | 1–16 seconds in the documented Q3 Pro routes |
| Generation routes | Image-to-Video; Reference-to-Video | Text-to-Video; Image-to-Video; Start-End Frame |
| Reference guidance | Up to 15 images and up to 3 audio references on Reference-to-Video | No equivalent Reference-to-Video route in this Q3 Pro comparison |
| Synchronized audio-video | Supported | Supported |
| Best initial fit | Reference-led, high-resolution short scenes | Text-only or start/end-frame workflows |

Sources: Vidu's [Q4 API documents](https://platform.vidu.com/docs/api-reference/video-models/vidu-q4-preview/reference-to-video) and [Q3 model documents](https://platform.vidu.com/docs/api-reference/video-models/vidu-q3/reference-to-video).

Q4 Preview is a better match when the production workflow depends on many visual references, audio references, or 2K/4K output. Q3 Pro remains relevant when text-to-video or start/end-frame control is required. The maximum duration is not itself a Q4 improvement: both can reach 16 seconds under their documented routes.

The comparison below uses [Q3 Pro](https://platform.vidu.com/docs/api-reference/video-models/vidu-q3/text-to-video) as its baseline. Both models generate short videos with synchronized audio. Q4 Preview adds a higher resolution ceiling and a multi-reference route; Q3 Pro retains text-to-video and start/end-frame workflows. These differences describe the documented routes and should not be generalized to every Q3 variant.

### Similarity: Short Clips，Audio, Quality Gains Remain Unproven

Both models support clips up to 16 seconds, so Q4 Preview does not extend the maximum duration and support synchronized audio-video generation and camera switching. Q4 Preview’s audio references add a way to guide the sound of a scene. These capabilities do not establish a measured improvement in lip synchronization, motion or identity consistency. The Artificial Analysis results below provide Q3 Pro context; they do not supply a Q4 score or a direct Q3-to-Q4 quality comparison.

### Difference: Reference Inputs and Generation Routes

Both provide Image-to-Video. Q4 Preview also offers [Reference-to-Video](https://platform.vidu.com/docs/api-reference/video-models/vidu-q4-preview/reference-to-video), accepting 1–15 images and up to three audio clips. Q3 Pro provides Text-to-Video and Start-End Frame routes. Q4’s reference route suits scenes guided by characters, products or visual style; Q3 Pro remains relevant when the starting input is text or a specified pair of frames. Q4 Preview raises the resolution ceiling from Q3 Pro’s 1080p to 4K, giving creators a higher-resolution delivery option.

### Difference: Pricing and Best-Fit Workflows

Under Vidu’s [standard native API pricing](https://platform.vidu.com/docs/overview/pricing), Q4 Preview costs 19 credits/second at 720p versus Q3 Pro’s 20; both cost 24 credits/second at 1080p. Q4 therefore is not uniformly cheaper. Its 2K and 4K options carry higher rates. Q4 fits high-resolution, reference-guided scenes; Q3 Pro fits text-only and start/end-frame work. These native rates are separate from CometAPI pricing.

## How Much Does Vidu Q4 Preview Cost?

Vidu bills native API generation in credits. Its [published credit price](https://platform.vidu.com/docs/overview/pricing) is RMB 0.03125 per credit. The following calculations use standard Q4 Preview generation rates, without optional services or negotiated terms.

| Resolution | Credits / second | Calculated RMB / second | Calculated RMB / 5 seconds |
| --- | --- | --- | --- |
| 540p | 9 | 0.28125 | 1.40625 |
| 720p | 19 | 0.59375 | 2.96875 |
| 1080p | 24 | 0.75 | 3.75 |
| 2K | 38 | 1.1875 | 5.9375 |
| 4K | 78 | 2.4375 | 12.1875 |

## How to Access Vidu Q4 Preview

**Official Vidu Web App** — Visit vidu.com/vidu-q4 or the main create interfaces for Reference-to-Video and Image-to-Video. Sign up or log in, upload references, write prompts, select duration/resolution, and generate. New-user promo codes have been shared on official social channels.

**Official API** — Available at platform.vidu.com. Model ID: `viduq4-preview`. Supports resolutions 540p–4K, callbacks for async task handling, and both generation modes. Ideal for developers building automated pipelines.

### Recommended for developers and teams: CometAPI

CometAPI (cometapi.com) is a unified, OpenAI-compatible API gateway that aggregates 500+ models across text, image, video, and audio from multiple providers under a single key and endpoint (`https://api.cometapi.com/v1`). It already lists Vidu models (including Q3 variants and Q4 Preview listings in model catalogs) with competitive pricing (often discounted relative to official rates) and easy integration. Benefits of using CometAPI for Vidu Q4 access:

- One API key for Vidu plus hundreds of other models (switch without rewriting integrations).
- Simplified billing and monitoring.
- Production-ready endpoints for video generation.
- Free test credits on signup; no credit card required to start.
- Drop-in compatibility with existing OpenAI SDKs (just change base\_url and key). To get started: Sign up at cometapi.com, create an API key, and call the video generation endpoint with the appropriate Vidu model ID (check the current models/vidu page for `viduq4-preview` or equivalent).

### Practical Use Cases and Tips for Best Results

- **AI short dramas / series**: Maintain character identity and voice across shots with multi-reference input.
- **Advertising & product videos**: Lock product appearance and brand style with multiple product shots + voiceover references.
- **Social / cinematic content**: Multi-shot storytelling with dynamic camera and high-impact VFX.
- **Iteration workflow**: Generate low-res drafts quickly, refine prompts and references, then render finals at 2K/4K.

Prompting tips: Be specific about camera moves (“slow push-in”, “tracking shot”), emotion, timing of dialogue, and which reference corresponds to which element. Iterate by changing one variable at a time. Review lip-sync and audio carefully, as native generation is strong but still benefits from selective post-editing for commercial delivery.

### Limitations to Keep in Mind

As a Preview, text-to-video is not supported (you need at least one image). Full Q4 may expand capabilities. Results can vary; complex multi-subject scenes still require careful reference preparation and prompt engineering. Always verify commercial licensing and content policies on the platform you use.

## Conclusion and Recommendation

Vidu Q4 Preview marks a meaningful leap for Shengshu’s Vidu line, delivering higher resolution, superior reference control, more expressive performances, and competitive economics that make high-quality AI video more accessible. Its strong showing on independent benchmarks and focus on production realities (consistency + native audio) position it as one of the top choices in late 2026 for reference-driven video work.

For creators and developers seeking the easiest path to experiment and scale: start on the official Vidu site for creative exploration, then integrate via the official API or a unified gateway like **CometAPI** for production workflows. CometAPI’s single-key access to Vidu models (alongside 500+ others) reduces integration overhead and often provides cost advantages — ideal for teams building content automation, A/B testing multiple video models, or combining video with text/image pipelines.

Explore Vidu Q4 Preview today at vidu.com/vidu-q4 or through CometAPI’s model catalog at cometapi.com/models/vidu/. The full Q4 release will likely build on the feedback from this Preview period — early adopters who test thoroughly will be best positioned to leverage the final model.

---

*Originally published at [https://www.cometapi.com/vidu-q4-preview-launches/](https://www.cometapi.com/vidu-q4-preview-launches/).*
