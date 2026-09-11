<!-- social-ops-fingerprint:ee92bd218ba2c26af5c33a58fa9e3648301dcfd3dfa6c32fdc53234aa44703f3 -->
---
title: 7 Nano Banana Pro Prompts that You Should to Try!
---
# 7 Nano Banana Pro Prompts that You Should to Try!

![7 Nano Banana Pro Prompts that You Should to Try!](https://resource.cometapi.com/blog/uploads/2025/11/7-Nano-Banana-Pro-Prompts-that-You-Should-to-Try.webp)

Google’s **Nano Banana Pro** (the marketing name for the Gemini 3 Pro Image family) landed as a major step forward in image generation and editing tools. It’s designed to combine Gemini 3’s language and reasoning strengths with pixel-level image control, and it’s already being rolled into the Gemini app, Google Workspace products, Adobe Firefly/Photoshop integrations, and selectable APIs and CometAPI endpoints.

## What is Nano Banana Pro and why does it matter?

Nano Banana Pro is Google’s new image generation and editing model built on **Gemini 3 Pro Image** (often referenced in docs and previews as `gemini-3-pro-image` or `gemini-3-pro-image-preview`). Compared with earlier “Nano Banana” versions, the Pro model emphasizes:

- **High-quality text rendering** inside images (longer copy, multilingual text, legible typography).
- **Deeper contextual/world knowledge** so images and infographics can embed factual references or be grounded in real-world data.
- **Expanded reference blending** — you can mix up to **14 reference images** (including multi-person consistency).
- **A “Thinking” or reasoning phase** that lets the model perform multi-step layout and factual checks before rendering.

Those changes make Nano Banana Pro particularly appealing for creatives, product teams, marketers making mockups, and data visualization/infographic authors who need text+image fidelity.

## How to Access Nano Banana Pro?

Nano Banana Pro([Gemini 3 Pro Image( Nano Banana Pro) API](https://www.cometapi.com/gemini-3-pro-image-nano-banana-2-api/)) is available globally inside the Gemini app under the Create images option when you choose the Thinking model. Free-tier users get limited Pro quotas, after which it switches back to the original Nano Banana. Google AI Plus, Pro and Ultra subscribers get higher limits.

You could also consider [CometAPI](https://www.cometapi.com/), which offers a 20% discount on the Google API and unlimited usage.

## How should I prompt Nano Banana Pro

Successful prompts for Nano Banana Pro combine **clarity**, **structure**, and **constraints**. Because Pro runs a “thinking” mode, it responds well to prompts that include both creative direction and precise constraints.

### Best-practice checklist (short)

1. **Start with intent:** “Create” vs “Edit” vs “Mockup”.
2. **Be explicit about text:** specify exact text, language, font style, alignment, and maximum characters.
3. **Provide references:** upload source images (up to 14) and label them in the prompt.
4. **Use camera/lighting terms:** “3⁄4 view, soft rim light, shallow depth of field.”
5. **Specify output constraints:** aspect ratio, resolution (2K/4K), and file format.
6. **Iterate conversationally:** Pro supports multi-turn edits — use the model to refine.

### Prompt anatomy that works well

- **Line 1 — Goal / action:** e.g., “Generate a 4K product hero image for an eco water bottle for a website hero.”
- **Line 2 — Composition & camera:** e.g., “Center product on white seamless background, 35mm lens look, softly diffused key light from top-left.”
- **Line 3 — Styling & color:** e.g., “Minimalist, clean shadows, brand color teal #009688 on label.”
- **Line 4 — Text to render exactly:** e.g., `TEXT: "Sip Green — 500 ml" (Helvetica Neue, bold, centered under product).`
- **Line 5 — Output constraints & references:** e.g., “Output 3840×2160 PNG, include person\_ref\_01 as background model, keep skin tone realistic.”

## What are practical applications and example workflows?

Nano Banana Pro is suited for a wide range of production workflows. Below are high-value verticals and pattern examples.

### Marketing & creative agencies

- **Use case:** Rapidly prototype ad concepts with accurate product text and multilingual variants.
- **Pattern:** Draft 3 rough concepts (Nano Banana fast mode), iterate on best candidate in Pro to produce print-ready assets with exact text and brand fonts. Integrate Pro outputs into Adobe Photoshop for final adjustments.

### Product design & prototyping

- **Use case:** Turn sketches or concept diagrams into photoreal mockups.
- **Pattern:** Upload CAD or sketch images, request photoreal material application, and generate multiple lighting variants for usability testing and stakeholder review.

### Localization & content ops

- **Use case:** Create localized versions of an event poster with accurate language rendering.
- **Pattern:** Use a single base prompt and replace the `text` block with localized strings; ask Pro to maintain layout and legibility constraints.

### Documentation & infographics

- **Use case:** Create technically accurate diagrams for manuals with embedded numeric data.
- **Pattern:** Attach source CSVs and use the “data-accurate infographic” template to prevent hallucinated numbers. Always attach the dataset and request exact axis labels.

### Archival & restoration

- **Use case:** Restore damaged photos and colorize for museum exhibits.
- **Pattern:** Use the restoration template with constraints to preserve facial identity and historical accuracy.

## 7 high-performance prompt templates and how to use them

Below are seven battle-tested prompt templates adapted for Nano Banana Pro. Each includes a short application note and a short code snippet showing how to pass the prompt to the API.

> Tip: Replace tokens like `{PRODUCT}`, `{TEXT}`, `{REF_IMAGE}` with your actual assets.

---

### 1) Product Hero (e-commerce / ads)

**Use when:** You need a clean, conversion-ready product image for a landing page or paid ad.

**Prompt template**

```
Generate a 4K product hero of {PRODUCT}.
Composition: centered product, 3/4 angle, white seamless background.
Camera: 50mm lens look, slight vignette, soft key light top-left, rim light back-right.
Styling: minimal shadows, glossy label finish.
Exact text (rendered on image): "{TEXT}" — font: {FONT_NAME}, bold, centered under product.
Output: PNG 3840x2160, transparent background optional.
```

**Example code snippet (Python):**

```
prompt = "...(use template above with replacements)..."
# call Gemini API as in previous example
```

**Why it works:** explicit camera + text instructions make Pro render legible, brand-safe assets.

---

### 2) High-detail Infographic (facts & diagrams)

**Use when:** Creating annotated diagrams, timelines, or data visuals.

**Prompt template**

```
Create an educational infographic titled "{TITLE}".
Include labeled diagram with arrows for: {LIST_OF_ELEMENTS}.
Text: use exact block labels provided below. Keep labels legible at 600px width.
Style: flat vector-esque with subtle shadows, color palette: {PALETTE_HEX}.
Output: PNG 3000x2000. Include alt-text below: {ALT_TEXT}.
```

**Why it works:** Pro’s world knowledge + text rendering makes complex labels and multi-part diagrams stable.

---

### 3) Photo restoration + controlled edits

**Use:** Restore and modernize historical photos while preserving authenticity.

**Prompt template**

```
Deliverable: Restored and colorized version of uploaded 1930s black-and-white photo.
Source image: <UPLOAD_VINTAGE_PHOTO>.
Edits: Remove scratches and stains, reconstruct missing edges, subtle colorization based on reference palette (olive greens, sepia highlights), maintain period-accurate clothing textures.
Style: Realistic historical colorization; avoid modern anachronisms.
Text: Caption overlay in lower left: "<NAME> — 1935", serif font, 12pt.
Constraints: Preserve facial identity; output must look plausible for archival use.
Output: 3500×2500 TIFF with metadata.
```

**Why it works:** Pro supports multi-turn editing; concise edit instructions keep continuity.

---

### 4) Character Consistency (comics / brand mascot)

**Use when:** Maintaining a character’s appearance across multiple frames.

**Prompt template**

```
Generate 3 images with consistent character "Mila", a young barista:
- skin tone: warm olive, freckles on nose
- hair: bob, chestnut
- outfit: green apron with logo
Action sequence:  making espresso,  handing cup to customer,  smiling at camera.
Ensure consistent facial features across images. Output: 1024x1024 each.
```

**Why it works:** Pro’s multi-reference/person consistency is built for this.

---

### 5) Localized Poster (multi-language text)

**Use when:** You need the same poster copy in several languages.

**Prompt template**

```
Create a poster for "Autumn Film Night".
Languages: English, Japanese, Spanish — render each as a separate panel (three panels).
Ensure fonts and text rendering remain legible in each language, translations provided below.
Style: retro cinema poster, film grain, bold headline type.
Output: 3840x1080 (three panels).
```

**Why it works:** Nano Banana Pro significantly improves multilingual on-image text rendering.

---

### 6) Photoreal Background Replacement (marketing compositing)

**Use when:** Putting product/person into a consistent lifestyle scene.

**Prompt template**

```
Composite subject_ref_01 into a Scandinavian kitchen scene.
Match perspective and lighting; keep subject shadow under feet tied to floor.
Add subtle motion blur to background to emphasize subject.
Color grade: warm +5 exposure, lift shadows +10.
Output: 4K PNG.
```

**Why it works:** Pro’s camera/lighting instructions produce believable composites for ads.

---

### 7) Historical/Time-range Portraits (creative & research)

**Use when:** Generating portraits across eras (e.g., for research or exhibits).

**Prompt template**

```
Generate portraits of the same subject across eras: 1880s (sepia, formal), 1920s (charcoal, studio), 2025 (high-res digital).
Maintain subject facial proportions; clearly label each era below portrait.
Style specifics provided for each era (lighting, grain, paper texture).
Output: three 1024×1536 vertical portraits.
```

**Why it works:** People are using Pro to generate historically styled portraits and visual timelines; it’s good for creative storytelling.

> **Handling image uploads for blends/consistency:** When you need to blend multiple source images: upload each source as a multipart/form-data file or provide pre-signed asset URLs, then reference them in the prompt payload (see `image1`, `image2` pattern in cURL). Provide constraints like “preserve face identity” or “match perspective of image2” inside prompt metadata.

## Common failure modes and fix

1. **Garbled or mis-rendered text** — Ensure exact strings in prompt, provide typography hints, or use inpainting to paste a real font if the tool allows.
2. **Inconsistent characters across images** — Provide consistent attribute lists (hair, scar, clothing) and, if available, upload a reference image to anchor likeness.
3. **Overfitting to stylized prompts** — If images become too stylized, remove ambiguous adjectives and be prescriptive about the photographic or illustration style (e.g., “photorealistic, 35mm lens, f/2.8”).
4. **Incorrect factual diagrams** — Add labeled constraints and explicit numerical labels; verify the rendered numbers in the returned image and re-ask with constrained correction when necessary.

## Conclusion

Nano Banana Pro is truly impressive. While some tasks had minor shortcomings, the tasks it completed were incredibly fun and creative. The Taj Mahal blueprint, annotated diagrams, and product mockups were particularly outstanding.

Using the structured methods, templates, and advanced techniques in this guide, you can reliably generate stunning, consistent, and professional-looking images every time.

Developers can access [Gemini 3 Pro Image( Nano Banana Pro) API](https://www.cometapi.com/gemini-3-pro-image-nano-banana-2-api/) through CometAPI. To begin, explore the model capabilities of CometAPI in the [Playground](https://www.cometapi.com/console/playground) and consult the API guide for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. cometapi offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/7-nano-banana-pro-prompts-that-you-should-to-try/](https://www.cometapi.com/7-nano-banana-pro-prompts-that-you-should-to-try/).*
