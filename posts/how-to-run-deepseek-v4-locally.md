<!-- social-ops-fingerprint:3f974de6718f324b866a6354e4b529e6abd24f377919d3465529a2598f985b73 -->
---
title: How to Run DeepSeek V4 Locally
---
# How to Run DeepSeek V4 Locally

![How to Run DeepSeek V4 Locally](https://resource.cometapi.com/How%20to%20Run%20DeepSeek%20V4%20Locally.webp)

## TR

The practical way to run DeepSeek V4 locally is to use the official open-source weights with a high-performance serving stack such as vLLM, then expose the model through a local OpenAI-compatible endpoint. DeepSeek’s current public materials describe two models in the V4 family: **DeepSeek-V4-Pro** at **1.6T total parameters / 49B active**, and **DeepSeek-V4-Flash** at **284B total parameters / 13B active**, both with **1M-token context** and three reasoning modes. vLLM’s current local deployment examples target **8× B200/B300** for Pro and **4× B200/B300** for Flash. If you do not have that kind of hardware, a hosted fallback like **CometAPI** is the more practical path.

DeepSeek AI dropped a bombshell on April 24, 2026, with the preview release of **DeepSeek-V4**, featuring two powerful Mixture-of-Experts (MoE) models: **DeepSeek-V4-Pro** (1.6T total parameters, 49B active) and **DeepSeek-V4-Flash** (284B total, 13B active). Both support a native **1 million token context window**—a game-changer for long-document analysis, agentic workflows, coding over massive codebases, and retrieval-augmented generation (RAG) at scale.

Trained on over 32 trillion tokens with architectural innovations like hybrid Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA), manifold-constrained hyper-connections (mHC), and efficient memory handling, V4 achieves up to 73% reduction in inference FLOPs and 90% lower KV cache footprint for 1M contexts compared to V3.2. Performance rivals top closed-source models while remaining open-weights (MIT license) and extremely cost-effective via API.

Running these models **locally** offers unmatched privacy, zero recurring API costs (beyond hardware), offline capability, and full customization. However, their scale presents challenges: V4-Pro's full weights exceed 800GB downloads, and inference demands significant hardware or aggressive quantization.

## Can DeepSeek V4 really run locally?

Yes, but “locally” here means something very different from running a 7B model on a laptop. DeepSeek’s own materials and the vLLM support post point to large multi-GPU systems: **V4-Pro** is a **1.6T-parameter** model with **49B active parameters**, while **V4-Flash** is **284B total / 13B active**. The official deployment examples from vLLM are written for **8× B200/B300** on Pro and **4× B200/B300** on Flash. That is the clearest practical signal that DeepSeek V4 is an enterprise-class local deployment, not a casual desktop experiment.

There is a reason for that scale. DeepSeek says V4 supports a **1M-token context window**, and the technical report claims the V4-Pro uses only **27% of the single-token inference FLOPs** and **10% of the KV cache** compared with DeepSeek-V3.2 at 1M context. vLLM further explains that, with **bf16 KV cache**, DeepSeek V4 uses **9.62 GiB of KV cache per sequence at 1M context**, which is about **8.7× smaller** than the estimated **83.9 GiB** for a comparable DeepSeek-V3.2-style stack. In other words, V4 is dramatically more efficient than earlier generations, but one million tokens is still an enormous systems problem.

### Architecture Comparison Table: DeepSeek V4 vs V3 and Competitors

| Model | Total Params | Active Params | Context Length | KV Cache Efficiency (1M) | Approx. Download | Inference Focus |
| --- | --- | --- | --- | --- | --- | --- |
| DeepSeek-V3.2 | 671B | ~37B | 128K | Baseline | ~数百 GB | Balanced |
| DeepSeek-V4-Flash | 284B | 13B | 1M | ~7-10% of V3 | ~160GB | Speed & Efficiency |
| DeepSeek-V4-Pro | 1.6T | 49B | 1M | ~10% of V3 | ~865GB | Max Capability |
| Llama 4 70B (dense) | 70B | 70B | 128K-1M+ | Higher | Smaller | Consumer-friendly |
| GPT-5.5 (est. closed) | ~2T? | N/A | High | Proprietary | N/A | Cloud-only |

V4's MoE design activates only a fraction of parameters per token, keeping compute closer to a 13B-49B dense model while benefiting from the knowledge of a much larger network.

## Which Deepseek V4 model should you use?

For most local deployments, DeepSeek-V4-Flash is the better starting point. V4-Flash delivers reasoning that closely approaches Pro on simpler agent tasks while remaining faster and more economical.

Use DeepSeek-V4-Pro when you care more about absolute capability than efficiency. Pro as the stronger model for harder reasoning, coding, and agentic tasks. The benchmark tables show why: on the official comparison, V4-Pro-Base reaches 90.1 MMLU, 76.8 HumanEval, and 51.5 LongBench-V2, while V4-Flash-Base scores 88.7, 69.5, and 44.7 respectively. Both are strong; Pro just pushes higher when you need the best possible result.

| Metric | DeepSeek-V3.2-Base | DeepSeek-V4-Flash-Base | DeepSeek-V4-Pro-Base |
| --- | --- | --- | --- |
| Total parameters | 671B | 284B | 1.6T |
| Activated parameters | 37B | 13B | 49B |
| AGIEval (EM) | 80.1 | 82.6 | 83.1 |
| MMLU-Pro (EM) | 65.5 | 68.3 | 73.5 |
| HumanEval (Pass@1) | 62.8 | 69.5 | 76.8 |
| LongBench-V2 (EM) | 40.2 | 44.7 | 51.5 |

A simple reading of the table is enough for product planning. Flash is not a stripped-down toy model; it is a serious long-context assistant with lower cost. Pro is the model to test first when the problem is hard, stateful, or close to a production knowledge workflow.

## Recommended local stack

### 1) vLLM for production-style serving

The strongest official option today is **vLLM**. The vLLM team says it now supports the **DeepSeek V4 family** and provides concrete single-node launch commands for both models. Their post frames V4 as a long-context model family designed for tasks up to one million tokens and describes the implementation work needed for hybrid KV cache, kernel fusion, and disaggregated serving.

For V4-Pro, vLLM’s example targets **8× B200 or 8× B300**. For V4-Flash, the example targets **4× B200 or 4× B300**. The commands also use `--kv-cache-dtype fp8`, `--block-size 256`, `--enable-expert-parallel`, and DeepSeek-specific parsing flags such as `--tokenizer-mode deepseek_v4`, `--tool-call-parser deepseek_v4`, and `--reasoning-parser deepseek_v4`. That combination is a very strong hint about how DeepSeek expects serious self-hosting to be done.

```
# DeepSeek-V4-Flash on a supported multi-GPU hostdocker run --gpus all \  --ipc=host -p 8000:8000 \  -v ~/.cache/huggingface:/root/.cache/huggingface \  vllm/vllm-openai:deepseekv4-cu130 deepseek-ai/DeepSeek-V4-Flash \  --trust-remote-code \  --kv-cache-dtype fp8 \  --block-size 256 \  --enable-expert-parallel \  --data-parallel-size 4 \  --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}' \  --attention_config.use_fp4_indexer_cache=True \  --tokenizer-mode deepseek_v4 \  --tool-call-parser deepseek_v4 \  --enable-auto-tool-choice \  --reasoning-parser deepseek_v4
```

To switch to **V4-Pro**, keep the same pattern and change the model to `deepseek-ai/DeepSeek-V4-Pro`, with the data-parallel size moved to the Pro example in vLLM’s post. That is the simplest way to start testing locally without reinventing the serving stack.

### 2) DeepSeek’s repository inference helpers

Deepseek V4 does **not** include a Jinja-format chat template. Instead, it provides a dedicated **`encoding`** folder with Python scripts and test cases for converting OpenAI-style messages into model input strings and parsing the output. The same page says to consult the **`inference`** folder for local deployment details, including weight conversion and interactive chat demos. That is useful if you want to build a custom front end or tightly control prompt formatting.

### 3) CometAPI as the practical backup plan

If you do not have B200/B300-class hardware, a hosted route is the sane choice. CometAPI says it offers **one API key for everything**, access to **500+ AI models**, and pricing that is **20–40% cheaper** than official vendor rates. It also publishes dedicated DeepSeek V4 pages, including **DeepSeek-V4-Pro** and **DeepSeek-V4-Flash**, with OpenAI-compatible integration examples.

## Step-by-Step: How to Run DeepSeek V4 Locally

### 1. Prerequisites

- **OS**: Linux preferred (Ubuntu 22.04/24.04) for best CUDA/ROCm support. Windows via WSL2 or native. macOS with Metal (limited for largest models).
- **Drivers**: NVIDIA CUDA 12.4+ (or latest). AMD ROCm for Radeon cards.
- **Python 3.11+**, Git, and sufficient disk space.
- **Hugging Face account** for gated models (if applicable): huggingface-cli login.

### 2. Easiest Way: Ollama or LM Studio (Beginner-Friendly)

Ollama provides the simplest CLI and WebUI experience. As of late April 2026, full V4 support may require custom Modelfiles or community tags, but V4-Flash quantized versions are emerging rapidly.

**Install Ollama** (Linux/macOS):

```
curl -fsSL https://ollama.com/install.sh | sh
ollama --version
```

**Run a compatible model** (start with smaller or check for V4 tags):

```
ollama pull deepseek-v4-flash:q4_0   # Example quantized tag; check ollama.com/library or community
ollama run deepseek-v4-flash:q4_0
```

For custom: Create a Modelfile(text):

```
FROM ./DeepSeek-V4-Flash-GGUF-Q4.gguf
TEMPLATE """{{ .Prompt }}"""
PARAMETER num_ctx 32768  # Start conservative; increase as hardware allows up to 1M with sufficient RAM/VRAM
```

Then ollama create my-v4-flash -f Modelfile.

**LM Studio**: GUI alternative. Download from lmstudio.ai, search/browse HF for DeepSeek-V4 GGUF quantizations (TheBloke-style or official), load, and chat. Excellent for experimentation with context sliders and GPU offloading.

**Open WebUI**: Layer on top of Ollama for a ChatGPT-like interface(Bash):

```
docker run -d -p 8080:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Access at <http://localhost:8080>.

### 3. Advanced: Hugging Face + vLLM or SGLang (High Performance)

For maximum speed and 1M context support, use vLLM (excellent MoE and PagedAttention support):

#### **Step 1:** Prepare the environment

Start by installing the current vLLM stack and making sure your CUDA, drivers, and GPU topology match the model you want to run. recommending temperature = 1.0 and top\_p = 1.0 for local deployment, and for Think Max it recommends a context window of at least 384K tokens. That is a useful starting point whether you are building a chat app, a coding assistant, or an agent workflow.

**Installation**:

```
Bash
pip install -U "vllm>=0.9.0"  # Check latest for V4 compatibility
```

**Download model** (use CLI for large files):

```
Bash
pip install -U "huggingface_hub[cli]"
huggingface-cli download deepseek-ai/DeepSeek-V4-Flash --local-dir ./DeepSeek-V4-Flash
```

**Serve with vLLM** (example for Flash on 2 GPUs):

#### **Step 2:** Launch the model server

Once the container is up, expose the model as an OpenAI-compatible local endpoint. That makes it easy to reuse your existing application code and swap backends without changing your app architecture.

**Serve with vLLM** (example for Flash on 2 GPUs):

```
Python
from vllm import LLM, SamplingParams

llm = LLM(
    model="deepseek-ai/DeepSeek-V4-Flash",
    tensor_parallel_size=2,      # Adjust to your GPU count
    max_model_len=1048576,       # 1M context (hardware permitting)
    dtype="auto",                # or "fp8" / "bfloat16"
    quantization="gptq" if using quantized weights else None,
    gpu_memory_utilization=0.9
)

sampling_params = SamplingParams(temperature=0.7, top_p=0.95, max_tokens=4096)

outputs = llm.generate(["Explain the architecture of DeepSeek V4 in detail."], sampling_params)
for output in outputs:
    print(output.outputs[0].text)
```

For server mode (OpenAI-compatible API):

```
Bash
vllm serve deepseek-ai/DeepSeek-V4-Flash \
  --tensor-parallel-size 2 \
  --max-model-len 1048576 \
  --port 8000
```

Then query via OpenAI client by setting base\_url="<http://localhost:8000/v1>".

**SGLang** alternative for potentially better long-context performance:

```
Bash
pip install "sglang[all]>=0.4.0"
python -m sglang.launch_server --model-path deepseek-ai/DeepSeek-V4-Flash --port 30000
```

### **Step 3:** Query the local endpoint from Python

```
from openai import OpenAI
# Adjust the base URL if your vLLM server is bound differently.

client = OpenAI(
base_url="http://localhost:8000/v1",
api_key="EMPTY",
)

response = client.chat.completions.create(
model="deepseek-ai/DeepSeek-V4-Flash",
messages=[
{"role": "system", "content": "You are a precise, technical assistant."},
{"role": "user", "content": "Explain the difference between V4-Pro and V4-Flash."},
],
temperature=1.0,
top_p=1.0,
)

print(response.choices[0].message.content)
```

## Performance Expectations and Optimization Tips

- **Tokens/sec**: On RTX 4090 with Q4 Flash: 15-40+ t/s at 8K-32K context (varies with implementation). Drops at 128K+ due to attention/KV but V4's efficiencies help. Multi-GPU scales well with tensor/pipeline parallelism.
- **Optimizations**:
- Use FlashAttention-3 or vLLM's PagedAttention.
- Speculative decoding for 1.5-2x speedup.
- Context pruning or compression techniques.
- Monitor with `nvidia-smi`; utilize `gpu_memory_utilization`.
- For CPU: llama.cpp with `--n-gpu-layers -1` (all offload if possible) or pure CPU with high RAM.

Benchmark your setup with tools like `llama-bench` or simple timing scripts. Real throughput depends on prompt length, generation length, and hardware.

### Challenges and Limitations of Local V4 Deployment

- **Resource Intensity**: Even Flash requires decent hardware for comfortable speeds at long contexts.
- **Quantization Trade-offs**: Lower bits can reduce reasoning quality, especially on complex tasks—validate with benchmarks like SWE-Bench, MMLU, or your domain-specific evals.
- **Software Maturity**: As a new preview (April 2026), full optimized support in all backends is rolling out. Check GitHub issues for vLLM, llama.cpp, and HF.
- **Download/Storage**: Terabyte-scale models need fast internet and storage.
- **Power & Heat**: High-end setups consume significant electricity.

For many users, **hybrid approaches** work best: Run smaller tasks locally, offload heavy 1M-context reasoning to cloud when needed.

## When Local Isn't Enough: Seamless Integration with CometAPI

For many teams, the smartest move is not to force a local deployment at all. While local deployment excels for privacy and control, scaling to production, handling peak loads, or accessing full unquantized performance without massive hardware investment often favors a reliable API.

[**CometAPI**](https://www.cometapi.com/) provides a unified, OpenAI-compatible gateway to DeepSeek models—including the latest [Deeppseek V4](https://www.cometapi.com/models/deepseek/deepseek-v4/) series—along with dozens of other top LLMs (Claude, GPT, Llama, Qwen, Grok, etc.).

### Where the API beats local deployment

The current Deepseek V4 models are available through OpenAI-style and Anthropic-style endpoints, with base URLs that stay stable while the model name changes. The docs also say the model names `deepseek-chat` and `deepseek-reasoner` will eventually be deprecated and map to V4-Flash behavior during the transition.

That matters because local deployment carries operational cost. If the workload is not sensitive to data residency or if your team wants faster time-to-value, the API route is usually the rational choice. V4-Flash at $0.14 per 1M input tokens on cache miss, $0.0028 per 1M input tokens on cache hit, and $0.28 per 1M output tokens. The same page says V4-Pro is currently discounted 75% through May 31, 2026, at $0.435 per 1M input tokens on cache miss and $0.87 per 1M output tokens.

### Deepseek's best alternative: Where CometAPI fits

CometAPI is useful when the goal is not just to call DeepSeek V4 once, but to build a stack that can switch models quickly. CometAPI says it provides one API key for 500+ models, an OpenAI-compatible API, usage analytics, and lower pricing than official vendor rates. It also positions itself as a way to avoid vendor lock-in and manage spend across multiple providers.

That makes CometAPI a strong recommendation for teams that are evaluating V4-Pro against V4-Flash, or comparing DeepSeek against other frontier models in the same application. Instead of wiring a new integration every time the model changes, the application can keep a stable OpenAI-style client and switch only the `model` value and base URL. [CometAPI’s V4 guide](https://www.cometapi.com/how-to-use-deepseek-v4-api/) shows exactly that pattern.

**Quick Start with CometAPI for DeepSeek V4**:

- Use OpenAI SDK:
- Register/login at [CometAPI.com](https://www.cometapi.com/).
- Generate an API key in the console.

Here is the hosted version of the same integration pattern:

```
from openai import OpenAIclient = OpenAI(    base_url="https://api.cometapi.com",    api_key="YOUR_COMETAPI_KEY",)response = client.chat.completions.create(    model="deepseek-v4-pro",    messages=[        {"role": "system", "content": "You are a senior coding assistant."},        {"role": "user", "content": "Review this architecture for bottlenecks."}    ],    stream=False,    extra_body={        "thinking": {"type": "enabled"},        "reasoning_effort": "high"    })print(response.choices[0].message.content)
```

The value of this route is operational, not rhetorical. It removes infrastructure work, keeps the client code portable, and gives the team one place to test cost, latency, and quality across several models. CometAPI also says it tracks spend, latency, and call volume, which is useful once the prototype becomes a production workload.

### When to choose local, API, or CometAPI

| Deployment path | Best for | Why it makes sense | Trade-off |
| --- | --- | --- | --- |
| Local multi-GPU | Private workloads, research, offline experiments | Full control, open weights, official inference workflow, MIT license | Heavy GPU requirements and more operational work |
| Official DeepSeek API | Fastest direct access | Stable base URLs, OpenAI/Anthropic compatibility, no self-hosting burden | Provider dependency and token-based cost |
| CometAPI | Multi-model product teams | One key, OpenAI-compatible routing, cheaper pricing claims, usage analytics | One more abstraction layer in the stack |

The local path is justified when control matters more than convenience. The API path is justified when speed and simplicity matter more than ownership. CometAPI is the middle layer when the team wants portability and cost control without rebuilding the integration every time the model changes.

## FAQ

### Can DeepSeek V4 run on a laptop?

Not in the practical sense implied by local inference tutorials. The official materials point to multi-GPU and multi-node deployment, and the model sizes are far beyond ordinary consumer memory budgets. A laptop is fine for API access, but not for meaningful self-hosting of V4-Pro or even a comfortable V4-Flash setup.

### Which is better: V4-Pro or V4-Flash?

V4-Pro is the stronger model for reasoning, coding, and research. V4-Flash is the better default for speed, throughput, and lower cost. The official release and the benchmark table point to the same conclusion.

### Is CometAPI required in local deployement?

No. It is an optional production layer. DeepSeek’s own API works directly, and local self-hosting is possible through the official inference path. CometAPI becomes attractive when you want one code path across many model providers, cost tracking, and an easier switch between model families.

## Conclusion

DeepSeek V4 is not just another model release. It is a long-context, agent-focused system with open weights, official API access, and a clear split between a high-end reasoning model and a lower-cost throughput model. The latest official news matters because it changes the decision tree: local deployment is possible, but only for teams with serious GPU infrastructure; API access is available immediately; and CometAPI is a sensible recommendation when portability and cost discipline matter more than owning the inference stack.

If the workload is complex and the hardware exists, start with V4-Pro. If the workload is volume-driven, start with V4-Flash. If the goal is to ship quickly and keep model options open, use the API layer and keep your code portable. That is the most defensible production strategy right now.

**Actionable Next Steps**:

1. Assess your hardware and start with quantized V4-Flash via Ollama or LM Studio.
2. Experiment with code examples above and benchmark against your workloads.
3. Explore GGUF quants and community optimizations as they mature post-release.
4. For production or heavy lifting, integrate **CometAPI** for reliable, cost-effective access to full V4-Pro/Flash without managing hardware.

---

*Originally published at [https://www.cometapi.com/how-to-run-deepseek-v4-locally/](https://www.cometapi.com/how-to-run-deepseek-v4-locally/).*
