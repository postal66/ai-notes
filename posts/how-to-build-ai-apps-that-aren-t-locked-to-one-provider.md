<!-- social-ops-fingerprint:e15b765868a3c59f810f35b485607892d62e735196d4ce13b1b4b0578f9a6393 -->
---
title: How to Build AI Apps That Aren't Locked to One Provider
---
# How to Build AI Apps That Aren't Locked to One Provider

![How to Build AI Apps That Aren't Locked to One Provider](https://resource.cometapi.com/image-1780677660316.jpeg)

Vendor lock-in in AI apps usually doesn't happen all at once. It creeps in — a direct `import openai` here, a hardcoded model name there, a response field you parse without checking if other providers return the same thing. Six months later, switching providers means rewriting half your backend.

## The four ways lock-in happens

Most developers think lock-in means "I'm using the OpenAI SDK." That's the least dangerous kind. The real traps are subtler:

| Lock-in type | How it happens | Consequence |
| --- | --- | --- |
| SDK lock-in | from openai import OpenAI everywhere | Switching SDK means touching every file |
| Model name lock-in | model="gpt-4o" hardcoded in business logic | Every model change is a code change |
| Parameter lock-in | Using logprobs, n>1, or reasoning\_effort | These don't exist on Claude or Gemini |
| Response format lock-in | Parsing provider-specific response fields | Different providers return different shapes |

The goal isn't to eliminate all of these — some are acceptable tradeoffs. The goal is to know which ones you're taking on.

## Use an OpenAI-compatible endpoint as your abstraction layer

The cleanest way to avoid SDK lock-in is to use a single OpenAI-compatible endpoint that routes to multiple providers. You keep the OpenAI SDK, but the backend can be any provider.

CometAPI does this — one endpoint, one key, 500+ models across OpenAI, Anthropic, Google, DeepSeek, xAI, and others:

```
import osfrom openai import OpenAIfrom dotenv import load_dotenv​load_dotenv()​api_key = os.environ.get("AI_API_KEY")if not api_key:    raise ValueError("AI_API_KEY environment variable is not set")​client = OpenAI(    base_url=os.environ.get("AI_BASE_URL", "https://api.cometapi.com/v1"),    api_key=api_key,)
```

Switching from GPT to Claude to Gemini is a one-line change:

```
# Beforeresponse = client.chat.completions.create(model="gpt-5.4", messages=[...])​# After — same code, different modelresponse = client.chat.completions.create(model="claude-sonnet-4-6", messages=[...])
```

**Note:** Model names like `gpt-5.4` and `claude-sonnet-4-6` are CometAPI's platform identifiers — they work through `https://api.cometapi.com/v1` only, not through OpenAI or Anthropic's APIs directly. See the [full model list](https://www.cometapi.com/models) for the complete catalog and pricing.

## Keep model names out of your business logic

Model names scattered through your code is the most common form of lock-in. The fix is a central config that reads from environment variables:

```
# config.py — one place to change model assignmentsimport os​MODEL_CONFIG = {    "summarize": os.environ.get("MODEL_SUMMARIZE", "claude-opus-4-7"),    "code":      os.environ.get("MODEL_CODE",      "gpt-5.4"),    "classify":  os.environ.get("MODEL_CLASSIFY",  "claude-haiku-4-5"),    "chat":      os.environ.get("MODEL_CHAT",       "gpt-5.4-mini"),}​# Validate at startup — fail fast rather than getting mysterious API errorsfor task, model in MODEL_CONFIG.items():    if not model:        raise ValueError(f"Model config for '{task}' is not set")
```

Your business logic never references a model name directly:

```
from config import MODEL_CONFIG​def summarize(text: str) -> str:    response = client.chat.completions.create(        model=MODEL_CONFIG["summarize"],        messages=[{"role": "user", "content": f"Summarize: {text}"}],        max_tokens=300  # move to config in production    )    return response.choices[0].message.content
```

To switch the summarization model across your entire app, change one environment variable. No grep, no find-and-replace.

## Wrap the response so your code doesn't depend on provider-specific fields

Different providers return slightly different response shapes. If you parse raw API responses throughout your codebase, you're locked to that provider's format.

Wrap it into a normalized dataclass:

```
from dataclasses import dataclassfrom typing import Optionalfrom openai import OpenAI, APIStatusError, APIConnectionError, APITimeoutErrorfrom openai.types.chat import ChatCompletionimport logging​@dataclassclass AIResponse:    content: str    model: str    input_tokens: int    output_tokens: int​def call_model(task: str, messages: list, **kwargs) -> AIResponse:    """    Single entry point for all LLM calls.    Returns a normalized AIResponse regardless of which model handled it.    Raises on 4xx (client errors). Logs and re-raises on 5xx/network errors.    """    model = MODEL_CONFIG.get(task, "gpt-5.4-mini")    if not model:        raise ValueError(f"No model configured for task '{task}'")​    try:        response: ChatCompletion = client.chat.completions.create(            model=model,            messages=messages,            **kwargs        )    except APIStatusError as e:        logging.error(f"API error for task={task} model={model}: {e.status_code} {e.message}")        raise    except (APIConnectionError, APITimeoutError) as e:        logging.error(f"Network error for task={task} model={model}: {e}")        raise​    # content is None when the model triggers a tool call instead of returning text    content = response.choices[0].message.content or ""​    # usage is None in streaming mode — default to 0 if not available    usage = response.usage    input_tokens = usage.prompt_tokens if usage else 0    output_tokens = usage.completion_tokens if usage else 0​    logging.info(        f"task={task} model={model} "        f"input_tokens={input_tokens} output_tokens={output_tokens}"    )​    return AIResponse(        content=content,        model=response.model,        input_tokens=input_tokens,        output_tokens=output_tokens,    )
```

Now your business logic works with `AIResponse` objects, not raw API responses. If a provider changes their response format, you fix it in one place.

## Add streaming support to the wrapper

For chat interfaces, you'll want streaming. The wrapper handles it as a separate path:

```
from typing import Iterator​def stream_model(task: str, messages: list, **kwargs) -> Iterator[str]:    """    Stream tokens from the routed model.    Note: streaming doesn't return usage data.    Fallback is not supported in streaming mode — you've already    started yielding tokens before you know if the full request succeeds.    """    model = MODEL_CONFIG.get(task, "gpt-5.4-mini")    if not model:        raise ValueError(f"No model configured for task '{task}'")​    stream = client.chat.completions.create(        model=model,        messages=messages,        stream=True,        **kwargs    )​    for chunk in stream:        delta = chunk.choices[0].delta.content        if delta:            yield delta​# Usagefor token in stream_model("chat", [{"role": "user", "content": "Hello"}]):    print(token, end="", flush=True)
```

## Know which parameters create lock-in

Some parameters only exist on specific providers. Using them is fine — just know you're making a deliberate choice:

| Parameter | Works on | Lock-in risk |
| --- | --- | --- |
| logprobs | GPT only | High — no equivalent on Claude or Gemini |
| n > 1 | GPT, Gemini (not Claude) | Medium — Claude requires looping |
| reasoning\_effort | GPT o-series only | High — no equivalent elsewhere |
| temperature > 1.0 | GPT, Gemini (not Claude) | Low — Claude caps at 1.0 |
| tools | All major providers | None — safe to use |
| response\_format | All major providers | Low — minor schema differences |

If you're using `logprobs` for confidence scoring, you're locked to GPT for that feature. That's a reasonable tradeoff — just document it so the next developer knows why.

## Make the provider endpoint configurable

Hard-coding `base_url="https://api.cometapi.com/v1"` is still a form of lock-in. Make it an environment variable:

```
# .env — using CometAPIAI_BASE_URL=https://api.cometapi.com/v1AI_API_KEY=your_cometapi_key​# To switch to OpenAI directly, change two lines:# AI_BASE_URL=https://api.openai.com/v1# AI_API_KEY=your_openai_key
```

The client initialization from Step 1 already reads from these variables. Switching between CometAPI and a direct provider connection is now a config change, not a code change.

## Node.js version

```
import OpenAI from 'openai';​const apiKey = process.env.AI_API_KEY;if (!apiKey) throw new Error('AI_API_KEY is not set');​const client = new OpenAI({  baseURL: process.env.AI_BASE_URL ?? 'https://api.cometapi.com/v1',  apiKey,});​// Model IDs are CometAPI platform identifiers — see cometapi.com/modelsconst MODEL_CONFIG = {  summarize: process.env.MODEL_SUMMARIZE ?? 'claude-opus-4-7',  code:      process.env.MODEL_CODE      ?? 'gpt-5.4',  classify:  process.env.MODEL_CLASSIFY  ?? 'claude-haiku-4-5',  chat:      process.env.MODEL_CHAT      ?? 'gpt-5.4-mini',};​// Validate at startupfor (const [task, model] of Object.entries(MODEL_CONFIG)) {  if (!model) throw new Error(`Model config for '${task}' is not set`);}​/** * Single entry point for all LLM calls. * Returns normalized response. Raises on 4xx, logs and re-raises on 5xx/network. */async function callModel(task, messages, options = {}) {  const model = MODEL_CONFIG[task] ?? 'gpt-5.4-mini';​  let response;  try {    response = await client.chat.completions.create({      model,      messages,      ...options,    });  } catch (err) {    // Don't swallow errors — log and re-raise    console.error(`API error task=${task} model=${model}:`, err.message);    throw err;  }​  // content is null when model triggers a tool call  const content = response.choices[0].message.content ?? '';​  // usage may be absent in some configurations  const inputTokens  = response.usage?.prompt_tokens     ?? 0;  const outputTokens = response.usage?.completion_tokens ?? 0;​  console.log(`task=${task} model=${model} input=${inputTokens} output=${outputTokens}`);​  return { content, model: response.model, inputTokens, outputTokens };}​/** * Stream tokens from the routed model. * Usage data is not available in streaming mode. */async function* streamModel(task, messages, options = {}) {  const model = MODEL_CONFIG[task] ?? 'gpt-5.4-mini';​  const stream = await client.chat.completions.create({    model,    messages,    stream: true,    ...options,  });​  for await (const chunk of stream) {    const delta = chunk.choices[0]?.delta?.content;    if (delta) yield delta;  }}​// Usage — blockingconst result = await callModel('classify', [  { role: 'user', content: 'Positive or negative? "Loved it!"' }]);console.log(result.content);​// Usage — streamingfor await (const token of streamModel('chat', [  { role: 'user', content: 'Hello' }])) {  process.stdout.write(token);}
```

## What lock-in is acceptable

Not all lock-in is worth fighting. Some tradeoffs make sense:

- **Using the** **OpenAI** **SDK** — It's the de facto standard. Most providers support it. Low-risk lock-in.
- **Provider-specific features you actually need** — If you need `logprobs`, use them. Isolate that code so it's easy to find and replace later.
- **Fine-tuned models** — A fine-tuned model is inherently tied to one provider. That's expected.

The lock-in worth avoiding is the accidental kind — model names in business logic, raw response parsing spread across files, API keys hardcoded in source.

## What's next

You now have an abstraction layer that keeps provider details out of your business logic. The last article in this series covers what happens when things go wrong: how to debug failed generations, interpret error codes, and build error handling that actually tells you what broke.

Next: **How to Debug Failed AI API Generations**

## FAQ

### **Q: What's the difference between SDK lock-in and model lock-in?**

SDK lock-in means your code imports a specific library and would need to change if you switched SDKs. Model lock-in means model names are scattered through your business logic. SDK lock-in is less dangerous because most providers now support the OpenAI SDK format. Model lock-in is more insidious because it's harder to find and fix.

### **Q: If I use CometAPI, am I just trading** **OpenAI** **lock-in for CometAPI lock-in?**

Partially. You're trading direct provider lock-in for a proxy layer. The upside: one key, one endpoint, easy model switching. The risk: if CometAPI has an outage, all your providers go down together. The mitigation is already in the code above — `AI_BASE_URL` is an environment variable. If you need to bypass CometAPI and call a provider directly, it's a config change, not a code change.

### **Q: Can I use Claude's extended thinking or** **OpenAI**'s **`reasoning_effort`** **through this pattern?**

Yes, pass them as `**kwargs` to `call_model`. Just know that if you route that task to a different model, those parameters will be ignored or cause an error. Document which tasks use provider-specific features so the next developer knows why.

### **Q: How do I handle Claude's** **`temperature`** **cap at 1.0 when routing between Claude and** **GPT\***\*?\*\*

Keep `temperature` at or below 1.0 to stay in the safe range for both. If you need higher temperature for creative tasks on GPT specifically, route those tasks to GPT explicitly in `MODEL_CONFIG` rather than letting them fall through the generic router.

### **Q: Should I abstract the image and video generation APIs the same way?**

The same principles apply — central config, normalized response wrapper, no provider-specific fields in business logic. Image and video APIs have more structural differences (async vs sync, different parameter sets) so the abstraction layer takes more work. Start with text, then extend the pattern once the structure is proven.

### **Q: What about** **context window** **differences between models?**

This is a real risk when routing. GPT-5.5 has a 1M token context window, Claude models support up to 200K, and [Gemini 3.5 Flash](https://www.cometapi.com/models/google/gemini-3-5-flash/) supports up to 1M. If you route a long document task to a model with a shorter context window, the input gets truncated silently. Add a context length check before routing if your tasks involve long inputs — or always route long-context tasks to a specific model in `MODEL_CONFIG` rather than letting them fall through to a default.

---

*Originally published at [https://www.cometapi.com/how-to-build-ai-apps-that-aren-t-locked-to-one-provider/](https://www.cometapi.com/how-to-build-ai-apps-that-aren-t-locked-to-one-provider/).*
