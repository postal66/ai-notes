<!-- social-ops-fingerprint:bbe819243aa09340bd650b07313c5b4008edd024fa77fe6467f35d7022c3e40a -->
---
title: How to Add AI Video Generation to a SaaS App
---
# How to Add AI Video Generation to a SaaS App

![How to Add AI Video Generation to a SaaS App](https://resource.cometapi.com/image-1780677443741.jpeg)

Adding video generation to your app is not the same as adding image generation. The API call returns immediately — but the video isn't ready yet. You get a task ID, and you have to keep asking "is it done?" until it is.

Most developers hit this the first time they call a video API, wait for a response body with a video URL, and get back a task ID instead. This guide walks through the full flow: submitting a task, polling for results, handling failures, and storing the output before the URL expires.

## What you'll build

A backend service that accepts a text prompt or image, submits a video generation task, polls until it's complete, and returns the final video URL. You'll work with four models — Veo 3 Fast, Sora 2, Kling Video, and Runway — all through a single API key.

### **Prerequisites:**

- Python 3.8+ or Node.js 18+
- A [CometAPI](https://www.cometapi.com/) key
- Basic familiarity with REST APIs

## Understand why video generation is different

With image generation, you send a request and get the image back in the same response. Video generation uses an async task queue:

1. **Submit** a generation request → get back a `task_id`
2. **Poll** a status endpoint every few seconds
3. When status reaches a terminal state, you get the video URL
4. **Download and store** the video — the URL is temporary

If you treat video generation like image generation and wait for the first response to contain your video, your request will time out every time.

In a production web service, this polling loop should run in a background worker (Celery, Bull, or similar), not in your request handler. The examples below use synchronous polling — fine for scripts and prototypes, but not for handling concurrent users.

## Choose a model

| Model | Provider | Max duration | Price (via CometAPI) | Best for |
| --- | --- | --- | --- | --- |
| Veo 3 Fast | Google | 8 sec | $0.05/sec | Fast prototyping, social clips |
| Sora 2 | OpenAI (via CometAPI model ID) | ~10 sec | $0.08/sec | High-quality creative shorts |
| Kling Video | Kuaishou | 10 sec | $0.13–$2.64/task | Marketing content, granular control |
| Runway Gen-3A Turbo | Runway | 5 or 10 sec | $0.32/task | Image-to-video, commercial content |

*Source\*\*: CometAPI model pages, May 2026. Note: "Sora 2" is CometAPI's model* *identifier* *— refer to their* [*model page*](https://www.cometapi.com/models/openai/sora-2/) *for the underlying model details.*

- **Veo 3 Fast** supports both text-to-video and image-to-video. Cheapest per second, good starting point.
- **Sora 2** generates audio natively alongside the video — dialogue, ambient sound, and effects without a separate TTS step.
- **Kling Video** gives you `negative_prompt`, `cfg_scale`, camera movement settings, and a `pro` mode. Most control of the four.
- **Runway** is image-to-video only via CometAPI. Give it a static image and a motion description, and it animates it.

## Submit a Veo task

Veo uses `multipart/form-data`. Use `files=` in Python requests to send it correctly — `data=dict` sends `application/x-www-form-urlencoded`, which is not the same thing:

```
import requestsimport osfrom dotenv import load_dotenv​load_dotenv()​def submit_veo_task(prompt: str, size: str = "16x9") -> str:    """Submit a Veo 3 Fast text-to-video task. Returns task_id."""    api_key = os.getenv("COMETAPI_KEY")    if not api_key:        raise ValueError("COMETAPI_KEY environment variable is not set")​    response = requests.post(        "https://api.cometapi.com/v1/videos",        headers={"Authorization": f"Bearer {api_key}"},        files={            "prompt": (None, prompt),            "model": (None, "veo3-fast"),            "size": (None, size)        },        timeout=30    )    response.raise_for_status()    return response.json()["id"]​​task_id = submit_veo_task("A paper kite drifting above a wheat field on a windy afternoon")print(f"Task submitted: {task_id}")
```

## Poll for the result

```
import time​def poll_veo_task(task_id: str, interval: int = 10, max_wait: int = 600) -> str:    """Poll until Veo task completes. Returns video URL."""    api_key = os.getenv("COMETAPI_KEY")    if not api_key:        raise ValueError("COMETAPI_KEY environment variable is not set")​    headers = {"Authorization": f"Bearer {api_key}"}    url = f"https://api.cometapi.com/v1/videos/{task_id}"    elapsed = 0​    while elapsed < max_wait:        response = requests.get(url, headers=headers, timeout=30)        response.raise_for_status()        result = response.json()        status = result.get("status")​        if status == "succeeded":            return result["output"][0]        elif status in ("failed", "cancelled"):            raise RuntimeError(                f"Task {task_id} failed with status '{status}': "                f"{result.get('error', 'no error detail returned')}"            )​        time.sleep(interval)        elapsed += interval​    raise TimeoutError(f"Task {task_id} did not complete within {max_wait} seconds")​​video_url = poll_veo_task(task_id)print(f"Video ready: {video_url}")
```

## Use Kling Video for more control

Kling has a different endpoint structure and uses JSON. Note that Kling's terminal status string is `"succeed"` (not `"succeeded"`) — this matches the API's actual response format:

```
def submit_kling_task(prompt: str, duration: str = "5", mode: str = "std") -> str:    """Submit a Kling text-to-video task. Returns task_id."""    api_key = os.getenv("COMETAPI_KEY")    if not api_key:        raise ValueError("COMETAPI_KEY environment variable is not set")​    response = requests.post(        "https://api.cometapi.com/kling/v1/videos/text2video",        headers={            "Authorization": f"Bearer {api_key}",            "Content-Type": "application/json"        },        json={            "model_name": "kling-v1-6",            "prompt": prompt,            "negative_prompt": "blurry, low quality, watermark",            "cfg_scale": 0.5,            "mode": mode,         # "std" or "pro"            "aspect_ratio": "16:9",            "duration": duration  # "5" or "10"        },        timeout=30    )    response.raise_for_status()    return response.json()["data"]["task_id"]​​def poll_kling_task(task_id: str, interval: int = 10, max_wait: int = 600) -> str:    """Poll Kling task until complete. Returns video URL."""    api_key = os.getenv("COMETAPI_KEY")    if not api_key:        raise ValueError("COMETAPI_KEY environment variable is not set")​    headers = {"Authorization": f"Bearer {api_key}"}    url = f"https://api.cometapi.com/kling/v1/videos/text2video/{task_id}"    elapsed = 0​    while elapsed < max_wait:        response = requests.get(url, headers=headers, timeout=30)        response.raise_for_status()        result = response.json()        status = result["data"]["task_status"]​        if status == "succeed":  # Kling uses "succeed", not "succeeded"            return result["data"]["task_result"]["videos"][0]["url"]        elif status == "failed":            error_detail = result.get("data", {}).get("task_result", "no detail")            raise RuntimeError(                f"Kling task {task_id} failed: {error_detail}"            )​        time.sleep(interval)        elapsed += interval​    raise TimeoutError(f"Kling task {task_id} timed out after {max_wait}s")
```

*Source\*\*:* [*CometAPI Kling Video docs*](https://apidoc.cometapi.com/video-generation/kling-video)

## Animate a static image with Runway

Runway is image-to-video only. It also requires an extra header (X-Runway-Version):

```
def submit_runway_task(image_url: str, motion_prompt: str, duration: int = 5) -> str:    """Submit a Runway image-to-video task. Returns task_id."""    api_key = os.getenv("COMETAPI_KEY")    if not api_key:        raise ValueError("COMETAPI_KEY environment variable is not set")​    response = requests.post(        "https://api.cometapi.com/runwayml/v1/image_to_video",        headers={            "Authorization": f"Bearer {api_key}",            "X-Runway-Version": "2024-11-06",            "Content-Type": "application/json"        },        json={            "model": "gen3a_turbo",            "promptImage": image_url,  # must be a stable HTTPS URL            "promptText": motion_prompt,            "duration": duration,            "ratio": "1280:720",            "watermark": False        },        timeout=30    )    response.raise_for_status()    return response.json()["id"]​​def poll_runway_task(task_id: str, interval: int = 5, max_wait: int = 600) -> str:    """Poll Runway task. Returns video URL when done."""    api_key = os.getenv("COMETAPI_KEY")    if not api_key:        raise ValueError("COMETAPI_KEY environment variable is not set")​    headers = {        "Authorization": f"Bearer {api_key}",        "X-Runway-Version": "2024-11-06"    }    url = f"https://api.cometapi.com/runwayml/v1/tasks/{task_id}"    elapsed = 0​    while elapsed < max_wait:        response = requests.get(url, headers=headers, timeout=30)        response.raise_for_status()        result = response.json()        status = result.get("status")​        if status == "task_not_exist":            # CometAPI-specific: task is still initializing, retry after a few seconds            time.sleep(interval)            elapsed += interval            continue        elif status == "succeeded":            return result["output"][0]        elif status in ("failed", "cancelled"):            raise RuntimeError(f"Runway task {task_id} failed: {result.get('error', 'no detail')}")​        time.sleep(interval)        elapsed += interval​    raise TimeoutError(f"Runway task {task_id} timed out after {max_wait}s")
```

*Source\*\*:* [*CometAPI Runway docs*](https://apidoc.cometapi.com/api/video/runway)

## Save the video before the URL expires

Video URLs from generation APIs are temporary. Download the file immediately and store it somewhere you control:

```
import requestsimport pathlib​def download_video(url: str, output_path: str) -> None:    """Download video from URL to local file using streaming."""    out = pathlib.Path(output_path)    if out.parent != pathlib.Path("."):        out.parent.mkdir(parents=True, exist_ok=True)​    with requests.get(url, stream=True, timeout=60) as r:        r.raise_for_status()        with open(out, "wb") as f:            for chunk in r.iter_content(chunk_size=8192):                f.write(chunk)    print(f"Saved to {output_path}")​​# Full flowtask_id = submit_veo_task("A timelapse of clouds moving over a city skyline")video_url = poll_veo_task(task_id)download_video(video_url, "output/city_timelapse.mp4")
```

In production, swap the local file write for an upload to S3, Cloudflare R2, or your storage of choice. The streaming pattern stays the same — pipe the bytes directly rather than loading the whole video into memory.

## Handle failures

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Task stuck in queued for 10+ min | Server load or model unavailable | Retry with a different model |
| task\_not\_exist on first Runway poll | Task still initializing | Wait 5 sec and retry — documented CometAPI behavior |
| failed with no error message | Prompt triggered content filter | Rephrase the prompt |
| Video URL returns 403 | URL expired before download | Download immediately after getting the URL |
| Timeout after 10 min | Generation took too long | Increase max\_wait or switch to Veo 3 Fast |
| Kling returns "succeed" not "succeeded" | Kling's API uses non-standard status string | This is correct — see Kling polling code above |

*Source:* [*CometAPI video generation docs*](https://apidoc.cometapi.com/api/video/veo3)

## Node.js version

Node.js 18+ includes `fetch` and `FormData` natively. This example covers all four models:

```
// Node.js 18+ — no extra packages needed​const API_KEY = process.env.COMETAPI_KEY;if (!API_KEY) throw new Error('COMETAPI_KEY is not set');​// --- Veo 3 Fast ---async function submitVeoTask(prompt, size = '16x9') {  const form = new FormData();  form.append('prompt', prompt);  form.append('model', 'veo3-fast');  form.append('size', size);​  const res = await fetch('https://api.cometapi.com/v1/videos', {    method: 'POST',    headers: { 'Authorization': `Bearer ${API_KEY}` },    body: form  });  if (!res.ok) throw new Error(`Veo submit failed: ${res.status}`);  return (await res.json()).id;}​async function pollVeoTask(taskId, intervalMs = 10000, maxWaitMs = 600000) {  let elapsed = 0;  while (elapsed < maxWaitMs) {    const res = await fetch(`https://api.cometapi.com/v1/videos/${taskId}`, {      headers: { 'Authorization': `Bearer ${API_KEY}` }    });    if (!res.ok) throw new Error(`Poll failed: ${res.status}`);    const result = await res.json();​    if (result.status === 'succeeded') return result.output[0];    if (['failed', 'cancelled'].includes(result.status)) {      throw new Error(`Task ${taskId} failed: ${result.error ?? 'no detail'}`);    }    await new Promise(r => setTimeout(r, intervalMs));    elapsed += intervalMs;  }  throw new Error(`Task ${taskId} timed out`);}​// --- Kling Video ---async function submitKlingTask(prompt, duration = '5', mode = 'std') {  const res = await fetch('https://api.cometapi.com/kling/v1/videos/text2video', {    method: 'POST',    headers: {      'Authorization': `Bearer ${API_KEY}`,      'Content-Type': 'application/json'    },    body: JSON.stringify({      model_name: 'kling-v1-6',      prompt,      negative_prompt: 'blurry, low quality, watermark',      cfg_scale: 0.5,      mode,      aspect_ratio: '16:9',      duration    })  });  if (!res.ok) throw new Error(`Kling submit failed: ${res.status}`);  return (await res.json()).data.task_id;}​async function pollKlingTask(taskId, intervalMs = 10000, maxWaitMs = 600000) {  let elapsed = 0;  while (elapsed < maxWaitMs) {    const res = await fetch(      `https://api.cometapi.com/kling/v1/videos/text2video/${taskId}`,      { headers: { 'Authorization': `Bearer ${API_KEY}` } }    );    if (!res.ok) throw new Error(`Kling poll failed: ${res.status}`);    const result = await res.json();    const status = result.data.task_status;​    if (status === 'succeed') return result.data.task_result.videos[0].url;    if (status === 'failed') {      throw new Error(`Kling task ${taskId} failed: ${JSON.stringify(result.data.task_result ?? 'no detail')}`);    }    await new Promise(r => setTimeout(r, intervalMs));    elapsed += intervalMs;  }  throw new Error(`Kling task ${taskId} timed out`);}​// --- Runway (image-to-video) ---async function submitRunwayTask(imageUrl, motionPrompt, duration = 5) {  const res = await fetch('https://api.cometapi.com/runwayml/v1/image_to_video', {    method: 'POST',    headers: {      'Authorization': `Bearer ${API_KEY}`,      'X-Runway-Version': '2024-11-06',      'Content-Type': 'application/json'    },    body: JSON.stringify({      model: 'gen3a_turbo',      promptImage: imageUrl,      promptText: motionPrompt,      duration,      ratio: '1280:720',      watermark: false    })  });  if (!res.ok) throw new Error(`Runway submit failed: ${res.status}`);  return (await res.json()).id;}​async function pollRunwayTask(taskId, intervalMs = 5000, maxWaitMs = 600000) {  let elapsed = 0;  while (elapsed < maxWaitMs) {    const res = await fetch(      `https://api.cometapi.com/runwayml/v1/tasks/${taskId}`,      { headers: { 'Authorization': `Bearer ${API_KEY}`, 'X-Runway-Version': '2024-11-06' } }    );    if (!res.ok) throw new Error(`Runway poll failed: ${res.status}`);    const result = await res.json();    const status = result.status;​    if (status === 'task_not_exist') {      // CometAPI-specific: task still initializing      await new Promise(r => setTimeout(r, intervalMs));      elapsed += intervalMs;      continue;    }    if (status === 'succeeded') return result.output[0];    if (['failed', 'cancelled'].includes(status)) {      throw new Error(`Runway task ${taskId} failed: ${result.error ?? 'no detail'}`);    }    await new Promise(r => setTimeout(r, intervalMs));    elapsed += intervalMs;  }  throw new Error(`Runway task ${taskId} timed out`);}​// Usage exampleconst taskId = await submitVeoTask('A paper kite drifting above a wheat field');const videoUrl = await pollVeoTask(taskId);console.log('Video ready:', videoUrl);
```

## What's next

You now have working code for four video models, a polling loop that handles failures, and a download step that keeps you from losing generated content.

The next problem most developers hit: they've hardcoded one model, and switching to a cheaper or faster option means touching multiple files. The next article covers how to route requests across models without rewriting your code.

Next: **How to Switch Between AI Models Without Rewriting Your Code**

## FAQ

### **Q: Why do I get a task ID instead of a video in the API response?**

Video generation is async — models like Veo, Sora, Kling, and Runway take 2–5 minutes to render. The API returns a task ID immediately so your request doesn't time out. You poll a separate status endpoint until the task reaches a terminal state (`succeeded`, `succeed`, `failed`).

### **Q: How long does a generated video URL stay valid?**

Video URLs from generation APIs are temporary. Download the file immediately after getting the URL and store it in your own storage (S3, Cloudflare R2, etc.). Don't store the URL and expect it to work hours later.

### **Q: What's the difference between Veo 3 Fast and Kling Video?**

Veo 3 Fast is cheaper ($0.05/sec), faster, and simpler to call. Kling Video gives you more control: `negative_prompt`, `cfg_scale`, camera movement settings, and a `pro` quality mode. If you need to fine-tune the output, use Kling. If you need speed and low cost, use Veo 3 Fast.

### **Q: Can I generate video from an image instead of a text prompt?**

Yes. Veo supports image-to-video by passing an `input_reference` file. Kling supports it via the `/kling/v1/videos/image2video` endpoint with an `image` parameter (URL or base64). Runway is image-to-video only — it doesn't accept text-only prompts via CometAPI.

### **Q: Why does Runway return** **`task_not_exist`** **on the first poll?**

This is documented CometAPI behavior — the task is still initializing on the backend. Wait a few seconds and retry. It's not an error. The polling code above handles this automatically.

### **Q: Why does Kling use** **`"succeed"`** **instead of** **`"succeeded"`**?

That's Kling's actual API response format. It's not a typo. Veo and Runway use `"succeeded"` — Kling uses `"succeed"`. If you're building a unified polling wrapper, you'll need to handle both strings.

### **Q: Is the synchronous polling loop safe to use in a web server?**

No. The polling loop in this guide blocks the thread for minutes at a time. In a real web service with concurrent users, run the polling in a background worker (Celery for Python, Bull for Node.js). Submit the task in the request handler, return the task ID to the client, and let the worker notify the client when the video is ready.

---

*Originally published at [https://www.cometapi.com/how-to-add-ai-video-generation-to-a-saas-app/](https://www.cometapi.com/how-to-add-ai-video-generation-to-a-saas-app/).*
