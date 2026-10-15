<!-- social-ops-fingerprint:baee0d6c1de1ccfb96bc3d6988374518f86042dafe7ef163cb20c834ed165256 -->
---
title: Claude Fable 5.1 Benchmarks: What Scores tell me
---
# Claude Fable 5.1 Benchmarks: What Scores tell me

![Claude Fable 5.1 Benchmarks: What Scores tell me](https://resource.cometapi.com/claude-logo-and-app-780x470.webp)

**TLDR** Claude Fable 5.1 is primarily an agentic-execution upgrade. Its largest reported gains appear in scientific research, business automation, terminal coding, and other workflows that require planning, tool use, verification, and recovery across many steps. Improvements are smaller on closed-ended reasoning and shorter IDE-style coding tasks, so the best deployment decision depends on the workload rather than a single headline score.

## Key Takeaways

- Fable 5.1 scores 52.6% on Terminal-Bench-Science 0.1, more than double Fable 5's 24.7% in Anthropic's evaluation.
- AutomationBench rises from 17.1% to 31.4%, showing a large improvement in end-to-end business workflows.
- Gains are more modest on CursorBench and tool-assisted Humanity's Last Exam, suggesting that the release improves sustained execution more than every form of reasoning equally.
- Fable 5.1 keeps the same standard token prices as Fable 5, while lower cache-read pricing can reduce the effective cost of context-heavy agent workflows.
- GPT-6 Astra is now the more current OpenAI comparison, but it was not included in Anthropic's September 1 benchmark table. Any direct performance claim requires a controlled same-harness evaluation.

Anthropic released Claude Fable 5.1 on September 1, 2026 for demanding reasoning, long-horizon agents, software engineering, research, and professional knowledge work. [Claude Fable 5.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) is also available through CometAPI for developers who want to evaluate it alongside other frontier models through a unified endpoint.

The headline results are strong, but the distribution of improvement is more informative than the average. Fable 5.1 gains most when an agent must preserve a goal, interact with tools, recover from errors, and verify a final state. This article focuses on what the benchmark results mean, where the model still falls short, and how to evaluate it against newer alternatives.

## Claude Fable 5.1 at a Glance

[Anthropic’s model documentation](https://platform.claude.com/docs/en/models/fable-5-1/overview) specifies a 1-million-token context window, 128K maximum output, text and image input, always-on adaptive thinking and a June 2026 knowledge cutoff. The Claude API model ID is `claude-fable-5-1`.

| Official specification | Claude Fable 5.1 |
| --- | --- |
| Provider | Anthropic |
| Release date | September 1, 2026 |
| Model ID | claude-fable-5-1 |
| Context window | 1,000,000 tokens |
| Maximum output | 128,000 tokens |
| Input / output | Text and images → text |
| Thinking | Adaptive, always on |
| Default effort | High |
| Knowledge cutoff | June 2026 |
| Anthropic input price | $10 / MTok |
| Anthropic output price | $50 / MTok |
| Cache read | $0.25 / MTok |
| Comparative latency | Slower |
| Primary positioning | Demanding reasoning and long-horizon agentic work |

Standard input and output prices remain the same as Fable 5, while cache reads fell to $0.25 per million tokens. Fable 5.1 does not have lower headline input/output token prices. Its lower effective cost comes primarily from a 75% reduction in cache-read pricing. Anthropic estimates around 25% lower cost for typical workloads and up to approximately 45% for highly agentic workloads.

That matters because a long-running agent repeatedly reuses repository context, instructions, tool definitions and prior state. Cost per completed task can improve even when headline input and output prices do not change.

> Anthropic also reports 60.9% for Claude Mythos 5.1 on Terminal-Bench 4.0. Mythos 5.1 is a separately deployed version with different safeguards and should not be treated as the generally available Fable 5.1 score.

## What Do Claude Fable 5.1 Benchmarks Show?

The following values come from [Anthropic’s September 2026 evaluation](https://www.anthropic.com/claude-fable-and-mythos-5-1). They describe a model-and-harness configuration, not an immutable property of the model.

| Benchmark | What it measures | Fable 5.1 | Fable 5 | Opus 5 | GPT-5.6 Sol |
| --- | --- | --- | --- | --- | --- |
| Terminal-Bench-Science 0.1 | Agentic scientific research | 52.6% | 24.7% | 29.0% | 22.4% |
| Terminal-Bench 4.0 | Agentic terminal coding | 55.8% | 42.0% | 52.3% | 37.3% |
| GDPval-AA v2 | Professional knowledge work, Elo | 1853 | 1723 | 1824 | 1711 |
| OSWorld 2.0, partial | Long-horizon computer use | 77.9% | 72.9% | 75.4% | — |
| OSWorld 2.0, strict | Fully completed computer tasks | 41.7% | 36.1% | 39.6% | — |
| Humanity’s Last Exam, no tools | Expert multidisciplinary reasoning | 60.9% | 57.8% | 56.6% | — |
| Humanity’s Last Exam, with tools | Expert reasoning with tools | 65.0% | 63.8% | 63.6% | — |
| AutomationBench | End-to-end business workflows | 31.4% | 17.1% | 26.9% | 19.6% |
| CursorBench 3.2.0 | Agentic IDE coding | 73.4% | 70.5% | 70.0% | 67.2% |

Fable 5.1 leads Fable 5 and Opus 5 across all nine reported rows. Its largest generational gains occur in scientific research, business workflow automation, and terminal coding. The smaller differences on Humanity's Last Exam and CursorBench are equally important because they show that the improvement is not uniform across every workload.

## Where Does Claude Fable 5.1 Improve the Most?

### Terminal-Bench-Science 0.1: the standout result

Fable 5.1 scores 52.6%, compared with 24.7% for Claude Fable 5, 29.0% for Claude Opus 5, and 22.4% for GPT-5.6 Sol in Anthropic's run. The large 27.9-point generational gap is much larger than the reported per-model standard error, whereas smaller gaps—such as the 3.5-point Fable 5.1 vs Opus 5 difference on Terminal-Bench 4.0—should be interpreted more cautiously.

Terminal-Bench-Science evaluates complete research workflows across scientific and engineering domains. Agents must produce code, analyses, proofs, simulations, or data products rather than merely answer isolated questions. Anthropic reports a standard error of approximately ±3.5–4.5 points per model, so small gaps should not automatically be interpreted as meaningful capability differences.

### Terminal-Bench 4.0: stronger autonomous coding

Fable 5.1 reaches 55.8%, ahead of Fable 5 at 42.0%, Opus 5 at 52.3%, and GPT-5.6 Sol at 37.3%. The 13.8-point improvement over Fable 5 is substantial, while the 3.5-point lead over Opus 5 is comparatively narrow.

The benchmark places agents in an execution environment, so success depends on navigating the environment, changing code, and validating outcomes. Because Terminal-Bench 4.0 uses a different task set from earlier releases, scores should be compared only within the same benchmark version.

### AutomationBench: a large gain with significant headroom

AutomationBench rises from 17.1% on Fable 5 to 31.4% on Fable 5.1. That is a 14.3-point absolute increase, or approximately an 84% relative gain.

The benchmark evaluates workflows across sales, marketing, operations, support, finance, and HR by checking the final environment state. This makes it a useful test of whether an agent actually completed a workflow rather than simply proposed the correct actions. The score also reveals the remaining limitation: roughly two thirds of tasks were still not completed under Anthropic's reported configuration.

### CursorBench 3.2.0: a smaller coding gain

Fable 5.1 reaches 73.4%, versus 70.5% for Fable 5, 70.0% for Opus 5 and 67.2% for GPT-5.6 Sol. The gain over Fable 5 is only 2.9 points.

The release therefore looks less transformative on shorter IDE-style coding tasks than on longer workflows involving planning, execution, verification and recovery. Evaluation suites should include repository-scale changes and failing-test recovery instead of only code-generation quality.

### OSWorld 2.0: computer use remains difficult

Fable 5.1 scores 77.9% with partial credit and 41.7% under strict completion. Opus 5 reaches 75.4% and 39.6%, while Fable 5 reaches 72.9% and 36.1%.

The strict score is the more revealing production signal. Fewer than half of the tasks were fully completed, demonstrating that progress in computer use does not eliminate the need for checkpoints, permissions, monitoring, and recovery logic.

### CursorBench and Humanity's Last Exam: smaller gains

Fable 5.1 reaches 73.4% on CursorBench 3.2.0, only 2.9 points above Fable 5. On Humanity's Last Exam, it gains 3.1 points without tools and 1.2 points with tools.

These narrower gaps support the central interpretation: Fable 5.1 is more transformative on long workflows involving planning, execution, verification, and recovery than on shorter IDE tasks or closed-ended academic reasoning.

## Claude Fable 5.1 vs Fable 5 vs GPT-6 Astra vs Opus 5

**Short answer:** Fable 5.1 is the strongest option in Anthropic’s published long-horizon benchmark table; Opus 5 is the more economical starting point when its smaller performance gap is acceptable; Fable 5 remains the legacy baseline; GPT-6 Astra requires a same-harness test before any direct ranking.

Fable 5.1 is a clear generational upgrade over Fable 5 on Anthropic’s reported long-horizon agent benchmarks. GPT-6 Astra is the more current OpenAI comparison, but it was released after Anthropic’s September 1 evaluation and was not included in the same benchmark harness.

| Dimension | Claude Fable 5.1 | Claude Fable 5 | GPT-6 Astra |
| --- | --- | --- | --- |
| Context window | 1M tokens | 1M tokens | 1.05M tokens |
| Maximum output | 128K | 128K | 128K |
| Standard input / output | $10 / $50 per MTok | $10 / $50 per MTok | $10 / $50 per MTok |
| Cache read | $0.25 / MTok | $1 / MTok | Verify current provider terms |
| Terminal-Bench-Science 0.1 | 52.6% | 24.7% | Not included in Anthropic’s launch table |
| Terminal-Bench 4.0 | 55.8% | 42.0% | Not included in Anthropic’s launch table |
| AutomationBench | 31.4% | 17.1% | Not included in Anthropic’s launch table |
| Primary positioning | Demanding reasoning and long-horizon agents | Previous Fable-class baseline | Difficult end-to-end professional work |

Against Fable 5, Fable 5.1 shows its largest measured gains in scientific research, business automation, and terminal coding while keeping the same standard token prices. Lower cache-read pricing further improves the economics of repeated-context agents.

**Selection rule:** Start with Opus 5 when cost is the priority, escalate to Fable 5.1 when long-horizon completion and recovery matter most, keep Fable 5 only for compatibility-sensitive workloads, and evaluate GPT-6 Astra in a controlled same-harness test before production adoption.

## What Does Benchmark Performance Look Like by Workload?

| Capability | Fable 5.1 result | Change vs Fable 5 | Interpretation |
| --- | --- | --- | --- |
| Agentic scientific research | 52.6% | +27.9 pts | Very large gain |
| Business workflow automation | 31.4% | +14.3 pts | Very large gain |
| Terminal coding | 55.8% | +13.8 pts | Large gain |
| Computer use, strict | 41.7% | +5.6 pts | Moderate gain |
| Computer use, partial | 77.9% | +5.0 pts | Moderate gain |
| Expert reasoning, no tools | 60.9% | +3.1 pts | Small gain |
| IDE agentic coding | 73.4% | +2.9 pts | Small gain |
| Expert reasoning, tools | 65.0% | +1.2 pts | Small gain |
| Professional knowledge work | 1853 Elo | +130 Elo | Strong, configuration-sensitive |

The pattern is consistent: the biggest improvements appear when success depends on persistence, planning, environment interaction, tool use, and recovery over time.

## What Do the Benchmarks Not Tell You?

Benchmark tables compress behavior into single numbers. They do not prove that autonomous agents are solved, and they do not predict every production workload.

- The main comparison table is vendor-run.
- Effort settings affect quality, latency, and cost.
- Agent benchmarks measure the combined model, harness, tools, and permissions.
- Production safeguards were enabled for Fable 5.1 and affected some outcomes.
- Benchmark versions change, so values from different task releases may not be comparable.
- AutomationBench remains at 31.4%, while OSWorld strict completion remains at 41.7%; substantial failure rates remain.

A practical evaluation should use public scores to shortlist candidates, reproduce a small comparison with identical settings, and then test the actual production workflow.

## Is Claude Fable 5.1 the best Claude model?

For maximum capability on difficult long-running work, the benchmark evidence makes a strong case for [Claude Fable 5.1](https://www.cometapi.com/models/anthropic/claude-fable-5-1/). For every workload, no.

Anthropic prices it at $10 per million input tokens and $50 per million output tokens, versus $5 and $25 for Opus 5. The premium is justified only when Fable 5.1 produces a higher success rate, fewer retries, fewer tokens per accepted task, or enough reduction in human review time.

Lower cache-read pricing can narrow the effective cost gap for agents. Cost per accepted result is therefore more useful than price per token alone.

## How Should You Benchmark Claude Fable 5.1?

Your evaluation should resemble the intended production workload.

- **Coding:** Test complete issues and record patch acceptance, tests passed, retries, tool calls, elapsed time, and human correction time.
- **Research:** Evaluate source quality, factual accuracy, evidence coverage, subtask completion, and goal retention over long runs.
- **Business agents:** Score the final environment state instead of counting individually correct actions.
- **Computer use:** Measure recovery from pop-ups, slow pages, interrupted sessions, and inconsistent application state.
- **Model comparison:** Keep prompts, harnesses, tools, permissions, effort settings, and scoring rules constant.
- **Economics:** Measure cost per accepted task, not only cost per token.

## Conclusion

The benchmark evidence suggests that Fable 5.1 is most valuable when a task requires sustained execution rather than a single response. The strongest use cases include scientific research, autonomous coding, complex business automation, and workflows with repeated verification and recovery.

The evidence does not support universal superiority. Smaller gaps on several benchmarks, meaningful failure rates on strict computer-use tasks, and the absence of GPT-6 Astra from Anthropic's launch table all reinforce the need for workload-specific testing.

For CometAPI users, a practical deployment rule is to test Fable 5.1 where long-horizon success could justify premium inference, then compare it with Opus 5, GPT-5.6 Sol, and GPT-6 Astra on the same representative tasks before choosing a production route.

## FAQs

### What is Claude Fable 5.1’s highest benchmark score?

Among Anthropic’s reported percentage metrics, Fable 5.1 reaches 77.9% partial credit on OSWorld 2.0 and 73.4% on CursorBench 3.2.0. Its largest generational improvement is Terminal-Bench-Science, at 52.6% versus 24.7% for Fable 5.

### How much better is Claude Fable 5.1 than Fable 5?

The gain varies sharply by workload: 27.9 points on Terminal-Bench-Science, 14.3 on AutomationBench and 13.8 on Terminal-Bench 4.0, but only 2.9 on CursorBench and 1.2 on tool-assisted Humanity’s Last Exam.

### Is Claude Fable 5.1 better than Claude Opus 5?

It scores higher across Anthropic’s reported table, but many gaps are small. Anthropic recommends starting with Opus 5 and escalating when additional long-horizon capability is required.

### Does Claude Fable 5.1 beat GPT-5.6 Sol?

Anthropic reports higher Fable 5.1 scores on five shared metrics. Because these are vendor-run competitor evaluations and configurations vary, the safe conclusion is that Fable 5.1 is highly competitive rather than universally superior.

### Are the results independently verified?

Only partially. Several benchmarks have public leaderboards, but effort, harness, fallback behavior and task versions must be aligned before their values can be compared directly with Anthropic’s launch run.

### What is Claude Fable 5.1 best for?

Its benchmark profile is strongest for long-running scientific research, autonomous coding, complex agent workflows, business automation and tasks that require planning, tools, verification and recovery.

### How can I access Claude Fable 5.1?

[Claude Fable 5.1 is listed on CometAPI](https://www.cometapi.com/models/anthropic/claude-fable-5-1/) with model ID `claude-fable-5-1`. A unified endpoint makes it practical to run the same evaluation workload across several models before choosing a production route.

---

*Originally published at [https://www.cometapi.com/claude-fable-5-1-benchmarks/](https://www.cometapi.com/claude-fable-5-1-benchmarks/).*
