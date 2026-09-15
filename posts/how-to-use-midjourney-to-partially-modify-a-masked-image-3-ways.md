<!-- social-ops-fingerprint:655cfa3f028fccd4b2451d28a982bfa08baaec10e13575a75fb3d1e15946f449 -->
---
title: How to Use Midjourney to Partially Modify a Masked Image? 3 Ways!
---
# How to Use Midjourney to Partially Modify a Masked Image? 3 Ways!

![How to Use Midjourney to Partially Modify a Masked Image? 3 Ways!](https://resource.cometapi.com/blog/uploads/2025/07/How-to-use-Midjourney-to-Partially-Modify-a-Masked-Image-3-Ways.webp)

Midjourney’s powerful editing capabilities have grown significantly in recent months, offering creators unprecedented control over every aspect of their images. One particularly versatile workflow involves uploading a custom mask image to guide partial modifications—allowing you to change specific areas of a picture while leaving the rest untouched. In this article, we’ll explore the end‑to‑end process of preparing, uploading, and leveraging mask images for partial editing in Midjourney, both via the web‑based Editor , within Discord and Midjourney API. Along the way, we’ll highlight the latest features and best practices to ensure your masking workflow is as smooth and precise as possible.

## What tools does Midjourney offer for mask‑guided editing?

Midjourney provides two primary interfaces for image editing: the web‑based **Editor** on midjourney.com and the **Vary Region** tool in Discord. Both can be used to achieve mask‑guided, partial modifications—but they differ in workflow and capabilities.

### What is the web‑based Editor?

The Midjourney **Editor** is a dedicated web interface designed for fine‑tuned adjustments of both Midjourney‑generated images and your own uploads. Key editing tools include:

- **Erase/Restore brushes** to paint areas you want to regenerate or preserve
- **Smart Select** for AI‑assisted masking via positive and negative selection points
- **Layers**, enabling non‑destructive compositing of multiple images
- **Retexture** for full‑image style shifts while preserving structure
- **Pan** and **Zoom** for reframing and scaling the canvas

### What is Vary Region in Discord?

Within Discord, **Vary Region** offers a more streamlined, in‑channel editing experience. After upscaling an image, clicking the “Vary (Region)” button launches a simple mask editor where you can:

- Draw freehand or rectangular masks over the target area
- Optionally revise the prompt (with Remix Mode enabled) to refine generated content
- Submit edits directly back to the Midjourney bot, receiving a new grid with only the selected region altered

## How do you prepare a mask image for partial modification?

Before uploading a mask to Midjourney, you need to craft a suitable mask file—typically a black‑and‑white or transparent PNG that clearly delineates the region to be modified.

### Which image formats and specifications work best?

- **PNG** with alpha transparency is ideal, as it preserves clear edges and mask fidelity.
- Ensure your mask matches the **aspect ratio** and **resolution** of the original image (e.g., 1024×1024, 1536×1024).
- Use pure black (RGB 0, 0, 0) to indicate “areas to keep” and white (RGB 255, 255, 255) for “areas to modify.” Transparent regions can also function as keep‑out zones if the Editor’s upload supports alpha channels.

### What tools can you use to create the mask?

- **Adobe Photoshop / Affinity Photo**: Use selection tools and fill commands to generate a high‑contrast mask layer, then export as PNG.
- **GIMP / Krita**: Free alternatives that offer brush, selection, and layer‑alpha controls.
- **Online editors** (Photopea, Pixlr): Quick, browser‑based solutions for simple masking tasks.

## How can you upload a mask image to Midjourney’s web Editor for partial modification?

The Editor’s **Layers** panel makes it straightforward to bring in an external mask image alongside your original.

### How do you access the full Editor?

1. Navigate to [midjourney.com](https://www.midjourney.com) and log in.
2. Click the **Edit** tab (pencil icon) in the top navigation to open the advanced Editor.
3. In “Using Your Own Images,” choose **Upload from Device** or **Paste URL** to bring in your original image .

### How do you add the mask as a layer?

1. Open the **Layers** panel in the Editor sidebar.
2. Click **Add** and upload your prepared mask PNG.
3. Use the **Move/Resize** tool to perfectly align the mask layer over your original image.
4. Select the mask layer (it will be highlighted with a check mark)—this tells the Editor which layer subsequent tools will affect.

### How do you apply the mask to guide modifications?

1. With the mask layer active, choose the **Erase** brush (or **Smart Select** if you prefer AI‑assisted refinement) to remove masked regions from that layer.
2. Any erased (transparent) areas on the mask layer now define the “hole” through which Midjourney will regenerate content on the base image.
3. Enter your desired prompt into the **Imagine** bar at the bottom—describing what you want to see in the masked zone.
4. Hit **Submit Edit**. Midjourney will produce four variations that replace **only** the masked section, leaving the rest of the image intact.
5. Use **Upscale** or **Download** to export your final result; you can also export a **Transparent PNG** of the masked edits for further compositing .

## How can you use Discord to upload a mask image for partialmodification?

While the Editor excels at layer‑based uploads, you can also leverage Discord for mask‑guided edits via the Vary Region workflow—by hosting both your original and mask images and using Mask + Imagine prompts.

### How do you host images on Discord?

1. In a private DM with the Midjourney bot (or in a private server channel), click the **+** icon or drag‑and‑drop your original image.
2. Press **Enter** to upload; once it appears in chat, right‑click and select **Copy Image Address** (or **Copy Media Link** on mobile) to obtain the URL.
3. Repeat for your mask PNG to get its own URL.

### How do you prompt with a mask URL?

1. Type `/imagine` and paste the **original image URL**, followed by descriptive text and any desired parameters.
2. Append your **mask image URL** in the prompt—ideally immediately after the base image URL, separated by spaces. For example:

```
   /imagine https://cdn.discordapp.com/…/original.png https://cdn.discordapp.com/…/mask.png red roses blooming in the masked area --v 7
```

3. This tells Midjourney to treat the second image as a mask reference, instructing it to generate new content only where the mask is white.
4. Adjust parameters like `--v` (version), `--ar` (aspect ratio), and `--q` (quality) as needed; then send the command.

### How can you refine the masked edit with Vary Region?

Submit and repeat until the masked region matches your vision.

After the initial grid is generated, click **U#** to upscale your preferred variation.

Click **Vary (Region)** and draw additional precise selections over any areas that still need adjustment.

With **Remix Mode** enabled in your Discord settings, you can tweak your prompt in the editor to fine‑tune the look of the regenerated sections.

## How to use Midjourney API to Partially Modify a Masked Image

Midjourney’s API (both the official web editor and third‑party wrappers like CometAPI) exposes an “inpainting” or “vary‑region” endpoint that lets you supply:

1. **An input image**
2. **A binary mask** (white = region to regenerate; black = region to keep)
3. **A text prompt** describing what you want in the masked area

Although Midjourney itself doesn’t expose an official public API, **third-party interfaces** like **CometAPI** provide equivalent capabilities.

**Obtain your CometAPI API key**: Sign up at [CometAPI](https://www.cometapi.com/) and grab your `CometAPI-KEY` from the dashboard.

```
# Example header for PiAPI inpainting

X-API-Key: YOUR_CometAPI_API_KEY
Authorization: Bot YOUR_DISCORD_BOT_TOKEN
```

### Setting request modes

Many services support modes akin to Midjourney’s Discord tiers:

- **fast**: results in ≤ 90 s (simulates official Fast mode)
- **relax**: results in ≤ 10 min (simulates Relax mode)
- **turbo**: results in ≤ 60 s (a paid “turbo” tier)

```
{
  "mode": "fast",
  "prompt": "a serene lakeside at sunset --v 7"
}
```

To partially modify (inpaint) an existing Midjourney image via API, you can use the **CometAPI** ’s Midjourney wrapper, which provides a dedicated `/inpaint` endpoint. Below is a step‑by‑step guide:

### 1. Generate or retrieve your base image

You can either:

Call the **Imagine** endpoint to create a new image from text:

```
POST https://api.cometapi.com/mj/submit/imagineHeaders: CometAPI-API-KEY: your_key
Body (JSON): { "prompt": "a sleek sports car on a mountain road", "mode": "fast" }
```

You’ll get back a `jobId` you can use to fetch the generated image .

Or, if you already have a `jobId` from a previous call (e.g. an upscaled or variation), you can skip straight to step 3.

### 2. Fetch the completed image and download it

```
   POST https://api.cometapi.com/mj/task/{id}/fetch
   Headers:
     TT-API-KEY: your_key
   Body (JSON):
     {
       "jobId": "afa774a3-1aee-5aba-4510-14818d6875e4"
     }
```

The response contains `cdnImage` (URL) or `discordImage` you can download.

### 3. Create your mask

- Make a **black‑and‑white** mask image (same width × height as the original).
- **White (255,255,255)** marks the area to be repainted.
- **Black (0,0,0)** marks pixels to keep unchanged.
- Export this mask as a PNG, then Base64‑encode its raw bytes **without** the `data:image/...` prefix.

```
   # example of reading and encoding a local mask.png

   import base64
   with open("mask.png", "rb") as f:
       mask_b64 = base64.b64encode(f.read()).decode()
```

### 4. Call the edit endpoint

Send your original `jobId`, the Base64 mask, and (optionally) a new prompt for the masked region:

```
   POST https://api.cometapi.com/mj/submit/edits
   Headers:
     CometAPI-API-KEY: your_key
   Body (JSON):
     {
       "jobId": "afa774a3-1aee-5aba-4510-14818d6875e4",
       "mask": "<your_mask_base64_string>",
       "prompt": "replace the car’s wheels with futuristic glowing rims",
       "timeout": 300
     }
```

– `mask`: the base64‑encoded PNG mask (white = repaint)
– `prompt`: text guiding what to generate in that region

### 5. Fetch your inpainted result

Just like before, poll `/fetch` or use your webhook to retrieve the new `jobId` and image URLs once complete.

---

### Example: Python snippet

```
import requests, base64

API_KEY = "YOUR_CometAPI_KEY"
HEADERS = {"CometAPI-KEY": API_KEY}

# 1. Imagine (or skip if you already have jobId)

resp = requests.post(
    "https://api.cometapi.com/mj/submit/imagine",
    headers=HEADERS,
    json={"prompt":"a serene lake at sunset","mode":"fast"}
)
job_id = resp.json()

# ... wait for image to generate, fetch and download it ...

# 2. Prepare mask

with open("mask.png", "rb") as f:
    mask_b64 = base64.b64encode(f.read()).decode()

# 3. Inpaint

inpaint_resp = requests.post(
    "https://api.cometapi.com/mj/submit/edits",
    headers=HEADERS,
    json={
      "jobId": job_id,
      "mask": mask_b64,
      "prompt": "replace the sky with dramatic storm clouds"
    }
)
new_job = inpaint_resp.json()

# 4. Fetch result

fetch_resp = requests.post(
    "https://api.cometapi.com/mj/task/{id}/fetch",
    headers=HEADERS,
    json={"jobId": new_job}
)
print(fetch_resp.json())
```

With this flow you can precisely target and modify any part of an existing Midjourney image by supplying your own mask and guiding text for inpainting.

You can refer to CometAPI’s [API doc](https://apidoc.cometapi.com/api-18989894) to edit.

## Tips & Gotchas

- **Mask precision**: jagged or semi‑transparent mask edges can bleed; stick to pure black/white.
- **Selection size**: too small → model may “hallucinate” inconsistently; too large → you lose context from the rest of the image.
- **Prompts**: keep them short and focused on the masked region. (Midjourney will blend with the surrounding content.)
- **Webhook callbacks**: if you need real‑time updates, supply a `hookUrl` in your `data` and your server will receive JSON when the job finishes .

### How do you optimize prompts for masked edits?

- **Concise yet descriptive**: Focus your prompt on the masked area’s content (“golden mechanical bird perched on a branch,” rather than generic color changes).
- **Contextual cohesion**: Mention lighting, style, or materials that match the unedited portions to maintain a unified look.
- **Use Remix sparingly**: If you only need color or texture tweaks, avoid rewriting the entire prompt in Remix Mode—which can unintentionally alter non‑masked regions.

## Getting Started

CometAPI provides access to over 500 AI models, including open-source and specialized multimodal models for chat, images, code, and more. Its primary strength lies in simplifying the traditionally complex process of AI integration.

[CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate [Midjourney API](https://www.cometapi.com/midjourney-api/), and you can try out in your account after registering and logging in! Welcome to register and experience CometAPI.CometAPI pays as you go.

**Important Prerequisite:** Before using MidJourney V7, you need to Start building on [CometAPI today – sign up](https://www.cometapi.com/console/login) here for free access. Please visit [docs](https://apidoc.cometapi.com/). Getting started with MidJourney V7 is very simple—just add the `--v 7` parameter at the end of your prompt. This simple command tells CometAPI to use the latest V7 model to generate your image.

## Conclusion

Mask‑guided, partial modification in Midjourney unlocks a new dimension of creative control—whether you’re replacing an object in a photo, adding fantastical elements to a painting, or fine‑tuning details in a composite. By mastering the workflow of preparing a precise mask, uploading it as a layer in the web Editor or hosting it in Discord, and leveraging Midjourney’s inpainting and layering tools, you can achieve professional‑grade results with surgical precision. Embrace the latest Editor enhancements—layers, smart selection, and a refreshed UI—and integrate these best practices into your creative process to push the boundaries of what’s possible in AI‑driven art.

---

*Originally published at [https://www.cometapi.com/how-to-use-midjourney-to-modify-a-masked-image/](https://www.cometapi.com/how-to-use-midjourney-to-modify-a-masked-image/).*
