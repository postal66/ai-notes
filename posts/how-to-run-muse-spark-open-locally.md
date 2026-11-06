<!-- social-ops-fingerprint:75d0824ad16889b51963032b1947403399bdc17fa52b5227b3ba1be237cbe327 -->
---
title: How to Run Muse Spark Open Locally
---
# How to Run Muse Spark Open Locally

![How to Run Muse Spark Open Locally](https://resource.cometapi.com/Muse%20Spark%20open.webp)

## TL;DR

Running Muse Spark Open locally is possible, but it is a large-scale deployment rather than a typical single-GPU setup. Meta’s documented configurations include four NVIDIA B300 GPUs for NVFP4, eight B300 GPUs for BF16, or a distributed MLX setup using multiple M5 Ultra Mac Studios.

For most developers, the first step is to match the checkpoint to a supported hardware and inference-runtime combination. Start with a conservative context length, verify that the server returns complete responses, and measure memory usage before increasing context or concurrency. If you do not have access to suitable hardware, a hosted inference API may be the more practical option such as CometAPI's [Muse Spark](https://www.cometapi.com/models/meta/muse-wonder/) .

## Key Takeaways

- Muse Spark Open has 816B total parameters and about 42B active per token; the full expert bank still needs storage and memory.
- Choose NVFP4 or BF16 using checkpoint size, accelerator memory, interconnect, and serving overhead.

---

*Originally published at [https://www.cometapi.com/how-to-run-muse-spark-open-locally/](https://www.cometapi.com/how-to-run-muse-spark-open-locally/).*
