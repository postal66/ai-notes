<!-- social-ops-fingerprint:2c47a94216ddf1c80e234ebb46ab89b7e2001381d6cf801419b67abc4055de52 -->
---
title: Best AI API Gateways in 2026: CometAPI, Portkey, LiteLLM, and Cloudflare Compared
---
# Best AI API Gateways in 2026: CometAPI, Portkey, LiteLLM, and Cloudflare Compared

![Best AI API Gateways in 2026: CometAPI, Portkey, LiteLLM, and Cloudflare Compared](https://resource.cometapi.com/image-1780995285827.jpeg)

Picking an AI API gateway is not the same problem it was two years ago. In 2024, most developers either called OpenAI directly or spun up LiteLLM locally. Now there are hosted options with pricing dashboards, per-key credit limits, and model catalogs that span dozens of providers. The category has expanded enough that choosing wrong means undoing real integration work later.

This article compares four gateways that show up repeatedly in developer discussions: CometAPI, Portkey, LiteLLM, and Cloudflare AI Gateway. The goal is not to pick a winner — each makes sense for a different situation — but to lay out what each one actually does so you can match the tool to your use case.

> **Note on model names:** Model identifiers used in this article (such as `gpt-5.4`, `claude-opus-4-7`) are CometAPI platform identifiers. They are not official names from OpenAI or Anthropic, whose own naming conventions differ.

## What These Tools Actually Do

Before comparing features, it helps to be precise about what an AI API gateway does. At minimum: it sits between your application and one or more AI providers, forwarding requests and returning responses. Beyond that minimum, gateways diverge significantly.

Some gateways — Cloudflare AI Gateway, for example — are primarily a pass-through layer that adds logging and caching without touching your API key or pricing. Others, like CometAPI, act as a reseller: you pay them, they pay the underlying provider, and the pricing difference is part of the value proposition. LiteLLM is different again — it is software you run yourself, not a hosted service.

Understanding this distinction matters before you evaluate any specific feature.

## Feature Comparison

The table below uses information from each product's official documentation or public-facing dashboard as of May 2026. Features marked with a dash (—) were not confirmed in official sources at time of writing.

| Feature | CometAPI | Portkey | LiteLLM | Cloudflare AI Gateway |
| --- | --- | --- | --- | --- |
| Deployment | Hosted (SaaS) | Hosted + self-host | Self-hosted (open source) | Hosted (Cloudflare edge) |
| Model catalog | 500+ models across providers | 1,600+ LLMs via unified API | Depends on your config | OpenAI, Anthropic, Workers AI |
| Pricing model | Reseller (pay CometAPI) | Pass-through + platform fee | Infrastructure cost only | Pass-through (free tier available) |
| OpenAI-compatible API | Yes (api.cometapi.com/v1) | Yes (api.portkey.ai/v1) | Yes (local or remote) | Yes (via gateway URL) |
| Per-key credit limits | Yes (dashboard) | Yes | Yes (via config) | — |
| Group-based pricing ratios | Yes (0.8x default, 0.1x internal) | — | — | — |
| Request logging | Yes (4 log types) | Yes | Yes | Yes |
| Success rate monitoring | Yes (30-day uptime view) | Yes | Yes | Yes |
| Free tier | Yes (new accounts) | Yes | Open source (infra cost) | Yes |
| Self-hosting option | No (enterprise: dedicated server) | Yes | Yes (core use case) | No |

Sources: [CometAPI dashboard](https://cometapi.com/), [Portkey homepage](https://portkey.ai/), [LiteLLM GitHub](https://github.com/BerriAI/litellm), [Cloudflare AI Gateway documentation](https://developers.cloudflare.com/ai-gateway/)

## Connecting to Each Gateway

All four gateways expose an OpenAI-compatible endpoint, which means the same client structure works for all of them — you change the `base_url`, credentials, and in Portkey's case, how you specify the model.

### Python

```
import osfrom openai import OpenAI​def require_env(name: str) -> str:    """Raise a clear error if a required environment variable is missing."""    val = os.environ.get(name)    if not val:        raise ValueError(f"Missing required environment variable: {name}")    return val​​# ── CometAPI ────────────────────────────────────────────────────────────────# Hosted reseller with 500+ models. Use CometAPI model identifiers (e.g. "gpt-5.4").cometapi_client = OpenAI(    base_url="https://api.cometapi.com/v1",    api_key=require_env("COMETAPI_KEY"),)​​# ── Portkey ─────────────────────────────────────────────────────────────────# Hosted gateway with observability and 1,600+ LLMs.# Route to a provider by prefixing the model name: "@openai/gpt-4o", "@anthropic/claude-3-5-sonnet", etc.# x-portkey-api-key is required; it authenticates requests to Portkey's gateway.portkey_client = OpenAI(    base_url="https://api.portkey.ai/v1",    api_key=require_env("PORTKEY_API_KEY"),    default_headers={        "x-portkey-api-key": require_env("PORTKEY_API_KEY"),    },)​​# ── LiteLLM ──────────────────────────────────────────────────────────────────# Self-hosted proxy. Provider credentials (OPENAI_API_KEY etc.) are set server-side.# By default the proxy does not validate the client API key — "anything" works.# If you have enabled virtual keys on your LiteLLM instance, pass a virtual key instead.litellm_client = OpenAI(    base_url=os.environ.get("LITELLM_BASE_URL", "http://localhost:4000"),    api_key=os.environ.get("LITELLM_API_KEY", "anything"),)​​# ── Cloudflare AI Gateway ───────────────────────────────────────────────────# URL-based pass-through. Keep your real provider API key — Cloudflare does not replace it.cf_account_id = require_env("CF_ACCOUNT_ID")cf_gateway_id = require_env("CF_GATEWAY_ID")cloudflare_client = OpenAI(    base_url=(        f"https://gateway.ai.cloudflare.com/v1"        f"/{cf_account_id}/{cf_gateway_id}/openai"    ),    api_key=require_env("OPENAI_API_KEY"),)​​def ask(client: OpenAI, model: str, question: str) -> str:    """    Minimal wrapper showing the common call pattern across all four gateways.​    Model format varies by gateway:      CometAPI:   "gpt-5.4", "claude-opus-4-7", etc. (CometAPI identifiers)      Portkey:    "@openai/gpt-4o", "@anthropic/claude-3-5-sonnet", etc.      LiteLLM:    whatever model names you configured in your proxy      Cloudflare: standard OpenAI model names, e.g. "gpt-4o"​    This function does not handle finish_reason, tool_calls, or provider errors.    For production error handling, see: How to Debug Failed AI API Generations.    """    response = client.chat.completions.create(        model=model,        messages=[{"role": "user", "content": question}],    )    return response.choices[0].message.content or ""
```

### Node.js

```
import OpenAI from "openai";​function requireEnv(name) {  const val = process.env[name];  if (!val) throw new Error(`Missing required environment variable: ${name}`);  return val;}​// ── CometAPI ────────────────────────────────────────────────────────────────const cometClient = new OpenAI({  baseURL: "https://api.cometapi.com/v1",  apiKey: requireEnv("COMETAPI_KEY"),});​// ── Portkey ─────────────────────────────────────────────────────────────────// Route to a provider by prefixing the model: "@openai/gpt-4o", "@anthropic/claude-3-5-sonnet"const portkeyClient = new OpenAI({  baseURL: "https://api.portkey.ai/v1",  apiKey: requireEnv("PORTKEY_API_KEY"),  defaultHeaders: {    "x-portkey-api-key": requireEnv("PORTKEY_API_KEY"),  },});​// ── LiteLLM ──────────────────────────────────────────────────────────────────// Self-hosted. Default mode accepts any API key value.// Set LITELLM_BASE_URL if your server runs on a different host or port.const litellmClient = new OpenAI({  baseURL: process.env.LITELLM_BASE_URL ?? "http://localhost:4000",  apiKey: process.env.LITELLM_API_KEY ?? "anything",});​// ── Cloudflare AI Gateway ───────────────────────────────────────────────────const cfClient = new OpenAI({  baseURL: `https://gateway.ai.cloudflare.com/v1/${requireEnv("CF_ACCOUNT_ID")}/${requireEnv("CF_GATEWAY_ID")}/openai`,  apiKey: requireEnv("OPENAI_API_KEY"),});​/** * Minimal wrapper showing the common call pattern. * Model format varies by gateway — see Python example above for details. * Does not handle finish_reason or error recovery; add those for production use. */async function ask(client, model, question) {  const response = await client.chat.completions.create({    model,    messages: [{ role: "user", content: question }],  });  return response.choices[0].message.content ?? "";}
```

The connection pattern is the same across all four. The meaningful differences show up elsewhere: what you can observe, what you can control, and what happens when something breaks.

## What Each Tool Is Actually Good At

### CometAPI

CometAPI's main offering is a hosted catalog with over 500 model endpoints, including image and video generation models alongside text models. Pricing runs through a group-based ratio system — the default group applies a 0.8x multiplier to CometAPI's base rates. You can configure different ratio groups for internal use (0.1x) versus paying customers, which makes it practical for building a tiered product without managing separate accounts.

The dashboard gives you four types of logs (standard API calls, image generation, video generation, Midjourney), a 30-day uptime view, and per-key credit limits. Credit limits let you give API keys to clients or contractors with a hard ceiling on spend, which solves a real problem when you are distributing access to a shared account.

What CometAPI does not offer: self-hosting (enterprise customers can request a dedicated server, but this is not a standard self-hosted option), rate limiting at the gateway level, or SSO.

**Best fit:** Indie developers and small teams that want to route across many models — including image and video — with one API key and one billing relationship, and who need per-key budget controls.

### Portkey

Portkey is a hosted gateway built around observability. It gives you access to 1,600+ LLMs through a unified API, with routing handled by prefixing the model name with the provider (`@openai/gpt-4o`, `@anthropic/claude-3-5-sonnet`). This means you do not need separate client configurations for each provider — one Portkey client handles all of them, and you swap the model string.

Beyond routing, Portkey provides request tracing, prompt versioning, and fallback routing that you configure in the dashboard rather than in code. The self-hosting option means you can run Portkey on your own infrastructure if compliance requires it.

The GitHub repository for Portkey's open-source gateway is actively maintained — check the [current star count](https://github.com/Portkey-AI/gateway) directly rather than relying on any number cited here, as it changes frequently.

**Best fit:** Teams that need audit trails, multi-provider routing from a single client configuration, or want to manage API key exposure across developers.

### LiteLLM

LiteLLM is a Python package and proxy server, not a hosted service. You run it yourself. This is a meaningful distinction: there is no third party handling your requests or holding your API keys. Provider credentials (your real OpenAI key, Anthropic key, etc.) are set as server-side environment variables; the client just points at the local proxy.

By default, LiteLLM does not validate the API key clients send — any value works. If you enable virtual key management, clients pass virtual keys that LiteLLM validates against its own database. Either way, the proxy translates OpenAI-format requests to whatever format the upstream provider expects, so your application code does not change when you add a new provider.

The tradeoff is operational overhead: you are responsible for running, scaling, and updating the server.

**Best fit:** Teams with devops capacity, organizations with compliance constraints that prohibit third-party API proxies, or anyone who wants cross-provider routing without trusting request content to a SaaS vendor.

### Cloudflare AI Gateway

Cloudflare AI Gateway is structurally different from the other three. You do not change your API key or pay Cloudflare for model access. Instead, you replace the provider's base URL with a Cloudflare-managed URL that adds logging, caching, and rate limiting at the edge.

Because Cloudflare sits between your application and the provider, it can cache identical requests — useful if your application sends the same prompts repeatedly. The free tier covers most indie developer use cases. The limitation is scope: Cloudflare does not aggregate models across providers. You still need separate provider accounts and keys for each provider you use.

**Best fit:** Developers already on Cloudflare's infrastructure, or anyone who wants caching and logging on top of existing provider accounts without introducing a new billing relationship or changing API keys.

## Scenario Matching

| Scenario | Recommended tool | Reason |
| --- | --- | --- |
| Indie app, want to try 10+ models with one API key | CometAPI | Broad catalog, simple setup, per-key credit limits |
| Need image + video generation in same integration | CometAPI | Unified endpoint for text, image, and video models |
| Team of 5, need to track who's using what model | Portkey | Request tracing, team management |
| Route to 1,600+ LLMs with one client config | Portkey | @provider/model routing, no per-provider setup |
| Want fallback routing across providers without code changes | Portkey | Declarative fallback config in dashboard |
| Enterprise with data residency requirements | LiteLLM (self-hosted) | No third-party traffic handling |
| Budget is zero, comfortable with self-management | LiteLLM | Open source, no platform cost |
| Already using OpenAI directly, want caching | Cloudflare AI Gateway | URL swap only, no new billing relationship |
| Need RBAC for multiple teams | Portkey or LiteLLM | Both have team/role management; CometAPI and Cloudflare do not |

## What These Four Do Not Cover

This comparison covers the gateways that appear most often in indie developer discussions. The market includes other options worth knowing about: Helicone focuses on observability without acting as a proxy, OpenRouter specializes in routing to open-weight and research models, and AWS Bedrock is Amazon's managed AI service aimed at enterprise workloads. If your requirements do not fit any of the four above, those are the next places to look.

## Making the Switch

If you are currently calling a provider directly and considering a gateway, the code change is small. For CometAPI, you add one environment variable and change the `base_url`. For Portkey, you add a header and change how you specify the model (`@openai/gpt-4o` instead of `gpt-4o`). For Cloudflare, you change the URL without touching your provider API key. For LiteLLM, you run a local server first, then point your client at it.

The larger question is not how to make the switch, but whether you need to. If you call a single provider, have no cost visibility problems, and do not need cross-model routing, a gateway adds complexity without benefit. If you are hitting multiple providers, distributing keys to contractors, or finding that unexpected bills are a recurring problem, the integration overhead is worth it.

## FAQ

### **Can I use these gateways together?**

Yes. Some teams run LiteLLM self-hosted for sensitive workloads and CometAPI for everything else. Cloudflare AI Gateway can sit in front of CometAPI requests if you want Cloudflare's caching layer on top — though this adds a network hop.

### **Do these gateways store my prompts?**

Depends on the tool and your configuration. Portkey and CometAPI log requests by default; both have retention settings. LiteLLM only stores what you configure it to store, on your own infrastructure. Cloudflare's logging behavior is described in their AI Gateway documentation. Read the privacy terms for any hosted service before sending sensitive content through it.

### **What happens if the gateway goes down?**

For hosted gateways (CometAPI, Portkey, Cloudflare), gateway downtime means your application cannot reach the AI provider through that path. LiteLLM running locally has the same availability characteristics as your own server. Before committing to any hosted gateway for production use, check its SLA and whether it offers direct-provider fallback if the gateway itself is unavailable.

### **Is there a free way to evaluate each before committing?**

Yes. CometAPI and Portkey both have free tiers. LiteLLM is open source and costs only the infrastructure you run it on. Cloudflare AI Gateway is free within generous limits. You can run all four against the same test prompts before making a decision.

### **How do I pick the right model names for each gateway?**

Each gateway has its own convention. CometAPI uses its own identifiers (`gpt-5.4`, `claude-opus-4-7`). Portkey uses `@provider/model-name` format (`@openai/gpt-4o`, `@anthropic/claude-3-5-sonnet`). LiteLLM uses the model names you define in your proxy config. Cloudflare passes standard provider model names through unchanged. Check each gateway's documentation for its current model list before writing code.

### **Does switching gateways affect my existing rate limits?**

Yes. If you move from direct OpenAI calls to a gateway that manages the provider relationship (like CometAPI), your effective rate limits are determined by the gateway's account with OpenAI, not your personal account. Verify rate limit behavior with the gateway before migrating production traffic.

---

*Originally published at [https://www.cometapi.com/best-ai-api-gateways-in-2026-cometapi-portkey-litellm-and-cloudflare-compared/](https://www.cometapi.com/best-ai-api-gateways-in-2026-cometapi-portkey-litellm-and-cloudflare-compared/).*
