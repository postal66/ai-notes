<!-- social-ops-fingerprint:a4f33ce7ddb3ab439aff58b6ec65ca8279becc044bf7c7501cfa9233c35040b9 -->
---
title: Hunyuan Hy4 Is Available on CometAPI: Features, API Access
---
# Hunyuan Hy4 Is Available on CometAPI: Features, API Access

![Hunyuan Hy4 Is Available on CometAPI: Features, API Access](https://resource.cometapi.com/console/blog-banner/2026/11/af11051e14504a09863c3def471ebf4d.png)

Hunyuan Hy4 and Hy4 Preview are both accessible through CometAPI, giving developers a way to test Tencent’s latest flagship against the earlier version within the same API integration. Hy4 Flash is coming soon.

Tencent officially released Hy4 on November 4, 2026. The [announcement on X](https://x.com/TencentHunyuan/status/2117870250838630539) introduces the model with “Hy4 is here, new with vision,” while the [official Hy4 release page](https://hy.tencent.ai/research/hy4?langVersion=en) details its improvements in coding, computer use, research, and productivity.

For developers, the immediate starting point is the [Hy4 API](https://www.cometapi.com/models/hunyuan/hy-4/) on CometAPI. The model is listed as available with the identifier `hy4`, priced at $0.6672 per million input tokens and $2.00 per million output tokens. Teams already using Hy4 Preview can keep it as a baseline while evaluating the full release.

## Key Takeaways

- Hy4 and Hy4 Preview are accessible on CometAPI. Developers can compare them through one OpenAI-compatible integration.
- Hy4 is officially released**.** “Coming soon” now applies to Hy4 Flash, whose final pricing and serving specifications remain unpublished in the cited announcements.
- The full release adds visual understanding and computer-use capabilities, alongside stronger long-horizon reasoning and productivity workflows.
- Tencent reports 78.9 on OSWorld 2.1 and 44.4 on Terminal Bench 4.0, with additional results covering coding, automation, and scientific work.
- CometAPI lists Hy4 input and output prices around 20% below the official prices shown on its model page.
- Practical deployment needs an application runtime: the model plans and requests actions; the runtime executes tools, maintains state, and checks results.

## What Is Hunyuan Hy4?

Hunyuan Hy4 is Tencent’s flagship model for complex reasoning, software engineering, office work, financial analysis, game development, and scientific research. The November release extends the Hy4 generation into visual tasks and computer interaction, including both command-line interfaces and graphical interfaces.

According to [Tencent Technology’s launch report](https://news.qq.com/rain/a/20261104A06OU500?adChannelId=news), Hy4 uses a 770-billion-parameter Mixture-of-Experts architecture. Tencent’s [API documentation](https://www.tencentcloud.com/zh/document/product/1300/80695) lists a 1M-token context window, with maximum API input of 960,000 tokens and maximum output of 64,000 tokens. These are Tencent’s documented limits; configure CometAPI requests against the limits exposed by its active endpoint.

An MoE model routes tokens through selected experts rather than using every parameter for every token. The earlier Hy4 Preview disclosed 49 billion active backbone parameters per token; that Preview figure should stay attached to Preview when discussing its architecture.

Tencent says Hy4’s weights will be open-sourced later, with deployment support being developed alongside vLLM and SGLang. API access is already available, while the final model’s downloadable weights are a separate release milestone.

### Hy4 Performance

Tencent’s [official release](https://hy.tencent.ai/research/hy4?langVersion=en) reports the following results. These are Tencent-reported scores under its evaluation configurations; the benchmarks use different scoring methods and should be compared within each benchmark.

| Benchmark | Hy4 reported score | Relevant workload |
| --- | --- | --- |
| OSWorld 2.1 | 78.9 | Computer interaction and GUI tasks |
| Terminal Bench 4.0 | 44.4 | Command-line problem solving |
| FrontierCode 2.0 | 31.0 | Difficult coding tasks |
| AutomationBench 1.0.6 | 56.2 | Multi-step automation |
| Hy-BrowseComp 2.0 — internal | 59.9 | Browsing and information gathering |
| TenureTrail — internal | 53.6 | Scientific research tasks |

The broader launch evidence includes a financial evaluation involving 213 experts and 579 tasks. Tencent Technology reports an average score of 3.04 for Hy4, compared with 2.97 for DeepSeek V4.1 Flash 1017 and 2.68 for both Kimi K3.1 Pro and GLM-5.3 in that evaluation.

For a team building financial document analysis or research assistants, that is a reason to include Hy4 in a controlled comparison. The benchmark scores do not provide a measured latency or tokens-per-second figure for CometAPI; those need to be collected from the intended deployment.

## Hy4 vs. Hy4 Preview: What Has Change?

Tencent has highlighted three major upgrades for the full Hy4 release.

### Stronger Long-Horizon Task Execution

Hy4 Preview established the family’s focus on extended coding and productivity tasks. Its documented weaknesses included excessive verification and spending longer than necessary reasoning through some problems. The full release targets more efficient reasoning and more sustained execution across a sequence of actions.

For an agent application, the useful comparison is whether Hy4 reaches the same acceptance criteria with fewer retries, less repeated context, or fewer abandoned steps. A shorter response only reduces cost when the resulting work still passes validation.

### Visual Understanding and Computer Use

Hy4 adds visual understanding and visual reasoning to the family. It can interpret charts, screenshots, and other images, while its computer-use training covers CLI and GUI interaction. Tencent specifically describes training involving Blender, CAD, and workflows that cross application boundaries.

This expands the tasks an agent can attempt. It can inspect a chart before explaining its errors, examine a webpage after generating it, or use a screenshot to decide the next interface action. Browser and desktop execution require a connected tool environment, as described in the runtime architecture below.

### More Concrete Evidence from Productivity Evaluations

Tencent reports improvements across engineering, office work, finance, and games. The launch report gives Hy4 a 96.15% pass rate in WorkBuddy’s internal evaluation and reports improvements over Preview of 19.1% on GameDev and 9.8% on GameLogic.

These results support testing Hy4 on multi-step productivity work. Their value is strongest when the application resembles the evaluated tasks: coding, document work, structured analysis, and repeated tool use.

## 4 Hands-On Scenarios: Where Hy4 Looks Useful

Tencent Technology has tested Hy4 across four scenarios covering coding, visual understanding, financial analysis, and planning.

### Interactive Frontend Development

Hy4 built an interactive solar-system webpage with clickable planets, adjustable orbital speed, and child-friendly explanations. The reported execution included 15 Chrome interaction checks, showing a workflow that extends from code generation to browser verification. Applications using CometAPI can support this workflow by connecting Hy4 to browser tools.

### Visual Planning Under Changing Constraints

Using a refrigerator photo, Hy4 planned nine meals over three days within a RMB 100 grocery budget and 40-minute preparation limit per meal. It flagged four uncertain ingredients and revised the plan when dietary requirements changed, demonstrating how visual understanding can support planning across multiple constraints.

### Financial Chart Analysis

Hy4 identified misleading claims in a fictional chart: revenue rose 25%, rather than the claimed 80%, while profit fell 40%, despite a claim that it doubled. It also detected a truncated axis that exaggerated growth, combining visual interpretation with numerical checks.

### Scheduling and Feasibility Checks

Given 555 minutes of serial work within a 480-minute window, Hy4 identified the 75-minute capacity shortfall and proposed three revised plans. The scenario illustrates its usefulness for detecting conflicting requirements and explaining the trade-offs needed to make a plan feasible.

## Hy4 Pricing on CometAPI

As of November 4, 2026, [CometAPI’s Hy4 pricing](https://www.cometapi.com/models/hunyuan/hy-4/#pricing) is:

| Token category | CometAPI price per 1M tokens |
| --- | --- |
| Input | $0.6672 |
| Output | $2.00 |
| Cache read | $0.0336 |

CometAPI lists Tencent’s official Hy4 rates at $0.8340 for input and $2.50 for output per million tokens, making CometAPI’s input and output prices approximately 20% lower. These rates apply to Hy4; consult the separate rate card for Hy4 Preview.

### Typical Request Cost

For an illustrative request using 10,000 uncached input tokens and 2,000 output tokens, the Hy4 token charge is:

```
Input:  10,000 / 1,000,000 × $0.6672 = $0.006672
Output:  2,000 / 1,000,000 × $2.00   = $0.004000
Total:                                  $0.010672
```

That is approximately $0.0107 per request, or $10.67 for 1,000 requests with the same token usage. This is a token-cost estimate, excluding browser or compute infrastructure and other tool charges. Cache-read pricing applies to tokens actually billed as cache reads.

For agents, calculate usage across the entire task. Repeated prompts, tool results, generated reasoning, and retries can make a ten-step run substantially more expensive than its final answer suggests. The useful business metric is total spend divided by successfully completed tasks.

## How to Access Hy4 API

Hy4 and Hy4 Preview are both accessible through CometAPI. Use `hy4` for the full release or `hy4-preview` to compare the earlier version.

### Create an Account and Get Your API Key

1. Register or sign in to [CometAPI](https://www.cometapi.com/console/login).
2. Open [API Keys](https://www.cometapi.com/console/token), select Create API Key, and copy your key.
3. Ensure your account has sufficient credits, then store the key in a server-side environment variable.

Install the Python SDK and configure your key:

```
pip install openai
export COMETAPI_KEY="YOUR_COMETAPI_KEY"
```

### Choose Chat Completions or Responses

CometAPI documents two OpenAI-compatible interfaces:

- Chat Completions (`/v1/chat/completions`) uses a `messages` array containing user and assistant turns. This is the interface used in the Hy4 example below and fits applications already built around chat messages.
- Responses (`/v1/responses`) uses an `input` field and a different output structure. Use it when the selected model explicitly supports Responses through CometAPI.

For Hy4, start with **Chat Completions**. Check the [CometAPI API documentation](https://apidoc.cometapi.com/api/text) for model compatibility before switching to Responses.

### Send Your First Request

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
)
result = client.chat.completions.create(
    model="hy4",  # Or "hy4-preview"
    messages=[{"role": "user", "content": "Explain how to resolve a scheduling conflict."}],
)
print(result.choices[0].message.content)
```

Keep the same client configuration when comparing Hy4 with Preview and change the model identifier. For current rates, see [Hy4 pricing on CometAPI](https://www.cometapi.com/models/hunyuan/hy-4/#pricing); for additional setup details, follow the [API key and first-call guide](https://apidoc.cometapi.com/overview/quick-start).

## What Developers Should Prepare Now

Developers can prepare for Hy4 and Hy4 Flash by making the model layer configurable. The model name, API endpoint, tool schema, routing logic, and evaluation scripts should not be hard-coded into the rest of the application.

Before sending production traffic to a new model, establish a baseline with Hy4 Preview or another currently available model. The baseline should cover the workloads that matter to the application, such as customer support, coding, document processing, or data analysis.

The evaluation should record more than whether the final answer looks good. Teams should track the following metrics:

- **Task completion rate:** Measure how often the agent completes the entire workflow and delivers the requested result without human intervention. A task should count as successful only when all required steps have been completed, not merely when the model produces a plausible intermediate response.
- **Tool-call success rate:** Record how often the agent selects the correct tool, uses valid parameters, receives a usable result, and continues the workflow successfully. This helps distinguish a reasoning problem from an integration or schema problem.
- **Retry frequency:** Count how many times the agent needs to retry a tool call, regenerate an answer, or restart a step. A high retry rate can increase costs and delay completion even when the final answer appears correct.
- **Average response latency:** Measure the time required for the model to return a response and, for agent workflows, the time required to complete the full task. It is useful to track both per-step latency and end-to-end latency because a fast individual response may still produce a slow multi-step workflow.
- **Token usage:** Track input tokens, output tokens, cached tokens where applicable, and total tokens per request. This shows whether a model's reasoning style is creating unnecessary context or verification overhead.
- **Cost per completed task:** Calculate the total model and infrastructure cost required to finish one successful task. This is more useful than comparing token prices alone because a cheaper model may require more retries, longer prompts, or additional human intervention.

Once Hy4 and Hy4 Flash become available, developers can run the same workloads against both models and compare completion quality, reliability, speed, and cost.

A practical routing policy would send repetitive, standardized tasks to Hy4 Flash and reserve Hy4 for complex planning, long tool chains, visual reasoning, and workflows that require stronger recovery behavior.

## Hy4 Flash: A Practical Model for High-Volume Workloads

Hy4 is already available, while Hy4 Flash is expected to launch soon. Tencent has yet to announce its release date. Tencent positions it as a highly cost-efficient model for practical applications.

The Flash version is expected to retain Hy4's visual and agent capabilities while benefiting from closer co-design between the model and Tencent's products. This positioning suggests a model optimized for frequent calls, faster response cycles, and larger request volumes.

Hy4 would be better suited to complex, long-running agent tasks that require deeper planning, multiple tool calls, and stronger recovery behavior. Hy4 Flash would be a better fit for high-volume classification, information extraction, routine document processing, and other structured tasks where cost and throughput are priorities.

Both models may be useful for visual workloads. Hy4 Flash could handle basic OCR, image classification, and field extraction, while Hy4 could be reserved for visual tasks that require cross-page analysis, complex judgment, or several rounds of tool use.

Hy4 Flash may also be useful during rapid agent development. Teams can use it to test prompts, tool schemas, and routing logic at a lower cost before sending more demanding workloads to Hy4.

For safety-critical or highly difficult decisions, Hy4 should be paired with human review. The model can perform the analysis, but a person should remain responsible for actions involving refunds, payments, permissions, or other consequential outcomes.

## Frequently Asked Questions

### Is Hy4 officially released?

Yes. Tencent released Hy4 on November 4, 2026, with an [official research announcement](https://hy.tencent.ai/research/hy4?langVersion=en) and an [announcement on X](https://x.com/TencentHunyuan/status/2117870250838630539).

### Can I access Hy4 and Hy4 Preview through CometAPI?

Yes. Both are accessible through CometAPI. Use `hy4` for Hy4 and `hy4-preview` for Preview, and keep the model identifier configurable when comparing results.

### Dos an API call let Hy4 operate my browser automatically?

A computer-use workflow needs an application that connects Hy4 to a browser or desktop environment. The application executes actions and returns screenshots or tool results to the model.

### How much does Hy4 cost on CometAPI?

The November 4 listing gives prices of $0.6672 per million input tokens, $2.00 per million output tokens, and $0.0336 per million cache-read tokens. The [model page](https://www.cometapi.com/models/hunyuan/hy-4/#pricing) is the reference for current rates.

### Is Hy4 Flash available now?

The cited announcements describe Hy4 Flash as coming soon. Its final pricing and serving specifications have not been published in those materials.

## Conclusion

Hy4 is ready for API evaluation on CometAPI, and Preview gives teams a baseline for measuring the upgrade. The published results and reported hands-on scenarios make coding, visual analysis, constrained planning, and multi-step productivity work the most useful places to start.

Begin with the [Hy4 API and pricing page](https://www.cometapi.com/models/hunyuan/hy-4/), connect the tools required by the workflow, and compare cost per completed task. When Hy4 Flash arrives, the same evaluation setup can determine which tasks benefit from its efficiency-focused

---

*Originally published at [https://www.cometapi.com/hunyuan-hy4-released/](https://www.cometapi.com/hunyuan-hy4-released/).*
