<!-- social-ops-fingerprint:6f30cdaf47dae30cb02def46977c4d865f71758e3aca188f42bae32853717f22 -->
---
title: Integrating LiteLLM with CometAPI — a practical guide for engineers
---
# Integrating LiteLLM with CometAPI — a practical guide for engineers

![Integrating LiteLLM with CometAPI — a practical guide for engineers](https://resource.cometapi.com/blog/uploads/2025/09/Integrating-LiteLLM-with-CometAPI.webp)

Over the past few months, the AI landscape has shifted quickly: OpenAI shipped GPT-5 to developers and refreshed its realtime stack; Anthropic updated Claude and its data-use policies; and Google pushed Gemini deeper into the home and smart-device ecosystem. Those shifts matter because they change which models you’ll want to reach and how you’ll monitor them—exactly where a “unified API + observability” pairing like **LiteLLM + CometAPI** shines.

In this guide, you’ll get a practical, code-heavy walkthrough of integrating **LiteLLM** with **CometAPI** (which speaks an **OpenAI-compatible** dialect), covering installation, basic calls, async & streaming, and deployment tips. Along the way, we’ll weave in what the newest model updates imply for your integration choices.

## What is LiteLLM?

LiteLLM is an open-source Python SDK and proxy (LLM gateway) that exposes a single, consistent API for many model providers (OpenAI, Anthropic, Vertex/Google, AWS Bedrock, Hugging Face, etc.). It normalizes provider differences (input format, errors, output shapes), provides retry/fallback/routing logic, and supports both a lightweight SDK **and** a proxy server for central LLM routing in infra stacks. In other words: one API to call many models.

### Feature:

- Unified Python functions like `completion`, `responses`, `embeddings`.
- OpenAI-compatible routing (so clients that speak OpenAI-style APIs can be pointed to other providers).
- Async + streaming support (async wrappers like `acompletion`, and `stream=True` for chunked responses).

### How LiteLLM models and endpoints map

- Use `completion()` (sync) and `acompletion()` (async) in the Python SDK for chat/completion style calls.
- For OpenAI-compatible endpoints, LiteLLM supports an `api_base`/`api_key` override so the SDK knows to hit an OpenAI-style path.

## What is CometAPI?

**CometAPI** is a “one API for many models” service that exposes **hundreds of models** (including OpenAI GPT-5, Anthropic Claude, xAI Grok, Qwen, GLM, and image/video generators) through an **OpenAI-compatible** REST interface. Because it’s compatible, you can typically point your OpenAI client to CometAPI’s `base_url` and keep the same request/response schema—making it a drop-in alternative or complement to first-party APIs.

> **Tip:** This compatibility is exactly what LiteLLM expects. You can reference CometAPI models via LiteLLM using OpenAI-style calls, or route them through the LiteLLM Proxy with `base_url` overrides.

## Prerequisites for integrating LiteLLM with CometAPI

Before you can connect LiteLLM to CometAPI, you’ll need a few things in place:

### Python environment

- Python 3.8+ (recommended: a virtual environment via `venv` or `conda`).
- `pip` upgraded: `python -m pip install --upgrade pip`

**LiteLLM installed** `pip install litellm` (Optional: install `litellm` if you want to run the LiteLLM proxy server.)

### CometAPI account & API key

1. Sign up at cometapi.com.
2. Get your **API key** from your dashboard.
3. Store it as an environment variable: `export COMETAPI_KEY="sk-xxxx"`

### Basic understanding of OpenAI-compatible APIs

- CometAPI exposes **OpenAI-style endpoints** like `/v1/chat/completions`.
- LiteLLM natively supports this format, so no custom client is needed.

## How do I make a basic completion call (using LiteLLM → CometAPI)?

Use LiteLLM’s completion function to send messages to a CometAPI model. You can specify models like cometapi/gpt-5 or cometapi/gpt-4o.

### Method 1: Use the environment variable for the API key (recommended).

```
from litellm import completion
import os

# Option A: use env var

os.environ = "sk_xxx" # CometAPI key

# Direct call with explicit api_base + api_key

resp = completion(
    model="cometapi/gpt-5",
    api_key=os.environ,
    api_base="https://www.cometapi.com/console/", # CometAPI base URL

    messages=[
        {"role":"system", "content":"You are a concise assistant."},
        {"role":"user", "content":"Explain why model-aggregation is useful in 3 bullets."}
    ],
    max_tokens=200,
    temperature=0.2
)

print(resp.choices.message)
```

If you prefer, you can also set `OPENAI_API_KEY`/`OPENAI_API_BASE` — LiteLLM accepts several provider conventions; check your version of the SDK docs.

### Method 2: Pass the API key explicitly：

Example:

```
from litellm import completion
import os
# Define your messages (array of dictionaries with 'content' and 'role')

messages =

api_key = 'your-cometapi-key-here'  # Alternative: Store it in a variable for explicit passing

# CometAPI call - Method 2: Explicitly passing API key

response_2 = completion(model="cometapi/gpt-4o", messages=messages, api_key=api_key)

# Print the responses

print(response_2.choices.message.content)
```

## How do asynchronous and streaming calls work with LiteLLM → CometAPI?

### Asynchronous Calls

- **Meaning**: An asynchronous call is when a request is made to do something (like fetch data or run a task), but instead of waiting for it to finish before moving on, the program continues executing other code.
- **Key Idea**: “Don’t block, keep working while waiting.”
- **Example**:
- In web apps: fetching data from an API without freezing the UI.
- In Python: using `async/await` with `asyncio`.
- In JavaScript: using `Promises` or `async/await`.

**Use case**: Improves performance and responsiveness by not blocking the main thread.

---

### Streaming Calls

- **Meaning**: A streaming call means that instead of waiting for all the data to be ready and then sending it back in one go, the server sends chunks of data as soon as they’re available.
- **Key Idea**: “Send data piece by piece while it’s being produced.”
- **Example**:
- Watching a YouTube video before the whole video file is downloaded.
- Real-time chat apps or stock ticker updates.
- In APIs: instead of waiting for the model’s full output, the client receives words/tokens progressively (like how ChatGPT streams text).

An **asynchronous streaming call** meBoth LiteLLM and CometAPI support streaming and asynchronous usage. LiteLLM exposes `stream=True` to receive an iterator of chunks, and `acompletion()` for async usage. Use streaming when you want low-latency partial outputs (UI interactivity, token-by-token processing).ans the request is made without blocking, and results are delivered progressively as they’re ready.For non-blocking or real-time applications, use LiteLLM’s acompletion function for asynchronous calls. This is useful with Python’s asyncio for handling concurrency.

Example:

```
from litellm import acompletion
import asyncio, os, traceback

async def completion_call():
    try:
        print("Testing asynchronous completion with streaming")
        response = await acompletion(
            model="cometapi/chatgpt-4o-latest",
            messages=,
            stream=True  # Enable streaming for chunked responses

        )
        print(f"Response object: {response}")

        # Iterate over the streamed chunks asynchronously

        async for chunk in response:
            print(chunk)
    except Exception:
        print(f"Error occurred: {traceback.format_exc()}")
        pass

# Run the async function

await completion_call()
```

**Explanation**:

- `acompletion` is the asynchronous version of `completion`.
- `stream=True` enables streaming, where the response is yielded in real-time chunks.
- Use `asyncio` to run the function (e.g., in a Jupyter Notebook with `await` or via `asyncio.run()` in scripts).
- If an error occurs, it’s caught and printed for debugging.

**Expected Output**:You’ll see the response object and individual chunks printed, e.g.:

```
Testing asynchronous completion with streaming
Response object: <async_generator object acompletion at 0x...>
Chunk: {'choices': }
Chunk: {'choices': }
... (full response streamed in parts)
```

## Additional Tips

- **Model not found / endpoint mismatch:** ensure you choose a model name that exists on CometAPI (their docs list available identifiers) and that your LiteLLM model prefix conventions match (e.g., `cometapi/<model>` when required).CometAPI models follow the format cometapi/, e.g., cometapi/gpt-5, cometapi/gpt-4o, cometapi/chatgpt-4o-latest. Check the CometAPI documentation for the latest models.
- **Error Handling:** Always wrap calls in try-except blocks to handle issues like invalid keys or network errors.
- **Advanced Features**: LiteLLM supports parameters like temperature, max\_tokens, and top\_p for fine-tuning responses. Add them to the completion or acompletion calls, e.g., completion(…, temperature=0.7).
- **403 / auth errors** — ensure you’re using the right CometAPI key and sending it either as `api_key` to LiteLLM

## Conclusion

[The integration of LiteLLM with CometAPI](https://apidoc.cometapi.com/litellm-1390375m0) is low friction because both sides use OpenAI-compatible, well-documented interfaces. Use LiteLLM to centralize LLM usage in your codebase, set `api_base` to CometAPI and pass the CometAPI key, and leverage LiteLLM’s sync/async/streaming helpers to create responsive and flexible applications.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [LiteLLM Integration Guide](https://apidoc.cometapi.com/litellm-1390375m0) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

---

*Originally published at [https://www.cometapi.com/integrating-litellm-with-cometapi/](https://www.cometapi.com/integrating-litellm-with-cometapi/).*
