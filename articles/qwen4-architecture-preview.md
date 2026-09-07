# Qwen4 Architecture Preview: What Qwen3.8-Flash-Next Tells Us

Qwen3.8-Flash-Next is **not Qwen4**. Qwen describes it as an experimental architecture preview for the future Qwen4 foundation; the final product lineup, API IDs, pricing, license, scorecard, and release date remain undisclosed.

## Evidence Levels

| Level | Meaning |
| --- | --- |
| Confirmed | Official Qwen material or the preview itself |
| Expected | A stated inference from confirmed design signals |
| Unknown | No disclosed final value |

## Confirmed Preview Architecture

| Signal | Qwen3.8-Flash-Next |
| --- | --- |
| Main / active parameters | 125B / 6B per token |
| Additional embeddings / MTP | 51B n-gram embeddings / 4B MTP |
| Layers / experts | 48 / 512; 10 routed plus one shared expert active |
| Context | 262,144 native; extension to 1,000,000 |
| Attention | Three Gated DeltaNet layers per Qwen Sparse Attention layer |
| Modality | Causal language model with vision encoder |

The design is an ultra-sparse MoE: it aims to preserve broad parameter capacity while limiting active compute. The hybrid attention design suggests attention and KV-cache efficiency are important for long-horizon workloads. These are architecture signals, not final Qwen4 specifications.

## Vendor-Reported Benchmarks

| Benchmark | Flash-Next | Qwen3.8-27B |
| --- | ---: | ---: |
| DeepSWE 1.1 | 58.7 | 42.2 |
| SWE-bench Pro | 62.5 | 61.7 |
| CoWorkBench | 73.9 | 70.7 |
| Toolathlon Verified | 73.5 | 67.1 |
| ClawEval-MM (Pass@3) | 64.4 | 57.4 |
| AndroidWorld | 84.5 | 81.9 |

These are preview-model results, not Qwen4 results.

## What It Suggests, And What It Does Not

Expected: Qwen4 may emphasize sparse activation, hybrid long-context attention, and native vision. Unknown: final parameter counts, product tiers, context policy, model IDs, pricing, license, release date, and final benchmark performance.

## Sources

- [CometAPI article](https://www.cometapi.com/qwen4-is-coming-soon-what-qwen3-8-flash-next-reveals/)
- [Qwen](https://qwen.ai/)
