<!-- social-ops-fingerprint:6e7cec5c4d4d1eef7a50f0d1828083c26d5107983d435e280291c5caa6525c66 -->
---
title: GPT-5.3 Codex: Features, Benchmarks, and how to get it
---
# GPT-5.3 Codex: Features, Benchmarks, and how to get it

![GPT-5.3 Codex: Features, Benchmarks, and how to get it](https://resource.cometapi.com/GPT-5.3-Codex%20Features,%20Benchmarks,%20and%20how%20to%20get%20it.webp)

On February 5, 2026, OpenAI announced **GPT-5.3-Codex**, a focused upgrade to its Codex family that merges advanced coding ability with broader professional reasoning, faster inference, and deeper “agentic” workflows. The release brings a new Codex desktop app and extends access across the Codex ecosystem (CLI, IDE extensions, web), with API access (promised “soon").

## What is GPT-5.3-Codex ?

GPT-5.3-Codex is the latest **agentic coding model** in OpenAI’s Codex line: a model trained and tuned specifically to operate inside developer workflows, interact with tools (terminals, editors, web endpoints), and execute long-horizon engineering tasks that require planning, tool use, and iterative debugging. OpenAI positions GPT-5.3-Codex as the successor that combines the coding strengths of GPT-5.2-Codex with the reasoning and professional-knowledge improvements from GPT-5.2, yielding a single model designed to act more like a collaborative engineering teammate.

### Origins and design goals

- **Agentic workflows:** The model is tuned to orchestrate sequences of actions over time (e.g., run tests, patch code, re-run), not just generate single answers.
- **Tool integration:** Codex is intended to use developer tools—CLIs, debuggers, package managers—safely and reliably, preserving state across sessions.
- **Practical developer help:** The aim is pragmatic: reduce context switching, speed troubleshooting, automate routine work (tests, refactors, code retrieval) and support collaborative steering by the human user.

## What’s new in GPT-5.3-Codex?

GPT-5.3-Codex introduces several concrete changes and product-level improvements compared with its immediate predecessors:

### 1. Faster inference for Codex users

OpenAI reports that GPT-5.3-Codex **runs approximately 25% faster** for Codex users due to improvements in the inference stack and infrastructure optimizations. That speed boost is framed both as lower latency during interactive debugging and as enabling longer, smoother agentic runs.

### 2. Unification of reasoning + coding strengths

Rather than being purely “coding-only,” GPT-5.3-Codex merges the frontier coding performance of GPT-5.2-Codex with enhanced professional reasoning (from GPT-5.2), making it better at research-heavy tasks: reading docs, planning multi-step migrations, and producing justification and test evidence alongside code.

### 3. Better collaboration and steerability during runs

A major user-facing change is improved collaborator-style interaction while the model is “working”: Codex will report progress more frequently, accept steering instructions mid-run, and retain context and state across multi-step tasks—so a user can interrupt, correct, or direct the agent as it executes. Product notes indicate this “steer” behavior is being stabilized across the Codex tools.

### 4. The Codex desktop app (plus tighter cross-client syncing)

OpenAI launched a **Codex app** that syncs session history and configuration with the Codex CLI and IDE extensions—so a developer can begin in their editor or terminal and pick up work in the desktop app without losing state. The app is positioned as the coordination hub for agentic workflows.

### 5. Agentic long-running behavior

GPT-5.3-Codex is explicitly optimized for tasks that can run for extended periods, interleave with tool calls, and require mid-task steering (pause/resume, change objectives). This improves capabilities on complex refactors, multi-module feature work, and cross-repository tasks.

## GPT-5.3-Codex on benchmarks

|  | GPT-5.3-Codex (xhigh) | GPT-5.2-Codex (xhigh) | GPT-5.2 (xhigh) |
| --- | --- | --- | --- |
| SWE-Bench Pro (Public) | 56.8% | 56.4% | 55.6% |
| Terminal-Bench 2.0 | 77.3% | 64.0% | 62.2% |
| OSWorld-Verified | 64.7% | 38.2% | 37.9% |
| GDPval (wins or ties) | 70.9% | - | 70.9% (high) |
| Cybersecurity Capture The Flag Challenges | 77.6% | 67.4% | 67.7% |
| SWE-Lancer IC Diamond | 81.4% | 76.0% | 74.6% |

### Representative benchmark results

- **Terminal-Bench 2.0:** GPT-5.3-Codex reportedly scores **≈77.3%**, a large jump that signals much greater proficiency in command-line and terminal workflows compared with the prior generation.
- **SWE-Bench Pro:** OpenAI reports **≈56.8%** on a rigorous software engineering benchmark spanning multiple languages and industrial challenges, a modest but useful improvement versus prior models.
- **OSWorld-Verified and cybersecurity CTF metrics:** OpenAI’s system card and reporting cite improvements on general "computer use" benchmarks (OSWorld) and on cybersecurity capture-the-flag style tasks (notable upticks vs. GPT-5.2-Codex).

## How can developers and organizations access GPT-5.3-Codex?

### In which products and interfaces is it available today?

- **Codex app (desktop & web):** OpenAI launched a dedicated Codex app that preserves sessions and syncs configuration with the CLI and IDE extension. For many users the app is the primary way to run agent workflows with a GUI and persistent state.
- **Codex CLI:** Terminal-first users can interact with Codex via a command-line interface that integrates with local repos and workflows.
- **IDE extensions:** Plugins for common IDEs (Visual Studio Code, JetBrains family) allow Codex to live inside the editor, proposing code, running local tests and executing changes in-place.
- **Web interface:** Standard web access through ChatGPT/Codex pages provides a no-install option for many users.

> **Important availability note:** OpenAI states GPT-5.3-Codex is available to **paid ChatGPT plans** across Codex surfaces, and that **API access is planned but not yet enabled** pending safety work.

While waiting for the [GPT-5.3 Codex API](https://www.cometapi.com/models/openai/gpt-5-3-codex/), developers can use the equally feature-rich GPT-5.2 Codex on [CometAPI](https://www.cometapi.com/) to prepare for migrating to GPT-5.3 Codex. When the GPT-5.3 Codex API is released, you can upgrade in minutes instead of starting from scratch.

### 1. Codex app (desktop)

- **Who:** individual devs and teams that want a GUI-centered coordination surface.
- **What:** syncs session history and configurations from the CLI and IDE, surfaces running agent tasks and logs, and acts as a hub for long-running operations.
- **How to start:** sign in with your ChatGPT account on the Codex app; sessions started in IDE/CLI appear in the app.

### 2. Codex CLI (terminal)

- **Who:** terminal-first developers, DevOps engineers, SREs.
- **What:** run Codex actions, execute commands, run tests, and receive structured feedback in-line with your project. The CLI is useful for automation and scripting with the model as a tool.
- **How to start:** install the Codex CLI (package and instructions available via OpenAI’s developer docs), sign in with your ChatGPT account or team credentials, and point it at your repository.

### 3. IDE extensions (VS Code and others)

- **Who:** editor-centric developers.
- **What:** in-editor assistance, pull request review automation (e.g., tag `@codex` on PRs to request automated review), and the ability to run agentic flows without leaving your editor. Extensions support account-based sign-in—no API key gymnastics for many workflows.

### 4. Web/ChatGPT

- **Who:** lightweight or exploratory users, product managers, and teams that want web access.
- **What:** GPT-5.3-Codex is available through the ChatGPT interface for paid subscribers. The web interface gives immediate access to Codex features in a browser.

### 5. API (coming soon)

- **Who:** companies that want to embed Codex into CI/CD pipelines, automated tooling, or proprietary platforms.
- **What to expect:** OpenAI states that API access for GPT-5.3-Codex is being prepared

## What does GPT-5.3-Codex mean for the developer ecosystem?

### Short-term impact

- **Productivity uplift for routine work:** many teams will see faster iteration on tests, refactors, and debugging. IDE and CLI integration lowers friction to adopt agentic workflows.
- **New patterns of collaboration:** engineers will increasingly interact with AI as a “teammate” — issuing steering commands, reviewing agent outputs, and trusting the model for repetitive—but critical—tasks such as code formatting, scaffolding, and routine fixes.

### Longer-term industry effects

- **Toolchain consolidation:** integrated agentic tooling (app + CLI + IDE) may reduce tooling fragmentation if teams embrace a single Codex-centered workflow.
- **Competition and specialization:** the same week’s releases from Anthropic and others underscore that providers are carving different niches (e.g., huge context windows vs. agentic coding speed), which will push enterprises to choose models by use-case rather than branding alone.

### Roles and workforce

- **Augmentation, not replacement (for now):** while Codex will automate many developer tasks, human engineers remain essential for architecture, safety, critical reasoning, and governance—especially when production safety is at stake. Codex changes the distribution of effort rather than outright eliminating roles.

Developers can access [GPT-5.2 Codex](https://www.cometapi.com/models/openai/gpt-5-2-codex/) via [CometAPI](https://www.cometapi.com/) now.To begin, explore the model’s capabilities in the [Playground](https://blendspace.ai/chat) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up fo code today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/gpt-5-3-codex-features-benchmarks-and-how-to-get-it/](https://www.cometapi.com/gpt-5-3-codex-features-benchmarks-and-how-to-get-it/).*
