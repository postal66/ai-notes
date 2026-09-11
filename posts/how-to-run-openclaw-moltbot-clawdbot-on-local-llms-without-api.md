<!-- social-ops-fingerprint:881f2a6d89e316c0792fbb5f9b40d5ea2051b217c9adccca46c5ab18657b59be -->
---
title: How to run openClaw (Moltbot/ Clawdbot ) on local LLMs without API
---
# How to run openClaw (Moltbot/ Clawdbot ) on local LLMs without API

![How to run openClaw (Moltbot/ Clawdbot ) on local LLMs without API](https://resource.cometapi.com/How%20to%20run%20openClaw(MoltbotClawdbot)%20on%20local%20LLMs%20without%20API.png)

OpenClaw (formerly Clawdbot, briefly Moltbot) has exploded faster than almost any agent project I’ve seen.

In less than three weeks, it crossed 100,000 GitHub stars. People call it a *“24/7 AI intern”*, and honestly, that description isn’t far off. It can read messages, run shell commands, manage files, and quietly live in the background while you go about your day.

But after the initial excitement, a very practical question started showing up everywhere:

> “This is cool… but how do I run it **without** burning money on APIs?”

That question is exactly why I wrote the guide .

## What is the Buzz Behind OpenClaw (Formerly Clawdbot)?

To understand the technical shift toward local execution, one must first appreciate what OpenClaw actually is. At its core, openClaw ( Moltbot / Clawdbot) is a "conversation-first" autonomous agent. Unlike traditional chatbots that live in a browser tab and wait for prompts, OpenClaw runs as a background daemon on your machine. It integrates directly with messaging platforms like WhatsApp, Telegram, Discord, and Signal, effectively turning your chat app into a command line for your life.

### The Evolution from Clawdbot to OpenClaw

The project's history is as volatile as it is fascinating.

**Clawdbot (Late 2025):** Created by Peter Steinberger, it was launched as a wrapper for Anthropic's Claude, designed to execute tasks rather than just output text. It was dubbed "Claude with hands."

**Moltbot (Jan 2026):** Following a trademark dispute with Anthropic regarding the name "Clawd," the project rebranded to "Moltbot," embracing a lobster mascot named "Molty" (referencing the molting of a shell).

**OpenClaw (Jan 30, 2026):** To emphasize its open-source nature and distance itself further from specific corporate identities while retaining the "Claw" heritage, the community settled on OpenClaw.

What sets OpenClaw apart is its permission system. It can read your emails, check your calendar, execute shell commands, and even manage its own memory in Markdown files stored locally. However, its default configuration relies on sending all this context to cloud APIs (primarily Anthropic or OpenAI), which raises two critical issues: Cost and Privacy.

## Why Should You Switch to Local LLMs?

The default "out-of-the-box" experience of openClaw ( Moltbot / Clawdbot) is powered by Claude 3.5 Sonnet or Opus. While these models are highly intelligent, they are priced per token. An autonomous agent that runs 24/7—checking for emails, monitoring server logs, and summarizing chats—can generate millions of tokens a day.

### The Cost of Autonomy

Autonomous agents don’t behave like chat sessions. They loop. They re-read context. They summarize logs. They check inboxes again and again.

I’ve seen users report things like:

> “I left Clawdbot running overnight to reorganize my Obsidian vault and woke up to a $40 bill.”

That’s not misuse — that’s just how autonomy works.

With a local model, the marginal cost drops to **zero** (aside from electricity). You stop thinking “should I let this run?” and start thinking “what else can I automate?”

### Privacy Isn’t a Side Benefit — It’s the Main One

openClaw ( Moltbot / Clawdbot) can read:

- Emails
- Chat histories
- Source code
- Personal documents

OpenClaw is designed to have deep access to your system. It reads your personal messages and file systems. When using an API, every file the bot reads is uploaded to a third-party server for processing. By using a local LLM, no data ever leaves your local network. Your financial documents, private chats, and codebases remain air-gapped from Big Tech.

## Running OpenClaw with Ollama (My Default Recommendation)

If you’re comfortable with the terminal, **Ollama** is the easiest way to run local LLMs today.

openClaw ( Moltbot / Clawdbot) speaks OpenAI-compatible APIs. Ollama exposes one by default. That’s the entire trick.

### Minimum system and software checklist

- **A machine** with a recent OS (Linux/macOS/Windows + WSL2). Local GPU acceleration recommended for larger models; CPU-only works for small models or lightweight tasks.
- **Node.js ≥ 22** (OpenClaw’s CLI and Gateway expect Node).
- **Ollama** (or another local LLM runtime) installed locally if you plan to run local models. Ollama exposes an OpenAI-compatible local API by default (commonly on `http://localhost:11434`).
- If using a proxy like **Lynkr**, install it (npm or clone the repo). Lynkr can present an Anthropic/OpenAI-like endpoint to OpenClaw while routing to local models.

### Step 1: Install OpenClaw (quick commands)

OpenClaw recommends installing via npm/pnpm. Run:

```
# install OpenClaw CLI globally (Node >= 22)
npm install -g openclaw@latest
# or using pnpm
pnpm add -g openclaw@latest

# run first-time onboarding (installs Gateway daemon)
openclaw onboard --install-daemon
```

The onboard wizard installs a user-service daemon (systemd/launchd) so the Gateway keeps running in the background. After onboarding you can run the Gateway manually for debugging:

```
openclaw gateway --port 18789 --verbose
```

### Step 2: Install Ollama and pull a model

Ollama is straightforward to install and run. On macOS/Linux:

```
# install Ollama (one-line installer)
curl -fsSL https://ollama.com/install.sh | sh

# pull a recommended assistant model (example)
ollama pull kimi-k2.5

# verify Ollama is running (default API on port 11434)
ollama list
# or check HTTP
curl http://localhost:11434/v1/models
```

Ollama exposes an API compatible with many OpenAI-style clients; OpenClaw’s provider integration supports Ollama and will auto-detect a local Ollama instance unless you override configuration.

### Step 3: Minimal OpenClaw model configuration

### deploy a compatibility layer (Lynkr) or configure OpenClaw to point to the local endpoint

Because openClaw ( Moltbot / Clawdbot) historically spoke to certain API shapes (e.g., Anthropic-style endpoints), the easiest path is to run a small proxy that translates OpenClaw calls into your local server’s API.

- **Lynkr**: install and configure Lynkr to listen on the port OpenClaw expects; configure it to forward to your Ollama/text-generation-webui instance. Community tutorials show step files and sample `config.json` entries. After Lynkr is running, OpenClaw can remain configured for the original provider but will actually talk to your local model.

If you prefer to change OpenClaw’s config directly, point the model backend URL in `.openclaw` configuration to your local server endpoint:

openClaw ( Moltbot / Clawdbot) stores configuration in `~/.openclaw/openclaw.json`. A minimal file to prefer a local model looks like this:

```
{
  "agent": {
    "model": "ollama/kimi-k2.5"
  },
  "models": {
    "providers": {
      "ollama": {
        "name": "Ollama (local)",
        "options": {
          "baseURL": "http://127.0.0.1:11434/v1"
        }
      }
    }
  }
}
```

If you leave out a `models.providers.ollama` block, openClaw ( Moltbot / Clawdbot) will often auto-detect a local Ollama instance if available. Use `openclaw models list` and `openclaw models set` to interactively manage model settings without directly editing the file.

### Step 4: Start OpenClaw and test a message

With Ollama running and the Gateway active:

```
# start the gateway (if not running as a daemon)
openclaw gateway --port 18789 --verbose

# send a test message to the agent
openclaw agent --message "Hello from local OpenClaw" --thinking low
```

If the Gateway and models are correctly configured, you’ll see the assistant respond and the message routed via the local Ollama model.

## Can I try to avoid modifying OpenClaw via proxy?

Yes — that’s exactly what proxy tools like **Lynkr** do: they present an Anthropic/OpenAI-style endpoint to openClaw ( Moltbot / Clawdbot) while listening on the port OpenClaw expects and forwards the content to a local Ollama or text-generation-webui instance.. This is valuable because it is **no API key, no cloud billing, and local model execution**, it avoids changing OpenClaw internals while giving you local control.

### Architectural overview (what components talk to what)

- **OpenClaw (agent/app)** — the main assistant, which issues model calls and orchestrates tools and message integration.
- **LLM proxy (e.g., Lynkr)** — receives OpenClaw’s API-style requests and forwards them to local model servers (or cloud fallback). The proxy can also implement caching, token trimming, and memory compression to reduce costs.
- **Local LLM server (e.g., Ollama, standalone ggml runtime, Llama.cpp, local containerized model)** — serves model inference on-machine. Ollama is widely used because it provides an easy local server and model packaging workflow; other runtimes are possible.
- **Optional cloud fallback** — proxy can route complex requests to cloud models when necessary (hybrid mode).

### Why use a proxy instead of patching openClaw directly?

**Privacy & TCO:** Local inference keeps data on your machine and avoids API bills.

**Compatibility:** openClaw ( Moltbot / Clawdbot) expects a particular API surface (Anthropic/“Copilot” style). A proxy preserves that surface so OpenClaw needs minimal changes.

**Safety & flexibility:** The proxy can implement request routing rules (local first, cloud fallback), rate limiting, request truncation, and other safeguards.

### Example: configure Lynkr to route to local Ollama

1. Install Lynkr:

```
npm install -g lynkr
# or: git clone https://github.com/Fast-Editor/Lynkr.git && npm install
```

1. Create a `.env` (example):

```
cp .env.example .env
```

Edit `.env` with:

```
# primary provider: local Ollama
MODEL_PROVIDER=ollama
OLLAMA_MODEL=kimi-k2.5
OLLAMA_ENDPOINT=http://localhost:11434

# optional hybrid fallback
PREFER_OLLAMA=true
FALLBACK_ENABLED=true
FALLBACK_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-...
```

1. Start Lynkr:

```
# if installed globally
lynkr

# if cloned
npm start
```

Lynkr by default will announce a local proxy (for example: `http://localhost:8081`) and an OpenAI/Anthropic-compatible `/v1` endpoint that OpenClaw can point to. Then configure OpenClaw’s model provider to use the Lynkr base URL (see next snippet).

### Point OpenClaw to the Lynkr endpoint

Either edit `~/.openclaw/openclaw.json` or use the CLI to set your provider base URL:

```
{
  "models": {
    "providers": {
      "copilot": {
        "options": {
          "baseURL": "http://localhost:8081/v1"
        }
      }
    }
  },
  "agent": {
    "model": "kimi-k2.5"
  }
}
```

Now openClaw ( Moltbot / Clawdbot) will call `http://localhost:8081/v1` (Lynkr), which routes into `ollama://kimi-k2.5` locally. You get the seamless experience of an external provider without leaving your machine.

> For users who prefer a Graphical User Interface (GUI) to manage their models, or who want to use specific quantized models (GGUF format) from Hugging Face, LM Studio is the preferred choice.

## Is It Safe to Run Autonomous Agents Locally?

This is perhaps the most critical question. When you run openClaw ( Moltbot / Clawdbot), you are essentially giving an AI shell access to your computer.

### The "Sudo" Problem

If you ask a cloud-based Claude to "delete all files in my documents," it might refuse due to safety filters. A local, uncensored Llama 3 model has no such inhibitions. If openClaw ( Moltbot / Clawdbot) misinterprets a command, it could theoretically execute destructive commands.

### Security Best Practices

Run in Docker: Do not run openClaw ( Moltbot / Clawdbot) directly on your host machine's "bare metal" unless you are absolutely sure of the risks. Use the official Docker image which sandboxes the environment.

The example below is a minimal `docker-compose.yml` that demonstrates three services: Ollama (local model runtime), Lynkr (proxy), and OpenClaw Gateway (CLI run in container). **Note:** adapt volumes and device passthrough for GPU access.

```
version: "3.8"
services:
  ollama:
    image: ollama/ollama:latest
    restart: unless-stopped
    ports:
      - "11434:11434"
    volumes:
      - ./ollama-data:/var/lib/ollama

  lynkr:
    build: ./lynkr
    restart: unless-stopped
    ports:
      - "8081:8081"
    environment:
      - MODEL_PROVIDER=ollama
      - OLLAMA_ENDPOINT=http://ollama:11434

  openclaw:
    image: node:22
    working_dir: /workspace
    volumes:
      - ~/.openclaw:/root/.openclaw
      - ./workspace:/workspace
    command: sh -c "npm install -g openclaw && openclaw gateway --host 0.0.0.0 --port 18789"
    depends_on:
      - lynkr
```

This is an illustrative stack; production deployments should add network isolation, resource limits, and GPU device mapping where appropriate.

## Common troubleshooting steps and limitations

### If openClaw ( Moltbot / Clawdbot) doesn’t see Ollama

- Ensure Ollama is running and the base URL is reachable (`http://127.0.0.1:11434/v1`).
- Use `openclaw models list` and `openclaw doctor` to surface configuration issues.

### If Lynkr routing fails

- Confirm Lynkr is listening (usually `http://localhost:8081`).
- Check `.env` for `OLLAMA_ENDPOINT` and `MODEL_PROVIDER` correctness.
- Validate that Lynkr maps the `/v1` paths openClaw ( Moltbot / Clawdbot) calls — some provider implementations expect slightly different paths; adjust base paths if needed.

### Model capability gaps

Local models vary: some excel at coding, others at chat. Hybrid strategies (local first, cloud fallback) can help: route routine tasks locally and escalate complex reasoning to a cloud model with caching to reduce cost. Lynkr and similar proxies implement exactly this logic.

## Conclusion

OpenClaw’s design and the active ecosystem around it make a local, API-free deployment practical today. With tools like Ollama for local hosting, Lynkr for API translation, and robust community documentation, you can run capable agents on machines you control — from a desktop GPU to a handheld device — without sending your data to a third-party LLM provider.

However, if you weigh the pros and cons, for example, if you still want to use openClaw ( Moltbot / Clawdbot) via the API without the necessary equipment, then I would recommend [CometAPI.](https://www.cometapi.com/) It provides Anthropic and OpenAI endpoints and frequently offers discounts—generally 20% off the official price.

Developers can access  and [Claude Sonnet](https://www.cometapi.com/models/anthropic/claude-sonnet-4-5/)/ [Opus 4.5](https://www.cometapi.com/models/anthropic/claude-opus-4-5-20251101/) and [GPT-5.2](https://www.cometapi.com/models/openai/gpt-5-2-pro/) via [CometAPI](https://www.cometapi.com/), the latest models listed are as of the article’s publication date. To begin, explore the model’s capabilities in the Playground and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for Gemini 3 today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-run-openclawmoltbotclawdbot-on-local-llms-without-api/](https://www.cometapi.com/how-to-run-openclawmoltbotclawdbot-on-local-llms-without-api/).*
