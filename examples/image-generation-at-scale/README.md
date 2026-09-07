# Batch Image Generation at Scale with CometAPI

## Features

- JSONL input and stable job IDs
- Model routing and live catalog validation
- Bounded concurrency and retryable HTTP handling
- URL or base64 output normalization
- Per-job success/failure manifest and estimated cost

## Requirements

Python 3.11+ and a CometAPI key.

## Installation

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables

Copy `.env.example` into your secret manager or shell. The script reads `COMETAPI_KEY`; it does not load a dotenv file.

## Job Format

One JSON object per line. Required fields are `id`, `kind`, and `prompt`; `model` is optional.

## Run

```bash
export COMETAPI_KEY=your_key
MAX_WORKERS=1 python batch_image_pipeline.py
```

## Output

Images are written to `output/`; `output/manifest.jsonl` records status, model, path, attempts, and estimated USD cost.

## Retry Behavior

The script retries 408, 429, and 5xx responses up to four attempts. Authentication, invalid-model, and other permanent 4xx errors fail immediately.

## Production Notes

Replace local output with object storage, use a durable queue, add a dead-letter queue, and set spend and retry limits. Re-check model capabilities and pricing before deployment.

## API Reference

The source endpoint is `https://api.cometapi.com/v1/images/generations`; the public catalog is `https://api.cometapi.com/api/models`.
