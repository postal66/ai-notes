<!-- social-ops-fingerprint:9e1b1ad02e79fd51ba5ae3978fab78efcfae6c44e8f8c766728e56e681b51700 -->
---
title: Qwen 3.8 Max API Pricing: $2 Input, $6 Output, 1M Context
---
# Qwen 3.8 Max API Pricing: $2 Input, $6 Output, 1M Context

![Qwen 3.8 Max API Pricing: $2 Input, $6 Output, 1M Context](https://resource.cometapi.com/qwen-3-8-max-api-pricing.png)

TL;DR Qwen 3.8 Max costs **$2 per 1 million input tokens** and **$6 per 1 million output tokens** on QwenCloud. Model-specific cache rates are **$0.25/M for implicit cached input**, **$2.50/M for explicit cache creation**, and **$0.17/M for explicit cache reads**.

The same standard token rates apply across the model's supported **1M-token context window**. Larger prompts cost more because they contain more tokens, not because they enter a higher long-context pricing tier.

At list price, Qwen 3.8 Max is **20% cheaper than Qwen 3.7 Max**. However, Qwen 3.7 Max is cheaper while its current 50% promotion remains active. The better production choice depends on **cost per accepted task**, including reasoning, cache hits, tools, retries, latency, and human review.

## Qwen 3.8 Max API Pricing at a Glance

| Item | Current official value |
| --- | --- |
| Production model ID | qwen3.8-max |
| Official release date | August 3, 2026 |
| Architecture | 2.4T total parameters; 95B active parameters |
| Standard input price | $2 / 1M tokens |
| Standard output price | $6 / 1M tokens |
| Implicit cached input | $0.25 / 1M tokens |
| Explicit cache creation | $2.50 / 1M tokens |
| Explicit cache read | $0.17 / 1M tokens |
| Context window | 1M tokens |
| Maximum input | 991K without thinking; 983K with thinking |
| Maximum output | 131K |
| Maximum reasoning | 262K |
| Input modalities | Text, image, and video |
| Output modality | Text |
| QwenCloud reference limits | 2M TPM and 15K RPM |

The [QwenCloud model page](https://www.qwencloud.com/models/qwen3.8-max) is the most direct source for the current model ID, pricing, cache rates, context limits, and modalities. Account- and region-specific quotas may differ, so use the limits shown in your own console when setting production concurrency.

The production release also replaces the preview identifier with `qwen3.8-max` and adds a complete model-specific rate card. Qwen's launch materials describe `low`, `medium`, and `xhigh` reasoning-effort settings, but production behavior should be verified against the endpoint and API reference you actually use.

> **Time-sensitive note:** Qwen announced that open weights would follow the API release. As of August 4, 2026, do not describe Qwen 3.8 Max as downloadable or self-hostable until an official checkpoint and license are published.

## How Qwen 3.8 Max Pricing Works

QwenCloud currently lists a flat standard rate of **$2 per 1M input tokens** and **$6 per 1M output tokens** across Qwen 3.8 Max’s supported 1M-token context window. The official pricing snapshot below was captured on August 4, 2026; always check the live model page before making production budget decisions.

![Qwen 3.8 Max API Pricing: $2 Input, $6 Output, 1M Context](https://resource.cometapi.com/%20qwen-3-8-max-pricing%20.png)

***Source***\*\*\*:\*\*\* [QwenCloud, “Qwen3.8-Max” official](https://www.qwencloud.com/models/qwen3.8-max)

| Billing item | Price per 1M tokens | When it applies |
| --- | --- | --- |
| Standard input | $2.00 | New prompt content, tool definitions, and uncached context |
| Standard output | $6.00 | Generated output and billed reasoning usage |
| Implicit cache hit | $0.25 | Automatically reused prompt prefixes; hits are not guaranteed |
| Explicit cache creation | $2.50 | Creating a marked reusable prompt prefix |
| Explicit cache read | $0.17 | Reusing a valid explicit cache block |

A 900K-token request therefore costs more than a 100K-token request because it processes nine times as many input tokens—not because it crosses into a higher price tier.

### Reasoning can increase output cost

A short visible answer is not always a low-cost answer. Reasoning-enabled calls may generate additional reasoning tokens, so production estimates should use the usage fields returned by the API rather than visible response length.

Where your endpoint supports reasoning controls for `qwen3.8-max`, compare the available settings on the same evaluation set. Do not assume that preview defaults carry over to the GA model.

### Cache savings depend on prompt stability

Qwen 3.8 Max's model page publishes model-specific cache rates. Use those rates—not generic cache ratios—when estimating spend.

Explicit cache entries have a five-minute validity period, and a successful hit resets that period. Implicit caching is automatic, but a hit is not guaranteed. Caching is most useful when system prompts, tool definitions, repository context, or large documents remain stable across frequent calls.

### Built-in tools create separate charges

QwenCloud currently lists the following tool fees in addition to token usage:

| Built-in tool | Current fee |
| --- | --- |
| Web Search | $10 / 1K calls |
| Image Search | $8 / 1K calls |
| Web Extractor | Free for a limited time |
| Code Interpreter | Free for a limited time |

Function calling and MCP do not have separate tool fees, but tool descriptions still count as input tokens. Free tool promotions may change, so check the [QwenCloud pricing guide](https://docs.qwencloud.com/developer-guides/getting-started/pricing) before finalizing a production budget.

For example, a request with 20K input tokens, 2K output tokens, and two Web Search calls costs approximately:

```
Input:      20,000 / 1,000,000 × $2  = $0.040
Output:      2,000 / 1,000,000 × $6  = $0.012
Web Search:  2 / 1,000 × $10          = $0.020
Total:                                      $0.072
```

In this example, the two search calls account for about 27.8% of the total request cost.

## Qwen 3.8 Max Real-World Cost Examples

These examples use the current QwenCloud model-specific rates. They exclude taxes, retries, fallbacks, and provider-specific markup.

### Example 1: Medium agent request

```
Assume 50K input tokens and 5K output tokens:
Input:  50,000 / 1,000,000 × $2 = $0.10
Output:  5,000 / 1,000,000 × $6 = $0.03
Total:                                $0.13
```

A successful first attempt costs about **$0.13**. One full retry would raise the model cost to roughly **$0.26**.

### Example 2: Long-document analysis

```
Assume 800K input tokens and 20K output tokens:
Input:  800,000 / 1,000,000 × $2 = $1.60
Output:  20,000 / 1,000,000 × $6 = $0.12
Total:                                  $1.72
```

The model does not apply a separate long-context surcharge on its current rate card, but large prompts still create substantial absolute cost.

### Example 3: Cached agent session

Assume a reusable 100K-token prefix, 10K new input tokens, 5K output tokens, and 50 calls while the explicit cache remains valid:

```
First call:
100K cache creation × $2.50/M = $0.250
10K new input × $2/M          = $0.020
5K output × $6/M              = $0.030
First-call total              = $0.300
Each of the next 49 calls:
100K cache read × $0.17/M     = $0.017
10K new input × $2/M          = $0.020
5K output × $6/M              = $0.030
Per-call total                = $0.067
Cached session total          = $3.583
Same 50 calls without cache   = $12.500
```

Estimated saving = $8.917, or 71.3%

The estimated saving depends on successful cache hits and a stable prefix. Long gaps or frequent changes to system prompts and tool schemas will reduce the benefit.

## Qwen 3.8 Max vs Qwen 3.7 Max：Pricing Comparison

**Qwen 3.8 Max is 20% cheaper than Qwen 3.7 Max at list price, but Qwen 3.7 Max is 37.5% cheaper while its current 50% promotion is active.**

| Model and pricing status | Input / 1M | Output / 1M | Context |
| --- | --- | --- | --- |
| qwen3.8-max standard price | $2.00 | $6.00 | 1M |
| qwen3.7-max list price | $2.50 | $7.50 | 1M |
| qwen3.7-max current promotion | $1.25 | $3.75 | 1M |

Keep the [CometAPI Qwen3.7 Max model page](https://www.cometapi.com/models/aliyun/qwen3-7-max/) available as a fallback while testing the new model.

Price per token is only one part of the decision. Qwen 3.8 Max can still be more economical if it improves first-pass success, uses tools more reliably, reduces retries, or requires less human correction.

Use this production metric:

Cost per accepted task =

(model tokens + tool calls + retries + fallback spend + review cost)

÷ accepted outputs

Vendor-reported benchmark gains are a reason to retest demanding coding and professional workflows, not proof that every Qwen 3.7 workload should migrate.

## How to Migrate to Qwen 3.8 Max

Changing the model string is necessary, but it is not a complete production migration.

### 1. Test the production model ID

Replace the preview identifier with `qwen3.8-max` in a test environment. Do not assume preview aliases, defaults, latency, or response behavior will remain unchanged.

A minimal OpenAI-compatible request can look like this:

```
import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
response = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {
            "role": "user",
            "content": "Review this migration plan and identify production risks.",
        }
    ],
)
```

print(response.choices[0].message.content)

Start with the minimum documented request. Add reasoning controls only when the current API reference for your endpoint explicitly supports them.

### 2. Rebaseline cost and performance telemetry

Record at least:

- input, output, and reasoning tokens
- cache hits and cache-creation tokens
- time to first token and total latency
- tool calls, retries, and fallbacks
- accepted versus rejected outputs
- human correction time

### 3. Retest the interface your application uses

Validate streaming events, multimodal payloads, tool schemas, structured output, finish reasons, usage fields, error handling, and multi-turn behavior. The production model page documents DashScope and OpenAI-compatible access; verify any additional compatibility layer before relying on it.

### 4. Respect the practical context limits

A 1M context window is not the same as a 1M-token user prompt. QwenCloud lists maximum input of 991K without thinking and 983K with thinking. Add a safety margin so the request still has room for output and reasoning.

### 5. Run Qwen 3.7 and Qwen 3.8 side by side

Use identical prompts, tools, validators, retry rules, and datasets. Compare cost per accepted task and latency rather than judging isolated responses by eye.

## How to Evaluate and Route Qwen 3.8 Max

Use real workloads rather than broad benchmark averages.

| Workload | Suggested tasks | Primary acceptance signal |
| --- | --- | --- |
| Repository coding | 4 | Tests pass without human patching |
| Long-document analysis | 3 | Claims are supported by supplied evidence |
| Multimodal analysis | 2 | Relevant image or video details are used correctly |
| Tool-using agents | 3 | Correct tool selection and valid arguments |

```
A practical routing policy is:
Simple, latency-sensitive task
→ Lower-cost Plus model
Existing workload that already meets quality targets
→ Qwen 3.7 Max while its promotion remains attractive
Hard coding, multimodal, or long-horizon task
→ Qwen 3.8 Max
Failed validation
→ One controlled retry, then a tested fallback
```

Use **Qwen 3.8 Max** for difficult repository work, long-horizon agents, multimodal analysis, and workflows where Qwen 3.7 fails acceptance tests. Keep **Qwen 3.7 Max** when the promotion materially lowers cost and the existing model already meets your quality target.

Check the [CometAPI pricing page](https://www.cometapi.com/pricing/) and live routing information before locking thresholds because provider availability and routed pricing can change independently from QwenCloud's direct list price. The [CometAPI Cookbook](https://github.com/cometapi-dev/cometapi-cookbook) can help you build repeatable requests and a consistent evaluation harness.

## FAQ

### How much does the Qwen 3.8 Max API cost?

QwenCloud currently lists Qwen 3.8 Max at **$2 per 1 million input tokens** and **$6 per 1 million output tokens**. Cache usage and built-in tools have separate rates.

### Does Qwen 3.8 Max cost more above 128K tokens?

No separate long-context tier is shown on the current model-specific rate card. Long requests cost more because they contain more tokens, not because they cross into a higher unit-price tier.

### Are Qwen 3.8 Max reasoning tokens billed?

Reasoning can increase generated usage and total cost. Use the reasoning- and output-token fields returned by the endpoint rather than estimating from the visible answer.

### Is Qwen 3.8 Max open source?

Qwen announced that open weights would follow the API release. Do not describe the model as downloadable or self-hostable until an official checkpoint and license are available.

### Should Qwen 3.7 Max users migrate immediately?

Not automatically. Qwen 3.8 Max has a lower standard list price, while Qwen 3.7 Max is cheaper during its current promotion. Migrate when your own quality, latency, cache behavior, and cost-per-accepted-task data support the change.

## Test Qwen 3.8 Max With CometAPI

Use the [CometAPI Quickstart](https://www.cometapi.com/quickstart/) to configure an OpenAI-compatible client. Before sending production traffic, confirm that `qwen3.8-max` is live in your account and verify the routed price displayed there.

Compare it with your Qwen 3.7 baseline using identical prompts, validators, retry policies, and telemetry. This keeps the evaluation focused on the model rather than changes in the test harness.

---

*Originally published at [https://www.cometapi.com/qwen-3-8-max-api-pricing/](https://www.cometapi.com/qwen-3-8-max-api-pricing/).*
