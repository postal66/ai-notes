<!-- social-ops-fingerprint:e3ac1f7522bc0b1279b69034403ccd7dadf1e788723ae902a7b21e9f3ec6946d -->
---
title: How to Create and Use Claude Skills? Detailed Guide of 3 methods！
---
# How to Create and Use Claude Skills? Detailed Guide of 3 methods！

![How to Create and Use Claude Skills? Detailed Guide of 3 methods！](https://resource.cometapi.com/blog/uploads/2025/10/How-to-Create-and-Use-Claudes-Skills-Detailed-Guide-of-3-methods%EF%BC%81.webp)

Claude’s new **Skills** feature—recently rolled out by Anthropic—lets teams and developers teach Claude repeatable, sharable capabilities: think of compact, versioned “toolkits” (folders with instructions, scripts, and assets) that let Claude reliably perform domain-specific tasks such as generating brand-aligned slide decks, producing Excel workbooks with formulas, or safely executing small code snippets. This article explains **what Skills are and why they matter**, then gives a practical, step-by-step guide for using Skills three ways: in Claude’s web apps (the no-code path), in **Claude Code** (developer IDE-style), and via the **Claude API** (programmatic integration). We’ll finish with security, comparison to other agent patterns, best practices, and troubleshooting tips.

## What exactly are Claude Skills and what advantages do they bring?

**Short definition:** A *Skill* is a self-contained folder/package that bundles instructions, scripts, resources, and optionally executable helpers that Claude can dynamically load when a task matches the Skill’s triggers. In practice a Skill acts like a reusable, versioned “capability” that teaches Claude how to perform a specific class of tasks (e.g., format spreadsheets to your company standards, apply brand guidelines to slide decks, generate reports following a regulated template).

### Core parts of a Skill (what you’ll typically find)

- `manifest` / `metadata` — name, version, triggers, permissions.
- `instructions.md` — high-level steps, guardrails, examples.
- `handlers` or `scripts` — actual code for generating files, calling internal tools, or transforming data.
- `resources/` — templates, style guides, sample data.
- `tests/` — automated tests used to validate a Skill.

### What capabilities do Skills add to Claude?

- **Custom instructions & content bundles:** Skills can include written instructions, templates, and resource files (style guides, CSVs, etc.) that Claude uses as authoritative context.
- **Executable components (Code Execution Tool):** Skills may include scripts or code that run inside Anthropic’s code execution container for deterministic operations (file parsing, numeric computation, data transforms). This offloads work that would be costly or unreliable if expressed purely as token generation.
- **Automatic activation & selective use:** Claude can automatically select and invoke relevant Skills when the user’s request matches the Skill’s scope, and it can explain why it chose a Skill.
- **Versioning & programmatic control:** Skills are first-class API objects: you can upload, manage versions, and reference `skill_id`s from the Claude API. That enables CI-style workflows and governance for updates.
- **Distribution across endpoints:** Skills work across Claude’s product family — the web apps, Claude Code, and Anthropic’s API/Agent SDK — enabling both end-user productivity and developer automation.

## How can I use Claude Skills in the Claude web apps (Claude.ai)?

**I need prerequisites:** (1) You must be on a paid Claude plan that supports Skills (Pro, Max, Team, or Enterprise at launch). Availability and admin controls differ by plan and org settings. (2) Access to Settings and the “Skills” capability toggle in your workspace (Settings → Capabilities → Skills). Admins may need to enable Skill creation or limit installation to approved Skills.

Step-by-step guide to creating and using Skills in Claude Apps Web:

### Step 1: Explore built-in examples and toggle Skills on

Open Claude.ai → Settings → Capabilities → Skills. Toggle on the preview/example Skills to see structure and activation behavior. This is the fastest way to learn how Skills look and behave.

### Step 2: Use the Skill-creator UI (first Skill)

Anthropic deployed a guided Skill-creator inside the apps: choose **Create Skill** to launch a wizard that asks what you want the Skill to do, supplies a default folder layout (README, instruction files, sample templates, optionally a script), and helps write basic instructions and triggers. Use the built-in test harness to validate behavior with example prompts.

### Step 3: Define the Skill’s intent, examples, and resources

- **Templates/resources:** Add templates, CSV examples, design specs, or entity dictionaries the Skill should reference.
- **Intent / description:** Write a short, explicit description of what the Skill is for (this helps Claude match it).
- **Activation cues / triggers:** Add keywords or example prompts that should cause Claude to load the Skill.
- **Instruction files:** Put stable instructions (e.g., brand tone, required sections) into a single canonical file inside the Skill.

### Step 4: Download and Upload the Skill

Once you’re satisfied, Claude packages the Skill as a ZIP file. In the left sidebar, click “Capabilities.”

![How to Create and Use Claude Skills? Detailed Guide of 3 methods！](https://resource.cometapi.com/blog/uploads/2025/10/Screenshot-2025-10-17-190929-1024x569.webp)

Or you can drag and drop the ZIP into the upload area. Claude validates and installs it, confirming activation.

### Step 5 : Use Skills during real conversations

After saving, try natural prompts that match the Skill triggers (or mention the Skill by name). The app will indicate when it loaded a Skill and may show what resources it used; run a few iterations and refine instructions until outputs are reliable. When a user asks Claude to perform the relevant task, Claude can auto-detect and load the matching Skill—or you can explicitly invoke it. The Skill’s instructions, templates, and code guide Claude’s outputs.

### Tips for Claude Apps Web

- The system includes built-in skills for common tasks, such as: Document generation; Report creation; PowerPoint presentation; Excel formula calculation.
- Users can directly customize their own skills.
- Claude automatically invokes relevant skills, eliminating the need for manual selection.
- During Claude’s reasoning process, users can see which skills are being invoked.
- Prefer non-executable tasks at first.\*\* Web Skills that only specify instructions (no code) are easier to audit.

## How can I use Claude Skills in Claude Code?

### Conditions

- **Access to Claude Code**: Claude Code is Anthropic’s IDE/terminal assistant surface — often included in developer plans or accessible via a plugin/marketplace. Some Skill features require access to the Code Execution Tool or ADK (agent development kit). CometAPI provides access to Claude code and Claude API. You can use skills in CometAPI’s Claude code and consult [documentation](https://apidoc.cometapi.com/claude-code-installation-and-usage-guide-1266358m0) using Claude code.
- **Local developer environment**: If a Skill includes test suites or code, you’ll want to clone the Skill repository and run tests locally.

### Step-by-Step Guide to creating and using Skills in Claude Code

### Step 1 : Create a Skill folder structure:

In Claude Code, Skills commonly live as folders with a manifest (metadata), instruction files, test inputs, helper scripts (Python/JS), and any binaries or templates:

1. **Define the Skill manifest**: The manifest includes `skill_id`, name, description, author, dependencies, entry points, and security notes. This tells Claude Code how and when to load the Skill.
2. **Implement helper scripts and tests**: If your Skill uses code to transform or generate files, add small, well-scoped scripts and unit tests that run inside the Code execution environment.

### Step 2 : Install or add a Skill package

- In Claude Code, open the plugin/marketplace panel and `add anthropics/skills` (or the specific Skill repo).
- Alternatively clone a Skill repository to your workspace.

![How to Create and Use Claude Skills? Detailed Guide of 3 methods！](https://resource.cometapi.com/blog/uploads/2025/10/image-148-1024x253.webp)

Select “Anthropic Agent Skills,”

![Anthropic Agent Skills](https://assets.apidog.com/blog-next/2025/10/image-149.png)

then choose between “document-skills” (for file generation) or “example-skills” (for demos). For this tutorial, opt for “document-skills”—it previews capabilities like Word doc creation. Click “Install Now”; Claude Code downloads and registers the skills.

### Step 3 : Author advanced code handlers

- Implement handlers that operate on files or call external tools (e.g., generate .pptx with python-pptx, create .xlsx with openpyxl).
- If the Skill requires remote code execution, ensure it conforms to Anthropic’s container model (API docs describe how Skills use containers for code runs).

### Step 4 : Load and test in Claude Code

- Start a Claude Code session and ask Claude to run your Skill (e.g., “Use the ReportGen Skill to create Q3 revenue slides”).
- Observe logs, outputs, and any generated artifacts in the workspace.

### Step 5 : Package & publish

Commit the Skill to your org’s Skill registry or push to an approved GitHub repo. Use version tags and include test suites for governance.

### Tips for Claude Code

- **Treat Skills like code projects**: use CI to run Skill tests when code or templates change.
- **Isolate side effects**: if a Skill can execute scripts, run them in disposable containers or sandboxes to avoid accidental data leaks.
- **Document inputs/outputs clearly** so non-developer teammates can use the Skill in the web app later.

## How can I use Claude Skills in the Claude API?

### Conditions

Access to Anthropic’s **Messages API** with the **code execution tool** enabled (Skills integrate with the Messages API via a container parameter). You’ll also need API credentials and any runtime permissions necessary to run skill code in containers.

**Step-by-step guide to creating and using a Skill via the API:**

### Step 1 : Prepare the Skill package locally

Create a Skill folder that follows the API’s expected manifest format (name, version, instruction files, triggers, optional resource paths and helper scripts). Anthropic’s docs provide the schema and examples.

### Step 2 : Upload or register the Skill

Anthropic-managed Skill: reference the `skill_id` and optional version in your API call (no upload needed).Use your API key to authenticate and call the Skill creation endpoint (for example, a `POST /v1/skills` or similar endpoint.

```
curl -X POST "https://api.anthropic.com/v1/skills" \
-H "x-api-key: $ANTHROPIC_API_KEY" \
-H "anthropic-version: 2023-06-01" \
-H "anthropic-beta: skills-2025-10-02" \
-F "display_title=My Excel Skill" \
-F "files=@excel-skill/process_excel.py;filename=excel-skill/process_excel.py"
```

Upload the Skill payload or point the API at a zipped artifact. The API will validate and store the Skill for your workspace.

Regardless of the source, skills are integrated into the messaging API in the same way. You can specify the skill version using the skill\_id, type, and optionally the skill\_version parameter, which will be executed in the code execution environment:

| Aspect | Anthropic Skills | Custom Skills |
| --- | --- | --- |
| **Type value** | `anthropic` | `custom` |
| **Skill IDs** | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv` |
| **Version format** | Date-based: `20251013` or `latest` | Epoch timestamp: `1759178010641129` or `latest` |
| **Management** | Pre-built and maintained by Anthropic | Upload and manage via Skills API |
| **Availability** | Available to all users | Private to your workspace |

### Step 3: Call the Messages API with a container parameter

In your Messages API request, include a `container` field specifying the `skill_id`, `type` (`anthropic` or `custom`), and optionally `version`. The Messages endpoint routes execution to the code environment where the Skill runs.

Example (conceptual):

```
   {
     "model": "claude-sonnet-4-5-20250929",
     "messages": }],
     betas=,
     "container": {"type":"custom","skill_id":"skill_01AbCdEf","version":"latest"}
   }
```

### Step 4:Downloading Generated Files

When a skill creates a document (Excel, PowerPoint, PDF, Word), it returns a file\_id property in the response. You must use the File API to download these files:

```
def extract_file_ids(response):
file_ids = []
for item in response.content:
if item.type == 'bash_code_execution_tool_result':
content_item = item.content
if content_item.type == 'bash_code_execution_result':
for file in content_item.content:
if hasattr(file, 'file_id'):
file_ids.append(file.file_id)
return file_ids

for file_id in extract_file_ids(response):
file_metadata = client.beta.files.retrieve_metadata(
file_id=file_id,
betas=
)
file_content = client.beta.files.download(
file_id=file_id,
betas=
)

file_content.write_to_file(file_metadata.filename)
print(f"Downloaded: {file_metadata.filename}")
```

### Tips for API use

- **Prefer Anthropic-managed skills for common formats** (pptx/xlsx/docx) to avoid reinventing the wheel.
- **Use the version field.** Pin to a Skill version in production to avoid unexpected behavior.
- **Implement guardrails** in your system: sanitize inputs, limit file sizes, and perform post-generation validations before exposing artifacts externally.

## Why use Claude Skills — what are the benefits and tradeoffs?

### benefits

- **Consistency and quality:** Skills encode organizational best practices (brand rules, legal wording), so outputs are consistent and reduce manual rework.
- **Productivity:** Automating repeatable tasks (data prep, slide creation, template application) shortens cycles—early customers reported faster time-to-output in beta trials.
- **Reusability & governance:** Skills become versioned artifacts that can be reviewed, tested, and rolled out like software, simplifying audits and compliance.
- **Lower token/compute cost for complex flows:** Because Claude loads only the relevant parts of a Skill when needed, you can avoid always sending long system prompts, reducing cost and context bloat.

### limitations:

- **Up-front work:** Building robust Skills takes design, documentation, and tests — you’re trading prompt engineering for product engineering.
- **Executable risk:** Skills that run code or access data increase security surface area; enterprises must limit who publishes and approves executable Skills.
- **Plan and feature availability:** Skills were rolled out to Pro, Max, Team, and Enterprise plans at announcement; Free users may not have Skills access by default. Check your plan.

## How do Claude Skills compare to other platforms and agent patterns?

Skills = richer, versioned artifacts.\*\* They’re more structured than one-off tool calls or templates: Skills bundle instructions, assets, scripts, and manifests in a reusable package. That makes them closer to a deployable micro-agent than a single tool invocation.

### Skills vs. ad-hoc system prompts and prompt libraries

System prompts are ephemeral and must be provided each session; Skills are persistent, versioned, and centrally managed. Skills are therefore better for enterprise scale and reproducibility.

### Skills vs. tool-based agents (tool calls / function calling)

Tool-based agents (e.g., function calling patterns) focus on giving models concrete external abilities (APIs, tool invocation). Skills combine *instructions + resources + optional helpers* and are intended to teach the model *how* to do a task (including when to use tools). In short: tools are *actuators*; Skills codify procedure and policy that may use tools.

### Skills vs. OpenAI’s AgentKit and similar agent frameworks

Recent launches (for example at OpenAI DevDay) emphasize packaged agents and developer toolkits to move from prototype to production. Claude Skills play a similar role but with an emphasis on *folderized instructions + resources* and tight cross-integration across Claude apps, Code, and API. The two approaches are converging: both aim to enable production agents, but implementation details (SDK APIs, governance controls, marketplace patterns) differ. If you already use an agent framework, Skills can often be the “capability modules” you load into those agents.

### When should you choose Skills vs a custom agent?

- **Use Skills when** you need standardized, shareable, low-friction capabilities across users and UIs (non-developers benefit).
- **Use custom agents when** you require complex multi-tool orchestration with bespoke control logic outside Claude’s Skill execution model. Skills are excellent for tidily packaged domain tasks; agents are for heavyweight orchestration.

### Where other patterns still win

- **Low-latency, light tasks**: For tiny tasks or where you don’t need reproducible outputs, function-calling or system prompts are still simpler.
- **Custom tool ecosystems**: If you already have a large custom tool infrastructure exposed via APIs, function calling/plugins integrated with orchestration layers may be a better fit.

## Practical, real-world examples and recipes

### Example 1 — Brand Slide Formatter (web app Skill)

- **What it does:** Converts raw slide bullet-points into company branded slides (fonts, tone, slide order).
- **Create in web app:** Use Skill creator → add brand style guide, slide template, and example input/output. Enable for the design team. Test by asking “Format these notes using Brand Slide Formatter.”

### Example 2 — CSV Data Auditor (Claude Code Skill)

- **What it does:** Validates CSV data columns, runs lightweight Python checks (missing values, type mismatches), and returns a summary report.
- **Create in Code:** Build Skill with `validators.py` helper, unit tests, and sample CSVs. Test iteratively in Claude Code’s notebook, then package and publish.

### Example 3 — Contract Redline Assistant (API Skill)

- **What it does:** Applies company legal standards to contract text and produces a redline and rationale.
- **Create via API:** Author instruction files and clause library, upload via `POST /skills`, then call from your contract management system with `skill_id` to produce standardized redline outputs.

## Conclusion

Claude Skills are a practical bridge between ad-hoc instructions and full-blown agent engineering: they let teams capture institutional know-how, enforce style and safety, and automate recurring tasks across UI and programmatic surfaces. Whether you’re a non-technical product manager using the web skill-creator, an engineer shipping repeatable developer tools in Claude Code, or a platform team integrating Skills into apps with the Messages API, following small, disciplined practices—versioning, testing, least privilege, and staged rollouts—will make your Skills reliable and auditable in production.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

CometAPI provides access to Claude code and Claude API. You can use skills in CometAPI’s Claude code and consult [documentation](https://apidoc.cometapi.com/claude-code-installation-and-usage-guide-1266358m0) using Claude code.

### Why to use claude code through CometAPI?

Top Artificial Intelligence features: Easily generate, debug and optimize code using models built specifically for developers.

- Flexible Model Selection: Our comprehensive range of models allows you to develop more seamlessly.
- Seamless Integration: APIs are always available. Integrate Claude Code directly into your existing workflow in minutes.
- **Using Claude Code via CometAPI will save more costs**. The Claude API provided by CometAPI is 20% off the official price and is updated with the latest model by the official. The latest model is [Claude Haiku 4.5 API](https://www.cometapi.com/claude-haiku-4-5-api/).

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-create-and-use-claudes-skills/](https://www.cometapi.com/how-to-create-and-use-claudes-skills/).*
