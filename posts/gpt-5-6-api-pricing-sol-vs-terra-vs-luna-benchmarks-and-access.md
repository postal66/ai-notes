# GPT\-5\.6 API: Pricing, Sol vs Terra vs Luna, Benchmarks, and Access

**Recommended URL:** /blog/gpt\-5\-6\-api\-pricing\-models\-benchmarks\-access

**SEO Description:** Compare GPT\-5\.6 API pricing, Sol, Terra, and Luna capabilities, availability, benchmarks, model selection, and CometAPI access with current code examples\.

**SEO Keywords:** GPT\-5\.6 API, GPT\-5\.6 pricing, GPT\-5\.6 discount, GPT\-5\.6 Sol, GPT\-5\.6 Terra, GPT\-5\.6 Luna, CometAPI, OpenAI\-compatible API

![gpt\-5\-6\-api\-watchlist\-cover\.png](Images_attachments/gpt-5-6-api-watchlist-cover.png)

## What Should You Know About the GPT\-5\.6 API?

GPT\-5\.6 is no longer only a release watchlist item\. OpenAI lists the Sol, Terra, and Luna models as generally available, while CometAPI documents access through an OpenAI\-compatible API\. As of September 2, 2026, the [CometAPI GPT\-5\.6 model page](https://www.cometapi.com/models/openai/gpt-5-6/) lists short\-context token prices 20% below OpenAI’s current Standard API rates for all three tiers\.

The practical choice is not simply “use the newest model\.” Use `gpt-5.6-sol` for the hardest coding and reasoning work, `gpt-5.6-terra` when capability and cost both matter, and `gpt-5.6-luna` for high\-volume, well\-bounded tasks\. Teams already using the OpenAI SDK can test the family through CometAPI by setting the base URL to `https://api.cometapi.com/v1`, supplying a CometAPI key, and choosing an explicit model ID\.

## How Much Does GPT\-5\.6 API Cost?

Prices below were checked on September 2, 2026\. They are US dollars per 1 million tokens for requests with no more than 272,000 input tokens\. The CometAPI rates come from the live [GPT\-5\.6 model page](https://www.cometapi.com/models/openai/gpt-5-6/); the direct rates come from the [official OpenAI model catalog](https://developers.openai.com/api/docs/models)\.

|Model|CometAPI input|CometAPI output|OpenAI input|OpenAI output|Listed difference|
|---|---|---|---|---|---|
|`gpt-5.6-sol`|$3\.20|$16\.00|$4\.00|$20\.00|20% lower|
|`gpt-5.6-terra`|$1\.60|$9\.60|$2\.00|$12\.00|20% lower|
|`gpt-5.6-luna`|$0\.16|$0\.96|$0\.20|$1\.20|20% lower|

Cached\-input and cache\-write rates follow the same published 20% difference on the CometAPI page\. Requests above 272,000 input tokens move to the long\-context tier for the entire request: input\-related rates double and output rates increase by 50%\. Because prices and promotions can change, use this table as a dated snapshot and recheck the model page or account dashboard before estimating a production budget\.

A simple cost estimate for one request is:

```text
estimated_cost =
  (input_tokens / 1,000,000 × input_rate)
  + (output_tokens / 1,000,000 × output_rate)
```

For example, a short\-context Terra call with 100,000 uncached input tokens and 10,000 output tokens would be about $0\.256 at the listed CometAPI rates: $0\.160 for input plus $0\.096 for output\. This estimate excludes tool fees, retries, and cache behavior\.

### Is GPT\-5\.6 Cheaper Through CometAPI?

Yes—on the public model page checked September 2, 2026, CometAPI lists each GPT\-5\.6 tier 20% below OpenAI’s current Standard API rate\. For short\-context calls, Sol is $3\.20/$16, Terra $1\.60/$9\.60, and Luna $0\.16/$0\.96 per 1 million input/output tokens\. This is pay\-as\-you\-go rather than a subscription discount: CometAPI's [pricing page](https://www.cometapi.com/pricing/) states that official\-model customer pricing is the official rate multiplied by 0\.8, with no monthly subscription or minimum spend\. Additional tiers are available for monthly volume, while enterprise pricing is negotiated\. Recheck the live model page before budgeting because promotions and account\-level terms can change\.

### What Happens When GPT\-5\.6 Requests Exceed 272K Tokens?

The higher tier applies to the entire request, not only the tokens above 272K\. At the current CometAPI rates, Sol becomes $6\.40 input/$24 output, Terra $3\.20/$14\.40, and Luna $0\.32/$1\.44 per 1 million tokens; cache\-read and cache\-write rates also double\. Near the threshold, remove duplicate retrieved passages, stale chat history, verbose tool logs, and unnecessary source files before sending the request\.

## How Do GPT\-5\.6 Sol, Terra, and Luna Compare?

OpenAI introduced GPT\-5\.6 as a three\-tier family rather than a single model\. Sol is the flagship route, Terra is the balanced route, and Luna is the low\-cost route\. The models share a 1,050,000\-token context window and a maximum output of 128,000 tokens\. They accept text and image input and produce text output; audio and video are not supported by these model routes\.

|Model ID|Position|Modalities|Context / output|Supported routes|
|---|---|---|---|---|
|`gpt-5.6-sol`|Frontier capability|Text and image in; text out|1\.05M / 128K tokens|Chat Completions, Responses|
|`gpt-5.6-terra`|Balanced capability and cost|Text and image in; text out|1\.05M / 128K tokens|Chat Completions, Responses|
|`gpt-5.6-luna`|High\-volume efficiency|Text and image in; text out|1\.05M / 128K tokens|Chat Completions, Responses|

The unsuffixed `gpt-5.6` alias routes to GPT\-5\.6 Sol according to the [official OpenAI model documentation](https://developers.openai.com/api/docs/models/gpt-5.6-sol)\. Use an explicit Terra or Luna ID when cost control is part of the routing decision\.

## Is GPT\-5\.6 Available Through the API?

Yes\. OpenAI lists GPT\-5\.6 Sol, Terra, and Luna as generally available through its API, with Chat Completions and Responses routes documented for the family\. Availability was checked on September 2, 2026\. Use the exact model ID required by your workload and confirm any account\-level rate limits or regional restrictions before production deployment\.

Third\-party gateways can provide another access path\. CometAPI documents `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna` through OpenAI\-compatible Chat Completions and Responses formats\. Treat a public listing as route documentation rather than a guarantee of quota: verify the exact ID in your account before rollout\.

## What Do the Published GPT\-5\.6 Benchmarks Show?

OpenAI publishes benchmark results for the three GPT\-5\.6 tiers\. The following small set is useful because it covers coding agents, research\-style browsing, and long\-context retrieval rather than repeating a broad leaderboard\.

|Evaluation|Sol|Terra|Luna|
|---|---|---|---|
|Artificial Analysis Coding Agent Index v1\.1|80\.0|77\.4|74\.6|
|BrowseComp|90\.4%|87\.5%|83\.3%|
|MRCR v2, 8\-needle, 512K–1M|73\.8%|72\.5%|41\.3%|

Source: [OpenAI’s GPT\-5\.6 launch report](https://openai.com/index/gpt-5-6/)\. These are vendor\-published results, not independent tests run through CometAPI\. Scores depend on the evaluation harness, reasoning effort, tools, and model snapshot, so they should not be converted directly into a price\-to\-performance claim for your application\.

## How Should You Benchmark GPT\-5\.6 Before Production?

Run the same prompt set through Sol, Terra, and Luna with the same reasoning effort and output limit\. Record task success, latency, input and output tokens, retries, and total cost\. A four\-part prompt set is usually enough to expose the main differences:

1. **Repository task:** diagnose a real multi\-file bug and propose a patch with tests\.

2. **Long\-context task:** extract conflicting requirements from a large specification and cite their locations\.

3. **Tool\-use task:** plan and execute a bounded workflow with structured outputs\.

4. **High\-volume task:** classify or summarize 100 representative production inputs\.

Score correctness before style\. Then calculate cost per successful task, not merely cost per token\. A cheaper model that triggers more retries, longer outputs, or human review may be more expensive in production\. Conversely, Luna or Terra can outperform a flagship\-only strategy when the task is well specified and repeated at scale\.

## Which GPT\-5\.6 Model Should You Choose?

**Choose GPT\-5\.6 Sol** for difficult agentic coding, architecture review, research synthesis, security analysis in authorized environments, and decisions where a failed answer is expensive\. It is the highest\-cost tier, so route only the work that benefits from frontier capability\.

**Choose GPT\-5\.6 Terra** for everyday coding assistants, technical writing, document analysis, business automation, and mixed production workloads\. It is the strongest default candidate when you want one model to start a controlled evaluation\.

**Choose GPT\-5\.6 Luna** for extraction, classification, support triage, repeated agent steps, monitoring, and other high\-volume tasks with clear acceptance criteria\. Its low list price is attractive, but long\-context benchmark results show why teams should test it carefully before using it for million\-token retrieval or difficult multi\-step reasoning\.

GPT\-5\.6 is not the best fit when the application requires native audio or video output, a fine\-tuned model, or a fixed cost that is independent of token usage\. In those cases, choose a route designed for the required modality or deployment model rather than forcing the GPT\-5\.6 family into the workflow\.

## How to Acces GPT\-5\.6 API by CometAPI?

CometAPI is most useful when you want one API key and billing account across GPT\-5\.6 Sol, Terra, Luna, and hundreds of other models\. As of September 2, 2026,GPT\-5\.6  lists rates 20% below OpenAI's Standard API prices, while its pricing page documents pay\-as\-you\-go billing with no monthly subscription or minimum spend and additional tiers for monthly volume\. For teams already using the OpenAI SDK, testing GPT\-5\.6 requires changing the base URL, API key, and model ID instead of building a provider\-specific integration\. Unified billing and failover can further reduce multi\-provider operations, although teams should still verify account access, latency, quota, and regional availability\. For the Open AI API, CometAPI accepts both chat and response formats\. The examples below use \\\\ [Chat Completions API](https://apidoc.cometapi.com/api/text/chat) at `https://api.cometapi.com/v1/chat/completions`\.

### How Do You Call GPT\-5\.6 Sol with Python?

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
)

completion = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[
        {
            "role": "user",
            "content": "Review this migration plan and identify the three highest-risk assumptions.",
        }
    ],
)

print(completion.choices[0].message.content)
```

### How Do You Call GPT\-5\.6 Sol with Node\.js?

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.COMETAPI_KEY,
  baseURL: "https://api.cometapi.com/v1",
});

const completion = await client.chat.completions.create({
  model: "gpt-5.6-sol",
  messages: [
    {
      role: "user",
      content: "Review this migration plan and identify the three highest-risk assumptions.",
    },
  ],
});

console.log(completion.choices[0].message.content);
```

### How Do You Call GPT\-5\.6 Sol with curl?

```bash
curl https://api.cometapi.com/v1/chat/completions \
  -H "Authorization: Bearer $COMETAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [
      {
        "role": "user",
        "content": "Review this migration plan and identify the three highest-risk assumptions."
      }
    ]
  }'
```

See the [CometAPI Quick Start](https://apidoc.cometapi.com/overview/quick-start), [base URL guide](https://apidoc.cometapi.com/guides/change-base-url-to-cometapi), and [Chat Completions API reference](https://apidoc.cometapi.com/api/text/chat) for authentication and parameter details\.

# FAQ

## Where can I access GPT\-5\.6 API at a discount?

As of September 2, 2026, CometAPI’s GPT\-5\.6 model page lists Sol, Terra, and Luna token rates 20% below OpenAI’s current Standard API rates for short\- and long\-context requests\. Access uses the OpenAI\-compatible base URL `https://api.cometapi.com/v1`\. Confirm the exact model ID, price, and account availability in the live CometAPI catalog or dashboard before production use\.

## Is GPT\-5\.6 still only a watchlist model?

No\. OpenAI describes the GPT\-5\.6 family as generally available, and CometAPI’s changelog says the family is available through Chat and Responses API formats\. The useful “watchlist” now concerns changing prices, promotions, quotas, route IDs, and account\-level availability rather than whether the family has launched\.

## What does the `gpt-5.6` model ID use?

OpenAI states that the generic `gpt-5.6` alias routes to GPT\-5\.6 Sol\. Use `gpt-5.6-terra` or `gpt-5.6-luna` explicitly when you need those cost tiers\.

## Which GPT\-5\.6 model is cheapest?

GPT\-5\.6 Luna is the lowest\-cost tier\. On the CometAPI model page checked September 2, 2026, its short\-context rate is $0\.16 per million input tokens and $0\.96 per million output tokens\.

## Does the 20% difference apply to long\-context requests?

The CometAPI model page lists the same 20% difference for both short\- and long\-context tiers\. Once input exceeds 272,000 tokens, the higher rates apply to the entire request, so long\-context tests should be budgeted separately\.

## Can I switch between Sol, Terra, and Luna without changing the SDK?

Yes\. With an OpenAI\-compatible CometAPI integration, the base URL and authentication remain the same\. Change the model ID, then validate any model\-specific behavior, reasoning settings, quality targets, and rate limits before routing production traffic\.



