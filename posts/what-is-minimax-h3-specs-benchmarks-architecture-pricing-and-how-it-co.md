<!-- social-ops-fingerprint:884e3f2c5bb991609964e56012109dee1f7b4fedb841d531729a4e5ef2352e13 -->
---
title: What Is MiniMax H3? Specs, Benchmarks, Architecture, Pricing and How It Compares
---
# What Is MiniMax H3? Specs, Benchmarks, Architecture, Pricing and How It Compares

![What Is MiniMax H3? Specs, Benchmarks, Architecture, Pricing and How It Compares](https://resource.cometapi.com/1785470302643.jpeg)

## TL;DR

AI video models are moving beyond the old text-to-video formula toward systems that can understand a complete creative brief—text, images, reference footage, motion, voices, music, and sound effects—and turn it into a coherent audiovisual scene. [MiniMax officially launched H3 on July 31, 2026](https://www.minimax.io/blog/minimax-h3) as a general-purpose omni-modal generation model that jointly understands text, images, video, and audio and generates clips of up to 15 seconds with native stereo sound. Its key change is a unified architecture that treats text-to-video, image-to-video, first/last-frame generation, reference-based generation, motion transfer, audiovisual editing, and audio-conditioned creation as variations of one multimodal generation problem rather than isolated pipelines. The hosted product offers 2K output by default through a workflow in which H3-Base first generates at a 768p short side and H3-Regenerate-2K then reconstructs the scene using the original context. This combination of competitive audiovisual quality, flexible multimodal control, downloadable H3-Base weights, and context-aware 2K finishing makes H3 one of the more technically distinctive video releases of 2026.

## Key Takeaways

- **New architecture:** Contextual Omni Representation, H3-VAE, H3-Omni Transformer, and In-Context Regeneration unify understanding and generation across modalities.
- **Performance improvements:** H3 generates 4–15 second clips with 24 FPS video, 32 kHz stereo audio, and hosted 2K output reconstructed from the original multimodal context.
- **API and open-weight availability:** MiniMax provides hosted H3-2K, H3-Context-IR, and H3-Regenerate-2K APIs, while H3-Base-FL2VA and H3-Base-Ref2VA are available as downloadable checkpoints.
- **Main use cases:** Advertising, branding, e-commerce, product design, UI/UX, gaming, film, reference-driven generation, motion transfer, and audiovisual editing.
- **Pricing and deployment boundary:** Official pay-as-you-go pricing is $0.08/second at 768P and $0.13/second at 2K; only H3-Base is downloadable, while H3-Context-IR and H3-Regenerate-2K remain hosted services.

## What Is MiniMax H3?

MiniMax H3 is a general-purpose omni-modal audio-video generation system developed by MiniMax. Instead of accepting only a prompt or one reference image, H3 can reason over a context containing text, images, videos, and audio and then generate synchronized video and stereo sound.

The hosted H3 system supports [4-15 second output](https://www.minimax.io/news/minimax-h3-open-source), 24 FPS video, and 32 kHz stereo audio. MiniMax markets the hosted system as providing 2K by default. Technically, H3-Base creates a 768p short-side result and H3-Regenerate-2K feeds that result and the original context back into H3 for 2K reconstruction. MiniMax also reports stable dialogue generation across [11 languages](https://www.minimax.io/news/minimax-h3-open-source), including English, Chinese, Japanese, Korean, French, German, Spanish, Portuguese, Italian, Russian, and Arabic.

This distinction matters. Many earlier video workflows are effectively pipelines:

**prompt -> silent video -> speech -> sound effects -> music -> synchronization**

H3 instead models audio and video as parts of one generation process. Its H3-Omni-Transformer [jointly predicts](https://www.minimax.io/news/minimax-h3-open-source) video and audio latents, reducing the need to assemble independent video, dubbing, music, and synchronization stages afterward.

## MiniMax H3 Specifications at a Glance

| Specification | MiniMax H3 |
| --- | --- |
| Developer | MiniMax |
| Model category | General-purpose omni-modal video generation |
| Input modalities | Text, image, video, audio |
| Output | Video plus native stereo audio |
| Output duration | 4–15 seconds |
| Base resolution | 768p short-side for H3-Base |
| Hosted resolution | Up to 2K through H3-Regenerate-2K 2K offered by default; produced through H3-Regenerate-2K after 768p base generation |
| Frame rate | 24 FPS |
| Audio | 32 kHz stereo |
| Stable dialogue languages | 11 |
| Aspect ratios | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, and additional dimensions |
| Reference limits | Up to 9 images, 3 videos, 3 audio clips, and 12 mixed files |
| Core generative model | 33B dense H3-Omni-Transformer |
| Position encoding | 3D Multimodal RoPE |
| Open-weight checkpoints | H3-Base-FL2VA and H3-Base-Ref2VA |
| Checkpoint precision | BF16 |
| License | MiniMax H3 Community License |

The 33B figure refers to the H3-Omni-Transformer rather than every component used across the complete hosted pipeline.

## What Makes MiniMax H3 Different?

### One Model for Multiple Video Tasks

Most video generators historically separate text-to-video, image-to-video, motion reference, video editing, audio generation, and subject-reference capabilities.

MiniMax takes a different approach. H3 was pretrained around generalized relationships between multimodal context and the desired output, allowing instructions to describe those relationships in natural language.

For example, a creator can conceptually ask H3 to follow the camera movement in one video, preserve the character from an image, and use another audio clip as the vocal reference. MiniMax's launch demonstrations use this kind of cross-modal instruction to illustrate H3's generalized reference system.

That makes H3 less like a collection of generation modes and more like a multimodal creative engine.

### Native Video and Stereo Audio Generation

MiniMax's technical description states that the H3-Omni-Transformer [predicts video and audio latents](https://www.minimax.io/news/minimax-h3-open-source) jointly. The audio side operates through H3-AudioVAE, which compresses 32 kHz audio into a 40 Hz latent sequence before decoding the generated result back into stereo sound.

This gives H3 a practical advantage for scenes containing dialogue, environmental audio, music, or sound effects: sound is part of the generative context instead of an entirely separate post-production step.

### Omni-Reference Inputs

H3-Base-Ref2VA supports as many as 9 images, 3 video clips, and 3 audio clips, subject to a maximum of 12 mixed input files. Reference videos and audio clips can each be 2-15 seconds long, with total duration restrictions for each modality. Audio cannot act as the sole reference input in Ref2VA mode.

The important part is not just the quantity of references. H3 is designed to infer the relationship between those assets.

- preserve a character from an image;
- reproduce motion from a reference clip;
- transfer a visual or cinematic style;
- preserve or replace audio;
- use one voice as a timbre reference;
- edit an existing audiovisual scene using natural-language instructions.

### In-Context 2K Regeneration

H3's approach to high resolution is unusually important.

Instead of simply passing the 768p output through a conventional super-resolution network, [H3-Regenerate-2K](https://www.minimax.io/news/minimax-h3-open-source) reintroduces the original multimodal context together with the base result and asks H3 to regenerate the scene at the higher resolution.

The intended advantage is semantic recovery. A normal upscaler can interpolate pixels but cannot reliably reconstruct information that has disappeared - small lettering, branded elements, or fine object details. H3's regeneration stage can consult the original prompt and references again while constructing the 2K result.

![What Is MiniMax H3? Specs, Benchmarks, Architecture, Pricing and How It Compares](https://resource.cometapi.com/27fc2e9-b933-425c-9c22-14604951855b.png)

## How Does the MiniMax H3 Architecture Work?

The complete H3 workflow has three major stages:

**H3-Context-IR -> H3-Base -> H3-Regenerate-2K**

H3-Context-IR interprets a potentially complicated multimodal instruction and converts it into a structured Context Intermediate Representation. H3-Base consumes that representation and generates 768p video plus audio. H3-Regenerate-2K then combines the generated result with the original context to construct a higher-resolution version.

![What Is MiniMax H3? Specs, Benchmarks, Architecture, Pricing and How It Compares](https://resource.cometapi.com/6ecd93-d55e-42a6-8e53-11f3a20ef9d2.png)

### H3-Contextual Omni Representation and H3-Context-IR

Contextual Omni Representation is MiniMax’s broader design concept: language acts as the bridge that describes relationships among the context, the target, and multiple modalities. In the released system description, H3-Context-IR is the hosted preprocessing and orchestration layer that parses instructions, associates modalities, reasons about time, and serializes the result for H3-Base.

The H3-Encoder remains a specific component inside H3-Base. It uses the pretrained weights of Qwen3-VL-32B and passes hidden states from layer 50 into the H3-Omni-Transformer.

### H3-VAE

The launch terminology “H3-VAE” covers the model family’s visual and audio latent representations. The open-weight documentation distinguishes H3-VisualVAE from H3-AudioVAE. H3-VisualVAE uses temporally causal encoding with 16× spatial compression, 4× temporal compression, and 24 latent channels, followed by 1 × 2 × 2 patchification. H3-AudioVAE compresses 32 kHz stereo audio into latent tokens at a 40 Hz temporal rate.

### H3-Omni-Transformer

The launch blog styles the name as “H3-Omni Transformer”; the open-weight technical documentation uses “H3-Omni-Transformer.” Both refer to the same core generative component. It is a 33B-parameter dense, single-stream Transformer. Roughly 13B parameters reside in AdaLN-related branches; their modulation outputs can be precomputed and cached, so they do not need to remain loaded during inference-only deployment.

Modality-specific components are concentrated in input/output layers and AdaLN branches, while the central Transformer operates on a unified packed sequence. Three-dimensional Multimodal RoPE represents temporal and spatial positions across (t, h, w).

### H3-In-Context Regeneration

MiniMax’s launch blog calls the technique H3-In-Context Regeneration; the production module is named H3-Regenerate-2K. It feeds the 768p result and original context back into H3 to reconstruct a 2K output, allowing semantic details to be regenerated instead of merely interpolated.

## Is MiniMax H3 Really Open Source?

**Moved here from its previous position after the comparison section because the open-weight boundary is a core architectural distinction.**

“Open-weight” is more precise than “fully open source.” MiniMax makes the H3-Base-FL2VA and H3-Base-Ref2VA checkpoints available for local use, including the required processor, tokenizer, text encoder, Transformer, visual VAE, and audio VAE components.

However, the complete production pipeline is not downloadable end to end. H3-Context-IR remains hosted, and H3-Regenerate-2K is not included in the initial open-weight release. Local H3-Base generation targets a 768p short-side resolution; reproducing the official full 2K workflow requires hosted services for context processing and regeneration.

H3 also uses the MiniMax H3 Community License rather than a standard permissive license such as Apache 2.0 or MIT. Organizations should review the license’s territorial, attribution, safety, and commercial-use conditions before deployment.

## MiniMax H3 Benchmark Performance

MiniMax's launch materials concentrate primarily on demonstrations, architecture, and use cases rather than publishing a conventional large VBench-style benchmark matrix. For a more neutral snapshot, one useful source is Artificial Analysis's Video Arena, where users blindly compare generations from the same prompts.

| Artificial Analysis task | H3 rank | H3 Elo | Leader | Leader Elo |
| --- | --- | --- | --- | --- |
| Text-to-Video with Audio | #4 | ≈1,228 | Wan 3.0 | 1,242 |
| Image-to-Video with Audio | #3 | 1,185 | H3 Max, post-trained by fal | 1,202 |
| Video Editing with Audio | #2 | 1,129 | Wan 3.0 | 1,190 |

These rankings are a September 2, 2026 snapshot, not permanent scores. H3 is competitive with leading proprietary systems and is especially notable among open-weight entries. Its value proposition is the combination of competitive quality, native audiovisual generation, multimodal references, and downloadable base weights—not simply a claim to the highest benchmark score.

## MiniMax H3 Pricing

The following pay-as-you-go prices were rechecked against MiniMax’s official pricing page on September 24, 2026. Prices may change, so production teams should verify them again before budgeting.

| Usage | Official list price |
| --- | --- |
| H3 generation at 768P | $0.08/second |
| H3 generation at 2K | $0.13/second |
| 768P → 2K regeneration output | $0.05/second |
| Standard-generation reference audio | Free |
| Standard-generation reference images | First 5 free; then $0.04/image |
| Regeneration reference images | First 5 free; then $0.025/image |
| Regeneration reference video | $0.05/second of original 768P input |
| H3-Context-IR input | $0.90/M tokens |
| H3-Context-IR output | $3.60/M tokens |

At list price, a 10-second direct generation is approximately $0.80 at 768P or $1.30 at 2K; a 15-second generation is approximately $1.20 or $1.95. These examples exclude billable references, Context-IR tokens, and other workflow-specific charges.

MiniMax H3 is also available through CometAPI. Its model page advertises a starting rate of $0.064/second under model ID **minimax-h3**. Third-party headline prices may depend on route, resolution, and billing rules, so they should not be treated as universal unit rates.

## MiniMax H3 vs Wan3.0 vs Seedance 2.5 vs Vidu Q3

The most useful competitors are not necessarily models that look identical on paper. MiniMax H3, Wan3.0, Seedance 2.5, and Vidu Q3 emphasize different parts of the professional-video workflow.

| Dimension | MiniMax H3 | Wan3.0 | Seedance 2.5 | Vidu Q3 |
| --- | --- | --- | --- | --- |
| Maximum single generation | 15s | 30s | 30s | 16s |
| Video resolution | 2K hosted; 768p open-weight base | Up to 1080P | Route-dependent | Up to 1080P |
| Native audio-video | Yes | Yes | Yes | Yes |
| Reference inputs | Text, image, video, audio | Image, video, audio, documents, webpages | Images, videos, audio | Image/reference workflows |
| Reference capacity | 12 mixed files | Up to 20 materials | Up to 50 materials | Not stated on main page |
| Major differentiator | Open-weight H3-Base plus 2K regeneration | 30s plus broad inputs | 30s storytelling plus large reference set | Short narrative and dialogue control |
| Strongest fit | Customizable multimodal pipelines | Long all-in-one production | Reference-heavy commercial storytelling | Short drama and dialogue-driven work |
| Strongest fit | Customizable creative pipelines | Long all-in-one production | Reference-heavy commercial storytelling | Short drama and dialogue-driven work |

### Which Model Is Better?

There is no universal winner. Choose MiniMax H3 when open weights, multimodal conditioning, native stereo audio, audiovisual editing, and 2K finishing matter more than maximum clip duration. Choose Wan 3.0 when 30-second output, 1080P, broad document/web references, and strong arena performance matter most. Choose Seedance 2.5 for very large reference sets, 30-second narrative structure, identity consistency, or targeted editing. Choose Vidu Q3 for short narrative scenes, multi-person dialogue, timing, and director-like camera control.

A responsible evaluation should run the same internal prompt set across all candidate APIs. Public leaderboards do not always expose directly comparable versions, and substituting an older or turbo variant can distort the result.

## What Are MiniMax H3's Main Limitations?

- **Duration:** H3 tops out at 15 seconds, while some competitors now support 30-second generations.
- **Open-weight scope:** only H3-Base is downloadable; Context-IR and 2K regeneration remain hosted.
- **Hardware requirements:** a 33B dense video model remains expensive to deploy locally, even with inference optimizations.
- **Pricing complexity:** generation, regeneration, reference videos and images, and Context-IR can create separate charges.
- **License conditions:** the Community License requires a closer legal review than standard permissive licenses.
- **Benchmark volatility:** arena rankings change and do not replace workload-specific testing.

## Who Should Use MiniMax H3?

H3 is a strong fit for developers and creative teams building multimodal video workflows that need consistent subjects, motion or voice references, native stereo audio, editing, and high-resolution finishing. It is also relevant to teams that want to customize or self-host the base model while using hosted stages only when needed.

Teams that primarily need the longest single generation, the lightest local deployment, or a completely permissive end-to-end stack may prefer another model. MiniMax highlights advertising, branding, e-commerce, product design, UI/UX, gaming, and film as commercial creation scenarios.

## How Can Developers Access MiniMax H3?

There are three main paths:

1. Use MiniMax’s hosted products, including Hailuo and MiniMax Design.
2. Use the first-party MiniMax Open Platform for H3-2K, H3-Context-IR, and H3-Regenerate-2K APIs.
3. Download H3-Base checkpoints for local deployment through the official repository and supported inference frameworks.

For implementation details, use the official API and deployment documentation linked in the source list below; this article stays focused on product evaluation.

## Conclusion

MiniMax H3 matters less because it leads every individual metric than because it compresses a fragmented production chain into one programmable multimodal system. Downloadable H3-Base weights give developers room to prototype, customize, and iterate locally, while the hosted H3-Context-IR and H3-Regenerate-2K stages provide the richer instruction processing and high-resolution finishing needed for production work. That hybrid model also creates trade-offs: the 15-second limit, local infrastructure requirements, hosted-service dependence, workflow-level costs, and Community License conditions all need to be evaluated against a team’s real prompts and delivery constraints. For teams that prioritize multimodal reference control, synchronized native audio, audiovisual editing, and 2K masters, H3 is a compelling platform; teams that primarily need longer clips or a fully self-contained permissive stack should benchmark alternatives before committing.

## FAQ

### How should a production team divide work between local H3-Base and MiniMax’s hosted services?

A practical hybrid workflow is to use local H3-Base for rapid exploration, prompt iteration, reference testing, and any stage where infrastructure control or data locality matters. Promising outputs can then move to hosted H3-Context-IR for richer instruction processing and H3-Regenerate-2K for final-resolution delivery. The right split depends on GPU capacity, turnaround time, governance requirements, and whether the quality gain from the hosted stages justifies the additional transfer, latency, and billing.

### What should an internal evaluation set measure before a team adopts H3?

Do not evaluate H3 only with visually impressive prompts. Use a repeatable set of real production briefs and score instruction adherence, subject and brand consistency, temporal stability, text rendering, camera-motion accuracy, audio-video synchronization, dialogue quality, regeneration fidelity, latency, failure rate, and total cost per accepted clip. Run the same assets and acceptance criteria across competing models so that arena rankings do not substitute for evidence from the team’s actual workload.

### How should multimodal reference assets be prepared to improve controllability?

Reference assets should have clear, non-conflicting roles: one image may define identity, one clip may define motion, and one audio sample may define voice or atmosphere. Remove low-quality or contradictory references, trim clips to the relevant action, and state the relationship between each asset and the target output explicitly in the instruction. Starting with the smallest sufficient reference set makes it easier to diagnose which asset improves the result and which one introduces ambiguity.

### Which production costs are easy to miss when comparing H3 with another API?

Per-second generation price is only the visible baseline. A realistic cost model should include billable reference videos and additional images, Context-IR tokens, 2K regeneration, retries, rejected generations, local GPU capacity, media storage and transfer, moderation handling, integration engineering, and human review. The useful comparison is cost per approved deliverable at the required resolution—not cost per raw generation.

### How should teams interpret “2K by default” when H3-Base itself generates at 768p?

The phrases describe different layers of the product. “2K by default” refers to the hosted commercial experience, while 768p describes the short-side output of the downloadable H3-Base stage; H3-Regenerate-2K then rebuilds the final output using both the base result and the original context. Quality testing should therefore compare local 768p output and final hosted 2K output as separate workflow stages, with attention to whether regeneration actually restores text, branding, faces, and fine details rather than merely increasing pixel dimensions.

### When is MiniMax H3 unlikely to be the best first choice?

H3 may be a poor fit when a project requires substantially longer single-pass clips, fully local 2K finishing, a standard permissive license, minimal GPU investment, or a very simple text-to-video workflow that gains little from multimodal references. In those cases, the value of H3’s generalized architecture may not offset the extra operational complexity. A short proof of concept using representative prompts is the safest way to determine whether its control and audio-video integration materially improve the final deliverable.

---

*Originally published at [https://www.cometapi.com/what-is-minimax-h3/](https://www.cometapi.com/what-is-minimax-h3/).*
