<!-- social-ops-fingerprint:8ce6457cf58c38b0ab766b82fb26fc35e0f188ba97206b7a8382d85b7182188b -->
---
title: How to Install OpenAI’s Codex CLI Locally? A Simple Guide
---
# How to Install OpenAI’s Codex CLI Locally? A Simple Guide

![How to Install OpenAI’s Codex CLI Locally? A Simple Guide](https://resource.cometapi.com/blog/uploads/2025/06/codex-cli.webp)

OpenAI’s Codex CLI has quickly become a must-have tool for developers seeking to integrate AI directly into their local workflows. Since its announcement on April 16, 2025, and subsequent updates—including internet-access capabilities on June 3, 2025—the Codex CLI offers a secure, privacy-focused, and highly customizable way to harness OpenAI’s powerful reasoning models right from your terminal. This article synthesizes the latest developments and provides a step-by-step guide to installing and configuring the Codex CLI on your machine.

## What Is OpenAI’s Codex CLI?

### Origins and Announcement

OpenAI unveiled the Codex CLI alongside its newest models, o3 and o4-mini, positioning it as an experimental, open-source project that brings AI-powered coding assistance directly to the terminal. Announced on April 16, 2025, this tool allows AI agents to read, modify, and execute code in your local environment, ensuring that sensitive code never leaves your machine.

### Key Features of Codex CLI

- **Lightweight and Open Source**: Designed for easy installation and community contributions, Codex CLI’s codebase lives on GitHub, encouraging bug reports and pull requests.
- **Natural-Language Commands**: Developers can prompt Codex in plain English to generate boilerplate code, refactor existing modules, or even write tests.
- **Local Execution**: All operations occur on your machine, eliminating concerns about uploading proprietary code to external servers .
- **Agent Internet Access**: As of June 3, 2025, Codex CLI can optionally access the internet for tasks like installing dependencies or fetching external resources, with granular domain and method controls .

### What are the latest architectural updates?

In early June 2025, OpenAI announced a major rewrite of the Codex CLI from its original Node.js and TypeScript stack into Rust. This shift aims to deliver “zero-dependency installation,” improved performance, and enhanced security guarantees by leveraging Rust’s memory-safe design. Developers can expect faster startup times, reduced binary sizes, and more robust compilation checks, all contributing to a smoother developer experience.

## Why Should You Install Codex CLI Locally?

### What Security and Privacy Benefits Does Local Installation Offer?

Running AI models locally means your source code remains on-premises. Unlike cloud-only solutions, Codex CLI never shares your files unless you explicitly request it, significantly reducing risks related to data leaks or unauthorized access.

### How Does Local Installation Enhance Performance and Offline Capability?

By processing commands on your own hardware, Codex CLI minimizes latency and dependencies on external API calls. Coupled with the new internet-access agent feature, you can work offline for most tasks and configure when the agent is allowed online, striking the right balance between autonomy and connectivity .

## How to Prepare Your Environment for Installation?

### What Are the Prerequisites?

Before installing Codex CLI, ensure you have:

- **Node.js (v14 or later)** installed and added to your `PATH`.
- **npm** (usually bundled with Node.js) for package management.
- A **valid OpenAI API key**, which you can obtain from your OpenAI dashboard under API settings .

### How Do You Obtain and Secure Your OpenAI API Key?

1. Log in to the [OpenAI dashboard](https://platform.openai.com/).
2. Navigate to **API Keys** and click **Create new secret key**.
3. Copy the generated key and store it in a secure credential manager.
4. Avoid committing it to version control; use environment variables for local development.

## How Can You Install Codex CLI on Different Operating Systems?

### How Do You Install via npm on macOS and Linux?

Open your terminal and run:

```
npm install -g @openai/codex
```

This command installs the `codex` executable globally, making it accessible from any directory .

### How Do You Install on Windows (PowerShell or Git Bash)?

1. Open **PowerShell** (as Administrator) or **Git Bash**.
2. Execute the same npm command: `npm install -g @openai/codex`
3. Optionally, set up Git Bash as your default shell with: ```` Set-Alias sh.exe "C:\Program Files\Git\bin\bash.exe" ``` :contentReference{index=10}. ````

## How Do You Configure and Authenticate Codex CLI?

### How Do You Set Environment Variables?

After installation, configure your API key by exporting it in your shell profile:

```
export OPENAI_API_KEY="your-api-key-here"
```

Add this line to `~/.bashrc`, `~/.zshrc`, or `~/.profile` for persistence .

### How Do You Log In with ChatGPT Integration?

Codex CLI supports a simplified login flow for ChatGPT Plus and Pro subscribers:

```
codex --free
```

This command guides you through authenticating with your OpenAI account and redeeming any eligible credits .

## How Can You Verify the Installation?

### How Do You Check the Version?

Run:

```
codex --version
```

A successful installation returns a version string (e.g., `0.1.0`), confirming that the CLI is reachable ).

### How Do You Run a Test Command?

Try a simple prompt to ensure everything works:

```
codex "Create a Python function to reverse a string."
```

Codex CLI should output the corresponding Python code directly in your terminal, demonstrating its core functionality.

### How do I keep the CLI up to date?

With npm:

```
npm update -g @openai/codex
```

With Rust binary:

1. Download the latest release from GitHub.
2. Replace your existing binary with the newly downloaded version.

Alternatively, if you installed via a package manager that supports updates (e.g., Homebrew), you can use its update commands.

## How do I extend and customize Codex CLI?

### Configuration options in codex.yml

Edit `codex.yml` to:

- Exclude directories (e.g., `node_modules`, `vendor`)
- Set default prompt templates
- Choose fallback models or local open-source alternatives (such as StarCoder for offline use) .

### Scripting and automation

Incorporate Codex CLI into build scripts or CI workflows:

```
yaml# .github/workflows/codex.yml

jobs:
  ai_lint:
    runs-on: ubuntu-latest
    steps:
- uses: actions/checkout@v3
- name: Run Codex Auto-Edit
        run: |
          codex --mode auto-edit "Optimize bundle size and tree-shake unused imports"
- name: Run Tests
        run: npm test
```

This enables continuous AI-driven code improvement alongside standard linters.

## What Are Best Practices and Tips for Using Codex CLI?

### How Should You Manage Internet Access for Agents?

By default, internet access is disabled. To grant access for specific tasks, use:

```
codex --allow-internet
```

Then specify the domains or HTTP methods you trust. This ensures that Codex only reaches out when you explicitly permit it, preserving security and auditability .

### How Can You Contribute and Report Issues?

As an experimental project, community feedback is vital. To contribute:

1. Fork the [GitHub repository](https://github.com/openai/codex) and submit pull requests.
2. File issues for bugs or feature requests, clearly describing steps to reproduce.
3. Engage with maintainers in discussions to help shape future directions .

---

By following the steps outlined above, you can seamlessly integrate OpenAI’s Codex CLI into your local development workflow—benefiting from the latest AI advances while maintaining full control over your code and environment. As the project evolves, keep an eye on the official changelog and community forums for updates, and don’t hesitate to share your experiences and enhancements with the broader developer community.

## Getting Started

CometAPI provides a unified REST interface that aggregates hundreds of AI models—under a consistent endpoint, with built-in API-key management, usage quotas, and billing dashboards. Instead of juggling multiple vendor URLs and credentials.

Developers can access chatGPT API suah as [GPT-4.1 API](https://www.cometapi.com/gpt-4-1-api/) those ***Deadline for article publication***through [CometAPI](https://www.cometapi.com/). To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide]for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

**See Also [Claude Code vs OpenAI Codex: Which is Better](https://www.cometapi.com/claude-code-vs-openai-codex/)**

---

*Originally published at [https://www.cometapi.com/how-to-install-openais-codex-cli-locally/](https://www.cometapi.com/how-to-install-openais-codex-cli-locally/).*
