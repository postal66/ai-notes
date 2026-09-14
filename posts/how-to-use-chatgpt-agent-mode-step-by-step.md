<!-- social-ops-fingerprint:9d5cb1edecdb652ba3b3e0d6faaf5fa22ab34e92ba0b21455a2319d2912ec3cd -->
---
title: How to use ChatGPT agent mode step by step
---
# How to use ChatGPT agent mode step by step

![How to use ChatGPT agent mode step by step](https://resource.cometapi.com/blog/uploads/2025/10/unnamed-file.png)

In mid-2025 OpenAI released *ChatGPT agent mode* — a capability that lets ChatGPT not just answer, but plan and carry out multi-step tasks using a virtual workspace (browsing, file manipulation, code execution and connector APIs). ChatGPT **Agent Mode** moves ChatGPT from a passive assistant that *tells you what to do* into an active assistant that can *do the steps for you* — browse, extract, fill forms, run code, create files, and interact with connected services under your supervision.

## What is ChatGPT Agent Mode?

Agent Mode turns ChatGPT from a reactive chat assistant into an *autonomous digital worker* that can plan and execute multi-step workflows. Unlike a single back-and-forth completion, an agent can:

- open and read web pages, follow links, and extract structured facts;
- run code in a sandbox or virtual desktop environment to process files, transform spreadsheets or generate documents;
- call connected APIs or services you configure (connectors) to read or write data;
- ask clarifying questions when the objective or constraints are ambiguous; and
- keep state across steps so a long task (research → draft → export) proceeds without re-telling the whole story each time.

OpenAI positions agent mode as “bridging research and action”: it is intended for iterative collaborative workflows where human oversight remains important — you give objectives, constraints, and approvals while the agent performs the heavy lifting.

### How did ChatGPT Agent Mode evolve?

Agent Mode builds on earlier OpenAI features (e.g., Operator and Deep Research) and the company’s Agents SDK / Responses API. The Agents SDK gives developers primitives to create custom agents and tools, while the ChatGPT Agent Mode packages similar capabilities in the consumer web and app interface so non-developers can create autonomous workflows without writing glue code. The system architecture includes guardrails such as request confirmations and “watch mode” when agents operate in sensitive contexts.

> Note: other vendors (notably Microsoft) are also shipping their own “Agent Mode” or Office Agent features that embed agentic behavior into productivity apps (Excel/Word/Copilot). These are separate implementations but reflect the same industry trend toward agentic AI in tools.

## What can ChatGPT Agent Mode do?

### Which actions are typical?

Agent Mode capabilities include:

- Autonomous web browsing and research (open pages, click, read, summarize).
- Data extraction and structured outputs (tables, CSVs, sheets).
- File authoring: generate and save documents, slides, spreadsheets.
- Form filling and submission (with explicit confirmation).
- Running code or orchestrating tool chains through SDKs or connectors.
- Integrating with services (email, calendars, GitHub, Zapier/Make) where permitted by connectors.
- Commerce/transactions in supported workflows (e.g., “Instant Checkout” integrations).

### Limitations to expect

Agent Mode is powerful but not omniscient: it respects sandbox limits, may hit tool or connector rate limits, and generally avoids risky actions without explicit confirmation. Expect failure modes in authentication flows, JavaScript-heavy sites, CAPTCHA-protected actions, or systems requiring multi-factor authentication.

## Who can access ChatGPT Agent Mode — and how does one get it?

### Who gets access?

OpenAI’s rollout targets paid plans: ChatGPT Agent Mode has been released to Plus/Pro/Team/Business users (and similar tiers where offered) with tiered quotas; it is not available on the free tier.

### How do you enable it (step-by-step)?

1. Sign in to ChatGPT with a qualified plan.
2. Start a new chat or open an existing one.
3. Open the **Tools** menu (the “+” in the composer) and select **Agent mode**, or type the `/agent` command in the message box to start an agent session.
4. Describe the task you want done. The agent will propose a plan and begin executing; it will pause to ask for confirmation before consequential actions. You can interrupt or take manual control at any time.

### Who should consider Agent Mode?

- **Knowledge workers and teams** who want to automate repetitive digital tasks (analysts, product managers, educators).
- **Developers and integrators** who want to prototype agentic workflows quickly via the Agents SDK or Responses API.
- **IT/security teams** evaluating autonomous workflows should pilot carefully due to data access and privacy considerations.

## How to get and set up a ChatGPT Agent

Below is a practical, step-by-step setup workflow you can follow in the ChatGPT web or mobile UI (based on OpenAI’s docs and published walkthroughs). Adjust steps for your org’s policies and the specific UI you see.

### Step 1: Confirm access and billing tier

Sign into your ChatGPT account and confirm you are on a plan that supports agents (Plus/Pro/Business/Enterprise). If you’re an admin, confirm organization-level switches and connector policies.

### Step 2: Create a new agent (UI)

1. From the ChatGPT home, look for **“Create agent”** or **“Agent Mode”** in the tools/menu.
2. Choose a base model (where applicable) and name your agent (e.g., “Competitive Researcher”).
3. Select allowed connectors and scopes carefully (Google Drive, Gmail, Slack, your CRM). Restrict permissions to the minimum required.

### Step 3: Provide identity, goals, and constraints

1. Give the agent a concise **mission statement** (goal), input sources, and non-functional constraints (max runtime, file formats, budget limits, whether it can send emails or only draft them).
2. Upload example files or links the agent should use. This creates context it can reference during execution.

### Step 4: Authorize connectors and test in sandbox

1. Authorize any connectors you need (Drive, GitHub). OpenAI will ask you to sign in and grant explicit scopes — review those scopes carefully.
2. Run a *small, harmless test job* (e.g., “Summarize these three documents and list 5 action items”) to confirm the agent can access and process the resources you allowed.

### Step 5: Set approval hooks and notifications

1. Configure human approval checkpoints for high-risk actions (e.g., “ask me before writing to CRM”).
2. Set output destinations (download, email draft, or deliver as a chat message).

### Step 6: Iterate and harden

Review runs, examine logs/audit trails, and tighten constraints or remove connectors if you see unexpected behavior. Maintain a run history for auditing.

> Tools → **Agent mode** (or `/agent`)

## How do we write a “runbook” prompt

### Runbook prompt principles

A “runbook” prompt is a structured instruction set that defines goals, constraints, success criteria, outputs, and error handling for an agent. To make it reliable, follow these principles:

- **Be explicit about the goal:** define the deliverable and format (e.g., “Create a 10-slide PowerPoint with title slide, 3 slides of competitor financials, method slide, and a summary slide”).
- **Define inputs and sources:** list trusted websites, file locations, or connectors the agent should prefer, plus prohibited sources.
- **Set constraints and safety checks:** e.g., “Never send emails without my explicit confirmation,” “Don’t log in to bank portals,” or “If fewer than 3 independent sources corroborate a claim, flag it instead of reporting as fact.”
- **Include stepwise checkpoints:** tell the agent when to pause for confirmation (e.g., before publishing or performing irreversible actions).
- **Specify error handling and rollbacks:** e.g., “If a page returns 403, try cached results; if unavailable, note the failure and continue with other sources.”

### Example runbook (concise)

**Mission:** Produce a competitive landscape brief for Product X.

**Inputs:** URLs A, B, C; spreadsheet `pricing.xlsx` in `/shared/Competitive`.

**Constraints:** Use only public pages and the supplied spreadsheet; do not use any credentials; finish in under 20 agent messages; produce a 2-page PDF + CSV with feature table.

**Steps:**

1. Crawl URLs A, B, C; extract product names, price tiers, and top 5 features.
2. Merge extracted features with `pricing.xlsx`, normalizing columns to `vendor, plan, monthly_usd, key_features`.
3. Create a 700-word executive summary (max 5 bullet recommendations).
4. Create `competitive_table.csv` and `brief.pdf`.
   **Decision rule:** If any site is paywalled or requires login, stop and ask for approval.
   **Output format:** `brief.pdf` (2 pages, A4), `competitive_table.csv` with columns as above, and a short chat message confirming job completion.

### Tip: Be explicit about failure modes

Tell the agent what to do if a step fails (stop and report; skip and continue; try alternative source). Agents interpret ambiguous instructions literally—explicit failure rules reduce surprises.

## Real-life examples and code reference

### Example 1 — Email triage (end user)

**Task:** “Scan my last 100 unread emails and summarize high-priority messages requiring a reply; suggest draft replies for those that can be handled automatically.”
**How the agent works:** agent reads inbox via authenticated connector, extracts sender, subject, urgency signals, and drafts replies in the requested style. It will *not* send messages without explicit confirmation and will present a list of suggested replies for review. (User tests recommend limiting initial runs to small batches.)

### Example 2 — Data cleaning & export (analyst)

**Task:** “Clean this CSV, remove duplicates, normalize phone numbers to E.164, and output a cleaned CSV and summary of records changed.”
**How the agent works:** agent uses the file access tool, executes deterministic transformations, writes back the cleaned file to Drive, and returns a change log.

### Developer code reference (Python + Agents SDK)

Below is a **conceptual** Python snippet based on the OpenAI Agents SDK and Responses API patterns — it demonstrates creating an agent programmatically and invoking it. (Adapt parameters to match the SDK or client library you use; check the SDK docs for exact method names and authentication flow.)

```
# conceptual example — adapt to the exact SDK you install

from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")

agent_spec = {
    "name": "CompetitorResearchAgent",
    "instructions": "Produce a 10-slide competitor analysis deck using sources A,B,C. Pause for confirmation before any email or purchase.",
    "tools": ,
    "config": {"watch_mode": True, "confirm_before_send": True}
}

# create agent (SDK-specific API)

agent = client.agents.create(agent_spec)

# run the agent on a specific task

task = {"prompt": "Create the 10-slide competitor analysis deck and upload to Drive:/AgentOutputs"}
run = client.agents.run(agent_id=agent, task=task)

print("Run started:", run)
```

### JavaScript (conceptual)

```
import OpenAI from "openai";
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const agentSpec = { /* same fields as above */ };

async function createAndRun() {
  const agent = await client.agents.create(agentSpec);
  const run = await client.agents.run(agent.id, { prompt: "Create the 10-slide deck" });
  console.log("Run ID:", run.id);
}
```

> Note: the exact client methods, names, and SDK packaging evolve — consult the OpenAI Agents SDK and platform docs for the current API surface.

---

## Troubleshooting common issues

### Agent gets stuck or stalls

- **Symptom:** Agent pauses without clear reason or times out.
- **Fixes:** check for blocked network calls (403/401 on a connector), confirm connectors are active, reduce the task scope (split into smaller subtasks), or increase verbosity to surface where it failed. OpenAI’s logs (if available) show the last successful tool call.

### Incorrect or hallucinated data

- **Symptom:** Agent reports facts that don’t verify.
- **Fixes:** tighten source constraints in the runbook, require citation for every factual claim, and instruct the agent to cross-check information against multiple trusted sources. Use the Responses API’s retrieval or browse tool instead of relying on model recall.

### Connector authentication failures

- **Symptom:** Agent cannot access Google Drive / Gmail.
- **Fixes:** re-authenticate connectors manually; confirm token scopes; ensure enterprise SSO policies aren’t blocking third-party app tokens. For sensitive connectors, use “watch mode” and explicit manual login flows.

### Unexpected actions (agent acted without permission)

- **Symptom:** Agent attempted a disallowed operation.
- **Fixes:** review and tighten the runbook, enable user confirmations for all state-changing actions, and consult run logs. If the behavior persists, disable connectors and open a support ticket.

---

## What are the security risks?

### Main risk categories

- **Data exposure & exfiltration:** agents with broad connectors might access sensitive files and — if not properly constrained — could write sensitive outputs to external locations.
- **Prompt injection & manipulation:** malicious web content or files could attempt to manipulate agent behavior if runbooks and guardrails aren’t strict. Build the runbook to ignore instructions embedded in scraped content.
- **Credential abuse:** automated logins or poorly isolated tokens could be misused; avoid storing long-lived credentials in agent profiles and prefer manual, per-session authentication.
- **Over-trust / automation of sensitive actions:** allowing automatic sends or purchases without human approval increases risk. OpenAI’s agent design includes enforced confirmations and blocks for specific high-risk actions, but organizations should still apply their own governance.

### Recommended mitigations

- **Least privilege connectors:** grant only the minimum scopes required.
- **Watch mode and confirmations:** enable “watch mode” for agents that might access email or banking pages and require confirmations for state changes.
- **Audit logs & observability:** log all agent actions and review them periodically. Use rate limits and task quotas per user/agent.
- **Test sandboxing:** validate agents first in accounts with synthetic or redacted data.
- **Policy and runbook governance:** maintain an approval flow for agents that perform high-impact tasks and require human signoff before broad deployment.

## Conclusion

Agent Mode marks a meaningful shift: from **advisory** AI to **operational** AI. It can accelerate workflows across research, marketing, finance, and engineering — but with that capability comes new operational and security responsibilities. Use structured runbooks, least-privilege connectors, human-in-the-loop approvals, and continuous auditing to realize the upside while limiting risk.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as ChatGPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

To begin, explore the ChatGPT model ’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

---

*Originally published at [https://www.cometapi.com/how-to-use-chatgpt-agent-mode-step-by-step/](https://www.cometapi.com/how-to-use-chatgpt-agent-mode-step-by-step/).*
