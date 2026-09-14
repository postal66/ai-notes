<!-- social-ops-fingerprint:f327b5d602d218d9247ea7292094dcba602c142b2174d283732d48086132eac2 -->
---
title: Claude Sonnet 4.5 API
---
# Claude Sonnet 4.5 API

![Claude Sonnet 4.5 API](https://resource.cometapi.com/blog/uploads/2025/09/67081be1ea2752e2a554e49a6aab2731b265d11b-2600x2288-1-1024x901.webp)

Anthropic’s **Claude Sonnet 4.5** is a 2025 update focused on long-duration autonomous work, stronger tool/computer use, tighter safety/alignment, and richer developer features (context editing, memory, in-chat code execution and file creation). Benchmarks and vendor tests emphasize large gains on coding and “agentic” tasks (e.g., Anthropic reports ~30 hours of continuous autonomous coding in internal tests and big jumps on OS/tool-use benchmarks).

## Key features

- **Agentic capability:** designed to run multi-step agents and coordinate multi-agent workflows.
- **Coding & software use:** Anthropic markets Claude Sonnet 4.5  as its **best coding model**, capable of end-to-end software work (design → implement → test → deploy).
- **Hybrid reasoning / Thinking mode:** supports on-demand extended reasoning (“thinking”) to trade latency for higher accuracy on complex tasks.
- **Large context & output:** advertised **200K context window** and up to **64K output tokens** for very large inputs/outputs.

## Technical details (what the release changes)

**Architecture & focus:** Claude Sonnet 4.5  is a Sonnet-series mid-to-frontier model tuned for **multi-step tool use**, extended task horizons, and improved deterministic behavior when interacting with external systems. Anthropic emphasizes improvements in **computer use** (automation of workflows across files, spreadsheets, and developer tools) and **reasoning/math** capabilities versus previous Sonnet releases.

**Long-horizon operation:** The release specifically highlights the model’s ability to run as a **continuous agent for extended periods** (reported examples up to **~30 hours** of autonomous operation in internal and early-customer tests), a large step up from previous multi-hour limits. This is important for use cases that require continuous monitoring, orchestration, or multi-step software projects.

**Tooling & context:** Claude Sonnet 4.5 ships with improved **context-management** and agent tooling (context editing, memory tools, multi-agent support), enabling developers to manage and persist agent state more robustly.

## Performance benchmarks

- **SWE-bench Verified:** **77.2%** (200K thinking budget, scaffold + tools); **78.2%** in 1M context; **82.0%** reported for a “high-compute” candidate selection regime.
- **OSWorld (computer tasks):** **61.4%** for Sonnet 4.5 vs **42.2%** for Sonnet 4 (four months earlier).
- **Autonomy length (internal tests):** >30 hours continuous autonomous coding/agent operation (previous generation ~7 hours).
- **Operating-system/tool benchmark:** Anthropic reports a jump to ~60% versus ~40% for the predecessor on an OS interaction benchmark — showing improved reliability when the model controls software.

![Claude Sonnet 4.5 API](https://resource.cometapi.com/blog/uploads/2025/09/67081be1ea2752e2a554e49a6aab2731b265d11b-2600x2288-1-1024x901.webp)
![Claude Sonnet 4.5 ](https://resource.cometapi.com/blog/uploads/2025/09/Screenshot-2025-09-29-at-10.08.34AM-1024x578.webp)

## Primary use cases

- **Software engineering & code generation:** Large-scale code synthesis, multi-file project generation, autonomous coding agents.
- **Agentic automation & orchestration:** Building long-lived agents that monitor systems, run repeated tasks, and coordinate tools (calendar, email, VMs, spreadsheets).
- **Data analysis & finance/cybersecurity workflows:** Deep analysis over documents, litigation briefs, financial models, and cybersecurity triage where multi-step reasoning and reliable tool use matter.

## How to call Claude Sonnet 4.5 API from CometAPI

### Model version:

|  |  |
| --- | --- |
| API call point | cursor suitable point |
| `claude-sonnet-4-5-20250929-thinking` | `cometapi-sonnet-4-5-20250929-thinking` |
| `claude-sonnet-4-5-20250929` | `cometapi-sonnet-4-5-20250929` |
| `claude-sonnet-4-5` | `cometapi-sonnet-4-5` |

### **`Claude Sonnet 4.5`** API Pricing in CometAPI，20% off the official price:

- Input Tokens: $2.4/ M tokens
- Output Tokens: $12/ M tokens

### Required Steps

- Log in to [cometapi.com](http://cometapi.com/). If you are not our user yet, please register first.
- Sign into your [CometAPI console](https://www.cometapi.com/console/token).
- Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.

![Claude Sonnet 4.5 API](https://resource.cometapi.com/blog/uploads/2025/09/cometapi-key-guide-1024x527.webp)

### Use Method

1. Select the “`claude-sonnet-4-5-20250929-thinking`”or “`claude-sonnet-4-5-20250929","claude-sonnet-4-5`” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience.
2. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account.
3. Insert your question or request into the content field—this is what the model will respond to.
4. . Process the API response to get the generated answer.

### API Example

CometAPI provides a fully compatible REST API—for seamless migration. [Key details](https://apidoc.cometapi.com/anthropic-claude-13851478e0):

- **Base URL:** `https://api.cometapi.com/v1/messages`
- **Model Names:** “ “`claude-sonnet-4-5-20250929-thinking`”or “`claude-sonnet-4-5-20250929","claude-sonnet-4-5`”
- **Authentication:** Bearer token via `Authorization: Bearer YOUR_CometAPI_API_KEY` header
- **Content-Type:** `application/json` .

Here’s a sample **cURL** snippet for invoking the Claude Sonnet 4.5 API:

```
curl --location --request POST 'https://api.cometapi.com/v1/messages' \
--header 'Authorization: Bearer {{api-key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"model": "claude-sonnet-4-5-20250929",
"max_tokens": 1000,
"thinking": {
"type": "enabled",
"budget_tokens": 1000
},
"messages": [
{
"role": "user",
"content": "Are there an infinite number of prime numbers such that n mod 4 == 3?"
}
]
}'
```

---

*Originally published at [https://www.cometapi.com/claude-sonnet-4-5-api/](https://www.cometapi.com/claude-sonnet-4-5-api/).*
