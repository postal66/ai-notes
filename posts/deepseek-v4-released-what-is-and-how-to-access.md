<!-- social-ops-fingerprint:2bc511c144148c7f56d21b48b3f707e1770f83689bbb97d3fd017db480a18646 -->
---
title: Deepseek v4 released: What is and How to Access
---
# Deepseek v4 released: What is and How to Access

![Deepseek v4 released: What is and How to Access](https://resource.cometapi.com/Deepseek%20v4%20.png)

DeepSeek has officially previewed V4 as an open-sourced model family, and the headline is not just “another model update.” The company is positioning V4 as a long-context, agent-friendly system built for real workloads: document-heavy analysis, coding assistants, search agents, and multi-step automation. The release is live on web, app, and API, and that the V4 line introduces a cost-effective **1M-token context window** across its official services.

What makes this launch especially noteworthy is the combination of scale and efficiency. DeepSeek says V4-Pro has **1.6T total parameters with 49B active**, while V4-Flash has **284B total parameters with 13B active**. In the technical report, DeepSeek also claims the V4 architecture uses hybrid attention, MoE routing, and post-training designed to improve agentic behavior while cutting the compute burden of ultra-long context.

## What is DeepSeek V4?

DeepSeek-V4 is the company’s latest preview flagship family, and the release includes two public variants: **V4-Pro** and **V4-Flash**. DeepSeek describes V4-Pro as the stronger model for world knowledge, math, STEM, coding, and agentic coding, while V4-Flash is the more responsive, cost-efficient option that still keeps much of the reasoning quality and long-context ability. V4-Pro leads current open models in agentic coding and world knowledge, while V4-Flash is designed for speed and economical deployment.

V4 uses a **hybrid attention architecture** combining **Compressed Sparse Attention (CSA)** and **Heavily Compressed Attention (HCA)**, plus **Manifold-Constrained Hyper-Connections** and the **Muon optimizer**. The company also says the models were pretrained on more than **32T tokens** and that, at 1M context, V4-Pro needs only **27% of the single-token inference FLOPs** and **10% of the KV cache** compared with DeepSeek-V3.2. That efficiency story is the real headline behind the release.

## DeepSeek-V4-Pro vs DeepSeek-V4-Flash

### DeepSeek-V4-Pro

V4-Pro is the flagship model for users who care most about quality. DeepSeek-V4-Pro delivers stronger agentic coding performance, richer world knowledge, and world-class reasoning, and that it leads current open models while trailing only **Gemini-3.1-Pro** in world knowledge according to the launch page. In the technical report, V4-Pro is the larger model in the family, and the DeepSeek-V4-Pro is available through the same OpenAI-compatible and Anthropic-compatible interfaces as V4-Flash.

### DeepSeek-V4-Flash

V4-Flash is the efficiency-first model, its reasoning capabilities closely approach V4-Pro, and that it performs on par with V4-Pro on simple agent tasks, while using a smaller parameter footprint and faster response times, it as supporting both thinking and non-thinking modes, with the same 1M context length and the same core features as Pro, but at much lower cost.

### Which one should you choose?

Use **V4-Pro** when the task is high-stakes, knowledge-heavy, or difficult to verify: enterprise research, complex coding, multi-step decision support, or tasks where you want the strongest possible answer. Use **V4-Flash** when throughput, latency, or token cost matter more than squeezing out the last few points of benchmark performance. That choice is consistent with the official positioning and with the reported benchmark gaps between the two models.

| Item | DeepSeek-V4-Flash | DeepSeek-V4-Pro |
| --- | --- | --- |
| Total parameters | 284B | 1.6T |
| Active parameters | 13B | 49B |
| Context length | 1M | 1M |
| Reasoning modes | Non-think + think | Non-think + think |
| Best fit | Fast inference, high-throughput apps, cost-sensitive agents | Highest-capability reasoning, harder coding and knowledge tasks |
| Official API pricing | Cache hit $0.028 / cache miss $0.14 / output $0.28 per 1M tokens | Cache hit $0.145 / cache miss $1.74 / output $3.48 per 1M tokens |
| Max output | 384K | 384K |

[CometAPI](https://www.cometapi.com/) provides access to [Deepseek v4 Pro](https://www.cometapi.com/models/deepseek/deepseek-v4/) and [V4 Flash](https://www.cometapi.com/models/deepseek/deepseek-v4-flash/),—20% cheaper than official—plus seamless switching between 500+ models (GPT-5.4, Gemini 3.1, etc.) via a single OpenAI-compatible or Anthropic Messages endpoint.

## Performance benchmark

### DeepSeek-V3.2 vs V4-Flash vs V4-Pro

On the base-model comparison table, V4-Flash and V4-Pro both outperform DeepSeek-V3.2 across core benchmarks, with V4-Pro usually taking the lead. For example, the report lists the following scores: AGIEval **82.6 / 83.1** vs V3.2’s **80.1**; MMLU **88.7 / 90.1** vs **87.8**; MMLU-Pro **68.3 / 73.5** vs **65.5**; HumanEval **69.5 / 76.8** vs **62.8**; and LongBench-V2 **44.7 / 51.5** vs **40.2** for V3.2, where the middle number is V4-Flash and the last is V4-Pro.

| Benchmark | DeepSeek-V3.2-Base | DeepSeek-V4-Flash-Base | DeepSeek-V4-Pro-Base |
| --- | --- | --- | --- |
| AGIEval (EM) | 80.1 | 82.6 | 83.1 |
| MMLU (EM) | 87.8 | 88.7 | 90.1 |
| MMLU-Pro (EM) | 65.5 | 68.3 | 73.5 |
| HumanEval (Pass@1) | 62.8 | 69.5 | 76.8 |
| LongBench-V2 (EM) | 40.2 | 44.7 | 51.5 |

Source: DeepSeek-V4 technical report, Table 1.

The pattern is straightforward: **Flash narrows the gap to Pro**, but **Pro is still the stronger general model**. That makes V4-Flash the practical default for many production systems, while V4-Pro is the model to reach for when answer quality is more important than cost or latency.

### Western model comparisons: where V4 fits

In one human evaluation on Chinese white-collar tasks, the report says **DeepSeek-V4-Pro-Max** outperformed **Claude Opus 4.6-Max**, with a **63% non-loss rate**. DeepSeek-V4-Pro “significantly outperforms” **Claude Sonnet 4.5** and approaches **Claude Opus 4.5** on an R&D coding benchmark.

| Evaluation area | DeepSeek result | Western model comparison | What it suggests |
| --- | --- | --- | --- |
| Chinese white-collar tasks | V4-Pro-Max, 63% non-loss rate | vs Claude Opus 4.6-Max | Strong showing in practical business-style tasks |
| R&D coding benchmark | V4-Pro-Max pass rate 67 | vs Claude Sonnet 4.5 at 47; Opus 4.5 at 70; Opus 4.6 Thinking at 80 | Competitive with leading frontier models, especially against Sonnet-tier systems |

It's not "number one in every aspect," but it's already at a level that "must be seriously evaluated."

DeepSeek's technical report compares V4-Pro-Max with Claude Opus 4.6 Max, GPT-5.4 xHigh, and Gemini 3.1 Pro High in the same table. The results aren't simplistic: Western closed-source models still perform strongly in some knowledge and inference aspects; however, V4-Pro-Max has a very strong presence in code, long contexts, and some agent tasks. In other words, it's no longer a low-dimensional narrative of "domestic alternatives," but has entered the stage of "which is more suitable for your scenario."

In terms of knowledge and reasoning ability, it's on par with Opus 4.6 Max, GPT-5.4 xHigh, and Gemini 3.1 ProHigh. However, it lags slightly behind in agentic capabilities, though the difference isn't significant.

![Deepseek v4 released: What is and How to Access](https://pica.zhimg.com/80/v2-1ae601a64543b101a0bd5fc8b0c4f21e_1440w.webp?source=1def8aca)

DeepSeek-V4-Pro-Max is highly competitive in code-oriented and long-context scenarios, while the Western models still look extremely strong in several pure reasoning and knowledge benchmarks. That is the right way to read the release: **DeepSeek V4 is firmly in the frontier conversation, but benchmark leadership remains task-dependent**.

## How to access DeepSeek V4

### 1) Use the official web and app

DeepSeek says V4 Preview is available right now on **web, app, and API**. For normal users, the simplest path is still the official chat interface, where the model can be accessed through **Expert Mode** or **Instant Mode**.

### 2) Use the API

I highly recommend CometAPI to access deepseek V4, because it offers the best price and aggregation advantages.

The model names are:

- `deepseek-v4-flash`
- `deepseek-v4-pro`

> DeepSeek also says the legacy names `deepseek-chat` and `deepseek-reasoner` will be deprecated and currently map to non-thinking and thinking modes of V4-Flash until **2026-07-24**. That is important for migration planning if you already have older integrations in production.

- Sign up at [CometAPI](https://www.cometapi.com/) and get your API key.
- Use the standard OpenAI Python SDK (or any compatible client) with a custom base URL:

Here is a clean example using the official OpenAI-compatible format:

```
import os
from openai import OpenAIclient = OpenAI(
    api_key=os.environ["cometapi_API_KEY"],
    base_url="https://api.cometapi.com"
)response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize the benefits of million-token context."}
    ],
    extra_body={"thinking": {"type": "enabled"}},
    reasoning_effort="high"
)print(response.choices[0].message.content)
```

That request pattern follows quick-start guidance: set the base URL, choose `deepseek-v4-pro` or `deepseek-v4-flash`, and enable thinking when you need deeper reasoning.

### How to use DeepSeek V4 effectively

For long-document workflows, the strongest pattern is to keep the context clean and structured. V4’s 1M-token window is a major advantage, but the model still performs best when the input is organized into sections, source excerpts, task instructions, and explicit output constraints. That is the most natural way to exploit the long-context capability DeepSeek is advertising.

For code and agent workflows, start with **V4-Flash** for fast iteration, then escalate to **V4-Pro** for the final run or the most difficult steps. That approach fits the official positioning: Flash is the efficient option, Pro is the stronger model, and both share the same API surface and context length.

## Final word

DeepSeek-V4 is notable because it combines four things the market has been asking for at the same time: **long context, strong reasoning, open availability, and aggressive pricing**. The real story is not just that DeepSeek released another model. It is that the company is trying to make frontier-style AI economically usable in production. For teams evaluating where to place their next AI bet, that is a signal worth testing, not ignoring.

For teams building across multiple providers, this is exactly the kind of release worth benchmarking inside your own stack. CometAPI can be the practical layer to compare DeepSeek-V4 alongside other frontier models without forcing your product team to rebuild the integration each time the market shifts.

---

*Originally published at [https://www.cometapi.com/deepseek-v4-released-what-is-and-how-to-access/](https://www.cometapi.com/deepseek-v4-released-what-is-and-how-to-access/).*
