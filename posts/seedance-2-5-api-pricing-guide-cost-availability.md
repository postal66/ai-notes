<!-- social-ops-fingerprint:802459f98053d6582f498288808b2d6582edff6623997183974002b159bb5b74 -->
---
title: Seedance 2.5 API Pricing Guide: Cost & Availability
---
# Seedance 2.5 API Pricing Guide: Cost & Availability

![Seedance 2.5 API Pricing Guide: Cost & Availability](https://resource.cometapi.com/seedance-2-5-api-pricing.png)

## TL;DR

BytePlus lists **Seedance 2.5 API pricing at $10.70 per 1 million tokens for requests without video input and $6.40 per 1 million tokens for requests with video input**. Its published five-second, 16:9 examples cost **$0.514 at 480p** and **$1.156 at 720p** without video input.

## Seedance 2.5 API Pricing at a Glance

| Item | Published information |
| --- | --- |
| Provider | ByteDance Seed / BytePlus ModelArk |
| Official BytePlus model ID | dreamina-seedance-2-5-260628 |
| Rate without video input | $10.70 per 1M tokens |
| Rate with video input | $6.40 per 1M tokens |
| Published output tiers | 480p and 720p |
| Five-second example without video input | $0.514 at 480p; $1.156 at 720p |
| Five-second example with video input | $0.553–$2.152 at 480p; $1.244–$4.838 at 720p |
| Failed-generation billing | BytePlus says only successfully generated videos are charged |
| API status | Pricing and model information are published; broad API access remains unconfirmed |

The token rate is only one part of the bill. Video-input requests use a lower rate, but the input-video duration is also included in estimated token consumption, so the final request can still cost more.

## What Is Seedance 2.5?

Seedance 2.5 is ByteDance Seed’s multimodal video-generation model for longer storytelling, reference-driven creation, and targeted editing. ByteDance says it can generate up to 30 seconds of audio-video content in one pass, use up to 30 image references, 10 video references, and 10 audio references, and support timestamp-level editing and multi-round extensions.

For a broader feature overview, see [What Is Seedance 2.5?](https://www.cometapi.com/what-is-seedance-2-5/). This guide focuses specifically on API pricing, billing, availability, and production budgeting.

AI video API pricing can look straightforward: choose a model, multiply the listed rate by clip length, and estimate the budget. In production, however, resolution changes, retries, rejected generations, and editing time can make the final cost very different from the price of a single attempt.

This guide explains how Seedance 2.5 pricing scales with duration, resolution, and volume, then compares it with Vidu Q3 and Wan 3.0 through CometAPI. It also looks at the costs that appear after generation and offers a practical way to test models, control reruns, and budget by usable output rather than headline price.

## How Seedance 2.5 Billing Works

The current customer model ID is `seedance-2-5`. It supports text-to-video and image-to-video through `POST` `https://api.cometapi.com/v1/videos`. The documented duration range is 4–30 seconds, with 5 seconds as the default. Supported Seedance 2.5 output tiers are 480p and 720p; the exact width and height depend on aspect ratio. For example, 16:9 uses `854x480` or `1280x720`.

This article uses the live per-second rates rather than a token estimate. The basic equation is:

`generation cost = requested seconds × resolution rate`

Volume estimates assume every job finishes once and every result is accepted. They exclude storage, delivery bandwidth, editing, moderation review, and reruns. The final production metric should be cost per accepted clip, not cost per submitted task.

## Seedance 2.5 Cost by Duration and Resolution

The following figures were calculated from the rates in the live [Seedance 2.5 model page](https://www.cometapi.com/models/doubao/seedance-2-5/) and [CometAPI model catalog](https://api.cometapi.com/api/models) on August 27, 2026.

| Duration | 480p at $0.103/s | 720p at $0.231/s |
| --- | --- | --- |
| 4 seconds | $0.41 | $0.92 |
| 5 seconds | $0.52 | $1.16 |
| 10 seconds | $1.03 | $2.31 |
| 15 seconds | $1.55 | $3.47 |
| 30 seconds | $3.09 | $6.93 |

Resolution is the larger lever in this table: at the current rates, 720p costs about 2.24 times as much as 480p for the same duration. For early prompt testing, 480p usually gives the clearer cost signal. Move to 720p only after the composition, motion, and reference handling are stable.

### How Much Do 100 or 1,000 Generations Cost?

At volume, 100 five-second generations cost about $51.50 at 480p or $115.50 at 720p. For 1,000 five-second generations, the same baseline becomes $515 or $1,155. If 10% of those jobs are regenerated, the 100-clip 720p budget rises from $115.50 to $127.05.

## Seedance 2.5 vs Vidu Q3 vs Wan 3.0：API Pricing

The three routes do not expose the same resolution menu. The figures below are current CometAPI-listed rates checked on August 28, 2026 from the [Seedance 2.5](https://www.cometapi.com/models/doubao/seedance-2-5/), [Vidu Q3](https://www.cometapi.com/models/vidu/vidu-q3/), and [Wan 3.0](https://www.cometapi.com/models/aliyun/wan3-0/) model pages. All published rates are billed per generated second. Five-second costs are the listed rate multiplied by five; “not listed” means the current CometAPI route does not publish that exact resolution tier.

### 480p API Pricing: Seedance 2.5 vs Vidu Q3 vs Wan 3.0

| Model | 480p rate | 5-second cost | Availability note |
| --- | --- | --- | --- |
| wan3.0 | USD 0.05/s | USD 0.25 | Native 480p tier |
| seedance-2-5 | USD 0.103/s | USD 0.52 | Native 480p tier |
| viduq3 | Not listed | Not applicable | Lowest published Vidu Q3 tier is 540p |

Wan 3.0 has the lowest like-for-like 480p rate. Vidu Q3 should not be assigned a 480p price: its closest published low-resolution tier is 540p at USD 0.056 per second, or USD 0.28 for five seconds.

### 720p API Pricing: Seedance 2.5 vs Vidu Q3 vs Wan 3.0

| Model | 720p rate | 5-second cost | Availability note |
| --- | --- | --- | --- |
| wan3.0 | USD 0.10/s | USD 0.50 | Native 720p tier |
| viduq3 | USD 0.1232/s | USD 0.62 | Native 720p tier with synchronized audio |
| seedance-2-5 | USD 0.231/s | USD 1.16 | Native 720p tier; 4–30-second output |

At 720p, Wan 3.0 is the lowest-priced of the three on the listed unit rate, followed by Vidu Q3 and Seedance 2.5.

### 1080p API Pricing: Seedance 2.5 vs Vidu Q3 vs Wan 3.0

| Model | 1080p rate | 5-second cost | Availability note |
| --- | --- | --- | --- |
| viduq3 | USD 0.1232/s | USD 0.62 | Native 1080p tier |
| wan3.0 | USD 0.20/s | USD 1.00 | Native 1080p tier |
| seedance-2-5 | Not listed | Not applicable | Current CometAPI pricing lists 480p and 720p only |

At 1080p, Vidu Q3 has the lower published rate of the two routes that currently list this tier. Seedance 2.5 should not be budgeted as a 1080p route until its live CometAPI model page publishes that resolution and rate. Across all tiers, compare cost per accepted clip after retries and post-production rather than choosing on the unit price alone.

## How to Reduce Seedance 2.5 API Costs

### Hidden Costs: Retries, Rejected Clips, and Long Generations

**Retries can turn one clip into two charges.** A polling timeout is not proof that generation failed. Retrieve the existing task before submitting it again; otherwise a client can create a duplicate billable job while the first task is still running.

**Quality rejection is usually the biggest hidden cost.** If only 70 of 100 five-second 720p Seedance clips pass review, the effective generation cost is $115.50 ÷ 70, or about $1.65 per accepted clip. That is more useful than quoting $1.16 per attempt.

**Longer output multiplies both generation and review work.** A 30-second 720p attempt costs $6.93. Repeating the full clip after a problem near the end is much more expensive than validating a short shot first.

**Resolution can be wasted upstream.** Paying for 720p does not help when the prompt, reference image, framing, or motion direction is still changing. It can also increase transfer, storage, review, and post-production costs.

### Reduce Seedance 2.5 API Costs

**Failed and moderated tasks need separate accounting.** Do not assume every terminal failure is free or every HTTP success contains a usable video. Store the task ID, model ID, requested seconds, size, terminal status, reported usage or charge, and rejection reason.

**Set a draft budget before scaling.** Test each shot at 480p and 4–5 seconds, then move to 720p or a longer duration only after motion, composition, and reference handling pass review.

**Track cost per accepted clip.** Record first-pass acceptance, rerun rate, generation time, and editing time for a fixed prompt set. This shows whether Seedance 2.5 earns back its higher per-second rate.

**Route models by shot requirements.** Use a cheaper route for concept tests, then reserve Seedance 2.5 for validated shots that benefit from its longer duration or reference controls. Keep automatic retries bounded and always retrieve the existing task before resubmitting.

## Using Seedance 2.5 Through CometAPI

Every price in this article is a **CometAPI-listed rate checked on August 27, 2026**. CometAPI exposes Seedance 2.5, Vidu Q3, and Wan 3.0 through the same base URL and `POST /v1/videos`, so a team can reuse one API key, authentication layer, queue, polling logic, billing account, and monitoring setup.

Video generation remains asynchronous: save the returned `id` or `task_id`, poll `GET /v1/videos/{id}` until a documented terminal state, and download completed media promptly. The unified workflow makes A/B tests and fallbacks easier, but route-specific sizes, duration limits, input fields, and callback support still need to be verified before production.

## FAQs

## Is Seedance 2.5 the cheapest AI video generation API?

No—not by 720p list price in this comparison. At CometAPI-listed rates checked on August 27, 2026, Wan 3.0 is $0.10/s, Vidu Q3 is $0.1232/s, and Seedance 2.5 is $0.231/s. Seedance 2.5 can still be cost-effective when its 4–30-second range reduces stitching or reruns.

## How much does a five-second Seedance 2.5 video cost?

At the rates checked on August 27, 2026, about $0.52 at 480p or $1.16 at 720p. Multiply the per-second rate by the requested duration, then add a realistic rerun allowance.

## Does Seedance 2.5 support 1080p or 4K?

The current CometAPI Seedance 2.5 route documents 480p and 720p exact sizes. Do not budget for 1080p or 4K unless the live model directory and API schema add those tiers.

## What is the maximum Seedance 2.5 duration?

The current documented range is 4–30 seconds, with 5 seconds as the default when duration is omitted.

## Are failed video tasks billed?

Do not make a universal assumption. Record the terminal status and actual billing data for each route. A network timeout can occur after a task has already been accepted, so retrieve the existing task before resubmitting.

## Which metric should a production team optimize?

Use total API spend divided by accepted clips. Add reviewer and editing time when those costs are meaningful. Per-second price is only the starting point.

---

*Originally published at [https://www.cometapi.com/seedance-2-5-api-pricing/](https://www.cometapi.com/seedance-2-5-api-pricing/).*
