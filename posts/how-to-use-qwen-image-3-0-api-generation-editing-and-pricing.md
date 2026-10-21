<!-- social-ops-fingerprint:11da108dc5d26d50deffcbfbe31ecfd80b3f173bc7e9549d843c1df186f93ce2 -->
---
title: How to Use Qwen Image 3.0 API: Generation, Editing, and Pricing
---
# How to Use Qwen Image 3.0 API: Generation, Editing, and Pricing

![How to Use Qwen Image 3.0 API: Generation, Editing, and Pricing](https://resource.cometapi.com/How%20to%20Use%20Qwen%20Image%203.0.webp)

## TL;DR

Qwen Image 3.0 unifies text-to-image generation and reference-guided editing under the Standard (qwen-image-3.0) and Pro (qwen-image-3.0-pro) variants. Start with a text prompt, choose an output size, submit an image-generation request, and promptly save the output. For editing, include one to three reference images and an explicit preservation instruction. On CometAPI, verify the actual route and compatible request schema before deploying the sample calls.

## Key Takeaways

- The Qwen Image 3.0 API supports text-to-image generation and reference-guided editing through Standard (qwen-image-3.0) and Pro (qwen-image-3.0-pro); native output is PNG.
- Qwen Image 3.0 API access is available through [CometAPI](https://www.cometapi.com/models/aliyun/qwen-image-3-0/). Developers can obtain an API key, verify the supported endpoint, and integrate image generation into their applications.
- Qwen Image 3.0 API pricing starts at $0.024/request on CometAPI, compared with Alibaba Cloud Singapore rates starting at $0.030 per Standard output image and $0.040 per Pro 1K output image.
- Qwen Image 3.0 image editing supports up to three reference images through the native Alibaba Cloud API, while generation supports one to six outputs per request.
- Qwen Image 3.0 API integration requires developers to verify provider-specific parameters, authentication, billing units, and temporary image URLs before deploying production workflows.

## What Is the Qwen Image 3.0 API?

The Qwen Image 3.0 API turns text instructions into images and can transform supplied photographs or design assets. Supported scenarios include multilingual posters, e-commerce photography, campaign mockups, background replacement, and composite-image editing.

**Qwen Image 3.0 Standard (qwen-image-3.0)** is the cost-focused baseline for text-to-image generation and reference-guided editing. Consider it first for high-volume workflows such as e-commerce background variations, social-media visual drafts, and campaign concept exploration. For example, use Standard to produce several product-background options, then review product fidelity and select the versions worth refining.

**Qwen Image 3.0 Pro (qwen-image-3.0-pro)** supports generation and reference-guided editing, with a higher-priced native 2K output tier. Evaluate it for quality-sensitive deliverables such as campaign hero images, detailed product compositions, and promotional posters. For example, test a shortlisted concept with Pro when fine detail or layout matters, and compare the accepted results with Standard before committing the larger budget.

**How to choose:** Start with Standard for cost-sensitive drafts and variations. Test Pro on the same brief for demanding final assets; select it when the measured improvement justifies the additional cost. Neither designation substitutes for application-specific testing of typography, product fidelity, object count, or layout accuracy.

| Specification | Qwen Image 3.0 | Qwen Image 3.0 Pro |
| --- | --- | --- |
| Model ID | qwen-image-3.0 | qwen-image-3.0-pro |
| Generation / editing | Both | Both |
| Reference images for editing | 1–3 | 1–3 |
| Generated images per request | 1–6 | 1–6 |
| Output format | PNG | PNG |
| Output pixel area | 512²–2048² | 512²–2048² |
| Recommended prompt length | 4,500 tokens | 4,500 tokens |
| Primary selection rationale | Cost-efficient throughput | Premium output evaluation |

## What Parameters Does Qwen Image 3.0 API Support?

Use these parameters with Alibaba Cloud’s native OpenAI-compatible interface. Add provider-specific options to CometAPI requests only when the selected route documents them.

Applies to both variants: qwen-image-3.0 (Standard) and qwen-image-3.0-pro (Pro) support the same parameters listed below on Alibaba Cloud's native OpenAI-compatible interface. Select the variant with model; the generation and editing controls are shared. This does not imply identical output quality or pricing, or guarantee that every CometAPI route exposes all native parameters.

| Parameter | Type / example | Purpose |
| --- | --- | --- |
| model | qwen-image-3.0 | Choose Standard or Pro |
| prompt | string | Instruction and content |
| image | URL / base64 string or array | 1–3 references for editing; omit for generation |
| size | 1024x1024 | Output dimensions; auto where supported |
| n | integer 1–6 | Outputs per call |
| negative\_prompt | string | Describe what to avoid |
| prompt\_extend | boolean | Enable prompt rewriting |
| prompt\_extend\_mode | direct / agent | Agent mode is T2I only |
| enable\_thinking | boolean | Reasoning control, subject to enhancement settings |
| watermark | boolean | Optional watermark |
| seed | integer | Reproducibility aid |

For native requests, output aspect ratio must stay between 1:8 and 8:1. Reference images must be at most 10 MB, with each side between 1 and 8,000 pixels and a longest-to-shortest-side ratio no greater than 10:1. Use a data URI for Base64 input. Thinking requires prompt\_extend=true; agent enhancement supports text-to-image only.

A compatible image request places generation fields at the JSON top level and formats dimensions as 1024x1024. Native DashScope uses nested input/parameters and commonly writes dimensions as 1024\*1024. A request copied between these endpoints without conversion can fail.

## How Do You Call Qwen Image 3.0 API with CometAPI?

This walkthrough assumes Python 3, a Bash-compatible terminal, a CometAPI account with model access, and sufficient balance. The first request uses only the model and prompt fields shown in the provider example. Documentation checked on October 16, 2026; these examples have not been executed against a paid account.

### Create credentials

Create a server-side API key in your CometAPI dashboard. Never ship it in a web or mobile client.

```
export COMETAPI_KEY="your_api_key"python -m pip install requests
```

### Submit a minimal generation request

Developers can access Qwen Image 3.0 API in CometAPI using the documented image-generation route. Begin with the minimal request below before introducing optional parameters.

```
curl --fail-with-body https://api.cometapi.com/v1/images/generations \  -H "Authorization: Bearer $COMETAPI_KEY" \  -H "Content-Type: application/json" \  -d '{"model":"qwen-image-3.0","prompt":"Premium skincare bottle on a stone pedestal, gentle studio lighting"}'
```

### Save every returned image

Save the following script as generate.py and run python generate.py. It submits a request, handles URL or Base64 image results, and writes each image locally. If the response contains task information instead of a data array, it stops rather than guessing a polling endpoint; use the account-specific asynchronous contract to retrieve the completed result.

```
import base64import osfrom pathlib import Pathimport requests​response = requests.post(    "https://api.cometapi.com/v1/images/generations",    headers={"Authorization": f"Bearer {os.environ['COMETAPI_KEY']}"},    json={"model": "qwen-image-3.0", "prompt": "A sunny bookstore cafe, editorial photograph"},    timeout=(15, 600),)response.raise_for_status()result = response.json()images = result.get("data")if not isinstance(images, list) or not images:    raise RuntimeError(f"No synchronous images; inspect task/error fields: {list(result)}")for index, item in enumerate(images, 1):    if item.get("url"):        download = requests.get(item["url"], timeout=(15, 120))        download.raise_for_status()        content = download.content    elif item.get("b64_json"):        content = base64.b64decode(item["b64_json"], validate=True)    else:        raise RuntimeError(f"Image {index} has no URL or Base64 payload")    path = Path(f"qwen_image_{index}.png")    path.write_bytes(content)    print(f"Saved {path}")
```

A successful run produces local image files. Open them to confirm they are readable and match the requested scene. Preserve the request identifier and usage fields in your server logs without logging credentials.

## How Do You Generate Multiple Images with Qwen Image 3.0?

On Alibaba Cloud’s native interface, set n to two through six for creative variations. For CometAPI, enable n only after confirming support on your selected route. Validate each returned asset separately; a larger n does not guarantee every result passes downstream review.

You can generate up to 6 images in a single request with Qwen Image 3.0 by setting the `n` parameter. This works with both `qwen-image-3.0` and `qwen-image-3.0-pro`, for text-to-image generation and image editing. The default is just one image.

There are two main ways to do it: use a graphical interface if your platform exposes the option, or call the API directly.

### Generate multiple images using the API

1. Open the API documentation.
2. Get an API key from the QwenCloud console/ CometAPI.
3. Select `qwen-image-3.0` or `qwen-image-3.0-pro`.
4. Set `n` to the number of images you want, from `1` to `6`.
5. Submit your prompt and save the returned images.

For example, set `"n": 4` to request four variations of the same prompt.

### Python example

Here's a ready-to-adapt example using the OpenAI-compatible API.

```
from openai import OpenAIimport requestsclient = OpenAI(    api_key="YOUR_QWEN_API_KEY",    base_url="https://maas.qwencloudapi.com/compatible-mode/v1")
result = client.images.generate(    model="qwen-image-3.0-pro",  
prompt=(        "A cozy Japanese cafe on a rainy evening, "        "warm glowing lights, cinematic photography, "        "rich details, realistic reflections"    ),  
n=4,  
size="1024x1024")# Save each generated image
for i, item in enumerate(result.data, start=1):    response = requests.get(item.url)    response.raise_for_status()    with open(f"qwen_image_{i}.png", "wb")
as f:      
f.write(response.content)print("Finished generating images!")
```

Install the required packages first:

```
pip install openai requests
```

The API returns an image URL for each result. Generated image URLs are temporary, so download the images promptly.

### Important settings

| Parameter | What it does |
| --- | --- |
| n=4 | Generates four output images |
| model="qwen-image-3.0-pro" | Selects the Pro model |
| size="1024x1024" | Requests square images |
| seed=12345 | Helps make results more reproducible |
| negative\_prompt | Excludes unwanted visual elements |

The maximum output count is six per request. Keep in mind that requesting more images increases generation cost.

One important distinction: `n=4` requests four variations of one prompt. If you want four different prompts, you should make separate requests or automate a loop over your prompts.

## How Do You Edit Images with Qwen Image 3.0?

An edit combines one to three image references with instructions. Explain both the desired transformation and what must not change—for example the product label, color, camera angle, or packaging geometry.

The next example uses Alibaba Cloud credentials and its [JSON image field for editing](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference). Create a regional Model Studio key, obtain your workspace ID, and configure the matching endpoint. Do not substitute a CometAPI key into this request.

```
export DASHSCOPE_API_KEY="your_model_studio_key"export ALIBABA_WORKSPACE_ID="your_workspace_id"export ALIBABA_IMAGE_ENDPOINT="https://${ALIBABA_WORKSPACE_ID}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/images/generations"
```

The reference image below comes directly from the official API example. It is an input image, not a generated result from this article.

```
import os, requests
endpoint = os.environ["ALIBABA_IMAGE_ENDPOINT"]  
# documented regional .../images/generations endpoint
payload = {
"model": "qwen-image-3.0",
"prompt": "Change the outfit to a charcoal business suit in a cafe. Preserve the face and hairstyle.",
"image": ["https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/yBRq1ZPYEaXdyOdv/img/33a80a19-7ac7-4c64-b0fa-7d685b7046a0.png"],
"size": "1024x1024",
"n": 1}
r = requests.post(endpoint, headers={
"Authorization": f"Bearer {os.environ['DASHSCOPE_API_KEY']}"}, json=payload, timeout=(15, 600))
r.raise_for_status()
print(r.json())
```

The native compatible endpoint uses JSON on /images/generations, not multipart uploads on /images/edits. It does not support masks or streaming. Read the returned data array and save each URL using the same download loop shown above.

For two references, include two URLs in the image array and specify their roles in the prompt (e.g., product from image one, room setting from image two). The Qwen Image 3.0 series accepts no more than three reference images; use a different model or preprocessing workflow for larger source sets.

## How Much Does Qwen Image 3.0 API Cost?

Qwen Image 3.0 API pricing varies by model variant, output resolution, and provider. The table below supplements the original Alibaba Cloud Singapore comparison with the CometAPI rates shown in the reviewer's attached pricing table. The attachment lists output prices in USD per image and a 20% discount for all four model/resolution combinations. These supplied rates have not been independently revalidated against live account billing; confirm the applicable rate card before production use.

| Pricing item | Alibaba Cloud Standard | Alibaba Cloud Pro | CometAPI |
| --- | --- | --- | --- |
| Input reference image | $0.003/image | $0.003/image | $0.0024/image for Standard and Pro |
| Successful 1K output | $0.030/image | $0.040/image | Standard: $0.0240/image; Pro: $0.0320/image |
| Successful 2K output | $0.030/image | $0.075/image | Standard: $0.0240/image; Pro: $0.0600/image |
| 100 successful 1K outputs | $3.00 | $4.00 | Standard: $2.40; Pro: $3.20 for 100 output images\* |
| 1,000 successful 2K outputs | $30.00 | $75.00 | Standard: $24.00; Pro: $60.00 for 1,000 output images\* |
| Billing unit | Input/output image | Input/output image | Per billable input reference image and successful output image, according to the supplied pricing table |
| CometAPI output-price discount | 20% at 1K and 2K | 20% at 1K and 2K | Input and output rates are 80% of the corresponding official image prices in the supplied table |

*\*The volume examples above cover output images only: 100 Standard 1K images cost $2.40 and 100 Pro 1K images cost $3.20; 1,000 Standard 2K images cost $24.00 and 1,000 Pro 2K images cost $60.00. For editing, add $0.0024 per billable input reference image. Failed-job rules, taxes, and account-specific adjustments are excluded.*

Using the supplied input and output image rates, estimate image charges for either provider as follows:

**Total cost = (billable reference images × input-image price) + (successful outputs × output-image price).**

For a job billed for two input reference images and three successful Standard 1K outputs, Alibaba Cloud image charges are (2 × $0.0030) + (3 × $0.0300) = $0.0960. The corresponding CometAPI image charges are (2 × $0.0024) + (3 × $0.0240) = $0.0768, based on the supplied rates.

CometAPI charges $0.0024 per input reference image for both variants. Output prices are $0.0240 per Standard image at 1K or 2K, $0.0320 per Pro image at 1K, and $0.0600 per Pro image at 2K. The supplied table lists each input and output rate at 20% below its corresponding official rate. For the same billable image counts, these image charges are therefore 20% lower; additional fees or account terms may change the final invoice.

For production budgeting, verify the selected variant, image resolution, reference-image charges, number of outputs per request, and applicable account discounts before estimating total usage costs.

## How Do You Handle Qwen Image 3.0 API Errors?

| Symptom | Likely cause | Action |
| --- | --- | --- |
| 401/403 | Invalid key or wrong region | Check credential, permissions, and deployment location |
| 400 invalid image | Wrong number/type of references | Use 1–3 images, valid URL/base64, supported formats |
| 400 invalid size | Unsupported area/aspect ratio or separator | Normalize dimensions for endpoint |
| Unexpected JSON | Wrong endpoint or response contract | Log response fields and adapt parser |
| Expired image URL | Image not saved before expiry | Download and store as soon as produced |
| Unexpected bill | Reference images or output tier not accounted | Use image usage fields and current rate card |
| Inconsistent brand text | Generative limitations | Use review gates or postproduction text overlay |

## FAQ

### Should I retry a Qwen Image 3.0 request after a timeout?

A client timeout does not prove that generation stopped. Preserve any request or task identifier, check the provider's job history or documented status API, and determine whether output already exists before resubmitting. Blind retries can create duplicate jobs and additional charges. Use bounded retries for transient failures and follow the provider's idempotency guidance where available.

### How can I use local reference images with Qwen Image 3.0?

For the native compatible interface, read the file as bytes, Base64-encode it, and prepend a data URI such as data:image/png;base64,. Put that complete string in image. Base64 input still has to meet the image size and dimension limits; a local filesystem path is not a URL the service can fetch.

### How do I pass Qwen-specific options through an OpenAI SDK?

Keep standard image fields in their usual SDK arguments and put Model Studio extension fields, such as image and prompt\_extend, inside extra\_body. Raw HTTP requests place these fields directly at the JSON top level. This guidance applies to the native compatible interface; check the selected CometAPI route before forwarding provider-specific options.

### What should I do when Qwen Image 3.0 returns fewer images than requested?

Save the successful outputs first and record the actual count. For native Alibaba Cloud billing, output charges follow successfully generated images. If additional assets are needed, request only the missing quantity after checking the response and usage record; CometAPI billing must be reconciled against its own account terms.

## Conclusion

Qwen Image 3.0 is a practical choice for teams that need generation and reference-driven edits within one model family. Use Standard for a cost-focused baseline, test Pro for more demanding 2K or creative tasks, and measure accepted-output cost instead of judging by per-request price alone. Start with the minimal generation call, persist its outputs, and then add editing or multiple outputs through the appropriate provider contract. Keep credentials and request schemas separate, handle errors explicitly, and reconcile image usage with the selected rate card.

---

*Originally published at [https://www.cometapi.com/how-to-use-qwen-image-3-0-api/](https://www.cometapi.com/how-to-use-qwen-image-3-0-api/).*
