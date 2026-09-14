<!-- social-ops-fingerprint:22ad707f022daeee1cffae8eee7a894f6671d2cf773e6367444506e4671727cb -->
---
title: Ultimate Guide to Nano-Banana: How to Use and Prompt for best
---
# Ultimate Guide to Nano-Banana: How to Use and Prompt for best

![Ultimate Guide to Nano-Banana: How to Use and Prompt for best](https://resource.cometapi.com/blog/uploads/2025/09/Nano-Banana.webp)

Google’s recent release of **Gemini 2.5 Flash Image — nicknamed “Nano-Banana”** has quickly become the go-to for conversational image editing: it keeps likenesses consistent across edits, fuses multiple images cleanly, and supports very natural prompt-based local edits. Below I’ll walk through what Nano Banana is, how to use it both via **Google’s Gemini** and via **third-party access (e.g., CometAPI)**, give concrete prompt examples and code you can drop into a project, and share developer tips for multi-turn editing, upscaling, and advanced prompts. I’m writing this as a developer who uses image models daily — consider this a practical, slightly opinionated playbook.

## What is Nano-Banana?

### What does “Gemini 2.5 Flash Image / Nano-Banana” actually mean?

**Nano-Banana** is the community nickname / codename for **Gemini 2.5 Flash Image**, Google DeepMind’s latest image generation & editing model. It’s designed for *prompt-first* editing (you give it natural language instructions) with special focus on **character consistency** (keeping the same person/pet/object looking right across edits), **multi-image fusion** (blending objects across source photos), and low-latency interactive use in apps like Gemini and Google AI Studio.The model is available through Google’s Gemini API, AI Studio, and is already being surfaced in CometAPI.

As a developer, think of Nano-Banana not primarily as a pure “from-scratch” image generator, but as a highly capable **photo-editing and composition assistant**: it understands the content of your image, remembers the subject across edits, and responds to natural language instructions in a way that fits a quick iterative design loop. That makes it particularly useful for product mockups, consistent character shots, fast concept iterations, and social creative play.

### developer-facing summary

- **Model name:** gemini-2.5-flash-image-preview / gemini-2.5-flash-image.
- **Consistency & continuity:** Nano-Banana holds onto character details across edits more reliably than many rivals, making it preferable for sequential edits and storytelling.
- **Speed:** Users report rapid generation—often under 10 seconds for many edits—helpful for iterative workflows.
- **Editing-first design:** While many models are optimized for pure text-driven generation, Nano-Banana’s UX and APIs emphasize editing (one-shot edits, multi-image fusion, style transfer).

## How can I edit with Nano-Banana on CometAPI?

CometAPI is an API marketplace/wrapper that aggregates many models (including [Gemini 2.5 Flash Image API(Nano Banana)](https://www.cometapi.com/gemini-2-5-flash-image/)) behind a single, OpenAI-compatible endpoint. If you want to prototype quickly or avoid provisioning Google Cloud/Vertex accounts for a first test, CometAPI is a practical bridge — you get an API key, choose `gemini-2.5-flash-image` (or `gemini-2.5-flash-image-preview` ), then send requests much like a Chat-style image edit. CometAPI also offers examples and [guide](https://apidoc.cometapi.com/guide-to-calling-gemini-2-5-flash-image-1425263m0) to try the model.

### Why use CometAPI?

- One API key to rule them all — simplifies testing multiple providers.
- Swap providers in production if pricing or SLAs change.
- Useful for teams that want service-level control (rate limiting, centralized logging).

### How to call Nano-Banana (CometAPI) — practical example

Below is straightforward example. Replace `YOUR_COMET_KEY` and file paths with your own.

**CURL — basic edit (image + prompt → edited image)**

**Example:**

```
curl --location --request POST 'https://api.cometapi.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent' \
--header 'Authorization: sk-xxx' \
--header 'User-Agent: Apidog/1.0.0 (https://apidog.com)' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--header 'Host: api.cometapi.com' \
--header 'Connection: keep-alive' \
--data-raw '{
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": "cat"
                },
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
						"data": "iVBORw0KGgoA Note: Base64 data here"
						}

            ]
        }
    ],
    "generationConfig": {
        "responseModalities": [
            "TEXT",
            "IMAGE"
        ]
    }
}'
```

\*\*Description:\*\*First, convert your source image file into a Base64 string and place it in `inline_data.data`. Second, Do not include prefixes like `data:image/jpeg;base64,` . The output is also located in `candidates.content.parts` and includes:

- An optional text part (description or prompt).
- The image part as `inline_data` (where `data` is the Base64 of the output image).

If you just want to try out image editing on the Nano-Banana, CometAPI offers free credits to new users. You can try the Nano-Banana in the playground or use the Gemini 2.5 Flash Image API. However, if you want unlimited use, you can pay 20% off the Gemini price.

**Nano-Banana has several core advantages: consistent likeness, targeted local edits via natural language, and multi-image fusion.**

Next, I will show the advantages of Nano-Banana through several use cases, and you will see its magic.

## Example 1: Combine multiple images into a single collage

**Upload an image：**

![Ultimate Guide to Nano-Banana: How to Use and Prompt for best](https://resource.cometapi.com/blog/uploads/2025/09/d36e91bb-9867-497a-a521-cb4ebf53f909-1024x643.webp)

**Example input description:** A model is posing and leaning against a pink bmw. She is wearing the following items, the scene is against a light grey background. The green alien is a keychain and it’s attached to the pink handbag. The model also has a pink parrot on her shoulder. There is a pug sitting next to her wearing a pink collar and gold headphones.

**Returned Base64 converted back to an image:**

![Ultimate Guide to Nano-Banana: How to Use and Prompt for best](https://resource.cometapi.com/blog/uploads/2025/09/cce6e077-7026-43f6-b742-08dda5c11633-1024x625.webp)

Code:

```
curl --location --request POST 'https://api.cometapi.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent' \
--header 'Authorization: sk-xxx' \
--header 'User-Agent: Apidog/1.0.0 (https://apidog.com)' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--header 'Host: api.cometapi.com' \
--header 'Connection: keep-alive' \
--data-raw '{
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": "A model is posing and leaning against a pink bmw. She is wearing the following items, the scene is against a light grey background. The green alien is a keychain and it's attached to the pink handbag. The model also has a pink parrot on her shoulder. There is a pug sitting next to her wearing a pink collar and gold headphones"
                },
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
						"data": "iVBORw0KGgoA Note: Base64 data here"
						}

            ]
        }
    ],
    "generationConfig": {
        "responseModalities": [
            "TEXT",
            "IMAGE"
        ]
    }
}'
```

Notes: convert your source image file to a Base64 string and insert it into `inline_data.data` (do not include prefixes like `data:image/jpeg;base64,`).

**Use case analysis:** By using multi-image fusion, designers can be more creative. For example, home designers can combine images to create a rough rendering of the effect. Consumers can combine their full-body images with the things they want to buy to help them decide whether to buy. This can also be used as a reference for animation and comic production.

## Example 2: Edit images to preserve similarity

Below I will provide several rounds of editing to test nano banana.

**First,upload a image:**

![Ultimate Guide to Nano-Banana: How to Use and Prompt for best](https://resource.cometapi.com/blog/uploads/2025/09/74d4c183389356c4f99003ab59321edf_t.webp)

Second, **Prompt:** Add a puppy to the lawn

**Output :**

![Ultimate Guide to Nano-Banana: How to Use and Prompt for best](https://resource.cometapi.com/blog/uploads/2025/09/Generated-Image-September-09-2025-6_07PM.webp)

Finally, **Prompt:** Use the attached reference image of the character. Preserve the dog. Place the character in a rainy neon-city street scene at night. Keep facial features identical to the reference.

![Ultimate Guide to Nano-Banana: How to Use and Prompt for best](https://resource.cometapi.com/blog/uploads/2025/09/Generated-Image-September-09-2025-6_12PM-1024x535.webp)

**Use case analysis:** It can be seen that a fairly high consistency is maintained in multiple rounds of image modification.

## Example 3: Style transfer and modifying facial details

**Upload a image:**

![Ultimate Guide to Nano-Banana: How to Use and Prompt for best](https://resource.cometapi.com/blog/uploads/2025/09/Generated-Image-September-09-2025-6_31PM-1.png)

**Prompt:** Sharpen face slightly, add 6% film grain, crop to 16:9. Do not change facial features,Add gentle rim light on the right side.

**output:**

![Ultimate Guide to Nano-Banana: How to Use and Prompt for best](https://resource.cometapi.com/blog/uploads/2025/09/Generated-Image-September-09-2025-6_36PM.png)

## Other use cases of Nano-Banana

### 1) Corporate headshots & professional portraits

Use: create uniform brand headshots quickly (marketing, LinkedIn, company bios). Nano-Banana keeps facial fidelity while changing outfit, background, or lighting.

**Prompt — outfit + lighting (edit)**

```
Edit the uploaded photo into a professional corporate headshot:
- Replace outfit with a navy single-breasted blazer and white shirt.
- Preserve face shape, eyeglasses, and expression exactly.
- Apply softbox studio lighting (slightly warm), remove harsh shadows.
- Output ratio 4:5 portrait, photorealistic, high detail.
```

**Prompt — background swap + retouch**

```
Edit the uploaded image: replace background with a clean light-gray studio backdrop, remove small blemishes, slightly sharpen eyes, and keep all facial proportions. Preserve left ear earring and hairline.
```

---

### 2) E-commerce & product visualisation

Use: place products into lifestyle scenes, generate consistent product shots from different angles, or show color variants.

**Prompt — product-in-scene (multi-image fusion)**

```
Using Image A (product photo on white) and Image B (cozy living room scene), place the product on the living room coffee table with natural shadows matching the scene. Keep product scale realistic and preserve product texture and labeling.
```

**Prompt — color variants (edit)**

```
Edit the uploaded product image: generate three color variants (forest green, deep navy, and charcoal). Keep product dimensions, seams, and label legible; output as a 3-up grid, photorealistic.
```

### 3) Social content & influencer marketing

Use: fast stylistic edits, outfit swaps, seasonal overlays, or multiple-format crops for social platforms.

**Prompt — seasonal edit for feed and story**

```
Edit the uploaded photo: swap casual tee for a chic leather jacket, add subtle golden-hour lighting from top-left, crop a square for feed and a 9:16 vertical for story. Preserve face and sunglasses.
```

**Prompt — stylized promo variant**

```
Edit the uploaded portrait to create a high-contrast editorial style: increase contrast moderately, add film grain, and maintain natural skin texture; preserve facial proportions and jewelry.
```

### 4) Character / brand asset consistency (mascots, recurring characters)

Use: keep logos, mascots, or characters visually identical across scenes, campaigns, or episodes.

**Prompt — character sheet enforcement**

```
Reference: character_sheet.png (attached). Key identifiers to preserve exactly across edits: warm olive skin, split-dimple on right cheek, green scarf with gold pin. Create a portrait of the character on a busy café terrace; maintain identifiers and expression.
```

---

### 5) Historical photo repair & colorization

Use: restore or colorize archival images while preserving composition and fine facial details.

**Prompt — colorize + repair**

```
Edit uploaded black-and-white photo: colorize with natural skin tones based on European 1940s palette, remove scratches and dust, repair torn left border, preserve original composition and facial proportions. Output: high-resolution TIFF-quality.
```

## What advanced prompting techniques increase reliability?

### Use *reference anchors* and *micro-constraints*

Reference anchors are brief, verifiable pieces of info you add to reduce ambiguity: exact clothing names (“navy blazer, single-breasted, notch lapel”), lighting references (“Rembrandt lighting”), or camera terms (“50mm portrait lens, f/2.8”). Micro-constraints tell the model what it must not change (e.g., “do not alter the tattoos on right forearm”). These reduce the model’s freedom in a productive way and typically improve outcome fidelity.

### Iteration loop: ask, evaluate, refine

1. **First pass:** use a precise but concise prompt.
2. **Assess results:** note what the model got wrong (e.g., changed face shape, lost an accessory).
3. **Targeted correction:** send a short follow-up prompt referencing the previous result (“Keep everything from last output but keep the original left ear earring and make the eyebrows thicker”). Nano-Banana’s conversational editing strengths let you recover quickly.

### Chain-of-edits for complex transformations

For large edits, break work into a chain of smaller edits rather than one massive instruction. Example chain: (1) background swap → (2) outfit update → (3) color grading → (4) final retouch. This keeps each prompt focused and reduces unexpected cross-effects.

## How should I structure prompts for Nano-Banana? (Prompt anatomy)

Good image prompts have a consistent structure. Use the following **prompt anatomy** to get precise, repeatable results:

### Prompt anatomy (recommended order)

1. **Action / Goal** — what do you want the model to *do*? (e.g., “Edit this selfie to create a professional headshot” or “Generate a product lifestyle photo combining these two images”).
2. **Subject(s)** — who or what is in the image? Be specific about identity, age, number of people, items, etc.
3. **Attributes** — visual characteristics: clothing, facial expressions, eye color, hair, props.
4. **Environment & Lighting** — location, time of day, mood lighting, focal length, lens hints (“35mm portrait”).
5. **Style & Finish** — photographic style (cinematic, studio, film grain, hyperreal), or art style (oil painting, vector, comic).
6. **Constraints / Safety** — anything to avoid (no logos, no nudity, no medical text).
7. **Consistency token** (optional) — short phrase that you reuse to maintain character recognition across multiple prompts (e.g., “Use the ‘Luna scarf’ character reference”).

### Hints for character consistency (practical steps)

- **Use a “reference phrase”**: include a short, unique phrase tied to the subject (e.g., “character token: ‘Maya-blue-jacket’”) in every prompt. The model will more reliably link edits to the same character if you reuse this phrase.
- **Include anchored details**: specify distinctive, immutable features (e.g., “left eyebrow scar, green birthmark on right cheek”) so the model has fixed anchors to maintain.
- **Maintain pose and framing when possible**: if you want true continuity, keep the camera angle/pose description similar across prompts.
- **Start from the same original image**: for editing workflows, always supply the same source image as the anchor. When you must change photos, include the original image as an extra input and explain the transformation.

## What are common failure modes and how do I fix them?

### Failure: identity drift (subject looks different)

**Cause:** the model over-generalized a requested style or misinterpreted a constraint.
**Fixes:** add an explicit “preserve” clause, attach the original image as a reference, or perform edits in smaller steps and validate intermediate outputs.

### Failure: inconsistent props or hands

**Cause:** hands and small accessories are historically tricky for many image models.
**Fixes:** include micro-constraints (“preserve watch on right wrist”), provide a detailed close-up reference for small items, or run a final targeted correction step focusing only on the problematic element.

### Failure: lighting or shadows look unnatural

**Cause:** large edits (background swap or major relighting) can create mismatches.
**Fixes:** ask the model to match “directional light from top-left, soft shadows” or provide the desired lighting reference image.

## Conclusion

Nano-Banana (Gemini 2.5 Flash Image) is a notable step forward in consumer-grade image editing and generation: fast, consistent, and integrated with Google’s Gemini ecosystem and safety tooling. The best results come from **clear, task-focused prompts**, explicit preservation instructions when you need identity consistency, and staged workflows that separate quick previews from final renders. As the model and ecosystem evolve, prompt engineers should keep testing, log outcomes, and build user-facing controls that make editing transparent and reversible.

---

*Originally published at [https://www.cometapi.com/ultimate-guide-to-nano-banana-how-to-use-and-prompt-for-best/](https://www.cometapi.com/ultimate-guide-to-nano-banana-how-to-use-and-prompt-for-best/).*
