<!-- social-ops-fingerprint:92c96a6908f18546160775a94173e38744fa1c00e123909c2b98f86fd17e2e2f -->
---
title: How to Use HappyHorse 1.1 API
---
# How to Use HappyHorse 1.1 API

![How to Use HappyHorse 1.1 API](https://resource.cometapi.com/How%20to%20Use%20HappyHorse1.1%20API.webp)

## Featured Snippet Answer

HappyHorse 1.1 is Alibaba's upgraded AI video generation model family for creating short videos from text prompts, first-frame images, or multiple reference images. Through CometAPI, developers can call HappyHorse 1.1 from a unified video endpoint, create an asynchronous video task, poll the task status, and download the completed MP4. The recommended workflow is: create a CometAPI key, confirm the live model ID such as `happyhorse-1.1`, submit a `POST /v1/videos` task with a prompt, duration, and resolution, poll `GET /v1/videos/{task_id}`, then store the returned video file permanently. Public Artificial Analysis data currently ranks HappyHorse-1.1 #2 for text-to-video with audio and #2 for image-to-video with audio, behind Dreamina Seedance 2.0 720p. Teams migrating from HappyHorse 1.0 should move new T2V, I2V, and R2V generation workloads to 1.1, but keep 1.0 video editing routes until a tested replacement is available.

## Why HappyHorse 1.1 Is a Game-Changer in 2026 AI Video

In the rapidly evolving landscape of generative AI, Alibaba's HappyHorse 1.1 stands out as one of the premier AI video models of 2026. Building on the anonymous success of [HappyHorse 1.0](https://www.cometapi.com/models/aliyun/happy-horse-1-0/)—which dominated the Artificial Analysis Video Arena in April 2026—version 1.1 delivers enhanced motion expressiveness, superior subject consistency, native synchronized audio with zero-drift lip sync, improved long-context instruction following, and a new video editing modality.

Whether you're a content creator producing e-commerce ads, a filmmaker prototyping storyboards, a marketer building branded micro-dramas, or a developer integrating video into apps, HappyHorse 1.1 offers production-ready output in 720P or 1080P with durations from 3 to 15 seconds.

Accessing it directly via Alibaba Cloud can involve regional complexities and setup overhead. [**CometAPI**](https://www.cometapi.com/) simplifies this dramatically as a unified gateway to 500+ AI models, including [HappyHorse 1.1](https://www.cometapi.com/models/aliyun/happy-horse-1-1/), with OpenAI-compatible endpoints, competitive pricing, high uptime, and easy integration. This guide focuses on using it through CometAPI for seamless, cost-effective workflows.

## What Is HappyHorse 1.1?

HappyHorse 1.1 is Alibaba's (via ATH/Alibaba Cloud Model Studio) next-generation unified multimodal video synthesis model. It processes text, visual, and audio tokens in a single stream using a ~15B parameter architecture (evolved from 1.0), enabling coherent, planned outputs rather than post-assembled clips.

**Key Capabilities:**

- **Text-to-Video (T2V):** Generate videos directly from descriptive prompts.
- **Image-to-Video (I2V):** Animate a first-frame image with optional motion guidance.
- **Reference-to-Video (R2V):** Use up to 9 reference images for style, character, or environment consistency.
- **Video Editing:** New in 1.1—edit existing videos with prompts and reference images (e.g., style transfer, clothing changes).
- **Native Audio & Lip Sync:** Multilingual support (English, Mandarin, etc.) with context-aware pacing and low Word Error Rate.
- **Output Specs:** 720P/1080P, flexible aspect ratios, 3-15s durations, MP4 with synced audio.

[API docs](https://apidoc.cometapi.com/api/video/happyhorse/create) describe 1 to 5 minute generation times for video tasks, a create-task then poll-result flow, task states such as `PENDING`, `RUNNING`, `SUCCEEDED`, and `FAILED`, and result URLs that must be downloaded before they expire. That means HappyHorse 1.1 is not used like a synchronous chatbot. It belongs inside a media workflow with task records, progress UI, retries, metadata capture, and durable storage.

## Performance Benchmark: How Good Is HappyHorse 1.1?

Video model benchmarks are harder than text benchmarks because users judge motion, coherence, prompt following, image fidelity, audio, lip-sync, camera style, physics, and aesthetics at the same time. Still, public preference leaderboards are useful for shortlisting models before you run your own prompt suite.

As of the latest public Artificial Analysis snapshot checked for this article on June 29, 2026, HappyHorse-1.1 is one of the strongest audio-enabled AI video models in the public arena. On the text-to-video with audio leaderboard, Dreamina Seedance 2.0 720p leads with Elo 1,219, while HappyHorse-1.1 ranks second with Elo 1,151 and HappyHorse-1.0 ranks third with Elo 1,123. On image-to-video with audio, Dreamina Seedance 2.0 720p leads with Elo 1,194, HappyHorse-1.1 ranks second with Elo 1,117, grok-imagine-video-1.5-preview ranks third with Elo 1,110, Wan 2.7 ranks fourth with Elo 1,090, and HappyHorse-1.0 ranks fifth with Elo 1,089.

The no-audio categories add nuance. Artificial Analysis currently lists HappyHorse-1.0 slightly ahead of HappyHorse-1.1 for text-to-video without audio, with HappyHorse-1.0 at Elo 1,290 and HappyHorse-1.1 at Elo 1,285. For image-to-video without audio, Dreamina Seedance 2.0 720p leads at Elo 1,343, while HappyHorse-1.1 ranks fifth at Elo 1,311.

### Benchmark Snapshot

| Category | Leader | HappyHorse 1.1 rank | HappyHorse 1.1 Elo | What it means |
| --- | --- | --- | --- | --- |
| Text-to-video with audio | Dreamina Seedance 2.0 720p, 1,219 | #2 | 1,151 | Strong audio-enabled T2V candidate and ahead of HappyHorse 1.0 |
| Image-to-video with audio | Dreamina Seedance 2.0 720p, 1,194 | #2 | 1,117 | Strong for image-led commercial workflows with native audio |
| Text-to-video without audio | HappyHorse 1.0, 1,290 | #2 | 1,285 | Very close to 1.0, but not the current no-audio T2V leader |
| Image-to-video without audio | Dreamina Seedance 2.0 720p, 1,343 | #5 | 1,311 | Competitive, but not the top no-audio I2V model |

The practical conclusion is not that HappyHorse 1.1 wins every category. The better conclusion is that HappyHorse 1.1 is a serious production candidate for with-audio short video, especially when reference consistency and visual controllability matter. If you are building with CometAPI, benchmark HappyHorse 1.1 against Seedance, Wan, Kling, Veo, Sora-style routes, and HappyHorse 1.0 using your own prompts, brand assets, review criteria, and budget.

## HappyHorse 1.1 vs Alternatives

| Model | Provider | Strongest fit | Public benchmark signal | CometAPI recommendation |
| --- | --- | --- | --- | --- |
| HappyHorse 1.1 | Alibaba | T2V, I2V, R2V, short clips with audio, reference-guided brand videos | #2 on Artificial Analysis T2V with audio and #2 on I2V with audio in the current snapshot | Test as default for new HappyHorse generation workflows |
| HappyHorse 1.0 | Alibaba | Existing HappyHorse prompts, no-audio T2V strength, video editing routes | #1 on Artificial Analysis T2V without audio; below 1.1 in with-audio T2V and I2V | Keep for stable legacy prompts and editing until replaced |
| Dreamina Seedance 2.0 720p | ByteDance Seed | General video quality and benchmark-leading audio-enabled generation | #1 on T2V with audio and #1 on I2V with audio in the current snapshot | Include in bake-offs for quality-sensitive campaigns |
| Wan 2.7 | Alibaba | Custom audio, first/last-frame workflows, continuation, broader video operations | Competitive I2V with audio result, but behind HappyHorse 1.1 in current snapshot | Use when workflow needs custom audio or continuation controls |
| Kling 3.0 Pro | KlingAI | Cinematic motion, action-heavy scenes, alternative style direction | Competitive top-ten audio-enabled video rankings | Keep as style and fallback option |
| Claude Opus 4.8 | Anthropic | Prompt planning, scriptwriting, QA, automation, agent workflows | Not a video generator; latest Anthropic release emphasizes coding and long-running agentic work | Use as the planning and QA layer around HappyHorse generation |

## Prerequisites

Before calling HappyHorse 1.1 through CometAPI, prepare the following:

1. A CometAPI account and API key.
2. A backend runtime such as Node.js, Python, Go, PHP, or serverless functions.
3. A server-side environment variable such as `COMETAPI_KEY`.
4. A target workflow: text-to-video, image-to-video, or reference-to-video.
5. A prompt written as a shot brief, not a loose caption.
6. Optional first-frame or reference images hosted at public HTTPS URLs, or uploaded according to the active CometAPI route.
7. A target duration, usually 3, 5, 10, or 15 seconds.
8. A target resolution, normally 720p for testing and 1080p for final assets.
9. A database table or job store for `task_id`, user ID, prompt, model, parameters, status, cost estimate, and output URL.
10. Durable storage for completed MP4 files because generated result URLs can be temporary.
11. Retry logic for `429`, timeouts, and temporary upstream failures.
12. A fallback model plan for provider outages, policy edge cases, latency spikes, or cost changes.

CometAPI is useful because it lets teams centralize model access, credentials, billing visibility, and model switching. For a production video application, that reduces the amount of provider-specific code you need to maintain.

## How to Use HappyHorse 1.1 API in CometAPI

The exact model catalog and parameter schema can evolve, so verify the live CometAPI model page and API docs before deploying. The practical pattern is stable: create a video task, poll the task, then download and store the final MP4.

### Step 1: Store Your API Key

Never expose a CometAPI key in browser JavaScript, mobile apps, public GitHub repositories, or client-side logs. Store it server-side:

```
export COMETAPI_KEY="your_cometapi_key"
```

For production, use a secret manager such as AWS Secrets Manager, Google Secret Manager, Azure Key Vault, Doppler, Infisical, or your platform's encrypted environment variable store.

### Step 2: Confirm the Model ID

For CometAPI examples, use the public model ID shown in the live catalog. The expected HappyHorse 1.1 model ID is commonly:

```
happyhorse-1.1
```

Alibaba's direct API exposes mode-specific IDs such as `happyhorse-1.1-t2v`, `happyhorse-1.1-i2v`, and `happyhorse-1.1-r2v`. CometAPI may simplify that behind one video model ID or expose route-specific variants. Check the CometAPI model catalog before hardcoding production traffic.

### Step 3: Create a Text-to-Video Task

Use this when you only have a written creative brief.

```
curl https://api.cometapi.com/v1/videos \  -H "Authorization: Bearer $COMETAPI_KEY" \  -F "model=happyhorse-1.1" \  -F "prompt=A 7-second vertical ecommerce video for a matte black smart speaker on a marble kitchen counter. The camera slowly dollies in from a three-quarter angle. Warm morning sunlight, soft reflections, tiny dust particles, premium consumer electronics commercial style. Native ambient room tone, subtle startup chime, no extra text, keep the speaker shape consistent." \  -F "seconds=7" \  -F "size=720x1280"
```

If your CometAPI dashboard shows `resolution` and `aspect_ratio` instead of `size`, use the active schema, for example:

```
curl https://api.cometapi.com/v1/videos \  -H "Authorization: Bearer $COMETAPI_KEY" \  -F "model=happyhorse-1.1" \  -F "prompt=A cinematic close-up of a glass perfume bottle on black stone, slow macro push-in, gold rim light, faint mist, elegant piano notes, label remains readable." \  -F "seconds=5" \  -F "resolution=720p" \  -F "aspect_ratio=16:9"
```

The response should return a task identifier. Store it immediately:

```
{  "id": "task_example",  "task_id": "task_example",  "object": "video",  "model": "happyhorse-1.1",  "status": "queued",  "progress": 0,  "created_at": 1779938152}
```

### Step 4: Create an Image-to-Video Task

Use image-to-video when you have an approved first frame, such as a product render, fashion shot, app screenshot, character portrait, or design mockup. The prompt should describe motion rather than re-describing everything visible in the image.

```
curl https://api.cometapi.com/v1/videos \  -H "Authorization: Bearer $COMETAPI_KEY" \  -F "model=happyhorse-1.1" \  -F "prompt=Animate the uploaded product photo into a 5-second premium product reveal. Keep the product color, shape, logo, and label unchanged. Add a slow clockwise camera orbit, soft studio highlights, gentle background movement, and subtle ambient sound. No new text or extra objects." \  -F "image_url=https://example.com/assets/smart-speaker-first-frame.png" \  -F "seconds=5" \  -F "size=1280x720"
```

For first-frame image workflows, use clean source images. Alibaba's image-to-video docs list JPEG, JPG, PNG, and WEBP inputs, up to 20 MB, with width and height at least 300 pixels and aspect ratio between 1:2.5 and 2.5:1. Even if CometAPI handles provider details for you, poor source images still produce poor outputs.

### Step 5: Create a Reference-to-Video Task

Use reference-to-video when identity matters. This is the right mode for brand mascots, recurring characters, fashion looks, product packaging, props, rooms, vehicles, or scenes that must stay recognizable.

```
curl https://api.cometapi.com/v1/videos \  -H "Authorization: Bearer $COMETAPI_KEY" \  -F "model=happyhorse-1.1" \  -F "prompt=[Image 1] is the exact red running shoe. [Image 2] is the athlete. Create an 8-second vertical sports ad: the athlete ties the shoe, steps onto wet pavement, then sprints through a neon-lit city street. Low-angle tracking shot, realistic splash physics, energetic drum rhythm, keep the shoe color and side logo visible throughout." \  -F "reference_image_urls[]=https://example.com/assets/red-shoe.png" \  -F "reference_image_urls[]=https://example.com/assets/athlete.png" \  -F "seconds=8" \  -F "size=720x1280"
```

Alibaba's reference-to-video docs allow 1 to 9 reference images and recommend referring to them in the prompt as `[Image 1]`, `[Image 2]`, and so on, matching the order of the media array. That is a useful habit even when calling through CometAPI because it makes the creative instruction unambiguous.

### Step 6: Poll the Task

Video generation is asynchronous. Poll until the task reaches a terminal state:

```
curl https://api.cometapi.com/v1/videos/{task_id} \  -H "Authorization: Bearer $COMETAPI_KEY"
```

A production poller should use a reasonable interval, such as 10 to 15 seconds, and should stop after a timeout that matches your product experience. Store the latest status in your database so users can refresh the page without losing progress.

### Step 7: Download the Completed MP4

When the status is complete, download the content:

```
curl https://api.cometapi.com/v1/videos/{task_id}/content \  -H "Authorization: Bearer $COMETAPI_KEY" \  -o happyhorse-1-1-output.mp4
```

Do not rely on a temporary provider URL as your permanent asset link. Download the MP4, upload it to your storage bucket, attach metadata, then serve the stored asset through your own CDN or media service.

## How Much Does HappyHorse 1.1 API Cost?

Alibaba Cloud's Model Studio pricing page lists HappyHorse 1.1 video generation by output duration. In Singapore, the listed HappyHorse 1.1 price is `$0.14/sec` for 720P and `$0.18/sec` for 1080P. In US (Virginia) and Germany (Frankfurt), Alibaba lists `$0.123769/sec` for 720P and `$0.165026/sec` for 1080P. Alibaba's listed 1080P price for HappyHorse 1.0 is higher in the same tables, which makes 1.1 attractive for teams rendering final 1080P clips.

### Cost Examples at CometAPI Public Prices

CometAPI's Happy Horse 1.1 model 720p generation at `$0.112/sec` and 1080p generation at `$0.144/sec`, compared with an official 720p price shown as `$0.14/sec`, or a listed 20% saving.

| Clip duration | 720p at $0.112/sec | 1080p at $0.144/sec |
| --- | --- | --- |
| 3 seconds | $0.336 | $0.432 |
| 5 seconds | $0.560 | $0.720 |
| 7 seconds | $0.784 | $1.008 |
| 10 seconds | $1.120 | $1.440 |
| 15 seconds | $1.680 | $2.160 |

The better production metric is not only cost per generation. Track cost per approved clip. If a 5-second 720p draft costs `$0.56` but you need eight retries, the approved clip costs `$4.48` before review and storage. If a better prompt or stronger reference image reduces retries from eight to three, the cost improvem

The better production metric is not only cost per generation. Track cost per approved clip. If a 5-second 720p draft costs `$0.56` but you need eight retries, the approved clip costs `$4.48` before review and storage. If a better prompt or stronger reference image reduces retries from eight to three, the cost improvement is larger than a small price difference between models.

Recommended CometAPI cost strategy:

1. Run first drafts at 720p and short duration.
2. Generate 3 to 5 variants per prompt family.
3. Score outputs with a consistent rubric.
4. Promote winning prompts to 1080p.
5. Save every prompt, image reference, model ID, seed if available, task ID, cost estimate, and reviewer decision.
6. Compare HappyHorse 1.1 against alternatives by cost per accepted asset.

## HappyHorse 1.0 Migration Guide

Most teams should not migrate by flipping every request to 1.1 overnight. Use a staged plan.

### What Changes From 1.0 to 1.1?

| Area | HappyHorse 1.0 | HappyHorse 1.1 | Migration recommendation |
| --- | --- | --- | --- |
| T2V generation | Strong, especially no-audio leaderboard results | Stronger current with-audio public ranking | Move new prompt-led generation tests to 1.1 |
| I2V generation | Strong image animation | Better with-audio public ranking and improved motion consistency | Move product-photo and first-frame workflows to 1.1 after batch testing |
| R2V generation | Supports reference-guided workflows | Alibaba highlights improved multi-reference interpretation and visual consistency | Prioritize 1.1 for brand and character consistency |
| Prompt behavior | Existing prompts may be tuned for 1.0 quirks | Better instruction following can change output style | Re-test top production prompts before switching |

### Migration Checklist

1. Export your top 20 to 50 HappyHorse 1.0 prompts.
2. Group them by workflow: T2V, I2V, R2V, and video edit.
3. Run the same prompt, duration, resolution, and reference images through HappyHorse 1.1.
4. Score outputs on prompt adherence, motion quality, subject fidelity, audio usefulness, artifact rate, brand safety, and cost.
5. Keep HappyHorse 1.0 for prompts where 1.0 still wins or where video editing is required.
6. Move new generation workflows to 1.1 where it improves acceptance rate.
7. Update your prompt templates to use clearer constraints and reference labels.
8. Add model routing in your backend so `happyhorse-1.0`, `happyhorse-1.1`, and alternatives can be selected per job type.
9. Monitor failure rate, average generation time, cost per accepted clip, and reviewer rejection reasons.
10. Roll out gradually by project, customer segment, or media type.

### Backward-Compatible Routing Example

```
function chooseVideoModel(job) {
  if (job.type === "video_edit") {
    return "happyhorse-1.0";
  }

  if (job.requiresCustomAudio || job.needsFirstLastFrameControl) {
    return "wan2.7";
  }

  if (job.hasReferenceImages || job.requiresBrandConsistency) {
    return "happyhorse-1.1";
  }

  if (job.isBenchmarkExperiment) {
    return job.experimentalModel ?? "happyhorse-1.1";
  }

  return "happyhorse-1.1";
}
```

This keeps the migration reversible. If a model route changes, you update routing rather than rewriting product code.

## Common Errors and Best Practices

### Store Outputs Immediately

Temporary result URLs can expire. Your worker should download the final MP4 and upload it to your own storage as soon as the task succeeds.

### Validate Image Inputs

Reject tiny, blurry, compressed, or wrong-aspect images before they hit the API. For R2V, use clean references with one obvious subject per image when possible.

### Build Human Review Into the Workflow

AI video is probabilistic. Even strong models produce artifacts. A production system needs approval states, rejection reasons, and regeneration controls.

### Keep Source Metadata

Save the original prompt, normalized prompt, model ID, image URLs, task ID, duration, resolution, cost estimate, output URL, permanent asset URL, reviewer, and decision. This dataset becomes your internal benchmark.

## Conclusion: Start Building with HappyHorse 1.1 on CometAPI Today

HappyHorse 1.1 represents a leap in accessible, high-quality AI video. Through CometAPI, integration is straightforward, cost-effective, and powerful. Sign up, grab your key, and experiment in the playground—your next viral video or ad campaign is seconds away.

**Call to Action:** Visit [CometAPI](https://www.cometapi.com) for free credits, full docs, and 500+ models. Share your creations and join the community pushing AI video boundaries.

## FAQs about HappyHorse 1.1

### What is HappyHorse 1.1?

HappyHorse 1.1 is Alibaba's upgraded AI video generation model family for creating short videos from text prompts, first-frame images, or multiple reference images. It is designed for short 3 to 15 second clips with 720P or 1080P output and audio-video generation.

### Is HappyHorse 1.1 available through CometAPI?

Yes. CometAPI lists Happy Horse 1.1 on its model and pricing pages and documents unified video generation APIs. Check the live CometAPI catalog for the current model ID, status, supported parameters, and resolution-specific pricing before deployment.

### What model ID should I use?

For CometAPI, use the live catalog value, commonly `happyhorse-1.1`. Alibaba's direct Model Studio API uses mode-specific IDs: `happyhorse-1.1-t2v`, `happyhorse-1.1-i2v`, and `happyhorse-1.1-r2v`.

### Does HappyHorse 1.1 support reference images?

Yes. 1 to 9 reference images. In prompts, refer to them as `[Image 1]`, `[Image 2]`, and so on in the same order as the media array.

### How long does HappyHorse 1.1 video generation take?

Typical video task times of 1 to 5 minutes. Actual latency can vary by duration, resolution, queue load, route, and provider availability.

### How much does HappyHorse 1.1 cost on CometAPI?

CometAPI's public Happy Horse 1.1 page lists `$0.112/sec` for 720p and `$0.144/sec` for 1080p. Always verify live pricing in the dashboard because video prices can vary by resolution, route, region, and promotion.

### Should I use HappyHorse 1.1 or HappyHorse 1.0?

Use HappyHorse 1.1 for new T2V, I2V, and R2V tests where smoother motion, better prompt following, audio-video quality, and reference consistency matter. Keep HappyHorse 1.0 for legacy prompts that already perform well and for video editing routes until you have tested a replacement.

---

*Originally published at [https://www.cometapi.com/how-to-use-happyhorse-1-1-api/](https://www.cometapi.com/how-to-use-happyhorse-1-1-api/).*
