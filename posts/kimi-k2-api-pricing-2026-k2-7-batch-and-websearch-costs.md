<!-- social-ops-fingerprint:122e89c93fffff08fc711cd1f8cca212c34c1a8730d0b9940f246db06102b708 -->
---
title: Kimi K2 API Pricing 2026: K2.7, Batch and WebSearch Costs
---
# Kimi K2 API Pricing 2026: K2.7, Batch and WebSearch Costs

![Kimi K2 API Pricing 2026: K2.7, Batch and WebSearch Costs](https://resource.cometapi.com/kimi-k2-api-pricing.png)

**TLDR** Moonshot AI currently prices Kimi K2.7 Code at **$0.19 per 1M cache-hit input tokens, $0.95 per 1M cache-miss input tokens and $4.00 per 1M output tokens**. Kimi K2.7 Code HighSpeed doubles those rates to **$0.38 / $1.90 / $8.00**.

The main cost considerations are:

- **Caching:** Moonshot’s K2.7 cache-hit input is 80% cheaper than cache-miss input.
- **HighSpeed:** The faster route costs twice as much at the token level.
- **Batch API:** Supported models cost 60% of their real-time rates, equivalent to a 40% saving.
- **WebSearch:** Moonshot charges $0.005 per successful built-in search call, plus the tokens used to process search results.
- **Compatibility:** K2.7 Code requires Thinking mode, while Moonshot’s built-in WebSearch requires Thinking to be disabled.

For coding agents, the most useful metric is not price per million tokens. It is **cost per completed task**, including reasoning, caching, retries, tool calls, latency and human corrections.

## Kimi K2 API Pricing at a Glance

![kimi-k2-api-pricing-at -a-glance](https://resource.cometapi.com/kimi-k2-api-pricing-at%20-a-glance.PNG "Kimi K2 API Pricing at a Glance")

*source:* *[Kimi K2.7 Code pricing](https://platform.kimi.ai/docs/pricing/chat-k27-code)*

| Model or route | Cache-hit input | Cache-miss or standard input | Output | Context |
| --- | --- | --- | --- | --- |
| Moonshot K2.7 Code | $0.19 / 1M | $0.95 / 1M | $4.00 / 1M | 256K |
| Moonshot K2.7 Code HighSpeed | $0.38 / 1M | $1.90 / 1M | $8.00 / 1M | 256K |
| Moonshot K2.6 | $0.16 / 1M | $0.95 / 1M | $4.00 / 1M | 256K |
| Moonshot K2.5 | $0.10 / 1M | $0.60 / 1M | $3.00 / 1M | 256K |
| CometAPI K2.7 Code | Not separately listed | $0.76 / 1M | Approx. $3.20 / 1M | 256K |

Moonshot’s K2.7 prices are currently promotional. Moonshot and CometAPI also use different input-billing structures, so their listed rates should not be treated as directly interchangeable.

## Moonshot Kimi K2 Pricing Explained

K2.7 Code and K2.6 share the same cache-miss input and output prices. The main token-level differences are that K2.7 Code charges slightly more for cached input, while HighSpeed doubles all K2.7 rates.

| Model | Best suited to |
| --- | --- |
| kimi-k2.7-code | Coding agents, repository edits and long-horizon engineering tasks |
| kimi-k2.7-code-highspeed | Interactive coding where lower latency has measurable value |
| kimi-k2.6 | General multimodal reasoning, agents and built-in WebSearch |
| kimi-k2.5 | Lower-cost general and multimodal workloads |

Moonshot describes HighSpeed as the same underlying K2.7 Code model served through a faster route. Its documented output speed is approximately 180 tokens per second, reaching up to 260 tokens per second in shorter-context scenarios. Capacity may fluctuate while Moonshot expands resources.

HighSpeed is therefore primarily a latency choice rather than a separate model-quality tier.

## A Moonshot Direct API Alternative: CometAPI

Developers can access Kimi K2.7 Code through Moonshot AI directly or through CometAPI’s OpenAI-compatible API.

| Access route | Standard input | Cached input | Output |
| --- | --- | --- | --- |
| Moonshot direct API | $0.95 / 1M cache miss | $0.19 / 1M | $4.00 / 1M |
| CometAPI | $0.76 / 1M | Not separately listed | Approx. $3.20 / 1M |

CometAPI’s listed standard input and output prices are about **20% lower**, while Moonshot may be more cost-effective for workloads with a high cache-hit ratio.

Choose CometAPI if you want one API for Kimi and other model providers. Choose Moonshot direct access if your workflow frequently reuses the same prompts or repository context.

![Kimi K2.7 Code price on CometAPI](https://resource.cometapi.com/Kimi%20K2.7%20Code%20price%20on%20CometAPI.png)

*source:* *[Kimi K2.7 Code price on CometAPI](https://www.cometapi.com/models/moonshot/kimi-k2-7-code/)*

At the currently listed rates, CometAPI is approximately **20% cheaper** than Moonshot’s cache-miss input and output prices.

However, CometAPI does not show a separate cache-hit price on its K2.7 model page. Its $0.76 standard input price should not be compared directly with Moonshot’s $0.19 cached-input rate.

Teams that repeatedly reuse long system prompts, tool definitions or repository context should test both routes using their actual traffic. A workload with a very high cache-hit ratio may produce a different result from one that sends mostly new context.

Review the latest [Kimi K2.7 Code price on CometAPI](https://www.cometapi.com/models/moonshot/kimi-k2-7-code/) or compare available models on the [CometAPI pricing page](https://www.cometapi.com/pricing/).

## How Context Caching Changes Kimi API Cost

Kimi bills input tokens as cache hits or cache misses.

Cache misses generally include new or modified content, such as:

- new repository files
- updated instructions
- fresh tool results
- changing conversation history

Cache hits may include repeated content, such as stable system prompts, tool schemas, coding conventions and unchanged repository context.

For K2.7 Code, cached input costs $0.19 per 1M tokens compared with $0.95 for uncached input. That makes a cache-hit token 80% cheaper.

Calculate the two categories separately:

```
Input cost =
(cache-hit tokens ÷ 1,000,000 × cache-hit price)
+
(cache-miss tokens ÷ 1,000,000 × cache-miss price)
```

### Caching cost example

Assume one workflow process:

- 800,000 cache-hit tokens
- 200,000 cache-miss tokens

| Token category | Calculation | Cost |
| --- | --- | --- |
| Cache hit | 800,000 ÷ 1M × $0.19 | $0.15 |
| Cache miss | 200,000 ÷ 1M × $0.95 | $0.19 |
| Total input cost | $0.152 + $0.190 | $0.34 |

Calculating the same 1M tokens entirely at the cache-miss rate would cost $0.95. In this example, the mixed cache profile reduces input cost by $0.608.

This is why production dashboards should record cache-hit and cache-miss tokens separately instead of reporting only total input usage.

## Kimi Batch API Pricing

Moonshot’s Batch API charges **60% of the corresponding real-time model price**, giving teams a 40% saving on supported asynchronous workloads. The current documentation lists K2.7 Code, K2.6 and K2.5 as supported Batch models.

| Batch model | Cache-hit input | Cache-miss input | Output |
| --- | --- | --- | --- |
| kimi-k2.7-code | $0.114 / 1M | $0.57 / 1M | $2.40 / 1M |
| kimi-k2.6 | $0.096 / 1M | $0.57 / 1M | $2.40 / 1M |
| kimi-k2.5 | $0.06 / 1M | $0.36 / 1M | $1.80 / 1M |

Batch API is a good fit for:

- repository-wide code analysis
- large evaluation runs
- offline classification
- nightly enrichment
- synthetic test generation
- migration analysis
- security-review backlogs

It is less suitable for IDE assistants, live chat and other workflows where a user is waiting for an immediate response.

For background processing, the 40% saving can be more valuable than switching to a cheaper model with a lower task-completion rate.

## Kimi WebSearch Pricing and Compatibility

Moonshot charges **$0.005 for each successful built-in** **`$web_search`** **call**. No separate tool fee is charged when the model finishes without triggering the search tool.

Search-result content may also be added to the next model request and billed as input tokens. Moonshot defines the resulting token calculation as:

```
Total tokens =
prompt tokens + search-result tokens + completion tokens
```

A complete search workflow may therefore include:

```
Initial model request
+ WebSearch tool fee
+ search-result input tokens
+ follow-up model request
+ retries
```

There is also an important model restriction. Moonshot’s built-in WebSearch requires Thinking to be disabled, while K2.7 Code does not support non-thinking mode. The official WebSearch example therefore uses K2.6 with Thinking disabled.

For Moonshot’s built-in search, use K2.6 or K2.5 with Thinking disabled.

A K2.7 coding agent can still call an independently implemented search service through normal function calling. In that case, search pricing is determined by the external provider rather than Moonshot’s $0.005 built-in fee.

## Example 1: K2.7 Code Cost for a Coding Task

Assume a coding-agent workflow uses:

- 30,000 cache-miss input tokens
- 8,000 output tokens, including reasoning
- no built-in WebSearch call

### Standard K2.7 Code

| Component | Calculation | Cost |
| --- | --- | --- |
| Input | 30,000 ÷ 1M × $0.95 | $0.03 |
| Output | 8,000 ÷ 1M × $4.00 | $0.03 |
| Total |  | $0.06 |

### K2.7 Code HighSpeed

| Component | Calculation | Cost |
| --- | --- | --- |
| Input | 30,000 ÷ 1M × $1.90 | $0.06 |
| Output | 8,000 ÷ 1M × $8.00 | $0.06 |
| Total |  | $0.12 |

For the same token usage, HighSpeed costs exactly twice as much.

### CometAPI K2.7 Code

Using the current CometAPI rates:

| Component | Calculation | Cost |
| --- | --- | --- |
| Input | 30,000 ÷ 1M × $0.76 | $0.02 |
| Output | 8,000 ÷ 1M × $3.19998 | Approx. $0.0256 |
| Total |  | Approx. $0.0484 |

That is approximately 20% below the $0.0605 Moonshot cache-miss token cost in this example. The calculation excludes taxes, external tools and other platform services.

## Example 2: K2.6 With Built-In WebSearch

Assume a K2.6 workflow with Thinking disabled uses:

- 30,000 cache-miss input tokens across the complete workflow
- 8,000 output tokens
- one successful built-in WebSearch call

The 30,000 input tokens include search-result content carried into the follow-up request.

| Component | Calculation | Cost |
| --- | --- | --- |
| Input | 30,000 ÷ 1M × $0.95 | 0.0285 |
| Output | 8,000 ÷ 1M × $4.00 | 0.0320 |
| WebSearch | 1 × $0.005 | 0.0050 |
| Total |  | 0.0655 |

In this example, the direct WebSearch fee represents about 7.6% of the total. In longer research workflows, the tokens added by the search results may cost more than the tool call itself.

## Engineering Details That Can Change the Final Bill

### K2.7 Code always uses Thinking mode

![](/Users/mi/Documents/cometapi/0713/Kimi K2.7 Code price on CometAPI.png)

Source:\* *[KIMI Thinking Mode Documentation](https://platform.kimi.ai/docs/guide/use-kimi-k2-thinking-model)*

K2.7 Code returns an error if Thinking is disabled. Its reasoning is returned through `reasoning_content`, and both reasoning and the visible answer contribute to token usage.

During multi-step tool calls, applications must preserve the assistant’s `reasoning_content` in the conversation context. Longer agent loops may therefore increase both current output usage and later input usage.

### `max_tokens` is a limit, not a fixed charge

The `max_tokens` parameter defines the maximum amount the model may generate. A higher setting gives the model enough room to complete its reasoning and response, but the full allowance is not automatically billed.

Costs are based on actual tokens processed and generated.

### Several request parameters are fixed

K2.7 Code requires fixed values for several parameters:

| Parameter | Required value |
| --- | --- |
| temperature | 1 |
| top\_p | 0.95 |
| n | 1 |
| presence\_penalty | 0 |
| frequency\_penalty | 0 |

Passing another value can return an error. Applications using the same OpenAI-compatible wrapper across multiple providers should inspect hardcoded defaults before switching models.

For a practical integration walkthrough, see [How to Use Kimi K2.7 Code API with CometAPI](https://www.cometapi.com/how-to-use-kimi-k2-7-code-api/).

## External Adoption and Developer Signals

Official pricing documentation explains how the model is billed. External adoption provides additional context on where it is being used and how developers are evaluating it.

### GitHub Copilot

GitHub made Kimi K2.7 Code generally available in Copilot on July 1, 2026, describing it as the first open-weight model offered in the Copilot model picker. Availability initially covered individual plans and was expanded to Business and Enterprise plans on July 7.

GitHub’s adoption is a useful distribution signal, but it does not prove that K2.7 will outperform other models on every coding workload.

External sources:

- [Kimi K2.7 Code is generally available in GitHub Copilot](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/)
- [Kimi K2.7 for Copilot Business and Enterprise](https://github.blog/changelog/2026-07-07-kimi-k2-7-now-available-for-copilot-business-and-enterprise/)

### Open-weight deployment ecosystem

Moonshot publishes Kimi K2.7 Code on Hugging Face under a modified MIT license. The model card describes a 1-trillion-parameter mixture-of-experts architecture with 32 billion activated parameters and a 256K context window. It also includes deployment instructions for frameworks such as Transformers, vLLM and SGLang.

Moonshot reports approximately 30% lower thinking-token usage than K2.6 and a 10% improvement in agentic capability. These are vendor-reported results and should be validated using independent workloads.

See the [Kimi K2.7 Code model card on Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.7-Code) for architecture and deployment details.

### Developer community discussion

Discussion on Hacker News is more mixed than the launch materials. Some developers focus on Kimi’s open-weight availability, token efficiency and integration with coding-agent tools. Others argue that a lower token price does not guarantee a lower project cost if the model requires more retries, supervision or context.

That debate supports the central recommendation of this guide: compare models using real repositories and measure task completion, retries and human edits—not just advertised token rates.

See the [Kimi K2.7 Code discussion on Hacker News](https://news.ycombinator.com/item?id=48502347).

## GPT vs Claude vs Kimi vs DeepSeek API Pricing

The table below compares the current standard API rates for Kimi K2.7 Code, DeepSeek V4 Pro, Claude Sonnet 5 and GPT-5.6 Sol as of July 13, 2026.

| Provider | Model | Standard input | Cached input or read | Output | Notes | CometAPI price |
| --- | --- | --- | --- | --- | --- | --- |
| Moonshot AI | [Kimi K2.7 Code](https://www.cometapi.com/models/moonshotai/kimi-k2-7-code) | $0.95 / 1M | $0.19 / 1M | $4.00 / 1M | Promotional pricing | $0.76 input / ~$3.20 output |
| DeepSeek | [DeepSeek V4 Pro](https://www.cometapi.com/models/deepseek/deepseek-v4) | $0.435 / 1M cache miss | $0.003625 / 1M | $0.87 / 1M | 1M context | $0.416 input / $0.832 output |
| Anthropic | [Claude Sonnet 5](https://www.cometapi.com/models/anthropic/claude-sonnet-5) | $2.00 / 1M | $0.20 / 1M cache read | $10.00 / 1M | Intro pricing through Aug. 31, 2026 | $1.60 input / $8.00 output |
| OpenAI | [GPT-5.6 Sol](https://www.cometapi.com/models/openai/gpt-5-6/) | $5.00 / 1M | $0.50 / 1M | $30.00 / 1M | Standard short-context pricing | $4.00 input / $24.00 output |

Official pricing references:

- [DeepSeek API pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)

DeepSeek V4 Pro currently lists a 1M context window with cache-hit input at $0.003625, cache-miss input at $0.435 and output at $0.87 per million tokens.

Claude Sonnet 5’s introductory rate is $2 per million input tokens, $0.20 per million cache-read tokens and $10 per million output tokens through August 31, 2026. Its cache writes are priced separately, and Anthropic notes that the model’s newer tokenizer may produce more tokens for the same text than earlier Claude models.

GPT-5.6 Sol’s standard short-context rate is $5 per million input tokens, $0.50 per million cached-input tokens and $30 per million output tokens. OpenAI also lists separate cache-write, long-context, Batch, Flex and Priority rates.

At the listed token rates, Kimi K2.7 Code is less expensive than Claude Sonnet 5 and GPT-5.6 Sol, while DeepSeek V4 Pro is cheaper. This does not establish which model offers the lowest cost for a specific coding workflow.

## Which Kimi Model Should You Use?

| Workload | Recommended starting point |
| --- | --- |
| Repository edits and long coding tasks | kimi-k2.7-code |
| Interactive coding where latency matters | kimi-k2.7-code-highspeed |
| General multimodal reasoning and agents | kimi-k2.6 |
| Moonshot built-in WebSearch | kimi-k2.6 or kimi-k2.5 with Thinking disabled |
| Lower-cost general workloads | kimi-k2.5 |
| Offline evaluations and bulk processing | Batch API |

K2.7 Code is the natural starting point for quality-sensitive coding work. HighSpeed is worth testing when faster responses improve developer experience, conversion or throughput.

K2.6 is more flexible for general multimodal and search-grounded workflows, while K2.5 has the lowest standard Kimi token rates.

## How to Evaluate the Real Cost

Build an evaluation set from production tasks rather than relying only on public benchmarks.

Useful test cases include:

- repository-level feature implementation
- pull-request review
- debugging and test generation
- long-context code analysis
- multi-step tool calls
- search-ground developer support

Track:

- successful task completion
- cache-hit ratio
- input and output tokens
- reasoning-token volume
- tool-call success
- retry count
- p50 and p95 latency
- human corrections
- total workflow cost

Calculate:

```
Cost per completed task =
total workflow cost ÷ successfully completed tasks
```

For example, if a team spends $10 and successfully completes 80 tasks:

```
Cost per completed task = $10 ÷ 80 = $0.125
```

A model with cheaper tokens can still cost more if it requires repeated attempts, longer reasoning or extensive manual correction.

For routing, fallback and evaluation examples, explore the [CometAPI Cookbook](https://github.com/cometapi-dev/cometapi-cookbook).

## Frequently Asked Questions

### How much does Kimi K2.7 Code cost?

Moonshot currently lists K2.7 Code at:

- $0.19 per 1M cache-hit input tokens
- $0.95 per 1M cache-miss input tokens
- $4.00 per 1M output tokens

The rates are currently marked as limited-time promotional pricing.

### How much does K2.7 Code cost through CometAPI?

CometAPI currently lists K2.7 Code at $0.76 per 1M input tokens and $3.19998 per 1M output tokens.

A separate cache-hit rate is not shown on the model page.

### Does Kimi Batch API reduce costs, and does it support K2.7 Code?

Yes. Batch inference costs **60% of the real-time price**, equivalent to a **40% saving**.

Moonshot’s current Batch documentation lists K2.7 Code, K2.6 and K2.5 as supported models.

### How much does Kimi WebSearch cost?

Moonshot’s built-in `$web_search` costs $0.005 per successful call.

Search-result content may also be billed as input tokens when included in the next model request.

### Can thinking be disabled on K2.7 Code?

No. Requests that disable Thinking return an error.

### Is Kimi OpenAI-compatible?

Yes. Moonshot documents compatibility with the OpenAI API format, although model-specific restrictions still apply to Thinking, parameters and multi-step tool calls.

## Test Kimi K2.7 Code With CometAPI

Kimi K2.7 Code offers competitive pricing for coding-agent workloads, but the best route depends on more than the advertised token rate.

Before choosing a provider, compare:

```
Total workflow cost =
tokens + retries + tools + latency + human correction
```

CometAPI lets developers test Kimi alongside GPT, Claude, Gemini, DeepSeek, Grok and other model families through a unified API workflow.

Review the latest [CometAPI pricing](https://www.cometapi.com/pricing/), open the [Kimi K2.7 Code model page](https://www.cometapi.com/models/moonshot/kimi-k2-7-code/), and benchmark the model using real tasks from your own repositories.

The goal is not simply to find the cheapest token. It is to find the lowest cost per completed task.

---

*Originally published at [https://www.cometapi.com/kimi-k2-api-pricing/](https://www.cometapi.com/kimi-k2-api-pricing/).*
