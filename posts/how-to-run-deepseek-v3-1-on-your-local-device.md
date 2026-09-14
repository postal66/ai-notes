<!-- social-ops-fingerprint:a0ce069fcd4223bef8013263da15d7a5832915b3512c4593f9e180c46a8a6cfc -->
---
title: How to Run DeepSeek-V3.1 on your local device
---
# How to Run DeepSeek-V3.1 on your local device

![How to Run DeepSeek-V3.1 on your local device](https://resource.cometapi.com/blog/uploads/2025/08/DeepSeek-V3.1-website.webp)

DeepSeek-V3.1 is a hybrid Mixture-of-Experts (MoE) chat model released by DeepSeek in August 2025 that supports *two inference modes* — a fast “non-thinking” mode and a deliberate “thinking” mode — from the same checkpoint. The model is available on Hugging Face and can be run locally via several paths (vLLM, Ollama/llama.cpp, Ollama-style GGUFs, or large-scale multi-GPU setups). Below I walk you through requirements, how the thinking mode works, several local run options (with runnable code snippets), and a step-by-step “Thinking Mode deploy” recipe with examples for tool calling and token templates.

## What is DeepSeek-V3.1 and why does it matter?

DeepSeek-V3.1 is the v3 family update from DeepSeek that introduces a *hybrid inference design*: the same model can be run in **thinking** (deliberative, multi-step) or **non-thinking** (direct answer, faster) modes by changing the chat template. Architecturally it’s a large MoE family (base checkpoint around 671B total parameters, ~37B activated per token) with long-context training extended to 128K tokens and FP8 micro-scaling support. DeepSeek positioned V3.1 as an agent-ready release: better tool calling, improved agent skills, and higher thinking efficiency compared to prior R1 releases. The release was announced in August 2025 and has been integrated into Hugging Face, CFD/OSS tooling, and cloud deployment guides.

### How the hybrid model works (concise)

- **One checkpoint, two templates:** Thinking vs Non-Thinking modes are controlled by the *chat template* and a `<think>`/`</think>` token convention in the prompt. The model card documents the exact prefixes.
- **Agent/tool improvements:** Post-training boosts enable smarter tool calls — the model expects a strict tool-call JSON format for safe, deterministic tool execution.
- **Performance tradeoffs:** Thinking mode spends tokens on internal chain-of-thought style reasoning and can be slower/more token-intensive; non-thinking is faster and cheaper. Benchmarks in the model card show substantial improvements across reasoning and code benchmarks for V3.1.

### How the model is structured

- **MoE backbone**: large total parameter count with a smaller activated subset per token (economical inference).
- **Long-context training**: V3.1 extends long-context phases significantly (32k → larger training on long documents) to support 128K+ windows in some builds.
- **FP8 native workflow**: DeepSeek uses FP8 formats extensively (w8a8 / UE8M0) for weight/activation efficiency; community conversion scripts exist if you prefer BF16/FP16.

## What are the requirements to run DeepSeek-V3.1 locally? (Hardware, storage, and software)

Running the **full** V3.1 model (unquantized) is a large undertaking. Below are realistic categories of setups and what they typically require.

### Practical Buckets

- **Cluster / research-lab (full model)**: multiple high-memory GPUs (H100/H800 class or many Ada/Hopper GPUs), multi-node with tens of GPUs, lots of NVMe storage (hundreds of GBs), and specialized inference frameworks (SGLang, vLLM, LMDeploy, TRT-LLM).
- **Single-server high-end (quantized)**: possible with heavy quantization (INT4/AWQ/AWQ2/gguf) and frameworks like Ollama (prepackaged) or community GGUFs — still requires ~tens to hundreds of GB GPU RAM or clever CPU+GPU offload.
- **Developer laptop / dev box**: not feasible for full model; use small distilled / fine-tuned variants or connect to local server/Ollama instance.

### Hardware checklist (practical)

- **GPUs**: For real inference throughput of the full V3.1: multi-GPU clusters (H100 / H800 / Ada Lovelace+). For FP8 execution, GPUs with compute capability and driver support needed.
- **RAM & storage**: Expect hundreds of GB free disk for the model files (model pages list a few hundreds GB depending on format/quantization), plus working space for converted formats. Ollama metadata lists a ~400GB footprint for a DeepSeek V3.1 Ollama package in the library.
- **Network**: For multi-node inference you need low-latency interconnects (NVLink / InfiniBand) and orchestration tooling for tensor-parallel setups.

### Software checklist

- **OS**: Linux is recommended for community inference tools (DeepSeek-Infer demo lists Linux/Python).
- **Python**: 3.10+ (in many DeepSeek examples). Typical package versions are pinned in repo `requirements.txt`.
- **Frameworks & tools** (pick one or more): SGLang, vLLM, LMDeploy, TRT-LLM/TensorRT-LLM, LightLLM, or Ollama for simpler local installs. Each has instructions and different precision/quantization support.

**Practical note:** If you have only one consumer GPU (e.g., 24–48 GB), you’ll likely use quantized GGUFs or remote inference; if you have a workstation with >128 GB of RAM plus an H100/H200 class GPU cluster, you can target higher fidelity FP8/FP16 inference with vLLM.

---

## How do I run DeepSeek-V3.1 locally?

Below are several practical paths you can use, from the most manual / flexible to the easiest path for a single developer box.I will provide step-by-step tutorials and code examples

---

### Option A — Official DeepSeek-Infer demo (development / cluster path)

This is the repo’s example/demo for FP8/BF16 inference. Use it if you plan multi-node or want to experiment with the official inference code.

1. **Clone, prepare environment**

```
git clone https://github.com/deepseek-ai/DeepSeek-V3.git
cd DeepSeek-V3/inference
# Create a dedicated venv / conda env

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

(Repo `inference/requirements.txt` lists pinned torch/triton/transformers versions recommended by the team.)

2. **Download model weights**

- Download from the Hugging Face model page (`deepseek-ai/DeepSeek-V3.1`) and place them under `/path/to/DeepSeek-V3`. The model card and repo note both the official Hugging Face storage links.

3. **Convert weights for demo**

```
# example conversion command shown in the repo

python convert.py --hf-ckpt-path /path/to/DeepSeek-V3 --save-path /path/to/DeepSeek-V3-Demo --n-experts 256 --model-parallel 16
```

4. **Run interactive generation (distributed)**

```
torchrun --nnodes 2 --nproc-per-node 8 --node-rank $RANK --master-addr $ADDR \
  generate.py --ckpt-path /path/to/DeepSeek-V3-Demo --config configs/config_671B.json \
  --interactive --temperature 0.7 --max-new-tokens 200
```

This is the canonical example from the DeepSeek repo for cluster-style runs.

---

### Option B — vLLM (recommended for server deployments & OpenAI-compatible API)

vLLM supports DeepSeek in FP8/BF16 modes and gives you an OpenAI-compatible server. It’s a popular production path for large models because of memory optimizations and API compatibility.

**Start a vLLM server that will fetch the model from Hugging Face** (example pattern):

```
# this will download/serve the model (replace with exact model id if needed)

vllm serve deepseek-ai/DeepSeek-V3.1 --host 0.0.0.0 --port 8000
```

Then request completions with curl or an OpenAI-compatible client:

```
curl -s -X POST "http://localhost:8000/v1/completions" \
  -H "Content-Type: application/json" \
  -d '{"model":"DeepSeek-V3.1","prompt":"Explain the QuickSort algorithm", "max_tokens":200}'
```

vLLM recipes and docs include DeepSeek examples and notes about FP8 compatibility and multi-GPU/pipeline parallelism. For heavy models you will still need multiple GPUs or a quantized variant.

---

### Option C — LMDeploy / SGLang / LightLLM & TensorRT-LLM (high performance)

The DeepSeek repo explicitly recommends **SGLang**, **LMDeploy**, and **TensorRT-LLM** as optimized engines for DeepSeek V3. They provide improved inference latency, throughput, and FP8 kernels.

A typical LMDeploy invocation (refer to LMDeploy docs for exact CLI):

```
# pseudo-example; refer to LMDeploy docs for exact options

lmdeploy serve --model /path/to/deepseek_v3.1 --precision fp8 --port 8080
```

SGLang benchmarks and launch recipes are available in the repo and in the SGLang project’s `benchmark/deepseek_v3` folder. Use these stacks when you control a GPU cluster and want production throughput.

---

### Option D — Ollama (the easiest local dev route, often single-machine)

If you want the lowest friction way to run DeepSeek locally (and you can spare the disk), **Ollama** provides packaged models and a simple CLI (`ollama pull`, `ollama run`). DeepSeek-V3.1 appears in the Ollama library and can be run locally (Ollama may require a recent/pre-release version for some features).

**Example (Ollama CLI):**

```
# Pull the model (downloads the model artifacts to your disk)

ollama pull deepseek-v3.1

# Start an interactive session:

ollama run deepseek-v3.1

# Or run as a local API server (Ollama supports a local API)

# Example: POSTing to Ollama's local API (adjust host/port to your setup)
curl -X POST http://localhost:11434/api/generate \
  -H 'Content-Type: application/json' \
  -d '{"model":"deepseek-v3.1","prompt":"Summarize the following paper: ..."}'
```

Ollama abstracts away many distribution/quantization details and can be a great way to test model behavior on a single host. Note: the model page lists a ~404GB packaged size for the Ollama entry, so plan disk & RAM accordingly.

---

## What is Thinking Mode and how to use it

DeepSeek-V3.1 implements a **hybrid thinking token** approach: the same checkpoint can run in *thinking* mode (internal “chain of thought” tokens) or *non-thinking* mode by switching the chat/prompt template. The model uses explicit tokens like `<think>` (and closing `</think>` in some templates) to signal internal chain-of-thought vs direct answer generation. The model card documents non-thinking and thinking prefixes and shows how templates differ.

### Example: constructing a message in Python (tokenizer helper)

The Hugging Face model card includes a handy snippet showing how to apply the chat template via the tokenizer. This is the recommended pattern for generating *thinking* or *non-thinking* formatted prompts:

```
import transformers
tokenizer = transformers.AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3.1")

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Who are you?"},
    {"role": "assistant", "content": "<think>Hmm</think>I am DeepSeek"},
    {"role": "user", "content": "1+1=?"}
]

# Thinking mode

tokenizer.apply_chat_template(messages, tokenize=False, thinking=True, add_generation_prompt=True)

# Non-thinking mode

tokenizer.apply_chat_template(messages, tokenize=False, thinking=False, add_generation_prompt=True)
```

Switch `thinking=True` to produce a prompt that uses the `<think>` prefix; `thinking=False` produces the non-thinking template. The model will behave differently (internal deliberation vs immediate response) depending on this flag.

---

## Quick reference — small troubleshooting & best practices

**If you run out of GPU memory:** Try quantized builds (AWQ/q4/INT4) or community GGUFs; many community spaces publish quantizations for local use. Ollama / vLLM can also serve smaller quantized builds.

**If you need the model to call external tools:** Adopt the **ToolCall** schema in the chat template exactly. Test the tool JSON format offline and check that your orchestration code (the piece that executes the tool) returns sanitized, typed JSON back to the model.

**If you need long context:** Use vLLM or SGLang with long-context plugins; DeepSeek was explicitly trained/extended for 32K/128K contexts and related tooling supports that window. Expect memory tradeoffs.

## Can I actually run DeepSeek-V3.1 on a laptop or small server?

Short answer: **Yes, but with caveats.** Community quantizations (AWQ/GGUF/1-bit dynamic) reduce the storage and memory footprint drastically and have enabled hobbyists to run V3.1 variants on high-end desktops (claims of ~170 GB working set ). However:

- **Fidelity vs size tradeoff:** aggressive quantization reduces memory but may affect reasoning/code performance. Test on your workloads.
- **Legal & licensing:** the model is MIT licensed per the model card, but third-party quantizations may carry their own licenses; review them before production use.

---

## Final words

DeepSeek-V3.1 is a significant step toward hybrid “agent” models with explicit thinking/non-thinking behavior and improved tool use. If you want to run it locally, choose a path that matches your hardware and risk tolerance:

**For research:** `transformers` + quantized safetensors and accelerate.

**For production & throughput:** vLLM + multi-GPU (H100/H200).

**For local experiments:** Ollama/llama.cpp + community GGUFs (merge + run).

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access [DeepSeek-V3.1](https://www.cometapi.com/deepseek-v3-1/) through CometAPI, the latest models version listed are as of the article’s publication date. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.deerapi.com/%E8%B0%83%E7%94%A8-gemini-2-5-flash-image-%E6%8C%87%E5%8D%97-7305430m0) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

---

*Originally published at [https://www.cometapi.com/run-deepseek-v3-1-on-your-local-device/](https://www.cometapi.com/run-deepseek-v3-1-on-your-local-device/).*
