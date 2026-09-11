<!-- social-ops-fingerprint:75ef13626d5d6c417933449cd4440335d195742ab4bfdb8d096a2065850f7e8e -->
---
title: Create a MCP Server for Claude Code — a practical, up-to-step guide
---
# Create a MCP Server for Claude Code — a practical, up-to-step guide

![Create a MCP Server for Claude Code — a practical, up-to-step guide](https://resource.cometapi.com/blog/uploads/2025/11/Create-a-MCP-Server-for-Claude-Code-%E2%80%94-a-practical-up-to-step-guide.webp)

The Model Context Protocol (MCP) is an open standard that lets models like Anthropic’s *Claude* and developer tools like *Claude Code* call out to external tools, data sources and prompts in a safe, standard way.

This guide will walk you through building your own MCP server from scratch, enabling Claude Code to access custom features and thus greatly extend its functionality far beyond its built-in features.

## What is the Model Context Protocol (MCP)?

MCP (Model Context Protocol) is an **open specification** designed to standardize how language-model clients (like Claude, Claude Code, or other LLM frontends) connect to tool servers and data sources. Think of MCP as a “USB-C port for LLMs”: it defines a transport/JSON-RPC schema and a common way for servers to publish three kinds of capabilities:

- **Resources** — file-like or document data that a client can read (e.g., a database row, a text file, a JSON payload).
- **Tools** — callable functions that the model can ask the host to execute (with user approval).
- **Prompts** — reusable prompt templates or workflows the model/client can invoke.

MCP supports multiple transports (stdio, HTTP, SSE) and provides schema, SDKs and example servers so you don’t have to invent the wire format yourself. The protocol is maintained publicly (spec + SDKs) and has tutorials and a gallery of example servers to accelerate adoption.

## How is MCP architected?

MCP’s architecture is intentionally simple and modular: the core pieces are MCP **servers**, MCP **clients**, and **transports** that carry JSON-RPC framed messages between them. Below are the principal components you’ll interact with when building a server for Claude Code (or other MCP clients).

### Server, client and the protocol

- **MCP server** — A service that *publishes* tools, resources and prompts. Tools can perform side-effects or fetch data; resources surface read-only content; prompts are reusable prompt templates the client can ask the model to sample from.
- **MCP client (host)** — Typically part of the LLM host (e.g., Claude Code, VS Code plugin, a browser client). It discovers available servers, presents tool descriptions to the model, and routes model-initiated calls to servers.
- **Protocol** — Messages are encoded as JSON-RPC; the spec defines lifecycle events, tool discovery, invocation, completions/sampling, and how structured results are transported back to the client and model.

### Communication pattern (what happens when a tool is used)

1. Client sends user message to the model.
2. Model analyzes context and decides to call a tool exposed by MCP (or multiple tools).
3. Client forwards the tool call to the MCP server over the chosen transport.
4. Server executes the tool and returns results.
5. Model receives tool output and composes the final answer to the user.

### Implementation primitives

- **JSON-RPC** messages follow the MCP schema.
- **Tool definitions** are published in the server’s discovery responses so clients can present them in the UI.
- **Resources** are referenced by `@source:path` syntax by clients (e.g., `@postgres:...`), letting models refer to external content without inlining huge data into the prompt.

## Why integrate Claude Code with MCP servers?

Claude Code is Anthropic’s offering focused on code- and developer-centric workflows (editor/IDE integration, code understanding, etc.). Exposing your internal tools (source search, CI runner, ticket system, private registries) through MCP servers lets Claude Code call them as **first-class tools** inside coding conversations and agent flows.

Integrating Claude Code with MCP servers unlocks practical, production-relevant capabilities for a coding agent:

### 1. Let the model *act* on real systems

Claude Code can ask an MCP server to query issue trackers, run database queries, read large docs, or produce GitHub PRs — enabling end-to-end automation from within the coding session. This is explicitly supported by Claude Code docs (examples: querying Postgres, Sentry, or creating PRs).

### 2. Offload large data and specialized logic

Instead of embedding every data source into the prompt (which consumes tokens), you publish data and tools through MCP. The model calls the tool, gets a structured response, and reasons with it — this reduces token usage and lets servers handle heavy work (DB queries, long file reads, auth).

### 3. Security and governance

MCP centralizes access control and auditing at the server layer, letting organizations whitelist approved servers, control what tools are available, and limit outputs. Claude Code also supports enterprise MCP configuration and per-scope consent.

### 4. Reusability and ecosystem

MCP servers are reusable across clients and teams. Build once and many Claude/LLM clients can use the same services (or swap implementations).

## What do you need before you start?

### Minimum requirements

- A development machine with **Python 3.10+** (we’ll use Python in the example). Alternatively Node / other languages are supported by MCP SDKs.
- `uv` (Astral’s tool) or equivalent runner for running MCP stdio servers (the MCP tutorial uses `uv`). Installation steps shown below.
- Claude Code installed or access to Claude client (desktop or CLI) to register and test your server; or any MCP-capable client. Claude Code supports HTTP, SSE and local stdio servers.
- **Security note**: Only add trusted MCP servers to Claude Code in team or enterprise settings — MCP gives servers access to sensitive data, and prompt injection risks exist if a server returns malicious content.

## How to install and verify the Claude Code CLI

This is [Claude Code Installation and Usage Guide](https://apidoc.cometapi.com/claude-code-installation-and-usage-guide-1266358m0).

### 1) Quick summary — recommended install methods

Use the **native installer** (recommended) or Homebrew on macOS/Linux. NPM is available if you need a Node-based install. Windows gets PowerShell / CMD installers. Source: official Claude Code docs & GitHub.

---

### 2) Prerequisites

- macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows 10+ (WSL recommended on Windows).
- Node.js 18+ **only required** for the NPM install method.

---

### 3) Installation commands (pick one)

Native (recommended — no Node dependency)，macOS / Linux / WSL:

```
curl -fsSL https://claude.ai/install.sh | bash
# optional: install latest explicitly

curl -fsSL https://claude.ai/install.sh | bash -s latest
# or install a specific version

curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

Windows PowerShell:

```
irm https://claude.ai/install.ps1 | iex
# or for latest: & (::Create((irm https://claude.ai/install.ps1))) latest
```

(These are the official native installer scripts).

NPM (if you want a Node-based global install)：

```
# requires Node.js 18+

npm install -g @anthropic-ai/claude-code
```

**Do not** use `sudo npm install -g` — warn against sudo global installs (permission/security issues). If you hit permission errors, use `nvm` or fix your npm global prefix rather than using sudo.

### 4) Verify the binary was installed (basic checks)

Run these locally immediately after installation:

```
# is the command on PATH?

which claude

# version (or -v)

claude --version
# or

claude -v

# help (sanity check)

claude --help
```

Expected: `which` shows a path (e.g. `/usr/local/bin/claude` or `~/.nvm/.../bin/claude`) and `claude --version` prints a semver-like string. The docs and README both show `claude` as the primary CLI entrypoint.

---

### 5) Verify install health and configuration (recommended checks)

#### a) `claude doctor`，Run:

```
claude doctor
```

This built-in diagnostic checks your install type, common problems (like npm permission issues), dependencies such as `ripgrep`, and suggests fixes. The docs explicitly recommend running `claude doctor` after install.

#### b) Run a smoke test (non-interactive)

From your project directory:

```
cd /path/to/your/project
claude -p "Explain this project in 3 sentences"
```

This uses **print** mode (`-p`) to send a single prompt then exit; good for CI or quick functional checks.

#### c) Authentication verification (make sure the CLI can reach Anthropic)

Claude Code supports several auth flows (Console OAuth, API key, provider integrations). Common checks:

1. **If using an API key (CI / headless / local env var)**:

```
export ANTHROPIC_API_KEY="sk-..."
# then

claude auth status
claude auth whoami    # or `claude auth whoami` / `claude whoami` depending on version
```

You can use [CometAPI](https://www.cometapi.com/)‘s API key to use Claude Code, Using Claude’s API through CometAPI will give you a 20% discount.

2. **If you used OAuth via the console** — run:

```
claude auth status
claude auth whoami
```

You should see account/plan info or a confirmation that you’re authenticated.

## Step-by-step environment preparation

Below are concrete steps to prepare two common developer stacks (TypeScript and Python), followed by quick checks to ensure everything works.

### H3 — A. TypeScript / Node setup (fastest path)

1. Create project and install SDK:

```
mkdir mcp-demo && cd mcp-demo
npm init -y
npm install @modelcontextprotocol/sdk express zod
npm install --save-dev typescript tsx @types/node @types/express
```

2. Create `server.ts`. (We provide a full example in the “How to Quickly Build…” section.)
3. Run:

```
npx -y tsx server.ts
```

4. Test locally with the **MCP Inspector** or add to Claude Code:

```
npx @modelcontextprotocol/inspector
# or (for Claude Code)

claude mcp add --transport http my-server http://localhost:3000/mcp
```

(Inspector and Claude commands let you validate discovery and invoke tools.)

## How to quickly build an MCP server for Claude Code?

### quick checklist

1.Start your server (Streamable HTTP recommended): `node server.ts` or `uvicorn server:app`.

2. From your dev machine, either:

- Use **MCP Inspector** to validate (`npx @modelcontextprotocol/inspector`) and confirm `tools/list` and `resources/list`; or
- Add the server to Claude Code: `claude mcp add --transport http <name> http://<host>:<port>/mcp` (or follow the web UI flows if your client supports remote MCP).

If you plan to use Anthropic’s Messages API connector for remote MCP (no separate client), read the Claude docs — a beta header may be required (check the docs for the exact header and current support status).

Below are two complete but compact server examples you can copy, run, and connect to Claude Code (or the MCP Inspector). The TypeScript example uses Express + the TypeScript SDK; the Python example demonstrates a FastAPI mounting.

> Note: the code below follows the public SDK examples and is intentionally minimal for clarity. For production, add authentication, logging, rate limiting and input validation beyond the SDK defaults.

---

### Example 1: TypeScript + Express (Streamable HTTP)

Create `server.ts` (complete):

```
// server.ts
import express from "express";
import * as z from "zod/v4";
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";

const server = new McpServer({ name: "claude-code-demo", version: "0.1.0" });

// Register a simple tool: add two numbers
server.registerTool(
  "add",
  {
    title: "Add",
    description: "Add two numbers a and b",
    inputSchema: { a: z.number(), b: z.number() },
    outputSchema: { result: z.number() }
  },
  async ({ a, b }) => {
    const output = { result: a + b };
    return {
      content: ,
      structuredContent: output
    };
  }
);

// Register a resource: greet user (dynamic)
server.registerResource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  { title: "Greeting", description: "Return a greeting for the name" },
  async (uri, params) => {
    return {
      contents:
    };
  }
);

// Express + Streamable HTTP transport
const app = express();
app.use(express.json());

app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({ enableJsonResponse: true });
  // Close transport when connection closes
  res.on("close", () => transport.close());
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});

const port = parseInt(process.env.PORT || "3000", 10);
app.listen(port, () => console.log(`MCP server listening: http://localhost:${port}/mcp`));
```

Run:

```
npm install
npx -y tsx server.ts
```

Then connect in Claude Code (example):

```
# Add the remote server to your Claude Code MCP list (local dev)

claude mcp add --transport http my-demo http://localhost:3000/mcp
```

This example is adapted from the official TypeScript SDK Quick Start and demonstrates how to register tools and resources, then expose them over Streamable HTTP.

---

### Example 2: Python + FastAPI (FastMCP + Streamable HTTP)

Create `server.py` (complete):

```
# server.py

from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()
mcp = FastMCP("claude-python-demo", stateless_http=True)

# tool: simple sum

@mcp.tool()
def add(a: int, b: int) -> dict:
    """Add two integers"""
    return {"result": a + b}

# resource: simple greeting resource template

@mcp.resource("greeting://{name}")
def greeting(name: str):
    return {"contents": }

# mount the streamable-http MCP endpoint (FastMCP exposes an ASGI app)

app.mount("/mcp", mcp.streamable_http_app())

# optional endpoint to demonstrate other API routes

@app.get("/")
async def root():
    return {"status": "OK"}
```

Run:

```
uvicorn server:app --reload --port 8000
```

Connect with the Inspector:

```
npx @modelcontextprotocol/inspector
# In Inspector select Streamable HTTP and enter http://localhost:8000/mcp
```

Python SDK examples and FastMCP utilities make it straightforward to register `@mcp.tool()` and `@mcp.resource()` decorated functions that the LLM can discover and call.

---

## How does Claude Code actually call your tools?

When an LLM decides to use a tool, the client sends a JSON-RPC invocation to the MCP server. The server executes the requested tool (for example, queries a DB, runs tests, or calls an external API) and returns **structured content** and **presentable content**. The client (Claude Code) can then include the structured output in the model’s context so the model can continue reasoning with that reliable data — not just the server’s textual output. The TypeScript SDK supports registering `inputSchema` and `outputSchema` (zod) so arguments and outputs are validated and machine-typed.

---

## What testing and debugging tools should you use?

### MCP Inspector

The **MCP Inspector** is the official visual developer tool for testing MCP servers. It allows you to connect to a server (stdio, SSE, or streamable-HTTP), list tools, invoke them manually, and inspect the lifecycle of JSON-RPC messages — invaluable during development. Start it via `npx @modelcontextprotocol/inspector`.

### Local vs Remote testing

- **Local (stdio)** — quick iteration cycle for desktop apps and offline debugging.
- **Streamable HTTP** — test with the Inspector or connect to Claude Code using the `claude mcp add` CLI or the MCP connector in Messages API for remote tests. Make sure to supply any auth headers required for your server.

## Conclusion

MCP is the practical bridge between modern LLMs and the systems that actually hold the data and perform actions. For code workflows, integrating Claude Code with an MCP server gives the model structured, auditable access to repositories, CI, issue trackers, and custom tooling—resulting in more precise automation and safer side-effects. With official SDKs in TypeScript and Python, Streamable HTTP for remote hosting, and tools like the MCP Inspector, you can build a minimal server in minutes and iterate toward a production deployment.

Developers can access [Claude Sonnet 4.5 API](https://www.cometapi.com/claude-sonnet-4-5-api/) and [Claude Opus 4.1 API](https://www.cometapi.com/claude-opus-4-1-api/) etc through CometAPI, [the latest model version](https://www.cometapi.com/pricing/) is always updated with the official website. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/create-a-mcp-server-for-claude-code/](https://www.cometapi.com/create-a-mcp-server-for-claude-code/).*
