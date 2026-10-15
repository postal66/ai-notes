<!-- social-ops-fingerprint:eef5c058976d8bc595e7c1a0636fd84b856bd5178216388cc9791b5797d0b8d8 -->
---
title: Grok 4.7: Benchmarks, Pricing, Features and API Access
---
# Grok 4.7: Benchmarks, Pricing, Features and API Access

![Grok 4.7: Benchmarks, Pricing, Features and API Access](https://resource.cometapi.com/grok-4-7-og.webp)

**TL;DR** [Grok 4.7](https://www.cometapi.com/models/xai/grok-4-7/) is SpaceXAI's frontier model for coding, agentic workflows, and professional knowledge work, released on September 21, 2026. It combines a 500,000-token context window, text and image input, configurable reasoning, function calling, web and X search, and code execution.

For prompts below 200,000 tokens, the official xAI API lists $2 per million input tokens, $0.50 per million cached input tokens, and $6 per million output tokens. CometAPI currently lists Grok 4.7 at $1.60 input, $0.40 cached input, and $4.80 output per million tokens for the same tier—a 20% reduction from the official rates shown on its model page.

The practical value proposition is not universal benchmark leadership. Grok 4.7 is most compelling when a workload combines engineering tasks, long agent loops, tool use, large working contexts, and sensitivity to output-token cost. Teams should validate it on their own repositories and workflows before production routing.

## Key Takeaways

- Grok 4.7 uses a larger base model than Grok 4.6, longer reinforcement learning on harder multi-hour tasks, and stronger self-verification.
- The API supports a 500,000-token context window, text and image input, text output, four reasoning levels, structured output, function calling, web and X search, and code execution.
- SpaceXAI reports 46.3% on CursorBench 4.0, 71.0% on DeepSWE v1.1, and 38.0% on Terminal-Bench 4.0. These are vendor-published results, not proof of universal leadership.
- CometAPI lists Grok 4.7 as available, with an OpenAI-compatible endpoint and prices 20% below the official xAI rates shown in its current catalog.
- Choose Grok 4.7 for cost-sensitive engineering agents and sustained tool use; choose alternatives when very long context or a benchmark-critical domain matters more than unit price.

## What Is Grok 4.7?

[Grok 4.7](https://www.cometapi.com/) is SpaceXAI's latest frontier large language model, positioned for **coding, autonomous agent tasks, and professional knowledge work**. The release focuses on tasks that require sustained interaction, tool use, verification, and revision rather than only one-shot answers.

SpaceXAI says Grok 4.7 was trained with a [longer reinforcement-learning run on a harder mix of tasks](https://x.ai/news/grok-4-7), weighted toward problems that can take many hours to complete. This training direction makes it especially relevant to repository-level software engineering, debugging, research, document creation, engineering analysis, and multi-step automation.

## How Is Grok 4.7 Different From—and Better Than—Grok 4.6?

### A Larger Base Model

Grok 4.7 moves to a larger base model than Grok 4.6. SpaceXAI has not disclosed a finalized public parameter count, so the defensible conclusion is increased base-model capacity—not a specific parameter estimate.

### Longer Reinforcement Learning on Harder Tasks

The reinforcement-learning stage was extended and shifted toward harder, longer-horizon problems. SpaceXAI emphasizes tasks that may require hours of work, aligning the model with autonomous coding, research, and professional agent workflows.

### Stronger Self-Verification

Grok 4.7 is trained to inspect its own work more carefully. That matters in software engineering because a reliable agent must repeatedly inspect, modify, test, diagnose failures, revise, and validate—not merely generate a first answer.

### Measured Improvements Over Grok 4.6

| Dimension | Grok 4.6 | Grok 4.7 | Change |
| --- | --- | --- | --- |
| CursorBench 4.0 | 40.4% | 46.3% | +5.9 pts |
| DeepSWE v1.1 | 65.2% | 71.0% | +5.8 pts |
| EEBench | 53.0% | 64.0% | +11.0 pts |
| AA Briefcase v1.1 | 1,546 | 1,657 | +111 |
| Terminal-Bench 4.0 | 20.3% | 38.0% | +17.7 pts |
| Harvey Legal Agent Benchmark | 15.8% | 19.6% | +3.8 pts |
| HealthBench Professional | 48.5% | 56.7% | +8.2 pts |

Across the published launch suite, Grok 4.7 improves over Grok 4.6 in every listed result. The largest absolute gain is on Terminal-Bench 4.0, consistent with the release emphasis on long-running command-line and tool-use workflows. These numbers remain vendor-published and should be tested against real tasks before a migration decision.

## How Good Is Grok 4.7 on Benchmarks?

SpaceXAI's launch evaluation covers software engineering, terminal work, professional office tasks, legal work, clinical reasoning, and electrical engineering. These are vendor-published results and should be validated against production workloads before procurement or routing decisions.

| Benchmark | Grok 4.7 xHigh | Grok 4.6 High | GPT-5.6 Sol Max | Fable 5.1 Max |
| --- | --- | --- | --- | --- |
| CursorBench 4.0 | 46.3% | 40.4% | 41.7% | 51.8% |
| DeepSWE v1.1 | 71.0%\* | 65.2% | 72.7% | 70.0% |
| EEBench | 64.0% | 53.0% | 39.4% | 56.4% |
| AA Briefcase v1.1 | 1,657 | 1,546 | 1,487 | 1,678 |
| Terminal-Bench 4.0 | 38.0% | 20.3% | 37.3% | 57.9% |
| Harvey Legal Agent Benchmark | 19.6% | 15.8% | 2.5% | 6.7% |
| HealthBench Professional | 56.7% | 48.5% | 60.5% | 62.1% |

In its [Grok 4.7 launch results](https://x.ai/news/grok-4-7), SpaceXAI marks the 71.0% DeepSWE v1.1 score as high reasoning effort.

The launch announcement does not disclose every per-benchmark harness, tool configuration, run count, or evaluation environment. Treat these values as vendor-published results and validate the model on your own repositories, tools, latency targets, and failure criteria before routing production work.

## What Does the Grok 4.7 Benchmark Profile Show?

### Software Engineering

CursorBench 4.0 rises from 40.4% on Grok 4.6 to 46.3% on Grok 4.7, while DeepSWE v1.1 rises from 65.2% to 71.0%. This supports Grok 4.7's positioning as a model for coding agents rather than only conversational coding assistance.

### Long-Running Terminal Work

Terminal-Bench 4.0 shows one of the largest generational changes: 20.3% for Grok 4.6 versus 38.0% for Grok 4.7. The 17.7-point absolute gain is consistent with SpaceXAI's emphasis on longer-horizon reinforcement learning and self-verification.

### Electrical Engineering

On EEBench, Grok 4.7 reaches 64.0%, compared with 53.0% for Grok 4.6. Among the published comparisons, this is one of Grok 4.7's strongest relative results.

### Professional Knowledge Work

AA Briefcase v1.1 rises from 1,546 to 1,657. These tasks are designed to reflect multi-hour professional work involving artifacts such as documents, presentations, analysis, and other structured deliverables.

## Grok 4.7 vs GPT-5.6 Sol vs Fable 5.1: How Do They Compare?

Provider-native pricing checks: OpenAI lists GPT-5.6 Sol at $4 per million input tokens and $20 per million output tokens, while Anthropic lists Claude Fable 5.1 at $10 per million input tokens and $50 per million output tokens.

| Dimension | Grok 4.7 | GPT-5.6 Sol | Claude Fable 5.1 |
| --- | --- | --- | --- |
| Primary positioning | Coding, agentic tasks, knowledge work | Complex professional reasoning and coding | Long-running agents, coding, and knowledge work |
| Context window | 500,000 tokens | 1,050,000 tokens | 1,000,000 tokens |
| Modalities | Text and image input; text output | Text and image input; text output | Text and image input; text output |
| Reasoning control | Low, medium, high, xhigh | None through max | Adaptive thinking with configurable effort |
| Provider API status | Available on the public xAI API | Available through OpenAI Chat Completions and Responses | Available through the Claude API and supported cloud marketplaces |
| Input price / 1M tokens | $2 | $4 | $10 |
| Output price / 1M tokens | $6 | $20 | $50 |
| CursorBench 4.0 | 46.3% | 41.7% | 51.8% |
| DeepSWE v1.1 | 71.0% | 72.7% | 70.0% |
| Best fit | Price-sensitive engineering agents and sustained tool use | Broad professional reasoning with very long context | Maximum-capability long-running agent and knowledge workflows |

### Which Model Should You Choose?

- **Choose Grok 4.7** when engineering workloads, sustained tool use, configurable reasoning, and lower output-token cost are the priority. It is particularly attractive for repository agents, terminal workflows, and large-context research that stays below the 200K pricing threshold.
- **Choose GPT-5.6 Sol** when the task needs broader professional reasoning, a context window above one million tokens, or when its stronger result on a business-critical evaluation such as DeepSWE or clinical reasoning has been validated in your own harness.
- **Choose Claude Fable 5.1** when maximum long-running agent performance, coding quality, terminal execution, or clinical reasoning justifies its higher token price.
- **Use model routing** when workloads vary. Route routine engineering and high-volume agent steps to the most cost-efficient qualified model, and reserve a more expensive model for tasks where measured success rates justify the premium.

The correct choice depends on end-to-end task success, latency, retries, tool-call accuracy, and human rework—not on a single benchmark or headline token rate.

## How Much Does the Grok 4.7 API Cost?

The table below compares the official xAI rates with the prices displayed on CometAPI's Grok 4.7 model page on September 22, 2026. CometAPI states a 20% discount; verify live pricing before production because gateway prices and promotional terms can change.

| Prompt tier | Price type | xAI official | CometAPI | Difference |
| --- | --- | --- | --- | --- |
| Below 200K prompt tokens | Input / 1M | $2.00 | $1.60 | 20% lower |
| Cached input / 1M | $0.50 | $0.40 | 20% lower |  |
| Output / 1M | $6.00 | $4.80 | 20% lower |  |
| Above 200K prompt tokens | Input / 1M | $4.00 | $3.20 | 20% lower |
| Cached input / 1M | $1.00 | $0.80 | 20% lower |  |
| Output / 1M | $12.00 | $9.60 | 20% lower |  |

### Standard Context Pricing for Prompts Up to 200,000 Tokens

For requests whose prompt does not exceed 200,000 tokens, Grok 4.7 costs **$2 per million input tokens**, **$0.50 per million cached input tokens**, and **$6 per million output tokens**. Cached input is the least expensive category, so applications with repeated system instructions or reusable context can reduce cost when those tokens qualify for caching.

For a simple example, a request using 100,000 uncached input tokens and producing 10,000 output tokens would cost about $0.26 before any other platform charges: $0.20 for input plus $0.06 for output.

### Long-Context Pricing Above 200,000 Prompt Tokens

Once the prompt exceeds 200,000 tokens, the rates double to **$4 per million input tokens**, **$1 per million cached input tokens**, and **$12 per million output tokens**. The higher tier applies because of prompt length, so teams should monitor accumulated conversation history, tool traces, retrieved documents, and repository context before sending each request.

The practical cost decision is therefore not only how many tokens a task uses, but whether the prompt crosses the 200,000-token boundary. Summarizing completed work, removing obsolete tool output, and retrieving only the most relevant files can keep suitable workloads in the standard tier without sacrificing necessary context.

The [SpaceXAI release notes](https://docs.x.ai/developers/release-notes) document this threshold. Production budgets should also account for retries, agent loops, failed tool calls, and output length rather than comparing providers only by their headline input-token price.

## What Makes Grok 4.7 Useful for AI Agents?

- **500K context window:** Holds substantial source code, specifications, tool output, logs, and conversation history in one working context. This is useful for repository-scale coding and multi-document analysis, although context still needs active pruning.
- **Configurable reasoning:** Applications can select low, medium, high, or xhigh effort, trading latency and compute for deeper reasoning according to task difficulty.
- **Function calling and structured output:** Agents can query databases, run tests, inspect documents, call internal APIs, and return machine-readable results.
- **Web and X search:** Search tools can retrieve current information when the model's training data is insufficient. Retrieved content should still be treated as untrusted input and verified.
- **Code execution:** The model can validate calculations, transform data, and test generated solutions instead of relying solely on language-model inference.
- **Long-horizon workflow focus:** The training emphasis on multi-hour tasks, context management, and self-verification targets agent loops that accumulate tool traces and require recovery after failure.

## How Does Grok 4.7 Improve Safety?

SpaceXAI says Grok 4.7 introduces an [entirely new safeguard stack](https://x.ai/news/grok-4-7) and reports stronger jailbreak resistance and dual-use safety. In the launch announcement, the company reports 62.4% on LatchBio's biosafety benchmark and says only 3.3% of risky dual-use prompts were allowed through on HackerBench v0.3.

These figures are vendor-published evaluations. They are useful for understanding the release claims but should not be treated as a universal measure of real-world safety performance.

## How Can Developers Use the Grok 4.7 API?

[Grok 4.7 is currently available through CometAPI](https://www.cometapi.com/models/xai/grok-4-7/) under the model ID **grok-4.7**. [CometAPI](https://www.cometapi.com/) provides an OpenAI-compatible endpoint, one API key and billing workflow across multiple model providers, easier side-by-side model testing and routing, and currently listed token prices that are 20% below the official xAI rates. Before production use, confirm the live model page, endpoint health, supported parameters, pricing, and data-handling requirements.

**CometAPI request example:**

```
curl "https://api.cometapi.com/v1/responses" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $COMETAPI_KEY" \
  -d '{
    "model": "grok-4.7",
    "input": "Explain how a distributed task queue handles worker failure."
  }'
```

## Is Grok 4.7 Worth Switching To?

For existing Grok 4.6 users who depend on coding agents or long-running professional workflows, Grok 4.7 is a material upgrade candidate because the launch benchmark set improves across every reported dimension while standard token pricing remains at the same $2/$6 level below the long-context threshold.

For users of other frontier models, the decision is workload-specific. Grok 4.7 is especially interesting when output-token cost, engineering workloads, large contexts, and sustained tool use matter. Where another model is stronger on a critical domain, model routing can be more rational than replacing every model with one provider.

## Conclusion

Grok 4.7 is more than a routine numerical update to Grok 4.6. The release is explicitly oriented toward **long-running work performed through tools, repeated verification, large contexts, and multiple execution steps**.

The strongest generational gains appear where that training direction should matter: Terminal-Bench 4.0 rises from 20.3% to 38.0%, EEBench from 53.0% to 64.0%, and CursorBench 4.0 from 40.4% to 46.3%, while standard pricing below the 200K prompt threshold stays at $2/M input and $6/M output.

The practical value proposition is therefore not “Grok 4.7 wins every benchmark.” It is that Grok 4.7 narrows the gap between frontier-class agent capability and lower-cost inference, making it especially relevant to coding agents, research systems, and professional workflows that need to operate for many steps rather than answer once.

---

*Originally published at [https://www.cometapi.com/what-is-grok-4-7/](https://www.cometapi.com/what-is-grok-4-7/).*
