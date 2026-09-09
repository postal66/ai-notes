<!-- social-ops-fingerprint:48249fbef3625ba4e3a389f01c0175858804172e15b024bd33b853252ef6fb30 -->
---
title: Kimi K3 API Pricing (2026): What it Costs & K2.7 Code Comparison
---
# Kimi K3 API Pricing (2026): What it Costs & K2.7 Code Comparison

![Kimi K3 API Pricing (2026): What it Costs & K2.7 Code Comparison](https://resource.cometapi.com/kimi-k3-api-pricing.png)

## TL;DR

Kimi K3 costs **$0.30 per 1M cache-hit input tokens, $3.00 per 1M cache-miss input tokens, and $15.00 per 1M output tokens**, with a **1,048,576-token** **context window**.

Compared with K2.7 Code, K3 is significantly more expensive per token, but offers 4× the context window plus native vision and stronger support for long-horizon agentic workloads.

> **Bottom line:** K2.7 Code remains the more economical choice for routine coding tasks within 256K context. Use K3 when you need larger context, multimodal capabilities, or as an escalation route for tasks that K2.7 cannot complete reliably.

## Kimi K3 API Pricing at a Glance

| Item | Kimi K3 |
| --- | --- |
| API model ID | kimi-k3 |
| Cache-hit input | $0.30 / 1M tokens |
| Cache-miss input | $3.00 / 1M tokens |
| Output | $15.00 / 1M tokens |
| Context window | 1,048,576 tokens |
| Reasoning | Always enabled |
| Supported reasoning effort | max only |
| Default maximum completion | 131,072 tokens |
| Configurable maximum completion | Up to 1,048,576 tokens, subject to the total context limit |
| Key capabilities | Native vision, tool calls, structured output, Partial Mode, dynamic tool loading, automatic context caching |
| Batch API | K3 is not currently listed among supported Batch models |

See Moonshot's [Kimi K3 quickstart](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart) for current API parameters and integration details.

## What Kimi K3 Adds Over K2.7 Code

The most obvious upgrade is context length.

K2.7 Code supports 262,144 tokens, while K3 increases that limit to **1,048,576 tokens**. This makes K3 more practical for large repositories, long agent histories, extensive documentation, and workflows that would otherwise require context reduction.

K3 also supports:

- native visual understanding
- strict structured output
- `tool_choice`
- dynamic tool loading
- automatic context caching
- long-running coding and knowledge-work workflows

Moonshot's [Kimi K3 technical blog](https://www.kimi.com/blog/kimi-k3) reports 88.3 on Terminal-Bench 2.1, 77.8 on Program Bench, and 81.2 on FrontierSWE.

These are provider-reported benchmarks and should be treated as reasons to evaluate K3—not guarantees that it will outperform K2.7 Code on every production workload.

For background on the previous generation, see CometAPI's [Kimi K2 API guide](https://www.cometapi.com/kimi-k2-api/).

## Kimi K3 vs Kimi K2.7 Code Pricing

| Model | Cache-hit input | Cache-miss input | Output | Context |
| --- | --- | --- | --- | --- |
| kimi-k3 | $0.30 / 1M | $3.00 / 1M | $15.00 / 1M | 1,048,576 |
| kimi-k2.7-code | $0.19 / 1M | $0.95 / 1M | $4.00 / 1M | 262,144 |
| kimi-k2.7-code-highspeed | $0.38 / 1M | $1.90 / 1M | $8.00 / 1M | 262,144 |

The K2.7 rates come from Moonshot's [official Kimi K2.7 Code pricing documentation](https://platform.kimi.ai/docs/pricing/chat-k27-code).

Compared with standard K2.7 Code, K3 is:

- **1.58× the price** for cache-hit input
- **3.16× the price** for cache-miss input
- **3.75× the price** for output

K3's premium is smaller relative to K2.7 Code HighSpeed, but the two models target different priorities: HighSpeed focuses on faster coding output, while K3 is aimed at more demanding long-context and agentic workloads.

Moonshot's current [Batch API pricing documentation](https://platform.kimi.ai/docs/pricing/batch) does not list K3, so do not assume Batch discounts available to other Kimi models also apply here.

## Kimi K3 Context Caching: How the 90% Input Discount Works

K3 supports automatic context caching.

Developers do not need to manually create a cache ID or TTL. Keeping large prefixes stable across repeated requests gives subsequent requests an opportunity to receive the cache-hit rate.

The price difference is:

- Cache miss: **$3.00 / 1M input tokens**
- Cache hit: **$0.30 / 1M input tokens**

So cache-hit input tokens cost **90% less** than cache-miss input tokens.

However, output remains priced at $15 per million tokens, so the total request cost does not fall by 90%.

For example, assume:

- 600,000 input tokens
- 20,000 output tokens

| Cache state | Input cost | Output cost | Total |
| --- | --- | --- | --- |
| All input cache miss | $1.80 | $0.30 | $2.10 |
| All input cache hit | $0.18 | $0.30 | $0.48 |

In this simplified case, the total cost falls by about **77%**.

Actual savings depend on the share of input tokens that receive the cache-hit rate.

## Example: What a Coding Task Costs on K3 vs K2.7

Assume a coding task uses:

- 200,000 input tokens
- 20,000 output tokens

| Route | Cold total | Fully cached total |
| --- | --- | --- |
| kimi-k3 | $0.90 | $0.36 |
| kimi-k2.7-code | $0.27 | $0.12 |
| kimi-k2.7-code-highspeed | $0.54 | $0.24 |

For this workload, K3 costs about 3.33× as much as standard K2.7 Code on a cold request.

Within K3 itself, moving from entirely cache-miss input to fully cached input reduces the estimated request cost from **$0.90 to $0.36**, a 60% reduction in this example.

But per-request cost is only part of the equation.

> **Cost per Successful Task = Total Workflow Spend ÷ Tasks That Pass Acceptance Checks**

A production comparison should also include retries, fallback calls, tool executions, and human review time.

A K3 request that succeeds once can be more economical than several cheaper attempts that fail.

## A Real-World Edge Case: Reasoning Token Cost

K3 always uses reasoning, so output-token consumption can become a meaningful part of the bill.

In a [launch-day test by Simon Willison](https://simonwillison.net/2026/Jul/16/kimi-k3/), a prompt asking K3 to generate an SVG consumed 13,241 reasoning tokens before producing 3,417 response tokens, for a total cost of approximately $0.25.

This was an informal single-prompt test rather than a benchmark, but it highlights an important cost consideration: the visible final answer may represent only part of the billed output.

Because K3 currently supports only maximum reasoning effort, teams should measure actual output-token usage on their own workloads.

## A Better Default: K2.7 First, K3 on Escalation

For mixed coding workloads, routing can be more economical than sending every request directly to K3.

A simple strategy is:

```
Start with K2.7 Code
        ↓
Task exceeds 256K context?
        → Yes: use K3
        ↓ No
Run task and validation
        ↓
Validation failed?
        → Yes: escalate to K3
        ↓ No
Return result
```

Using the previous example:

- K2.7 Code costs $0.27 per cold attempt
- K3 costs $0.90
- K2.7 successfully completes 70% of tasks
- 30% are retried once on K3

The average cost becomes:

```
$0.27 + (30% × $0.90) = $0.54 per task
```

Sending every task directly to K3 would cost $0.90 per task under the same token assumptions.

That makes the routed strategy **40% cheaper** in this simplified scenario.

The exact savings will vary, but the principle is useful: route routine work to the cheaper model and escalate when additional capability is actually needed.

## When Is Kimi K3 Worth the Upgrade?

K3 is most compelling when:

- The required context exceeds K2.7 Code's 262,144-token limit.
- The task combines code with visual input.
- A long-running agent needs to work across large repositories and external tools.
- K2.7 requires frequent retries or fallback calls.
- The task is valuable enough that completion quality matters more than minimizing the first-call cost.

K2.7 Code remains a strong option for repetitive, well-scoped coding tasks that already achieve a high success rate within 256K context.

For latency-sensitive coding applications, K2.7 Code HighSpeed should also be tested separately.

## Migrating from K2.7 to K3: Five Engineering Checks

1. ### K3 Reasoning Cannot Currently Be Reduced

K3 always reasons, and the current API supports only:

```
reasoning_effort="max"
```

Because `max` is the default, the parameter can also be omitted.

2. ### Remove K2-Specific `thinking` Parameters

Do not use the K2.x `thinking` parameter with K3.

Use the top-level `reasoning_effort` field instead.

3. ### Omit Fixed Sampling Parameters

K3 currently uses fixed values for parameters including:

```
temperature=1.0
top_p=0.95
n=1
presence_penalty=0
frequency_penalty=0
```

Moonshot recommends omitting these fields rather than overriding them.

4. ### Preserve Complete Assistant Messages

For multi-turn conversations and tool-calling loops, pass the complete assistant message into the next request rather than retaining only the visible `content`.

5. ### Validate Vision and Search Before Production

K3's current vision API does not support public image URLs directly. Use a supported image format such as base64 data or Moonshot's file-reference mechanism.

Moonshot also advises against relying on its current Web Search functionality for near-term production use while the feature is being updated.

## Kimi K3 API Example in Python

K3 can be called through an OpenAI-compatible API interface:

```
from openai import OpenAI

client = OpenAI(
    base_url="YOUR_OPENAI_COMPATIBLE_BASE_URL",
    api_key="YOUR_API_KEY",
)

response = client.chat.completions.create(
    model="kimi-k3",
    messages=[
        {
            "role": "system",
            "content": "You are an expert software engineer.",
        },
        {
            "role": "user",
            "content": "Analyze this repository logic and identify potential issues.",
        },
    ],
    reasoning_effort="max",  # Optional while "max" is the default
)

assistant_message = response.choices[0].message
print(assistant_message)
```

Avoid overriding K3's fixed sampling parameters. For multi-turn and tool-calling workflows, preserve the complete assistant message.

## How to Evaluate Kimi K3 Before Upgrading

Test K3 on real workloads rather than benchmark prompts alone.

A practical evaluation set might include:

- routine repository edits
- tasks close to the 256K context limit
- tasks that exceed 256K
- visual engineering tasks
- long-horizon agentic or knowledge-work tasks

Compare K3, K2.7 Code, and K2.7 Code HighSpeed where applicable.

Track:

- task success rate
- cached and uncached input tokens
- output and reasoning tokens
- retries and fallback calls
- p50 and p95 latency
- tool-call errors
- human review time
- cost per successful task

Then compare three policies:

1. All K2.7 Code
2. All K3
3. K2.7 Code with K3 escalation

The best route is the one that meets your quality and latency requirements at the lowest cost per successful task.

## Kimi K3 Pricing on CometAPI

The calculations above use Moonshot AI's official API pricing to keep the K3 and K2.7 comparison consistent.

At the time of publication, [Kimi K3 on CometAPI](https://www.cometapi.com/models/moonshotai/kimi-k3/) is priced **20% lower than Moonshot AI's standard API rates**:

| Route | Input | Output |
| --- | --- | --- |
| Moonshot AI | $3.00 / 1M | $15.00 / 1M |
| CometAPI | $2.40 / 1M | $12.00 / 1M |

Because API pricing may change, check the live model page before using these figures for production budgeting.

CometAPI's OpenAI-compatible API makes it easy to test `kimi-k3` alongside other model routes using the same prompts and evaluation workflow.

> **Ready to test Kimi K3?** [View Kimi K3 on CometAPI](https://www.cometapi.com/models/moonshotai/kimi-k3/) and compare pricing before moving it into production.

For integration and evaluation examples, see the [CometAPI Cookbook on GitHub](https://github.com/cometapi-dev/cometapi-cookbook).

## FAQ

### How much does the Kimi K3 API cost?

Moonshot AI lists Kimi K3 at **$0.30 per 1 million cache-hit input tokens, $3.00 per 1 million cache-miss input tokens, and $15.00 per 1 million output tokens**.

The API model ID is `kimi-k3`.

### Is Kimi K3 cheaper than Kimi K2.7 Code?

No. Based on Moonshot's official rates, K3 is approximately 3.16× the price for cache-miss input and 3.75× the price for output.

It may still reduce workflow costs if it improves task success or reduces retries.

### Does Kimi K3 have a 1M-token context window?

Yes. Kimi K3 supports a **1,048,576-token** **context window**, compared with 262,144 tokens for Kimi K2.7 Code.

### Does Kimi K3 support automatic context caching?

Yes. Context caching is automatic. Cache-hit input tokens cost $0.30 per million compared with $3.00 per million for cache-miss input tokens.

### Can I turn off Kimi K3 reasoning to reduce costs?

Not currently. K3 always uses reasoning, and `reasoning_effort="max"` is the only supported reasoning-effort level.

## Final Thoughts

Kimi K3 offers substantially more context and broader capabilities than K2.7 Code, but at a higher token price.

For routine coding within 256K context, K2.7 Code is usually the more economical choice. For long-context, multimodal, or difficult agentic tasks, K3 can justify its premium—especially when it improves successful completion.

For many production systems, the most efficient strategy is therefore not to replace K2.7 entirely, but to use **K2.7 as the default and K3 as the escalation route**.

The metric that ultimately matters is not cost per API call, but **cost per successful task**.

---

*Originally published at [https://www.cometapi.com/kimi-k3-api-pricing/](https://www.cometapi.com/kimi-k3-api-pricing/).*
