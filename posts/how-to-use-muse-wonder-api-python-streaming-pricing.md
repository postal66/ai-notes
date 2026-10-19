<!-- social-ops-fingerprint:ccadcbcf78a299d51aafc3dd2e68135bd94cc4f73a1d1426a654e6e00e1d42fd -->
---
title: How to Use Muse Wonder API: Python, Streaming & Pricing
---
# How to Use Muse Wonder API: Python, Streaming & Pricing

![How to Use Muse Wonder API: Python, Streaming & Pricing](https://resource.cometapi.com/11%E4%B8%8B%E8%BD%BD.png)

## TL;DR

Muse Wonder is Meta’s preview model for complex coding, reasoning and agentic workflows. Developers can access [Muse Wonder API in CometAPI](https://www.cometapi.com/models/meta/muse-wonder/) with an OpenAI-compatible client and model="muse-wonder". This guide helps developers familiar with Python or JavaScript send a first request, add streaming, and evaluate reasoning, media and cost. Compared with Muse Spark, the practical reason to evaluate Wonder is its potential to complete difficult tasks more reliably; a large context window alone is not a reason to migrate.

## Key Takeaways

- Integration: use a backend API key, `https://api.cometapi.com/v1`, and `model="muse-wonder"`.
- Capacity: Muse Wonder has a 1,048,576-token context window; trim repeated context to control cost.
- Capabilities: evaluate streaming, tool calls and media separately on the selected gateway route.
- Reasoning: native Muse Wonder supports minimal through max; higher effort increases token use and latency.
- Deployment: benchmark real tasks, verify current billing, and preserve a rollback model before expanding traffic.

## What Is Muse Wonder API?

Meta introduced Muse Wonder on October 12, 2026. The model is available in preview through the Meta Model API for complex coding, reasoning and tool-driven workflows. CometAPI uses the model identifier muse-wonder; Meta's native identifier is muse-wonder-1.0.

The native model focuses on sustained reasoning, coding and tool-driven work. Applications still supply tools, persistent state, stopping conditions and permission checks; an individual model call does not create an autonomous execution environment.

![How to Use Muse Wonder API: Python, Streaming & Pricing](https://resource.cometapi.com/1280Xm1280.PNG)

### Muse Wonder API specifications

| Specification | Meta model documentation |
| --- | --- |
| Developer | Meta |
| Release | October 12, 2026 |
| Native Meta identifier | muse-wonder-1.0 |
| CometAPI identifier | muse-wonder |
| Native context window | 1,048,576 tokens |
| Native inputs | Text, image, video, audio and PDF; gateway formats require separate validation |
| Output | Text |
| Native API status | Preview |
| Streaming and tools | Native API capabilities; validate the selected CometAPI route |
| Full variant | Eligible Muse Code subscriptions; not selected by reasoning effort |

### Muse Wonder vs Muse Wonder Full

Muse Wonder is available through Meta Model API; Muse Wonder Full is available only through the Power Usage and Maximum Usage subscriptions in Muse Code, and setting reasoning\_effort to max does not switch to Muse Wonder Full. See [Meta's launch announcement](https://dev.meta.ai/resources/blog/build-with-muse-wonder).

## Muse Spark API vs Muse Wonder API

Choose between the models by measured task success and cost. The native model guide recommends Wonder for complex work and Spark for cost-sensitive workloads; it gives both a 1,048,576-token context window. Compare a specific Spark version rather than assuming all versions have identical capabilities.

Muse Spark is better suited to cost-sensitive workloads; Muse Wonder targets complex coding and sustained reasoning. Verify media support, reasoning controls and billing for the exact model version and gateway route. Keep the model that meets your measured task-success and cost targets.

## How to Use Muse Wonder API with CometAPI Step by Step

### Step 1: Create and secure your CometAPI key

Create an account, generate a backend API key, and keep it out of browser code and public repositories. Follow the [CometAPI integration documentation](https://apidoc.cometapi.com/) for authentication. These examples require a funded or eligible account, Python 3.10+ or a supported Node.js LTS environment, and outbound HTTPS access. Save JavaScript examples as .mjs files.

Set the API key in a Bash session.

```
export COMETAPI_KEY="your_cometapi_api_key"
```

Set the API key in a PowerShell session.

```
$env:COMETAPI_KEY="your_cometapi_api_key"
```

### Step 2: Configure the Muse Wonder endpoint

| Setting | Value |
| --- | --- |
| Base URL | `https://api.cometapi.com/v1` |
| Chat endpoint | /chat/completions |
| HTTP method | POST |
| Authorization | Bearer API key |
| Model | muse-wonder |

### Step 3: Send your first request with cURL

Send a minimal authenticated chat request.

```
curl -X POST "https://api.cometapi.com/v1/chat/completions" \
  -H "Authorization: Bearer $COMETAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "muse-wonder",
    "messages": [
      {"role": "system", "content": "You are a senior engineer."},
      {"role": "user", "content": "List three ways to improve Python API reliability."}
    ],
    "stream": false
  }'
```

A successful non-streaming request should return choices[0].message.content. Inspect the returned model and usage, when supplied, and confirm the text answers your prompt. Authentication failures need credential checks; an invalid model error needs model-access checks. Examples illustrate request patterns and do not represent measured latency or benchmark results.

### Step 4: Make a Python request

Install the Python client library.

```
pip install --upgrade openai
```

Send a Python request and inspect token usage.

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
    timeout=120.0,
)
response = client.chat.completions.create(
    model="muse-wonder",
    messages=[
        {"role": "system", "content": "You are a Python engineer."},
        {"role": "user", "content": "Review: def divide(a,b): return a/b"},
    ],
)
print(response.choices[0].message.content)
if response.usage:
    print("Total tokens:", response.usage.total_tokens)
```

### Step 5: Use JavaScript or Node.js

Install the JavaScript client library.

```
npm install openai
```

Send a Node.js request.

```
import OpenAI from "openai";
const client = new OpenAI({
  apiKey: process.env.COMETAPI_KEY,
  baseURL: "https://api.cometapi.com/v1",
});
const response = await client.chat.completions.create({
  model: "muse-wonder",
  messages: [{role: "user", content: "Explain async/await."}],
});
console.log(response.choices[0].message.content);
```

## How to Stream Muse Wonder Responses with CometAPI

Streaming returns incremental response chunks over server-sent events. It improves perceived responsiveness, though not necessarily the total cost or completion time. Only display chunks containing content, and handle interruption and timeout cases.

### Python streaming example

Read incremental Python response chunks.

```
import os
from openai import OpenAI
client = OpenAI(api_key=os.environ["COMETAPI_KEY"],
                base_url="https://api.cometapi.com/v1", timeout=180.0)
stream = client.chat.completions.create(
    model="muse-wonder",
    messages=[{"role": "user", "content": "Design a scalable FastAPI service."}],
    stream=True,
)
parts = []
for chunk in stream:
    if not chunk.choices:
        continue
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
        parts.append(content)
print("\nResponse complete.")
```

### JavaScript streaming example

Read incremental Node.js response chunks.

```
import OpenAI from "openai";
const client = new OpenAI({
  apiKey: process.env.COMETAPI_KEY,
  baseURL: "https://api.cometapi.com/v1",
});
const stream = await client.chat.completions.create({
  model: "muse-wonder",
  messages: [{role: "user", content: "Outline a research agent."}],
  stream: true,
});
for await (const chunk of stream) {
  const text = chunk.choices?.[0]?.delta?.content;
  if (text) process.stdout.write(text);
}
```

## What Reasoning Effort Levels Does Muse Wonder Support?

### Supported Reasoning Effort Values

The native model accepts minimal, low, medium, high, xhigh and max; none is unsupported. Start with a moderate setting and raise it only when your evaluations justify the extra latency and output-token cost. See the [Meta reasoning reference](https://dev.meta.ai/docs/reasoning). Test gateway forwarding separately.

### How to Set Reasoning Effort in Chat Completions

The following example sends high through the gateway as a capability test. If rejected, inspect the error before removing the field: a 400 can also indicate invalid messages, an incorrect model or another request issue. Retry with the minimal text request to isolate the cause.

Test high reasoning effort on the gateway.

```
import os
from openai import OpenAI, BadRequestError
client = OpenAI(api_key=os.environ["COMETAPI_KEY"],
                base_url="https://api.cometapi.com/v1")
try:
    response = client.chat.completions.create(
        model="muse-wonder",
        messages=[{"role": "user", "content": "Diagnose a distributed timeout."}],
        extra_body={"reasoning_effort": "high"},
    )
    print(response.choices[0].message.content)
except BadRequestError as err:
    print("This reasoning parameter may not be accepted:", err)
```

### How to Set Reasoning Effort in the Responses API

Meta's native Responses API nests the field as reasoning.effort and uses muse-wonder-1.0. The example below uses Meta credentials and its native endpoint; confirm Responses support independently before adapting it to CometAPI.

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["META_API_KEY"],
    base_url="https://api.meta.ai/v1",
)
response = client.responses.create(
    model="muse-wonder-1.0",
    input="Diagnose a distributed timeout.",
    reasoning={"effort": "high"},
)
print(response.output_text)
```

### Why max Does Not Select Muse Wonder Full

max changes the reasoning budget of the selected model. It does not change the model identifier or grant access to Full; the access distinction is explained in the model introduction.

## How Can Muse Wonder API Analyze Images and PDFs

Meta documents [image, video, audio and PDF input](https://dev.meta.ai/docs/models) for native Wonder. Meta’s native media support does not guarantee that CometAPI accepts the same content schema, URL format, file types or size limits. Verify those details on the selected route before production use. The image\_url example below is a compatibility pattern: use an accessible image you control, confirm endpoint support, and check the answer against visible details.

Test an image URL with a known image.

```
import os
from openai import OpenAI
client = OpenAI(api_key=os.environ["COMETAPI_KEY"],
                base_url="https://api.cometapi.com/v1")
response = client.chat.completions.create(
    model="muse-wonder",
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "Describe anomalies in this dashboard."},
        {"type": "image_url", "image_url": {
            "url": "https://example.com/dashboard.png"}},
    ]}],
)
print(response.choices[0].message.content)
```

For a predictable text-only PDF workflow, extract selectable text locally and send selected passages as text. This does not test native PDF input or preserve page layout, figures or scanned content. The example limits input to 50,000 characters for a small test; production ingestion should select or chunk content and preserve page references instead of silently truncating a report.

Extract selectable PDF text for a bounded test.

```
# pip install pymupdf openai
import os
import fitz
from openai import OpenAI
client = OpenAI(api_key=os.environ["COMETAPI_KEY"],
                base_url="https://api.cometapi.com/v1")
with fitz.open("report.pdf") as doc:
    document_text = "\n".join(p.get_text() for p in doc)
response = client.chat.completions.create(
    model="muse-wonder",
    messages=[{"role": "user", "content":
        "Summarize the risks in this report:\n" + document_text[:50000]}],
)
print(response.choices[0].message.content)
```

## How Can You Build a Tool-Calling Agent With Muse Wonder API

A model can request a function call, but the application must authorize and execute it. This example demonstrates one bounded, read-only order lookup; production implementations should validate inputs and constrain tools by permission.

Execute a bounded order-status tool request.

```
import json, os
from openai import OpenAI
client = OpenAI(api_key=os.environ["COMETAPI_KEY"],
                base_url="https://api.cometapi.com/v1")
tools = [{"type": "function", "function": {
    "name": "get_order_status",
    "description": "Look up an order status",
    "parameters": {"type": "object",
        "properties": {"order_id": {"type": "string"}},
        "required": ["order_id"], "additionalProperties": False}
}}]
messages = [{"role": "user", "content": "Status of order A1001?"}]
r = client.chat.completions.create(model="muse-wonder",
    messages=messages, tools=tools, tool_choice="auto")
msg = r.choices[0].message
messages.append(msg)
if msg.tool_calls:
    for call in msg.tool_calls:
        if call.function.name != "get_order_status":
            raise ValueError("Tool not permitted")
        args = json.loads(call.function.arguments)
        status = {"A1001": "Shipped"}.get(args["order_id"], "Not found")
        messages.append({"role": "tool", "tool_call_id": call.id,
                         "content": json.dumps({"status": status})})
    r = client.chat.completions.create(model="muse-wonder",
        messages=messages, tools=tools)
    print(r.choices[0].message.content)
else:
    print(msg.content)
```

This teaching example handles one tool-call round. If the follow-up response requests another tool call, continue only within a bounded loop and validate its name and arguments again. Persist tool results for retry safety; a production agent also needs a time limit, an iteration limit and a clear completion condition.

## How Much Does Muse Wonder API Cost

Meta's [official pricing](https://dev.meta.ai/resources/blog/build-with-muse-wonder) states $4.00 per million uncached input tokens, $0.20 per million cached input tokens, and $20.00 per million output tokens.

The source article's October 14, 2026 pricing snapshot lists CometAPI at $3.20 per million uncached input tokens and $16.00 per million output tokens. These are gateway rates, not a replacement for Meta's $4.00 input and $20.00 output prices. Confirm your current account and route rates before use; no CometAPI cached-input tariff is assumed.

| Per 1M tokens | Meta native API | Muse Wonder API in CometAPI |
| --- | --- | --- |
| Uncached input | $4.00 | $3.20 |
| Cached input | $0.20 | Confirm route tariff |
| Output | $20.00 | $16.00 |

For 100,000 uncached input tokens and 50,000 billed output tokens, the listed Meta rates give $0.40 + $1.00 = $1.40. The listed CometAPI rates give $0.32 + $0.80 = $1.12. This example excludes extra charges and does not assume any cache discount.

For this uncached example, the displayed CometAPI rates give a 20% lower estimate. Real invoices depend on token usage, route billing and any additional charges. If caching applies, calculate it using the verified cached tariff rather than applying the uncached input rate to every token.

Estimate cost with the CometAPI rates in the source snapshot; replace them with your verified account rates.

```
def estimate_cost(input_tokens, output_tokens,
                  input_rate=3.20, output_rate=16.00):
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError('Token counts must be non-negative')
    return (input_tokens * input_rate
            + output_tokens * output_rate) / 1_000_000

print(estimate_cost(100000, 50000))  # 1.12
```

## How to Migrate and Run Muse Wonder in Production

### Update and Validate the Integration

Most OpenAI-compatible client integrations can retain their overall structure. Update the base URL, credential and model ID, then run a staged evaluation on real prompts. Protocol-specific reasoning and multimodal fields need independent verification.

Set `COMETAPI_KEY`, update the base URL to `https://api.cometapi.com/v1` and select muse-wonder. Verify authentication and model access with a minimal text request. Then test reasoning fields, streaming chunks, tool-call execution and any media format separately. Inspect errors and answer quality: an HTTP 400 can have several causes, while a successful HTTP response alone does not prove capability support. Record returned usage and compare cost with your budget. Keep the base URL and model configurable so you can roll back.

Configure an environment-driven migration and rollback.

```
import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url=os.getenv("AI_BASE_URL", "https://api.cometapi.com/v1"),
)
model = os.getenv("AI_MODEL", "muse-wonder")
r = client.chat.completions.create(
    model=model,
    messages=[{"role":"user", "content":"Review this API design."}],
)
print(r.choices[0].message.content)
```

Start with a small canary fraction of live traffic. Compare correctness, tool success, first-token latency, total latency, retry rate and total cost per successfully completed task before widening rollout.

### Add Timeouts, Retry Limits and Monitoring

Set request timeouts and explicit limits; log non-sensitive request IDs and token usage; redact personal information when possible; retry only transient failures; and require authorization for irreversible tool actions. A cheaper model call is not necessarily a cheaper task if it causes retries.

Retry transient errors with bounded exponential backoff.

```
import os, time, random
from openai import (OpenAI, APIConnectionError, APITimeoutError,
    RateLimitError, InternalServerError)
client = OpenAI(api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1", timeout=60, max_retries=0)
def complete_with_retry(prompt, attempts=4):
    for i in range(attempts):
        try:
            r = client.chat.completions.create(
                model="muse-wonder",
                messages=[{"role": "user", "content": prompt}])
            return r.choices[0].message.content
        except (RateLimitError, APIConnectionError,
                APITimeoutError, InternalServerError):
            if i == attempts-1:
                raise
            time.sleep(min(2**i, 16) + random.uniform(0, 0.5))
```

Suggested operating metric: cost per successful task = total model and tool costs / number of successful tasks. Track safety and correctness guardrails as well as aggregate costs.

## FAQ

### Why can Muse Wonder API stop before its final answer?

Reasoning and visible text share a completion budget on the native API. A long reasoning pass can leave less room for the final answer. Check the finish reason and usage, reduce effort or narrow the task, and increase the route-supported completion limit only within your budget. An interrupted stream requires a separate transport diagnosis.

### Should I retry a Muse Wonder API stream from the beginning?

A new request is a new generation, not an automatic continuation of the interrupted answer. Save partial output and the request identifier, mark the answer incomplete, and decide whether to restart or ask for a continuation using explicit context. For tool workflows, persist completed actions so a retry cannot execute them twice.

### How do I validate Muse Wonder API media answers?

Use a small test image or document with known facts and ask questions whose answers require those facts. Compare the response with the original, including numbers and page references. Successful HTTP status alone does not prove that the endpoint accepted or interpreted the media correctly; inspect errors and request formats before scaling ingestion.

### How can I audit a Muse Wonder API cost discrepancy?

Record returned usage, model, route, request time and the account rate at that time. Separate uncached input, verified cache reads and total billed output, including reasoning where applicable. Compare those quantities with the billing record; check currency, rate changes and additional charges before assuming a token-accounting error.

## Conclusion

Start with one authenticated CometAPI request, confirm the returned answer, then add streaming and the capabilities your application needs. Before production rollout, validate the selected route, verify billing, enforce tool permissions and keep a rollback model. Expand traffic only when measured task success, latency and cost meet your acceptance criteria.

---

*Originally published at [https://www.cometapi.com/how-to-use-muse-wonder-api/](https://www.cometapi.com/how-to-use-muse-wonder-api/).*
