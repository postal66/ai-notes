<!-- social-ops-fingerprint:9280ee245fabeb1fbefc192af1abc6040ff65f27e00019563d1756db1430a960 -->
---
title: How to Use Veo 3.1 API
---
# How to Use Veo 3.1 API

![How to Use Veo 3.1 API](https://resource.cometapi.com/blog/uploads/2025/10/How-to-Use-Veo-3.1-API.webp)

Veo 3.1 is the latest iteration of Google’s Veo family of video-generation models. It brings richer native audio, better narrative and cinematic control, multi-image guidance, and new editing primitives (first/last-frame transitions, “ingredients” / reference images, and scene extension workflows). For developers the quickest way to access Veo 3.1 is the API (for consumer-facing integrations) and Vertex AI (for enterprise and cloud workloads).

## What is the Veo 3.1 API and what are its key features?

Veo 3.1 is a text-and-image → video generative model from Google designed to produce short, high-quality, cinematic clips with natively generated audio (dialogue, ambient cues, sound effects). The release focuses on improving prompt adherence, character consistency, audio generation, and more granular editing controls (for example: first→last frame transitions and guidance via up to three reference images).

### Key capabilities (at a glance)

- **Text → Video**: Generate videos straight from narrative prompts (dialogue & audio included).
- **Image → Video**: Transform an image into a short animated scene. ()
- **Reference images (“Ingredients to video”)**: Supply up to **3** images (characters, objects, styles) to keep visual consistency across outputs.
- **First & Last Frame generation**: Create transitions bridging two images (the model generates frames that smoothly morph between them, with matching audio).
- **Scene extension workflows**: Tools to extend an existing clip by generating new clips tied to the tail of a prior video (note: capabilities and support differ between Gemini API and Vertex preview—see the “conditions” section).
- **Native audio & SFX**: The model can synthesize speech, ambient sound, and synchronized effects that match the generated visuals.

## How do I use the Veo 3.1 API — what are the prerequisites and conditions?

## What do you need before calling the API?

1. **Access & billing**: Veo 3.1 is in paid preview—ensure you have a API key or a Google Cloud project with Vertex AI enabled and billing set up. Some features and model variants are region-limited in preview.
2. **Quotas & preview constraints**: Preview models often have per-project request rate limits (examples: 10 RPM for preview variants) and limits on videos per request. Check the model page in Vertex AI / Gemini docs for exact numbers for your account.
3. **Input assets & format**: You can generate from text prompts, from single or multiple images, or extend an existing Veo-generated video by referencing its URI. For image-to-video workflows, supply images in the supported formats (URLs or bytes depending on the endpoint).
4. **Safety & provenance**: Generated content must comply with Google’s content policies. In preview, watermarks or usage flags may appear; be prepared to handle provenance and content moderation steps in your application.

## Which authentication methods are supported?

- **API key**: For the Gemini hosted endpoints or key of the third-party API platform. I recommend CometAPI,  [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate Veo 3.1 API(veo3.1-pro; veo3.1)
- **Google Cloud credentials / ADC**: For Vertex AI, use Application Default Credentials (service account / gcloud auth) or an API key attached to your Google Cloud project.

## What are the Veo 3.1 API endpoints and which parameters matter most?

> Short answer: You will either call the **CometAPI API** video generation endpoint (for CometAPI-hosted access, `v1/chat/completions`) . Both use a JSON request body describing model, prompt(s), and a `video`/`output` configuration; larger video jobs are returned as long-running operations.

Common endpoints (examples):

```
curl --location --request POST 'https://api.cometapi.com/v1/chat/completions' \
--header 'Authorization: {{api-key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"model": "veo3.1-pro",
"stream": true,
"messages":
}'
```

## Typical request parameters (logical breakdown)

- **model** — model identifier to target (veo3.1-pro; veo3.1 names listed in [model reference](https://www.cometapi.com/pricing/)).
- **prompt / input** — human text describing the scene; can include multiple prompts or multi-shot instructions depending on model capabilities. Use structured prompts to control camera moves, time of day, mood, and audio cues.
- **image\_references** — 1–3 image URIs or base64 imagesto guide objects/characters/styles (Veo 3.1 supports multiple image references).
- **video** — used when *extending* a previous Veo output (pass the initial video URI). Some features only operate on Veo-generated videos.
- **duration / fps / resolution / aspectRatio** — select from supported lengths and formats (preview models list supported durations and framerates—e.g., 4, 6, 8s in some preview docs; extensions may allow longer outputs in Flow/Studio).

## What are advanced usage patterns and techniques?

### 1) Maintain character consistency with reference images

Supply up to three reference images (faces/poses/costume) to maintain the look of a character across multiple generated shots. Typical flow:

1. Upload or inline encode your reference images.
2. Pass them in `config.reference_images` when generating each shot.
3. Use the same images for subsequent generation calls (or combine with seed values) to maximize visual consistency.

```
curl -s -X POST "https://api.cometapi.com/v1/chat/completions" \
-H "Authorization: Bearer cometapi_KEY" \
-H "Content-Type: application/json" \
-d '{
"model": "veo3.1-pro",
"messages": [
{
"role": "user",
"content": "Create a cinematic 6s shot: a fashion editorial on a city rooftop at golden hour. Keep the subject look consistent with the reference images."
}
],
"extra_body": {
"google": {
"referenceImages": [
{ "image": { "uri": "https://example.com/ref1.jpg" }, "referenceType": "asset" },
{ "image": { "uri": "https://example.com/ref2.jpg" }, "referenceType": "asset" },
{ "image": { "uri": "https://example.com/ref3.jpg" }, "referenceType": "asset" }
],
"config": {
"resolution": "1080p",
"durationSeconds": 6,
"fps": 24,
"aspectRatio": "16:9",
"generateAudio": true
}
}
}
}'
```

### 2) First-and-last frame transitions (shot synthesis)

Use `image` (first frame) + `config.last_frame` to instruct Veo to synthesize the intermediate motion. This is ideal for cinematic transitions — it produces natural visual interpolation and synchronized audio.

Provide a **first frame** (`image`) and a **last frame** (`lastFrame`) and Veo 3.1 will interpolate the motion between them to produce a smooth transition (with optional audio). cURL (REST) example — first + last images:

```
curl -s -X POST "https://api.cometapi.com/v1/chat/completions" \
-H "Authorization: Bearer cometapi_KEY" \
-H "Content-Type: application/json" \
-d '{
"model": "veo-3.1",
"messages": [
{
"role": "user",
"content": "Interpolate between these two images to create an 8s cinematic morph: from 'sunlit victorian parlor' (first) to 'overgrown ruin' (last). Add soft ambient sound."
}
],
"extra_body": {
"google": {
"image": { "uri": "https://example.com/first_frame.jpg" },
"lastFrame": { "uri": "https://example.com/last_frame.jpg" },
"config": {
"resolution": "1080p",
"durationSeconds": 8,
"fps": 24,
"aspectRatio": "16:9",
"generateAudio": true
}
}
}
}'
```

### 3) Scene extension (chain multiple generations)

There are two patterns:

- **API/Flow approach (preview features)**: You pass an existing video (a returned video object or URI) as `video=video_to_extend` to create a follow-on clip that is consistent with the prior scene. Use the operation response to capture the `video.uri` and feed it into the next call to extend the narrative. Note: availability and behavior can vary by platform, so validate on the platform you choose.
- **Vertex cloud pattern**: Vertex’s preview model has stricter document-listed limits (e.g., current preview only returns 4/6/8 second segments), so to produce minute-long outputs you must chain multiple requests and stitch them in your application or use the engine’s official scene extension tools where available. Check Vertex’s “Veo 3.1 preview” page for current support matrix.

Take a **previously Veo-generated** video and extend it forward (add seconds) while preserving style and continuity. The API requires the input to be a Veo-generated video (extensions of arbitrary MP4s may be unsupported). You can extend by 7s hops up to documented limits (Veo preview limits apply):

```
curl -s -X POST "https://api.cometapi.com/v1/chat/completions" \
-H "Authorization: Bearer cometapi_KEY" \
-H "Content-Type: application/json" \
-d '{
"model": "veo-3.1",
"messages": [
{
"role": "user",
"content": "Extend the last scene: the origami butterfly flies into the garden and a puppy runs up to the flower; continue action for ~7 seconds."
}
],
"extra_body": {
"google": {
"video": { "uri": "https://storage.googleapis.com/your-bucket/butterfly_video_id.mp4" },
"config": {
"numberOfVideos": 1,
"resolution": "720p",
"durationSeconds": 7,
"fps": 24,
"generateAudio": true
}
}
}
}'
```

### 4) Audio & dialogue control

Veo 3.1 generates native audio (speech and effects) from prompts. Tricks:

- Put any spoken lines in your prompt (wrap dialogue in quotes) to encourage realistic lip sync.
- Add audio descriptors (“soft footsteps left to right”, “muffled thunder crescendo”) to shape SFX and mood.
- Use seed values to reproduce the same audio/visual outcome across test runs.

### 5) Deterministic outputs for testing (seeds)

If you need repeatable outputs for CI or A/B testing, supply a `seed` parameter (uint32). Changing the prompt or reference images will still alter the result; seed guarantees repeatability *only* when everything else is identical.

### 6) Cost & performance optimizations

- **Batch fewer, larger jobs**: Where allowed, set `sampleCount` to produce multiple candidate videos in one request (1–4) to reduce setup overhead. ()
- **Cache reference images and reuse seeds** for reproducibility so you avoid re-uploading large binaries.
- **Use Cloud Storage outputs** (Vertex) for large output sizes to avoid returning raw bytes in the request body.

### 7) Multi-step pipelines with other Gemini models

A useful pipeline: use a still-image generator (e.g., Gemini image model) to create assets → pass best images as `image` + `referenceImages` to Veo 3.1 → iterate audio/dialogue prompts with the text model for generated narration. The Gemini docs explicitly show examples chaining image generation and Veo calls.

## Practical tips, gotchas, and best practices

- **Use seeds** when you want deterministic, repeatable outputs between runs (same prompt + same references + same seed → same generation).
- **Keep reference images consistent**: same crop, same face angle, consistent clothing/background helps the model keep identity and style. Reuse the same three images across shots to preserve continuity.
- **Prefer GCS URIs for production**: storing images and outputs in Cloud Storage avoids base64 transfer size limits and simplifies chaining / extension.
- **Explicitly describe transitions & audio**: for first/last transitions, add camera move, tempo, and SFX/voice cues in the prompt for better synchronized audio.
- **Test short loops first**: iterate with short durations (4–8s) while you tune prompts, seeds, and reference images, then chain extensions for longer scenes.
- **Confirm exact field names**: SDKs may use `reference_images` (snake\_case), `referenceImages` (camelCase), or nested `image` objects with `content` / `gcsUri`. Check the SDK docs or the Vertex model schema for the exact property names in the version you use.

## What does Veo 3.1 cost and how is it billed?

Veo 3.1 is billed **per second of generated video**, and Google exposes multiple variants (for example **Standard** and **Fast**) with different per-second rates. The published developer pricing shows example paid-tier rates of **$0.40 / second for Veo 3.1 Standard** and **$0.15 / second for Veo 3.1 Fast**. The Gemini pricing page also notes you’re charged only when a video is successfully generated (failed attempts may not be billed).

### [Veo 3.1 API](https://www.cometapi.com/veo-3-1-api/) Pricing in CometAPI

|  |  |
| --- | --- |
| veo3.1 | 0.4000 |
| veo3.1-pro | 2.0000 |

## Conclusion — why Veo 3.1 matters for developers right now

Veo 3.1 is a clear incremental leap for AI video generation: richer native audio, reference-image guidance, and new editing primitives make it a stronger option for storytelling, previsualization, and creative apps. The model ‘s exact capabilities differ slightly between endpoints and preview builds (For example, the version difference between CometAPI and gemini)— so test and validate the model variant you intend to use. The examples in this guide give a practical starting point for prototyping and production.

## How to Access [Veo 3.1 API](https://www.cometapi.com/veo-3-1-api/) API

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access [Veo 3.1 API](https://www.cometapi.com/veo-3-1-api/) through CometAPI, [the latest model version](https://www.cometapi.com/pricing/) is always updated with the official website. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-use-veo-3-1-api/](https://www.cometapi.com/how-to-use-veo-3-1-api/).*
