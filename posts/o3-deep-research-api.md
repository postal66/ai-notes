<!-- social-ops-fingerprint:e6f4b3efb5d1f1b76c5c02ae96058f9d884a19955ca0df7c63af472816ef2364 -->
---
title: O3-Deep-Research API
---
# O3-Deep-Research API

![O3-Deep-Research API](https://resource.cometapi.com/blog/uploads/2025/11/Where-Is-Deep-Research-in-ChatGPT-A-professional-overview-710x373.webp)

The **O3-Deep-Research** model is OpenAI’s flagship agent designed for **autonomous, multi-step research workflows**. Launched as part of the Deep Research API, it leverages advanced reasoning capabilities to **plan**, **search**, **analyze**, and **synthesize** information across diverse web sources, delivering **expert-level reports** within minutes .

## Basic Information

The **O3-Deep-Research** model, unveiled by OpenAI on **June 26, 2025**, represents a significant leap in automated knowledge work, enabling **agentic workflows** that autonomously decompose complex tasks, gather web-based data, and synthesize citation-rich outputs . As a flagship offering in the Deep Research API suite—alongside its sibling **O4-Mini-Deep-Research**—it is designed for professionals in **finance**, **science**, **policy**, and **engineering**, who demand thorough, accurate, and up-to-date research capabilities .

- **Model Name**: o3-deep-research-2025-06-26
- **Developer**: OpenAI
- **Release Date**: June 26, 2025
- **Integration**: Fully compatible with ChatGPT Agent framework, supports **function calls**, **webhooks**, and **browser tools** for **visual and PDF parsing** .

## Key Features

- **Agentic Task Decomposition**: O3-Deep-Research breaks down high-level queries into discrete subtasks, enabling step-by-step data gathering and reasoning.
- **Web Grounding**: Integrates securely with Bing Search to access **authoritative**, **recent** sources, minimizing hallucinations and ensuring **data validity** .
- **Citation-Rich Outputs**: Automatically embeds citations in final reports, enhancing **transparency** and **traceability**.
- **Adaptive Reasoning**: Incorporates a **private chain of thought** framework, allowing dynamic backtracking and hypothesis revision when faced with new information .

## Technical Details

The model builds upon the core **O3** architecture by integrating specialized modules for deep research tasks:

1. **Reinforcement Learning with Private Chain of Thought**: O3-Deep-Research employs **RLHF** (Reinforcement Learning from Human Feedback) to internalize multi-step planning, simulating a researcher’s thought process before emitting responses, thereby improving **logical coherence** and **contextual depth**.
2. **Tool Invocation Layer**: A dedicated component orchestrates calls to **web search**, **code execution**, and **data extraction** APIs. This layer ensures that each subtask is addressed using the optimal tool, fostering **modularity** and **scalability** .
3. **Safety & Compliance Sandbox**: All external web interactions pass through a **sandboxed environment** that filters out low-credibility domains, applies content safety checks, and logs audit trails for compliance with organizational policies.

### Tooling:

- **Web Search** & **Fetch** for real-time data retrieval
- **Function Calling** for custom workflows
- **Webhooks** to integrate external data sources
- **Token Handling**: Optimized to manage **long-form inputs** and **expanded outputs** (up to 16 K tokens), though very large contexts may incur increased **token consumption** .

## Benchmark Performance

- **Humanity’s Last Exam (HLE)**: Achieved **26.6%** accuracy, surpassing DeepSeek’s R1 (9.4%) and GPT-4o (3.3%) .
- **GPQA Diamond**: Expert-level science benchmark; O3 models have demonstrated **87.7%** on advanced questions (o3 full model) .
- **Software Engineering (SWE-bench Verified)**: Scored **71.7%**, a significant uplift over non-reasoning counterparts .
- **Codeforces**: Reached an **Elo of 2727**, outpacing earlier O1 models (1891).

## Model Versions

`o3-deep-research-2025-06-26`: Debut version with enhanced **webhooks** and **search integration** .

**Updates:**

- **Visual browser** integration (July 17, 2025)
- **Rate-limit adjustments** for **openAI Official Price** :/Pro (+125 full-model +125 lightweight queries per 30 days) and Free/Plus tiers

## Limitations

Despite its advances, **O3-Deep-Research** has notable constraints:

- **Latency**: The multi-step reasoning and external tool calls introduce higher response times compared to standard LLMs, potentially impacting **interactive applications**.
- **Compute Cost**: Reliance on **agentic decomposition** and **chain-of-thought** mechanisms increases GPU utilization and operational expenses, requiring careful **budget management**.
- **Hallucinations**: While reduced, hallucination rates can still spike in **highly ambiguous** domains or when encountering **paywalled** or **low-quality sources**, necessitating human oversight.
- **Scope Boundaries**: The model may struggle with **non-public** or **proprietary** data without specialized connectors, limiting its applicability in closed-access environments.

## How to call **O3-Deep-Research** API from CometAPI

### **`O3-Deep-Research`** API Pricing in CometAPI，20% off the official price:

|  |  |
| --- | --- |
| Input Tokens | $8.00 |
| Output Tokens | $32.00 |

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.
- Get the url of this site: `https://api.cometapi.com/`

### Use Method

1. Select the “`o3-deep-research`”/ “`o3-deep-research-2025-06-26`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

CometAPI provides a fully compatible REST API—for seamless migration. Key details to Response [API doc](https://apidoc.cometapi.com/):

- **Base URL:** `https://api.cometapi.com/v1/responses`
- **Model Names:** “`o3-deep-research`”/ “`o3-deep-research-2025-06-26`“
- **Authentication:** `Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

### API Integration & Examples

Developers can integrate O3-deep-research via the **Responses API**. A minimal example:

```
curl
--location 'https://api.cometapi.com/v1/responses' \
--header 'Authorization: Bearer sk-xxxxx' \
--header 'Content-Type: application/json' \
--data '{
"model": "o3-deep-research-2025-06-26",
"stream": true, "reasoning": { "summary": "detailed" },
"tools": ,
"input": "who are you"
}'
```

**See also**

- [o3-Pro](https://www.cometapi.com/o3-pro-api/)
- [O3](https://www.cometapi.com/o3-api/)

---

*Originally published at [https://www.cometapi.com/o3-deep-research-api/](https://www.cometapi.com/o3-deep-research-api/).*
