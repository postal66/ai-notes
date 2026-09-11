<!-- social-ops-fingerprint:acdc78e972970e16ff595f7a983963fbaf27ac57c6c0f7c4b6b7d08816e7e9e7 -->
---
title: How to make the Codex app work on Windows/Linux
---
# How to make the Codex app work on Windows/Linux

![How to make the Codex app work on Windows/Linux](https://resource.cometapi.com/How%20to%20make%20the%20Codex%20app%20work%20on%20WindowsLinux.webp)

OpenAI’s Codex is a new “command center” for agent-driven software development: a desktop app + CLI + IDE extensions that let developers run multi-agent coding workflows, create isolated worktrees for experiments, and automate large, long-running engineering tasks. OpenAI’s Codex app is a desktop interface for running and orchestrating AI coding agents locally and in the cloud. It launched on macOS and — as of early March 2026 — was expanded to Windows, with Linux support planned.

## What is the Codex app — and why it matters

Codex is a family of AI coding agents and related tooling that help developers write, refactor, test, and orchestrate code through agent workflows, long-running tasks, and multi-agent coordination. The Codex *app* is a desktop product that brings those agents into a single UI for project management, parallel agent threads, and persistent/cloud-backed threads. The app complements the Codex CLI and IDE integrations (e.g., plugins) and is designed to be the "mission control" for agentic coding.

Why this matters now:

- **Productivity multiplier:** Agentic workflows let you run many tasks in parallel — e.g., generate scaffold code, run test suites, and triage bug reports — saving real developer time.
- **Long-running automation:** Codex can maintain and progress tasks across hours or days (important for CI investigations, dependency upgrades, or large refactors).
- **Platform integration:** OpenAI has expanded Codex into desktop and IDE experiences, and the app now supports Windows natively (and macOS already), which broadens reach to more developers. Early metrics reported the macOS version topped one million downloads in its first week — a signal of strong demand.
- **Competitive momentum:** The app launch is part of a broader race with other vendors adding agentic coding features (context from industry coverage).

OpenAI is iterating rapidly — frequent changelog entries in late Feb 2026 show daily fixes and performance improvements, so expect the app to evolve while you integrate it into your workflow.

### Current availability & supported workflows

- The Codex **CLI** is supported on macOS, Windows, and Linux and can be installed via package managers (npm/Homebrew) or by downloading platform binaries. The CLI runs locally, can inspect and edit repositories, and prompts you to sign in with ChatGPT or an API key.
- The Codex **desktop app** (GUI) shipped first on macOS; Windows availability was added in a follow-up update. At the time of writing, a sign-up form exists for Linux desktop availability (OpenAI solicits distro info). If you want a Linux GUI today, your options are: use the CLI + IDE extensions, run the cloud/web Codex at chatgpt.com/codex, or (for adventurous users) run community projects that port the macOS Electron app to Linux (unofficial).

## 3 Ways to run Codex on your machine

There are three practical modes for Windows and Linux users:

1. **Native desktop app (Windows):** Official Windows build (native sandboxing, PowerShell integration). Recommended for most Windows desktops.
2. **WSL (Windows Subsystem for Linux) + Codex app:** Useful if you prefer a Linux environment or your developer toolchain is Linux-native. The Windows app can be configured to use WSL for agent runtime.
3. **Linux (CLI / developer mode):** While the desktop Linux build was initially “coming soon,” you can run the Codex CLI, IDE plugins, or community efforts to run the desktop experience on Linux (or follow OpenAI’s notification sign-up). The codex CLI repo (OpenAI) is available for local agent workflows.

### System requirements & security considerations (summary)

- **Windows:** Windows 10/11 (64-bit). Native PowerShell and Windows sandbox available in the Windows app to limit untrusted code execution. If you use WSL, WSL2 is recommended.
- **Linux:** Varies by distro. The desktop app is not yet generally available; use the CLI or IDE plugins for now. Signup is available to be notified about Linux builds.
- **RAM/CPU:** Agent workloads can be heavy if you ask them to run tests or builds — plan for multiple cores and 8–16GB RAM for casual use, more for heavy concurrency.
- **Security best practice:** Use the app’s sandboxing features, run agents with least privilege, isolate project directories, and use short-lived API keys or user sign-in rather than embedding keys in repos.

## How to make the Codex app work on **Windows** — step-by-step

> Two normal scenarios on Windows:1) Use the native Codex **desktop app** (Microsoft Store / native installer).
> 2) Use the **Codex CLI** in PowerShell or WSL, optionally paired with the VS Code extension.

Below is a practical, tested-style sequence: install, configure, connect to WSL (optional), and troubleshoot.

### 1) Download & install the official Windows Codex app

1. Visit the Codex app page and download the Windows installer (MSI/EXE) from the official docs/download page. (OpenAI’s Codex app page shows the Windows download and Windows support notes.)
2. Run the installer as Administrator. If Windows SmartScreen warns, verify the publisher and allow installation.

**PowerShell example (silent install via admin prompt):**

```
# From an elevated PowerShell prompt (Admin)$installer = "C:\path\to\Codex-Setup.exe"Start-Process -FilePath $installer -ArgumentList "/S" -Wait
```

### 2) First run, sign-in, and API vs. account mode

Launch Codex from Start Menu. On first run you’ll be prompted to sign in with your ChatGPT/OpenAI account or provide an OpenAI API key. Signing in with your account gives the smoothest experience (cloud threads, persistent state). Using an API key works but may limit certain cloud features. See the developer docs for exact differences.

**Set API key as environment variable (PowerShell):**

```
# Temporary for session$env:OPENAI_API_KEY = "sk-..."# Permanent (example - user environment)setx OPENAI_API_KEY "sk-..." /M
```

> **Security tip:** Prefer interactive sign-in or short-lived keys; avoid checking keys into source control.

### 3) Configure sandboxing and PowerShell integration

The Windows app runs agent tasks using a native sandbox to reduce risk of arbitrary host modification. Check the app’s Security or Settings page to toggle sandbox strictness and review which directories are shared with agents.

If you prefer PowerShell for agent hooks, ensure the app is allowed to run PowerShell profiles and that your execution policy permits the required scripts. Example to set an execution policy (admin):

```
Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### 4) Optional: configure Codex to use **WSL2** (recommended if you have Linux toolchains)

If you develop in Linux toolchains (apt, pip, make, systemd services), configure Codex to execute agent tasks in WSL2 rather than native Windows:

**Install WSL2 (if not already):**

```
# Run in an elevated PowerShellwsl --install# Reboot if requested
```

**Choose distribution (Ubuntu recommended):**

```
wsl --install -d Ubuntu
```

Inside the Codex app Settings → Runtime, choose **WSL** as the execution backend and point Codex to the default WSL distro (e.g., `Ubuntu`). The app will then spawn agent processes inside your WSL environment so that Linux toolchains and file paths behave natively.

### 5) Verify installation & run a smoke test

From the app UI, create a simple agent task to scaffold a small program and run the unit tests. Alternatively, use the CLI:

**CLI test (PowerShell):**

```
# Check codex version (if installed)codex --version# Run a quick agent job (pseudo-command; follow CLI docs)codex agent run --task "create python app skeleton with pytest" --project "demo"
```

If the CLI is not on PATH, add the installation folder to your PATH or use the launcher supplied by the installer.

### 6) Troubleshooting common Windows issues

- **App won’t start:** Check Windows Event Viewer and `%LOCALAPPDATA%\Codex\logs`.
- **Sandbox blocks agents from writing files:** Adjust app settings for folder sharing or map a project folder to the app’s allowed list.
- **PowerShell scripts blocked:** Revisit execution policy and unblock scripts (`Unblock-File path\script.ps1`).
- **Agent fails to use WSL:** Ensure WSL2 is installed and that the distro is initialized (first-run completes). Use `wsl -l -v` to check status.

## H2 — How to make the Codex app/CLI work on **Linux** (step-by-step)

> Two practical Linux approaches:1) **Officially supported:** Codex CLI + IDE extension (fully supported).
> 2) **Unofficial GUI:** community bridge projects that run the macOS Electron app on Linux (experimental, not supported).

At the time of writing, OpenAI’s desktop Linux app was announced as coming soon and users can sign up for notifications; however, the Codex CLI and developer integrations are available and are the practical path for Linux users. Additionally, community cross-platform rebuilds exist for advanced users.

### Official path: Codex CLI + VS Code (stable, recommended)

The most robust, supported Linux experience today is the CLI plus the Codex IDE extensions (VS Code, Cursor, etc.). The CLI is explicitly supported on Linux.

**Step 1 — Prepare your system (Ubuntu example)**

```
# update OSsudo apt update && sudo apt upgrade -y# install build essentials & gitsudo apt install -y build-essential git curl# install Node.js via nvm (recommended)curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash# restart shell or source ~/.bashrc, then:nvm install --lts
```

**Step 2 — Install Codex CLI**

```
# install globally without sudo (using npm + nvm)npm install -g @openai/codex# verifycodex --version
```

**Step 3 — Authenticate**

```
# run the interactive CLI to authenticatecd /path/to/your/repocodex# follow the sign-in prompt: sign in with ChatGPT (OAuth) or paste API key
```

**Step 4 — Use codex**
Examples:

```
# interactive modecodex# single-shot non-interactivecodex "Write unit tests for utils/crypto.js"# run specific commands# create a sandboxed change and show diffcodex "Add a users table migration" --dry-run
```

**Step 5 — Use Git worktrees (recommended)**

```
# from repository rootgit checkout -b maingit worktree add ../codex-sandbox codex-sandbox-branchcd ../codex-sandbox# run Codex here so it operates on an isolated worktreecodex
```

**Security & config**

- The CLI stores config in `~/.codex/config.toml` (defaults/overrides) — be mindful of permissions. Use OS credential stores (Secret Service / Gnome Keyring / pass) or environment variables for API keys rather than plaintext files when possible.

### Unofficial path: running the desktop GUI on Linux (experimental)

OpenAI’s desktop app started on macOS and Windows; Linux users currently can sign up for notifications for an official Linux release. Meanwhile, community projects have reverse-engineered ways to run the macOS Electron bundle on Linux by extracting `app.asar`, recompiling native modules, and launching a local `codex app-server` backend to connect the UI. This approach is **unsupported** and may break with updates—use only for experimentation and never on production code or sensitive repos.

**If you still want to try (high-level):**

1. Download macOS `.dmg` (from official source you control).
2. Extract the `app.asar` (Electron package).
3. Rebuild native Node modules for Linux (node-pty, better-sqlite3, etc.).
4. Install the Codex CLI and run a local `codex app-server` to act as the backend.
5. Create a wrapper script that sets environment variables and launches the unpacked Electron UI connected to the local backend.

*Do not do this on sensitive machines. Community repos and scripts exist to automate these steps, but they’re not official support channels.*

## Best practices: security, performance, and team workflows

### Security — keep your host safe

- **Use sandboxing:** When possible, enable the app’s strict sandbox or run agent workloads in containers/VMs. The Windows build adds native sandbox support; prefer it for untrusted code.
- **Least privilege for file mounts:** Only share specific project folders with the app.
- **Short-lived credentials:** Use short-lived API keys, role-based tokens, or interactive sign-in. Rotate keys and audit their use.
- **Repository hygiene:** Never commit secrets — use `.gitignore` and secret scanners. Use environment variables or secret stores.

### Performance — manage resource contention

- **Throttle agent concurrency:** Don’t run dozens of full builds in parallel on a modest laptop. Use the app’s concurrency settings or scheduler.
- **Use WSL or containers for heavy tasks:** Offload heavy builds and tests to WSL or a containerized environment to avoid Windows filesystem performance pitfalls.
- **Profile tasks:** Use CPU/RAM monitoring (Task Manager, top, htop) while agents run to understand bottlenecks.

### Team workflow recommendations

- **Shared configurations:** Keep agent recipes (task prompts, toolchains, launch scripts) in a shared `codex/` directory (without secrets) so the team can reproduce agent runs.
- **CI gatekeeping:** Use Codex agents to propose code changes, but gate merging with CI checks — don’t let an agent auto-merge without human review.
- **Logging & audit:** Enable detailed logging for agent actions so you can trace what an agent did and roll back if needed.

## Troubleshooting matrix (quick reference)

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| App crashes on start | Corrupted install / missing native runtime | Reinstall, check %LOCALAPPDATA%/Codex/logs or ~/.local/share/codex logs |
| Agent cannot access files | Sandbox or file share restriction | Add project folder to allowed list / adjust sandbox settings |
| CLI command not found | PATH not set | Add CLI install dir to PATH or symlink to /usr/local/bin |
| WSL tasks failing | Distro not initialized / permission mismatch | Ensure wsl -l -v shows running distro; set proper file permissions inside WSL |
| Excessive memory use | Parallel agents running tests/builds | Lower concurrency or run heavy tasks in a server/CI |

## Closing notes

The Codex app represents a concrete step toward agentic, long-running automation for developers. With the Windows release and ongoing iteration, developers now have more ways to run, orchestrate, and integrate Codex into cross-platform workflows. If you’re installing it for the first time, favor the official Windows installer or the official CLI on Linux; prefer sandboxing and WSL for compatibility with Linux toolchains; and follow the security and operational best practices above.

CometAPI is a one-stop aggregation platform for large model APIs, offering seamless integration and management of API services. It supports the invocation of various mainstream AI models, such as  [Claude Sonnet](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/)/ [Opus 4.6](https://www.cometapi.com/models/anthropic/Claude-Opus-4-6/) and [GPT-5.3 Codex](https://www.cometapi.com/models/openai/gpt-5-3-codex/). Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate Codex.

Ready to Go?→ [Sign up for coding today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-make-the-codex-app-work-on-windowslinux/](https://www.cometapi.com/how-to-make-the-codex-app-work-on-windowslinux/).*
