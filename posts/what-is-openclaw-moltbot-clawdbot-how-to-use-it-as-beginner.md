<!-- social-ops-fingerprint:c4d56941fb7e9ea410900040318bf289b2db9f6dc91a7dc31adb34aace0c88a9 -->
---
title: What is Openclaw (Moltbot / Clawdbot)?  how to use it as beginner?
---
# What is Openclaw (Moltbot / Clawdbot)?  how to use it as beginner?

![What is Openclaw (Moltbot / Clawdbot)?  how to use it as beginner?](https://resource.cometapi.com/Clawdbot.webp)

The landscape of Artificial Intelligence is shifting rapidly from passive "chatbots" that answer questions to active "agents" that perform tasks. At the forefront of this revolution is **Clawdbot** (often stylized with the lobster emoji 🦞), an open-source tool that has taken the developer community by storm. Unlike traditional AI tools confined to a browser tab, Clawdbot acts as a locally deployed operator that lives in your messaging apps and controls your computer to execute real-world workflows.

This guide provides an in-depth look at Clawdbot, covering its architecture, installation, configuration, and advanced usage to help you transform your daily productivity.

### What makes it different from a chatbot?

Unlike single-session chatbots, Clawdbot is built to be persistent and *procedural*: it stores long-lived state, loads skills selectively, executes scripts on your machine (with configured permissions), and is designed to act autonomously when triggered by schedules, webhooks, or messages. That design opens new workflows, but also increases the need for operational controls and proper isolation.

## What Is Clawdbot and Why Is It Revolutionizing AI Assistance?

**Clawdbot** is an open-source, local-first AI automation framework designed to function as a "private execution assistant" rather than a simple conversationalist. While tools like ChatGPT or standard Claude allow you to chat with an AI, they are typically "sandboxed," meaning they cannot touch your files, manage your local network, or execute code on your machine without specific, limited environments.

### The Core Philosophy: "Execution Over Conversation"

Clawdbot bridges the gap between high-level reasoning (provided by Large Language Models like Anthropic’s Claude 3.5 Sonnet or local Ollama models) and low-level system operations. It runs as a daemon (background service) on your hardware—often a Mac Mini, Raspberry Pi, or a local server—and connects to your preferred messaging platforms like Telegram, WhatsApp, Discord, or Slack.

### Key Differentiators

1. **Local Sovereignty:** Clawdbot runs on your infrastructure. Your data, memories, and logs are stored locally, often in simple Markdown formats, ensuring that you maintain ownership of your digital footprint.
2. **Agentic Behavior:** It doesn’t just wait for prompts. Clawdbot can be configured to be proactive—sending you morning briefings, monitoring server statuses, or reminding you of deadlines without you initiating the conversation.
3. **Universal Interface:** Instead of requiring a dedicated app, it meets you where you already are. You text your AI assistant in the same WhatsApp or Telegram thread where you message your friends.

## What Are the Core Features of Clawdbot?

Clawdbot is packed with features that cater to power users, developers, and productivity enthusiasts.

### 1. Multi-Platform Connectivity

Clawdbot acts as a central brain that can speak through multiple "mouths." It supports a wide array of messaging protocols, allowing you to switch devices seamlessly.

- **Supported Platforms:** Telegram, WhatsApp, Discord, Slack, Signal, and iMessage.
- **Unified Context:** A conversation started on Telegram can be referenced later via Slack if configured to share the same memory context.

### 2. Deep System Integration

Unlike cloud agents, Clawdbot has (permissioned) access to your local environment.

- **File System Access:** It can read, write, and organize files on your hard drive.
- **Shell Execution:** It can run terminal commands (e.g., `git pull`, `npm install`, system updates).
- **Browser Control:** It can automate web interactions, such as filling out forms or scraping data.

### 3. Self-Evolution and Dynamic Skills

One of the most futuristic features of Clawdbot is its ability to "self-improve." You can instruct it to write a new "skill" or plugin for itself. For example, if you want it to check the weather but it lacks a weather plugin, you can ask it to write a Python or Node.js script to query a weather API, and it will integrate that capability immediately.

### 4. Long-Term Memory

Clawdbot utilizes a persistent memory architecture. It creates a "knowledge graph" of sorts by storing interaction history and user preferences in local files. This means it remembers that you prefer Python over JavaScript or that your meetings are usually on Tuesdays, without needing to be reminded in every session.

## How does Clawdbot work?

### Architectural overview

At a high level, Clawdbot has three interacting layers:

1. **Gateway / Control Plane:** A network-facing service that routes messages from chat platforms to your agent instance(s) and manages authentication and configuration.
2. **Agent (assistant) runtime:** The process that maintains state, executes skills, talks to LLMs (local or cloud), and performs actions.
3. **Channels & Skills:** Connectors for messaging channels (WhatsApp, Telegram, iMessage, Slack, Discord, etc.) and skill plugins that implement concrete capabilities (send email, manage calendar, GitHub ops, home automation).

### Flow of a typical interaction

1. A message arrives on a channel (e.g., you message your Clawdbot on Telegram).
2. The gateway authenticates and forwards the message to the agent.
3. The agent processes the message (optionally uses an LLM or rule engine), decides whether to respond or perform an action (e.g., send an email or trigger a script), and then replies or triggers the configured integration.
4. The agent logs the action and can notify you proactively if the task finishes or if a follow-up is needed.

### LLM and tooling integration

Clawdbot is model-agnostic: it sends prompts and tool invocation requests to whichever LLM API you configure in `.env` (OpenAI, Anthropic, Google, etc.). The agent’s reasoning and step planning come from the LLM responses, but the agent executes concrete steps locally or via configured APIs (for example, calling your SMTP server, invoking a shell script, or calling a cloud API). Because the “brains” are external LLMs but the execution plane resides on your device, operators must manage API keys and local permission boundaries carefully.

## How Do You Install and Configuration Clawdbot?

Installation requires basic familiarity with the command line (Terminal).

 The recommended setup is on a machine that stays on 24/7, like a Mac Mini or a Raspberry Pi 5.

### Prerequisites

- **Node.js:** Version 18 or higher.
- **API Key:** An Anthropic API key (if using Claude) or OpenAI key.
- **Messaging Bot Token:** E.g., a Telegram Bot Token from `@BotFather`.

### Step 1: Installation via NPM

The easiest way to install Clawdbot is using `npm` (Node Package Manager).

bash

```
# [...](asc_slot://start-slot-41)Open your terminal and run:
npm install -g clawdbot@latest

# Verify installation
clawdbot --version
```

### Step 2: The Onboarding Wizard

Clawdbot comes with an interactive wizard that simplifies the complex configuration process.

```
bash
clawdbot onboard --install-daemon
```

**During the onboarding, you will be asked:**

1. **Gateway Mode:** Choose `Local` for personal use.
2. **Authentication:** Enter your Anthropic or OpenAI API Key.
3. **Model Selection:** Select `Claude 3.5 Sonnet` for the best balance of speed and capability.
4. **Channel Setup:** Select your primary chat app (e.g., Telegram). You will need to paste your Bot Token here.
5. **Daemon Setup:** Selecting `yes` ensures Clawdbot restarts automatically if your computer reboots.

### Step 3: Manual Configuration (Optional)

For advanced users, you can directly edit the configuration file, typically located at `~/.clawdbot/clawdbot.json`.

**Example Configuration (`clawdbot.json`):**

JSON

```
{
  "system": {
    "timezone": "America/New_York",
    "name": "Jarvis"
  },
  "llm": {
    "provider": "anthropic",
    "model": "claude-3-5-sonnet-20240620",
    "apiKey": "sk-ant-..."
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "123456789:ABCdefGHIjklMNOpqrsTUVwxyz",
      "allowedUsers": ["your_telegram_username"]
    },
    "whatsapp": {
      "enabled": false
    }
  },
  "permissions": {
    "fileSystem": true,
    "shell": true,
    "browser": false
  }
}
```

### Step 4: Starting the Gateway

If you didn't install the daemon, you can start the bot manually:

bash

```
clawdbot gateway --port 18789 --verbose
```

Once running, you should see logs indicating a successful connection to your messaging platform.

## How Can You Master ClawdBot AI with Best Practices?

Once installed, interacting with Clawdbot is as simple as sending a text. However, to get the most out of it while maintaining security, follow these guidelines.

### Basic Usage Commands

You speak to Clawdbot in natural language, but understanding its capabilities helps.

| Intent | Example Command |
| --- | --- |
| File Management | "Find all PDF files created last week and move them to the 'Archive' folder." |
| Web Research | "Search for the latest news on Quantum Computing and write a summary." |
| Coding | "Read the main.py file in the current directory and fix the syntax error on line 40." |
| Scheduling | "Check my Google Calendar for free slots on Tuesday afternoon." |

### What is a simple “skill” and how do I write one?

A Clawdbot skill is a folder that contains a `SKILL.md` file with YAML frontmatter (metadata: `name`, `description`, `triggers`) and a body that describes the procedure, plus optional `scripts/` that do the heavy lifting. This pattern is AgentSkills-compatible and similar to Claude/Agent skill patterns. Here is an example minimal skill that outlines sending a templated email (this is illustrative — adapt scripts to your environment):

**Directory**

```
my-email-skill/
  SKILL.md
  scripts/
    send_email.py
```

**`SKILL.md`**

```
---
name: send-email
description: Send a templated email from the local SMTP server.
triggers:
  - "send an email"
  - "email to"
---

# Send Email Skill

When the user asks to send an email, gather `to`, `subject`, and `body`.
Run `scripts/send_email.py` with these args and report result.
```

**`scripts/send_email.py` (Python, minimal)**

```
#!/usr/bin/env python3
import sys, smtplib
from email.message import EmailMessage

to = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3]

msg = EmailMessage()
msg["From"] = "you@example.com"
msg["To"] = to
msg["Subject"] = subject
msg.set_content(body)

# NOTE: configure SMTP credentials beforehand in a secure store
with smtplib.SMTP("localhost") as s:
    s.send_message(msg)
print("sent")
```

Clawdbot will call the script when the agent decides the skill is needed. Skills can be much more advanced (run tests, call remote APIs, manipulate files, etc.). The public skill registry (ClawdHub) contains many community skills you can inspect.

### Security Best Practices

Giving an AI shell access to your computer carries risks.

1. **Limit Permissions:** In your `clawdbot.json`, set `shell: false` if you do not strictly need terminal access. Only enable it when performing development tasks.
2. **Sandboxing:** When asking Clawdbot to write code, ask it to output the code for review rather than executing it blindly ("Write a script to delete old files, but show me the code first").
3. **Network Isolation:** If running on a server, use a firewall to restrict incoming traffic to the Gateway port only from localhost or trusted IPs.
4. **Use "Loopback" Mode:** Ensure the Gateway binds to `127.0.0.1` (localhost) so it isn't exposed to the public internet, unless you are using a secure tunnel like Cloudflare Tunnel or Tailscale.

### Optimizing Costs

**Context Management:** Clawdbot sends conversation history to the LLM. Periodically clear the context (often a command like `/clear` or "Forget previous context") to prevent token usage from bloating.

**Model Selection:** Use "Haiku" or "Flash" models for simple tasks (summaries, categorization) and "Opus" or "Sonnet" for complex coding or reasoning.

## How does the CometAPI API help Clawdbot?

Clawdbot connects with CometAPI by utilizing [CometAPI](https://www.cometapi.com/)’s **OpenAI-compatible endpoint**. Since Clawdbot allows you to define custom LLM (Large Language Model) providers, you can effectively swap out the default "brain" (like Anthropic or OpenAI) with CometAPI.

This connection transforms Clawdbot from a single-model assistant into a multi-model powerhouse, giving it access to the 500+ models aggregated by CometAPI.

In other words:

> **Clawdbot treats CometAPI as an LLM provider endpoint**, just like OpenAI or Anthropic.

CometAPI acts as a **unified LLM gateway**, while Clawdbot acts as the **agent runtime** that sends prompts, tool calls, and reasoning requests to that gateway.

### How does Clawdbot technically connect to CometAPI?

Clawdbot uses environment variables to configure its LLM backend. To connect CometAPI, you configure:

1. **API base URL**
2. **API key**
3. **Model name (mapped to CometAPI’s supported models)**

#### Example `.env` configuration

```
# Tell Clawdbot to use an OpenAI-compatible provider
LLM_PROVIDER=openai

# CometAPI endpoint
OPENAI_API_BASE=https://api.cometapi.com/v1

# Your CometAPI key
OPENAI_API_KEY=cmpt-xxxxxxxxxxxxxxxx

# Model routed by CometAPI
OPENAI_MODEL=gpt-4o-mini
```

Because CometAPI follows the OpenAI-compatible schema, **no code changes inside Clawdbot are required**. The agent simply sends requests to CometAPI instead of OpenAI.

### Why use **Clawdbot + CometAPI**

**Clawdbot + CometAPI is a natural fit**:

- Clawdbot provides the **agent, skills, memory, and execution**
- CometAPI provides the **LLM abstraction, routing, reliability, and cost control**

Together, they form a **production-ready autonomous AI stack**:

> **Clawdbot thinks and acts — CometAPI decides which brain to use.**

### Summary Table

| Feature | Without CometAPI | With CometAPI |
| --- | --- | --- |
| Model Selection | Locked to one vendor (e.g., only Anthropic) | Access to 500+ models (OpenAI, Google, Meta, etc.) |
| Reliability | Susceptible to single-vendor outages | High availability via aggregated routing |
| Configuration | Requires re-auth for every new provider | One API Key for everything |
| Cost Control | Fixed vendor pricing | Ability to route to cheapest effective model |

## 5 Top Use Cases for Clawdbot?

Clawdbot shines in scenarios where context switching between apps kills productivity.

### 1. The "DevOps" Assistant

Developers use Clawdbot to manage deployments without leaving Slack or Discord.

- **Scenario:** You receive a server alert while at dinner.
- **Action:** You text Clawdbot: "Check the logs for the Nginx service on the production server."
- **Result:** Clawdbot SSHs into the server (if configured), runs `tail -f /var/log/nginx/error.log`, and pastes the last 20 lines into your chat.

### 2. Intelligent Email Triage

Connect Clawdbot to your Gmail API.

- **Scenario:** You have 500 unread emails.
- **Action:** "Scan my inbox for urgent emails from 'Client X' and summarize any action items."
- **Result:** It parses the JSON/XML of your inbox, filters by sender, reads the bodies, and sends you a bulleted list of tasks.

### 3. Personal Learning & Research

Clawdbot can be a research companion that builds a knowledge base.

- **Scenario:** You are learning Rust.
- **Action:** "Create a learning plan for Rust. Every morning at 8 AM, send me a small coding exercise."
- **Result:** It sets up a cron job (Proactive Automation) to message you daily with content it retrieves or generates.

### 4. Smart Home Orchestrator

By integrating with Home Assistant APIs, Clawdbot becomes a natural language interface for your home.

- **Scenario:** "I'm heading home."
- **Action:** Clawdbot triggers a script to set the thermostat to 72°F and turn on the living room lights.

### 5. Automated Content Creation

For content creators (like users of CometAPI), Clawdbot can streamline the drafting process.

- **Scenario:** "Monitor TechCrunch for news about 'LLM Pricing'. If a new article appears, draft a 500-word blog post in markdown format."
- **Result:** It acts as a 24/7 news watchdog and drafter, saving hours of manual checking.

## Conclusion

Clawdbot represents a significant leap forward in personal AI computing. By decoupling the AI from the browser and embedding it into the operating system and messaging layers, it empowers users to automate the mundane and focus on the creative. While it requires a technical setup and a mindful approach to security, the productivity gains of having a 24/7, proactive, and context-aware assistant are unparalleled in the current market.

Whether you are a developer looking to automate git workflows or a power user managing a complex digital life, Clawdbot offers the framework to build your ultimate digital sidekick.

If you want an API platform with multiple vendor models (such as OpenAI, Chatgpt, Claude, etc.) that is priced lower than the official , then CometAPI is the best choice. , To begin, explore the model’s capabilities in the Playground and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/clawdbot-getting-started-guide-what-it-is-and-how-to-use/](https://www.cometapi.com/clawdbot-getting-started-guide-what-it-is-and-how-to-use/).*
