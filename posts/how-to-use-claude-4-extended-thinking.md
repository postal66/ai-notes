<!-- social-ops-fingerprint:b67166b752132631e6bae481cc52daf9512dfff4be8cf0ce0b47855aa9f8fbf7 -->
---
title: How to Use Claude 4 extended thinking?
---
# How to Use Claude 4 extended thinking?

![How to Use Claude 4 extended thinking?](https://resource.cometapi.com/blog/uploads/2025/06/claude-4.webp)

Claude 4, Anthropic’s latest family of large language models—including Claude Opus 4 and Claude Sonnet 4—introduces a powerful new “extended thinking” capability that unlocks deeper, step-by-step reasoning for tackling complex, long‑running tasks and agentic workflows. As organizations race to integrate AI into development pipelines, research projects, and business processes, mastering Claude 4’s extended thinking unlocks its full potential for advanced problem‑solving, content generation, and autonomous orchestration. This article synthesizes the latest announcements, API documentation, and hands‑on guidance to explain how to enable, configure, and maximize Claude 4 extended thinking in your workflows.

## What is Claude 4 extended thinking

Extended thinking is a feature of both Claude Opus 4 and Claude Sonnet 4 that enables the model to expose its internal reasoning process in “thinking” content blocks. This transparency allows developers and end‑users to see how Claude arrives at its conclusions, improving trust and debuggability in complex tasks . Unlike standard mode—which optimizes for brevity and speed—extended thinking allocates more compute and context to produce deeper, multi‑step reasoning workflows, crucial for high‑stakes or intricate problem domains.

### Core Concepts

- **Thinking Blocks**: Structured segments where Claude 4 articulates its chain of thought before delivering final answers .
- **Summarized Thinking**: A condensed version of the full thought stream, balancing transparency with safety by omitting overly sensitive or proprietary logic .
- **Interleaved Tool Use** (beta): Enables seamless mixing of external tool calls (e.g., search or databases) with reasoning, further enriching responses.

### How It Differs from Standard Mode

- **Response Pattern**: Extended thinking may stream in “chunky” segments with deliberate pauses, reflecting the model’s deeper inference steps .
- **Latency Trade‑off**: Prioritizes reasoning quality over raw speed; expect slight increases in response time when compared to instant‑mode replies.

### Who Has Access to Extended Thinking?

- **Free Users**: Can access Extended Thinking with Sonnet 4 through both API and web applications;
- **Pro/Team/Enterprise**: Get access to the full Opus 4 functionality, including larger token budgets;
- **Cloud Integrations**: Amazon Bedrock and Google Cloud Vertex AI also fully support Claude 4 Extended Thinking, ensuring seamless enterprise-level workload integration.  .

## How Can You Enable Extended Thinking in Claude 4?

Activating extended thinking depends on your access channel—Anthropic API, Amazon Bedrock, or Google Cloud Vertex AI—and your subscription tier.

### API Configuration

1. **Messages API Header**: Include the parameter `extended_thinking: true` in your JSON payload when calling the Claude Opus 4 or Sonnet 4 endpoint.
2. **Beta Mode for Interleaving**: To mix tool use and reasoning, add the beta header `interleaved-thinking-2025-05-14` alongside `extended_thinking` .

```
{
  "model": "claude-opus-4",
  "max_tokens": 200000,
  "extended_thinking": true,
  "stream": false,
  "headers": {
    "Anthropic-Client": "your_api_key",
    "interleaved-thinking-2025-05-14": "true"
  }
  "messages": [
    { "role": "user", "content": "Please analyze the properties of quadratic functions in detail." }
  ]
}
```

- `budget_tokens` defines the available tokens for internal thinking;
- `max_tokens` is the total limit for both thinking and final answer tokens;
- To use real-time streaming thinking, set `stream` to `true`.  .

### How to Configure Token Budgets and Stream Settings?

- **Token Budget**: It’s recommended to set `budget_tokens` to 40%-60% of `max_tokens` to ensure sufficient reasoning while leaving space for a complete final answer;
- **Streaming Mode**: After enabling SSE (Server-Sent Events), the client can capture `thinking_delta` and `text_delta` events, dynamically rendering reasoning and final answers for a smoother user interaction experience;
- **Cost Considerations**: Extended Thinking generates additional thinking token costs, and some platforms (like Amazon Bedrock) charge based on the total number of thinking tokens, so it’s important to assess the budget in advance.  .

### Platform Access

- **Anthropic Playground**: Toggle the “Extended Thinking” switch in the UI when launching an Opus 4 or Sonnet 4 session .
- **AWS Bedrock**: In the Bedrock console, select “Claude Opus 4” or “Claude Sonnet 4” and enable the extended thinking option under model settings.
- **Google Cloud Vertex AI**: Choose the Claude 4 model and check “Enable Extended Reasoning” in the deployment configuration.

## What Benefits Does Extended Thinking Offer?

Extended thinking unlocks new dimensions of AI collaboration, especially for tasks demanding multi‑step logic, transparency, and integration with external data sources.

### Improved Reasoning Depth

By allocating additional compute and context windows—up to thousands of tokens—extended thinking can tackle problems such as complex code refactoring, strategic planning, and legal analysis more reliably .

### Transparent Reasoning Summaries

The “thinking summary” output provides end‑users and developers with a compressed audit trail of Claude’s decision‑making, facilitating debugging, compliance reviews, and knowledge transfer .

### Enhanced Tool Use

When interleaved tool use is enabled, Claude 4 can call web search, databases, or internal APIs mid‑stream, weaving real‑time data into its thought process and final responses .

## How to Interpret and Process Extended Thinking Responses?

### What Is Summarized Thinking vs Full Trace?

By default, Claude 4 outputs a **Summarized Thinking** form of reasoning block summaries, while the complete reasoning is encrypted and included in the signature field, balancing interpretability with reduced risk of misuse. To access the full reasoning logs for debugging or auditing purposes, contact Anthropic to apply for full trace access.  .

### How to Handle Streaming (SSE) Events?

In streaming mode, you will receive various SSE events:

- `thinking_delta`: Incremental reasoning content;
- `text_delta`: Incremental answer fragments;
- `content_block_start`/`end`: Mark the start and end of reasoning and answer blocks.
  The client can switch between visual states: first rendering the reasoning in real time, then switching to the final answer once reasoning is complete.  .

## How Does Extended Thinking Impact Performance?

While the quality of reasoning improves, response times and token usage will increase. Understanding this trade‑off helps you balance cost, latency, and depth.

- **Latency Increase**: Extended thinking can add 500 ms to several seconds per request, depending on query complexity.
- **Token Consumption**: Expect 20–50 % more tokens for “thinking” blocks; plan your budget accordingly, as Opus 4 costs $75 per million output tokens and $15 per million input tokens .
- **Cost‑Benefit Analysis**: Use extended thinking selectively—reserve it for high‑stakes queries or debugging sessions, and default back to instant mode for routine tasks.

## What Are Best Practices for Harnessing Extended Thinking?

Adopting extended thinking effectively requires thoughtful prompting, context management, and result interpretation.

### Prompt Engineering

- **Explicit Instruction**: Begin with “Please use extended thinking to…” to signal the model .
- **Incremental Complexity**: Start with smaller subtasks (e.g., “Outline the steps to refactor this code”), then build up to larger workflows .

### Context Window Optimization

- **Chunking**: Break large inputs into logical sections so Claude 4 can apply extended reasoning to each block without hitting context limits .
- **Memory Files** (Opus 4 only): Use long‑term memory files for recurring context, reducing repeated reasoning overhead .

### Interpretation and Validation

- **Review Thinking Blocks**: Examine the chain‑of‑thought for gaps or logical leaps before accepting outputs as final .
- **Automated Checks**: Combine with unit tests or rule‑based validations to ensure correctness when extended reasoning suggests code changes or data analyses.

## What Are Common Challenges and How Can You Troubleshoot Them?

Despite its power, extended thinking may introduce complexities you’ll need to manage.

### Excessive Latency

**Solution**: Limit thinking mode to critical segments; use shorter context windows for preliminary exploration.

### Token Overrun

**Solution**: Monitor token usage in API logs; employ summarization prompts to compress thinking blocks when verbosity spikes.

### Incomplete or Confusing Chains of Thought

**Solution**: Refine prompts to guide structure (e.g., “Step 1: Identify assumptions; Step 2: Evaluate alternatives”), and use summarized thinking to cross‑check.

## Getting Started

CometAPI provides a unified REST interface that aggregates hundreds of AI models—including Claude family—under a consistent endpoint, with built-in API-key management, usage quotas, and billing dashboards. Instead of juggling multiple vendor URLs and credentials.

Developers can access [Claude Sonnet 4 API](https://www.cometapi.com/claude-sonnet-4-api/)  (model: `claude-sonnet-4-20250514` ; `claude-sonnet-4-20250514-thinking`) and [Claude Opus 4 API](https://www.cometapi.com/claude-opus-4-api/) (model: `claude-opus-4-20250514`; `claude-opus-4-20250514-thinking`)etc through [CometAPI](https://www.cometapi.com/).  . To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. CometAPI’ve also added `cometapi-sonnet-4-20250514`and`cometapi-sonnet-4-20250514-thinking` specifically for use in Cursor.

*New to CometAPI?* [Quick Start](https://www.cometapi.com/console/login) and unleash Sonnet 4 on your toughest tasks.

We can’t wait to see what you build. If something feels off, hit the feedback button—telling us what broke is the fastest way to make it better.

## Conclusion

Through this comprehensive guide to Extended Thinking, you should now have a clear understanding of how to enable, configure, and optimize the feature for your projects. With the ongoing iteration of the Claude 4 family, Extended Thinking will play an increasingly pivotal role in explainable AI, automated agents, and solving complex tasks. Moving forward, we look forward to seeing how you integrate it into more industry scenarios, opening a new chapter in AI collaboration.

---

*Originally published at [https://www.cometapi.com/how-to-use-claude-4-extended-thinking/](https://www.cometapi.com/how-to-use-claude-4-extended-thinking/).*
