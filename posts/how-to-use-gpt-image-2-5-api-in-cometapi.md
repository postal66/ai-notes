<!-- social-ops-fingerprint:b1b294f2d31bf2371baf10a5a0b74b347aa6d2037cdf782660c6dc4190b040aa -->
---
title: How to Use GPT-Image-2.5 API in CometAPI
---
# How to Use GPT-Image-2.5 API in CometAPI

![How to Use GPT-Image-2.5 API in CometAPI](https://resource.cometapi.com/04e0e3ef-6c9a-490e-ad5f-4d77a5a8cb64.png)

## **TL;DR**

GPT-Image-2.5 is a two-model image API family: Flare prioritizes fast, everyday generation, while Sunburst prioritizes editing precision and final-output fidelity. Through CometAPI, existing OpenAI SDK integrations can usually migrate by changing the base URL, API key, and model ID. Start with Flare at medium quality, measure latency and accepted-image cost, and route demanding edits or premium outputs to Sunburst.

## Key Takeaways

- Flare is the speed-first choice for interactive products, rapid iteration, and high-volume generation.
- Sunburst is the precision-first choice for localized edits, reference preservation, and complex final compositions.
- Both models accept text and image inputs, support six quality modes, and generate or edit images through the Images API.
- CometAPI supports the two model IDs through an OpenAI-compatible base URL and SDK pattern.
- Current Arena results favor Sunburst for generation and editing, while both new models remain marked preliminary.
- Production selection should be based on latency, acceptance rate, edit fidelity, token usage, and effective cost per approved image.

On September 8, 2026, OpenAI introduced ChatGPT Images 2.5 and launched two new image-generation models in the API: [GPT Image 2.5 Flare](https://www.cometapi.com/models/openai/gpt-image-2-5-flare/) for fast, everyday image generation and [GPT Image 2.5 Sunburst](https://www.cometapi.com/models/openai/gpt-image-2-5/) for workflows that prioritize image quality and tighter editing control. OpenAI positions Flare as the default for most applications, while Sunburst is its most capable image-generation and editing model.

Both models are now available through CometAPI. The practical advantage is that developers can call them through the familiar OpenAI SDK interface while replacing the API key and base URL with CometAPI credentials. [CometAPI’s OpenAI-compatible API](https://apidoc.cometapi.com/) means an existing image-generation application usually needs only a small integration change rather than a new SDK or request architecture.

This guide shows how to generate and edit images with GPT-Image-2.5 through CometAPI using cURL, Python, and JavaScript, and how to choose the right model, quality level, dimensions, and output format for a production workflow.

## What Is the GPT-Image-2.5 API?

GPT-Image-2.5 is OpenAI’s current image-generation family. It accepts text and image inputs and returns images. The family has two models: GPT-Image-2.5 Flare, optimized for speed and everyday use, and GPT-Image-2.5 Sunburst, optimized for maximum capability and precise editing.

![How to Use GPT-Image-2.5 API in CometAPI](https://resource.cometapi.com/11280X1280.PNG)

## How to GPT-Image-2.5 API Compared with GPT Image 2 API?

The key change is not merely a single faster replacement. GPT-Image-2.5 separates the workload into two purpose-built choices. Flare targets routine generation with lower latency, while Sunburst targets the most demanding generation and editing tasks. Both models expose the same broad control surface, including quality levels from `low` through `max`, image inputs for editing, and streaming partial images.

For migration, start by keeping your current prompts and request structure, then select a model according to latency and fidelity requirements. Re-test text rendering, preservation instructions, masks, reference-image order, output size, and cost before changing production traffic.

## Why Use GPT-Image-2.5 Through CometAPI?

CometAPI provides an OpenAI-compatible access layer that can reduce integration work when a team already uses its gateway. The practical benefits are centralized key management, a familiar request format, usage visibility, and the ability to route image generation and editing through one base URL.

| Item | Value |
| --- | --- |
| Base URL | `https://api.cometapi.com/v1` |
| Generation route | POST /images/generations |
| Editing route | POST /images/edits |
| Authentication | Authorization: Bearer $COMETAPI\_KEY |

> Provider prices and model availability can change. Confirm the model identifier, endpoint behavior, and current billing in the CometAPI dashboard before production rollout.

## How to Use GPT-Image-2.5 API in CometAPI

## Step 1: Get a CometAPI API Key

Create or sign in to your CometAPI account and generate a token from the [CometAPI API token console](https://www.cometapi.com/console/token).

Store the key as an environment variable rather than hard-coding it into application source:

| export COMETAPI\_KEY="your-cometapi-key" |
| --- |

On Windows PowerShell:

| $env:COMETAPI\_KEY="your-cometapi-key" |
| --- |

Do not expose the API key in browser-side JavaScript, public repositories, screenshots, or client applications. Server-side environment variables or a secret manager are safer choices for production.

## Step 2: Generate Your First Image with cURL

For most applications, start with Flare. A minimal generation request looks like this:

| curl "`https://api.cometapi.com/v1/images/generations`" \  -H "Authorization: Bearer $COMETAPI\_KEY" \  -H "Content-Type: application/json" \  -d '{  "model": "gpt-image-2.5-flare",  "prompt": "Premium product photograph of a matte black wireless speaker on a light concrete pedestal, soft window light, realistic material texture, clean editorial composition, no text",  "size": "1536x1024",  "quality": "medium",  "output\_format": "png"  }' |
| --- |

The critical CometAPI-specific pieces are the endpoint and API key. The [GPT Image 2.5 Flare API in CometAPI](https://www.cometapi.com/models/openai/gpt-image-2-5-flare/) uses the `api.cometapi.com/v1/images/generations` endpoint with Bearer authentication.

GPT Image models [normally return generated image content](https://www.cometapi.com/automate-image-generation-at-scale-one-api/) through `data[].b64_json` rather than requiring your application to download a permanent image URL.

A simplified response looks like:

| {  "data": [  {  "b64\_json": "<base64-image-data>"  }  ],  "usage": {  "input\_tokens": 32,  "output\_tokens": 1372,  "total\_tokens": 1404  }  } |
| --- |

Your application should decode the Base64 field and save the returned bytes instead of storing the Base64 string as the final asset.

## Step 3: Generate an Image with Python

| import base64  import os  import requests    response = requests.post(  "[https://api.cometapi.com/v1/images/generations",&#xA](https://api.cometapi.com/v1/images/generations%22,&#xA); headers={"Authorization": f"Bearer {os.environ['COMETAPI\_KEY']}"},  json={  "model": "gpt-image-2.5-flare",  "prompt": (  "A clean isometric illustration of a solar-powered research lab, "  "white background, precise geometry, no labels or watermarks"  ),  "size": "1536x1024",  "quality": "high",  "output\_format": "png",  },  timeout=180,  )  response.raise\_for\_status()  payload = response.json()  image\_b64 = payload["data"][0]["b64\_json"]  with open("research-lab.png", "wb") as file:  file.write(base64.b64decode(image\_b64)) |
| --- |

This is one of the biggest practical advantages of CometAPI for an existing OpenAI-SDK project: the official CometAPI example uses the same OpenAI client, changing the `base_url`, key, and model ID rather than replacing the application’s SDK layer.

## Step 4: Use Multiple Reference Images with the Responses API

Assign a stable role to every image before writing the prompt. A useful order is: subject first, style second, then background or layout reference. Name those roles explicitly in the prompt so the model does not have to infer which properties to copy.

```
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
)

response = client.responses.create(
    model="gpt-6-astra",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": (
                "Create a campaign image. Use image 1 only for the product "
                "shape and colors; image 2 only for lighting and visual style; "
                "image 3 only for the background composition. Preserve the "
                "product logo exactly and add no other text."
            )},
            {"type": "input_image", "image_url": "https://example.com/product.png"},
            {"type": "input_image", "image_url": "https://example.com/style.png"},
            {"type": "input_image", "image_url": "https://example.com/background.png"},
        ],
    }],
    tools=[{
        "type": "image_generation",
        "model": "gpt-image-2.5-sunburst",
    }],
)

for item in response.output:
    if item.type == "image_generation_call":
        with open("campaign.png", "wb") as file:
            file.write(base64.b64decode(item.result))
```

The Responses API uses a supported mainline model at the top level and selects GPT-Image-2.5 inside the image-generation tool. If the gateway does not yet expose the selected mainline model or tool schema, check the current CometAPI model catalog and use its documented equivalent.

> Note: Multiple reference images can be input at once, with each image serving a distinct role; clearly specify the purpose of each image in the prompt. When performing multi-image editing, pay attention to the input order and semantic correspondence.

## How to Edit Existing Images

Use the editing route when an existing asset must be preserved and changed. State what must remain fixed before describing the requested change.

```
curl https://api.cometapi.com/v1/images/edits \
  -H "Authorization: Bearer $COMETAPI_KEY" \
  -F "model=gpt-image-2.5-sunburst" \
  -F "image[]=@product.png" \
  -F "prompt=Preserve the product shape, label, and camera angle. Replace only the background with a warm studio gradient. Add no new text." \
  -F "quality=high" \
  -F "output_format=png"
```

![How to Use GPT-Image-2.5 API in CometAPI](https://resource.cometapi.com/12345.JPEG%2018-31-25-996.JPEG)

Input

![How to Use GPT-Image-2.5 API in CometAPI](https://resource.cometapi.com/123451.png)

Output

### Assign Roles to Multiple Input Images

Do not rely only on upload order. Say “image 1 is the subject,” “image 2 is the style reference,” and “image 3 is the background reference.” Then list the attributes allowed to transfer from each image. This reduces accidental copying of faces, logos, text, or layout from the wrong reference.

### Use a Mask for Localized Edits

A mask guides the editable area: transparent pixels indicate where change is allowed, while the remaining area should be preserved. The mask should match the source image’s size and format, include an alpha channel, and remain within the API’s file-size limit. With multiple input images, the mask applies to the first image.

A mask is guidance rather than a pixel-perfect selection. Reinforce it with preservation language such as “change only the transparent region; preserve all other pixels, text, and geometry.”

### Production Tips for GPT-Image-2.5 in CometAPI

The model specification does not list generic model-level streaming as a supported feature, but the Image API and Responses API support image-generation streaming with `partial_images`. This provides progressive image previews rather than token-by-token text streaming.: the Images API accepts [partial\_images values from 0 to 3](https://developers.openai.com/api/docs/guides/image-generation) and can return that many previews during generation. Each partial image adds 100 output tokens. Teams can use these previews for a generation-progress UI; applications that do not need previews can continue using the standard generation and editing flow.

> Even if
>
> `partial_images: 3`
>
> is set, there is no guarantee that exactly three partial images will be received; if the final image is generated quickly enough, the actual number received may be less than the requested amount.

## GPT-Image-2.5 API Parameters

GPT-Image-2.5 exposes more output control than simply choosing a prompt and model.

| Parameter — OpenAI image guide | What it controls | Recommended starting point |
| --- | --- | --- |
| quality | Compute/detail level | medium for development |
| size | Image resolution/aspect | 1024×1024 or 1536×1024 |
| output\_format | PNG, JPEG, WebP | PNG for fidelity; WebP/JPEG for delivery |
| background | Opaque or transparent output | Use transparent only when needed |
| output\_compression | JPEG/WebP compression | Tune for web delivery |
| n | Number of returned images | Start with 1 |
| prompt | Visual requirements | Make layout and constraints explicit |

### Image API vs Responses API

| Criterion | Image API | Responses API |
| --- | --- | --- |
| Best for | Direct one-shot generation and editing | Conversational, multi-step, or agentic image workflows |
| Model selection | Set the image model directly | Use a mainline model plus the image-generation tool |
| Multiple references | Supported for edits, depending on route | Natural fit for several URL or file-ID inputs |
| Iteration | Application resubmits context | Designed for iterative turns and tool calls |
| Streaming previews | Supports partial images | Supports partial images |
| Choose when | You know the desired output and want the shortest request | The model must reason over context, references, or previous results |

**Rule of thumb:** begin with the Image API. Move to the Responses API when the workflow needs conversation state, multiple semantic references, or other tools around image generation.

### Choosing quality

The supported quality ladder is:

| auto  low  medium  high  xhigh  max |
| --- |

auto lets the model decide. For development, however, explicitly choosing medium makes A/B tests more controlled.

A useful deployment pattern is:

| low / medium → drafts, previews, high-volume experimentation  high → approved production assets  xhigh / max → demanding final renders where the quality gain is worth the cost |
| --- |

Do not automatically use max because it is available. More image-output tokens increase cost, and a weak prompt does not become a good prompt merely by increasing quality.

### Choosing image size

The common presets are:

| 1024x1024  1536x1024  1024x1536 |
| --- |

The 2.5 models also support arbitrary valid dimensions, which is useful for banners, product pages, mobile creatives, and other non-square assets. OpenAI?s current specification allows dimensions up to 3840 pixels per edge within its pixel-count and aspect-ratio limits. OpenAI image prompting guide

### Creating transparent images

Use:

| {  "background": "transparent",  "output\_format": "png"  } |
| --- |

or WebP. Transparent output requires a format that supports alpha transparency, so JPEG is not appropriate. Transparent-background requirements

This is especially useful for product cut-outs, UI assets, icons, stickers, and compositing pipelines.

## How to Prompt GPT-Image-2.5

A reliable production prompt separates the creative goal from constraints. Write positive instructions first, then preservation and negative constraints.

### Define Composition

Specify the subject, camera angle, framing, depth, background, and relative position of important objects. Example: “Three-quarter product view, centered, generous negative space on the right, eye-level camera, 50 mm lens look.”

### Describe Lighting and Materials

Name the light direction, softness, contrast, color temperature, and material response. Example: “Large softbox from the upper left, subtle rim light, realistic brushed aluminum, controlled reflections.”

### Control Exact Text

Put required text in quotation marks and specify its position, hierarchy, capitalization, and typography. Ask for no additional text. Example: “Place the exact headline ‘BUILD WITH CLARITY’ at the top center in bold uppercase sans serif. Preserve spelling exactly. Add no other words, letters, labels, or watermarks.”

### State What Must Be Preserved

For editing, name the elements that cannot change: identity, pose, product geometry, logo, label text, proportions, camera angle, or background. Put these constraints before the requested modification.

### Add Negative Constraints

List likely failure modes in plain language: “No extra fingers, no duplicated products, no warped logo, no misspelled text, no border, no watermark.” Negative constraints are most useful when they address specific risks rather than generic quality terms.

## How Much Does GPT-Image-2.5 Cost?

### Official OpenAI API Costs

At the time of verification, both Flare and Sunburst list the same token prices: $5 per million text-input tokens, $1.25 per million cached text-input tokens, $8 per million image-input tokens, $2 per million cached image-input tokens, and $30 per million image-output tokens. The final cost depends on the actual tokens used, not only on the number of requests.

### CometAPI Pricing and Ways to Reduce Cost

CometAPI currently advertises a 20% discount for GPT-Image-2.5 Flare in its model catalog. Treat the dashboard and invoice as the source of truth because gateway pricing can change. To reduce spend, use Flare for routine work, start at `medium` or `high`, reserve `xhigh` or `max` for approved use cases, reuse cached inputs where supported, avoid unnecessary variants, and set `partial_images` to 0 unless previews improve the user experience.

### Other Cost Factors and a Worked Example

Cost is influenced by prompt length, number and resolution of reference images, output dimensions, quality, final output tokens, requested variants, partial previews, retries, and rejected results. Track both spend per request and spend per accepted image.

> Accepted-image cost = total generation spend ÷ number of outputs that pass review.
> Illustrative example: 10 attempts at $0.18 each cost $1.80. If 6 images pass review, the accepted-image cost is $0.30, not $0.18. If better prompting reduces the run to 8 attempts with 6 accepted images, the accepted-image cost falls to $0.24.

## Flare vs. Sunburst: Which Model Should You Use?

The model decision should be workload-driven rather than treating Sunburst as an automatic replacement for Flare.

| Decision | GPT Image 2.5 Flare | GPT Image 2.5 Sunburst |
| --- | --- | --- |
| Interactive application | Recommended | Use selectively |
| Rapid prompt iteration | Recommended | Usually unnecessary |
| High-volume creative generation | Recommended | Depends on acceptance rate |
| Product/reference editing | Good | Recommended |
| Complex final composition | Good | Recommended |
| Maximum editing control | Good | Recommended |
| Latency-sensitive UI | Recommended | Less suitable |
| Premium final asset | Test first | Recommended when quality gain is measurable |

For many products, the optimal architecture is not “choose one forever.” Route most requests to Flare, then send demanding revisions or high-value final outputs to Sunburst.

## How Do You Migrate from GPT Image 2 to GPT-Image-2.5?

If you already use [GPT Image 2](https://www.cometapi.com/models/openai/gpt-image-2/) through CometAPI, migration is comparatively small because generation and editing remain on the Images API routes.

The simplest change is:

| # Before  model="gpt-image-2"    # After: speed-first  model="gpt-image-2.5-flare"    # After: precision-first  model="gpt-image-2.5-sunburst" |
| --- |

But do not stop at swapping the ID. Re-evaluate quality, output dimensions, latency, subject preservation, text correctness, edit locality, and real token usage using a fixed evaluation set.

OpenAI specifically recommends holding the prompt, references, dimensions, and output format constant when comparing models so the model change is the variable being measured. OpenAI migration guidance

## Production Tips for GPT-Image-2.5 in CometAPI

For a production service, keep the implementation around GPT-Image-2.5 deliberately small: store the API key server-side, persist the decoded image in your own storage, log model/quality/size/latency/usage, cap retries, and treat 400 errors differently from transient 429 or 5xx failures.

CometAPI has already published a dedicated guide covering queueing, bounded concurrency, exponential backoff, durable IDs, storage, manifests, and batch cost tracking. Rather than duplicating that implementation here, see [How to Automate Image Generation at Scale](https://www.cometapi.com/automate-image-generation-at-scale-one-api/) when moving from a single API call to batch production.

That distinction is particularly important when adapting examples written for OpenAI’s native API directly to a third-party OpenAI-compatible endpoint.

## Common GPT-Image-2.5 API Errors

| Error | Likely cause | What to do |
| --- | --- | --- |
| 401 Unauthorized | Invalid/missing CometAPI key | Verify COMETAPI\_KEY and Bearer header |
| 400 Bad Request | Invalid parameter, size, format, or model ID | Remove optional fields and test a minimal request |
| 429 Too Many Requests | Concurrency or account limit reached | Back off and retry with jitter |
| Repeated 5xx | Temporary upstream/API issue | Retry a limited number of times |
| Image appears as Base64 text | b64\_json was not decoded | Base64-decode and save the bytes |
| Transparent output fails | Incompatible output format | Use PNG or WebP |
| Edit changes too much | Prompt does not constrain preservation | Explicitly state what must stay unchanged |
| Costs rise unexpectedly | Higher quality/resolution or retries | Log usage per request and calculate accepted-image cost |

Do not retry every failure automatically. A malformed 400 request will generally remain malformed, while retrying an authentication error only generates more failed traffic.

### Rate Limits and Concurrency

| Tier | TPM | IPM |
| --- | --- | --- |
| Tier 1 | 100K | 5 |
| Tier 2 | 250K | 20 |
| Tier 3 | 800K | 50 |
| Tier 4 | 3M | 150 |
| Tier 5 | 8M | 250 |

## Conclusion

GPT-Image-2.5 gives developers a more useful model split than a simple generational upgrade: Flare is optimized for fast everyday image workloads, while Sunburst gives demanding generation and editing workflows a higher-precision option.

Through CometAPI, both can fit into an existing OpenAI-compatible application with minimal integration work. Start with the /v1/images/generations endpoint, Flare, a controlled quality setting, and one representative prompt set. Add /v1/images/edits and Sunburst when your product requires stronger reference preservation or precise visual changes.

The key optimization is not simply selecting the most powerful setting. Measure latency, token usage, acceptance rate, editing accuracy, and effective cost per approved image on the workload your application actually serves. That is what determines whether Flare or Sunburst is the better production model.

## FAQ

### Is GPT-Image-2.5 available on CometAPI?

Yes. Both GPT Image 2.5 Flare and GPT Image 2.5 Sunburst are available through CometAPI.

### Do I need a separate OpenAI API key?

No. When calling the model through CometAPI, authentication uses your CometAPI key against the CometAPI endpoint.

### Should I use Flare or Sunburst?

Start with Flare for most generation workloads. Use Sunburst when editing precision, complex compositions, or preservation of reference-image details has a measurable impact on output acceptance. This follows OpenAI’s own positioning of the two models.

### Can GPT-Image-2.5 edit existing images?

Yes. The current model specifications support image input and image editing, and CometAPI exposes image-editing capability for the family. GPT Image 2.5 Flare API in CometAPI

### Does GPT-Image-2.5 support transparent images?

Yes. Set background to transparent and use PNG or WebP as the output format. OpenAI image prompting guide

### Can I use the OpenAI Python SDK with CometAPI?

Yes. CometAPI’s current examples instantiate the standard OpenAI client with base\_url="`https://api.cometapi.com/v1`" and a CometAPI key. CometAPI SDK example

---

*Originally published at [https://www.cometapi.com/how-to-use-gpt-image-2-5-api-cometapi/](https://www.cometapi.com/how-to-use-gpt-image-2-5-api-cometapi/).*
