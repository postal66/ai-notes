<!-- social-ops-fingerprint:33d28cdaed67c27615ac4ce8180a8cd646fc725722352a97c0b8825948b96195 -->
---
title: A Look Back at OpenAI DevDay 2026: What can developers do?
---
# A Look Back at OpenAI DevDay 2026: What can developers do?

![A Look Back at OpenAI DevDay 2026: What can developers do?](https://resource.cometapi.com/OpenAI%20DevDay%202026.jpg)

## TL;DR

OpenAI DevDay 2026, held on September 29 in San Francisco, introduced GPT-6.1 Sol, persistent Dots agents, faster inference, and new developer and collaboration tools. The central change is from answering prompts to executing ongoing work. For developers, the priorities are cost per successful task, reliable tool use, and the access conditions attached to each product; several announcements were previews or future releases rather than universally available features.

## Key Takeaways

- GPT-6.1 Sol: GPT-6 Astra capability for coding, computer use, and professional work at $2 input and $10 output per million tokens under Standard short-context pricing.
- Dots: Persistent delegated work with permissions and subscription eligibility, including administrator-controlled beta access for some organizations.
- Codex and agent infrastructure: Reusable cloud environments, code review, security scanning, and hosted Agents API execution extend AI beyond code suggestions.
- ChatGPT collaboration: Space, Pages, plugins, and event-driven tasks connect shared knowledge to ongoing workflows.
- Availability and economics: Separate launch-day access from planned releases, and evaluate total task cost rather than token prices or peak speed alone.

The following recap examines what OpenAI announced, how the technologies compare, and which developments matter most for developers and businesses.

## DevDay 2026: The Shift to Executable AI

OpenAI DevDay 2026 took place on September 29, 2026, at Fort Mason in San Francisco. According to the [official DevDay recap](https://openai.com/index/devday-2026-recap/), the event was the company’s largest DevDay, with announcements organized around models, developer tools, ChatGPT customization, collaboration, and subscription capabilities.

Unlike previous developer conferences centered primarily on APIs and model improvements, DevDay 2026 emphasized three connected changes. First, OpenAI introduced more capable models at different price and performance levels. Second, it expanded infrastructure for agents that use tools and operate applications. Third, it turned ChatGPT into a collaborative environment where people, specialized agents, and connected software work together.

| Category | Major announcements | Main significance |
| --- | --- | --- |
| AI models | GPT-6.1 Sol, Ultrafast | More capable and faster inference |
| Autonomous agents | Dots, specialist dots | Persistent delegated responsibilities |
| Developer infrastructure | Agents API, computer use, Decisions API | Hosted execution and structured decisions |
| Software development | Codex Cloud, CLI, Code Review, Security Cloud | AI-assisted development lifecycle |
| ChatGPT ecosystem | Plugin extensions, MCP Events, Sites | Third-party integrations and event-driven workflows |
| Collaboration | ChatGPT Space, Pages, collaborative slides | Human-agent teamwork |
| Enterprise and access | Private Intelligence, Sign in with ChatGPT, Pro 500 | Security, distribution, usage allowances |

The announcements reveal a broader platform strategy. OpenAI is building not only the intelligence layer but also execution, collaboration, and distribution infrastructure around it.

## 1. GPT-6.1 Sol and Ultrafast: Capability and Speed

GPT-6.1 Sol was a major model announcement at DevDay. It upgrades GPT-6 Sol for agentic coding, computer use, document understanding, and professional workflows. Its value is the balance of task quality and operating cost, rather than a promise to outperform GPT-6 Astra on every workload.

OpenAI positioned the model between its cost-efficient GPT-6 Luna family and high-capability GPT-6 Astra model. Its practical appeal is not simply better benchmark performance: GPT-6.1 Sol approaches flagship-model capabilities while significantly reducing the cost of demanding tasks.

### GPT-6 Models: Differences, Pricing, and Selection

The three models serve different workloads. GPT-6 Astra is the flagship option for demanding reasoning and coding; GPT-6.1 Sol balances capability and cost for complex coding, computer use, and professional work; GPT-6 Luna targets focused, high-volume tasks where cost matters most.

A practical routing strategy is to test GPT-6 Luna on routine extraction and classification, use GPT-6.1 Sol for more complex workflows, and reserve GPT-6 Astra for difficult cases. This is a deployment recommendation: choose with representative tasks, acceptance criteria, retries, latency, and review costs rather than token price alone.

| Standard short-context pricing / 1M tokens | GPT-6 Astra | GPT-6.1 Sol | GPT-6 Luna |
| --- | --- | --- | --- |
| Input | $10.00 | $2.00 | $0.10 |
| Cached input | $1.00 | $0.10 | $0.01 |
| Output | $50.00 | $10.00 | $0.50 |
| Best fit | Most demanding reasoning | Complex coding and agents | Focused high-volume tasks |

These are [official Standard short-context prices](https://developers.openai.com/api/docs/pricing), not a guarantee of equal cost per completed task.

At standard rates, GPT-6.1 Sol processes five times as many input or output tokens as GPT-6 Astra for the same token budget. This does not automatically mean five times lower total application cost: inference settings, tool calls, retries, and success rates also matter.

### Ultrafast: Faster Token Generation

~~At DevDay, OpenAI announced up to six times faster API token generation and up to eight times faster Codex generation, including a reported 300 tokens per second in Codex. The price comparison below concerns GPT-6 Astra. GPT-6.1 Sol Ultrafast subsequently became available to all API users on October 8, 2026, subject to rate limits. Faster token generation does not guarantee the same improvement in total workflow time. See ~~[~~Ultrafast configuration and limits~~](https://developers.openai.com/api/docs/guides/ultrafast-mode)~~ and the ~~[~~dated release entry~~](https://developers.openai.com/api/docs/changelog)~~.~~

#### Ultrafast for Latency-Sensitive Work

Ultrafast is a premium speed tier for workloads where waiting matters, such as interactive coding and agent workflows. DevDay's advertised gains reached six times faster API token generation and eight times faster Codex generation, with a reported peak of 300 tokens per second. These are generation-speed claims, not equivalent reductions in complete task time.

GPT-6 Astra and GPT-6.1 Sol Ultrafast are now available to all API users with separate rate limits. GPT-6.1 Sol's release is no longer a future announcement. Configure the Ultrafast service tier and check model-specific limits; persistent WebSocket connections can reduce overhead in workflows with frequent tool calls. See [API configuration and availability](https://developers.openai.com/api/docs/guides/ultrafast-mode).

In Codex and ChatGPT Work, Ultrafast supports GPT-6 Astra and ~~Sol~~GPT-6.1 Sol on Pro $500 and eligible Enterprise and Edu plans. Enterprise access is off by default and requires workspace-owner enablement. ~~Sol~~GPT-6.1 Sol's October 8 rollout is covered in the [dated product update](https://learn.chatgpt.com/docs/whats-new/october-5-9-2026). API billing and subscription usage are separate.

#### Ultrafast vs Fast Mode

Fast mode offers a smaller latency upgrade for regular user-facing traffic; its API guide advertises up to 2.5 times faster speeds, with results depending on the model and workload. Ultrafast targets the highest-speed GPT-6 Astra and GPT-6.1 Sol workloads at a larger premium. See the [Fast mode guide](https://developers.openai.com/api/docs/guides/fast-mode) and [Codex speed and usage requirements](https://learn.chatgpt.com/docs/agent-configuration/speed).

| Dimension | Fast | Ultrafast |
| --- | --- | --- |
| API request setting | service\_tier: fast; priority is also supported | service\_tier: ultrafast |
| API rate limits | Shared with Standard for the same model | Separate from Standard and Fast |
| Best fit | Regular interactive traffic | Work where minimum waiting time justifies the premium |
| Codex purchased credits / Enterprise usage | 2 times Standard | 6 times Standard |
| Codex included subscription allowance | 2.5 times Standard | 8 times Standard |

Subscription multipliers above are usage rules, not API token prices. Benchmark end-to-end latency, accepted-task rate, and total charges before changing tiers. The following price table retains its narrower scope: GPT-6 Astra, Standard versus Ultrafast, short context.

#### GPT-6 Astra: Standard vs Ultrafast Pricing

| GPT-6 Astra, short context | Standard | Ultrafast |
| --- | --- | --- |
| Input / 1M | $10 | $60 |
| Cached input / 1M | $1 | $6 |
| Output / 1M | $50 | $300 |
| Relative token price | 1× | 6× |
| Advertised generation speed | Baseline | Up to 6× via API |
| Best use | Cost-aware tasks | Interactive latency-critical workflows |

For offline batches, the premium is harder to justify. In real-time coding and expensive human-in-the-loop workflows, reduced waiting can have meaningful value. Teams should measure end-to-end response time, cost per successful task, and user outcomes.

### GPT-6.1 Sol Benchmark Performance

| Benchmark | Reported result | Comparison | Practical implication |
| --- | --- | --- | --- |
| DeepSWE 1.1 | Matches GPT-6 Astra in reported evaluation | 6.4 percentage points above GPT-6 Sol’s best score | More reliable complex coding |
| OSWorld 2.0, offline partial reward | 7 percentage points above GPT-6 Sol | Within 2.1 percentage points of GPT-6 Astra at maximum effort | Stronger GUI automation |
| AutomationBench 1.0.6 | 4.8 percentage points above GPT-6 Sol at medium effort | 2.2 percentage points above Opus 5.5 | Better multistep workflows |
| Terminal-Bench Science 0.1 | More than double GPT-6 Sol’s maximum-effort score | Average cost $5.47 per task | Research economics |
| Factuality evaluation | 7.7% responses with errors, low effort | Down from 11.4% for GPT-6 Sol | Fewer errors on challenging prompts |

> OpenAI's launch evaluations use different effort and task settings. OSWorld reports partial reward on the offline v2026.08.08 set at maximum effort; AutomationBench 1.0.6 compares medium effort across business workflows. Terminal-Bench Science costs are reported at maximum effort. Factuality uses de-identified conversations in which users had flagged earlier errors, so its 7.7% result does not represent ordinary usage.

The practical argument for GPT-6.1 Sol is cost-adjusted quality. Teams comparing it with [Opus 5.5 API in CometAPI](https://www.cometapi.com/models/anthropic/claude-opus-5-5/) should preserve effort settings and account for fallbacks, tool calls, and retries. GPT-6 Astra remains a candidate for the hardest scientific tasks; its reported Terminal-Bench Science 0.1 score was 68.1%.

## 2. Dots: Persistent Delegated Work

### What is Dots

Dots are persistent AI agents that keep context, use connected applications, and carry out ongoing responsibilities within approved permissions. Instead of repeatedly issuing isolated prompts, you can assign continuing work and review the results. See [Dots capabilities and access](https://learn.chatgpt.com/docs/dots).

For example, a research assistant may monitor competitors, prepare weekly summaries, and update an internal document. A traditional chatbot usually requires repeated prompts; a persistent agent can be assigned the continuing responsibility.

### Dots vs ChatGPT vs API-Based Agents

| Dimension | ChatGPT | Dots | Custom API agent |
| --- | --- | --- | --- |
| Primary interaction | Conversations | Delegated responsibilities | Developer-defined workflows |
| Persistent execution | Feature-dependent | Core design | Requires implementation |
| Tool integration | Connected tools and plugins | Connected applications and cloud execution | Custom-defined interfaces |
| Custom logic | Product constraints | Product-managed workflows | Extensive developer control |
| Cost control | Subscription allowances | Subscription access | Usage-based accounting |
| Infrastructure | OpenAI-managed | OpenAI-managed | Developer-managed or hosted |
| Best fit | Individuals and teams | Delegating ongoing work | Building custom products |

Dots reduces the infrastructure needed for delegated work, while a custom API agent offers more control over tools, interfaces, evaluation, and accounting. At launch, Dots was available to Pro and Business Premium users in eligible markets; Enterprise, Edu, and Healthcare beta access required workspace-admin enablement and was off by default. Persistent operation should be evaluated against permission boundaries, recovery behavior, and reviewable results.

### How to Start Using Dots

1. Open Dots in the ChatGPT mobile app, desktop app, or a desktop browser. If the entry is unavailable, check account eligibility and workspace settings.
2. Create your dot, give it a name, and connect plugins for the apps its assignment needs, such as email, calendar, or files.
3. Describe an ongoing responsibility, its sources, expected output, and decisions requiring your input. For example: draft a weekly competitor summary for review.
4. If a fixed schedule matters, specify the time zone and duration, and ask the dot to confirm it. Review the first output and refine the assignment.
5. Inspect Activity in the desktop app to review delegated work. Local-computer access is optional; when used, keep the computer online with ChatGPT open.

See the [Dots setup guide](https://learn.chatgpt.com/docs/dots/getting-started) for device setup and connected tools. Start with a bounded assignment and review early results before expanding its scope.

## 3. Codex: An Expanded Development Workflow

Codex received upgrades across the software-development lifecycle, from implementing features to reviewing changes and investigating security concerns. It increasingly resembles an integrated development environment with AI task execution rather than a standalone code assistant.

| Feature | Core functionality | Benefit | Availability |
| --- | --- | --- | --- |
| Codex Cloud | Remote tasks, reusable environments | Work across devices | Eligible paid plans |
| Refreshed Codex CLI | Voice commands, /agents, worktrees | Parallel task coordination | All plans |
| Code Review | Diffs, change summaries, automated review | Faster pull-request review | All plans; integrations may be previews |
| Codex Security Cloud | Repository scanning and fix preparation | Continuous security analysis | Eligible paid or organizational plans |
| GPT-6.1 Sol integration | Agentic coding model | Quality-cost balance | Eligible plans and API |

Reusable cloud environments reduce repeated setup, while the /agents interface helps developers coordinate parallel tasks. [OpenAI's Codex release documentation](https://learn.chatgpt.com/docs/whats-new/devday-2026) describes remote environments and Security Cloud's repository checks and proposed patches. Findings and fixes require review; the useful engineering metrics are verified behavior, test coverage, and operational risk.

## 4. API Updates: Agents API and Decisions API

### What Is the Agents API?

The Agents API exposes OpenAI's managed Codex harness for durable, multistep work. OpenAI maintains orchestration, session state, context compaction, and recovery; developers configure models, instructions, tools, and environments. A session can continue across turns instead of rebuilding context for each request. See the [Agents API overview](https://developers.openai.com/api/docs/guides/agents-api/overview).

### What Is the Decisions API?

The Decisions API evaluates text and images and returns typed judgments for classification, routing, and prioritization. As of October 10, 2026, it is in public beta and supports gpt-6-luna. Its dedicated endpoint is POST /v1/decisions.

### Agents API vs Decisions API vs Responses API

| Dimension | Agents API | Decisions API | Responses API |
| --- | --- | --- | --- |
| Purpose | Execute workflows | Structured decisions | Generate model responses |
| Task scope | Multi-step | Focused choice | Single call or managed sequence |
| Computer use | Supported | Not core purpose | Tool dependent |
| Execution | Hosted | Managed decision endpoint | Developer orchestration |
| Ideal use | Browser and agent workflows | Classification and routing | Chat, reasoning, tool integration |
| DevDay status | Public beta | Limited preview | Established API |

A full agent is not necessary for a focused classification or routing problem. Decisions API was a limited preview at DevDay and entered beta with GPT-6 Luna on October 6, 2026. Check current access, pricing, and evaluation results before choosing it for production. See the [API changelog](https://developers.openai.com/api/docs/changelog).

## 5. ChatGPT Updates: Collaboration and Connected Work

### Space and Pages: Shared AI Work

DevDay framed ChatGPT as a collaborative workspace. ChatGPT Space organizes shared projects and agent participation; Pages supports collaborative documents; collaborative slides were announced for a subsequent release window. Together these features aim to connect discussion, documents, and execution.

| Feature | Primary purpose | Human collaboration | Agent participation |
| --- | --- | --- | --- |
| ChatGPT Space | Shared project workspace | Yes | Yes |
| Pages | Collaborative documents | Yes | Yes |
| Collaborative slides | Presentation creation | Yes | Yes |
| Team Tasks | Recurring responsibilities | Yes | Yes |
| Meetings plugin | Notes and action items | Sharing and review | Follow-up workflows |
| @ChatGPT in Slack and Teams | In-channel assistance | Yes | Tool-connected assistance |

### Plugins and MCP Events: Connected Workflows

[Plugin extensions](https://developers.openai.com/plugins/build/extensions) add interfaces such as panels, sidebar entries, and file viewers to ChatGPT. [MCP Events](https://developers.openai.com/plugins/build/mcp-events) supports event-triggered automations rather than relying on a new prompt for every action. Integration choices still depend on platform support, user permissions, and how teams manage failed or duplicate events.

## 6. Privacy and Distribution: Enterprise Access

As agents gain access to internal data and software, privacy controls and accountability matter alongside capability. [Private Safety Processing](https://developers.openai.com/api/docs/guides/private-safety-processing) supports automated safety review without exposing underlying content to OpenAI personnel. At DevDay, Private Inference was a planned confidential-computing preview; Sign in with ChatGPT and Pro 500 addressed separate access and usage needs.

| Announcement | Main benefit | Important consideration |
| --- | --- | --- |
| Private Intelligence | Stronger privacy controls | Varies by offering |
| Sign in with ChatGPT | Third-party authentication and partner access | Eligible integrations only |
| Pro 500 | Higher usage and Ultrafast | Premium subscription |
| OpenAI Marketplace | Procurement flexibility | Eligible enterprise customers |
| Specialist dots | Delegated organizational roles | Permissions and governance |
| Bedrock Managed Agents | OpenAI agents inside AWS | AWS architecture |

Enterprise AI adoption depends not only on benchmarks but also on procurement, compliance, data handling, and operational accountability.

## Feature Availability: Launch Status and Later Updates

| Feature | Launch status / verified later update | Access considerations |
| --- | --- | --- |
| GPT-6.1 Sol API | Available | API; other products have distinct entitlement |
| GPT-6 Astra Ultrafast | Available | Premium pricing and limits |
| GPT-6.1 Sol Ultrafast | Available via API since October 8, 2026 | All API users, subject to rate limits; unavailable at the DevDay launch |
| Dots | Limited rollout | Pro and Business Premium in eligible markets; admin-enabled beta for Enterprise, Edu, and Healthcare |
| Agents API with computer use | Public beta | Developer integration |
| Decisions API | Limited preview at launch; beta with GPT-6 Luna since October 6, 2026 | Check current beta access and pricing |
| Codex Cloud | Available | Plus, Pro, Business, Healthcare, Education, and Enterprise |
| Codex Security Cloud | Eligible rollout | Pro, Business, Enterprise, and Edu; review preview conditions |
| ChatGPT Space | Available | Pro, Business, and Enterprise; device capabilities vary |
| Collaborative slides | Coming in subsequent weeks | Planned rollout |
| Plugin extensions | Available | Developer submission and permissions |
| Private Inference | Preview planned | Enterprise focus |

This table retains DevDay launch status for entries without a dated update. GPT-6.1 Sol Ultrafast and Decisions API include verified post-launch updates checked on October 10, 2026. Other launch entries should not be read as confirmation of current availability. Consult the [API changelog](https://developers.openai.com/api/docs/changelog) and current product documentation for region, plan, quota, and billing requirements.

## Implications and Next Steps for Teams

The announcements make AI deployment a question of measurable work: task quality, operating cost, permission boundaries, and recovery. Teams can translate that shift into four practical actions:

- Evaluate before switching models. Benchmark GPT-6 Luna, GPT-6.1 Sol, and GPT-6 Astra on representative tasks and route work by difficulty; compare accepted outcomes, retries, latency, and review effort.
- Pilot bounded agent workflows. Use Agents API for multistep execution or Decisions API for structured choices, then test interruptions, approvals, escalation, and failure recovery.
- Give Dots a narrow recurring responsibility. Define sources, output, schedule, and review rules, then expand the assignment after checking its results.
- Measure engineering and collaboration outcomes. Review Codex changes and security findings, connect plugins only where they improve work, and verify product access, privacy, and total cost before scaling.

| Audience | Relevant announcement | Expected value | Main challenge |
| --- | --- | --- | --- |
| Software developers | GPT-6.1 Sol and Codex | Faster engineering | Review quality |
| AI application builders | Agents API | Less orchestration burden | Reliability and permissions |
| Support teams | Decisions API | Structured routing | Accuracy and escalation |
| Knowledge workers | Dots | Recurring task delegation | Trust and oversight |
| Collaborative teams | ChatGPT Space | Shared execution | Adoption and governance |
| Enterprise IT | Private Intelligence | Data protections | Compliance validation |
| SaaS providers | Plugins and sign-in | Distribution | Platform dependency |
| Latency-sensitive apps | Ultrafast | Faster generation | Higher inference cost |

### How CometAPI will help you after OpenAI dev 2026

[GPT-6.1 Sol is available on CometAPI](https://www.cometapi.com/models/openai/gpt-6-1-sol/). Use a CometAPI-issued key with its documented Responses endpoint and the model identifier gpt-6.1-sol; this route uses your CometAPI account rather than requiring a separate OpenAI API account.

Create a CometAPI account, generate an API key, and configure your application for the CometAPI endpoint. Keep the key in secure configuration and test a small request before production. Model access does not automatically include Dots, OpenAI-hosted agent environments, or ChatGPT subscription features; verify those entitlements separately.

For Standard requests with up to 272K input tokens, CometAPI lists $1.60 input, $0.08 cached input, and $8 output per million tokens. Longer-context requests list $3.20, $0.16, and $12 respectively. These figures concern model-token charges; tool fees, retries, and processing settings can change total cost.

## FAQ

### How should teams test GPT-6.1 Sol before switching?

Use representative tasks with explicit acceptance criteria, including examples that previously failed. Run the same inputs and tool permissions across candidate models, then measure accepted-task rate, correction time, latency, and full billable usage. A lower token rate is useful only if retries and human review do not erase the saving; preserve a rollback path for workflows with costly failures.

### When does OpenAI Ultrafast justify its higher price?

Start with workflows where a person is waiting for the output, then measure the full response rather than tokens per second alone. Network overhead, tool calls, and application processing can limit the benefit of faster generation. Compare the added inference charge with observed waiting-time reduction and task success; offline work may be better served by a lower-cost processing option.

### Does CometAPI access include Dots and hosted OpenAI agents?

Access to a supported model endpoint should not be treated as access to every product that uses that model. Dots, hosted agent environments, and ChatGPT subscriptions have separate credentials, entitlements, and service behavior. Confirm each required capability with the provider before designing the integration, especially when an application needs persistent state or platform-managed tools.

### How should a team scope its first Dots assignment?

Choose a bounded recurring task with clear inputs, a reviewable output, and an escalation rule. For example, ask for a draft weekly summary rather than granting open-ended authority to change external records. Define what the agent may access, which decisions need review, and how the team will notice missing or duplicate work before increasing responsibility.

## Conclusion

OpenAI DevDay 2026 demonstrated that the next phase of AI goes beyond smarter models. GPT-6.1 Sol improves the economics of powerful reasoning and coding; Dots extends AI into persistent responsibilities; the Agents API and Codex provide execution infrastructure; and Space and plugin extensions make the results collaborative. The larger shift is toward systems that complete measurable work while remaining accountable for cost, permissions, reliability, and human oversight.

---

*Originally published at [https://www.cometapi.com/a-look-back-at-openai-devday-2026/](https://www.cometapi.com/a-look-back-at-openai-devday-2026/).*
