# CometAPI AI Developer Notes

A developer-focused collection of model comparisons, architecture notes, API experiments, and production AI engineering guides.

## Model Guides

Specs, benchmarks, and pricing for individual models.

| Article | What it covers |
| --- | --- |
| [What Is Claude Fable 5.1?](posts/claude-fable-5-1-guide.md) | Features, benchmarks, 1M-token context, pricing, and access paths. |
| [GPT-5.6 API: Sol vs Terra vs Luna](posts/gpt-5-6-api-pricing-sol-vs-terra-vs-luna-benchmarks-and-access.md) | Tier pricing, benchmark deltas, and which variant fits which workload. |
| [MiniMax M3 Is Live](posts/minimax-m3.md) | 1M context, 428B MoE, and what the vendor benchmarks actually show. |
| [What Is Qwen3.8-Flash?](posts/qwen3-8-flash-guide.md) | Specs, 6B-active MoE architecture, coding benchmarks, and price-performance. |
| [What Is Gemini 3.8 Flash?](posts/gemini-3-8-flash-guide.md) | Specs, benchmarks, pricing, and what changed from the previous Flash. |
| [Seedream 5.0 Pro](posts/seedream-5-0-pro.md) | 2K output, multi-reference image inputs, and the arena snapshot in context. |
| [Seedance 2.5](posts/seedance-2-5-whats-new-pricing-and-api-access.md) | Audio-video generation for longer, reference-controlled clips. |

## Comparisons and Roundups

Side-by-side evaluations and monthly launch tracking.

| Article | What it covers |
| --- | --- |
| [Best Multi-LLM Gateways in 2026](posts/best-multi-llm-gateways-in-2026.md) | What a production gateway needs beyond forwarding one prompt to another model. |
| [Best Open-Weight and Chinese LLMs for Coding and Reasoning](posts/best-open-weight-and-chinese-llms-for-coding-and-reasoning.md) | Comparing DeepSeek V4, Kimi K3, Qwen3.8-Max, and GLM 5.3 under one API. |
| [Wan 2.7 vs Vidu Q3](posts/wan-2-7-vs-vidu-q3.md) | Pricing, video quality, audio support, and API trade-offs. |
| [August 2026 AI Model Launch Radar](posts/august-2026-ai-model-launch-radar-whats-new-on-cometapi.md) | The month's model releases, with stable catalog IDs under one billing workflow. |

## Release Status Trackers

Evidence-labeled notes separating confirmed releases from reports and rumours.

| Article | What it covers |
| --- | --- |
| [Claude Opus 6 Release Date](posts/claude-opus-6-release-date.md) | What is confirmed against the Opus 5 baseline, and how to prepare. |
| [Gemini 4 Is Reportedly in Training](posts/gemini-4-reportedly-in-training.md) | No model card, API ID, or pricing exists yet. What is reported vs unknown. |
| [DeepSeek V4.1 Status Guide](posts/deepseek-v4-status-guide.md) | Confirmed V4 releases separated from reported features and open questions. |
| [Seedance 3 Status](posts/seedance-3-status-guide.md) | No official announcement as of September 2026. Availability and how to prepare. |

## Long-Form Notes

| Article | What it covers |
| --- | --- |
| [GPT-6 Astra vs Claude Fable 5.1](articles/gpt-6-astra-vs-claude-fable-5-1.md) | Benchmarks, API economics, and workload choices. |
| [DeepSeek V5](articles/deepseek-v5-what-we-know.md) | Confirmed status, reports, and an evaluation plan. |
| [Image Generation at Scale](articles/automate-image-generation-at-scale.md) | A queue-based image pipeline with an executable Python example. |
| [Qwen4 Architecture Preview](articles/qwen4-architecture-preview.md) | What Qwen3.8-Flash-Next confirms, suggests, and leaves unknown. |

## Code Examples

- [Batch Image Generation at Scale](examples/image-generation-at-scale/)

## Focus

- Frontier-model evaluation and API economics
- Multi-model routing through a single API key
- Production pipelines for text, image, and video generation
