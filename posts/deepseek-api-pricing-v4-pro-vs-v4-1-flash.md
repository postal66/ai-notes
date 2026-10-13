<!-- social-ops-fingerprint:771960c22c0b99c8dea5538eb67bc50262a1fc73afcd70b7801ed3ea8922032e -->
---
title: DeepSeek API Pricing: V4 Pro vs. V4.1 Flash
---
# DeepSeek API Pricing: V4 Pro vs. V4.1 Flash

![DeepSeek API Pricing: V4 Pro vs. V4.1 Flash](https://resource.cometapi.com/1f3fc0e29-c60a-4fc7-8f0b-70d653fe5e1a.png)

## TL;DR

DeepSeek V4 Pro and V4.1 Flash are separate, live API offerings with different prices. The official [Models & Pricing table](https://api-docs.deepseek.com/quick_start/pricing/) identifies **deepseek-v4-pro** as DeepSeek-V4-Pro-0813 and **deepseek-flash** as DeepSeek-V4.1-Flash. DeepSeek's [September 10 update](https://api-docs.deepseek.com/updates/) says it will continue providing V4 Pro API service after September 14 with its billing method unchanged. The earlier claim that V4 Pro requests are routed to Flash and billed at Flash rates is no longer supported by the current official documentation.

## Key Takeaways

- V4.1 Flash costs $0.003/M cache-hit input, $0.15/M uncached input, and $0.60/M output off-peak.
- V4 Pro costs $0.022/M cache-hit input, $0.66/M uncached input, and $1.98/M output off-peak.
- Peak rates are twice the off-peak rates for both models. Chinese public holidays are off-peak for the full day under the official schedule.
- Use **deepseek-flash** for V4.1 Flash and **deepseek-v4-pro** for V4 Pro. Only the retired V4 Flash model names are described as compatibility routes to V4.1 Flash.

## What Are the Current DeepSeek API Prices?

DeepSeek's [current pricing table](https://api-docs.deepseek.com/quick_start/pricing/) lists cache-hit input, cache-miss input, and output separately for each model and time band. The table below reproduces those direct-provider rates; it does not describe third-party pricing.

| Model | Time band | Cache-hit input | Cache-miss input | Output |
| --- | --- | --- | --- | --- |
| V4.1 Flash | Off-peak | $0.003/M | $0.15/M | $0.60/M |
| V4.1 Flash | Peak | $0.006/M | $0.30/M | $1.20/M |
| V4 Pro | Off-peak | $0.022/M | $0.66/M | $1.98/M |
| V4 Pro | Peak | $0.044/M | $1.32/M | $3.96/M |

Peak hours are 01:00–04:00 UTC and 06:00–10:00 UTC, Monday through Friday, excluding Chinese public holidays. In Beijing time, the weekday windows are 09:00–12:00 and 14:00–18:00. Weekends and Chinese public holidays are off-peak throughout the day. Check the official table before budgeting because prices may change.

![DeepSeek API Pricing: V4 Pro vs. V4.1 Flash](https://resource.cometapi.com/12180X1280.JPEG)

*Official DeepSeek V4.1 Flash API pricing. Source:* [*DeepSeek release announcement*](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)*.*

## What Does DeepSeek V4 Pro Cost Now?

DeepSeek's [release update](https://api-docs.deepseek.com/updates/) explicitly says it will continue V4 Pro API service after September 14, 2026, with its billing method unchanged. Its current [model table](https://api-docs.deepseek.com/quick_start/pricing/) lists **deepseek-v4-pro** as DeepSeek-V4-Pro-0813, alongside **deepseek-flash** as DeepSeek-V4.1-Flash. The two names therefore should not be treated as two price labels for the same served model.

| API model name | Model listed by DeepSeek | Billing |
| --- | --- | --- |
| deepseek-flash | DeepSeek-V4.1-Flash | V4.1 Flash rates |
| deepseek-v4-pro | DeepSeek-V4-Pro-0813 | V4 Pro rates |
| deepseek-v4-flash | V4.1 Flash via compatibility routing | V4.1 Flash rates |

The compatibility note applies to the retired **deepseek-v4-flash** and **deepseek-v4-flash-vision-exp** names. The official note does not include **deepseek-v4-pro** in that routing group.

## DeepSeek V4 Pro vs. V4.1 Flash Price

| Price state | Cached input | Uncached input | Output |
| --- | --- | --- | --- |
| Former V4 Pro off-peak | $0.022/M | $0.66/M | $1.98/M |
| V4.1 Flash off-peak | $0.003/M | $0.15/M | $0.60/M |
| Current V4 Pro route off-peak | $0.003/M | $0.15/M | $0.60/M |

For uncached input, V4 Pro's current off-peak $0.66/M rate is 4.4 times Flash's $0.15/M. For output, $1.98/M is 3.3 times Flash's $0.60/M. Flash is about 77.3% cheaper on uncached input and 69.7% cheaper on output for this direct-provider comparison. These percentages compare two concurrently listed models; they are not savings from a V4 Pro route switching to Flash.

The $0.022/M cache-hit input rate for V4 Pro is also current, not merely historical. Flash's $0.003/M cache-hit rate is about 86.4% lower. The official table shows separate model prices at peak as well: V4 Pro is $1.32/M for cache-miss input and $3.96/M for output, while Flash is $0.30/M and $1.20/M.

## What Does the Price Mean for a Real Workload?

Assume a workload uses 10 million uncached input tokens and 2 million output tokens. At today’s direct-provider rates:

| Model | Off-peak cost | Peak cost |
| --- | --- | --- |
| deepseek-flash | $2.70 | $5.40 |
| deepseek-v4-pro | $10.56 | $21.12 |

The off-peak calculations are 10 × $0.15 + 2 × $0.60 = $2.70 for Flash, and 10 × $0.66 + 2 × $1.98 = $10.56 for V4 Pro. Peak totals double under the current time-band rates.

Caching can reduce the current bill further. If 80% of the 10 million input tokens hit cache, the off-peak calculation becomes $0.024 for cached input, $0.30 for uncached input, and $1.20 for output, for a total of **$1.524** on V4.1 Flash. For the same token mix on V4 Pro, the total is $0.176 + $1.32 + $3.96 = $5.456.

## How Has DeepSeek API Availability Changed?

V4.1 Flash is available through the official DeepSeek API under the model name **deepseek-flash**. The previous V4 Flash and V4 Flash Vision Exp models have been retired, although their legacy IDs are temporarily accepted and routed to V4.1 Flash.

V4 Pro remains available under **deepseek-v4-pro**. DeepSeek says its billing method remains unchanged and will provide further notice if that changes. Do not infer a V4 Pro retirement or a Flash migration from the retirement of the older V4 Flash names.

[CometAPI's changelog](https://www.cometapi.com/changelog/) lists DeepSeek Flash and V4.1 Flash. Its [V4.1 Flash model page](https://www.cometapi.com/models/deepseek/deepseek-v4-1-flash/) currently displays a starting price of $0.12/M input tokens, with separate request-time adjustments. That is CometAPI pricing, not DeepSeek's direct-API rate; check the live checkout terms for a specific workload.

## What Could DeepSeek V4.1 Pro Cost?

DeepSeek has confirmed a future V4.1 Pro release, but no official price has been published. Any precise number presented today would be speculation. A safer planning method is to model several premiums over the live V4.1 Flash price.

| Planning scenario | Off-peak uncached input | Off-peak output | 10M input + 2M output |
| --- | --- | --- | --- |
| 2× Flash | $0.30/M | $1.20/M | $5.40 |
| 3× Flash | $0.45/M | $1.80/M | $8.10 |
| 4× Flash | $0.60/M | $2.40/M | $10.80 |

> These are budgeting scenarios, not leaked or official V4.1 Pro prices. They assume DeepSeek preserves the current peak/off-peak structure and applies a 2×–4× premium over Flash. The company may choose a different ratio, caching rate, launch promotion, or billing design.

The historical V4 Pro price provides a useful ceiling reference: its $0.66/M uncached input and $1.98/M output sat approximately 4.4× and 3.3× above the new V4.1 Flash off-peak rates. That makes a 2×–4× scenario band reasonable for internal budgeting, but it does not predict DeepSeek’s final decision.

## How Should Teams Control DeepSeek API Cost?

- **Choose the intended model.** Use deepseek-flash for V4.1 Flash or deepseek-v4-pro for the separately listed V4 Pro model.
- **Schedule flexible work off-peak.**The listed peak token rates are twice the off-peak rates; account for the Chinese public-holiday exception.
- **Preserve reusable prompt prefixes.** Cache-hit input is 50× cheaper than uncached input at the current Flash rate.
- **Track output length.** Output remains the largest component in many agent workloads.
- **Verify the live price table.** Recheck both model columns and third-party terms before committing a production budget.

## FAQ

### How much does DeepSeek V4.1 Flash cost?

Official off-peak pricing is $0.003/M cache-hit input, $0.15/M uncached input, and $0.60/M output. Peak rates are $0.006/M, $0.30/M, and $1.20/M.

### Is DeepSeek V4 Pro still available at its own price?

Yes. DeepSeek says it will continue V4 Pro API service with unchanged billing. Its pricing table lists $0.022/M cache-hit input, $0.66/M cache-miss input, and $1.98/M output off-peak; peak rates are $0.044/M, $1.32/M, and $3.96/M.

### Are V4 Pro and V4.1 Flash currently the same price?

No. The official table lists them as distinct models with distinct direct-API rates. The old Flash compatibility names route to V4.1 Flash; V4 Pro is not included in that note.

### Has DeepSeek published a V4.1 Pro price?

No V4.1 Pro price appears in the current official model and price table. Do not substitute the V4 Pro price for an unlisted future model.

### Can I use DeepSeek V4.1 Flash through CometAPI?

Yes. CometAPI supports deepseek-flash and deepseek-v4.1-flash through its Chat API format. Its displayed price and time adjustments are separate from DeepSeek's direct-API billing.

## Conclusion

The central comparison is between two live DeepSeek API models. V4.1 Flash starts at $0.15/M uncached input and $0.60/M output off-peak. V4 Pro remains listed at $0.66/M and $1.98/M, respectively. The routes do not share an official price: choose the model for its capabilities, then calculate costs using that model's cache and time-band rates.

Before publishing or budgeting, verify the [live DeepSeek price table](https://api-docs.deepseek.com/quick_start/pricing/) and [release updates](https://api-docs.deepseek.com/updates/). Third-party offers should be checked on their own pricing pages.

## SEO Metadata

**Meta title:** DeepSeek API Pricing: V4 Pro vs. V4.1 Flash

**Meta description:** Compare current DeepSeek V4 Pro and V4.1 Flash API rates, model IDs, peak and off-peak prices, cache savings, and real workload costs.

**Keywords:** DeepSeek API price, DeepSeek V4 Pro price, DeepSeek V4.1 Flash price, DeepSeek API pricing, V4 Pro vs V4.1 Flash, DeepSeek V4.1 Pro price

**URL slug:** deepseek-api-price-v4-pro-vs-v4-1-flash

---

*Originally published at [https://www.cometapi.com/deepseek-api-price-v4-pro-vs-v4-1-flash/](https://www.cometapi.com/deepseek-api-price-v4-pro-vs-v4-1-flash/).*
