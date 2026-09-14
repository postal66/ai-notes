<!-- social-ops-fingerprint:993e0a323ed253a6f64760b0efceca06400e346bf523a678d2bb874fd12e8b1b -->
---
title: How to access and use Minimax M2 API
---
# How to access and use Minimax M2 API

![How to access and use Minimax M2 API](https://resource.cometapi.com/blog/uploads/2025/10/How-to-access-and-use-Minimax-M2-API.webp)

MiniMax M2, a new generation large language model optimized for agentic workflows and end-to-end coding. MiniMax publicly released MiniMax-M2 and published weights on Hugging Face; it’s an MoE (sparse) model with a very large total parameter budget but a much smaller active set per token, and it supports very large contexts (200k+ tokens).

The Minimax M2’s design is indeed excellent, and I believe developers are eager to experience its features. Here are some solutions for using the M2, as well as advanced techniques that can be used as a reference. For using the Minimax M2, I recommend CometAPI. This article explains what M2 is and its key features, compares hosted API access vs self-hosting, lays out pricing and practical examples for calling the model, and finishes with advanced optimization and tooling techniques to get production-grade performance and cost efficiency.

## What is MiniMax M2?

MiniMax M2 is the latest flagship from MiniMax: an open-weights, mixture-of-experts (MoE) style text model designed for “agentic” workflows (tool-use, code, multi-step reasoning) and long context work. Public reporting and community documentation describe M2 as a very large model (hundreds of billions of parameters in total under an MoE design, with a substantially smaller number of active parameters used per pass) that targets high throughput and cost efficiency while supporting large context windows for complex multi-file, multi-tool tasks. Independent benchmarkers and recipe maintainers have quickly added MiniMax M2 to vLLM/Ollama/other inference stacks, and MiniMax publishes APIs and developer docs for the model and its agent tools.

**Why M2 matters:** MiniMax M2 is positioned to be the practical choice for organisations building agentic systems — assistants that need to call tools, edit files, maintain long-lived context, and move fast on inference cost. Early analyses show strong capability per dollar on common benchmarks for coding, mathematics, and tool use.

## Core features and architecture

### Mixture-of-Experts, large total parameters but small active footprint

M2 is reported to contain a very large total parameter count (reporting ranges around hundreds of billions), while only activating a much smaller number of parameters per forward pass — MiniMax publish materials highlight ~**230B total parameters** with an **active parameter footprint on the order of ~10B** for inference. That tradeoff is what gives M2 its claim to high capability with comparatively low per-token compute and latency (typical MoE benefits: high model capacity, lower activation cost).

### Long context support

MiniMax advertises very large context windows for M2 (targeting enterprise-scale long contexts). Some platform docs in the release materials note support for extremely large token windows (tens to hundreds of thousands of tokens), which is useful for multi-document coding tasks, long agent traces, and retrieval-augmented flows. (If you plan to use very long context, test the provider’s practical limits: providers sometimes impose rollout or engineering limits even when model architecture supports extreme windows.)

### Agent-native tooling and coding focus

MiniMax M2 is explicitly tuned for tool calling and multi-step automation (shell/browser/Python tool integrations), and for coding workflows (multi-file edits, run-fix cycles, test-based repairs). Expect better zero-shot tool orchestration behavior and improved “follow-through” on multi-step developer tasks compared with generic chat models.

## How can developers use and access MiniMax M2?

You have two main operational paths: **use the hosted API** (fast, low friction) or **self-host** the model (more control, potentially lower marginal cost at very high scale or for privacy reasons). Below are practical, runnable steps for both.

### Option A — Hosted API (recommended for most teams)

[CometAPI](https://www.cometapi.com/) exposes [MiniMax M2](https://www.cometapi.com/minimax-m2-api/) behind an OpenAI-compatible HTTP surface so you can call the model with the same chat/completion patterns you already use — simply sign up, get a `sk-...` API key, point your client at CometAPI’s base URL, and request the `minimax-m2` model. CometAPI offers a playground, free trial tokens, and cost discounts versus the vendor’s direct hosted price, which makes it an attractive path for rapid prototyping and production migration.

**When to choose this:** quick integration, small teams, production deployment without managing inference infra, or when you value automatic model updates and monitoring.

**Steps (hosted API):**

1. Create an account on CometAPI and log in.
2. From the dashboard (Console / Tokens), create or copy an API token — keys look like `sk-XXXXX`. Store this in your secrets manager or environment variables; do not commit it. CometAPI gives limited free tokens for testing in many accounts..
3. CometAPI’s HTTP surface is OpenAI-compatible. Change your client’s **base URL** to `https://api.cometapi.com/v1/chat/completions` and then use OpenAI-style JSON payloads (e.g., `model`, `messages`, `max_tokens`, `temperature`). This means most OpenAI SDK code works with a small change to `api_base` / `base_url`.
4. Choose the model string: Use the model name published by CometAPI for MiniMax M2 — commonly `minimax-m2` (the CometAPI model page shows the model and sample usage).
5. **Make calls** — A generic curl example (OpenAI-style JSON) looks like:

```
curl -X POST "https://api.cometapi.com/v1/chat/completions" \
  -H "Authorization: Bearer $CometAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-m2",
    "messages": [
      {"role":"system","content":"You are a helpful coding assistant."},
      {"role":"user","content":"Refactor this function to be async..."}
    ],
    "max_tokens": 1024,
    "temperature": 0.2
  }'
```

> Note: replace the endpoint and parameter names with the exact values from CometAPI’s API docs; MiniMax documents OpenAI-compatible patterns and agent primitives in their developer portal.

A common pattern is:

1. **Planner** — produce a stepwise plan (e.g., fetch data, call web, run tests).
2. **Actor** — call tools (APIs, shell, code execution) as specified by the plan.
3. **Verifier** — run tests or checks and loop back if failure.

MiniMax M2’s training and configuration emphasize these interleavings, so the model tends to produce well-formed tool calls and structured outputs when given the scaffold.

**Integration tips for hosted API**

- Use **streaming** where supported to reduce perceived latency for users and allow partial output handling.
- Implement **rate limiting & retry logic** for transient failures.
- **Token accounting**: build logging to track input vs output tokens per request so you can monitor spend and set alerts.

### Option B — Self-hosting (recommended when you need isolation, custom infra, or very high sustained throughput)

**When to choose this:** compliance/privacy needs (data residency), very high throughput where amortized infra can be cheaper, or custom modifications to the stack.

**Requirements & ecosystem**

- **Hardware:** MoE models’ active parameter footprint may be small (10B active), but the physical model files, expert tables and routing logic have memory/IO implications. Large GPU memory (A100/H100 class or multi-GPU clusters), fast NVMe for model shards, and a high-bandwidth interconnect (NVLink/InfiniBand) are typical for production. Offloading strategies and quantization can reduce requirements.
- **Inference stack:** vLLM, Ollama, and other community stacks have M2 recipes and docs. Use vLLM for throughput and multi-tenant serving; Ollama provides an easier local dev loop.
- **Containerisation & orchestration:** pack the model server into containers (Docker) and run with Kubernetes / Autoscaler for production.

**Basic self-hosted flow (high level)**

1. **Obtain weights** (follow license & usage terms) from MiniMax distribution or official mirrors. Because MiniMax M2 weights are open, the community provides packaging and recipes.
2. **Choose an inference engine** — vLLM for high throughput, or a runtime like Ollama for local/testing. Install and configure the engine.
3. **Serve the model** — run the vLLM or chosen server with model path and tune GPU/parallelism settings.
4. **Front the server** with your own API gateway that mirrors the headers/semantics your application expects (e.g., OpenAI-style or a custom RPC). Add auth, logging, and rate limits.

vLLM and similar runtimes optimize for throughput and memory efficiency. MiniMax published vLLM recipes and example configs for running M2 with GPU memory partitioning and efficient dispatch, Example (conceptual)::

```
# Example: launch vLLM server (stylized)

vllm_server --model-name MiniMaxAI/MiniMax-M2 \
            --num-gpus 4 \
            --dtype fp16 \
            --max-seq-len 8192
# Client snippet to call vLLM server

from vllm import Client
client = Client("http://localhost:8080")
resp = client.generate("Implement a Unix-style recursive directory listing in Python.")
print(resp.get_completions().text)
```

## Hosted API vs Self-hosting from a cost perspective

### Hosted API — pros & cons

- **Pros:** Simple billing (per token), managed throughput, SLAs, lower engineering lift. Published token prices are extremely low for many use-cases (good starting point for experiments).
- **Cons:** Per-token pricing still scales with usage; output tokens are billed at higher rate; less control over latency/throughput tuning, and vendor lock for specialized routing or private data handling.

### Self-hosted — pros & cons

- **Pros:** Pay one-time infra & ops cost (GPUs + infra) and gain control over quantization, batching, and throughput tuning; potential to reduce $/token for extremely high-volume steady workloads. MoE models like M2 can be cheaper to serve per token when run with correct parallelism and quantization.
- **Cons:** High up-front capital and ops: cluster design (H100/A100/A800/H200), networking, expert parallelism, load balancing. Expert parallelism / vLLM recipes are non-trivial to tune. Also, if you need strict maintenance/uptime, managed hosting can still be less expensive overall.

### Simple decision heuristic

- If you expect **low-to-medium traffic** or want speed-to-market: start with hosted API.
- If you expect **sustained, very high throughput** (millions+ tokens/day) and can staff ops, run a cost model comparing hosted per-token billing vs estimated infra/ops amortized costs; MoE self-hosting often becomes attractive at scale.

## Price & commercial options

MiniMax lists per-token pricing on its platform pricing pages (example published rates mid-release): **input tokens ≈ $0.3 per 1M tokens** and **output tokens ≈ $1.2 per 1M tokens** on their platform.

**Hosted vs hidden costs:** If you use a hosted API you’ll pay the published API rates and can avoid ops and GPU capital expenditure. If you self-host, expect GPU, storage, networking and engineering costs: MoE models require specific runtime support and can impose different memory/IO profiles than dense models (see self-hosting section above).

### Pricing on CometAPI for MiniMax M2

CometAPI lists model-specific pricing on its model pages. For MiniMax M2, CometAPI’s page reports example pricing and a promotional discount relative to the vendor:

- **Input tokens:** ~$0.24 per 1M tokens
- **Output tokens:** ~$0.96 per 1M tokens
- CometAPI advertises discounts (e.g., “~20% off official price” on some listings) and often a free token allotment for trial accounts. Always verify the price on the model page and your account billing screen before large runs.

**Practical note:** CometAPI bills you for the requests routed through its gateway. That means you get centralized billing and usage reports for models you call through CometAPI (convenient for multi-model teams).

## Prompt & message protocol (practical templates)

Below are copy/pasteable templates for a robust ReAct-style protocol. They are OpenAI-style chat messages (works with CometAPI or any OpenAI-compatible gateway).

### System instruction (keeps model in agent mode)

```
System: You are an agentic assistant. For each turn, follow this strict structured format in the assistant output:

1) THOUGHT: a short plan or reasoning step (internal).
2) ACTION: one of:
- CALL_TOOL(name, args_json)  // request me to run a tool
- FINAL_ANSWER: <short text>  // when finished
3) RATIONALE: one-sentence justification for the action (optional).

Only include one ACTION per assistant reply. Do not output tool results. Wait for the tool result (OBSERVATION) from the environment and then continue. Use concise tokens to reduce cost.
```

### Assistant example (what the model returns)

```
Assistant -> (to server):

THOUGHT: Need latest release notes to verify API changes.
ACTION: CALL_TOOL("web_search", {"query":"MiniMax M2 release notes Oct 2025"})
RATIONALE: Confirm model behavior for agentic tool schema.
```

### Environment / server sends tool output back as user/system message

```
System: TOOL_RESULT for CALL_TOOL("web_search", ...):
OBSERVATION: {"top_result_title":"MiniMax M2 v1.2 release notes", "snippet":"...agent APIs updated..."}
```

Then the model continues with another thought/action.

### Final user-facing answer (after verification)

```
Assistant -> (to user):

FINAL_ANSWER: "MiniMax M2 now supports function-style tool calls. To call it, use ... ."
```

---

## Advanced techniques (increase robustness & capability)

### 1) Tree-of-Thoughts and branching search

Instead of a single linear thought path, expand multiple candidate actions/plans in parallel, evaluate them (via the model or a scoring function), and explore the most promising branches. Use when tasks are hard (complex planning, puzzles, multi-step coding with many options).

- Maintain a beam of partial solutions.
- Score branches by heuristics: factuality check, tool success rate, or predicted utility.
- Prune low-scoring branches to control cost.

### 2) Self-consistency & ensemble

Generate multiple independent solution traces (different temperatures, seeds). Aggregate final answers by majority voting or quality scoring. Reduces single-run hallucinations.

### 3) Calibration of thinking vs acting

- Use **low temperature** for actions (deterministic, reliable tool calls).
- Use **higher temperature** for brainstorming/planning if creativity is needed.
- Separate these via different model calls or explicit temperature in the same call.

### 4) Scratchpad & memory

- Keep an internal scratchpad for working memory (facts discovered during tool calls, intermediate code snippets).
- Persist important facts to a session memory or vector DB so future queries reuse them (avoids re-searching).

### 5) Verification layers

Before executing high-impact actions (e.g., deploy, delete, financial transactions), require:

- Model to produce a short human-readable summary,
- Cross-check via secondary model or verification script,
- Manual human approval for destructive actions.

### 6) Cost & latency optimizations

- Use short, structured deliberation messages (one action per response).
- Use streaming for long outputs to reduce perceived latency.
- Cache deterministic or repeated tool call responses.

## Example implementation (Python pseudocode using CometAPI)

This pseudocode demonstrates server-side orchestration. It assumes CometAPI supports OpenAI-compatible chat completions.

```
import requests, os, json

API_KEY = os.getenv("COMETAPI_KEY")
ENDPOINT = "https://api.cometapi.com/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def call_model(messages, model="minimax-m2", max_tokens=512, temperature=0.2):
    payload = {"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": temperature}
    r = requests.post(ENDPOINT, headers=HEADERS, json=payload)
    return r.json()

# Initial conversation: system + user request

messages = [
    {"role":"system", "content": "You are an agentic assistant... "},
    {"role":"user", "content": "Help me update the CI job to use M2's new agent API."}
]

# Loop: ask model for thought/action, execute action, provide observation, repeat

for step in range(8):  # max 8 steps to avoid runaway loops

    resp = call_model(messages)
    assistant_text = resp
    # parse assistant_text for ACTION (e.g., CALL_TOOL)

    action = parse_action(assistant_text)
    if action == "FINAL_ANSWER":
        final = extract_final_answer(assistant_text)
        # present final to user

        print("FINAL:", final)
        break
    elif action == "CALL_TOOL":
        tool_name = action
        tool_args = action
        # Execute the tool safely (validate inputs first!)

        obs = safe_execute_tool(tool_name, tool_args)
        messages.append({"role":"system", "content": f"TOOL_RESULT: {json.dumps(obs)}"})
        # loop continues: model gets observation and responds
```

Key points:

- **`parse_action`** must be robust and strict; do not rely on free-form parsing.
- **`safe_execute_tool`** must validate tool args (whitelist allowed actions, parameter sanitization).
- Enforce a maximum step count and timeouts.

## Closing thoughts

MiniMax M2 represents a major new option in the open LLM ecosystem: an MoE-based model optimized for coding and agentic workflows, published with weights and tooling that let teams choose between hosted convenience or self-hosted control. For many teams the best approach is a two-phase journey: (1) validate rapidly on a hosted endpoint or the free demo , then (2) evaluate self-hosting only if you need the control, customization, or long-term cost profile that justifies the ops investment. The combination of a long context window, agent-native capabilities, and open weights makes M2 especially attractive for developer tools, multi-step agents, and production assistants — provided teams apply prudent optimization and safety engineering.

### How to Access MiniMax M2 API

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access [Minimax M2 API](https://www.cometapi.com/minimax-m2-api/) through CometAPI, [the latest model version](https://www.cometapi.com/pricing/) is always updated with the official website. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-access-and-use-minimax-m2-api/](https://www.cometapi.com/how-to-access-and-use-minimax-m2-api/).*
