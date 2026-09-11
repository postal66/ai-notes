<!-- social-ops-fingerprint:8c6050f5b00166d27a8b6aa1ceff0e8b65ada2293f2976121cf826785ddb2422 -->
---
title: How to Debug Failed AI API Generations
---
# How to Debug Failed AI API Generations

![How to Debug Failed AI API Generations](https://resource.cometapi.com/How%20to%20Debug%20Failed%20AI%20API%20Generations.jpeg)

AI API failures are different from regular API failures. A 200 response doesn't mean your generation succeeded. A `null` content field isn't always an error. And the same prompt that worked yesterday might fail today because a provider updated their content policy.

This guide covers how to read AI API errors, what each failure mode actually means, and how to build error handling that tells you what broke instead of just that something broke.

**Note:** Model names like `gpt-5.4` and `gpt-5.4-mini` used in this article are CometAPI's platform identifiers. They work through `https://api.cometapi.com/v1` only — not through OpenAI or Anthropic's APIs directly. See the [full model list](https://www.cometapi.com/models).

## Why AI API debugging is harder than regular API debugging

With a typical REST API, a 200 means success and a 4xx means you did something wrong. AI APIs add a third category: **soft failures** — responses that return 200 but contain no usable content.

Three things can go wrong:

1. **Hard** **failure** — HTTP error (4xx, 5xx). The request didn't complete.
2. **Soft failure** — HTTP 200, but `finish_reason` is `content_filter` or `length`, or `content` is `null`.
3. **Silent failure** — HTTP 200, content looks fine, but the output is wrong in a way you only catch at the application layer.

Most error handling only covers case 1. Cases 2 and 3 are where most production bugs live.

## Understand the error response format

The text completions endpoint returns a consistent error structure:

```
{  "error": {    "message": "human-readable description (often includes request id)",    "type": "comet_api_error",    "param": "the_problematic_parameter_or_null",    "code": "error_code_or_null"  }}
```

Image and video endpoints return different error formats — always parse the raw response body rather than assuming a fixed structure across endpoints.

The `message` field usually tells you exactly what's wrong. The `param` field tells you which parameter caused it. Always log both.

## Know what each HTTP status code means

| Status | Meaning | Common cause | Fix |
| --- | --- | --- | --- |
| 400 | Bad request | Missing model, wrong parameter for this model | Check error.param in the response |
| 401 | Unauthorized | Wrong or missing API key | Verify Authorization: Bearer <key> format |
| 429 | Rate limited | Too many requests | Exponential backoff (see Step 4) |
| 500 | Server error | Provider-side issue, or malformed request body | Retry with backoff; check request format |
| 504 | Gateway timeout | Provider took too long | Retry; consider a faster model |

*Source\*\*:* [*CometAPI chat completions docs*](https://apidoc.cometapi.com/api/text/chat)

The `400` vs `500` distinction matters for retry logic. A `400` means your request is wrong — retrying the same request won't help. A `500` or `504` means the server had a problem — retrying makes sense.

## Check `finish_reason` — the most overlooked field

A `200` response with `finish_reason: "content_filter"` means your generation was blocked. The `content` field will be `null` or empty. If you don't check this, your app silently returns nothing.

| finish\_reason | Meaning | What to do | Fix |
| --- | --- | --- | --- |
| stop | Normal completion | Nothing — this is success | Check error.param in the response |
| length | Hit token limit | Increase max\_tokens or shorten the prompt | Verify Authorization: Bearer <key> format |
| content\_filter | Blocked by safety policy | Rephrase the prompt; avoid specific names/topics | Exponential backoff (see Step 4) |
| tool\_calls | Model called a tool instead of returning text | Handle the tool call; content will be null | Retry with backoff; check request format |
| 504 | Gateway timeout | Provider took too long | Retry; consider a faster model |

*Source\*\*:* [*CometAPI chat completions docs*](https://apidoc.cometapi.com/api/text/chat)

```
import osimport loggingfrom openai import OpenAI, APIStatusError, APIConnectionError, APITimeoutErrorfrom dotenv import load_dotenv​load_dotenv()​api_key = os.environ.get("COMETAPI_KEY")if not api_key:    raise ValueError("COMETAPI_KEY is not set")​client = OpenAI(    base_url="https://api.cometapi.com/v1",    api_key=api_key,)​def safe_complete(messages: list, model: str = "gpt-5.4-mini", **kwargs) -> dict:    """    Complete a chat request with full error and finish_reason handling.    Returns {"content": str, "finish_reason": str, "tool_calls": list | None}    Raises on API errors.    """    try:        response = client.chat.completions.create(            model=model,            messages=messages,            **kwargs        )    except APIStatusError as e:        error_body = {}        try:            error_body = e.response.json().get("error", {})        except Exception:            pass        logging.error(            f"API error status={e.status_code} "            f"message={error_body.get('message')} "            f"param={error_body.get('param')}"        )        raise    except (APIConnectionError, APITimeoutError) as e:        logging.error(f"Network/timeout error: {e}")        raise​    choice = response.choices[0]    finish_reason = choice.finish_reason​    if finish_reason == "content_filter":        raise ValueError(            f"Generation blocked by content filter. "            f"Model: {model}. Rephrase the prompt."        )​    if finish_reason == "length":        used = response.usage.completion_tokens if response.usage else "unknown"        logging.warning(f"Output truncated at token limit. Used {used} tokens.")​    # Return structured result so callers can handle tool_calls explicitly    return {        "content": choice.message.content or "",        "finish_reason": finish_reason,        "tool_calls": choice.message.tool_calls,    }​# Usageresult = safe_complete(    messages=[{"role": "user", "content": "Summarize this article: [text]"}],    model="gpt-5.4-mini")​if result["finish_reason"] == "tool_calls":    # Handle tool call — content will be empty    print("Model wants to call a tool:", result["tool_calls"])else:    print(result["content"])
```

## Detect silent failures at the application layer

Silent failures are the hardest to catch. The API returns 200, `finish_reason` is `stop`, but the output is semantically wrong. You can only catch these at the application layer.

Common patterns:

```
def validate_completion(result: dict, task: str) -> str:    """    Application-layer validation for silent failures.    Raises ValueError if the output doesn't meet basic expectations.    """    content = result["content"].strip()​    # Empty output that isn't a tool call    if not content and result["finish_reason"] != "tool_calls":        raise ValueError(f"Empty output for task '{task}' with finish_reason='{result['finish_reason']}'")​    # Task-specific checks    if task == "classify":        valid_labels = {"positive", "negative", "neutral"}        if content.lower() not in valid_labels:            logging.warning(                f"Unexpected classification output: '{content}'. "                f"Expected one of {valid_labels}. "                f"Model may have returned explanation instead of label."            )​    if task == "json_extract":        import json        try:            json.loads(content)        except json.JSONDecodeError:            raise ValueError(                f"Expected JSON output but got: '{content[:100]}...'. "                f"Try adding 'respond with valid JSON only' to the prompt, "                f"or use response_format={{\"type\": \"json_object\"}}."            )​    if task == "summarize" and len(content.split()) < 10:        logging.warning(            f"Suspiciously short summary ({len(content.split())} words). "            f"Check if the input was too short or the model misunderstood the task."        )​    return content​​# Full flow with silent failure detectionresult = safe_complete(    messages=[{"role": "user", "content": "Classify as positive/negative/neutral: 'Great product!'"}],    model="claude-haiku-4-5")label = validate_completion(result, task="classify")
```

Silent failures usually come from one of three sources: the prompt is ambiguous, the model ignored your format instructions, or the input was too short/long for the task. Logging the full output when validation fails is the fastest way to diagnose which one.

## Add exponential backoff for rate limits

Rate limit errors (429) are temporary. The right response is to wait and retry with increasing delays — a standard practice for any API with rate limits:

```
import timeimport randomfrom openai import RateLimitError​def complete_with_retry(    messages: list,    model: str = "gpt-5.4-mini",    max_retries: int = 3,    **kwargs) -> dict:    """Retry on rate limits and server errors with exponential backoff."""    last_error = None​    for attempt in range(max_retries):        try:            return safe_complete(messages, model=model, **kwargs)​        except APIStatusError as e:            if e.status_code < 500:                raise  # 4xx: don't retry, request is wrong            last_error = e​        except RateLimitError as e:            last_error = e​        except (APIConnectionError, APITimeoutError) as e:            last_error = e​        if attempt < max_retries - 1:            wait = (2 ** attempt) + random.random()  # jitter prevents thundering herd            logging.warning(f"Attempt {attempt + 1} failed. Waiting {wait:.1f}s before retry.")            time.sleep(wait)​    raise RuntimeError(f"All {max_retries} attempts failed") from last_error
```

Don't retry on `400` or `401` — those are client errors that won't resolve on their own.

## Debug image generation failures

Image generation has its own failure modes on top of the standard HTTP errors:

```
import base64import requests​def generate_image_safe(prompt: str, model: str = "dall-e-3") -> dict:    """    Generate an image with full error handling.    Returns {"url": str | None, "bytes": bytes | None, "blocked": bool}    """    api_key = os.environ.get("COMETAPI_KEY")    if not api_key:        raise ValueError("COMETAPI_KEY is not set")​    BASE64_MODELS = {"gpt-image-2", "qwen-image"}​    headers = {        "Authorization": f"Bearer {api_key}",        "Content-Type": "application/json"    }​    payload = {"model": model, "prompt": prompt, "size": "1024x1024"}    if model in BASE64_MODELS:        payload["output_format"] = "png"    else:        payload["response_format"] = "url"​    try:        response = requests.post(            "https://api.cometapi.com/v1/images/generations",            json=payload,            headers=headers,            timeout=60        )        response.raise_for_status()    except requests.exceptions.HTTPError as e:        logging.error(f"Image generation HTTP error: {e.response.status_code} {e.response.text}")        raise    except requests.exceptions.Timeout:        logging.error("Image generation timed out after 60s")        raise​    data = response.json().get("data", [])​    if not data:        logging.warning("Image generation returned empty data — prompt may have been filtered.")        return {"url": None, "bytes": None, "blocked": True}​    item = data[0]​    if "revised_prompt" in item:        logging.info(f"Provider revised prompt to: {item['revised_prompt']}")​    if "url" in item:        return {"url": item["url"], "bytes": None, "blocked": False}​    return {        "url": None,        "bytes": base64.b64decode(item["b64_json"]),        "blocked": False    }
```

Image-specific issues to watch for:

| Symptom | Cause | Fix |
| --- | --- | --- |
| Empty data array | Prompt filtered | Check revised\_prompt; rephrase |
| response\_format error on GPT Image 2 | Parameter not supported | Use output\_format instead |
| n > 1 error on Qwen Image | Model limitation | Loop requests instead |
| URL returns 403 later | URL expired | Download immediately after generation |

*Source\*\*:* [*CometAPI image generation docs*](https://apidoc.cometapi.com/api/image/openai/images)

## Debug video generation failures

Video generation fails differently because it's async. Initialize status variables before the loop so the timeout error message is always well-formed:

```
def submit_and_poll_video(    prompt: str,    model: str = "veo3-fast",    max_wait: int = 600) -> str:    """Submit video task and poll to completion. Returns video URL."""    api_key = os.environ.get("COMETAPI_KEY")    if not api_key:        raise ValueError("COMETAPI_KEY is not set")​    headers = {"Authorization": f"Bearer {api_key}"}​    try:        response = requests.post(            "https://api.cometapi.com/v1/videos",            headers=headers,            files={                "prompt": (None, prompt),                "model": (None, model),                "size": (None, "16x9")            },            timeout=30        )        response.raise_for_status()    except requests.exceptions.HTTPError as e:        logging.error(f"Video submit failed: {e.response.status_code} {e.response.text}")        raise​    task_id = response.json()["id"]    logging.info(f"Video task submitted: {task_id}")​    poll_url = f"https://api.cometapi.com/v1/videos/{task_id}"    elapsed = 0    interval = 10    status = "unknown"   # initialize before loop    progress = 0         # initialize before loop​    while elapsed < max_wait:        try:            poll_response = requests.get(poll_url, headers=headers, timeout=30)            poll_response.raise_for_status()        except requests.exceptions.HTTPError as e:            logging.error(f"Poll request failed: {e.response.status_code}")            raise​        result = poll_response.json()        status = result.get("status", "unknown")        progress = result.get("progress", 0)​        logging.info(f"Task {task_id}: status={status} progress={progress}%")​        if status == "succeeded":            return result["output"][0]        elif status in ("failed", "cancelled"):            error_detail = result.get("error", "no error detail returned")            raise RuntimeError(f"Video task {task_id} failed: {error_detail}")​        time.sleep(interval)        elapsed += interval​    raise TimeoutError(        f"Video task {task_id} did not complete within {max_wait}s. "        f"Last status: {status}, progress: {progress}%"    )
```

Video-specific issues:

| Symptom | Cause | Fix |
| --- | --- | --- |
| Task stuck in queued 10+ min | Server load | Retry with a different model |
| failed with no error detail | Prompt filtered or model error | Rephrase prompt |
| Video URL returns 403 | URL expired | Download immediately |
| task\_not\_exist on Runway first poll | Task still initializing (CometAPI-documented behavior) | Wait 5s and retry |
| Kling returns "succeed" not "succeeded" | Kling's API uses non-standard status string | Handle both in polling logic |

*Source\*\*:* [*CometAPI video generation docs*](https://apidoc.cometapi.com/api/video/veo3)*\*\*,* [*Kling Video docs*](https://apidoc.cometapi.com/video-generation/kling-video)

## Node.js version

```
import OpenAI from 'openai';​const apiKey = process.env.COMETAPI_KEY;if (!apiKey) throw new Error('COMETAPI_KEY is not set');​const client = new OpenAI({  baseURL: 'https://api.cometapi.com/v1',  apiKey,});​async function safeComplete(messages, model = 'gpt-5.4-mini', options = {}) {  let response;​  try {    response = await client.chat.completions.create({ model, messages, ...options });  } catch (err) {    if (err.status && err.status < 500) {      console.error(`Client error ${err.status}: ${err.message}`);    } else {      console.error(`Server/network error: ${err.message}`);    }    throw err;  }​  const choice = response.choices[0];  const finishReason = choice.finish_reason;​  if (finishReason === 'content_filter') {    throw new Error(`Generation blocked by content filter. Model: ${model}`);  }​  if (finishReason === 'length') {    console.warn(`Output truncated. Used ${response.usage?.completion_tokens ?? 'unknown'} tokens.`);  }​  return {    content: choice.message.content ?? '',    finishReason,    toolCalls: choice.message.tool_calls ?? null,  };}​async function completeWithRetry(messages, model = 'gpt-5.4-mini', maxRetries = 3) {  let lastError;​  for (let attempt = 0; attempt < maxRetries; attempt++) {    try {      return await safeComplete(messages, model);    } catch (err) {      // Don't retry 4xx client errors      if (err.status && err.status < 500) throw err;​      lastError = err;      if (attempt < maxRetries - 1) {        const wait = (2 ** attempt + Math.random()) * 1000;        console.warn(`Attempt ${attempt + 1} failed. Retrying in ${(wait / 1000).toFixed(1)}s`);        await new Promise(r => setTimeout(r, wait));      }    }  }​  throw new Error(`All ${maxRetries} attempts failed: ${lastError?.message}`);}​// Usageconst result = await safeComplete(  [{ role: 'user', content: 'Classify as positive/negative/neutral: "Great product!"' }],  'claude-haiku-4-5');​if (result.finishReason === 'tool_calls') {  console.log('Tool call requested:', result.toolCalls);} else {  console.log(result.content);}
```

## A debugging checklist

When a generation fails and you're not sure where to start:

### **For text generation:**

- Is the API key set and in `Authorization: Bearer <key>` format?
- Is `finish_reason` something other than `stop`?
- Is `content` null? Check if `finish_reason` is `tool_calls`
- Did the output get truncated? Check `finish_reason: "length"` and `usage.completion_tokens`
- Is the error a 4xx (fix the request) or 5xx (retry)?
- Does the output pass your application-layer validation? (silent failure)

### **For image generation:**

- Is `data` array empty? (content filter)
- Did you use `response_format` on GPT Image 2? (not supported — use `output_format`)
- Did you set `n > 1` on Qwen Image? (not supported)
- Did you download the image before the URL expired?

### **For video generation:**

- Is the task stuck in `queued`? (try a different model)
- Did you check the `error` field in the failed task response?
- Did you download the video before the URL expired?
- Are you handling both `"succeed"` (Kling) and `"succeeded"` (Veo, Runway)?

## FAQ

### **Q: My request returns 200 but there's no content. What happened?**

Check `finish_reason`. If it's `content_filter`, the generation was blocked — the request succeeded but the output was suppressed. If it's `tool_calls`, the model called a tool instead of returning text, and `content` is null by design. If `finish_reason` is `stop` but content is still empty, that's a silent failure — log the full response and check your prompt.

### **Q: How do I know if my prompt is being filtered?**

For text: check `finish_reason === "content_filter"`. For images: check if the `data` array is empty. For video: check if the task reaches `failed` status shortly after submission with no error detail. In all cases, try rephrasing the prompt to be more neutral.

### **Q: When should I retry a failed request?**

Retry on `429` and `5xx` using exponential backoff. Don't retry on `4xx` — a bad request won't fix itself. The exception is `401` if you're rotating API keys.

### **Q: What's exponential backoff and why does it matter?**

Instead of retrying immediately, you wait progressively longer: 1s, 2s, 4s. Adding random jitter (+ random.random()) prevents multiple clients from retrying in sync. This is a standard practice for any API with rate limits — not specific to CometAPI.

### **Q: The video task is stuck in** **`queued`** **for 10 minutes. Is it failed?**

Not necessarily — queues can back up under load. Wait up to your `max_wait` threshold, then raise a `TimeoutError` and retry with a different model. Log the task ID so you can check status manually if needed.

### **Q: How do I catch silent failures?**

Silent failures require application-layer validation — the API won't tell you the output is semantically wrong. Check that the output matches the expected format (valid JSON, expected label, minimum length). Log the full output when validation fails. The most common causes are ambiguous prompts, ignored format instructions, or inputs that are too short or too long for the task.

---

*Originally published at [https://www.cometapi.com/how-to-debug-failed-ai-api-generations/](https://www.cometapi.com/how-to-debug-failed-ai-api-generations/).*
