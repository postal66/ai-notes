<!-- social-ops-fingerprint:4b86b453abd9967279c1b8df9ba8ab06b97d3ac0f080e3d3a8d8612cedf06205 -->
---
title: OpenAI Launches Deep Research API and Adds Web Search to o3, o3-Pro, and o4-Mini Models
---
# OpenAI Launches Deep Research API and Adds Web Search to o3, o3-Pro, and o4-Mini Models

![OpenAI Launches Deep Research API and Adds Web Search to o3, o3-Pro, and o4-Mini Models](https://resource.cometapi.com/blog/uploads/2025/03/OpenAI-002.webp)

On June 27, 2025, OpenAI officially opened API access to its Deep Research capabilities—empowering developers to automate complex, multi-step research workflows programmatically. Dubbed the **Deep Research API**, this new service exposes two purpose-built models—`o3-deep-research-2025-06-26` for in-depth synthesis and “higher-quality” output, and the lighter, lower-latency `o4-mini-deep-research-2025-06-26`—via the standard Chat Completions endpoint. These models build on the reasoning engines first introduced in ChatGPT’s Deep Research agent earlier this year, but now grant developers full control over prompt design, tool configuration, and asynchronous execution via background mode.

Beyond opening up these specialized Deep Research flavors of o3 and o4-mini, OpenAI also enhanced its mainstream reasoning models—**o3**, **o3-pro**, and **o4-mini**—with built-in web search capabilities. This integration allows the models to conduct live searches, retrieve up-to-the-minute information, and synthesize findings directly in a single call. Pricing for the new “reasoning web search” service starts at **$10 per 1,000 calls**, reflecting the premium compute and API orchestration required; simultaneously, OpenAI slashed the cost of web search on its flagship multimodal models (GPT-4o and GPT-4.1) to **$25 per 1,000 calls** .

![OpenAI Launches Deep Research API and Adds Web Search to o3, o3-Pro, and o4-Mini Models](https://resource.cometapi.com/blog/uploads/2025/06/o4-mini-deep-reserch-1024x962.webp)
![OpenAI Launches Deep Research API and Adds Web Search to o3, o3-Pro, and o4-Mini Models](https://resource.cometapi.com/blog/uploads/2025/06/o3-deep-1024x957.webp)

To streamline long-running research tasks, the API now supports **webhooks**: developers can register callback endpoints to receive automated notifications when a Deep Research job completes, eliminating the need for polling or manual status checks. This webhook mechanism is especially recommended for workflows that run asynchronously—such as multi-hour market analyses or policy reviews—ensuring reliability and efficient resource usage in production systems .

Accessing the Deep Research API is straightforward. After installing the latest OpenAI SDK and authenticating with your API key, developers simply specify one of the two new Deep Research model names in their Chat Completions request. By enabling **tools** like `web_search_preview` and `code_interpreter` and setting the `background` flag to true, the model autonomously decomposes high-level queries into sub-questions, issues searches, executes analyses, and returns a structured, citation-rich report—complete with inline metadata and source URLs .

This launch represents a significant evolution in OpenAI’s product roadmap. Earlier this year, in February 2025, the Deep Research agent debuted within ChatGPT as a “next-generation” capability—powered by an optimized variant of o3—for tasks that would once consume human analysts dozens of hours. It combined browsing, Python tool use, and iterative reasoning to produce thorough, verifiable outputs in under half an hour . With the API release, enterprises and startups alike can embed that analytic power into their own applications, driving use cases from competitive intelligence and literature reviews to technical due diligence and beyond.

Moreover, the broader rollout of web search in o3, o3-pro and o4-mini models blurs the line between static knowledge and real-time information retrieval. Developers can now craft prompts that instruct the model to “find the latest quarterly earnings announcement” or “summarize current regulatory developments in EU data privacy,” and the model will autonomously fetch, interpret, and cite relevant sources—all within a single API transaction. This unified approach contrasts with prior patterns where separate search-then-summarize pipelines were required, reducing integration complexity and latency.

From a business perspective, the pricing adjustments accompanying these features reflect OpenAI’s push to democratize advanced reasoning while managing infrastructure costs. The $10/1K-call rate for reasoning web search positions the service competitively against specialized data-pipeline providers, while the reduced $25/1K rate for GPT-4o/4.1 web search underscores OpenAI’s commitment to making dynamic, tool-enabled AI affordable at scale.

Looking ahead, OpenAI has signaled ongoing investment in the Deep Research ecosystem: model updates, expanded tool support (including direct database connectors and private document integrations via MCP), and deeper multi-modal analysis features are on the roadmap. As these capabilities mature, the boundary between AI as a conversational partner and AI as an autonomous research assistant will continue to dissolve—heralding a new era of agentic applications that can investigate, reason, and deliver actionable insights with minimal human intervention.

## Getting Started

CometAPI provides a unified REST interface that aggregates hundreds of AI models—under a consistent endpoint, with built-in API-key management, usage quotas, and billing dashboards. Instead of juggling multiple vendor URLs and credentials.

Developers can access [o3-Pro API](https://www.cometapi.com/o3-pro-api/)(model: `o3-pro; o3-pro-2025-06-10`), [O3 API](https://www.cometapi.com/o3-api/) (model:`o3;o3-2025-04-16` )and [O4-Mini API](https://www.cometapi.com/o4-mini-api-cometapi/)(model: `o4-mini`;`o4-mini-2025-04-16`) through [CometAPI](https://www.cometapi.com/), the latest models listed are as of the article’s publication date. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

The latest integration o3-deep-research(model:
o3-deep-research-2025-06-26) and o4-mini-deep-research (model: `o4-mini-deep-research-2025-06-26`) will soon appear on CometAPI, so stay tuned！While we finalize Gemini 2.5 Flash‑Lite Model upload, explore our other models on the Models page or try them in the AI Playground.

---

*Originally published at [https://www.cometapi.com/openai-launches-deep-research-api-add-web-search/](https://www.cometapi.com/openai-launches-deep-research-api-add-web-search/).*
