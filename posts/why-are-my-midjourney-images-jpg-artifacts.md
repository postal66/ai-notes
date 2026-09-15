<!-- social-ops-fingerprint:b97927548bf4d01b1a17c006c1916246f7576e0bdf67a46bb52fef16628e5eed -->
---
title: Why Are My Midjourney Images jpg Artifacts
---
# Why Are My Midjourney Images jpg Artifacts

![Why Are My Midjourney Images jpg Artifacts](https://resource.cometapi.com/blog/uploads/2025/04/Midjourney-Releases-V7-Credit-Midjourney.webp)

In recent weeks, two major developments have thrust Midjourney back into the spotlight: the long‑awaited alpha release of the V7 model and a high‑profile copyright lawsuit filed by Disney and Universal. While V7 promises dramatic improvements in image quality, many users continue to encounter unexpected JPEG “blockiness” or “ringing” artifacts when saving and sharing their creations. This article explores the root causes of these artifacts, explains how JPEG compression works, and offers practical strategies for minimizing unwanted distortions in your Midjourney‑generated images.

## What is Midjourney V7?

Midjourney V7 represents the first ground‑up model redesign in over a year, introducing faster throughput, smarter prompt interpretation, and enhanced visual fidelity.

### Key Improvements in V7

- **Enhanced Detail and Coherence**: According to Midjourney’s release notes, V7 delivers significantly higher texture resolution and more consistent rendering of complex elements—hands, fabric folds, and natural landscapes all exhibit smoother gradients and finer details compared to V6.1 .
- **Personalization by Default**: V7 is the first Midjourney model with default model “personalization,” requiring users to rate roughly 200 sample images to unlock a fully personalized experience. This feedback loop helps the system better align outputs with individual aesthetic preferences .

### Alpha Release and Community Access

Midjourney opened V7 for alpha testing in early April 2025. Community members can access the new model by appending the `--v 7` flag to their prompts or through the dedicated V7 channel. This alpha release allows broader testing of the model’s core improvements—prompt understanding, image quality, and coherence—before a full public rollout.

## Why am I seeing JPEG artifacts in my Midjourney images?

Despite V7’s internal PNG‑based rendering, many users still report JPEG‑style compression artifacts. These visible distortions typically arise during downstream handling—especially on platforms like Discord.

### Internal PNG Generation and External JPEG Conversion

Midjourney itself generates and stores images in lossless PNG format, ensuring that the model’s full detail and subtle gradients are preserved. However, when these files are shared on Discord or downloaded via certain links, they may be converted to lossy formats (JPEG or WebP) for bandwidth efficiency .

### Discord’s Automated Compression

By default, Discord re‑encodes large images to reduce file size, often using JPEG or WebP compression. This automated step introduces block boundary artifacts (“macroblocking”) and slight color shifts, which can be especially noticeable in smooth gradients or uniform background areas.

### Workflow‑Induced Recompression

Although Midjourney generates and stores images internally as lossless PNGs or even higher‑precision representations, the moment you choose “Save as JPEG” or share via platforms that auto‑convert to JPEG (e.g., some web galleries, social media), the artifacts appear. Discord’s image proxy, browsers saving previews as WebP, and conversion via right‑click “Save image as…” all trigger recompression. Each recompression step accumulates generation loss: cropping, resizing, or re-encoding at default quality settings (often around 75–85%) amplifies blocking and banding.

## How does JPEG compression produce artifacts?

Understanding the technical underpinnings of JPEG encoding illuminates why artifacts appear and how to combat them.

### Block‑Based DCT and Quantization

JPEG compression works by dividing an image into 8×8 pixel blocks and applying a discrete cosine transform (DCT) to each block. To reduce file size, it quantizes high-frequency components—effectively discarding fine detail. When the quantization level is too high (i.e., stronger compression), this process leads to visible block boundaries, loss of texture, and color banding. AI-generated images, especially those with complex gradients and fine textures, are highly susceptible to these artifacts if saved or transmitted as JPEGs without sufficient quality settings.

### Common Artifact Types

- **Blocking (Macroblocking)**: When entire 8×8 blocks become visibly distinct, creating a “checkerboard” pattern.
- **Ringing/Contour Effects**: Halo‑like distortions along sharp edges, arising from high‑frequency component loss.
- **Color Banding**: Smooth gradients degrade into discrete “bands” of color when subtle differences are eliminated.

## What file formats does Midjourney support, and how have they changed recently?

### Which formats are native to Midjourney?

By default, Midjourney delivers high‑resolution PNG files—lossless, 8‑bit per channel (24‑bit RGB) images that preserve every pixel value. When you upscale or use “Light Upscale” modes, you still receive PNGs via the web gallery download button . However, preview thumbnails shown directly in Discord are served as WebP (a modern lossy/optional lossless format) to speed loading. Depending on your browser or Discord client, right‑click downloads may grab the WebP thumbnail rather than the full PNG.

### Why have some users suddenly encountered JPEG outputs?

A few factors drive involuntary JPEG conversion:

1. **Third‑party pipelines:** If you route Midjourney images through bots or automation tools that default to saving as JPG for smaller payloads, you inherit artifacts.
2. **Batch processing scripts:** Some community upscalers (e.g., Automatic1111 for Stable Diffusion) save outputs in the same format as the input—turning final PNGs back into JPGs if chained after a JPG .
3. **Platform defaults:** Social media platforms like Instagram or Twitter auto‑compress user‑uploads to JPEG‑based formats, further degrading the image.

## How can you minimize JPEG artifacts in your images?

While you cannot change Discord’s default compression policy, you can optimize your workflow to preserve image fidelity.

### Use Lossless Formats and Higher‑Bitrate Exports

- **Direct PNG Downloads**: Always download the PNG version of your image from the Midjourney web app rather than relying on Discord previews. PNG avoids the quantization pitfalls of JPEG.
- **Specify Higher Quality**: If you must use JPEG (for web delivery, etc.), export at a quality setting of 90–100% to retain more DCT coefficients and reduce visible block boundaries.

### Adjust Your Workflow to Avoid Recompression

- **Bypass Discord’s Preview Layer**: In Discord, replace links from `media.discordapp.net` with `cdn.discordapp.com` to access original uploads without preview compression.
- **Maintain Single‑Step Compression**: Open your original PNG just once in your editor; if a JPEG is needed, export directly without additional edits or re‑saves.

### Leverage AI‑Powered Artifact Removal

Recent research has produced diffusion‑based models that can selectively remove JPEG artifacts while maintaining detail. For instance, the CODiff model employs a compression‑aware visual embedder (CaVE) to guide a one‑step diffusion denoiser, achieving state‑of‑the‑art artifact reduction with minimal overhead .

## Use MidJourney in CometAPI

CometAPI provides access to over 500 AI models, including open-source and specialized multimodal models for chat, images, code, and more. Its primary strength lies in simplifying the traditionally complex process of AI integration.

[CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate [Midjourney API](https://www.cometapi.com/midjourney-api/), and you can try it for free in your account after registering and logging in! Welcome to register and experience CometAPI.CometAPI pays as you go.

**Important Prerequisite:** Before using MidJourney V7, you need to Start building on [CometAPI today – sign up](https://www.cometapi.com/console/login) here for free access. Please visit [docs](https://apidoc.cometapi.com/).

Getting started with MidJourney V7 is very simple—just add the `--v 7` parameter at the end of your prompt. This simple command tells CometAPI to use the latest V7 model to generate your image.

Please refer to [Midjourney API](https://www.cometapi.com/midjourney-api/) for integration details.

---

## Conclusion

By understanding where—and why—JPEG artifacts enter your Midjourney workflow, you can take concrete steps to preserve the model’s full creative potential. Whether through strategic use of PNG, streamlined export practices, or cutting-edge artifact removal tools, it’s possible to showcase V7’s remarkable fidelity without the unwanted side‑effects of lossy compression.

---

*Originally published at [https://www.cometapi.com/why-are-my-midjourney-images-jpg-artifacts/](https://www.cometapi.com/why-are-my-midjourney-images-jpg-artifacts/).*
