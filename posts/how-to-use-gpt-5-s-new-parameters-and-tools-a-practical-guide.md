<!-- social-ops-fingerprint:6ea2dff1a9a9876a7aa9557175e546133137ba9ae9325b52be04525a2d521001 -->
---
title: How to Use GPT-5’s new parameters and tools: A Practical Guide
---
# How to Use GPT-5’s new parameters and tools: A Practical Guide

![How to Use GPT-5’s new parameters and tools: A Practical Guide](https://resource.cometapi.com/blog/uploads/2025/08/How-to-Use-GPT-5s-New-parameters-and-tools.webp)

OpenAI’s GPT-5 rollout brings a familiar goal — better accuracy, speed, and developer control — but pairs it with a fresh set of API parameters and tool integrations that change how teams design prompts, call models, and hook models to external runtimes. This article explains the key changes, shows concrete usage patterns, and gives best practices for safe, cost-effective adoption.

## What new GPT-5 models, parameters and tools should I know about?

### What is GPT-5?

OpenAI now publishes GPT-5 in multiple flavors so developers can tradeoff latency, cost and capability: `gpt-5` (full reasoning model), `gpt-5-mini` (balanced), and `gpt-5-nano` (low-cost, low-latency). These sizes allow you to pick the model most appropriate for short inquiries, batch processing, or heavy reasoning tasks. GPT-5 in ChatGPT is presented as a system with “thinking” components, and an API version targets the reasoning model directly for developer use.

### New API parameters (high level)

A few surfaced parameters that change how you control output and cost are particularly notable:

- **New params:** `verbosity` (low/medium/high) to control answer length/shape, and `reasoning_effort` (now: `minimal`, `low`, `medium`, `high`) to control how much thinking the model does before replying. Use `minimal` when you want speed over deep chain-of-thought.
- **minimal / reasoning modes** — options to prefer faster, lower-reasoning replies (useful for short factual retrieval) vs extended reasoning (“thinking”) when deeper chains of thought are required.
- **Long context & tokens:** GPT-5 supports very large contexts (total ~400k tokens: ~272k input + 128k output in docs) — use this for huge documents, codebases, or long conversations.

These parameters let you tune the tradeoff between quality, latency, and cost at the call level instead of only by choosing a model size.

### New tool types and raw payload support

One of GPT-5’s most practical additions is the new **`custom` tool type** that allows the model to send *raw text payloads* to your tool runtime (for example: Python scripts, SQL statements, shell commands, or arbitrary configuration text) without requiring JSON-wrapped function calls. This reduces friction when hooking the model to sandboxes, interpreters, or databases and enables richer “software-on-demand” patterns.

**Constraining outputs:** You can enforce grammars / contracts (Context-Free Grammar, CFG) so tool payloads are syntactically valid for your runtime. Parallel tool calls + CFGs let you safely automate multi-step agentic workflows.

## How do I call the new parameters and tools in the API?

(Using the official Python SDK pattern `from openai import OpenAI` and the Responses API as in the docs.)

### 1) Set verbosity + reasoning\_effort

```
from openai import OpenAI
client = OpenAI(
    base_url="https://api.cometapi.com/v1/responses",
    api_key="<YOUR_CometAPI_KEY>",
)

resp = client.responses.create(
    model="gpt-5",
    input="Summarize the following meeting notes in one short paragraph: ...",
    parameters={
        "verbosity": "low",            # low / medium / high

        "reasoning_effort": "minimal", # minimal / low / medium / high

        "max_output_tokens": 200
    }
)

print(resp.output_text)  # SDK convenience property aggregates returned text
```

This returns a short, fast answer when you want latency + brevity.

### 2) Call a custom tool with a raw text payload (free-form)

```
# Example: send a raw SQL query (not JSON) to your "sql_runner" custom tool

from openai import OpenAI
client = OpenAI(
    base_url="https://api.cometapi.com/v1/responses",
    api_key="<YOUR_CometAPI_KEY>",
)

resp = client.responses.create(
    model="gpt-5",
    input="Fetch the average order value for last month and return a SQL query only.",
    tools=[
        {
            "name": "sql_runner",
            "type": "custom",
            "description": "Executes raw SQL and returns results."
        }
    ],
    parameters={
        "verbosity": "medium"
    }
)

# The model can emit text that the tool receives directly (raw SQL)

# How your backend receives and executes the model->tool payload depends on your webhook/runtime.
print(resp.output_text)
```

Use CFG if the SQL must follow strict syntax or allowed patterns. (, )

### 3) Example: require a constrained output with CFG

```
# Pseudocode / conceptual example for attaching a grammar to a tool call.

client.responses.create(
    model="gpt-5",
    input="Generate a safe shell command to list .txt files.",
    tools=[{
        "name":"shell_exec",
        "type":"custom",
        "description":"Runs a shell command in a sandbox",
        "grammar": "COMMAND -> 'ls' ' ' DIR_FILTER; DIR_FILTER -> '*.txt' | '-la *.txt'"
    }],
    parameters={"verbosity":"low"}
)
```

The `grammar`/CFG ensures GPT-5 only outputs allowed command patterns accepted by your runner.

### How do I register and use a `custom` tool to send raw payloads?

The `custom` tool is defined when you register tools in your system. The tool receives plain text (not structured JSON), so your runtime must be ready to parse and validate it.

1. **Register the tool** (server side; pseudodefinition):

```
{
  "name": "code_executor",
  "type": "custom",
  "description": "Runs Python code in a sandbox and returns output or errors."
}
```

2. **Model invokes the tool** — example assistant instruction (what the model produces when it wants to call the tool):

```
<tool name="code_executor">
print(run_tests_on_module('payment_processor'))
</tool>
```

3. **Your runtime executes** the raw text safely (sandboxed), returns an output string back to the API or to your agent loop, and the model continues the conversation using the returned text.

## How should prompt engineering change with GPT-5’s new options?

### When should I use “thinking” (extended reasoning) vs minimal responses?

Use thinking/extended-reasoning modes for tasks that require stepwise deduction, multi-stage planning, or code generation that must respect constraints. Reserve minimal-reasoning or `mini/nano` for short queries, retrieval tasks, and large fan-out workloads (e.g., scoring many candidates). When accuracy is critical (finance, law, diagnosis), prefer the higher-reasoning/default `gpt-5` and add post-checks. OpenAI still emphasizes that GPT-5 is not AGI — it enhances capabilities but is not a perfect source of truth — so pick reasoning modes accordingly.

## What are best practices for integrating GPT-5 with external runtimes and tools?

### How should I design the tool runtime architecture?

- **Isolate** tool execution environments: per-request ephemeral containers or dedicated sandboxed processes.
- **Rate-limit and quota** tool usage separately from the model API to control cost and risk.
- **Audit logs**: log tool inputs, outputs, and the model’s decision to invoke the tool for postmortem and compliance.
- **Error handling**: design the runtime to return structured error codes and a short human-readable message so the model can retry, fall back, or explain the error.

### What security controls are essential?

- **Static analysis** for code received as raw text, white-listing allowed modules and runtime APIs.
- **Network isolation** and strict egress rules for containers.
- **Secrets management** — never expose service-account keys directly to the model; use ephemeral tokens generated by your backend if remote access is required.
- **Human-in-the-loop gating** for high-risk operations (financial transactions, deployments). These are standard safety patterns for tool-enabled agents.

### Practical tips & best practices

- **Pick `verbosity` not prompt surgery.** Use `verbosity` to tune length/level-of-detail instead of rewriting prompts repeatedly.
- **Use `reasoning_effort` for cost/latency tradeoffs.** Set `minimal` for quick fact retrieval or UIs, `high` for complex reasoning tasks.
- **Tool safety:** always validate/escape any raw text the model emits before executing it. Use CFGs and server-side sanitization as a second line of defense. (Cookbook warns about tool-security practices.)
- **Parallel tool calling:** you can issue several tool calls at once for speed (e.g., web search + DB lookup), then have the model synthesize the results. Good for agentic flows.
- **Structured outputs when you need them.** If your consumer needs JSON, use Structured Outputs / JSON Schema support. Use free-form only when raw text is more natural for the target runtime.
- **Streaming & long outputs:** use streaming to process long outputs (especially with huge token budgets) while they generate.

## How do I measure, test, and optimize performance and cost?

### What metrics should I track?

- **Tokens per request** and **cost per call** (use model size + verbosity to estimate).
- **Latency (p95/p99)** and **error rates** — especially for requests that trigger external tool execution.
- **Quality metrics**: automated check success rates, human validation rates, hallucination frequency on gold tests.

### How to run experiments

- A/B model sizes (`gpt-5` vs `gpt-5-mini`) on a representative workload to measure accuracy vs cost. For workloads that need many short answers, `mini` or `nano` often reduces cost dramatically while preserving acceptable accuracy. Vendor and press coverage highlights these tradeoffs in early benchmarks; run your own tests on critical tasks.

## What are the limitations and responsible-use considerations?

### Is GPT-5 AGI or infallible?

OpenAI positions GPT-5 as a substantial improvement in usability and reasoning, not AGI. Expect meaningful capability gains (coding, math, multi-step reasoning), but also occasional errors and hallucinations. Plan product workflows that verify model outputs for correctness before automated execution in sensitive domains.

### Compliance, privacy and data governance

- Treat prompts and model outputs as sensitive: mask PII before sending to the API if your policy forbids sending such data.
- Understand retention and usage policies in the OpenAI terms for your account/region. Use enterprise contracts for stronger data protections if required.
- Document and disclose the model’s role to end users where decisions materially affect them (transparency requirements in many jurisdictions).

## Quick checklist and code patterns to get started

### Pre-launch checklist

1. Choose target model (accuracy vs cost): `gpt-5`, `gpt-5-mini`, or `gpt-5-nano`.
2. Define `verbosity` defaults for each endpoint (e.g., API endpoints that power quick search vs deep analysis).
3. Register and harden `custom` tool runtimes (sandboxing, validators, logs).
4. Add automated verification steps for any tool output executed on your systems.
5. Create monitoring dashboards for tokens, latency, and model-quality metrics.

### Example orchestration pattern (pseudocode)

1. User request → choose model & verbosity (routing logic).
2. System prompt defines tool syntax + reasoning mode.
3. Send chat completion request.
4. If assistant invokes `custom` tool: validate payload → execute in sandbox → return result to assistant → assistant finalizes response.
5. If operation is high-risk: require human approval.

## Use GPT-5 in CometAPI

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

For the definitive references , review OpenAI’s the Cookbook entry on GPT-5 params and tools — these are the primary sources for API fields, tool registration, and usage patterns.

## Final thoughts

GPT-5’s combination of model sizes, new parameters such as `verbosity`, and `custom` tool raw-payload support creates powerful new options for product teams — from lower-cost massive scoring jobs to “software-on-demand” workflows where the model generates code or SQL that your safe runtime executes. The tradeoffs are familiar: capability vs cost, speed vs depth, and automation vs human supervision. Start small (pick a single discovery use case), instrument heavily, and iterate — design your tool runtimes and prompts so the model’s outputs are *verifiable* before they become actions.

Developers can access [GPT-5](https://www.cometapi.com/gpt-5-api/) , GPT-5 Nano and GPT-5 Mini through CometAPI, the latest models version listed are as of the article’s publication date. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

You can use Cpmr’s gpt-5 API to experiment with new parameters. Just replace the openAI key with the CometAPI key.You can use CometAPI’s gpt-5 API to experiment with new parameters. Just replace the openAI key with the CometAPI key.Two Choice: [Chat Completions function-calling pattern](https://apidoc.cometapi.com/) and [Response function-calling pattern.](https://apidoc.cometapi.com/)

Passing CoT exists only in the Responses API,this improves intelligence, reduces the number of inference tokens generated, improves cache hit rates, and reduces latency. Most other parameters remain the same, but the format is different.So We recommend using [Response](https://apidoc.cometapi.com/) format to access gpt-5 in CometAPI.

---

*Originally published at [https://www.cometapi.com/how-to-use-gpt-5s-new-parameters-and-tools/](https://www.cometapi.com/how-to-use-gpt-5s-new-parameters-and-tools/).*
