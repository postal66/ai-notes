<!-- social-ops-fingerprint:e86d99fd3f1291d5567da4c01da9b0a5db43281605aa0f4243304d688014a466 -->
---
title: What Is MiMo-V2.5? Specs, Benchmarks, Features, Pricing, and API Access
---
# What Is MiMo-V2.5? Specs, Benchmarks, Features, Pricing, and API Access

![What Is MiMo-V2.5? Specs, Benchmarks, Features, Pricing, and API Access](https://resource.cometapi.com/3012288c-7d5b-4f4e-86f3-23cf24d5d4a2.png)

## TL;DR

Xiaomi's standard V2.5 model combines native text, image, video, and audio understanding with a 1-million-token context window, tool use, and sparse Mixture-of-Experts efficiency. It is the better fit when multimodal input and cost per completed task matter. The Pro variant is larger and stronger on demanding coding and long-horizon agent work, but it is text-input focused and costs roughly three times as much per token at Xiaomi's published rates.

The practical decision is simple: choose the standard model for multimodal agents, document and media analysis, and high-volume automation; choose Pro when difficult software engineering or sustained autonomous execution is the bottleneck.

## Key Takeaways

- The standard model uses 310B total parameters while activating 15B per token.
- It accepts text, images, video, and audio, then returns text.
- Its API supports 1M context, up to 128K output, tool calls, web search, streaming, structured output, and context caching.
- Publisher-reported results include 65.8 on Terminal-Bench 2.0 and 56.1 on SWE-Bench Pro.
- Xiaomi’s current MiMo-V2.5-Pro model card lists 1.02T total and 42B active parameters. The publisher-listed SWE-Bench Pro scores are 56.1 for MiMo-V2.5 and 57.2 for Pro; these are dated, publisher-reported comparisons, not a guarantee for a specific coding workflow.
- At current Xiaomi rates, standard input/output costs $0.14/$0.28 per million tokens; Pro costs $0.435/$0.87.
- Both APIs in CometAPI are priced 20% below the official uncached price pairs.
  **Information checked:** September 28, 2026. Prices, benchmarks, limits, availability, and request formats can change. Xiaomi has announced that its official mimo-v2.5 and mimo-v2.5-pro API model names will be deprecated at 10:00 Beijing time on October 21, 2026, without automatic replacement. Plan migration and confirm the live route before deployment.

API lifecycle note: the official Xiaomi platform plans to retire both V2.5 model IDs on October 21, 2026. This notice concerns Xiaomi’s API platform; check any third-party gateway separately. [Xiaomi model deprecation notice](https://mimo.mi.com/docs/en-US/updates/deprecate)

## What the Standard Model Is

[**MiMo-V2.5**](https://www.cometapi.com/models/XiaomiMiMo/mimo-v2-5/) is Xiaomi MiMo's efficiency-oriented foundation model for multimodal perception and agentic work. It provides [native text, image, video, and audio input](https://mimo.mi.com/models/en-US/mimo-v2.5) within one architecture and produces text output.

Xiaomi’s model release log dates the MiMo-V2.5 series public beta to April 23, 2026. The weights were subsequently released under the MIT license. MiMo-V2.5 has 310B parameters in total, but activates only about 15B for each token; it uses a large pool of specialists without running all of them at once.

[**MiMo-V2.5-Pro**](https://www.cometapi.com/models/XiaomiMiMo/mimo-v2-5-pro/) targets a different workload. It is a trillion-parameter, text-input model designed for the hardest coding, terminal, and long-running agent tasks. The two variants share a 1M maximum context but differ sharply in modality, active compute, and price.

## MiMo-V2.5 Specifications and Features

| Official architecture details | Value | Why it matters |
| --- | --- | --- |
| Architecture | Sparse MoE | Large expert capacity with selective activation |
| Total / active parameters | 310B / 15B | Active compute is far below total capacity |
| Transformer layers | 48: 1 dense + 47 MoE | Most layers use routed experts |
| Routed experts | 256; 8 active per token | Specialization without dense 310B execution |
| Attention | 39 SWA + 9 global layers | Balances local efficiency and long-range flow |
| SWA window | 128 tokens | Reduces long-context cache pressure |
| Context / maximum output | 1M / 128K tokens | Supports long documents and extended traces |
| Input / output | Text, image, video, audio / text | Native perception across four input types |
| Vision encoder | 729M ViT; 28 layers | Image and video understanding |
| Audio encoder | 261M transformer; 24 layers | Native audio understanding |
| Multi-Token Prediction | 3 modules; about 329M parameters | Supports speculative decoding efficiency |
| Training scale | About 48T tokens | Broad text and multimodal training pipeline |
| API capabilities | Tools, web, streaming, structured output, caching | Production-oriented agent primitives |
| License | MIT | Commercial use and modification permitted |

The operating envelope includes 1M context and 128K output, plus published limits of 100 requests per minute and 10 million tokens per minute. Provider-level limits may differ by account and integration route.

![What Is MiMo-V2.5? Specs, Benchmarks, Features, Pricing, and API Access](https://resource.cometapi.com/1280000.PNG)

*Xiaomi MiMo's official architecture diagram.* [*Official architecture asset*](https://huggingface.co/XiaomiMiMo/MiMo-V2.5/resolve/main/assets/architecture.svg)*.*

## How MiMo-V2.5 Architecture Works

### Sparse Experts: Total Capacity Is Not Active Compute

The central efficiency fact is the 310B-total, 15B-active design. The router selects eight of 256 experts for each token. That gives the model access to a much larger parameter pool than a conventional 15B dense model without executing all 310B parameters every time.

This does not make self-hosting trivial. The complete weights still have to be stored and distributed, so memory capacity, interconnect bandwidth, expert routing, and serving software remain material constraints.

### Hybrid Attention for Long Context

The backbone interleaves sliding-window and global attention at a [5:1 SWA-to-global ratio](https://mimo.mi.com/docs/en-US/news/latest/v2.5-open-sourced). Thirty-nine local layers control cache growth, while nine global layers preserve long-distance information flow. Xiaomi reports nearly a sixfold KV-cache reduction versus an all-global design.

A 1M-token maximum is capacity, not guaranteed accuracy. Retrieval quality, latency, tool-state growth, and attention over distant evidence still require workload-specific evaluation.

### Native Encoders and Agent Features

A 729M-parameter vision transformer handles image and video inputs; a 261M-parameter audio transformer handles audio. The projectors map both streams into the language backbone, letting one agent combine a screenshot, a video segment, an audio track, text instructions, and tool results.

Three Multi-Token Prediction modules support speculative decoding and reinforcement-learning efficiency. The model was trained on about 48T tokens, with context progressively extended to 1M during post-training.

The open weights use an [MIT license](https://mimo.mi.com/docs/en-US/news/latest/v2.5-open-sourced). Commercial deployment is permitted, but infrastructure cost and third-party dependencies still need separate review.

## MiMo-V2.5 Benchmarks: Coding, Agents, and Multimodal Results

> **Benchmark note:**
>
> the figures below are publisher-reported. They are directional evidence, not a guarantee for a specific repository, media format, tool stack, latency target, or safety policy.

### Coding and Agent Results

![What Is MiMo-V2.5? Specs, Benchmarks, Features, Pricing, and API Access](https://resource.cometapi.com/986f8c0e-f.png)

*Official Xiaomi MiMo coding and agent benchmark chart.*

| Official coding benchmark | Reported score | Decision signal |
| --- | --- | --- |
| MiMo Coding Bench | 71.8 | Broad coding-agent capability |
| Claw-Eval Text | 62.3 | General text-agent completion |
| Terminal-Bench 2.0 | 65.8 | Interactive terminal execution |
| SWE-Bench Pro | 56.1 | Real-world software engineering |
| Claw-Eval Multi-Turn | 63.2 | Longer multi-step agent work |
| ResearchClawBench | 16.91 | Autonomous research workflows |

**Result:** the strongest case is practical tool use rather than isolated code completion. A 65.8 Terminal-Bench result supports terminal-oriented agents, while 56.1 on SWE-Bench Pro suggests useful repository-level ability. The much lower research score is a reminder to test evidence gathering and citation behavior separately.

### Multimodal Results

![What Is MiMo-V2.5? Specs, Benchmarks, Features, Pricing, and API Access](https://resource.cometapi.com/1c616c0c-655b-4870-af7c-9159d106a095.png)

*Official Xiaomi MiMo image, video, and multimodal-agent benchmark chart.*

| Official multimodal benchmark | Reported score | Capability tested |
| --- | --- | --- |
| CharXiv RQ | 81.0 | Chart and document reasoning |
| MMMU-Pro | 77.9 | Expert-level multimodal reasoning |
| HR-Bench 4K | 88.5 | High-resolution image understanding |
| OmniDocBench | 87.2 | Document understanding |
| Claw-Eval Multimodal | 23.8 | Multimodal agent completion |
| Video-MME | 87.7 | Video understanding |
| DailyOmni | 83.5 | Everyday audiovisual reasoning |
| VideoHolmes | 64.0 | Temporal video reasoning |

**Result:** document, high-resolution image, and video understanding are the clearest strengths. The 23.8 multimodal-agent score is much lower than the perception scores, so a system that must both understand media and reliably operate tools should be evaluated end to end.

## MiMo-V2.5 vs MiMo-V2.5-Pro: Multi-Dimensional Comparison

| Official architecture comparison | MiMo-V2.5 | MiMo-V2.5-Pro  Official Pro specifications  Official Pro benchmarks | Practical implication |
| --- | --- | --- | --- |
| Total parameters | 310B | 1.02T | Pro has over 3× the total capacity |
| Activated parameters | 15B | 42B | Pro uses about 2.8× more active parameters |
| Layers / routed experts | 48 / 256 | 70 / 384 | Pro is a larger serving target |
| Model-card context ceiling | 1M | 1M | Both list up to 1M tokens; test retrieval and latency at your workload size |
| Official API maximum output | 128K | 128K | Both current Xiaomi API model pages list 128K; provider-specific limits may differ |
| Native input | Text, image, video, audio | Text | MiMo-V2.5 is the documented multimodal choice; verify the exact Pro endpoint before sending media |
| SWE-Bench Pro | 56.1 | 57.2 | Pro leads by 1.1 points |
| Terminal-Bench 2.0 | 65.8 | 68.4 | Pro leads by 2.6 points |
| Primary fit | Efficient multimodal agents | Complex coding and long-horizon agents | Choose by tested workload; the model-level margins do not prove a general quality lead |

**Comparison result:** Pro's benchmark advantage is modest on the two shared coding-agent tests, while the standard variant adds native image, video, and audio input and uses far fewer active parameters. Pro is justified when small gains in hard task completion are more valuable than multimodal input and lower unit cost.

## How Much Do MiMo-V2.5 and MiMo-V2.5-Pro Cost?

| Price basis: May 27, 2026 | Official standard API | Official Pro API | MiMo-V2.5 API in CometAPI | MiMo-V2.5-Pro API in CometAPI |
| --- | --- | --- | --- | --- |
| Input, cache miss / MTok | $0.14 | $0.435 | $0.112 | $0.348 |
| Output / MTok | $0.28 | $0.87 | $0.224 | $0.696 |
| Input, cache hit / MTok | $0.0028 | $0.0036 | Check live billing | Check live billing |
| Discount vs official uncached rate | Baseline | Baseline | 20% | 20% |

At official rates, Pro costs about 3.1× as much as standard for both uncached input and output. The provider prices shown above reduce each uncached pair by 20%, but the relative gap between the variants remains essentially unchanged.

Price per token is not total cost. Tool retries, context size, output length, latency, failed task recovery, and human review determine cost per completed task. Run a representative workload sample before selecting a default production model.

## What Is MiMo-V2.5 Best For?

- **Multimodal agents:** combine screenshots, documents, video, audio, instructions, and tools in one workflow.
- **Long-document analysis:** process repositories, contracts, research archives, logs, and support histories.
- **Media understanding:** summarize videos, extract events, interpret charts, and answer audiovisual questions.
- **Coding and terminal agents:** inspect files, run commands, modify code, and iterate on test results.
- **High-volume automation:** use sparse activation and lower token pricing for repeated production tasks.

## Limitations and Risks

- Only 15B parameters are active per token, but self-hosting still requires the full 310B-weight system.
- Multimodal output is text; image, speech, and video generation require other models.
- A 1M context ceiling does not guarantee uniform retrieval accuracy across the full window.
- Publisher benchmarks may not transfer to custom tools, repositories, prompts, or safety constraints.
- Provider modality exposure can differ from the underlying open-weight model's full capability.

> **Production gate:**
>
> validate accuracy, tool-call completion, latency, token consumption, modality handling, and fallback behavior on representative tasks before committing traffic.

## API Example

The following Python example uses an OpenAI-compatible CometAPI endpoint and the standard model ID. Confirm the current endpoint and supported request schema before deployment.

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
    max_retries=0,
)

response = client.chat.completions.create(
    model="mimo-v2.5",
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "Summarize the main findings in this technical report.",
        }
    ],
)

print(response.choices[0].message.content)
```

## Decision Guide

| Workload signal | Start with | Switch when |
| --- | --- | --- |
| Images, video, or audio are first-class inputs | Standard | Do not switch unless multimodal preprocessing is acceptable |
| Large document or mixed-media volume | Standard | Pro only if reasoning failures dominate cost |
| Difficult repository engineering | Test both | Choose Pro if its completion gain offsets 3.1× unit cost |
| Long autonomous terminal trajectories | Pro | Return to standard if gains are not measurable |
| High-volume routine automation | Standard | Escalate only failed or high-value tasks |

> **Recommended routing:**
>
> use standard as the default for multimodal and high-volume work, then route only difficult text-first coding or long-horizon tasks to Pro. This preserves capability while controlling total cost.

## Conclusion

The standard model is not merely a smaller Pro. It is a distinct optimization point: native multimodal input, 1M context, strong tool-oriented benchmarks, and 15B active parameters at a much lower token price.

Pro is the specialist option for difficult software engineering and sustained autonomous execution. Its extra capacity produces measurable but not universal gains, so the strongest deployment pattern is workload-based routing rather than selecting one variant for every request.

## FAQ

### Is the standard model open source?

Its weights are released under the MIT license, allowing commercial use, modification, fine-tuning, and redistribution subject to the license terms.

### How many parameters does it use?

The sparse MoE contains 310B total parameters and activates 15B for each token. Active parameters describe per-token computation, not the storage size of the complete model.

### Does it support images, video, and audio?

Yes. The standard variant accepts text, images, video, and audio and returns text. The Pro variant's official specification lists text input.

### What is the maximum context window?

Both model cards specify a context window of up to 1M tokens. Xiaomi’s current API pages list a 128K maximum output for MiMo-V2.5 and MiMo-V2.5-Pro. Actual usable limits can vary by endpoint, provider, account, and request format; verify the deployed route before relying on those ceilings.

The current official Pro API page separately confirms the 1M context and 128K maximum output: [MiMo-V2.5-Pro API specifications](https://mimo.mi.com/models/en-US/mimo-v2.5-pro)

### Which variant is better for coding agents?

Pro reports higher results on shared coding and terminal benchmarks, but the margin is modest. Test both on the target repository and choose based on task completion, latency, and total cost.

### Which variant is better for multimodal agents?

The standard variant is the natural choice because it natively accepts image, video, and audio input. Pro is text-input focused.

### How should a production team choose?

Start with standard, measure failures, and route only the difficult text-first tasks that benefit from Pro. Compare cost per completed task rather than price per token alone.

---

*Originally published at [https://www.cometapi.com/what-is-mimo-v2-5/](https://www.cometapi.com/what-is-mimo-v2-5/).*
