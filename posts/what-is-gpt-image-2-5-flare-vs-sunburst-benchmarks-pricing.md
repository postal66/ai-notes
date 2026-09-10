<!-- social-ops-fingerprint:a7a361fcdf6e114675d0d588b34508551a3ad244f2b6fd0eead4ac80492ac73e -->
---
title: What Is GPT-Image-2.5? Flare vs Sunburst, Benchmarks & Pricing
---
# What Is GPT-Image-2.5? Flare vs Sunburst, Benchmarks & Pricing

![What Is GPT-Image-2.5? Flare vs Sunburst, Benchmarks & Pricing](https://resource.cometapi.com/images2point5_16-9c.png)

## TL;DR

GPT-Image-2.5 is OpenAI’s newest generation of image creation and editing technology, launched on [September 8, 2026](https://openai.com/index/introducing-chatgpt-images-2-5/) as the successor to ChatGPT Images 2.0 and the GPT-Image-2 API generation.

For developers, GPT-Image-2.5 is available as two models: Flare and Sunburst. Flare is designed as the default option for most production applications, combining higher image quality with substantially faster generation. Sunburst targets workflows where editing precision and final-image fidelity matter more than latency.

The upgrade is not simply about sharper pictures. GPT-Image-2.5 improves reference-image preservation, localized edits, multi-turn editing consistency, visual realism, instruction following, transparent-background generation, and high-resolution output. OpenAI says image-generation latency has been reduced by [up to 50% compared with Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-5/).

Early human-preference benchmarking is also strong. In the September 9 Arena snapshot, Sunburst ranked first for text-to-image generation at 1421 ± 13 Elo, while Flare ranked second at 1399 ± 13, ahead of Image 2 at 1381 ± 4.

Developers can access both variants through CometAPI: [GPT-Image-2.5 Flare](https://www.cometapi.com/models/openai/gpt-image-2-5-flare/) uses `gpt-image-2.5-flare` for faster, high-volume work, while [GPT-Image-2.5 Sunburst](https://www.cometapi.com/models/openai/gpt-image-2-5/) uses `gpt-image-2.5-sunburst` when editing precision and final-image fidelity matter most. Both can be used through the familiar `/v1/images/generations` and `/v1/images/edits` routes; transparent output should use PNG or WebP.

## Key Takeaways

- GPT-Image-2.5 is a generation-level upgrade, not just a minor image-quality refresh.
- Developers get two variants: Flare for speed and scale, and Sunburst for maximum editing precision.
- Flare delivers higher quality than Image 2 with 50% lower latency, according to OpenAI.
- Both variants support low, medium, high, xhigh, max, and auto quality modes.
- Custom output dimensions can reach 4K-class pixel counts, with individual edges up to 3840 pixels.
- Current Arena results place Sunburst and Flare above Image 2 in both text-to-image and single-image editing.
- Both models use the same official token rates: $5/M text input tokens, $8/M image input tokens, and $30/M image output tokens.
- Flare API in CometAPI currently provides a lower headline input/output price for developers building production image workflows.

## What Is GPT-Image-2.5?

GPT-Image-2.5 is OpenAI’s latest image generation and image editing model family. In ChatGPT, the technology appears as ChatGPT Images 2.5. At the API layer, developers can choose between two distinct models:

- gpt-image-2.5-flare
- gpt-image-2.5-sunburst

This distinction matters because “GPT-Image-2.5” is best understood as the model generation or family, rather than a single API model ID.

GPT-Image-2.5 builds on the capabilities of [Image 2 API in CometAPI](https://www.cometapi.com/models/openai/gpt-image-2/) while focusing much more heavily on the workflow around image creation. Instead of treating every generation as a mostly independent result, the new generation is designed to preserve subjects, compositions, styles, and previous edits as users iterate.

OpenAI highlights improvements in [reference-image fidelity and precision editing](https://openai.com/index/introducing-chatgpt-images-2-5/), as well as multi-turn consistency, richer textures, and natural lighting. That makes GPT Image 2.5 especially relevant to commercial creative work, where a single requested edit should not unpredictably reconstruct the rest of the asset.

One important change is the introduction of xhigh and max. Earlier GPT Image models only supported quality settings through high; GPT-Image-2.5 therefore provides developers with more control over the latency-versus-fidelity tradeoff. The models also support [custom dimensions up to 8,294,400 total pixels](https://developers.openai.com/api/docs/guides/image-generation), although OpenAI marks resolutions above 2560×1440 as experimental. Width and height must be multiples of 16.

### Flare vs Sunburst

Flare and Sunburst share the same core GPT-Image-2.5 capabilities, but they optimize different production constraints.

| Decision factor | Flare | Sunburst |
| --- | --- | --- |
| Primary goal | Fast, high-quality generation at scale | Maximum generation and editing precision |
| Relative latency | Faster; preferred for interactive workflows | Slower; prioritizes fidelity and control |
| Best workloads | Social assets, prototypes, visual search, high-volume apps | Campaign creative, product hero images, difficult localized edits |
| Editing behavior | Strong reference fidelity and multi-turn consistency | Strongest choice when preserving exact details matters |
| Recommended routing | Default model for routine requests | Precision tier for demanding generations and final edits |

For most applications, start with Flare and route difficult final edits to Sunburst. This preserves responsiveness without giving up the higher-precision option.

## What Is New in GPT-Image-2.5?

### Better Reference-Image Fidelity

One of the most important GPT-Image-2.5 improvements is how faithfully it preserves a source image. Reference-based generation has traditionally had an uncomfortable tradeoff: the more aggressively a model transforms an image, the more likely it is to alter identity, proportions, products, backgrounds, or small visual characteristics that were supposed to remain unchanged.

GPT-Image-2.5 is designed to retain more of those details. OpenAI says subjects should remain more recognizable while lighting, environments, clothes, composition, or style are transformed. This matters for product-background replacement, campaign variations around the same character, outfit changes that preserve pose and identity, and alternative compositions built from the same source asset.

OpenAI’s official “Remixed baby portrait” example shows a source-aware edit that changes the outfit while preserving the pose and blue studio background.

![What Is GPT-Image-2.5? Flare vs Sunburst, Benchmarks & Pricing](https://resource.cometapi.com/12345.JPEG)

*Official input image from OpenAI.*

![What Is GPT-Image-2.5? Flare vs Sunburst, Benchmarks & Pricing](https://resource.cometapi.com/123456.PNG)

*Official edited output from OpenAI.*

### More Precise Image Editing

A second major upgrade is edit localization. If a product photo contains a bottle, background, headline, logo, shadows, and supporting props, a useful image editor should be able to replace only the headline without unexpectedly changing the bottle shape, camera angle, or lighting. GPT-Image-2.5 is better at distinguishing between what should change and what should remain fixed.

### More Reliable Multi-Turn Editing

The real value of image editing often appears after the first edit. A typical creative workflow may generate a product scene, change the background, move the product, replace the headline, add a promotional badge, adjust the lighting, and finally export a transparent version.

With weaker image models, each successive step can gradually degrade details established earlier in the workflow. GPT-Image-2.5 is specifically designed to make previous changes more persistent across multiple editing turns, moving image generation closer to an interactive editing process rather than a sequence of unrelated generations.

### More Natural Lighting and Texture

GPT-Image-2.5 also targets visual artifacts that make AI-generated photographs easy to recognize. OpenAI reports improvements in natural lighting and richer material textures. In practice, those changes can matter for skin, fabric, glass, metal, packaging, furniture, food photography, and realistic environmental scenes.

### Better Complex Instruction Following

Modern image-generation prompts increasingly resemble design briefs. A user may specify several objects, exact locations, a headline, product packaging, camera perspective, brand colors, lighting, foreground and background relationships, transparent areas, and exclusions. GPT-Image-2.5 improves its ability to translate these structured requests into a coherent image.

### Transparent Backgrounds and Flexible Output

Both GPT-Image-2.5 API models support transparent backgrounds when the output format is PNG or WebP.

```
background="transparent"
output_format="png"
```

The [official image-generation specification](https://developers.openai.com/api/docs/guides/image-generation) also allows arbitrary valid WIDTHxHEIGHT dimensions rather than forcing developers into only a few fixed aspect ratios. This is useful for e-commerce assets, overlays, presentation graphics, UI components, stickers, isolated objects, thumbnails, and ad creatives.

## GPT-Image-2.5 Benchmark Performance

Image-generation benchmarks require careful interpretation. There is no single metric equivalent to a language-model math benchmark that captures aesthetics, prompt adherence, edit precision, visual realism, text rendering, and reference fidelity simultaneously. For GPT-Image-2.5, three kinds of quantitative evidence are currently useful: Arena human-preference results, OpenAI’s latency measurements, and OpenAI’s safety-stack evaluations.

### Arena Text-to-Image Benchmark

[Arena](https://arena.ai/leaderboard/text-to-image) evaluates models through blind human preference: users receive outputs from two anonymous models for the same task and select the result they prefer. The snapshot shows the following:

> Arena preliminary snapshot

| Model | Text-to-Image Elo | Rank | Votes |
| --- | --- | --- | --- |
| Sunburst | 1421 ± 13 | 1 | 3,149 |
| Flare | 1399 ± 13 | 2 | 2,856 |
| Image 2 (medium) | 1381 ± 4 | 3 | 78,731 |
| MAI Image 2.6 | 1331 ± 7 | 4 | 11,213 |
| Grok Imagine Image 2.0 (low) | 1315 ± 12 | 5 | 2,681 |

### Image Editing Benchmark

The same pattern is visible in Arena’s single-image editing leaderboard.

| Model | Single-Image Edit Elo | Difference vs Image 2 |
| --- | --- | --- |
| Sunburst | 1520 ± 9 | +59 |
| Flare | 1491 ± 9 | +30 |
| Image 2 | 1461 ± 3 | Baseline |
| Grok Imagine Image 2.0 | 1439 ± 8 | -22 |
| MAI Image 2.6 | 1434 | -27 |

Sunburst’s advantage is particularly visible in editing: its lead over Image 2 is larger here than in text-to-image generation, which aligns with its positioning as the precision-oriented model.

### Generation Latency

OpenAI says GPT-Image-2.5 reduces generation latency by up to 50% versus Images 2.0. For the API specifically, OpenAI positions Flare as delivering higher-quality images than Image 2 with 50% lower latency. Sunburst is deliberately designed to trade more generation time for additional precision.

### Safety Evaluation

OpenAI also published a quantitative safety evaluation using adversarial prompts intentionally designed to request policy-violating images.

| Model | Safe Generated | Unsafe Blocked | Unsafe Presented |
| --- | --- | --- | --- |
| Sunburst | 77.0% | 21.9% | 1.09% |
| Flare | 79.4% | 19.2% | 1.41% |
| ChatGPT Images 2.0 baseline | 75.2% | 23.1% | 1.64% |

Source: [OpenAI Images 2.5 safety evaluations](https://deploymentsafety.openai.com/chatgpt-images-2-5/safety-evaluations). Compared with the 1.64% baseline, the final unsafe-outcome rate falls by 0.55 percentage points for Sunburst and 0.23 percentage points for Flare.

> These figures are safety-stress-test results, not general image-quality scores or estimates of normal user traffic.

## Flare vs Sunburst vs Image 2

For most developers, the more useful question is not whether GPT-Image-2.5 is better in the abstract. It is which model makes sense for a particular workload.

| Dimension | Flare | Sunburst | Image 2 |
| --- | --- | --- | --- |
| Main goal | Speed + high quality | Maximum precision | Previous-generation general image model |
| Text-to-image | Excellent | Best current Arena result | Excellent |
| Image editing | Excellent | Best of the three | Strong |
| Arena T2I Elo | 1399 ± 13 | 1421 ± 13 | 1381 ± 4 |
| Arena image-edit Elo | 1491 ± 9 | 1520 ± 9 | 1461 ± 3 |
| Relative latency | Fastest choice | Slower | Baseline |
| Reference fidelity | Improved | Improved / precision focused | Strong |
| Multi-turn editing | Improved | Improved | Less optimized |
| Quality settings | Up to max | Up to max | Up to high |
| Custom dimensions | Yes | Yes | Yes |
| 4K-class output | Yes | Yes | Yes |
| Transparent backgrounds | Yes | Yes | Yes |
| Best use | Apps, social, prototyping, batch generation | Campaigns, polished products, difficult edits | Existing integrations |
| Recommended for new API projects | Yes, default | Yes, when precision matters | Mainly when maintaining existing workflows |

### Which Model Wins on Quality?

The current answer is Sunburst. It leads both major Arena image categories and is explicitly positioned by OpenAI as its most capable model for image generation and editing.

### Which Model Wins on Speed?

The answer is Flare. Its combination of high preference scores and substantially reduced latency makes it the most attractive general-purpose option in the family.

### Does Flare Cost Less Than Sunburst?

> **Not at the published unit-rate level.**
>
> Both models currently use the same published token prices. Flare's economic advantage comes primarily from latency and workflow throughput, not a lower token price.

## GPT-Image-2.5 Pricing

OpenAI currently applies the same token rates to Flare and Sunburst:

| Token Type | Flare | Sunburst |
| --- | --- | --- |
| Text input | $5 / 1M tokens | $5 / 1M tokens |
| Cached text input | $1.25 / 1M tokens | $1.25 / 1M tokens |
| Image input | $8 / 1M tokens | $8 / 1M tokens |
| Cached image input | $2 / 1M tokens | $2 / 1M tokens |
| Image output | $30 / 1M tokens | $30 / 1M tokens |

The official token rates therefore do not create a simple “Flare is cheap, Sunburst is expensive” distinction. Instead, the economic difference comes from workflow behavior. A faster model can reduce end-user waiting time, application concurrency requirements, abandoned generation attempts, iterative design time, and infrastructure occupied by long-running requests.

### Image input cost

Example: Reference-Image Editing Cost: Total request cost = text input tokens × $5/M + image input tokens × $8/M + image output tokens × $30/M

### GPT-Image-2.5 Flare and Sunburst Pricing in CometAPI

Currently, CometAPI presents a 20% headline discount relative to the matching official input/output rates. Because OpenAI publishes the same unit rates for Flare and Sunburst, the displayed comparison is the same for both variants.

| Model | Model ID | CometAPI input | CometAPI output | Official input/output |
| --- | --- | --- | --- | --- |
| Flare | gpt-image-2.5-flare | $4 / 1M tokens | $24 / 1M tokens | $5 / $30 per 1M tokens |
| Sunburst | gpt-image-2.5-sunburst | $4 / 1M tokens | $24 / 1M tokens | $5 / $30 per 1M tokens |

These are simplified headline input/output figures. OpenAI separately prices text input, image input, cached inputs, and image output, so reference-image and editing workloads should be budgeted from the token categories returned by real requests. Confirm the live model catalog before production deployment because provider pricing can change.

## Best Use Cases for GPT-Image-2.5

### Product Photography

Reference preservation and targeted editing are particularly valuable in e-commerce. A seller can retain the same product while changing the background, lighting, seasonal setting, promotional text, shadows, composition, or regional campaign treatment.

### Advertising and Campaign Creative

Sunburst is particularly attractive when one master creative needs several carefully controlled variations. A marketing team can preserve the product and brand composition while changing a headline, background scene, promotion, language, or visual treatment.

### Social Content at Scale

Flare’s latency advantage makes it a better fit for social-image generators, creator tools, personalized thumbnails, memes, profile assets, and automated content pipelines, where throughput and iteration speed often matter more than squeezing out the final few points of image preference.

### Visual Prototyping

Designers can use GPT-Image-2.5 for rapid exploration of app screens, website concepts, packaging, interiors, product concepts, presentation visuals, and advertising layouts.

### Image Editing Products

For applications where users upload their own photos, improved preservation can be more important than pure text-to-image quality. Examples include outfit changes, interior redesign, background replacement, product retouching, headshot variations, and personalized creative assets.

### Transparent Assets

Native transparent-background output makes the models more practical for isolated product objects, stickers, UI graphics, presentation assets, and compositing pipelines.

## GPT-Image-2.5 Limitations

### Text Can Still Fail

Text rendering has improved substantially across recent GPT Image generations, but generated text should still be verified manually for high-stakes advertisements, packaging, menus, legal copy, and UI screenshots.

### Exact Layout Control Is Not Guaranteed

A natural-language instruction such as “place the logo exactly 40 pixels from the top-left corner” is not equivalent to a deterministic design-tool constraint. Pixel-critical layouts are better handled by generating the visual asset first and composing exact text or interface elements programmatically or in a design tool.

### Character and Brand Consistency Can Still Drift

Multi-turn consistency is improved, not perfect. Long image sequences, repeated character generation, and large brand campaigns should still include quality-control checks.

### Very High Resolutions Are Experimental

> Although the API allows up to 8,294,400 total pixels and a maximum edge of 3840 pixels, resolutions above 2560×1440 are currently experimental. Production systems should test high-resolution output rather than assuming every 4K configuration behaves identically.

### Complex Prompts Can Still Take Time

Difficult requests can still take substantial processing time. Applications should implement proper loading states, timeouts, retries for transient failures, and asynchronous handling for batch pipelines.

## Flare or Sunburst: Which Should You Choose?

The choice can be simplified to one question: is speed or final-edit precision more important to the workflow?

### Choose Flare when you are building:

- consumer-facing image applications
- high-volume generation
- social-content tools
- rapid prototypes
- visual-search result generation
- product experiences
- interactive editors where users expect fast feedback

### Choose Sunburst when you are creating:

- production-ready campaign assets
- premium product imagery
- demanding reference-image edits
- difficult multi-step revisions
- visuals where preserving exact details matters more than response time

For most new applications, Flare should be the starting point. Sunburst is better treated as a precision tier rather than the automatic choice for every request. A sophisticated production system could route routine requests to Flare and reserve Sunburst for edits that require higher precision.

## Why Use GPT-Image-2.5 Through CometAPI?

CometAPI can simplify a production image stack in ways that go beyond the advertised price difference:

- **One API:** use the same authentication and the familiar `/v1/images/generations` and `/v1/images/edits` routes for supported generation and editing workflows.
- **Model switching:** change the model field to route from `gpt-image-2.5-flare` to `gpt-image-2.5-sunburst`, or fall back to `gpt-image-2`, without rebuilding the surrounding application integration.
- **Unified billing:** consolidate usage and billing for supported models instead of maintaining a separate account and invoice for each route.
- **Multi-model experimentation:** run controlled comparisons with the same prompts, reference images, dimensions, and quality settings, then measure latency, token use, edit accuracy, and accepted-output rate.
- **Cost optimization:** default to Flare for responsive, high-volume work, escalate precision-sensitive edits to Sunburst, and retain Image 2 where an existing workflow needs its mature behavior. Combine routing with real usage data rather than choosing solely from headline token prices.

The practical advantage is operational consistency: teams can test and route models within one integration while selecting the quality, latency, and cost profile appropriate to each request.

## Conclusion

GPT-Image-2.5 represents OpenAI’s latest step from generative image creation toward a more controllable image-editing platform. Flare is the most broadly useful version: it combines the new family’s quality and editing improvements with significantly reduced latency, making it suitable for interactive applications and high-volume production.

Sunburst pushes further toward precision. Current Arena results place it ahead of Flare and Image 2 in both text-to-image generation and single-image editing, making it the stronger choice for demanding professional creative workflows.

The most meaningful change, however, is workflow reliability. Better subject preservation, targeted editing, multi-turn consistency, custom high-resolution output, and transparent-background generation make GPT-Image-2.5 more practical for real creative pipelines rather than isolated image-generation demos.

## FAQ

### What is GPT-Image-2.5?

GPT-Image-2.5 is OpenAI’s newest image generation and editing model family, released in September 2026. In the API it is divided into Flare and Sunburst.

### What is the difference between ChatGPT Images 2.5 and GPT-Image-2.5?

ChatGPT Images 2.5 refers to the image-generation experience integrated into ChatGPT. Developers access the new generation through API models including gpt-image-2.5-flare and gpt-image-2.5-sunburst.

### What is GPT-Image-2.5Flare?

GPT-Image-2.5 Flare is the speed-oriented GPT-Image-2.5 variant and OpenAI’s recommended default for most API applications. It focuses on high image quality, image editing, and significantly lower generation latency.

### What is GPT-Image-2.5 Sunburst?

GPT-Image-2.5 Sunburst is OpenAI’s highest-capability GPT-Image-2.5 variant for generation and editing. It is intended for workflows where precision and control matter more than generation speed.

### Is GPT-Image-2.5 better than Image 2?

Current evidence indicates yes. In the September 9 Arena snapshot, Sunburst scored 1421 ± 13 and Flare 1399 ± 13 in text-to-image, compared with 1381 ± 4 for Image 2. Single-image editing shows an even larger advantage for the two new models.

### Is GPT-Image-2.5 faster than Image 2?

Flare is. OpenAI says Flare delivers higher image quality than Image 2 at 50% lower latency. Sunburst intentionally accepts longer generation times in exchange for tighter editing control.

### Does GPT-Image-2.5 support 4K images?

Yes. Both API variants support custom dimensions with up to 8,294,400 total pixels and an individual edge of up to 3840 pixels. OpenAI currently considers resolutions above 2560×1440 experimental.

### How much does GPT-Image-2.5 cost?

OpenAI currently charges both Flare and Sunburst $5 per million text input tokens, $8 per million image input tokens, and $30 per million image output tokens. Cached-input rates are lower.

### Should I use Flare or Sunburst?

Use Flare for most interactive, high-volume, consumer, social, and rapid-prototyping workloads. Use Sunburst when maximum edit precision and final visual fidelity are more important than latency.

---

*Originally published at [https://www.cometapi.com/what-is-gpt-image-2-5/](https://www.cometapi.com/what-is-gpt-image-2-5/).*
