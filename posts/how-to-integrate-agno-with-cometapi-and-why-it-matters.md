<!-- social-ops-fingerprint:a489f286892a2f599c61948013bcc5a9439dcbee25f62afd8053fe4c59b0ce17 -->
---
title: How to integrate Agno with CometAPI (and why it matters)
---
# How to integrate Agno with CometAPI (and why it matters)

![How to integrate Agno with CometAPI (and why it matters)](https://resource.cometapi.com/blog/uploads/2025/10/How-to-integrate-Agno-with-CometAPI.webp)

Agno has been evolving rapidly into a production-grade *AgentOS*—a runtime, framework and control plane for multi-agent systems—while CometAPI (the “all models in one API” aggregator) announced official support as a model provider for Agno. Together they make it straightforward to run multi-agent systems that can switch between hundreds of model endpoints without rewriting your agent code, demand for using unified gateways like CometAPI as drop-in model providers for agent frameworks such as Agno — so the pattern we describe below is both practical and timely.

## What are Agno and CometAPI — exactly?

### What is Agno and why should I care?

Agno is a high-performance, Pythonic multi-agent framework, runtime and UI built to compose agents, teams and agentic workflows with memory, tools, knowledge and human-in-the-loop support. It provides a ready FastAPI runtime (AgentOS), local development tooling, and a control plane UI so you can test and monitor running agents without shipping data out of your environment. If you want to build production-grade agent systems quickly and keep full control of data and observability, Agno is designed for that use case.

### What is CometAPI and why would I use it as an LLM provider?

CometAPI is an API aggregator / model gateway that gives a single, consistent API to dozens to hundreds of LLMs and modalities (text, images, video, etc.). Instead of binding to one model vendor, developers call the CometAPI gateway and can switch providers or models via parameters—useful for cost management, A/B tests, and fallbacks. The platform supports switching between models, unified billing, and claims OpenAI-compatible endpoints — i.e., you can often point an OpenAI-style client at CometAPI’s base URL and authentication token and call models as if they were OpenAI endpoints. That makes CometAPI a convenient “drop-in” provider for frameworks that already speak the OpenAI API surface.

**Recent signal:** CometAPI was announced as a model provider in [Agno’s official docs](https://docs.agno.com/concepts/models/cometapi) and community channels, meaning Agno ships a `CometAPI` model provider class you can pass to your `Agent`. That makes integrating the gateway straightforward and supported.

### Why integrate Agno with CometAPI?

- **No provider lock-in**: CometAPI lets you experiment with many models (OpenAI, Claude, LLama variants, Gemini, etc.) without swapping SDKs. That complements Agno’s model-agnostic design.
- **Faster dev loop**: Because CometAPI supports OpenAI-style endpoints, you’ll often avoid writing a custom Agno provider — you can point Agno’s OpenAI model adapter at CometAPI and start.
- **Observability + control**: Use Agno’s AgentOS runtime and control plane to run agents locally or in your cloud while dialing models through CometAPI, combining the best of model flexibility and runtime observability.

## How do you integrate Agno with CometAPI step-by-step?

Below is a practical, copy-pasteable workflow — from virtualenv creation through running a local AgentOS instance that calls models via CometAPI.

> **Key idea:** Because CometAPI exposes an OpenAI-compatible endpoint, the simplest approach is to use Agno’s OpenAI model adapter and point `OPENAI_API_BASE` (or `openai.api_base`) at CometAPI’s base URL while providing your CometAPI token as the OpenAI API key. CometAPI explicitly documents this “change base\_url + use OpenAI format” flow.

## Environment and Prerequisites you need before starting

### Which OS, Python version, and tools are recommended?

- **OS:** macOS, Linux or Windows — Agno and the tooling support all three. ([GitHub][1])
- **Python:** Use a modern CPython (Agno docs and repo target modern Python versions; recommmend to use Python 3.12). Check Agno’s repo/docs for exact compatibility before production deployments.
- **Package manager / virtualenv:** `uv` (the Astral `uv` project) is an excellent, fast option to manage virtual environments and dependencies.

### What accounts, keys, and network prerequisites must you prepare?

- **CometAPI account & API key.** Get your key from CometAPI and store it in an environment variable (`COMETAPI_KEY`). Agno’s CometAPI model adapter reads `COMETAPI_KEY`.
- **Optional Agno Control Plane account (AgentOS UI).** If you plan to connect a local AgentOS to the Control Plane for monitoring or team features, have your Control Plane access and org/team permissions ready.
- **Database for agent state (optional).** For persistence you’ll typically configure SQLite/Postgres depending on scale; Agno has examples showing Sqlite for local dev.

## How do you integrate Agno with CometAPI step-by-step?

Below is a practical, copy-pasteable workflow — from virtualenv creation through running a local AgentOS instance that calls models via CometAPI.

> **Key idea:** Because CometAPI exposes an OpenAI-compatible endpoint, the simplest approach is to use Agno’s OpenAI model adapter and point `OPENAI_API_BASE` (or `openai.api_base`) at CometAPI’s base URL while providing your CometAPI token as the OpenAI API key. CometAPI explicitly documents this “change base\_url + use OpenAI format” flow.

### 1) Install `uv` and create the virtual environment

`uv` installer (one-line):

```
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create and activate a reproducible venv (Agno quickstart uses Python 3.12):

```
# create a venv managed by uv
uv venv --python 3.12
# activate (POSIX)
source .venv/bin/activate
```

(If you prefer traditional `python -m venv .venv` that works too; `uv` gives lockfile + reproducibility benefits.)

### 2) Install Agno and runtime deps (via `uv pip`)

```
```bash
uv pip install -U agno openai mcp 'fastapi[standard]' sqlalchemy 'httpx[socks]'
# optionally, add extras you need
uv pip install -U agno[infra]  # if using cloud infra plugins
```
```

(install other libraries you need: vector DB clients, monitoring libs, etc.)
Agno’s commonly install `agno` + provider SDKs.

### 3) Export the CometAPI API key

Set the environment variable the Agno Comet provider will read:

```
bash
# macOS / Linux
export COMETAPI_KEY="sk-xxxx-your-cometapi-key"

# Windows (PowerShell)
setx COMETAPI_KEY "sk-xxxx-your-cometapi-key"
```

Agno’s CometAPI provider defaults to reading `COMETAPI_KEY`.

### 4) Create a small Agno Agent that uses the CometAPI provider

Open the folder and create a new file. Save below as `comet_agno_agent.py`:

```
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.cometapi import CometAPI
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

#  1) Create an Agent which uses CometAPI as the model provider
#  id parameter selects a model id from the CometAPI catalog
agno_agent = Agent(
    name="Agno Agent",
    model=CometAPI(id="gpt-5-mini"),
    # Add a database to the Agent
    db=SqliteDb(db_file="agno.db"),
    # Add the Agno MCP server to the Agent
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    # Add the previous session history to the context
    add_history_to_context=True,
    markdown=True,
)

# 2) Attach Agent to AgentOS and get FastAPI app
agent_os = AgentOS(agents=[agno_agent])
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()
```

### 5) Run Agno locally to test

Start the AgentOS (FastAPI) dev server:

```
# In the activated .venv (uv-managed)
fastapi dev agno_comet_agent.py
# defaults to http://localhost:8000
```

Open `http://localhost:8000/docs` to inspect the automatically generated endpoints.

> Ensure env vars are set (COMETAPI\_KEY\_API\_KEY)

### 6) Connect your local AgentOS to the AgentOS Control Plane (optional)

If you want the Agno web control plane to monitor your local AgentOS:

1. Visit the AgentOS Control Plane: `os.agno.com` and sign in.
2. Click **Add new OS → Local**, enter `http://localhost:8000`, give it a name, and **Connect**.
   Once connected you get the web UI for chat, sessions, metrics and management.

## What are the configuration & security best practices?

### Secrets & API keys

Never commit API keys. Use environment variables, a secrets manager, or `.env` combined with local `.gitignore`. Best practice: rotate keys regularly and restrict usage by IP if the provider supports that. (OpenAI docs and other vendors recommend env vars.)

### Model selection & cost control

Use CometAPI’s model catalog to choose models with appropriate cost/latency trade-offs. Put sensible rate limits and implement retries with exponential backoff. CometAPI exposes model lists and pricing in its docs.

### Observability

Use Agno’s AgentOS control plane for agent logs, session traces and metrics. Combine that with provider-level metrics (CometAPI dashboard) to correlate costs/latency with agent activity.

### Privacy & data residency

Because AgentOS runs in your cloud, you retain control of session data. Still, avoid sending sensitive PII to third-party models unless explicitly permitted by policy; if needed, use on-prem or private model hosting.

## What are best practices and recommended use cases?

### Best practices

- **Start small:** test with a development agent and a low-tier model (cheaper) before scaling.
- **Model fallback:** implement a fallback chain (e.g., cheaper small model → stronger model on failure). CometAPI makes it easy to switch models by name.
- **Fine-grained tooling:** give agents limited, audited tools (websearch, DB access) and instrument tool calls with traces. Agno provides tools integrations and a pattern for instrumented calls.
- **Rate limiting and batching:** batch similar requests, and apply rate limits at the gateway or client to avoid surges.

### Typical use cases

- **RAG (Retrieval-Augmented Generation) chatbots** — Agno agents for documents + CometAPI for language generation.
- **Automated workflows** — multi-agent workflows that combine web scraping tools, vector DBs, and generative steps.
- **Prototype-to-production** — iterate quickly using CometAPI to try different models, then pin the chosen provider or move to an enterprise contract.

## How to get started with Comet API

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

To begin, explore the model capabilities of [CometAPI](https://www.cometapi.com/?utm_source=agno%20uted) in the [Playground](https://api.cometapi.com/console/playground) and consult the Continue [API guide](https://apidoc.cometapi.com/continue-1624859m0) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. CometAPI offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

## Final thoughts

Integrating Agno with CometAPI gives you a pragmatic way to build flexible, observable, and vendor-agnostic agentic systems. Agno supplies the runtime and control plane; CometAPI supplies a single gateway to many models. Together they reduce operational friction: less per-agent model plumbing, easier experimentation, and centralized billing/controls.

---

*Originally published at [https://www.cometapi.com/how-to-integrate-agno-with-cometapi/](https://www.cometapi.com/how-to-integrate-agno-with-cometapi/).*
