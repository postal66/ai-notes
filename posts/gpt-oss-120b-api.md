<!-- social-ops-fingerprint:195d7d708e59aec6a046cda71ae0a19bd6760ec38bc6583b064f4b175c3f2fe1 -->
---
title: GPT-OSS-120B API
---
# GPT-OSS-120B API

![GPT-OSS-120B API](https://resource.cometapi.com/blog/uploads/2025/10/How-much-computing-power-is-required-for-GPT-OSS-deployment-710x373.webp)

OpenAI’s **gpt-oss-120b** marks the organization’s first open-weight release since GPT-2, offering developers **transparent**, **customizable**, and **high-performance** AI capabilities under the **Apache 2.0 license**. Designed for sophisticated **reasoning** and **agentic** applications, this model democratizes access to advanced large-language technologies, enabling on-premises deployment and in-depth fine-tuning.

## Core Features and Design Philosophy

GPT‑OSS models are designed as general-purpose, text-only LLMs. They support high-level cognitive tasks, including mathematical reasoning, structured analysis, and language comprehension. Unlike closed commercial models such as GPT‑4, GPT‑OSS allows full download and use of model weights, giving researchers and developers unprecedented access to inspect, fine-tune, and deploy models entirely on their infrastructure.

### Basic Information

- **Parameters**: 117 billion total, 5.1 billion **active** via **Mixture-of-Experts (MoE)**
- **License**: Apache 2.0 for unrestricted commercial and academic use
- **Context Window**: Up to **128 K tokens**, supporting long-form inputs and multi-document reasoning
- **Chain-of-Thought**: Full **CoT** outputs for auditability and fine-grained control
- **Structured Outputs**: Native support for JSON, XML, and custom schemas .

## Technical Details

GPT-OSS leverages a **Transformer** backbone augmented with a **Mixture-of-Experts (MoE)** architecture to achieve sparse activation and reduce inference costs. The **gpt-oss-120b** model contains **128 experts** distributed across **36 layers**, activating **4 experts per token** (5.1 B active parameters), while **gpt-oss-20b** utilizes **32 experts** over **24 layers**, activating **4 experts per token** (3.6 B active parameters). It employ **alternating dense and locally banded sparse attention**, **grouped multi-query attention** (group size 8), and support a **128 k** token context window—unmatched in open-weight offerings to date. Memory efficiency is further enhanced via \*\*4-bit mixed-precision quantization \*\*, enabling larger contexts on commodity hardware.

GPT‑OSS models have undergone rigorous benchmarking against well-known datasets, revealing competitive—if not superior—performance when compared to similarly sized proprietary models.

## Benchmarking and Performance Evaluation

On standard benchmarks, **gpt-oss-120b** matches or exceeds OpenAI’s proprietary **o4-mini** model:

- **MMLU (Massive Multitask Language Understanding)**: ~88% accuracy
- **Codeforces Elo (coding reasoning)**: ~2205
- **AIME (math competition with tools)**: ~87.9%
- **HealthBench**: Significantly outperforms o4-mini in clinical QA and diagnosis tasks
- **Tau-Bench (Retail + Reasoning tasks)**: ~62% on average

## Model Version

- **Default Variant**: `gpt-oss-120b` (v1.0)
- **Active Parameters**: 5.1 B (dynamic MoE selection)
- **Follow-Up Releases**: Planned patches to improve **safety filters** and **specialized domain fine-tuning**

## Limitations

Despite their power, GPT‑OSS models come with certain limitations:

- **Text-only interface**: Unlike GPT-4o or Gemini, GPT‑OSS does not support multimodal inputs (images, audio, video).
- **No training set transparency**: OpenAI has not released details on specific datasets used, which may raise concerns for academic reproducibility or bias auditing.
- **Performance inconsistency**: Some community benchmarks (e.g., Simple-Bench) report poor results in specific reasoning tests (~22% on some tasks for 120b), suggesting **performance may vary significantly across domains**.
- **Hardware limitations**: The 120B model requires significant compute for local inference, making it inaccessible for casual developers without GPU access.
- **Safety tradeoffs**: Although tested under adversarial fine-tuning scenarios, the open-weight nature means these models can still be misused—e.g., for spam, misinformation, or model jailbreaks—if not properly governed.

Nevertheless, OpenAI reports that gpt‑oss models **do not raise current frontier-level safety risks**, especially in biorisk or cybersecurity domains.

## How to call ****gpt-oss-120b**** API from CometAPI

### **`gpt-oss-120b`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Input Tokens | $0.16 |
| Output Tokens | $0.80 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`gpt-oss-120b`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to  [API doc](https://apidoc.cometapi.com/):

- **Endpoint:** `https://api.cometapi.com/v1/chat/completions`
- **Model Parameter:** gpt-oss-120b
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY`
- **Content-Type:** `application/json` .
- **Core Parameters**: `prompt`, `max_tokens_to_sample`, `temperature`, `stop_sequences`

While GPT‑OSS can be used entirely offline, it also supports **OpenAI-compatible chat APIs** when hosted on services like Hugging Face or AWS Bedrock.

Here’s a sample integration using Python:

```
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://api.cometapi.com/v1/chat/completions",  # or AWS/Azure provider

    api_key=cometapi_key
)

response = client.chat.completions.create(
    model="gpt-oss-120b",
    messages=[
        {"role": "user", "content": "Explain how quantum tunneling works."}
    ]
)

print(response.choices.message.content)
```

Alternatively, you can run the models locally using tools like **LMDeploy**, **Text Generation Inference (TGI)**, or **vLLM**.

**See Also [GPT-OSS-20B](https://www.cometapi.com/gpt-oss-20b/)**

---

*Originally published at [https://www.cometapi.com/gpt-oss-120b/](https://www.cometapi.com/gpt-oss-120b/).*
