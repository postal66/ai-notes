<!-- social-ops-fingerprint:7332f0fdcbd5207bf63dee39317378a3b9dd756b8110c7178fc8e20edfed60ac -->
---
title: How to Use GPT-5.4 API: Parameters and Tools Usage Guide
---
# How to Use GPT-5.4 API: Parameters and Tools Usage Guide

![How to Use GPT-5.4 API: Parameters and Tools Usage Guide](https://resource.cometapi.com/gpt-5.4-1.jpg)

On March 5–7, 2026, OpenAI publicly rolled out **GPT-5.4**, a frontier model explicitly tuned for professional, document-heavy, and agentic workflows. The release highlights three converging advances: (1) substantially larger context windows (≈1,050,000 tokens), (2) a new “reasoning” capability that lets developers control internal reasoning effort, and (3) first-class **computer-use / tool orchestration** and improved multimodal understanding (text + images + screenshots). These features make GPT-5.4 especially well suited to tasks like spreadsheet modeling, contract review, slide generation, multi-step agentic workflows and writing code that operates live systems.

You can experience [GPT-5.4](https://www.cometapi.com/models/openai/gpt-5-4/) in [CometAPI](https://www.cometapi.com/), A higher-compute variant — [**GPT-5.4 Pro**](https://www.cometapi.com/models/openai/gpt-5-4-pro/) — is available for the hardest reasoning and multi-turn workloads.

## What is GPT-5.4 (including the *Thinking* and *Pro* variants)

### The model family, at a glance

GPT-5.4 is positioned as the “frontier” GPT-5 model for **complex professional work**: long-form documents, code, multi-step reasoning, and agentic workflows. The release folds together capabilities previously split between Codex (coding) and the GPT line — so you get one model that can code, reason, use tools, and manage long contexts. The official model guide lists `gpt-5.4` as the default for most work and `gpt-5.4-pro` for the toughest problems.

Key specs (official):

- **Context window**: ~1,050,000 tokens (≈ 700–800k words of English), enabling very large inputs like entire book drafts, multi-file codebases, or long legal documents.
- **Max output tokens**: reports indicate very large outputs supported (e.g., up to 128,000 tokens in some Pro configurations).
- **Variants:** `gpt-5.4` (default), `gpt-5.4-pro` (more compute, longer thinking), and lighter/mini models for cost-sensitive use.

### “Thinking” and “Pro” explained

- **GPT-5.4 Thinking**: a tuned mode for *interactive reasoning*. It emphasizes plan-first workflows — the model may present an upfront plan (an “upfront plan”) before generating full results, allowing mid-generation steering and reducing wasted token spend on wrong directions. This mode improves visibility into the model’s intended steps and makes long tasks safer and more controllable.
- **GPT-5.4 Pro**: the high-compute sibling for the hardest problems — deeper chain-of-thought, larger internal compute budgets, and more deterministic/stable results on difficult benchmarks. It’s exposed in the Responses API and is intended for multi-turn, heavy reasoning tasks (expect higher latency and cost).

---

## Key improvements & new features in GPT-5.4

### Massive context windows (≈1,050,000 tokens)

This is one of the headline improvements: a model that can consume and reason over *whole books*, multi-file codebases, or enterprise document sets without streaming them in piecemeal. Practically, that simplifies tasks like end-to-end contract review, full-document summarization, and multi-document Q&A. Use cases: legal due diligence, technical audits, and agent logs.

**Practical note:** the larger context window changes system design — instead of chunking aggressively, you can now keep more “global” state in context, but you should still use compaction (see Parameter Control) to keep costs sensible.

### Native computer use & tool integrations

GPT-5.4 is the first general-purpose model with **native computer-use capabilities**: generating sequences of browser or OS actions (Playwright scripts, keyboard/mouse events), reading screenshots, interacting with web UIs and orchestrating multi-tool workflows. This is a major step toward building autonomous agents that perform real tasks end-to-end.

GPT-5.4 includes built-in **computer use**: the model can interact with local/remote software agents, call connectors, manipulate spreadsheets, take screenshots, and automate multi-step workflows when permitted. That reduces glue code: instead of building fragile instruction wrappers, the model can operate in a build-run-verify-fix loop (agentic behavior) using documented tool APIs. This is a big step toward safe, practical autonomous agents.

### Reasoning modes & `reasoning.effort`

A tunable `reasoning.effort` parameter allows you to control how much internal compute the model invests in chain-of-thought and solution search (options: `none`, `low`, `medium`, `high`, `xhigh`). Higher effort yields better answers for complex problems but costs more and increases latency — ideal for `gpt-5.4-pro`.

### Upfront planning / interactive plans

“Upfront plans” let the model output a short plan before executing a long generation. That plan can be inspected and modified by the developer or user, minimizing wasted outputs and enabling mid-task course corrections (great for long document creation or multi-step analyses).

### Better multimodal/document skills

Benchmarks and internal evaluations released with the model show big gains on spreadsheet tasks (example internal spreadsheet eval: GPT-5.4 mean 87.3% vs GPT-5.2 68.4%) and human preference for presentation outputs (presentations from GPT-5.4 preferred 68% vs GPT-5.2 in human trials). The company also reports reductions in factual errors (individual claim false-rate down ~33%, full response error rate down ~18% versus GPT-5.2).

## How to use the GPT-5.4 API (Responses API / Chat API )

[GPT-5.4 pro](https://www.cometapi.com/models/openai/gpt-5-4-pro/) only supports response access. [GPT-5.4](https://www.cometapi.com/models/openai/gpt-5-4/) (thinking) supports chat and responses. CometAPI( a one-stop aggregation platform for large model APIs with discounts) offers GPT-5.4 Series, two access methods and a compatible helpful playgrounds).

> Note: the Responses API is the recommended integration for GPT-5.x models because it directly supports reasoning parameters, tool registration, and the larger context sizes.

### Python — Responses API (illustrative)

```
# pip install openai (or use the official package named in docs)
from openai import OpenAI
import os

api_key = os.environ.get("OPENAI_API_KEY")  # or set env var
client = OpenAI(api_key=api_key)

resp = client.responses.create(
     model="gpt-5.4-pro-2026-03-05",
    input="How much gold would it take to coat the Statue of Liberty in a 1mm layer?",
    reasoning={"effort": "high"},          # hidden internal reasoning tokens used
    max_output_tokens=4096,               # keep below max output limit for your use case
    temperature=0.0,                      # deterministic for legal/technical tasks
    tools=[                                # optionally register tools the model can call
        {
            "name": "file_search",
            "type": "file_search",
            "config": {"root": "/mnt/data/contracts"}
        }
    ],
    response_format={"type":"json", "json_schema":{
        "name":"redlines",
        "schema":{"type":"object","properties":{"summary":{"type":"string"},"redlines":{"type":"array","items":{"type":"object"}}}}
    }}
)

print(resp.output_text)  # final model answer
```

**Notes**: `reasoning` is an object controlling internal effort; `tools` registers available tool interfaces for the model to call; `response_format` enforces structured output. The `reasoning.effort` label values available range from `none` (fastest) up to `xhigh` (most internal effort) depending on SDK and provider support. Use low effort for simple summaries; raise it for complex, multi-step tasks.

### Crul— chat API (illustrative)

```
curl --location --request POST 'https://api.cometapi.com/v1/chat/completions' \
--header 'Authorization: Bearer ' \
--header 'Content-Type: application/json' \
--data-raw '{
  "model": "gpt-5.2\4",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello!"
    }
  ]
}'
```

## Using tools with GPT-5.4 (Computer Use, connectors, and agents)

GPT-5.4’s most practical leap is its agentic, tool-aware behavior: it can discover and call the right tool, operate on spreadsheets and UIs when authorized, and reason about the actions it will take.

GPT-5.4 is *designed* to work with tools. There are three major tool classes to consider:

1. **Hosted tools** (e.g., `web_search`, `file_search`) — model can call these as part of the response loop. Great for retrieving up-to-date info or vector DB lookups.
2. **Custom tools / function calling** — your own server endpoints or function schemas. Declare functions (schemas) so the model returns structured outputs that your code executes.
3. **Computer use** — model emits GUI actions and expects a harness to execute them (clicks, typing, screenshots). This is powerful but **high risk**.

When you have dozens/hundreds of tools, pass `tool_search` and let the model discover relevant tool schemas at runtime. This reduces token usage and caches performance across deployments.

### How tool integration works (conceptual)

1. **Tool discovery**: model finds available connectors (e.g., Google Sheets, Salesforce, internal DB) based on a catalog.
2. **Plan & permission**: model outputs an upfront plan describing which tools it will call and why; this is reviewed and approved.
3. **Call & verify**: model calls tools (via connectors or action APIs), reads results, and runs verification checks (or asks for human confirmation).
4. **Fix loop**: on failures, the model attempts repairs or asks for guidance.

This pattern reduces brittle custom orchestration and centralizes logic in the model, but it requires strict access controls and audit logs.

### Calling with **tools** (web\_search / file\_search / computer use)

The Responses API supports passing a `tools` array. The model can choose tools (hosted tools like `web_search`, `file_search`), or you can pre-declare and restrict tools. Example: ask the model to use web search.

```
response = client.responses.create(    model="gpt-5.4",    input="What are the three most-cited 2025 papers on federated learning?",    tools=[{"type": "web_search", "name": "web_search"}],    tool_search={"enabled": True})
```

If you pass many tool definitions, `tool_search` allows GPT-5.4 to **defer** loading most tools and only load the relevant ones — crucial for large tool ecosystems.

## GPT-5.4 Parameter Compatibility and Control Guide

Traditional LLM parameters still exist but **are restricted depending on reasoning mode**.

### Core GPT-5.4 API Parameters

reasoning.effort: The following parameters are **fully supported and recommended** when calling GPT-5.4. Controls how much internal reasoning the model performs before generating the final output.

Supported values:

```
nonelowmediumhighxhigh
```

Example:

```
response = client.responses.create(    model="gpt-5.4",    reasoning={"effort": "high"},    input="Explain the Nash equilibrium in game theory.")
```

Effects:

| Value | Behavior |
| --- | --- |
| none | Fastest response |
| low | Lightweight reasoning |
| medium | Default balance |
| high | Strong reasoning |
| xhigh | Maximum reasoning depth |

Higher reasoning effort generally increases:

- answer accuracy
- reasoning tokens
- latency
- cost

The default level is typically **medium**.

### Tools

Defines tools the model can call. `tools` + `tool_search`

- `tool_search` defers loading of tool definitions for efficiency; enable it for large tool sets.
- `tools` declares tool definitions (web\_search, file\_search, custom RPCs).

Supported built-in tools include:

- web search
- file search
- code interpreter
- image generation

Example:

```
tools=[{
   "name":"get_weather",
   "description":"Get current weather",
   "parameters":{
      "type":"object",
      "properties":{
         "city":{"type":"string"}
      }
   }
}
```

### Sampling Parameters (Randomness Control)

Important compatibility rule: When **reasoning.effort ≠ none**, some sampling parameters may not be supported. If `reasoning.effort` is `high`, the request may fail or ignore `temperature`.

GPT-5.4 models disable parameters like:

- `temperature`
- `top_p`
- `logprobs`

because reasoning models control sampling internally.

1. `temperature` Controls randomness in token sampling.

| Value | Effect |
| --- | --- |
| 0.0 | deterministic |
| 0.2–0.4 | stable |
| 0.7 | balanced |
| 1.0 | highly creative |

Example:

```
{ "model": "gpt-5.4", "temperature": 0.2, "reasoning": { "effort": "none" }}
```

If `reasoning.effort` is `high`, the request may fail or ignore `temperature`.

2. `top_p`: Nucleus sampling parameter.

| Value | Meaning |
| --- | --- |
| 0.9 | consider top 90% probability tokens |
| 0.5 | conservative generation |
| 1.0 | full distribution |

3. stop: Stops generation when encountering specific tokens.

Useful for:

- code generation
- tool pipelines
- chat delimiters

### Verbosity: Controls response length.

Several **new parameters appeared starting with GPT-5 models**, including GPT-5.4.

Values:

```
lowmediumhigh
```

Example:

```
verbosity="high"
```

Use cases:

| Value | Behavior |
| --- | --- |
| low | concise answers |
| medium | balanced |
| high | long explanations |

This parameter helps control output length without manipulating token limits.

### Parameter Differences of GPT-5.4

Below is a simplified compatibility chart.

| Parameter | reasoning:none | reasoning:low+ |
| --- | --- | --- |
| temperature | ✓ | ✗ / ignored |
| top\_p | ✓ | ✗ |
| logprobs | ✓ | ✗ |
| max\_output\_tokens | ✓ | ✓ |
| tools | ✓ | ✓ |
| tool\_choice | ✓ | ✓ |
| verbosity | ✓ | ✓ |
| reasoning.effort | ✓ | ✓ |

### Comparison of GPT-5.4 and GPT-5.4-Pro parameters and capabilities

| Feature | GPT-5.4 | GPT-5.4-Pro |
| --- | --- | --- |
| Reasoning flexibility | Full range from none → xhigh | Only medium → xhigh |
| Latency | Lower | Higher (complex tasks may take minutes) |
| Cost | Lower | Higher due to additional compute |
| Background execution recommended | Optional | Recommended for long tasks |
| Supported Reasoning Levels | none, low, medium, high, xhigh | medium, high, xhigh |

## Best practices for adopting GPT-5.4 in production

### 1) Start small, then increase reasoning

- Begin with `reasoning.effort=none`/`low` + `text.verbosity=low` for latency-sensitive endpoints.
- For complex flows, move to `medium` then `high` only after A/B testing cost vs accuracy.

### 2) Prefer structured outputs for programmatic tasks

Use **function schemas** or Pydantic/JSON schemas so the model returns machine-parsable outputs; reduces downstream parsing errors.

### 3) Keep humans in the loop for high-impact decisions

Any workflow that involves money, legal outcomes, or personal data should require human approval before external effects.

### 4) Limit exposed capabilities

Use `allowed_tools` lists (deny by default) and granular tool permissions. For computer use, enforce a strict action whitelist.

### 5) Cost & token budgeting

Use `max_output_tokens` and `text.verbosity` for predictable costs. For very large contexts, paginate or compress content where appropriate—even with 1M tokens, compaction/selection strategies help reduce cost.

## Closing notes — migration and next steps

GPT-5.4 represents a meaningful step forward in building AI systems that can **think more**, **work across software**, and **handle very large contexts**. For most teams, the recommended migration path is:

1. **Prototype** with a small subset of workflows (e.g., contract review, slide generation) using the `gpt-5.4` alias in a sandbox.
2. **Measure** task accuracy, token usage, latency and cost vs prior models.
3. **Harden** by adding structured outputs, tool guards, and human approvals for risky flows.
4. CometAPI’s API discounts can be able to solve if cost or latency requirements push that choice.

Developers can access [GPT-5.4](https://www.cometapi.com/models/openai/gpt-5-4/), [GPT-5.4-pro](https://www.cometapi.com/models/openai/gpt-5-4-pro/), API via [CometAPI](https://www.cometapi.com/) now.To begin, explore the model’s capabilities in the [Playground](https://blendspace.ai/chat) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up fo GPT-5.4 today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-use-gpt-5-4-api/](https://www.cometapi.com/how-to-use-gpt-5-4-api/).*
