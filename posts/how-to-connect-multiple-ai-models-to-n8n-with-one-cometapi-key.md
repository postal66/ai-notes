<!-- social-ops-fingerprint:2621f9769a3edddc840b0aa9dcfdc28fbe3ae98518d4052a052d7ebf283ebd65 -->
---
title: How to Connect Multiple AI Models to n8n With One CometAPI Key
---
# How to Connect Multiple AI Models to n8n With One CometAPI Key

![How to Connect Multiple AI Models to n8n With One CometAPI Key](https://resource.cometapi.com/Connect%20Multiple%20AI%20Models%20to%20n8n.jpeg)

## How Can You Connect Multiple AI Models to n8n With One API?

Connecting AI models one provider at a time can work for a prototype, but it becomes fragile as usage grows. Each provider brings separate credentials, endpoints, request formats, rate limits, billing, and response structures. In n8n, that often creates duplicated HTTP nodes and provider-specific branches, so adding a model or changing a fallback path means editing several parts of the workflow.

n8n and CometAPI solve different layers of that problem. n8n controls when a job runs, validates inputs, routes synchronous and asynchronous tasks, retries failures, and stores results. CometAPI centralizes model access behind one API key and one base URL. Together, they keep provider changes out of the orchestration layer: you can switch a model ID while preserving the same queue, polling, storage, and monitoring logic.

This combination is especially useful for mixed image and video jobs coming from spreadsheets or internal tools. The workflow remains visual and auditable in n8n, while credentials, model availability, and usage costs stay easier to manage through one API layer.

The easiest way to integrate multiple AI providers into one app is to separate orchestration from model access. Let n8n handle triggers, branching, retries, and storage, while CometAPI gives every branch one API key and one base URL. The model ID becomes a field in each job instead of a separate provider account, SDK, and billing setup.

In this guide, you will build a working low-code pipeline that reads image and video jobs from Google Sheets, sends them to OpenAI and ByteDance models through CometAPI, saves asynchronous video task IDs, polls for completion, and upserts the final result into an n8n Data Table.

## What You Will Build

The finished workflow follows this path:

**Google Sheets Trigger → Normalize Job → Switch by media type → CometAPI image or video request → Wait and poll video tasks → Upload or reference the output → Data Table upsert.**

Use these columns in the source sheet:

```
job_id | media_type | model | prompt | size | seconds | status
```

A typical image row uses `image`, `gpt-image-2`, and `1024x1024`. A video row uses `video`, `seedance-2-5`, `1280x720`, and a duration from 4 to 30 seconds.

## Before You Start

You need an n8n instance, a Google Sheet, a CometAPI API key, and an n8n Data Table named `ai_jobs`. Create these columns in the Data Table: `job_id`, `media_type`, `model`, `status`, `task_id`, `result_url`, `error`, and `updated_at`.

For self-hosted n8n, add the following values to the environment used by your n8n process:

```
COMETAPI_BASE_URL=https://api.cometapi.com/v1COMETAPI_KEY=your_cometapi_key
```

Restart n8n after changing its environment. In n8n Cloud, or whenever you do not want to expose environment variables in node expressions, create an HTTP Header Auth credential named `CometAPI Bearer`. Set the header name to `Authorization` and the value to `Bearer your_cometapi_key`. The examples below use this credential and the fixed OpenAI-compatible base URL `https://api.cometapi.com/v1.`

### Use Current Model IDs

| Job | Provider and model | Request | Result |
| --- | --- | --- | --- |
| Image | OpenAI · gpt-image-2 | POST /v1/images/generations | Synchronous base64 image |
| Video | ByteDance · seedance-2-5 | POST /v1/videos | Asynchronous task, then poll |

Both IDs and capabilities were available in the [live CometAPI model directory API](https://api.cometapi.com/api/models) on August 11, 2026. The image model supports text-to-image generation. Seedance 2.5 supports text-to-video and image-to-video generation, 4–30 second clips, and the documented 480p and 720p sizes.

**Pricing as of August 11, 2026:** the [GPT Image 2 model page](https://www.cometapi.com/models/openai/gpt-image-2/) lists $4 per million input tokens and $24 per million output tokens. The [Seedance 2.5 model page](https://www.cometapi.com/models/doubao/seedance-2-5/) lists $0.103 per second at 480p and $0.231 per second at 720p. Prices can change, so use the live model directory or model page as the runtime source of truth.

> The important architectural difference is that image generation can be handled as a request-response operation, while video generation should be treated as a stateful job. Persisting the video task ID before polling prevents an n8n execution restart from losing the job.

## Build the Workflow in n8n

### 1. Trigger New Jobs from Google Sheets

Add a **Google Sheets Trigger** node and choose **Row added or updated**. Point it at the worksheet that contains your job queue. Add an IF node immediately after the trigger and continue only when `status` is empty or equals `queued`. This prevents completed rows from being submitted again when the sheet changes.

### 2. Normalize and Validate Each Row

Add a **Code** node named `Normalize Job`. This node applies safe defaults, restricts the workflow to approved model IDs, and produces the same fields for both branches.

```
const row = $json;​const allowedModels = {  image: new Set(['gpt-image-2']),  video: new Set(['seedance-2-5']),};​const mediaType = String(row.media_type || '').trim().toLowerCase();if (!allowedModels[mediaType]) {  throw new Error(`media_type must be image or video; received: ${row.media_type}`);}​const defaultModel = mediaType === 'image' ? 'gpt-image-2' : 'seedance-2-5';const model = String(row.model || defaultModel).trim();if (!allowedModels[mediaType].has(model)) {  throw new Error(`Model ${model} is not allowed for ${mediaType} jobs`);}​const prompt = String(row.prompt || '').trim();if (!prompt) throw new Error('prompt is required');​const seconds = mediaType === 'video' ? Number(row.seconds || 4) : null;if (mediaType === 'video' && (!Number.isInteger(seconds) || seconds < 4 || seconds > 30)) {  throw new Error('Seedance 2.5 seconds must be an integer from 4 to 30');}​return [{  json: {    job_id: String(row.job_id || $execution.id),    media_type: mediaType,    model,    prompt,    size: String(row.size || (mediaType === 'image' ? '1024x1024' : '1280x720')),    seconds,    status: 'processing',    updated_at: new Date().toISOString(),  },}];
```

Add a **Switch** node after `Normalize Job`. Route `image` to the image branch and `video` to the video branch.

### 3. Generate Images Through One Endpoint

Add an **HTTP Request** node named `Create Image` with these settings:

- Method: `POST`
- URL: `https://api.cometapi.com/v1/images/generations`
- Authentication: the `CometAPI Bearer` Header Auth credential
- Body Content Type: JSON

```
{  "model": "={{ $('Normalize Job').item.json.model }}",  "prompt": "={{ $('Normalize Job').item.json.prompt }}",  "size": "={{ $('Normalize Job').item.json.size }}"}
```

GPT Image 2 returns base64 image data. Add a Code node named `Prepare Image File` to turn that data into an n8n binary item:

```
const job = $('Normalize Job').item.json;const b64 = $json.data?.[0]?.b64_json;if (!b64) throw new Error('CometAPI returned no image data');​return [{  json: {    ...job,    status: 'completed',    task_id: '',    result_url: '',    error: '',    updated_at: new Date().toISOString(),  },  binary: {    media: {      data: b64,      mimeType: 'image/png',      fileName: `${job.job_id}.png`,    },  },}];
```

Connect this node to your preferred object-storage node, such as S3 or Google Drive. Store the returned file URL in `result_url`, then upsert the row into `ai_jobs`. Keep large base64 payloads out of the Data Table.

### 4. Create an Asynchronous Video Task

Add an **HTTP Request** node named `Create Video`:

- Method: `POST`
- URL: `https://api.cometapi.com/v1/videos`
- Authentication: `CometAPI Bearer`
- Body Content Type: Form-Data

Add four form fields: `model`, `prompt`, `seconds`, and `size`. Map their values from `Normalize Job`.

Next, add a Code node named `Save Video Task`:

```
const job = $('Normalize Job').item.json;const taskId = $json.id || $json.task_id;if (!taskId) throw new Error('Video task ID missing from create response');​return [{  json: {    ...job,    task_id: taskId,    status: $json.status || 'queued',    result_url: '',    error: '',    updated_at: new Date().toISOString(),  },}];
```

Upsert this item into `ai_jobs` before polling. Saving the task ID immediately means a restart or timeout does not lose the job.

### 5. Wait, Poll, and Store the Video URL

Add a **Wait** node set to 15 seconds. Then add an **HTTP Request** node named `Get Video`:

- Method: `GET`
- URL: `=https://api.cometapi.com/v1/videos/{{ $json.task_id }}`
- Authentication: `CometAPI Bearer`

After the request, use a Switch node on `status`:

- `queued` or `in_progress`: return to the Wait node.
- `completed`: continue to `Finalize Video`.
- `failed` or `error`: write the error to `ai_jobs` and stop.

Add this Code node for the completed branch:

```
const prior = $('Save Video Task').item.json;const resultUrl = $json.video_url || $json.url || $json.data?.video_url;if (!resultUrl) throw new Error('Completed video response has no video URL');​return [{  json: {    ...prior,    status: 'completed',    result_url: resultUrl,    error: '',    updated_at: new Date().toISOString(),  },}];
```

Upsert the final item into `ai_jobs` by `job_id`. CometAPI video URLs can be signed and temporary, so production workflows should download and rehost the file before saving the permanent URL. If your app can receive inbound requests, replace polling with a webhook where the selected model supports callbacks.

## Complete Node Map

The full workflow can be assembled with the following nodes:

1. Google Sheets Trigger — Row added or updated
2. IF — Process only new or queued rows
3. Code — Normalize Job
4. Switch — Image or video
5. Image branch: HTTP Request → Prepare Image File → Object Storage → Data Table Upsert
6. Video branch: HTTP Request → Save Video Task → Data Table Upsert → Wait → HTTP Request → Status Switch
7. Completed video: Finalize Video → Object Storage or permanent URL → Data Table Upsert
8. Failed video: Set Error → Data Table Upsert

For a failure branch, use this expression in an Edit Fields node:

```
{  "job_id": "={{ $('Save Video Task').item.json.job_id }}",  "status": "failed",  "task_id": "={{ $('Save Video Task').item.json.task_id }}",  "result_url": "",  "error": "={{ $json.error?.message || $json.message || 'Video generation failed' }}",  "updated_at": "={{ $now.toISO() }}"}
```

## Test the Workflow

Add these two rows to the source sheet:

```
img-001 | image | gpt-image-2 | A cinematic product photo of a glass robot on a dark desk | 1024x1024 | | queuedvid-001 | video | seedance-2-5 | A paper airplane flies through a sunlit studio, smooth tracking shot | 1280x720 | 4 | queued
```

The image request should return a structure similar to:

```
{  "created": 1786400000,  "data": [    { "b64_json": "iVBORw0KGgoAAA..." }  ]}
```

The video create request should return a task structure similar to:

```
{  "id": "video_task_abc123",  "object": "video",  "status": "queued",  "progress": 0}
```

After polling, a completed response should contain the same task ID, `status: completed`, and a `video_url`. Exact optional fields can vary by model, which is why the normalization code reads the stable task status and result URL instead of copying the entire provider response into your database.

## Common Errors and Fixes

| Error | Fix |
| --- | --- |
| 401 Unauthorized | Confirm the Header Auth value starts with Bearer and the key is active. |
| 404 model or task not found | Check the live model directory and confirm the stored task ID is used in GET /v1/videos/{id}. |
| 400 invalid size or seconds | Use a supported size and keep Seedance 2.5 duration between 4 and 30 seconds. |
| 429 rate limited | Reduce n8n concurrency and retry with exponential backoff and jitter. |
| Polling never ends | Persist attempt count and stop after a defined timeout; treat failed and error as terminal. |
| Image payload is too large | Convert base64 to binary, upload it, and store only the permanent URL. |

## Production Checklist

**Protect credentials.** Keep the API key in n8n credentials or server-side environment variables. Never place it in the spreadsheet or return it to a browser.

**Make every job idempotent.** Use `job_id` as the Data Table upsert key. Before creating a new task, skip rows already marked `processing` or `completed`.

**Control polling and concurrency.** Poll video jobs every 10–20 seconds, cap the number of attempts, and limit simultaneous executions. Back off on 429, 500, and 503 responses instead of creating duplicate tasks.

**Validate model policy before every request.** Keep an allowlist by media type. Refresh model availability and prices from the live directory on a schedule, but deploy model changes through review rather than letting spreadsheet users submit arbitrary IDs.

**Track cost per job.** Store model, resolution, duration, and usage fields with each result. A four-second 720p Seedance 2.5 job is about $0.924 at the August 11, 2026 listed rate; the same four seconds at 480p is about $0.412. Enforce maximum duration and resolution before submitting the request.

**Rehost generated media.** Treat signed provider URLs as delivery links, not permanent storage. Download completed media, upload it to your controlled bucket, and save the durable URL plus checksum.

**Keep an audit trail.** Store the request model, sanitized parameters, task ID, status transitions, retry count, response time, and final asset location. Do not log API keys or full private prompts.

## Why This Pattern Scales

The workflow stays simple because each new provider or model is a routing decision, not a new account integration. The spreadsheet remains the job queue, n8n remains the orchestration layer, and CometAPI remains the single access layer. Add a model by extending the allowlist and branch configuration; the trigger, task persistence, polling, storage, and monitoring logic remain unchanged.

That is the practical answer to multi-provider AI integration: one controlled endpoint and key, explicit model routing, separate synchronous and asynchronous paths, and a durable record for every job.

## FAQs

### Can n8n call multiple AI providers through one API?

Yes. With a unified API layer such as CometAPI, n8n can send requests to different supported models while keeping the provider credential and HTTP integration centralized.

### Can I use CometAPI with n8n's HTTP Request node?

Yes. The HTTP Request node can send requests to CometAPI's API endpoint with the required authentication and model-specific parameters.

### Can n8n automatically switch AI models when one fails?

Yes. Use an IF/Switch branch after the API request and route retryable or model-specific failures to a fallback model. The fallback should support the same modality and required capabilities.

---

*Originally published at [https://www.cometapi.com/how-to-connect-multiple-ai-models-to-n8n-with-one-cometapi-key/](https://www.cometapi.com/how-to-connect-multiple-ai-models-to-n8n-with-one-cometapi-key/).*
