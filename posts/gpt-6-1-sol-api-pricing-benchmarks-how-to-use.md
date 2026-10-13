<!-- social-ops-fingerprint:041963e24d96f6155d225f0f5401f2858816633cb79aced03f0f73b3af855554 -->
---
title: GPT-6.1 Sol API: Pricing,  Benchmarks & How to Use
---
# GPT-6.1 Sol API: Pricing,  Benchmarks & How to Use

![GPT-6.1 Sol API: Pricing,  Benchmarks & How to Use](https://resource.cometapi.com/0bfca731-b3bf-4700-9ef3-c5e543962807.png)

## TL;DR

GPT-6.1 Sol is OpenAI's [September 2026 upgrade to GPT-6 Sol](https://openai.com/index/introducing-gpt-6-1-sol/), built for developers running advanced coding, computer-use, document, and multi-step agent workflows. It keeps standard short-context API pricing at $2 per million input tokens and $10 per million output tokens, while improving capability and task efficiency in OpenAI's reported evaluations. Its context window remains 1.05 million tokens, with up to 128,000 output tokens.

## Key Takeaways

- OpenAI released GPT-6.1 Sol on September 29, 2026 for complex coding, computer use, and professional workflows.
- It retains a 1,050,000-token context window and a 128,000-token output limit, with text and image input and text output.
- Standard short-context API rates are $2 input, $0.10 cached input, $2.50 cache writes, and $10 output per million tokens; larger prompts and processing modes change the bill.
- Official evaluations show improvements over GPT-6 Sol and near-Astra performance on several tested workloads; benchmark task-cost ratios are distinct from token-price ratios.
- Use the Responses API for tool calling. At launch, the model was available through the API, Codex, and ChatGPT Work for eligible paid plans, but not regular Chat.

## What Is GPT-6.1 Sol?

[GPT-6.1 Sol](https://deploymentsafety.openai.com/gpt-6-1-sol) is OpenAI's upgraded efficiency-focused model in the GPT-6 family. OpenAI describes it as an upgrade to GPT-6 Sol that nearly matches GPT-6 Astra on agentic coding, computer use, and professional work while costing one-fifth as much as Astra at standard input and output token rates.

The update is less about increasing raw context limits and more about improving how much useful work the model can complete per dollar. For teams already using the [GPT-6 Sol API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-sol/), GPT-6.1 Sol is best understood as a capability upgrade that keeps the same standard $2/$10 input-output pricing while cutting cached-input pricing in half.

That positioning matters for production agents. High-volume coding, document-processing, workflow-automation, and computer-use systems may execute hundreds or thousands of reasoning-heavy requests. A model that approaches frontier capability while maintaining lower per-task cost can be more practical than routing every difficult request to Astra.

One migration detail is important: GPT-6.1 Sol does not support `none` or `minimal` reasoning effort. The lowest setting is `low`, so developers migrating from GPT-6 Sol should review routing logic and request parameters.

## How Does GPT-6.1 Sol Perform on Benchmarks?

The results below come from OpenAI's launch evaluations. They measure particular tasks and configurations, rather than a universal model ranking. OpenAI evaluated its models in its research environment or through its API; system prompts, tools, and reasoning settings can differ from production ChatGPT. Competitor results were taken from public reports. Cost per task and standard token prices are different measures: the former depends on tokens, reasoning, tools, and the evaluation protocol. Where the announcement does not specify a full harness or configuration, the figures should be treated as reported comparisons rather than independently reproduced results.

### Agentic Coding Performance on DeepSWE v1.1

DeepSWE v1.1 evaluates long-horizon software-engineering tasks in real codebases. OpenAI reports that GPT-6.1 Sol matches GPT-6 Astra at roughly one-fifth of the cost and exceeds GPT-6 Sol's best score by 6.4 percentage points at a lower reasoning effort and cost.

This makes the upgrade particularly relevant to coding agents that repeatedly inspect repositories, modify files, run tools, execute tests, and debug failures rather than simply generate isolated code snippets.

### Business Workflow Performance on AutomationBench

AutomationBench measures whether agents can complete multi-step workflows across business applications. At medium reasoning effort, OpenAI reports that GPT-6.1 Sol scores 2.2 percentage points above Opus 5.5 at roughly one-third of the cost and improves 4.8 points over GPT-6 Sol at the same setting.

The benchmark uses 47 tools across sales, marketing, operations, support, finance, and HR, making it more representative of enterprise automation than a simple question-answer test.

The launch report identifies AutomationBench 1.0.6. Its Opus comparison is at medium reasoning effort; it is an OpenAI-reported result, not a claim that GPT-6.1 Sol wins every enterprise workflow. Developers can also access [Claude Opus 5.5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-opus-5-5/) for workload-specific comparisons.

### Computer-Use Performance on OSWorld 2.0

On the OSWorld 2.0 offline set, GPT-6.1 Sol at maximum reasoning effort outperforms GPT-6 Sol by seven percentage points at less than half the cost. It comes within 2.1 percentage points of GPT-6 Astra at roughly one-seventh of Astra's cost per task.

The OSWorld result uses partial reward on the offline set from the v2026.08.08 release. Keep that metric, version, and maximum-effort setting attached to the comparison; results from other releases or reward definitions are not directly interchangeable.

That improvement matters for browser agents, desktop automation, software operation, and workflows where the model must interact with graphical interfaces rather than only produce text.

### Scientific Workflow Performance on Terminal-Bench Science

Terminal-Bench Science 0.1 evaluates scientific workflows such as data analysis, simulation, model fitting, and theorem proving through code and terminal tools. OpenAI reports that GPT-6.1 Sol more than doubles GPT-6 Sol's score at maximum reasoning effort while costing less than half as much per task.

| Model | Average task cost at maximum effort |
| --- | --- |
| GPT-6.1 Sol | $5.47 |
| Opus 5.5 | $23.21 |
| GPT-6 Astra | $23.80 |

GPT-6 Astra remains the highest-scoring model in this evaluation at 68.1%, so GPT-6.1 Sol should not be interpreted as replacing Astra for every frontier research workload. Its advantage is the much lower task cost required to approach that capability.

### Factuality on Difficult Prompts

OpenAI reports the largest factuality improvement over GPT-6 Sol at low reasoning effort, where the share of answers containing a factual error falls from 11.4% to 7.7%, a reduction of about 32%. Across the tested reasoning settings, GPT-6.1 Sol stays within 1.9 percentage points of GPT-6 Astra while costing less than one-fifth as much per task.

OpenAI cautions that this evaluation uses deliberately difficult, de-identified conversations in which users previously flagged factual errors. The percentages therefore should not be treated as ordinary hallucination rates.

OpenAI's official factuality graphic plots error rate against mean simulated latency. It is reproduced directly from the system-card addendum; these selected, difficult conversations do not establish ordinary usage error rates.

![GPT-6.1 Sol API: Pricing,  Benchmarks & How to Use](https://resource.cometapi.com/1280000.PNG)

*Official OpenAI factuality evaluation: error rates on conversations flagged by users*

## GPT-6.1 API Pricing

GPT-6.1 Sol uses the same headline Standard input and output rates as GPT-6 Sol, but reduces the cached-input rate from $0.20 to $0.10 per million tokens. OpenAI prices the model differently depending on context length and processing mode, so production cost should be estimated from the full request pattern rather than only the headline token rate.

### Standard Pricing

Under OpenAI Standard processing, GPT-6.1 Sol costs $2 per million input tokens and $10 per million output tokens. Cached input is priced at $0.10 per million tokens, while cache writes cost $2.50 per million tokens.

| Standard pricing | OpenAI GPT-6.1 Sol | CometAPI GPT-6.1 Sol |
| --- | --- | --- |
| Input | $2.00 / 1M tokens | $1.60 / 1M tokens |
| Cached input | $0.10 / 1M tokens | $0.08 / 1M tokens |
| Cache write | $2.50 / 1M tokens | $2.00 / 1M tokens |
| Output | $10.00 / 1M tokens | $8.00 / 1M tokens |

### Cached Input and Cache Writes

Caching matters more for GPT-6.1 Sol than the headline input price alone suggests.

Its $0.10 cached-input rate is only 5% of the $2 uncached-input rate, making repeated context substantially cheaper when an application reuses the same system prompt, tool definitions, repository instructions, or long reference documents. Cache writes are billed at $2.50 per million tokens, or 1.25× the standard uncached input rate.

For long-running agents, this means cost depends heavily on how much context can be reused. A workflow that repeatedly sends a large stable prompt can have a very different effective cost from one that rebuilds the entire context on every request.

### Long-Context Pricing

GPT-6.1 Sol supports a 1.05 million-token context window, but requests above 272,000 input tokens move into OpenAI's long-context pricing tier.

For the full request, the rates become:

| Long-context pricing | OpenAI GPT-6.1 Sol | CometAPI GPT-6.1 Sol |
| --- | --- | --- |
| Input | $4.00 / 1M tokens | $3.20 / 1M tokens |
| Cached input | $0.20 / 1M tokens | $0.16 / 1M tokens |
| Cache write | $5.00 / 1M tokens | $4.00 / 1M tokens |
| Output | $15.00 / 1M tokens | $12.00 / 1M tokens |

In other words, once a prompt exceeds 272K input tokens, OpenAI applies 2× input and cache pricing and 1.5× output pricing to the entire request, not only to the portion above the threshold.

This makes context management important for large codebases, document-analysis systems, and persistent agents. A request just above the threshold can cost materially more than one kept below it through retrieval, summarization, or prompt segmentation.

### Batch, Flex, and Fast Modes

OpenAI also changes GPT-6.1 Sol pricing according to processing mode.

Batch and Flex processing are priced at 50% below Standard, making them useful when latency is less important than cost. Under short-context pricing, that reduces GPT-6.1 Sol to approximately $1/M input, $0.05/M cached input, $1.25/M cache write, and $5/M output.

Fast mode moves in the opposite direction. It costs 2× Standard, giving short-context rates of approximately $4/M input, $0.20/M cached input, $5/M cache write, and $20/M output. This mode is intended for workloads where lower latency is worth a higher token cost.

Regional processing can add another 10% premium where supported.

The practical choice is therefore straightforward: use Standard for normal interactive workloads, Batch or Flex when cost matters more than response time, and Fast only when latency has enough business value to justify roughly double the Standard rate.

## What Makes GPT-6.1 Sol Different?

GPT-6.1 Sol sharpens the separation between two high-end deployment choices. GPT-6 Astra is the capability-first option, while GPT-6.1 Sol becomes the efficiency-first option for advanced work.

That distinction can support hybrid routing: attempt GPT-6.1 Sol first for demanding production work, then escalate only unusually difficult or failed cases to Astra. This can preserve access to maximum capability without paying Astra-level rates for every request.

### Near-Astra Performance Without Astra-Level Cost

The central feature is the capability-to-cost ratio. OpenAI says GPT-6.1 Sol delivers near-Astra performance on several difficult professional workloads while charging one-fifth of Astra's standard input and output token prices.

For production systems, this can matter more than a small benchmark gap. Lower per-task cost can leave room for retries, verification steps, larger context, and higher request volume under the same budget.

### Better Agentic Coding

The DeepSWE result suggests that the upgrade is aimed at longer coding loops: repository-scale debugging, multi-file modification, test execution and repair, shell-based development workflows, and agentic software maintenance.

### Stronger Computer Use

The OSWorld improvement indicates stronger performance when reasoning must be combined with GUI interaction, making GPT-6.1 Sol more relevant to browser and desktop automation.

### Better Professional Document Work

On GDP.pdf, GPT-6.1 Sol scores higher than Opus 5.5 with fallbacks across tested reasoning settings at less than half the task cost, while approaching Astra at roughly one-fifth the cost.

That makes it promising for workflows involving financial reports, legal documents, healthcare materials, research papers, and other complex professional PDFs.

### Deep Tool Integration

Through the Responses API, GPT-6.1 Sol supports web search, file search, image generation, Code Interpreter, hosted shell, Apply Patch, Skills, computer use, MCP, and tool search.

## GPT-6.1 Sol vs GPT-6 Sol vs GPT-6 Astra

| Category and official model specifications | GPT-6 Sol | GPT-6.1 Sol | GPT-6 Astra |
| --- | --- | --- | --- |
| Positioning | Complex coding and agentic workflows | Near-Astra performance at lower cost | Highest capability for demanding work |
| Context window | 1.05M | 1.05M | 1.05M |
| Max output | 128K | 128K | 128K |
| Standard input / 1M | $2 | $2 | $10 |
| Cached input / 1M | $0.20 | $0.10 | $1.00 |
| Cache write / 1M | $2.50 | $2.50 | $12.50 |
| Output / 1M | $10 | $10 | $50 |
| Lowest reasoning effort | None | Low | Low |
| Agentic coding | Baseline for the reported DeepSWE improvement | 6.4 points above Sol's best score; matches Astra in the reported comparison | Matches Sol 6.1 in the reported DeepSWE comparison |
| Computer use | Baseline for the reported OSWorld comparison | 7-point gain vs Sol; 2.1 points below Astra at max effort on the specified offline set | Leads Sol 6.1 by 2.1 points in that reported comparison |
| Best fit | Existing Sol workloads | High-volume advanced agents | Hardest frontier workloads |

The pricing difference is especially clear when comparing with the [GPT-6 Astra API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-astra/). Official OpenAI pricing is $10 input and $50 output per million tokens for Astra versus $2 and $10 for GPT-6.1 Sol.

### Which GPT-6 Model Should You Choose?

**GPT-6.1 Sol is the strongest default choice for most advanced production workloads.** It keeps the same $2 input and $10 output pricing as GPT-6 Sol, but improves agentic coding, computer use, and professional workflows while moving much closer to GPT-6 Astra.

Choose **GPT-6 Sol** if your existing workflow already performs well and you do not need the newer agentic improvements.

Choose **GPT-6.1 Sol** if you want the best balance of performance and cost, especially for coding agents, automation, computer use, and high-volume reasoning workloads.

Choose **GPT-6 Astra** when maximum capability matters more than cost. Its official OpenAI pricing is $10 input and $50 output per million tokens, compared with $2 and $10 for GPT-6.1 Sol. The [GPT-6 Astra API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-astra/) is therefore better suited to the most difficult or high-value tasks rather than routine large-scale deployment.

### When Should You Still Use GPT-6 Astra?

GPT-6.1 Sol does not replace Astra. OpenAI continues to position GPT-6 Astra as its highest-capability model, and Astra still leads difficult evaluations such as Terminal-Bench Science.

- Task success matters much more than token cost.
- The job is unusually complex or research-heavy.
- You need the highest available reasoning ceiling.
- Failed attempts are expensive enough that higher model cost is secondary.
- A small quality difference produces disproportionate business value.

A practical routing strategy is to use GPT-6.1 Sol for the majority of demanding production work and reserve Astra for escalation paths where maximum capability justifies the added cost.

### Is GPT-6.1 Sol Cheaper Than GPT-6 Astra in Real Workloads?

At standard token rates, yes: GPT-6.1 Sol costs one-fifth as much as Astra for both input and output. But production economics should be evaluated as cost per successful task, not only cost per token.

If an agent needs repeated reasoning, tool calls, and retries, a cheaper model can still be less economical if it requires many more attempts. Conversely, if GPT-6.1 Sol achieves nearly the same completion rate as Astra on your workload, the fivefold token-price difference can translate into substantial savings.

## Where Can You Use GPT-6.1 Sol?

At launch on September 29, 2026, GPT-6.1 Sol was available to Plus, Pro, Business, Enterprise, and Edu users in ChatGPT Work and Codex, as well as through the OpenAI API. It was not yet available in regular Chat. Actual access can depend on plan, client, region, and workspace settings. As checked on September 30, 2026, the [CometAPI live model catalog](https://api.cometapi.com/api/models) lists gpt-6.1-sol with both /v1/responses and /v1/chat/completions routes. Use Responses for tool workflows, and verify model access and billing for your API key before deployment.

## How Do You Use the GPT-6.1 Sol API?

Use the [Responses API for tool calling](https://developers.openai.com/api/docs/models/gpt-6.1-sol). GPT-6.1 Sol supports Chat Completions requests without tools; tool-dependent agents should not assume the same tool behavior across both endpoints. The minimal Python example below uses OpenAI's endpoint and credentials.

Install the official OpenAI Python SDK, set OPENAI\_API\_KEY in your environment, and use an API project with access to the model. The following text-only example sends one Responses API request and prints its text output; it does not itself enable agent tools.

```
from openai import OpenAI

client = OpenAI()  # Reads OPENAI_API_KEY from the environment

response = client.responses.create(
    model="gpt-6.1-sol",
    input="Review this software architecture and identify the three highest-risk design decisions.",
    reasoning={"effort": "medium"},
)

print(response.output_text)
```

For harder coding, research, or agent tasks, reasoning effort can be increased to `high`, `xhigh`, or `max`. For lower-cost work, `low` is available, but `none` and `minimal` are not supported.

### Use GPT-6.1 Sol Through CometAPI

Follow the [CometAPI quickstart](https://www.cometapi.com/quickstart/) to create an account and an API key. Store the key in COMETAPI\_KEY, install the OpenAI Python SDK with pip install openai, and configure the gateway as shown below.

The catalog currently lists gpt-6.1-sol. This text-only example uses the [documented Responses endpoint](https://apidoc.cometapi.com/api/text/responses); tools require additional request configuration. Model listing confirms catalog availability, while a successful request with your key confirms access for your account.

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
)

response = client.responses.create(
    model="gpt-6.1-sol",
    input="Review this architecture and list three design risks.",
    reasoning={"effort": "medium"},
)
print(response.output_text)
```

Choose low, medium, high, xhigh, or max reasoning effort. Do not send none or minimal. For authentication failures, check the key and account balance; for model or route errors, recheck the current catalog and endpoint. Run a small smoke test before switching production traffic.

## What Do OpenAI's GPT-6.1 Sol Safety Evaluations Show?

OpenAI's [GPT-6.1 Sol system-card addendum](https://deploymentsafety.openai.com/gpt-6-1-sol/respecting-auto-review) reports alignment improvements over GPT-6 Sol, including lower failure rates in difficult evaluations involving broken-tool transparency, explicit restrictions, unauthorized outcomes, and computer-use safety.

OpenAI treats GPT-6.1 Sol as Critical in cybersecurity capability and High in biological and chemical capability under its Preparedness Framework, and applies the same safeguards stack used for GPT-6 Astra.

These evaluations intentionally use difficult scenarios designed to elicit failures, so their rates should not be read as representative of typical usage.

## FAQ

### Is GPT-6.1 Sol a replacement for GPT-6 Sol?

GPT-6.1 Sol is a newer upgrade rather than a completely different product direction. It targets the same advanced coding and agentic workloads as GPT-6 Sol, but improves performance in areas such as software engineering, computer use, and multi-step automation.

### Is GPT-6.1 Sol as powerful as GPT-6 Astra?

Not across every workload. GPT-6 Astra remains OpenAI's higher-capability option for the most demanding tasks, while GPT-6.1 Sol is designed to close much of the performance gap with better efficiency for large-scale production use.

### Who should use GPT-6.1 Sol?

GPT-6.1 Sol is most relevant to developers and teams running coding agents, automation systems, document workflows, computer-use agents, and other workloads where strong reasoning needs to be used repeatedly at scale.

### What is the biggest improvement in GPT-6.1 Sol?

The biggest improvement is not a larger context window or a new input modality. It is stronger real-world agent performance, especially in coding, computer use, and professional workflows, while staying in the same general cost tier as GPT-6 Sol.

## Conclusion

GPT-6.1 Sol is less about extending GPT-6's raw specification limits and more about moving advanced reasoning down the cost curve. It keeps the 1.05M context window and 128K output ceiling while improving coding agents, business workflows, computer use, scientific workflows, and factual accuracy over GPT-6 Sol.

At the same time, standard input and output pricing remains $2/$10 per million tokens, compared with Astra's $10/$50.

For developers, that creates a useful deployment tier: Astra remains available when maximum capability matters, while GPT-6.1 Sol can handle a larger share of advanced production workloads without forcing every request into flagship-level economics. The most meaningful benchmark, however, remains your own workload.

---

*Originally published at [https://www.cometapi.com/what-is-gpt-6-1-sol/](https://www.cometapi.com/what-is-gpt-6-1-sol/).*
