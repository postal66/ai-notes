<!-- social-ops-fingerprint:acbb3e5e225edab3d4d15f43e985af7a46c7bdf2a5dde17586af60e068dbfd99 -->
---
title: Gemini 3.6 Flash API Pricing & Migration Guide (2026)
---
# Gemini 3.6 Flash API Pricing & Migration Guide (2026)

![Gemini 3.6 Flash API Pricing & Migration Guide (2026)](https://resource.cometapi.com/gemini-3-6-flash-api-pricing-migration.png)

TL;DR

Gemini 3.6 Flash costs **$1.50/M input and $7.50/M output**, with lower output pricing and better reported coding and agent performance than Gemini 3.5 Flash. For production, use 3.6 Flash for complex reasoning and agents, while routing simpler high-volume workloads to the cheaper Gemini 3.5 Flash-Lite.

Gemini 3.6 Flash is more than another model-ID update.

For developers already using Gemini 3.5 Flash, the bigger change is economic. Google kept the input price unchanged at $1.50 per million tokens, lowered the output price from $9.00 to $7.50, and reports better performance on several coding and agentic benchmarks.

The practical question is whether those improvements are large enough to justify moving production workloads.

That answer depends on the workload. Coding agents, multimodal analysis, and multi-step tool use may benefit more than simple extraction or classification. Migration also requires a few API compatibility checks that are easy to miss if you only change the model name.

This guide covers Gemini 3.6 Flash API pricing, free-tier access, benchmark results, migration changes, Python examples, and what to test before switching production traffic.

## What Is Gemini 3.6 Flash?

Gemini 3.6 Flash is Google's newer Flash model for coding, multimodal reasoning, and multi-step agent workflows. Released on July 21, 2026, it is designed for production workloads that need stronger reasoning and agentic performance while remaining within Google's Flash model tier.

Its main specifications include:

| Item | Gemini 3.6 Flash |
| --- | --- |
| Model ID | `gemini-3.6-flash` |
| Standard input price | $1.50 / 1M tokens |
| Standard output price | $7.50 / 1M tokens |
| Standard cached input | $0.15 / 1M tokens |
| Default thinking level | `medium` |
| Input context | 1,048,576 tokens |
| Maximum output | 65,536 tokens |
| Inputs | Text, image, video, audio, PDF |
| Output | Text |
| Best suited for | Coding, multimodal reasoning, complex agents |

Google positions Gemini 3.6 Flash for workloads such as coding, spatial and multimodal reasoning, and multi-step agentic tasks.

The model also supports features including function calling, structured outputs, code execution, context caching, File Search, URL context, Google Search grounding, and Google Maps grounding.

You can review the latest specifications and migration guidance in Google's [latest Gemini model guide](https://ai.google.dev/gemini-api/docs/latest-model).

For developers coming from the previous generation, the [CometAPI Gemini 3.5 Flash API guide](https://www.cometapi.com/how-to-use-gemini-3-5-flash-api/) provides a useful integration baseline.

## How Much Does the Gemini 3.6 Flash API Cost?

Gemini 3.6 Flash costs **$1.50 per million input tokens** and **$7.50 per million output tokens** on Google's Standard paid tier.

Compared with Gemini 3.5 Flash, the input price remains unchanged, while the output price falls from $9.00 to $7.50 per million tokens - a 16.7% reduction.

Google also offers Batch, Flex, and Priority processing.

| Gemini 3.6 Flash Tier | Input / 1M | Cached Input / 1M | Output / 1M |
| --- | --- | --- | --- |
| Standard | $1.50 | $0.15 | $7.50 |
| Batch | $0.75 | $0.075 | $3.75 |
| Flex | $0.75 | $0.075 | $3.75 |
| Priority | $2.70 | $0.27 | $13.50 |

> Important:\*\* Thinking tokens are billed at the output-token rate. A short visible response can therefore consume more billable output tokens than the final answer length suggests.

Context caching can also make a meaningful difference for applications that repeatedly send the same large system prompt, repository context, document set, or conversation history.

On the Standard paid tier, Gemini 3.6 Flash cached input costs **$0.15 per million tokens**, compared with $1.50 for normal input.

### Example: 15,000 Input Tokens + 8,000 Output Tokens

Consider a task using 15,000 input tokens and 8,000 output tokens.

| Model | Estimated Cost |
| --- | --- |
| Gemini 3.5 Flash | $0.0945 |
| Gemini 3.6 Flash at the same token volume | $0.0825 |
| Gemini 3.6 Flash with 17% fewer output tokens | $0.0723 |
| Gemini 3.5 Flash-Lite at the same token volume | $0.0245 |

At identical token usage, Gemini 3.6 Flash is about **12.7% cheaper** than Gemini 3.5 Flash in this example.

Google also reports that Gemini 3.6 Flash used **17% fewer output tokens** on the Artificial Analysis Index. If a production workload reproduced that reduction, the modeled saving in this example would increase to roughly **23.5%**.

Google separately reports output-token reductions of **up to 65% on DeepSWE**. These figures measure different workloads and should not be treated as interchangeable: 17% refers to the Artificial Analysis Index, while 65% comes from a specific coding benchmark.

The basic token-cost calculation is:

```
Request cost =
(input tokens x input price + output tokens x output price) / 1,000,000
```

For agents, the real cost is broader:

```
Total task cost =
initial model call
+ retries
+ fallback calls
+ paid tools
+ grounding or search costs
```

This is why the cheapest model per token is not always the cheapest model to complete a task.

## Is Gemini 3.6 Flash Free?

Yes. Google's current Gemini Developer API pricing lists Free Tier access for Gemini 3.6 Flash Standard usage.

Free-tier availability does not mean unlimited production capacity. API limits depend on the project and usage tier, so developers should check the rate limits applied to their own project rather than relying on a fixed requests-per-minute figure from a third-party article.

For production planning, use Google's current [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) and rate-limit documentation when estimating capacity.

Developers can access Gemini 3.6 Flash through the Gemini API and Google AI Studio. Teams using a unified multi-model workflow can also test the model through the [CometAPI Gemini 3.6 Flash model page](https://www.cometapi.com/models/google/gemini-3-6-flash/).

## How Does Gemini 3.6 Flash Compare With Gemini 3.5 Flash?

Google's published results show the largest improvements in coding, agentic execution, computer use, and knowledge work.

| Benchmark | Gemini 3.6 Flash | Gemini 3.5 Flash | Change |
| --- | --- | --- | --- |
| DeepSWE | 49.00% | 37.00% | +12.0 points |
| MLE-Bench | 63.90% | 49.70% | +14.2 points |
| OSWorld-Verified | 83.00% | 78.40% | +4.6 points |
| GDPval-AA v2 | 1,421 | 1,349 | 72 |

Google also says Gemini 3.6 Flash completes multi-step workflows with fewer reasoning steps, conversational turns, and tool calls than Gemini 3.5 Flash.

The company reports:

- **17% fewer output tokens** on the Artificial Analysis Index.
- **Up to 65% fewer output tokens** on DeepSWE.
- Fewer unwanted code edits and execution loops.
- Improved multimodal and spatial reasoning.

The original results are available in Google's [Gemini 3.6 Flash launch announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/).

These benchmarks make 3.6 Flash a strong candidate for evaluation, particularly for workloads where one request can turn into several rounds of reasoning, tool calls, and corrections.

They should not, however, replace testing on your own application.

Google also notes that 3.6 Flash may perform more upfront programmatic inspection before making code changes. On a large repository, that can improve accuracy. On a narrowly scoped frontend edit, it may simply add unnecessary exploration.

Clear file boundaries, acceptance criteria, and implementation instructions still matter.

## Gemini 3.6 Flash vs Gemini 3.5 Flash-Lite: Which Should You Use?

Once you have decided that Gemini 3.6 Flash is worth testing, the next question is whether every request actually needs it.

For many production systems, the answer will be no.

Gemini 3.5 Flash-Lite is substantially cheaper and can be a better default for predictable, high-volume workloads.

| Item | Gemini 3.6 Flash | Gemini 3.5 Flash-Lite |
| --- | --- | --- |
| Standard input price | $1.50 / 1M tokens | $0.30 / 1M tokens |
| Standard output price | $7.50 / 1M tokens | $2.50 / 1M tokens |
| Standard cached input | $0.15 / 1M tokens | $0.03 / 1M tokens |
| Default thinking level | `medium` | `minimal` |
| Best suited for | Complex reasoning, coding, agents | Extraction, routing, classification |

At Standard pricing, Flash-Lite is **5× cheaper on input** and **3× cheaper on output** than Gemini 3.6 Flash.

### Start with Gemini 3.5 Flash-Lite for:

- Classification
- Request routing
- JSON and structured extraction
- Document processing
- Data transformation
- Translation at scale
- Lightweight subagents
- High-volume repeatable tasks

A practical routing strategy might look like this:

| Workload | First Route | Escalation |
| --- | --- | --- |
| Classification or routing | Gemini 3.5 Flash-Lite | 3.6 Flash after validation failure |
| Structured extraction | Gemini 3.5 Flash-Lite | 3.6 Flash for complex documents |
| Lightweight subagent | Gemini 3.5 Flash-Lite | Raise thinking level or use 3.6 Flash |
| Multi-file coding | Gemini 3.6 Flash | Stronger fallback if unresolved |
| Complex tool workflow | Gemini 3.6 Flash | Fallback after tool or validation failure |
| Multimodal reasoning | Gemini 3.6 Flash | Task-specific fallback |

For mixed production traffic, the more useful metric is:

```
Cost per successful task =
(model calls + retries + tools + fallbacks) / accepted tasks
```

A cheap first call becomes less attractive if it fails repeatedly and eventually requires a stronger model anyway.

The reverse is equally important. There is little reason to send millions of predictable classification requests to Gemini 3.6 Flash if Flash-Lite already meets the required accuracy.

For applications that need this kind of routing, see our guide to [calling multiple AI models through an OpenAI-compatible base URL](https://www.cometapi.com/how-to-call-multiple-ai-models-using-an-openai-compatible-base-url/).

## What Changes When Migrating to Gemini 3.6 Flash?

Moving from Gemini 3.5 Flash to Gemini 3.6 Flash involves more than changing the model ID.

Developers should review five areas before switching production traffic: deprecated sampling parameters, thinking controls, `candidate_count`, prefilled model turns, and function-calling state.

### 1. Remove `temperature`, `top_p`, and `top_k`

Google has deprecated these sampling controls for Gemini 3.6 Flash and Gemini 3.5 Flash-Lite:

```
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
}
```

The new models currently ignore these parameters. Google says future Gemini model generations may return an HTTP 400 error when they are supplied.

For predictable output formats, use clearer system instructions and structured outputs instead.

### 2. Replace `thinking_budget` With `thinking_level`

Gemini 3.6 Flash defaults to `medium` thinking.

Google's migration guidance recommends moving from numerical `thinking_budget` configurations to `thinking_level`.

Gemini 3.5 Flash-Lite defaults to `minimal`, which is appropriate for many high-volume extraction, classification, and routing workloads.

Higher thinking levels should be tested when the task involves multi-step reasoning, code execution, or tool use.

### 3. Remove `candidate_count`

Google lists `candidate_count` as unsupported in Gemini 3.x.

This can be easy to miss when several models share the same generation configuration. Remove it before migrating production requests.

### 4. Stop Prefilling Model Turns

Requests can no longer end with a non-empty `model` role turn.

An older application might use a payload such as:

```
{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "Translate 'Hello world' to Spanish."}]
    },
    {
      "role": "model",
      "parts": [{"text": "Translation:"}]
    }
  ]
}
```

That pattern can now return HTTP 400.

If you previously used prefilling to force an answer format, move the requirement into `system_instruction` or use structured outputs instead.

### 5. Retest Function Calling and Multi-Turn State

Tool-using agents need separate migration testing.

Google recommends using `previous_interaction_id` for server-side multi-turn state in the Interactions API.

When returning a function result, preserve both the function name and the original call ID:

```
final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
    previous_interaction_id=interaction.id,
    tools=tools,
    input=[
        {
            "type": "function_result",
            "name": step.name,
            "call_id": step.id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps(result),
                }
            ],
        }
    ],
)
```

Applications using `generateContent` should also verify their `FunctionResponse` payloads and monitor tool-call errors after migration.

See Google's [latest-model migration guide](https://ai.google.dev/gemini-api/docs/latest-model) and [function-calling documentation](https://ai.google.dev/gemini-api/docs/function-calling) for current implementation details.

## How Do You Call Gemini 3.6 Flash in Python?

Install or update Google's GenAI SDK:

```
pip install -U google-genai
```

Set your API key:

```
export GEMINI_API_KEY="your-api-key"
```

Then call Gemini 3.6 Flash:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=(
        "Review this migration plan and list the three "
        "highest-risk compatibility issues."
    ),
)

print(interaction.output_text)
```

For a task that needs more reasoning, configure the thinking level:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Analyze this multi-step debugging problem.",
    generation_config={
        "thinking_level": "medium",
    },
)

print(interaction.output_text)
```

The main migration difference can be summarized as:

```
# Older shared configuration
old_config = {
    "temperature": 0.2,
    "top_p": 0.9,
    "top_k": 40,
    "candidate_count": 1,
    "thinking_budget": 4096,
}

# Gemini 3.6 Flash
new_config = {
    "thinking_level": "medium",
}
```

Do not assume a higher thinking level is always better. Measure latency, token consumption, and completion rate on your own tasks.

## How Should You Test Gemini 3.6 Flash Before Production?

You do not need a large public benchmark suite to decide whether Gemini 3.6 Flash belongs in your production stack.

A better starting point is 30-50 recent tasks that resemble your actual traffic.

Include a mix of:

1. Coding and debugging
2. Multi-step tool use
3. Multimodal documents
4. Data extraction
5. Classification and routing

Run the same inputs through:

- Your current production model
- Gemini 3.6 Flash
- Gemini 3.5 Flash-Lite

Keep prompts, tools, validators, and acceptance criteria unchanged.

Track:

- Input tokens
- Output and thinking tokens
- Latency
- Tool calls
- Retries
- Function-call errors
- Validator pass rate
- Human correction time
- Final task success

Then compare the total cost required to produce an accepted result.

A coding request that costs $0.08 and succeeds on the first attempt may be cheaper than a $0.02 request that fails twice and eventually escalates.

At the same time, paying Gemini 3.6 Flash prices for a simple classification task makes little sense if Flash-Lite handles it reliably.

The goal is not to find one model for every request. It is to use the stronger model only where its additional capability actually changes the outcome.

Developers can compare the current [Gemini 3.6 Flash](https://www.cometapi.com/models/google/gemini-3-6-flash/) and [Gemini 3.5 Flash-Lite](https://www.cometapi.com/models/google/gemini-3-5-flash-lite/) routes through CometAPI using the same evaluation set.

## FAQ

### How much does the Gemini 3.6 Flash API cost?

Google's Standard paid rate is **$1.50 per million input tokens** and **$7.50 per million output tokens**. Standard cached input costs $0.15/M. Batch and Flex cost $0.75/M input and $3.75/M output.

### Is Gemini 3.6 Flash free?

Yes. Google's current Gemini Developer API pricing lists Free Tier Standard usage for Gemini 3.6 Flash. Free access remains subject to project and usage-tier rate limits.

### Is Gemini 3.6 Flash generally available?

Yes. Google released `gemini-3.6-flash` on July 21, 2026 and lists it as a production model in the Gemini API documentation.

### What is the Gemini 3.6 Flash context window?

Gemini 3.6 Flash supports up to **1,048,576 input tokens** and **65,536 output tokens**. It accepts text, image, video, audio, and PDF inputs and produces text output.

### Is Gemini 3.6 Flash cheaper than Gemini 3.5 Flash?

Yes for output tokens. Both models cost $1.50/M standard input tokens, while Gemini 3.6 Flash reduces the output price from $9.00/M to $7.50/M.

### Should I use Gemini 3.6 Flash or Gemini 3.5 Flash-Lite?

Use Gemini 3.6 Flash when coding quality, multimodal reasoning, or complex agent execution can reduce failures and retries. Start with Flash-Lite for high-volume extraction, classification, routing, and other predictable workloads where lower cost matters more.

### What should I change before migrating to Gemini 3.6 Flash?

Remove `temperature`, `top_p`, `top_k`, and `candidate_count`; replace `thinking_budget` with `thinking_level`; remove prefilled model turns; and retest function calling and multi-turn state management.

## Final Take

Gemini 3.6 Flash is worth benchmarking if you already use Gemini 3.5 Flash for coding, multimodal work, or agent workflows.

Its output price is lower, and Google's early results suggest that some workloads may also require fewer tokens and fewer execution steps. For agents that repeatedly reason, call tools, and retry failed actions, those savings can matter more than the headline price difference.

But that does not mean every request should move to 3.6 Flash.

Gemini 3.5 Flash-Lite is substantially cheaper and may be all you need for predictable work such as extraction, classification, and routing.

The better production strategy is to use each model where it makes economic sense: **Flash-Lite for simple, high-volume tasks; 3.6 Flash where stronger reasoning can improve the chance of finishing correctly on the first attempt.**

Then measure the result that actually matters - **the total cost of getting an accepted answer**.

To compare both models through the same workflow, see the [Gemini 3.6 Flash model page](https://www.cometapi.com/models/google/gemini-3-6-flash/) and [Gemini 3.5 Flash-Lite model page](https://www.cometapi.com/models/google/gemini-3-5-flash-lite/) on CometAPI, or review current model routes on the [CometAPI pricing page](https://www.cometapi.com/pricing/).

---

*Originally published at [https://www.cometapi.com/gemini-3-6-flash-api-pricing-migration/](https://www.cometapi.com/gemini-3-6-flash-api-pricing-migration/).*
