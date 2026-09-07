# How to Automate Image Generation at Scale with One API

## TL;DR

Use a JSONL queue, a bounded worker pool, model routing, and a manifest. The CometAPI-compatible endpoint in the source article is `POST https://api.cometapi.com/v1/images/generations`; the catalog is checked at runtime so model IDs and pricing are not frozen in code.

## Architecture

```text
jobs.jsonl -> bounded workers -> /v1/images/generations -> local/object storage -> manifest.jsonl
```

Each job has a durable ID. Product jobs route to `gpt-image-2`; ad and content jobs use `doubao-seedream-4-5-251128` in the article's August 20, 2026 catalog snapshot. Treat those mappings as examples and re-check the live catalog.

## Operational Rules

- Start with four workers and tune from latency and 429 evidence.
- Retry only 408, 429, and 5xx responses, with capped exponential backoff and jitter.
- Support both `data[0].b64_json` and `data[0].url` response containers.
- Write the image before marking a manifest row successful; use durable IDs to avoid duplicate work.
- Store provider URLs only temporarily; move accepted assets to object storage.

The article's catalog snapshot lists `gpt-image-2` at $5 input and $30 output per million tokens, and `doubao-seedream-4-5-251128` at $0.04 per request, with a listed 0.8 billing ratio. Rates are time-sensitive; the example records usage and estimates cost from the live catalog.

## Run The Example

See [the runnable example](../examples/image-generation-at-scale/). It uses Python 3.11+, `requests`, JSONL jobs, validation, retry handling, URL/base64 normalization, and a JSONL manifest.

## Sources

- [CometAPI article](https://www.cometapi.com/automate-image-generation-at-scale-one-api/)
- [CometAPI Quick Start](https://apidoc.cometapi.com/doc-873781)
