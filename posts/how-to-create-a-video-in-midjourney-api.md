<!-- social-ops-fingerprint:2d9feb17ff8b139a9a4d8171096f533eadc5742e7bb6e3f90cf13b85423455aa -->
---
title: How to create a video in midjourney API
---
# How to create a video in midjourney API

![How to create a video in midjourney API](https://resource.cometapi.com/blog/uploads/2025/12/How%2520to%2520create%2520a%2520video%2520with%2520CometAPI%25E2%2580%2599s%2520Midjourney%2520integration.webp)

Midjourney’s move into video has been one of 2025’s biggest creative-technology stories. What started as a beloved image-first tool has added an “Image-to-Video” workflow that turns stills into short animated clips — and the system is changing fast.

Midjourney’s video capability is an image-to-video workflow that animates a single image into a short clip via an “Animate” flow, producing five-second clips by default and allowing extensions up to ~21 seconds. The feature launched in mid-2025 as Midjourney’s V1 video model and is available through CometAPI's Midjourney Video V1 API.

## What is Midjourney V1

### What Midjourney V1 does and how it’s surfaced to users

Midjourney’s V1 video model turns a single still image (either one generated inside Midjourney or an externally hosted image) into short animated clips — by default about 5 seconds — using either automatic or manual animation modes and motion intensity flags (`--motion low` / `--motion high`). Users can extend clips in 4-second increments (up to ~21 seconds) and control batch size, looping and end frames; video outputs are MP4. Midjourney’s V1 Video model is an **image-to-video** model optimized for short, stylized, loopable clips. Typical characteristics of the V1 model include:

- Base clip length ~5 seconds, with a controlled extension mechanism (4-second increments, up to a documented limit).
- Emphasis on preserving artistic style from the source image (brushwork, color, mood).
- Resolution and quality tradeoffs for fast iteration; V1 is oriented toward social and web content rather than full cinematic output.

These constraints shape how you design assets and prompts: V1 is best used for concise motion, animated stills, product hero loops, or short character tunes rather than long scenes.

### How CometAPI surfaces the Midjourney Video model

CometAPI is a multi-model gateway that aggregates access to hundreds of AI models (text, image, audio, and now image-to-video) behind a single REST surface.Its Midjourney Video offering wraps Midjourney’s V1 Video capability so engineers can call image-to-video generation programmatically rather than relying solely on Discord/web interaction. That makes it useful for automating creative pipelines, building proof-of-concepts, and integrating short animated assets into apps or content-production workflows.

CometAPI’s [Midjourney Video](https://www.cometapi.com/midjourney-video-api/) can provide developers authenticate, call a `/mj/submit/video` endpoint and pass parameters such as the `prompt` (which can include a starting image URL), `videoType` (e.g., `vid_1.1_i2v_480`), `mode` (fast/relax), and `animateMode` (automatic/manual). CometAPI has lower per-call pricing and convenience (single API key + REST interface) versus integrating directly via Midjourney’s Discord-centric workflow.

## How do I prepare before I call the API?

### What credentials and accounts do I need?

1. Sign up at CometAPI and generate an API key from your account dashboard (CometAPI uses a bearer token like `sk-xxxxx`).
2. Make sure you have image assets available online (a publicly accessible URL) if you plan to use external images as the starting frame. Midjourney needs reachable URLs for external image→video workflows.

### What decisions to make up front

- **Starting image** — pick an image with a clear subject and composition; aspect ratio affects final video resolution/aspect (Midjourney maps starting aspect ratios to SD/HD pixel sizes).
- **Motion style** — decide Low vs High motion (`--motion low` vs `--motion high`) and whether you want automatic inference or manual control of camera/subject motion.
- **Length & batch size** — default is 5 seconds; you can extend up to ~21s. Batch size defaults to 4 (Midjourney returns 4 variants), but you can request 1 or 2 to save compute.
- **Resolution** — V1 is primarily SD (480p) by default; HD (720p) needs parameter description, such as vid\_1.1\_i2v\_480.

## How do I call CometAPI’s Midjourney video endpoint (step-by-step with examples)?

### What’s the minimal request payload?

At minimum, you send:

- `prompt`: the starting image URL and optional textual motion prompt (e.g., `"https://.../frame.png add a dog running from left to right"`).
- `videoType`: e.g., `vid_1.1_i2v_480`.
- `mode`: `"fast"` (or `"relax"` if allowed by plan).
- `animateMode`: `"automatic"` or `"manual"`.

This is a sample `curl` illustrating a POST to[`https://api.cometapi.com/mj/submit/video`. Here’s a cleaned, copy-ready `curl` example adapted from CometAPI’s example:

```
curl --location --request POST 'https://api.cometapi.com/mj/submit/video' \
  --header 'Authorization: Bearer sk-YOUR_COMETAPI_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "prompt": "https://cdn.midjourney.com/example/0_0.png A peaceful seaside scene — camera slowly zooms out and a gull flies by",
    "videoType": "vid_1.1_i2v_480",
    "mode": "fast",
    "animateMode": "manual",
    "motion": "low",
    "bs": 1
  }'
```

### Python example (requests)

If you prefer Python, here’s a robust example using `requests` that submits a video job and polls for completion (replace placeholders). This is a practical pattern: submit → poll → download. The example below is intentionally simple and should be adapted to your app’s async/job system in production.

```
import time
import requests

API_KEY = "sk-YOUR_COMETAPI_KEY"
BASE = "https://api.cometapi.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

payload = {
    "prompt": "https://cdn.midjourney.com/example/0_0.png A calm city street — camera pans left, rain falling",
    "videoType": "vid_1.1_i2v_480",
    "mode": "fast",
    "animateMode": "manual",
    "motion": "low",
    "bs": 1
}

# Submit job
r = requests.post(f"{BASE}/mj/submit/video", json=payload, headers=HEADERS)
r.raise_for_status()
job = r.json()
job_id = job.get("id") or job.get("job_id")

# Poll for completion (example polling)
status_url = f"{BASE}/mj/status/{job_id}"
for _ in range(60):  # poll up to ~60 times
    s = requests.get(status_url, headers=HEADERS)
    s.raise_for_status()
    st = s.json()
    if st.get("status") == "completed":
        download_url = st.get("result", {}).get("video_url")
        print("Video ready:", download_url)
        break
    elif st.get("status") in ("failed", "error"):
        raise RuntimeError("Video generation failed: " + str(st))
    time.sleep(2)
```

## How do I add audio (voice, music, sound effects) to a Midjourney/CometAPI video?

### Does Midjourney produce audio natively?

No — as of V1, Midjourney’s video output is silent (MP4 without embedded audio). Users augment sound externally. (There are other AI systems that generate audio/video together, but Midjourney’s V1 focuses on visual motion.)

### Recommended pipelines to add voice and sound

1. **Text-to-Speech (TTS) for narration/voice** — Use ElevenLabs, Replica, or similar voice-cloning/TTS services to generate speech tracks from scripts. These services let you produce natural speech styles and sometimes at low cost per minute. (LinkedIn / community posts recommend ElevenLabs as a lightweight choice for voice.)
2. **AI audio design tools for music/SFX** — Tools like MM Audio, Magicshot or specialized SFX generators can generate background ambiances and effects that fit the clip. Community guides and tutorials show good quality from MM Audio and other audio AIs.
3. **Manual DAW/Editor approach (fine control)** — Import the generated MP4 into DaVinci Resolve / Premiere / Audacity, add TTS audio, sound effects, and mix. This is the best route for precise lip sync and timing. Community tutorials and YouTube walkthroughs show step-by-step approaches for matching audio to Midjourney videos.

### Quick example: combine audio + video with `ffmpeg`

Assuming `video.mp4` (silent) and `speech.mp3` (TTS) are ready:

```
# Normalize audio length (optional), then combine:
ffmpeg -i video.mp4 -i speech.mp3 -c:v copy -c:a aac -shortest output_with_audio.mp4
```

For more advanced mixes (background music + dialogue + sound fx), render a single mixed audio track from your DAW and then mux it into the video as above.

## How should I write motion prompts to control animation?

### Motion prompt patterns

Motion prompting in Midjourney V1 is natural-language driven. Useful patterns:

- **Directional / action**: “camera dolly left while the subject walks forward”
- **Object motion**: “leaf falls from tree and drifts toward camera”
- **Camera instruction**: “slow zoom in, slight parallax, 2x speed”
- **Temporal quality**: “subtle motion, loopable, cinematic rhythm”

Start with a concise motion sentence, then append adjectives for style and timing: e.g., `"start_frame_url animate: 'slow spiral camera, subject bobs gently, loopable', style: 'film grain, cinematic, 2 fps tempo'"`. Experimentation and small iterations are essential.

### Manual vs automatic animation

- **Automatic**: Let the model infer plausible motion. Best for quick experiments.
- **Manual**: Supply explicit camera paths and subject vectors for consistent, repeatable results — useful when you need predictable choreography or to match live-action footage.

## How do I extend videos, change batch size, or create loops?

### Extending video length

After generation, Midjourney (and wrappers like CometAPI) expose "Extend" controls. Midjourney’s UI lets you extend a 5-second clip by 4 seconds per extend (up to ~21 seconds). Programmatically, you either call the same endpoint with an `extend` flag or submit a new `extend` job referencing the original clip (CometAPI’s docs show the parameterized endpoints and buttons in their overview). Expect extension costs similar to an initial generation.

### Creating looped videos or specifying end frames

- To loop, reuse the starting frame as the ending frame or add the `--loop` parameter.
- For a different end frame, provide another image URL (as `end`) and ensure it’s compatible in aspect ratio. Midjourney supports a `--end` parameter. Consider using `manual` extend to tweak prompts mid-extension for continuity.

### Batch size and cost control

Midjourney generates multiple variants by default (batch size 4). For production or cost-sensitive flows, set `bs:1` to reduce compute. Midjourney’s docs include GPU-time estimates for SD vs HD and different batch sizes (useful for cost forecasting). CometAPI provides competitive pricing.

## Conclusion

Midjourney’s V1 Video model is the first public step into programmatic video — it’s conservative by design but promising. We expect iterative model updates improving longer sequences, higher fidelity, and more controllable camera rigs. CometAPI’s role as an aggregator lowers the integration barrier for developers who want to add Midjourney video into apps without dealing with multiple provider-specific authentication and concurrency idiosyncrasies.

Developers can access [MIdjourney Video API](https://www.cometapi.com/midjourney-video-api/) through CometAPI. To begin, explore the model capabilities of [CometAPI](https://www.cometapi.com/) in the [Playground](https://www.cometapi.com/console/playground) and consult the API guide for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. CometAPI offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Free trial of Midjourney](https://www.cometapi.com/console/login)!

---

*Originally published at [https://www.cometapi.com/how-to-create-a-video-in-midjourney-api/](https://www.cometapi.com/how-to-create-a-video-in-midjourney-api/).*
