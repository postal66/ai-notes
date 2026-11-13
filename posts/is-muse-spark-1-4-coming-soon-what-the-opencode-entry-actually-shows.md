<!-- social-ops-fingerprint:5821c8493991f70517d86c43c1852fa66f92d8389c11386fdcf92e3a91bf572b -->
---
title: Is Muse Spark 1.4 Coming Soon? What the OpenCode Entry Actually Shows
---
# Is Muse Spark 1.4 Coming Soon? What the OpenCode Entry Actually Shows

![Is Muse Spark 1.4 Coming Soon? What the OpenCode Entry Actually Shows](https://resource.cometapi.com/console/blog-banner/2026/11/dfd9a8ff55bc4232a4b6c18cdfb51a05.png)

## TL;DR

As of November 10, 2026, OpenCode Data has a page for `muse-spark-1.4-contributor` under Meta. It reports two completed sessions but zero tokens and zero unique users, while Meta’s official API documentation still lists Spark 1.3 as the latest version. The listing is a clue worth monitoring, but it does not establish public access, specifications, pricing, or a release date.

## Key Takeaways

* Muse Spark 1.4 has a third-party usage-dashboard entry, but the entry does not establish a working public API.
* Muse Spark 1.3 remains the documented baseline for context, multimodal input, pricing, and performance comparisons.
* The Contributor suffix points to a possible data-use and pricing distinction; it does not establish the terms of an unannounced model.
* Treat any future Muse Spark 1.4 release as a new integration to validate: confirm the model ID, access route, data terms, and task-level results before migrating.

## What Does the Muse Spark 1.4 Entry Actually Reveal?

[OpenCode has a dedicated page](https://opencode.ai/data/meta/muse-spark-1-4-contributor) for `muse-spark-1.4-contributor`, categorized under Meta. The page displays the following information:

| Field                                              | Observed information       |
| -------------------------------------------------- | -------------------------- |
| Model identifier                                   | muse-spark-1.4-contributor |
| Provider label                                     | Meta                       |
| Context length, output limit, inputs, release date | Unknown                    |
| Token usage                                        | 0                          |
| Unique users                                       | 0                          |
| Completed sessions                                 | 2                          |
| Token share                                        | 0%                         |

The dashboard reports two completed sessions but zero tokens and users, without explaining how those sessions were counted. These figures do not establish successful public inference.

### What Does Meta Officially Document?

[Meta’s Spark documentation](https://dev.meta.ai/docs/muse-spark) lists `muse-spark-1.3`, `muse-spark-1.2`, and `muse-spark-1.1`, with Contributor variants for 1.3 and 1.2. It describes Spark 1.3 as the latest version and recommends it for new work. Neither `muse-spark-1.4` nor `muse-spark-1.4-contributor` appears in that list.

## When Could Muse Spark 1.4 Be Released?

There is currently no official release date for Muse Spark 1.4.

Earlier versions provide historical context, not a release forecast. Meta’s [official announcement timeline](https://research.meta.ai/) records Spark 1.1 on July 9, Spark 1.2 on August 5, and Spark 1.3 on September 2, 2026. Two roughly four-week intervals are too little evidence to establish a continuing schedule.

Meta is also expanding beyond numbered Spark updates, including an [open-weight release](https://research.meta.ai/blog/muse-spark-open). That broader roadmap does not establish when 1.4 will arrive.

## What Could Contributor Mode Mean for Muse Spark 1.4?

Meta offers Spark 1.3 in Standard and [Contributor modes](https://dev.meta.ai/docs/pricing-rate-limits). Contributor lowers token prices in exchange for permission to use submitted content and model responses to train future Meta models. Standard content is not used for training.

| Muse Spark 1.3 pricing per 1M tokens | Standard | Contributor |
| ------------------------------------ | -------- | ----------- |
| Input                                | $1.25    | $0.10       |
| Cached input                         | $0.15    | $0.002      |
| Output                               | $4.25    | $0.20       |

Spark 1.3 Contributor does not support `max` reasoning effort. The same suffix in the OpenCode listing suggests a possible Contributor variant, but Meta has not published Spark 1.4 pricing, supported settings, or data-use terms.

## What Could Improve in Muse Spark 1.4?

Meta has not published Spark 1.4 specifications. Spark 1.3’s documented capabilities and limitations suggest three areas where a successor could deliver practical improvements.

### More Reliable Long-Horizon Agentic Workflows

Meta describes [Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3) as better at sustaining long tasks, preserving detailed requirements, and correcting gaps in its plans. A useful next step would be more consistent execution across workflows that combine repository inspection, code changes, testing, and browser operations.

For Spark 1.4, the improvements worth watching would be fewer lost constraints, better recovery from failed tool calls, and less need for users to restate instructions. Higher completion rates on the same multi-step tasks would provide a clear measure of progress.

### Better Coding Efficiency Without Sacrificing Quality

Meta engineers reported that Spark 1.3 used approximately 20% fewer tool calls and 25% fewer tokens than Spark 1.2. A successor could build on this by reducing redundant file edits, unnecessary tool calls, and repeated attempts to fix the same error.

The practical benefit would be faster completion and lower cost per successful task. Evaluations should include failed runs and manual corrections, since lower token usage is valuable only when the model still completes the work correctly.

### More Complete Multimodal Support

Spark 1.3 accepts text, images, video, audio, and PDFs, but Meta notes that its audio understanding is not fully supported and that audio requests may produce degraded responses.

More reliable audio understanding would therefore be a concrete improvement to test in Spark 1.4. Workflows combining meeting recordings, screenshots, and documents would help show whether a successor can connect information across formats and preserve relevant details.

## What Can You Use While You Wait?

The available Muse models address different needs: Spark 1.3 for coding and tool-based workflows, Wonder for demanding engineering tasks, and Spark Open for teams that want control over deployment.

### Muse Spark 1.3: The Closest Available Baseline

Spark 1.3 is Meta’s latest documented Spark version and the most direct starting point for developers interested in a future 1.4 upgrade. It supports coding assistants, multi-step tool use, and long-context workflows.

For cost-sensitive experiments, its Contributor variant offers lower token prices under the data-use terms described above, though it does not support `max` reasoning effort.

### Muse Wonder: For Complex Engineering Tasks

Muse Wonder is positioned for complex software engineering and longer agent runs. Consider it when your current model needs repeated corrections or struggles to complete difficult tasks.

Developers can explore the [Muse Wonder API on CometAPI](https://www.cometapi.com/models/meta/muse-wonder/) and check the listing for supported settings and current pricing.

### Muse Spark Open: For Control Over Deployment

Muse Spark Open is worth evaluating when access to model weights or self-hosting is a project requirement. The choice depends on its license, hardware requirements, and performance on your workload.

Its deployment model differs from API-hosted Spark, so assess the infrastructure and operating costs alongside model quality.

## How Should Developers Prepare for Muse Spark 1.4?

Developers who already use Muse Spark do not need to change their integrations based on the current rumor.

Instead, they can prepare a simple evaluation process for when a confirmed model becomes available.

### Keep Muse Spark 1.3 as the Baseline

Record the performance of your existing model on representative tasks:

* Repository-level code debugging.
* Multi-file software modifications.
* Long-context document retrieval.
* Browser-based automation.
* Multimodal document and video analysis.

These tasks provide a practical baseline for evaluating a future update.

### Evaluate More Than Benchmark Scores

When a verified candidate becomes accessible, run the same task set with fixed prompts, tool permissions, and success criteria. Record completion rate, total tokens, tool calls, retries, elapsed time, and cost per successful task. Keep failures in the results rather than comparing only successful runs.

For coding agents, successful completion with fewer corrections is often more useful than a marginal improvement in a standalone benchmark.

### Check Contributor-Mode Data Policies

If the future model uses a Contributor variant, developers should review its data-use terms before submitting proprietary source code, internal documents, or customer information.

A future 1.4 release should be evaluated using its own official documentation rather than assuming that existing terms automatically carry over.

## FAQ

### Would a Muse Spark 1.4 request error prove the model does not exist?

No. A failed request can reflect an unsupported identifier, missing access, an unavailable route, or a configuration problem. Check the provider’s documented model list and the exact error response. Avoid repeatedly sending production data to a guessed model ID to test a rumor.

### How should a team pilot Muse Spark 1.4 without disrupting production?

Once access is officially documented, isolate the candidate behind a configurable model setting and start with non-sensitive evaluation traffic. Define acceptable quality, latency, and cost thresholds before the trial. Keep the existing model available for rollback, and expand traffic only after the candidate meets those thresholds.

### Can Muse Spark 1.4 be compared fairly across different API providers?

Only after confirming that each route serves the same model variant and supports the settings used in the test. Record provider, model ID, reasoning effort, tool schema, timeout, and retry policy. Measure end-to-end latency and billed usage separately, because gateway behavior and billing can differ even when the model name appears identical.

## Conclusion

Set a concrete threshold for revisiting your model choice: a documented endpoint, acceptable data terms, and a measurable improvement on your own tasks. Until that threshold is met, spend the time on a repeatable evaluation set and a reversible integration. That preparation will remain useful whether Meta eventually ships Spark 1.4, renames the successor, or offers a better fit elsewhere in the Muse family.

---

*Originally published at [https://www.cometapi.com/muse-spark-1-4-coming-soon/](https://www.cometapi.com/muse-spark-1-4-coming-soon/).*
