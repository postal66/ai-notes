# DeepSeek V5: What We Know, What Is Rumored, and What to Watch

> Status: Unreleased / not officially documented as of September 7, 2026.

## TL;DR

There is no official V5 model card, API model ID, price, weights release, benchmark card, or release date. The current CometAPI article describes V5 through community reports, not primary DeepSeek documentation. Treat every capability and date claim below as reported until DeepSeek publishes artifacts.

## Confirmed Vs Reported

| Claim | Status | Evidence |
| --- | --- | --- |
| V5 is officially released | Unknown | No official announcement cited |
| New foundation / architecture | Reported | Community leaks and secondary coverage |
| Stronger coding and agents | Reported | Community leaks |
| GPT-6 Astra-level performance | Reported | Repeated social-media claim; no verified benchmark |
| Mid-September 2026 timing | Reported | Posts from Sep 6 saying "next week" |
| Official pricing | Unknown | No V5 pricing published |

## Current Baseline

The source article identifies V4-Pro and V4-Flash as current production models, with V4-Flash-Vision-Exp as an experimental multimodal variant. It reports MIT open weights and 1M context for the V4 line. The cited approximate off-peak official prices are $0.22/$0.66 per MTok input/output for V4-Flash and $0.66/$1.98 for V4-Pro; confirm directly with DeepSeek before billing decisions.

## What To Test At Launch

Do not infer a benchmark table from rumors. Evaluate real repositories and tool workflows using: task success rate, accepted completion rate, retries, tool failures, latency, input/output/cache tokens, total cost, and cost per completed task. Include failure recovery and long-context behavior, not only code completion.

## Migration Notes

Keep model IDs and base URLs configurable. A model-swappable, OpenAI-compatible client lets a V5 evaluation run alongside V4 without changing queueing, observability, or acceptance criteria.

## Sources

- [CometAPI article](https://www.cometapi.com/deepseek-v5/)
- [DeepSeek](https://www.deepseek.com/)
