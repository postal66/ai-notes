<!-- social-ops-fingerprint:76c5c2cb42703e41a7523366f020de8fd8dd0cfe58aa45e1bdcb2debfbd83a86 -->
---
title: How to Build a MCP Server in Claude Desktop — a practical guide
---
# How to Build a MCP Server in Claude Desktop — a practical guide

![How to Build a MCP Server in Claude Desktop — a practical guide](https://resource.cometapi.com/blog/uploads/2025/11/How-to-Build-a-MCP-Server-in-Claude-Desktop-%E2%80%94-a-practical-guide-1.webp)

Since Anthropic’s public introduction of the **Model Context Protocol (MCP)** on **November 25, 2024**, MCP has moved quickly from concept to practical ecosystem: an open specification and multiple reference servers are available, community implementations (memory servers, filesystem access, web fetchers) are on GitHub and NPM, and MCP is already supported in clients such as **Claude for Desktop** and third-party tools. The protocol has evolved (the specification and server examples have been updated through 2025), and vendors and engineers are publishing patterns for safer, token-efficient integrations.

This article walks you through building an MCP server, connecting it to **Claude Desktop**, and practical / security / memory tips you’ll need in production.

## What is the Model Context Protocol (MCP)?

### A plain-English definition

The Model Context Protocol (MCP) is an **open, standardized protocol** that makes it straightforward for LLM hosts (the apps running the model, e.g., Claude Desktop) to call out to external services that expose *resources* (files, DB rows), *tools* (functions the model can invoke), and *prompts* (templates the model can use). Instead of implementing N×M integrations (every model to every tool), MCP provides a consistent client–server schema and a runtime contract so that any MCP-aware model host can use any MCP-compliant server—so developers can build services once and let any MCP-aware model or UI (e.g., Claude Desktop) use them.

### Why MCP matters now

Since Anthropic open-sourced MCP in late 2024, the protocol has rapidly become a de-facto interoperability layer for tool integrations (Claude, VS Code extensions, and other agent environments). MCP reduces duplicate work, speeds development of connectors (Google Drive, GitHub, Slack, etc.), and makes it easier to attach persistent memory stores to an assistant.

## What is the MCP architecture and how does it work?

At a high level, MCP defines three role groups and several interaction patterns.

### Core components: clients, servers, and the registry

- **MCP client (host):** The LLM host or application that wants contextual data—Claude Desktop, a VS Code agent, or a web app. The client discovers and connects to one or more MCP servers.
- **MCP server (resource provider):** A network service that exposes resources (files, memories, databases, actions) via the MCP schema. Servers declare their capabilities and provide endpoints the client can call.
- **Registry / Discovery:** Optional components or configuration files that help the client discover available MCP servers, list capabilities, and manage permissions or installation (desktop “extensions” are one UX layer for this).

### Message flows and capability negotiation

MCP interactions typically follow this pattern:

1. **Discovery / registration:** The client learns about available servers (local, network, or curated registries).
2. **Capability announcement:** The server shares a manifest describing resources, methods, and authorization requirements.
3. **Request / response:** The client issues structured requests (e.g., “read file X,” “search memories for Y,” or “create PR with these files”) and the server responds with typed contextual data.
4. **Action results & streaming:** Servers may stream results or provide long-running operation endpoints. The spec defines schemas for typed resource descriptors and responses.

### Security model and trust boundaries

MCP intentionally standardizes control surfaces so LLMs can act on user data and perform actions. That power requires careful security controls:

- **Explicit user consent / prompts** are recommended when servers can access private data or perform privileged actions (e.g., write to repos).
- **Least privilege manifests:** Servers should declare minimum scopes and clients should request only required capabilities.
- **Transport and auth:** Use TLS, tokenized credentials, and local-only endpoints for sensitive integrations. The community and platform vendors (e.g., Microsoft in Windows) are experimenting with registries and UI affordances to reduce risks.

---

## Why integrate Claude with MCP servers?

Integrating Claude with MCP servers unlocks three practical classes of capabilities:

### Real-time, actionable context

Instead of copying and embedding outdated snapshots into prompts, Claude can request up-to-date context (files, conversation history, DB rows) at query time. This means fewer approximate retrievals and fresher outputs. Anthropic’s demos show Claude doing things like creating GitHub PRs or reading local files via MCP.

### Small, composable tools rather than one giant adapter

You can write focused MCP servers—one for calendar, one for file system, one for a vector memory store—and reuse them across different Claude instances or clients (desktop, IDE, web). This modularity scales better than bespoke integrations.

### Persistent and standardized memory

MCP enables memory services: persistent stores that encode conversation history, personal preferences, and structured user state. Because MCP standardizes the resource model, multiple clients can reuse the same memory server and maintain a consistent user context across apps. Several community memory services and extension patterns already exist.

### Better UX and local control (Claude Desktop)

On desktop clients, MCP enables local servers with direct access to a user’s file system (with consent), making privacy-sensitive integrations feasible without cloud APIs. Anthropic’s Desktop Extensions are an example of simplifying installation and discovery of MCP servers on local machines.

## How to Create an MCP Server

### What you need before you start

1. **Claude Desktop**: Install the latest Claude Desktop release for your OS and ensure MCP/Extensions support is enabled in settings. Some features may require a paid plan (Claude Pro or equivalent).
2. **Developer machine**: Node.js (>=16/18 recommended), or Python 3.10+, plus ngrok or a local tunneling solution if you want to expose a local server to the internet for testing. Use TLS in production.
3. The MCP project provides SDKs and templates on the main docs and GitHub repo; install the Python or Node SDK via the official instructions in the docs/repo.

### Option A — Install an existing (example) MCP server

Anthropic provides example servers, including memory, filesystem, and tools.

Clone the reference servers:

```
git clone https://github.com/modelcontextprotocol/servers.git
cd servers
```

Inside, you will find folders such as:

```
filesystem/
fetch/
memory/
weather/
```

To install an example server:

```
cd memory
npm install
npm run dev
```

This starts the MCP server, usually at:

```
http://localhost:3000
```

Confirm the manifest endpoint works and that calling a tool returns properly typed JSON.

### Option B — Create your own MCP server (recommended for learning)

#### 1) Create a project folder

```
mkdir my-mcp-server
cd my-mcp-server
npm init -y
```

#### 2) Install the MCP server SDK

```
npm install @modelcontextprotocol/server
```

#### 3) Create a basic server file

Create `server.js`:

```
touch server.js
```

Paste the minimal MCP server implementation:

```
import { createServer } from "@modelcontextprotocol/server";

const server = createServer({
  name: "my-custom-server",
  version: "0.1.0",

  tools: [
    {
      name: "hello_world",
      description: "Returns a simple greeting",
      input_schema: {
        type: "object",
        properties: {
          name: { type: "string" }
        },
        required:
      },
      output_schema: {
        type: "object",
        properties: {
          message: { type: "string" }
        }
      },
      handler: async ({ name }) => {
        return { message: `Hello, ${name}!` };
      }
    }
  ]
});

server.listen(3000);
console.log("MCP server running on http://localhost:3000");
```

This is a **full MCP server** exposing a single tool: `hello_world`.

## How to connect Claude Desktop to an MCP server?

Below is a practical walkthrough for creating a simple MCP server and registering it with Claude Desktop. This section is hands-on: it covers environment setup, creating the server manifest, exposing endpoints the client expects, and configuring Claude Desktop to use the server.

### 1) Open the Claude Desktop developer connection area

In Claude Desktop: **Settings → Developer** (or **Settings → Connectors** depending on client build). There’s an option to add a remote/local MCP server or “Add connector.” The exact UI may change between releases—if you don’t see it, check the Desktop “Developer” menu or the latest release notes.

![MCP Server in Claude Desktop](https://resource.cometapi.com/blog/uploads/2025/11/1-claude-config-1024x761.webp)

### 2) If you are configuring a local server: Create or locate the configuration file

After launching the Claude desktop application, it automatically configures all found MCP servers into a file named ClaudeDesktopConfig.json. The first step is to locate and open this file, or create it if it doesn’t already exist:

For Windows users, the file is located under “%APPDATA%\Claude\claude\_desktop\_config.json”.

For Mac users, the file is located under “~/Library/Application Support/Claude/claude\_desktop\_config.json”.

### 3) Add the server to Claude Desktop

There are two UX patterns to let Claude Desktop know about your MCP server:

**Desktop Extensions / One-click installers**: Anthropic has documented “Desktop Extensions” which package manifests and installers so users can add servers via a one-click flow (recommended for broader distribution). You can package your manifest and server metadata for easy install.

**Local server registration (developer mode)**: For local testing:

- Place the manifest in a well-known local path or serve it at `https://localhost:PORT/.well-known/mcp-manifest.json`.
- In Claude Desktop settings, open the MCP/Extensions panel and choose “Add local server” or “Add server by URL,”and paste the manifest URL or token.
- Grant required permissions when the client prompts. Claude will enumerate server resources and present them as available tools/memories.

Now we choose to install the local MCP：**Add an `mcpServers` section** that lists your server name and an absolute path/command to start it. Save and restart Claude Desktop.

After restart, Claude’s UI will present the MCP tools (Search & Tools icon) and allow you to test the exposed operations (e.g., “What’s the weather in Sacramento?”). If the host doesn’t detect your server, consult the `mcp.log` files and `mcp-server-<name>.log` for STDERR output.

### 4)Test the integration

In Claude chat, type:

```
Call the hello_world tool with name="Alice"
```

Claude will invoke your MCP server and respond using the tool output.

## How do I implement a memory service over MCP (advanced tips)?

Memory services are among the most powerful MCP servers because they persist and surface user context across sessions. The following best practices and implementation tips reflect the spec, Claude docs, and community patterns.

### Memory data model and design

- **Structured vs. unstructured:** Store both structured facts (e.g., name, preference flags) and unstructured conversational chunks. Use typed metadata for fast filtering.
- **Chunking & embeddings:** Break long documents or conversations into semantically-cohesive chunks and store vector embeddings to support similarity search. This improves recall and reduces token usage during retrieval.
- **Recency & salience signals:** Record timestamps and salience scores; allow queries that favor recent or high-salience memories.
- **Privacy tags:** Tag items with sensitivity labels (private, shared, ephemeral) so the client can prompt for consent.

### API patterns for memory operations

Implement at least three operations:

- `write`: Accepts a memory item with metadata, returns acknowledgement and storage ID.
- `query`: Accepts a natural language query or structured filter and returns top-k matching memories (optionally with explainability metadata).
- `delete/update`: Support lifecycle operations and explicit user requests to forget.

Design responses to include provenance (where the memory came from) and a confidence/similarity score so the client and model can decide how aggressively to use the memory.

### Retrieval augmentation strategies for Claude

- **Short context windows:** Return concise memory snippets instead of full documents; let Claude request full context if required.
- **Summarization layer:** Optionally store a short summary of each memory to reduce tokens. Use incremental summarization on writes.
- **Controlled injection:** Provide memory as an attachable “context bundle” the client can inject selectively into prompts rather than flooding the model with everything.

### Safety & governance for memory MCPs

- **Consent and audit trail:** Record when a memory was created and whether the user consented to sharing it with the model. Present clear UI affordances in Claude Desktop for reviewing and revoking memories.
- **Rate limiting & validation:** Defend against prompt-injection or exfiltration by validating types and disallowing unexpected code execution requests from servers.
- **Encryption at rest and in transit:** Use strong encryption for stored items and TLS for all MCP endpoints. For cloud-backed stores, use envelope encryption or customer-managed keys if available.

## Conclusion: How to Build a MCP Server in Claude Desktop

The article is a compact, pragmatic recipe to go from zero → working Claude + memory server on your laptop:

- **Test a workflow:** ask Claude to “remember” a short fact and verify the server stored it; then ask Claude to recall that fact in a later prompt. Observe logs and tune retrieval ranking.
- **Install prerequisites:** Node.js >= 18, Git, Claude Desktop (latest).
- **Clone a reference server:** fork the `modelcontextprotocol/servers` examples or a community memory server on GitHub.
- **Install and run:** `npm install` → `npm run dev` (or follow the repo README). Confirm manifest endpoint (e.g., `http://localhost:3000/manifest`) returns JSON. ()
- **Register connector in Claude Desktop:** Settings → Developer / Connectors → Add connector → point to `http://localhost:3000` and approve scopes.

Integrating Claude (or any host) with MCP servers lets you build a connector once and have it available across MCP clients — Claude Desktop, IDEs, or other agent frameworks — which dramatically reduces maintenance and speeds feature parity across tools.

Developers can access claude AI’s latest API(as of the date of publication of this article) such as [Claude Sonnet 4.5 API](https://www.cometapi.com/claude-sonnet-4-5-api/) and [Claude Opus 4.1 API](https://www.cometapi.com/claude-opus-4-1-api/) through CometAPI, [the latest model version](https://www.cometapi.com/pricing/) is always updated with the official website. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-build-a-mcp-server-in-claude-desktop/](https://www.cometapi.com/how-to-build-a-mcp-server-in-claude-desktop/).*
