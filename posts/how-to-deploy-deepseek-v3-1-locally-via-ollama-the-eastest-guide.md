<!-- social-ops-fingerprint:c0c323416ca4a7ad517e3bf619ce682f220a85c2265b06ac4c9e9c2c285ef9da -->
---
title: How to deploy deepseek-v3.1 locally via ollama: The Eastest Guide
---
# How to deploy deepseek-v3.1 locally via ollama: The Eastest Guide

![How to deploy deepseek-v3.1 locally via ollama: The Eastest Guide](https://resource.cometapi.com/blog/uploads/2025/09/How-to-deploy-deepseek-v3.1-locally-via-ollama.webp)

DeepSeek-V3.1 is a hybrid “thinking / non-thinking” MoE language model (671B total, ≈37B activated per token) that can be run locally if you use the right provider/quantization and tooling. Below I explain what DeepSeek-V3.1 is, the hardware/software requirements, step-by-step local run tutorials (Ollama + llama.cpp examples), and how to **deploy and use Thinking Mode** (the `<think>`/`</think>` chat template) with code examples you can copy/paste.

---

## What is DeepSeek-V3.1?

DeepSeek-V3.1 is the v3.1 release of DeepSeek’s MoE (Mixture-of-Experts) family. It was designed as a hybrid inference model that supports two conversational templates/modes — **Thinking** and **Non-Thinking** — from the same checkpoint by changing the chat template. The model architecture traces to the DeepSeek-V3 MoE design (671B total parameters; ≈37B parameters activated per token for inference) and adds post-training improvements for tool use, agent skills, and long-context handling.

### Quick feature highlights

- Hybrid **Thinking / Non-Thinking** modes (toggled by chat template tokenization).
- MoE architecture: large total parameter count but limited activated params per token (enables efficiency).
- Post-training boosts for tool calls and agent workflows (tool-call format and agent templates documented in the model assets).

---

## What do I need to run DeepSeek-V3.1 locally?

Running the **full** DeepSeek-V3.1 (raw checkpoints) is heavyweight — training/checkpoint storage and inference orchestration are nontrivial. But there are practical paths:

### Hardware

- **Full distributed inference (research / cluster)**: multiple high-memory GPUs (A100/H800 class) or a GPU cluster with model-parallel serving (typical for 600B+ checkpoints). Use only if you’re running production research clusters.
- **Practical local options**: use the *activated-param* perspective (≈37B activated) or a quantized GGUF/1-bit dynamic build. Community quantizations (1-bit dynamic / GGUF) reduce disk+RAM requirements significantly — e.g., community posts report compressing a 720GB checkpoint down to ~170GB GGUF for a quantized variant. That makes local single-server GPU inference feasible for well-resourced desktops/servers.

**Bottom line:** expect a large-model workflow (tens to low-hundreds of GB disk for quantized artifacts); for GPU VRAM, use quantized variants and target ≥24–48GB VRAM for reasonable throughput; otherwise use CPU+swap with performance tradeoffs.

### Software & tooling

Python 3.10+ (for transformer/tokenizer tooling and custom scripts).

`transformers` (for tokenizer & helper functions) — the model card shows examples using `transformers.AutoTokenizer`.

One or more local inference runtimes:

- **Ollama** (easy: `ollama pull` / `ollama run` integration; some DeepSeek builds on Ollama require pre-release versions, check the model/ollama note). Ollama has become a standard local runner for community models.
- **llama.cpp / ggml** stacks or `llama-server` for GGUF quantized files — great for direct GGUF execution.
- **text-generation-inference / Triton / FlashAttention stacks** for higher-performance GPU inference (advanced setups).

Disk: large free space for model files (tens → hundreds of GB depending on quantization).

### Model artifacts (which file to get)

- Official safetensors / BF16 / FP8 / GGUF variants: Hugging Face hosts V3.1 model artifacts and multiple quantizations. If you need a GGUF/quantized file for `llama.cpp`, look for a community quantization release (or a conversion script from safetensors → GGUF) — the model card lists quantized variants.

---

## How do I prepare the model for local inference?

Below are the recommended preparation steps arranged from simple → advanced.

### Step 1 — Pick a runtime (recommendation)

- **Beginner / fast test:** Ollama — minimal setup: download, run model, call API. Note: some DeepSeek-V3.1 builds note Ollama v0.11.7 as required for specific features.
- **Advanced / low-level control:** `llama.cpp` + GGUF quant (if a GGUF quantization is available). This gives you direct inference control and integration with `llama-server`.

### Step 2 — Download the model

If you use Ollama:

```
# install ollama (see https://ollama.com/docs)

# Pull the model (this downloads the model to your machine)
ollama pull deepseek-ai/DeepSeek-V3.1
# or a specific tag: ollama pull deepseek-ai/DeepSeek-V3.1:quant-q4_0
```

(Ollama’s `run` will pull automatically if not present; `pull` lets you control timing.)

If you use Hugging Face + llama.cpp:

```
# Example: download via huggingface-cli or hf_transfer

pip install huggingface_hub
hf_hub_download(repo_id="deepseek-ai/DeepSeek-V3.1", filename="DeepSeek-V3.1.gguf")
# or use a community quant file (gguf) referenced on the Hugging Face model page
```

Hugging Face lists model artifacts, templates, and quantizations on the model card.

### Step 3 — Convert / quantize (optional)

If you only find safetensors or BF16 artifacts but need GGUF for `llama.cpp`, use the conversion scripts in `llama.cpp` (or community tools) to convert → quantize. There are community tools for 1-bit dynamic quantization that preserve accuracy while shrinking size; see the community posts that report down to ~170GB.

---

## How do I actually run DeepSeek-V3.1 locally? (Practical run tutorials)

I’ll show **Ollama** (easy, recommended) and **llama.cpp** (GGUF) examples plus a short Python example using the model-card tokenizer helpers.

### A — Running with Ollama (quick start)

1. Install Ollama (follow official instructions).
2. Pull and run the model:

```
# pull model to disk (optional; run will pull automatically)

ollama pull deepseek-ai/DeepSeek-V3.1

# start an interactive session (runs model and exposes local API)

ollama run deepseek-ai/DeepSeek-V3.1
```

3. Make an HTTP request to the local Ollama server:

```
# curl usage example (local Ollama server usually listens on port 11434)

curl -sS -X POST 'http://localhost:11434/api/generate' \
  -H 'Content-Type: application/json' \
  -d '{
    "model":"deepseek-ai/DeepSeek-V3.1",
    "prompt":"Explain the difference between thinking and non-thinking mode in DeepSeek.",
    "max_tokens":256
  }'
```

Ollama’s CLI and API patterns are designed to be simple: `ollama run` will pull if needed and launch a model server. See Ollama docs and model pages for memory hints and exact model names/tags.

### B — Running a quantized GGUF via llama.cpp

1. Build `llama.cpp` with CUDA (optional) or CPU:

```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
# for CUDA:

make clean && make LLAMA_CUBLAS=1
# or CPU only:

make
```

2. Place the model GGUF file in a path and run:

```
./main -m /path/to/DeepSeek-V3.1.q4_K_M.gguf \
  -p "Explain how to enable thinking mode." \
  --temp 0.2 --n_predict 512
```

3. For server use, `llama-server` (community project) can expose an HTTP endpoint:

```
llama-server -m /path/to/DeepSeek-V3.1.q4_K_M.gguf
# then POST to the server like:

curl -X POST "http://localhost:8080/api/v1/generate" -d '{"prompt":"Hello","max_tokens":200}'
```

Use community GGUF quantizations (q4/q8/1-bit dynamic) to fit into GPU/CPU budgets; the `llama.cpp` repo provides conversion tools and guidance.

### C — Python example using the tokenizer + chat template

Hugging Face model card provides a `tokenizer.apply_chat_template` helper and shows how to encode a conversation with `thinking=True`. Here’s a minimal Python example adapted from the model card:

```
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3.1")

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Who are you?"},
    {"role": "assistant", "content": "<think>Hmm</think>I am DeepSeek"},
    {"role": "user", "content": "1+1=?"}
]

# apply thinking chat template

s = tokenizer.apply_chat_template(messages, tokenize=False, thinking=True, add_generation_prompt=True)
print(s)  # the template includes the special <think> token placement
```

You can then feed the tokenized prompt into your inference runtime (Ollama/llama.cpp/TGI) depending on your stack.

---

## How does Thinking Mode work and how do I deploy it locally?

DeepSeek-V3.1 uses **chat templates** that contain a special thinking token (e.g., `<think>` and `</think>`). The *template* determines whether the model is in Thinking or Non-Thinking mode:

- **Non-Thinking** template places `</think>` in the assistant prefix, which instructs the model to produce direct responses (toolcall format is supported in non-thinking).
- **Thinking** template places `<think>` in the assistant prefix which makes the model output internal chain-of-thought style intermediate signals (the model is trained to use that token sequence to reason internally and produce higher-quality multi-step answers). The Hugging Face model card documents these exact tokens and the `tokenizer.apply_chat_template(..., thinking=True)` API.

### Programmatic toggle (examples)

**A — With the tokenizer (Python):**

```
# thinking=True or thinking=False changes how the prompt is formatted

prompt_thinking = tokenizer.apply_chat_template(messages, thinking=True, add_generation_prompt=True)
prompt_non_thinking = tokenizer.apply_chat_template(messages, thinking=False, add_generation_prompt=True)
```

Feed `prompt_thinking` to your inference runtime to get the Thinking behavior.

**B — With raw prompt (llama.cpp / manual):**

Insert `<think>` before the assistant turn when you prompt:

```
<｜begin_of_sentence｜>You are a helpful assistant<｜User｜>How to optimize this code?<｜Assistant｜><think>
```

(That exact token framing is in the model card — you must respect spacing and special markers if you use the raw template.)

**C — With Ollama (UI toggle):**
The official DeepSeek web demo and release notes mention a “DeepThink” toggle/button for switching modes in the hosted UI. Locally, Ollama or your app should replicate that behavior by switching the chat template (i.e., changing the prompt you send to the runtime between the two tokenized forms). If you run DeepSeek via Ollama, you can implement this in your application by maintaining two prompt templates (thinking vs non-thinking) and toggling which you pass through the Ollama API.

---

## How do I deploy Thinking Mode as an agent (tool calls, code agents)?

DeepSeek-V3.1 documents *toolcall* and *agent* templates in the model assets. The model expects tools to be presented in a specific JSON/instruction format and supports chaining multiple tool calls in a single turn if you follow the exact wrapper tokens described in the model card.

### Example: simple tool-call wrapper (pseudo)

The model specifies a tool descriptor block and a strict `tool_calls_begin` / `tool_call_begin` format. A minimal example (conceptual):

```
## Tools

You have access to the following tools:

### web_search

Description: Query the web
Parameters: {"q": "string"}

<｜begin_of_sentence｜>{system prompt}

## Tools

...tool descriptions...

<｜User｜>Find the population of Tokyo<｜Assistant｜></think>
<｜tool_calls_begin｜><｜tool_call_begin｜>web_search<｜tool_sep｜>{"q":"population of Tokyo 2025"}<｜tool_call_end｜><｜tool_calls_end｜>
```

The tool output should then be fed back to the model in the next turn following the model’s prescribed format (see `assets/search_tool_trajectory.html` on the model page for the exact flow). Implementing agents requires programmatic orchestration: call tool → capture result → inject result back into chat context exactly as the template prescribes → call model again.

---

## Practical tips, troubleshooting, and safety notes (What should I watch for?)

- **Token templates are strict.** Use the model’s `tokenizer.apply_chat_template` or reproduce the exact `<think>`/`</think>` tokens as shown. Incorrect spacing or missing markers will change model behavior.
- **Tool format must be valid JSON.** The model will parse tool arguments as JSON — invalid JSON will break tool calls.
- **Quantization tradeoffs.** 1-bit dynamic / aggressive quantizations shrink storage and RAM but may slightly alter numeric fidelity. Test on your workloads. Community quantizations that drop 80% of disk usage exist (example report: 720GB → ~170GB), but always validate with your prompts.
- **Ollama compatibility.** Some DeepSeek variants note Ollama v0.11.7 as required for pre-release features — check the Ollama model page and update accordingly.

---

## Example end-to-end: run DeepSeek-V3.1 locally with Thinking Mode (mini walkthrough)

1. Install Ollama and pull the model:

```
# install ollama per docs, then:

ollama pull deepseek-ai/DeepSeek-V3.1
ollama run deepseek-ai/DeepSeek-V3.1 &
```

2. Use the Python tokenizer to compose a thinking prompt:

```
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3.1")

msgs = [
  {"role":"system","content":"You are a helpful assistant."},
  {"role":"user","content":"Plan a multi-step strategy to prototype a mobile app in 2 weeks."}
]
prompt = tokenizer.apply_chat_template(msgs, thinking=True, add_generation_prompt=True)

import requests
resp = requests.post("http://localhost:11434/api/generate", json={
    "model": "deepseek-ai/DeepSeek-V3.1",
    "prompt": prompt,
    "max_tokens": 400
})
print(resp.json())
```

3. If the model returns a tool call in the toolcall format, parse the JSON and run the tool, then inject results into the next message as per the model card templates.

## How should you choose your deployment path?

- **If you want the fastest path to experiment:** use **Ollama** and the Hugging Face model card’s examples. Ollama hides many infra details and gives a local HTTP API.
- **If you need lower cost / more portability:** use a community **GGUF quantized** artifact and run with `llama.cpp` or `llama-server`. Quantization saves disk and memory but test accuracy for your workload.
- **If you are building agents or tools:** follow the model card’s **toolcall** and **agent** templates exactly; orchestrate tool outputs back into model context.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access [DeepSeek V3.1](https://www.cometapi.com/deepseek-v3-1/) through CometAPI, the latest models version listed are as of the article’s publication date. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.deerapi.com/%E8%B0%83%E7%94%A8-gemini-2-5-flash-image-%E6%8C%87%E5%8D%97-7305430m0) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

---

## Conclusion

DeepSeek-V3.1 brings a practical hybrid inference philosophy (one checkpoint + templated thinking behavior) that makes experimenting with chain-of-thought-style reasoning and agent tool use straightforward when you respect the chat templates and tooling requirements. Use the Hugging Face model card and the DeepSeek release notes as your first stop, pick a local runtime (Ollama for simplicity, `llama.cpp` for control), and test quantized builds for practical local deployments.

---

*Originally published at [https://www.cometapi.com/how-to-deploy-deepseek-v3-1-locally-via-ollama/](https://www.cometapi.com/how-to-deploy-deepseek-v3-1-locally-via-ollama/).*
