<!-- social-ops-fingerprint:3bed9a5f2063b5e20a5b1e0a925a8b85f4b5d15a6d4ba35adc00fd8f729f8fb8 -->
---
title: OpenAI Dots: What Are OpenAI's Always-On AI Agents?
---
# OpenAI Dots: What Are OpenAI's Always-On AI Agents?

![OpenAI Dots: What Are OpenAI's Always-On AI Agents?](https://resource.cometapi.com/1Dots-Hero-Image.webp)

## TL;DR

**OpenAI Dots are persistent, always-on personal agents inside ChatGPT.** Powered by [GPT-6 Astra](https://learn.chatgpt.com/docs/dots), a Dot has its own cloud computer and can continue assigned work between conversations. This guide helps users and developers understand what Dots do and choose between a Dot, Codex, ChatGPT Work, and a custom API agent.

Dots are not simply a replacement for Codex or ChatGPT Work. Codex remains focused on software engineering, while ChatGPT Work is designed around longer, multi-step tasks and finished deliverables. A Dot acts more like a persistent personal agent sitting above ongoing work and can coordinate Work or Codex tasks when appropriate.

**The main developer tradeoff is convenience versus implementation control.** Dots manage the agent experience. A custom API agent lets developers define tool interfaces, application behavior, and cost attribution. Accurate billing still requires reconciling usage records with model, tool, compute, and third-party charges.

## Key Takeaways

- OpenAI Dots are persistent personal agents, not a standalone foundation model.
- A Dot combines a cloud computer, connected apps, memory, and ongoing work; proactive research is read-only.
- Codex focuses on software engineering, ChatGPT Work on substantial deliverables, and Dots on continuing responsibility across tasks.
- API agents give developers control over function schemas, execution logic, approvals, logs, and application UX.
- API usage records support granular cost attribution, but exact charges require billing reconciliation; Dots do not expose an equivalent public developer-facing ledger in the documentation reviewed.

## What Are OpenAI Dots?

OpenAI describes Dots as always-on agents built to handle ongoing work. They are better understood as a managed agent product than as a new AI model. Their underlying intelligence comes from GPT-6 Astra, which developers can also access through [GPT-6 Astra API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-astra/) for their own applications. Calling that model does not provide the Dots product or its managed runtime.

A normal ChatGPT conversation is primarily request-driven: you ask something, ChatGPT responds, and later interactions continue from available context. A Dot adds a much stronger notion of persistence. You give it an objective, decide which applications it may access, and define how independently it may operate.

Each Dot receives its own cloud computer and browser. It can research, analyze data, prepare documents, build software, and return results for review. Cloud work can continue when the user's computer is off; work delegated to a connected local computer has separate availability requirements.

| OpenAI Dots specification | Current implementation |
| --- | --- |
| Product type | Persistent, always-on personal AI agent |
| Underlying model | GPT-6 Astra |
| Execution environment | Dedicated cloud computer |
| Browser | Cloud browser |
| Memory | Ongoing context plus ChatGPT memory integration |
| Connected tools | Plugins and permitted connected apps |
| Proactive work | Yes, including read-only proactive research |
| Work delegation | Can create or use ChatGPT Work and Codex tasks |
| Local computer access | Optional; disabled until explicitly connected |
| Human oversight | Approvals, Custom Rules, and separate safety checks |
| Initial access | Eligible Pro plans, Business Premium, and Enterprise; gradual rollout with plan-specific conditions |
| Creation | ChatGPT mobile app, desktop app, or desktop browser |
| Public API endpoint named dots | None publicly documented |

### Primary Role and Ongoing Responsibility

Choose by the outcome you need rather than assuming the products have exclusive capabilities. A launch owner might use Dots for continuity, Work to prepare a deck, and Codex to implement a feature. The table describes product emphasis, not a hard technical boundary.

### Task Delegation and Local Availability

Dots can create background work, cloud threads, and Work or Codex tasks on connected computers. For local tasks, keep the connected computer online with the ChatGPT app open. A Dot's cloud environment does not automatically transfer a local browser login or give access to every existing conversation.

**Codex asks:** “What software should I build or change?”

**ChatGPT Work asks:** “What piece of work should I finish?”

**Dots asks:** “What responsibility should I keep handling for you?”

## What Can OpenAI Dots Do?

### Ongoing Work and Follow-up

A Dot carries an ongoing responsibility across conversations. It can keep a launch brief current, investigate new feedback, and revisit decisions when relevant information changes. Give it the sources, desired outcome, update schedule or trigger, and decisions that need your input.

It can also perform [read-only proactive research](https://learn.chatgpt.com/docs/dots/tasks-and-memory) and keep private notes. This mode gathers context; consequential follow-up actions remain subject to permissions and review.

### Cloud Computer and Connected Apps

Each Dot has a cloud computer and browser, so cloud work can continue when your own device is off. Plugins provide access to connected apps within the account’s permissions. A local computer is a separate, optional connection; keep it online with the ChatGPT app open for local work.

### Documents, Analysis, and Software Tasks

A Dot can research, analyze data, prepare documents, and build software directly, or coordinate Work and Codex tasks when useful. Review the output, important decisions, and required approvals as the responsibility develops.

The following struck-through material is retained at its original section position for revision review; its useful points are consolidated above.

## How Do OpenAI Dots Work?

Conceptually, Dots combine five layers:

- GPT-6 Astra provides the reasoning and agentic intelligence.
- Persistent agent context lets the Dot remember goals and continue responsibility between conversations.
- A dedicated cloud computer gives it an environment for browsing, file work, and computer-based tasks.
- Plugins and connected services provide structured access to external data and actions.
- Approval and safety systems determine whether an intended action may actually be executed.

The model itself is therefore only one part of the agent. The product wraps the model in a persistent execution environment, permissions, connected tools, memory, and action review.

Conceptually, a goal leads to planning, context retrieval, tool use or delegation, review, and continued work. This is a reader's mental model of the product, rather than a published diagram of OpenAI's internal architecture.

Memory has distinct layers: the conversation, relevant ChatGPT saved memory, and the Dot's own notes about preferences, decisions, and responsibilities. Those notes are not a complete transcript, and changing a ChatGPT memory setting does not necessarily change notes already made.

## How Does OpenAI Dots Handle Safety and Permissions?

An always-on agent requires stronger controls than an ordinary chatbot because it can potentially read private information and take actions. OpenAI therefore separates proactive information gathering from consequential action.

[Dots permissions and custom rules](https://learn.chatgpt.com/docs/dots/controls) let users allow actions, require checks, or block actions. Plugin permissions apply separately. These controls do not override built-in safeguards, and workspace administrators may restrict whether custom rules are available.

Dots can still make mistakes. Permissions, approval boundaries, and review remain important for consequential workflows.

### Automatic Action Review

Before an action affects an account or shares information, [automatic review](https://learn.chatgpt.com/docs/dots/controls) checks instructions, permissions, custom rules, and safeguards. It may allow the action, require your approval, or hand a step to you, such as changing a password. Custom rules cannot override built-in safeguards or grant app access.

### Privacy and Training Data

For [Business, Enterprise, and Edu workspaces](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-cloud-security), business data is not used to train models by default. Eligible conversations and tasks on personal plans follow the account’s data-control settings. OpenAI does not train directly on proactive research or a Dot’s private notes; when that information enters an eligible conversation or task, the applicable settings govern its use. This data policy does not imply that every listed plan has access to Dots.

## OpenAI Dots vs. Codex vs. ChatGPT Work

Dots, Codex, and ChatGPT Work overlap because all three can perform agentic work. Their intended unit of responsibility is different.

[Codex](https://openai.com/codex/) focuses on software-development workflows. [ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work) handles tasks you want to delegate, such as research, analysis, or file creation, either immediately or on a schedule. Dots add continuity across an ongoing responsibility; they can also perform work directly and delegate tasks when useful.

| Dimension | OpenAI Dots | Codex | ChatGPT Work |
| --- | --- | --- | --- |
| Primary role | Persistent personal agent | Software engineering agent | General-purpose work agent |
| Typical starting point | Ongoing goal or responsibility | Codebase or engineering task | Concrete task or deliverable |
| Persistence | Core design | Engineering workflow; ongoing tasks also possible | Task and schedule oriented |
| Cloud environment | Yes | Yes, depending on workflow | Cloud browser/computer available |
| Code specialization | General | Very high | General |
| Documents/slides/spreadsheets | Can create, coordinate, or delegate | Not primary focus | Core capability |
| Connected business apps | Yes | Supported integrations | Yes |
| Proactive research | Yes | Not primary interaction model | Task or schedule driven |
| Memory orientation | Personal and ongoing | Repository/task oriented | Project/task oriented |
| Best mental model | Persistent AI delegate | AI software engineer | AI project worker |

### Finished Deliverables vs. Ongoing Responsibility

ChatGPT Work and Dots overlap in the work they can perform. A Work assignment typically centers on a concrete result, such as a competitive analysis deck; a Dot keeps responsibility for the launch over time and coordinates follow-up when circumstances change. This describes their product emphasis, rather than an exclusive technical boundary.

## How Should You Evaluate OpenAI Dots in Real Work?

A model benchmark does not establish how reliably Dots will complete a particular business workflow. The model is one component; connected apps, permission boundaries, login requirements, changing context, and user review all affect the final result.

Evaluate Dots with representative work, such as maintaining a launch brief or investigating a support issue. Measure whether the result is correct, how much human intervention is needed, how well the agent respects permissions, and whether it resumes appropriately after new information arrives. Keep the task, available tools, acceptance criteria, and review method consistent when comparing alternatives.

For an API implementation, also measure completed-task cost, retries, latency, and failed tool calls. Raw model scores alone cannot answer whether a managed Dot or a custom agent is the better fit.

## OpenAI Dots vs. Building Your Own Agent on the API

### Managed Setup and Developer Responsibilities

**Dots optimize for convenience. API agents optimize for control.**

With Dots, OpenAI operates most of the agent stack for you: model choice within the product, cloud environment, memory, connected apps, the agent loop, and safety infrastructure. With the OpenAI API, developers define far more of the agent themselves.

OpenAI's [Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview) and lower-level Responses/Agents tooling give developers explicit control over models, instructions, tool schemas, MCP connections, execution environments, observability, and application logic.

| Capability | OpenAI Dots | Custom API Agent |
| --- | --- | --- |
| Setup effort | Low | Medium to high |
| Persistent agent | Built in | Developer-configured |
| Cloud computer | Built in | Configurable |
| Model choice | Managed by OpenAI; Dots currently use Astra | Developer chooses |
| Custom function schema | Not exposed as low-level Dot interface | Yes |
| tool\_choice control | Not exposed | Yes |
| Custom MCP topology | Plugin-oriented | Yes |
| Own application backend | Not required | Yes |
| Structured outputs | Product-dependent | Schema-constrained outputs where supported |
| Approval workflow | Built-in safeguards, permissions, and user rules | Application-defined controls plus provider safeguards |
| Exact tool interface | Supported integrations and product permissions | Developer-defined schemas and execution code |
| Token usage per agent turn | No equivalent documented public API telemetry | Best-effort recorded usage; not the final bill |
| Agent traces | User-facing activity | Detailed traces/logs |
| Cost attribution by request/task | Product-level allowances; no equivalent documented public ledger | Granular attribution with billing reconciliation |
| Model routing | Managed | Application-defined routing among supported models |
| Retry logic | Managed | Developer-defined |
| Observability integration | Limited product controls | Logs, traces, events, exports |
| UX | ChatGPT-native | Completely custom |
| Deployment in your product | No public Dot embedding endpoint identified in the reviewed docs | Custom application integration |

A custom API agent shifts engineering responsibility to your team: persistence, scheduling, permissions, credential handling, failure recovery, deployment, and user-facing controls still need to be built or configured. Provider safety requirements and API feature support continue to apply.

### Cost Attribution and Billing Reconciliation

[Dot conversations do not count toward ChatGPT usage limits.](https://learn.chatgpt.com/docs/dots) The plan provides an allowance for deeper work, while delegated Work and Codex tasks use those products’ limits. Treat these as separate usage categories. A custom API agent instead exposes accounting hooks for attributing spending to customers, tickets, or departments.

[Recorded agent usage and traces](https://developers.openai.com/api/docs/guides/agents-api/observability) help developers attribute root-agent and subagent work. Usage is best-effort: it can be missing or updated later, and it is not a final bill. The documented usage fields do not expose separate cache-write counts, so those fields alone cannot determine exact charges when cache-write pricing applies.

For a production cost estimate, use the model’s [current pricing documentation](https://developers.openai.com/api/docs/models/gpt-6-astra) and the selected provider’s own billing records. Context length, service tier, regional processing, tools, and infrastructure can change the total. OpenAI pricing is not a quote for CometAPI.

Maintain a task ledger that separates uncached input, cached reads, cache writes where available, output including reasoning, retries, and subagent calls. Add applicable tool, sandbox-compute, infrastructure, and third-party fees, then reconcile that estimate with billed charges. Do not add cached input on top of total input without adjusting for the cached portion.

This enables a precise accounting process when complete billing data is available; it does not make every API usage response an exact cost statement. It also does not imply that Dots are inherently more expensive.

### Tool Schemas and Execution Control

Dots let users connect supported integrations and define permissions or custom rules. An API agent lets developers define the callable interface: function names, argument types, allowed values, execution code, backend authorization, and the UI shown to users. This is implementation-level control within the API's supported capabilities.

The schema below exposes one operation with two required arguments and a fixed set of status values. It is a tool definition, not a complete runnable application; your backend must implement the function and enforce access to the lead.

```
{
  "type": "function",
  "name": "update_lead_status",
  "description": "Update only the sales-stage field for an existing lead.",
  "strict": true,
  "parameters": {
    "type": "object",
    "properties": {
      "lead_id": {
        "type": "string"
      },
      "status": {
        "type": "string",
        "enum": [
          "qualified",
          "unqualified",
          "follow_up"
        ]
      }
    },
    "required": [
      "lead_id",
      "status"
    ],
    "additionalProperties": false
  }
}
```

[Strict function schemas](https://developers.openai.com/api/docs/guides/function-calling) constrain generated arguments. The application executes the function, checks tenant ownership and authorization, validates state transitions, and applies any required approval. A valid schema does not itself guarantee that an action is authorized or that the model will make the right business decision.

Dots do not provide this same public developer-facing interface for replacing their internal tool schemas, orchestration, and billing instrumentation. However, they do provide meaningful user controls over connected apps and permitted actions. The difference is the level of control exposed, rather than an absence of controls in Dots.

### Can Developers Build a Dots-Like Agent with OpenAI's API?

Yes, although it is not a one-call clone of Dots. Developers can combine persistent sessions, function calling, web search, computer use, MCP servers, background execution, tracing, and custom orchestration to reproduce many architectural ideas behind an always-on agent.

The tradeoff is engineering work: Dots package the agent stack into a managed product, while the API exposes the building blocks.

## When Should You Use OpenAI Dots Instead of an API Agent?

Dots make sense when the agent primarily exists for you: keeping track of personal work, coordinating research, following projects, organizing information across connected services, or maintaining continuity across many small tasks.

A custom API agent makes more sense when the agent primarily exists inside your product or business process. If you need tenant-level billing, deterministic function schemas, exact model routing, proprietary approval systems, internal observability, application-specific UIs, tool-level access control, or explicit cost limits, an API architecture is the better fit.

This comparison focuses on personal Dots. OpenAI is also piloting specialist dots for organizational roles. A custom API agent is most relevant when you need to embed agent behavior in your own application and control its implementation.

## Can OpenAI Dots Access Your Local Computer?

Not automatically. A Dot's cloud computer is separate from the user's device. [Connecting a local computer](https://learn.chatgpt.com/docs/dots/computers-and-apps) grants a separate permission for local work; connecting that computer to Codex or enabling Work Sync does not by itself grant the Dot access. Some websites block cloud browsers or require verification, and starting a local task does not transfer the cloud browser session.

## How Can CometAPI Fit Into an API-Based Alternative to Dots?

If the goal is not to reproduce the ChatGPT Dots interface but to build your own agent product, a unified model API can be useful for the model layer.

[GPT-6 Sol API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-sol/) can support complex agentic workloads through an OpenAI-compatible interface. For newer workloads, [GPT-6.1 Sol API in CometAPI](https://www.cometapi.com/models/openai/gpt-6-1-sol/) provides another option for agentic coding and professional work.

In a custom deployment, your application sends work to an agent orchestrator. The orchestrator applies business rules and calls supported model endpoints and tools. Your application maintains its own logs, cost ledger, and approval layer. A model gateway supplies the model-access layer; it does not automatically supply an entire agent runtime.

For each selected endpoint, verify support for the API features you plan to use, including tool calling, structured outputs, and usage fields. OpenAI-hosted Agents API environments and traces should not be assumed to be available through an OpenAI-compatible gateway. CometAPI billing must be checked against CometAPI's own rates and records.

## What Are the Main Limitations of OpenAI Dots?

- Control granularity: Dots provide rules and permissions, but not the same developer-level orchestration surface as the API.
- Cost observability: subscription access is simple, but it does not provide the same per-call, per-token, and per-tool accounting as API workloads.
- Website compatibility: automated agents may encounter login, anti-bot, or action restrictions.
- Availability: access depends on plan, region, and workspace configuration.
- Autonomy risk: persistent agents can still make mistakes, so permissions and review remain necessary.

## Who Can Use OpenAI Dots and Where Can You Create One?

[Dots availability](https://learn.chatgpt.com/docs/dots) is rolling out gradually. As checked on October 12, 2026, eligible Pro 100, Pro 200, and Pro 500 users must be over 18 and outside the European Economic Area, United Kingdom, and Switzerland. Business Premium and Enterprise are rolling out worldwide; Enterprise requires an administrator to enable Dots. Eligibility does not guarantee that an account already has access.

Create a Dot in the latest ChatGPT mobile app, desktop app, or desktop browser, and continue with the same Dot across devices. Mobile web is not supported. [The October 5–9 update](https://learn.chatgpt.com/docs/whats-new/dots-october-9-2026) added mobile creation, appearance customization, and plugin connection; connecting your local computer still requires the desktop app.

## Conclusion

Dots extend ChatGPT from individual conversations toward ongoing delegated responsibility. They can preserve context, work in the cloud, use connected apps, and coordinate Work or Codex tasks, while involving the user when review or a decision is needed.

Choose Dots when you want a managed personal agent to keep work moving. Choose Codex for engineering workflows and ChatGPT Work for substantial deliverables. Build an API agent when your product needs custom tool interfaces, application-specific orchestration, and a billing process tied to individual customers or workflows. That additional control brings implementation and maintenance work.

## FAQ

### Can a Dot Resume Local Work After My Laptop Goes Offline?

Cloud work and connected-computer work have different execution environments. A Dot can continue work in its own cloud environment when your laptop is off, but a task assigned to that laptop needs the connected computer online with the ChatGPT app open. Check the task's execution location before assuming it will continue unattended; the cloud browser does not inherit the local browser session.

### Does Pausing a Dot Stop Every Delegated Task?

No. [Pause, task stopping, and schedule cancellation](https://learn.chatgpt.com/docs/dots/controls) are separate controls. Pause stops the Dot's main task. Open Activity to stop a delegated task, and Scheduled to disable or delete a recurring task. Ending a call also does not necessarily stop assigned work. Completed actions are not undone by stopping the agent.

### Does Messaging a Dot in Slack Grant It Access to Other Apps?

No. A messaging channel and an app connection grant different kinds of access. [App connections depend on account permissions](https://learn.chatgpt.com/docs/dots/computers-and-apps) and the environment where the work runs. Connect the required integration separately and inspect its allowed actions; a communication method alone does not grant access to an inbox, repository, or local files.

### Can API Usage Fields Alone Determine an Exact Agent Bill?

Not in every case. Usage can arrive late or be unavailable, and some costs require additional billing data. Include retries, subagent work, cache writes where applicable, tools, compute, and third-party services. Treat recorded usage as accounting input, attach it to your own task identifiers, and reconcile the result with billed charges rather than treating one usage response as the complete cost.

### Do a Dot's Private Notes Reset When ChatGPT Memory Settings Change?

Not necessarily. A Dot's private notes and ChatGPT saved memory are distinct sources of context. Notes can track decisions and preferences across contact methods, and they are not a complete transcript. Changing a ChatGPT memory setting does not necessarily remove existing Dot notes; review the relevant controls when changing the context you want it to retain.

---

*Originally published at [https://www.cometapi.com/openai-dots/](https://www.cometapi.com/openai-dots/).*
