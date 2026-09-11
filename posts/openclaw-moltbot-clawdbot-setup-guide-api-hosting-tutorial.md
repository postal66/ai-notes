<!-- social-ops-fingerprint:f90df3ca0c9787f8deddcd9ab4d286d26a929444e2fb64e488c0d80fd75725b7 -->
---
title: Openclaw(Moltbot /Clawdbot) : Setup Guide+ API hosting Tutorial
---
# Openclaw(Moltbot /Clawdbot) : Setup Guide+ API hosting Tutorial

![Openclaw(Moltbot /Clawdbot) : Setup Guide+ API hosting Tutorial](https://resource.cometapi.com/Moltbot.webp)

Leading this charge is **Moltbot** (formerly known as **Clawdbot**), a project that went from a niche developer tool to a viral sensation with over 60,000 GitHub stars in just weeks. Created by Peter Steinberger, Moltbot represents the "molting" of the AI agent—shedding the limitations of web interfaces to inhabit the messaging apps and file systems we use every day.

> Recent attention: the project rebranded from *Clawdbot* to *Moltbot* after a trademark-related request from Anthropic issued a trademark request because "Clawd" sounded too similar to "Claude."

## What is Moltbot (Clawdbot) and Why is it Viral?

Moltbot is an open-source, self-hosted AI agent designed to bridge the gap between powerful Large Language Models (LLMs) and your local computer. Unlike ChatGPT or Claude.ai, which exist within a "walled garden" browser tab, Moltbot runs as a **Gateway** on your hardware (Mac, Linux, or VPS).

It translates natural language messages from platforms like **Telegram**, **WhatsApp**, and **Slack** into executable actions on your machine. Whether you need to find a file on your desktop while you're at the grocery store or trigger a complex deployment script from your phone, Moltbot acts as your digital proxy with full system access.

Why it’s different

- **Local-first execution & tools**: Moltbot can actually run commands on your host (with consent), call external APIs, and use “skills” that are small programs or markdown-defined workflows.
- **Multi-channel**: you use the same assistant from Telegram, WhatsApp, Slack, Discord and more — it can proactively message you.
- **Memory & persistence**: Moltbot stores memory files in the workspace (Markdown) and indexes them for retrieval so the assistant “remembers” across sessions (details below).

### Core Capabilities at a Glance

| Feature | Description |
| --- | --- |
| Multi-Channel | Use Telegram, WhatsApp, Discord, Slack, iMessage, and more. |
| Full PC Access | Execute shell commands, manage files, and control browsers. |
| Proactive AI | It doesn't just wait for you; it can send "heartbeat" alerts or reminders. |
| Privacy First | Your files and logic stay on your hardware; only prompts go to the API. |
| Self-Evolution | It can write its own "Skills" to extend its functionality over time. |
| openai-compatible | Moltbot supports the OpenAI-compatible API protocol; Connects to any compatible service |
| Custom baseUrl | Supports modifying the API endpoint address; Switch between providers with ease |

## How Does Clawdbot "Remember" Everything Without a Database?

One of the most innovative aspects of Moltbot is its **transparent memory architecture**. Most AI tools suffer from "amnesia" between sessions. Moltbot solves this using a layered system of plain Markdown files located in your workspace. This approach ensures you can read, edit, and audit exactly what your AI knows about you.

### What is the memory design and how does it work?

Moltbot’s memory is deliberately simple and auditable: memory is **plain Markdown files** inside the agent workspace. The files are the source of truth — the model only “remembers” what was written to disk. The default layout uses:

- `memory/YYYY-MM-DD.md` — daily append-only logs (the assistant reads today + yesterday on session start).
- `MEMORY.md` — curated long-term memory you can control and only load into private sessions.

This design has two big benefits:

1. **Auditability** — you can read and edit what the assistant will use as memory.
2. **Simplicity for tooling** — memory plugins provide vector/BM25 indexing so the agent can search relevant memory entries quickly.

### Technical approach

- **Conversation/session store**: The gateway tracks sessions and forwards the right context to the agent runtime. This allows the agent to preserve conversation state across messages and channels.
- **Indexed local data**: Moltbot can index local files and documents and expose them via search tools (semantic or keyword) for retrieval. This is how the agent can "remember" your meeting notes, snippets, or code.
- **Tool outputs and memory primitives**: Skills and tools can write to a durable store (database or filesystem), and Moltbot can reference those entries on later prompts. Many deployments use SQLite, Postgres, or local JSON/YAML for small setups.
- **LLM embeddings & vector store**: For semantic recall the usual pattern is to embed documents and store vectors in a vector DB, then retrieve nearest neighbors to include in prompts. Moltbot’s architecture accommodates model-agnostic tool calls, so you can plug in your embedding + vector store combo.

Security caveat: because memory is persistent and skills can run commands on the host, the recommended defaults are conservative: DM pairing for unknown senders, sandboxing for non-main sessions, and a `moltbot doctor` check to surface risky configurations. Always review the security documentation and treat inbound messages as untrusted input.

### The Memory Hierarchy

| File | Purpose |
| --- | --- |
| SOUL.md | Defines the agent's personality, tone, and core operating rules. |
| USER.md | Stores facts about you (e.g., "I prefer Python over Ruby," "I work in fintech"). |
| MEMORY.md | Long-term, curated memories that the agent saves for permanent recall. |
| memory/YYYY-MM-DD.md | Daily logs and raw context from specific dates. |

When you tell Moltbot, "Remember that I like my reports in PDF format," it doesn't store this in a hidden SQL database. It literally opens `USER.md` and appends a new bullet point. This allows the agent to maintain context across weeks of conversation, making it feel like a true personal assistant rather than a fresh instance every morning.

---

## Moltbot setup guide: prerequisites and installation

Below is a practical setup checklist and commands for getting a basic Moltbot instance running on macOS/Linux (Ubuntu). This is a condensed, production-minded guide — if you need a GUI or managed host, skip to the API hosting section.

### What you’ll need (prerequisites)

- A machine running macOS or Linux (Windows can work via WSL2). Node.js **v22+** is required for the gateway and CLI.
- A text editor and basic shell familiarity.
- At least one LLM API key (OpenAI, Anthropic, Venice, or a local model like Ollama) — Moltbot itself is model-agnostic.
- Optional: Docker, if you prefer containerized deployment.

### Step-by-Step Installation

1. **Install the Package**: Run the following command in your terminal: `npm install -g clawdbot@latest`
2. **Launch the Onboarding Wizard**: The wizard is the heart of the setup. It will guide you through security confirmations and model selection. `clawdbot onboard --install-daemon`
3. **Confirm Security Risks**: Moltbot will ask you to acknowledge that it has "root-like" access to your machine. You must type a confirmation to proceed.
4. **Configure the Gateway**: The wizard will install the `clawdbot gateway` as a background service (`launchd` on Mac or `systemd` on Linux) so it stays online 24/7.

### Quick install (macOS / Linux)

This example uses the recommended git + npm method that mirrors the official docs.

```
# Clone and enter repo
git clone https://github.com/moltbot/moltbot.git
cd moltbot

# Install via npm (global CLI) or run locally
npm install -g @moltbot/cli   # or: npm ci && npm run build

# Create environment file from example
cp .env.example .env

# Edit .env and add your API keys (OPENAI_API_KEY, ANTHROPIC_API_KEY, etc.)
# Then run onboarding
moltbot onboard --install-daemon
moltbot start
```

### Docker (basic)

```
# docker-compose.yml (simplified)
version: "3.8"
services:
  moltbot:
    image: moltbot/moltbot:latest
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OTHER_KEYS=...
    volumes:
      - ./data:/app/data
    ports:
      - "3000:3000"
```

Run with:

```
docker compose up -d
```

### Post-install: pair a messaging channel

Moltbot supports multiple channels. Pairing usually involves generating a pairing token from the gateway UI or CLI and using a small "pairing URL" to connect a Telegram bot or WhatsApp account — the specific steps depend on the channel connector you choose (Telegram Bot API vs. grammY wrapper, WhatsApp via Baileys, etc.). See the docs for `moltbot connect telegram` or `moltbot connect whatsapp`.

## How do I control my PC from Telegram via Moltbot(step by step)?

Below is a secure, practical walkthrough for controlling a host via Telegram messages — useful for remote administration, running scripts, fetching logs, or asking Moltbot to run a small job. **Important security note**: do **not** expose your Gateway to the open Internet without an API token and firewall; only allow trusted Telegram users to talk to your bot.

### 1) Create a Telegram bot with BotFather

1. In Telegram, message `@BotFather`.
2. Send `/newbot` and follow the prompts.
3. Copy the bot token `123456789:ABC-...` (BotFather will display it).

### 2) Add the token to your gateway

Set the environment variable or config:

```
export TELEGRAM_BOT_TOKEN="123456789:ABC-..."
# or add to your gateway's config file:
# channels:
#   telegram:
#     botToken: "123456789:ABC-..."
```

You can also add the token via `moltbot channels add` or `moltbot configure` commands depending on your CLI version. The Telegram docs show this quick setup path.

### 3) Run the onboarding wizard and pick Telegram

Run:

```
moltbot onboard --install-daemon
```

During the wizard:

- Choose your model provider (Anthropic Opus, OpenAI, or local).
- When prompted for channels, choose **Telegram** and paste the token.
- Configure pairing/allowlist to restrict who can message the bot (important — set your user ID so only you can control it).

Community walkthroughs and the onboarding process will ask you to paste a small command output from your host to prove node pairing — follow the prompt.

### 4) Enable the exec tool and approvals (safely)

Moltbot can run system commands via its `exec` tool, but it does so under an explicit approval model:

- Exec approvals are recorded in `~/.clawdbot/exec-approvals.json`.
- The system will prompt in chat for approval the first time an action is requested; you can respond `/approve` to continue (or deny).
- For fully automated workflows you can create a limited allowlist of commands or a “bin” of pre-approved scripts.

Example: enable the exec tool in `moltbot` config (or via UI/plugin):

```
{
  "tools": {
    "exec": {
      "enabled": true,
      "allowlist": ["/usr/local/bin/backup.sh", "/usr/bin/uptime"]
    }
  }
}
```

The project has explicit exec approval flows and forwards approval prompts to chat channels when asked, making it easier to review and approve operations.

### 5) Try a safe command from Telegram

From your Telegram account (the allowed user) send:

```
@YourMoltbot Hi — please run: uptime
```

The assistant will:

1. Ask for confirmation (if exec requires approval).
2. Run the allowed command on the host.
3. Return the output to the chat.

### 6) Create safer actions via skills

Instead of giving direct shell access via chat, prefer skills that encapsulate actions (e.g., `backup` skill that calls a script and returns a nicely formatted result). Skills can be installed/uninstalled and are safer to review.

## How do I host the Moltbot API (Gateway) and use the HTTP API?

### Can Moltbot serve an API that other programs can call?

Yes. Moltbot’s Gateway can expose **OpenResponses-compatible** HTTP endpoints (like `POST /v1/responses`) and an OpenAI-style `/v1/chat/completions` shim. These endpoints are **disabled by default** and must be enabled in the gateway config. The OpenResponses HTTP endpoint maps directly to the gateway agent run path, so requests are executed as real agent sessions (with the same routing/permissions).

## What Is an API Proxy in Moltbot?

An **API proxy** in Moltbot is an intermediary service that sits between Moltbot’s agent runtime and upstream LLM providers such as:

- OpenAI
- Anthropic
- Venice
- Azure OpenAI
- Self-hosted OpenAI-compatible endpoints

Instead of Moltbot calling the provider directly, **all requests are routed through the proxy**, which can:

- Rewrite requests and responses
- Enforce rate limits
- Track token usage and costs
- Switch models dynamically
- Mask real API keys from Moltbot
- Add authentication, logging, and caching

Conceptually:

```
Moltbot → API Proxy → LLM Provider
```

This architecture dramatically improves **security, observability, and cost control**.

> 🚀 Quick Start: We recommend using [CometAPI](https://www.cometapi.com/) (apiyi.com) to obtain your API key. Registration grants you free credits. It supports all major algorithms, such as Claude Sonnet 4.5, Claude Opus 4.5, and GPT-5.2, and is typically 10-20% cheaper than official prices.

### Step 1: Get your API Proxy Key

#### Method 1: Set Environment Variables. In your Moltbot `.env` file:

```
OPENAI_API_BASE=https://cometapi.com/v1
OPENAI_API_KEY=moltbot-internal-token
OPENAI_MODEL=gpt-4.1-mini
```

Key points:

- `OPENAI_API_BASE` points to your proxy, not OpenAI
- `OPENAI_API_KEY` is a **proxy-issued token**
- The proxy decides what provider/model is actually used

Restart Moltbot after updating these values.

#### Method 2: Configuring via config.json:

- Finding the Moltbot Config File
- Open up your config file and add or update the `models.providers`

The config file usually lives in one of these spots:

| Operating System | Config File Path |
| --- | --- |
| macOS | ~/.clawdbot/config.json or ~/.moltbot/config.json |
| Linux | ~/.clawdbot/config.json or ~/.moltbot/config.json |
| Windows | %USERPROFILE%\.clawdbot\config.json |

You can also find it using the command line:

```
# See your current config
moltbot config list

# Get the exact path to your config file
moltbot config path
```

---

### Step 2: Verify Connectivity

Run a simple test prompt:

```
moltbot test llm
```

If configured correctly, Moltbot will receive responses normally—without ever contacting the upstream provider directly.

## Cost estimates for running Moltbot Using hosted models

The cost of using a managed model depends on the API price, so choosing a cheap API provider is quite important, which is why I recommend CometAPI.

### Pricing factors typically depend on:

- Vendor pricing. The cost of using a managed model depends on the API price, so choosing a cheaper API vendor is crucial, which is why I recommend [CometAPI](https://www.cometapi.com/).
- The choice between a flagship or lightweight model; for example, the price difference between Claude Opus 4.5 and GLM 4.7 is significant.
- The complexity of the content being processed. If your workflows are text-heavy (file parsing, long replies), add tokens.

**Ballpark examples (illustrative, Jan 2026 prices reported in community posts):**

- Occasional personal use (a few hundred responses / month, mixed local models and cheap API calls): **$0–$50/month**.
- Heavy personal/pro developer use (file indexing, lots of tool calls): **$100–$1,000/month**.
- Team or always-on production (many users + web scraping + chaining): **$1,000+/month** unless you optimize model use aggressively.

### Ways to cut costs

- **Model routing:** send lightweight tasks to cheaper models or local LLMs, reserve expensive models for long-haul reasoning — community testing suggests this can cut costs by ~50% or more.
- **Relays & bulk pricing:** use API relays that offer better per-token rates or private model hosting (Venice, private endpoints).
- **Aggressive caching & truncation:** cache LLM outputs, truncate long histories, and summarize instead of re-sending full context.

## Advanced API Proxy Features for Moltbot

### Model Routing by Task Type

You can inspect the request payload and dynamically route:

```
function selectModel(messages) {
  const systemPrompt = messages[0]?.content || "";
  if (systemPrompt.includes("shell") || systemPrompt.includes("automation")) {
    return "gpt-4.1";
  }
  return "gpt-4.1-mini";
}
```

This pattern reduces costs without sacrificing quality.

---

### Token and Cost Limits

You can enforce hard limits:

```
if (req.body.max_tokens > 2000) {
  return res.status(400).json({
    error: "Token limit exceeded"
  });
}
```

Some teams also track cumulative usage per Moltbot user ID.

---

## Is it Safe to Give an AI Shell Access to My Computer?

This is the most critical question for any Moltbot user. Giving an LLM the ability to run `rm -rf` is inherently risky. Moltbot includes several guardrails to mitigate this:

1. **Sandboxing**: You can run Moltbot inside a **Docker container**. This limits the agent's "world" to a specific folder, preventing it from touching your system files.
2. **Explicit Approval**: By default, "Main Sessions" (direct chats with you) have higher trust, but you can configure the bot to ask for permission before running any destructive shell commands.
3. **Password Protection**: If you expose the Moltbot Web UI, always enable password authentication in your `config.json`:

```
{
  "gateway": {
    "auth": {
      "mode": "password",
      "password": "YOUR_STRONG_SECURE_PASSWORD"
    }
  }
}
```

## Final Thoughts:

Moltbot is more than just a chatbot; it is the infrastructure for a **personal digital employee**. By hosting it yourself, you regain control over your data while gaining the productivity of an AI that never sleeps. Whether you use it to manage your calendar via Telegram or to automate your devops pipeline from your couch, Moltbot is a glimpse into a future where everyone has their own "Jarvis" running on a Mac Mini in the corner of the room.

If you want an API platform with multiple vendor models (such as [Chatgpt-5.2](https://www.cometapi.com/models/openai/gpt-5-2-pro/), [Claude opus 4.5](https://www.cometapi.com/models/anthropic/claude-opus-4-5-20251101/), etc.) that is priced lower than the official , then CometAPI is the best choice. , To begin, explore the model’s capabilities in the Playground and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/moltbot-clawdbot--setup-guide-api-hosting-tutorial/](https://www.cometapi.com/moltbot-clawdbot--setup-guide-api-hosting-tutorial/).*
