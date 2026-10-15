<!-- social-ops-fingerprint:bf9fa0e2bbe819a46c63889924cba857f2a026c2934f5517042a7a4116c96c69 -->
---
title: What Is MiniMax H3 Max
---
# What Is MiniMax H3 Max

![What Is MiniMax H3 Max](https://resource.cometapi.com/MiniMax%20H3%20Max.jpg)

## TL;DR

MiniMax H3 Max is not a brand-new foundation model that replaces MiniMax H3. It is a [post-trained variant of MiniMax H3 created by fal Research](https://fal.ai/learn/devs/introducing-h3-max-by-fal), using H3 open weights and additional post-training focused on prompt adherence, visual aesthetics, and inference efficiency.

That distinction explains most of the differences between the two models. [MiniMax H3 Max](https://www.cometapi.com/models/minimax/minimax-h3-max/) is optimized for fast production inference and stronger prompt adherence, while [MiniMax H3](https://www.cometapi.com/models/minimax/minimax-h3/) remains the broader omni-modal system, including richer multimodal conditioning, open H3-Base weights, video editing workflows, and output up to 2K through H3-Regenerate-2K.

As of September 18, 2026, independent preference data shows H3 Max at 1227 Elo in text-to-video with audio versus 1220 for H3, and 1195 Elo in image-to-video with audio versus 1181 for H3. The gaps are meaningful enough to track, but not large enough to imply a dramatic quality difference in every prompt.

## Key Takeaways

- **H3 Max is a post-trained H3 variant, not H4 or a larger H3 architecture.** fal started from MiniMax H3 open weights and optimized the model and serving stack together.
- **Speed is H3 Max's clearest differentiator.** fal reports roughly three seconds or less for a five-second 768p generation on its optimized infrastructure.
- **H3 Max currently leads H3 in the two directly comparable independent preference tests used here.** The latest snapshot shows +7 Elo in text-to-video with audio and +14 Elo in image-to-video with audio.
- **MiniMax H3 is still the broader foundation-model workflow.** It supports richer multimodal references, editing, open H3-Base weights, and 2K regeneration.
- **Resolution is an important distinction.**H3 Max exposes 480p/768p generation plus 1080p latent refinement, while H3 can reach 2K through H3-Regenerate-2K.

## What Is MiniMax H3 Max?

MiniMax H3 Max is an AI video generation model developed by fal Research through post-training of MiniMax H3 open weights. Instead of replacing the underlying H3 architecture with a completely new foundation model, fal concentrated on [prompt adherence, aesthetics, and inference throughput](https://fal.ai/learn/devs/introducing-h3-max-by-fal).

The word “Max” can therefore be misleading if it is interpreted as a conventional larger-parameter tier. Public materials do not establish a larger Transformer or a new parameter scale for H3 Max. The differentiation comes primarily from post-training and a serving stack designed around the modified model.

fal also describes substantial new post-training data and evaluation loops centered on user-visible quality. In practice, H3 Max is best understood as a production-optimized H3 variant rather than a clean-sheet successor.

### MiniMax H3 Max specifications at glance

| Specification | MiniMax H3 Max |
| --- | --- |
| Base model | MiniMax H3 |
| Post-training developer | fal Research |
| Model category | Audio-video generation |
| Text-to-video | Yes |
| Image-to-video | Yes |
| First/last-frame control | Yes |
| Reference-to-video | Yes |
| Output duration | 5-15 seconds |
| Native generation resolution | 480p / 768p |
| 1080p option | Latent refinement from native 768p |
| Frame rate | 24 FPS |
| Audio | Synchronized stereo audio |
| Aspect ratios | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 |
| Primary optimization | Prompt adherence, aesthetics, throughput |
| CometAPI model ID | minimax-h3-max |

The current fal API schema describes the 1080p option as latent refinement from a native 768p source, which matters when comparing H3 Max with systems that regenerate at a genuinely higher resolution.

## How Does MiniMax H3 Max Work?

Understanding H3 Max starts with the H3 foundation beneath it. MiniMax describes H3 as an omni-modal generative system rather than a collection of isolated text-to-video, image-to-video, audio, and editing models.

The complete H3 workflow is organized around H3-Context-IR, H3-Base, and H3-Regenerate-2K. H3-Context-IR interprets free-form multimodal instructions, H3-Base performs core audiovisual generation at 768p, and H3-Regenerate-2K reuses the original context plus the lower-resolution result to regenerate a higher-resolution output.

### The H3 foundation beneath H3 Max

MiniMax documents H3-Omni-Transformer as a [33-billion-parameter dense single-stream Transformer](https://www.minimax.io/news/minimax-h3-open-source), with approximately 13B parameters in AdaLN-related branches. The H3-Encoder uses pretrained Qwen3-VL-32B weights, while separate visual and audio VAEs encode their respective modalities before joint generation.

The H3-Omni-Transformer jointly predicts video and audio latents rather than treating sound as a separate post-processing stage. That architecture is why both H3 and H3 Max can produce synchronized audiovisual output.

Official MiniMax H3 model architecture

### What fal changed for H3 Max

fal post-trained H3 with additional data targeting instruction fidelity and visual quality, then developed the inference system alongside the model rather than optimizing serving only after training was complete. The launch article describes this model-and-inference co-design as the core reason H3 Max can shift the quality-speed trade-off.

That matters because simply reducing sampling steps or precision can lower latency while degrading output quality. fal says candidate optimizations were retained only when the resulting checkpoints continued to hold up in its preference evaluations.

MiniMax H3 provides the multimodal generation foundation; H3 Max changes where that foundation sits on the quality-speed-cost curve.

## What Are the Main Features of MiniMax H3 Max?

### Stronger prompt adherence

Prompt adherence was a direct post-training target. This matters for structured prompts that combine multiple actions, scene transitions, camera directions, temporal constraints, and style instructions.

### Faster-than-video-duration generation

H3 Max is designed for unusually low generation latency. fal reports five-second 768p clips in roughly three seconds or less on its optimized infrastructure, enabling much tighter iterative creative loops.

### Native synchronized audio

H3 Max retains H3’s joint audio-video generation approach, so dialogue, ambience, sound effects, and motion can be produced in a coordinated audiovisual workflow.

### Multiple generation workflows

The H3 Max family supports text-to-video, image-to-video, first-to-last-frame generation, and reference-to-video workflows.

### Built-in prompt expansion

The text-to-video endpoint exposes prompt-expansion modes such as disabled, balanced, and quality, allowing developers to trade preprocessing time for richer prompt interpretation.

## How Does MiniMax H3 Max Perform ?

### Benchmarks of MiniMax H3 Max

Provider-run benchmarks are useful for showing what the post-training targeted, but continuously updated third-party preference tests are more useful for comparing H3 Max with the original H3 under the same arena methodology.

| Benchmark snapshot — Sep. 18, 2026 | MiniMax H3 Max | MiniMax H3 | Difference |
| --- | --- | --- | --- |
| Text-to-Video with Audio Elo | 1227 ±9 | 1220 ±8 | +7 |
| Text-to-Video samples | 5,689 | 8,602 | — |
| Image-to-Video with Audio Elo | 1195 ±10 | 1181 ±8 | +14 |
| Image-to-Video samples | 5,569 | 6,949 | — |
| Video Editing with Audio Elo | Not ranked in this comparison | 1132 ±6 | — |

**Benchmark methodology note.** The Artificial Analysis figures are dated blind human-preference Elo snapshots; this article reports the score, 95% confidence interval, sample count, category, and snapshot date. Exact prompts, generation settings, and evaluation procedures should be checked against the [current Artificial Analysis methodology](https://artificialanalysis.ai/methodology). fal's #1 result is provider-run on fal infrastructure, and its [public comparison chart](https://v3b.fal.media/files/b/0aa7ed68/bJAr59iUjAXlDj6JZmORv_h3-max-cost-vs-quality-pareto.png) does not disclose every prompt, hardware, or serving parameter required for independent reproduction.

The current snapshot supports a narrow conclusion: H3 Max has the higher measured preference score in both directly comparable audio-video generation categories. The confidence intervals overlap, so the gap should not be presented as a universal or dramatic quality lead.

### fal’s own H3 Max evaluation

fal reports that H3 Max ranked first across overall preference, prompt understanding, and aesthetics in its head-to-head evaluation against twelve video models. That is provider-run evidence, so it is best read alongside independent arena data rather than as a substitute for it.

![What Is MiniMax H3 Max](https://resource.cometapi.com/blog/uploads/2026/09/MInimax-%20H3-max.png)

Official fal H3 Max cost-vs-quality chart

The most useful interpretation is not “H3 Max universally wins.” It is that H3 Max materially improves H3’s speed-quality operating point while the independent preference-score gap over H3 remains comparatively modest.

### Speed, Quality, and the Trade-off

fal reports that H3 Max generates a five-second 768p video in under three seconds on its optimized infrastructure—roughly 35× the throughput of the official MiniMax H3 endpoint in fal's comparison. Treat this as provider-specific inference evidence: queueing, network transfer, safety checks, and a different backend can increase end-to-end latency.

The quality advantage is more modest than the speed advantage. In the September 18 independent snapshot used here, H3 Max led H3 by 7 Elo for text-to-video with audio and 14 Elo for image-to-video with audio, but the confidence intervals overlap. The defensible conclusion is that H3 Max shifts the speed-quality frontier; it does not guarantee a visibly better result for every prompt.

**Practical choice:** use H3 Max for rapid iteration, high-throughput short-form production, and prompts where adherence matters. Prefer standard H3 when the workflow depends on the broader multimodal system, video editing, open-weight deployment, or the H3-Regenerate-2K path.

## How Much Do MiniMax H3 Max Cost?

Pricing needs context because provider rates and promotions can change independently. The following snapshot reflects publicly displayed rates checked on September 18, 2026.

| Pricing source | H3 Max | H3 |
| --- | --- | --- |
| fal 480p | $0.025/sec promotional | — |
| fal 768p | $0.04/sec promotional | — |
| fal 1080p refinement | $0.08/sec promotional | — |
| MiniMax official 768p | — | $0.08/sec |
| MiniMax official 2K | — | $0.13/sec |
| MiniMax 768p → 2K regeneration | — | $0.05/sec |
| CometAPI starting price | $0.064/sec | $0.064/sec |

fal currently labels its H3 Max rates as promotional launch pricing and states that the discount ends September 30, 2026. The MiniMax H3 Max API in CometAPI currently shows $0.064 per second, while the MiniMax H3 API in CometAPI also starts at $0.064 per second. Provider pricing should be rechecked before forecasting a large production workload.

## How to try MiniMax H3 Max

The [MiniMax H3 Max API in CometAPI](https://www.cometapi.com/models/minimax/minimax-h3-max/) is currently available with model ID minimax-h3-max, a production endpoint under /v1/videos, asynchronous task handling, and a displayed starting price of $0.064 per second.

1. **Create an API key.** Sign in to CometAPI, create a token, and store it securely as `COMETAPI_KEY`.
2. **Submit a generation task.** Send a `POST` request to `https://api.cometapi.com/v1/videos` with model `minimax-h3-max`, a prompt, duration, and output size. Add an image URL when using image-to-video.
3. **Poll the asynchronous task.** Read the returned task ID and request `GET /v1/videos/{task_id}` until the status becomes `completed` or `failed`. Use a polling interval instead of sending continuous requests.
4. **Download and review.** Retrieve `GET /v1/videos/{task_id}/content`, save the MP4, and inspect prompt adherence, motion, audio synchronization, and visual artifacts before scaling the workload.

For a fair H3 Max versus H3 comparison, keep prompt, duration, aspect ratio, resolution, reference inputs, audio settings, and retry policy fixed. Confirm the live schema and price on the model page before production because routing and exposed parameters can change independently of the underlying model.

## Limitations of MiniMax H3 Max

First, H3 Max does not replace H3’s 2K regeneration workflow. Its currently documented 1080p option is a refinement of native 768p output rather than the same in-context 2K regeneration path used by H3.

Second, H3 Max’s headline latency is closely tied to fal’s optimized inference stack, so the same wall-clock speed should not be assumed on another backend.

Third, the independent quality lead over H3 is currently modest. The September 18 benchmark snapshot shows +7 Elo in text-to-video with audio and +14 Elo in image-to-video with audio, with overlapping confidence intervals.

Finally, H3 remains the broader system if “better” means video editing, multimodal-reference depth, open-weight deployment, or maximum output resolution rather than raw generation throughput.

## Conclusion

MiniMax H3 Max is best understood as a production-optimized H3 variant, not a larger successor. fal's post-training and inference co-design create a compelling operating point for fast short-form audiovisual generation, while the independent preference lead over standard H3 remains modest rather than universal.

Choose H3 Max when iteration speed, throughput, and prompt adherence are the main constraints. Choose standard H3 when you need the broader multimodal workflow, video editing, open H3-Base weights, or 2K regeneration. Before committing to either route, run a controlled benchmark with identical prompts and settings and calculate cost per accepted clip—not only cost per generated second.

## FAQ

### **How should teams interpret H3 Max's benchmark lead when the confidence intervals overlap?**

Treat the lead as directional evidence, not proof that H3 Max wins every prompt. In the cited snapshot, H3 Max leads H3 by 7 Elo in text-to-video with audio and 14 Elo in image-to-video with audio, but the confidence intervals overlap. Teams should therefore test a representative prompt set, report win rate and failure modes, and avoid turning a modest aggregate lead into a universal quality claim.

### **How should teams compare the true production cost of H3 Max and H3 beyond the listed price per second?**

Calculate cost per accepted clip rather than cost per generated second. Include retries, rejected outputs, 1080p refinement or 2K regeneration, storage and transfer, review time, and any downstream editing. H3 Max may lower iteration cost through faster generation and stronger prompt adherence, while H3 can be more economical when its editing, multimodal controls, or 2K workflow avoids additional tools and rework.

### **What generation speed can teams realistically expect, and which factors affect end-to-end latency?**

fal reports under three seconds of inference for a five-second 768p clip on its optimized infrastructure. That is not a universal end-to-end guarantee: queue time, input uploads, prompt expansion, safety processing, resolution, duration, and provider routing all affect observed latency. Benchmark the exact endpoint and configuration you plan to deploy

### **Which H3 Max workflow should be used for text-only, image-conditioned, keyframe-controlled, or reference-driven jobs?**

Use text-to-video when the scene can be defined entirely in language; use image-to-video when identity, composition, or visual style must begin from a supplied frame. Choose first-to-last-frame control when the opening and ending states are both important, and reference-to-video when consistency with multiple visual references matters. The correct workflow reduces prompt ambiguity and should be fixed before comparing H3 Max with H3.

### **How should teams choose among 480p, 768p, H3 Max 1080p refinement, and H3 2K regeneration?**

Use 480p for inexpensive drafts and high-volume concept screening, then move to 768p for normal evaluation and many web deliveries. Choose H3 Max's 1080p refinement when rapid production remains the priority but the delivery format needs more pixels. Choose H3's 2K regeneration when maximum detail and the broader H3 workflow justify higher latency and cost; compare final artifacts at the actual display size rather than selecting by resolution label alone.

### **How does MiniMax H3's 2K regeneration differ from H3 Max's 1080p refinement?**

Yes. Standard MiniMax H3 can reach 2K through H3-Regenerate-2K. This is an in-context regeneration stage that reuses both the original multimodal instructions and the 768p result, allowing it to reconstruct details rather than applying a conventional super-resolution pass. That broader workflow is a reason to prefer H3 over H3 Max for maximum resolution.

### **Which parts of MiniMax H3 are open-weight, and which parts still require hosted APIs?**

Partly. MiniMax released the H3-Base FL2VA and Ref2VA checkpoints under the H3 Community License, enabling local validation of core 768p generation. The complete production system is not fully open: H3-Context-IR and H3-Regenerate-2K remain hosted components, so reproducing the entire official 2K workflow requires MiniMax APIs.

### **When should an API product choose H3 Max instead of standard H3?**

Often, when the application values low latency, rapid creative iteration, and production throughput. It is not automatically the better API choice: standard H3 is preferable for 2K regeneration, broader multimodal conditioning, video editing, or open-weight deployment. Run an acceptance test and compare cost per usable output before choosing.

### **What should a production evaluation suite measure before switching from H3 to H3 Max?**

Measure prompt adherence, motion coherence, visual artifacts, audio quality and synchronization, identity consistency, and reviewer acceptance rate. Add operational metrics such as task-failure rate, retry rate, p50 and p95 end-to-end latency, and cost per accepted clip. Segment results by text-to-video, image-to-video, duration, resolution, aspect ratio, and prompt complexity so a strong average does not hide a weak production-critical scenario.

---

*Originally published at [https://www.cometapi.com/what-is-minimax-h3-max/](https://www.cometapi.com/what-is-minimax-h3-max/).*
