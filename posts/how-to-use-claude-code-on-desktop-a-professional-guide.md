<!-- social-ops-fingerprint:dbfec156bcbb4878faf3d3a20670b475996998695c94193fd377200e5998accb -->
---
title: How to Use Claude Code on Desktop— a professional guide
---
# How to Use Claude Code on Desktop— a professional guide

![How to Use Claude Code on Desktop— a professional guide](https://resource.cometapi.com/blog/uploads/2026/01/How%2520to%2520Use%2520Claude%2520Code%2520on%2520Desktop.webp)

Anthropic this month pushed a desktop **preview** of Claude Code — a native desktop app that brings Anthropic’s agentic coding workflows out of the terminal and into a graphical environment with built-in support for running multiple, isolated coding sessions in parallel. The desktop preview is designed to sit alongside the web and mobile versions of Claude Code and focuses on two practical developer problems: running multiple AI agents on the same repository without stepping on each other, and making it easier to start local or cloud sessions from one GUI.

## What is Claude Code on Desktop?

Claude Code on Desktop is the native (preview) desktop application that lets developers run Claude Code sessions either locally or on Anthropic’s secure cloud infrastructure using a GUI rather than only the CLI. It combines the core agentic coding capabilities of Claude Code with desktop conveniences: session management, local environment integration, and one-click launching of web sessions. The app is explicitly positioned as a companion to Claude Code’s CLI and web offerings; it bundles a stable Claude Code runtime and manages versions for you to preserve a consistent and stable experience.

Why does this matter? Historically, AI coding tools ran either purely in the terminal (developers comfortable with CLI workflows) or purely in the cloud (browser UIs). The desktop app bridges that gap by enabling low-latency local runs and by letting you switch seamlessly to Anthropic-hosted (web) sessions when you need isolated cloud compute or enterprise controls. The desktop preview is particularly notable for supporting **multi-session parallelism** — you can run several independent Claude Code agents on the same repository simultaneously, each in its own Git worktree (isolated branch workspace) so the agents don’t conflict with each other. That’s the headline feature many teams will find immediately useful.

### How does the desktop edition relate to the web and CLI versions?

Claude Code began as a command-line tool and later expanded to web and mobile interfaces; the desktop preview builds on those foundations. The desktop app mirrors many of the capabilities available on the web (launching sessions, repository connections, viewable progress) but focuses on local workflow ergonomics—desktop UX, native installation, and tighter integrations with local Git repositories via worktrees—so that sessions can run concurrently without interfering with each other’s file state.

**See also** [Claude Code Web: What it is and how to use it](https://www.cometapi.com/claude-code-web-what-it-is-and-how-to-use-it/)

## 7 Excellent features of Claude Code on Desktop

### 1) Multi-session parallelism

Claude Code for Desktop supports running multiple independent Claude sessions at the same time. That means you can have one session focused on a bugfix, another writing tests, and a third generating documentation — all executing simultaneously rather than queuing in a single session. This parallelism speeds workflows and lets you delegate different tasks concurrently.

For example:

Suppose you have a project called my-app, and you want to:

- Have Claude change the homepage in one window;
- Have Claude optimize the database logic in another window.

Claude Desktop will automatically create for you:

```
~/.claude-worktrees/my-app/homepage/
~/.claude-worktrees/my-app/database/
```

Two independent copies (without conflict). This is like running two branches of development simultaneously, with Claude handling each for you.

### 2. .worktreeinclude: Make Claude aware of ignored files

Sometimes your project has files like .env or .local, which are usually ignored by .gitignore and won't be copied to the Claude working directory. Files listed in `.gitignore` aren’t automatically copied into new worktrees. Claude provides a new mechanism: You can create a .worktreeinclude file in the project root directory, telling it which files need to be copied.— a `.gitignore`-style list specifying which ignored files should be copied into newly created worktrees (for example, local `.env` files or developer-specific settings). Only files that *both* appear in `.worktreeinclude` and `.gitignore` are copied, which avoids accidentally duplicating tracked files. This is critical for preserving per-session secret or environment files without checking them into Git.

For example:

```
.env
.env.local

.env.production

**/.claude/settings.local.json
```

This means: When Claude creates the working directory, these files will also be copied.

Note:

- Only files that exist in both .gitignore and .worktreeinclude will be copied;
- Avoid accidentally copying important tracked files.

### 3) Launch and sync with web/cloud sessions

The desktop app can act as a launcher for web/cloud sessions—meaning you can kick off cloud-based Claude Code sessions from the desktop UI and monitor or steer them locally. This hybrid mode is useful if you want the convenience of local controls with the scaling or permissions model of cloud-hosted runs.

Note:

- When running in the cloud, Claude's tasks will execute on the Anthropic security server.
- The switching between local and cloud environments is seamless.
- To create a session, simply select "remote environment".

### 4) Launch and sync with web/cloud sessions

The desktop app can act as a launcher for web/cloud sessions—meaning you can kick off cloud-based Claude Code sessions from the desktop UI and monitor or steer them locally. This hybrid mode is useful if you want the convenience of local controls with the scaling or permissions model of cloud-hosted runs(local for quick tasks, cloud for risky or resource-heavy tasks).

### 5) Bundled Version and Enterprise Configuration

Desktop includes a bundled, stable Claude Code runtime that is downloaded on first launch and automatically managed. Enterprise admins can disable local Claude Code use if required (`isClaudeCodeForDesktopEnabled` enterprise policy). Desktop installers support common enterprise deployment formats (MSIX for Windows, PKG for macOS), and administrators can control updates and extension access. These controls are designed to make adoption easier for large teams.

Note:

- The application will automatically download upon first opening;
- The desktop application automatically manages version updates;
- It automatically cleans up old versions to keep the system clean;
- Even if you have the CLI version installed on your computer, it will still use its own version (for greater stability).
- The desktop version prioritizes stability and compatibility; the CLI (command-line version) may update faster, but new features may not be immediately synced to the desktop version.

### 6) Custom Environment Variables

Claude Desktop allows you to set variables just like .env files.

These variables only take effect within the Claude session, making them ideal for project configuration.

For example:

```
API_KEY=abcd123
DEBUG=true
CERT="-----BEGIN CERT-----
MIIE...
-----END CERT-----"
```

### 7) Integrate with local tools and environments

When running local sessions, the desktop app extracts your shell `$PATH` so session processes can use the same node, npm, yarn, Python, or other CLI tools you rely on. It also provides a UI for adding custom environment variables (in `.env` format), with values masked for security. This makes running tests or builds inside an agentic session smoother because the agent can invoke the same toolchain as your terminal.

## How do I install Claude Code on Desktop?

This section walks through the installation process with minimal friction. The instructions below are current for the desktop preview and point you to the canonical installers.

### Pre-requisites and account setup

1. **Anthropic account and workspace**: Claude Code ties into the Anthropic Console. You will need to complete an OAuth flow in the Claude Console and have an active billing or research preview access as required by Anthropic’s workspace model. Claude Code uses an internal workspace in the console for tracking usage; you cannot create API keys for that workspace — it’s managed for Claude Code usage.
2. **Git and repo readiness**: Ensure Git is installed and that the project you want to operate on is a Git repository (or initialize Git). The desktop app expects valid repos for features like worktrees; if you open a folder without Git initialized, a worktree will not be created.
3. **OS specifics**: macOS and Linux installations are generally native binaries; Windows users are recommended to use WSL for full command compatibility in many workflows. Some community guides cover advanced Windows/WSL setups if you run into PATH or distribution issues.

### Step-by-step installation (short)

1. Open the Claude Download page and choose the correct installer for your platform.
2. Run the installer (PKG on macOS, MSIX or EXE on Windows). For enterprise fleets, use the MSIX/PKG packages provided for centralized deployment.
3. Launch the Claude Desktop app and sign in with your Anthropic/Claude account. Your conversations and preferences sync across desktop, web, and mobile.
4. On first launch the app will download a bundled Claude Code runtime. Allow that download to complete; it’s required and ensures a stable, managed version is used.

### Post-installation checks

• Open Settings > Environments and confirm the desktop app has extracted your shell `$PATH`.
• Choose whether you want local sessions enabled (if your machine and policy allow them) or whether your workflow will create web sessions instead.

### Optional installation method should I choose

- **Native installer (recommended)**: Use the native OS installer for the simplest, most integrated experience.
- **Homebrew (macOS)**: Convenient for macOS users who manage apps with Homebrew.
- **NPM or script-based installers**: Useful for more automated or scripted setups (CI or provisioning), or for Linux distributions where a simple installer script is preferred.

### Installation: macOS, Linux, WSL (recommended flow)

1. Download the desktop preview installer from the Claude Code downloads page (the in-product docs provide the installer link).
2. Run the installer and open the Claude desktop app.
3. Complete the OAuth sign-in through the in-app Claude Console flow.
4. Configure default worktree location and local/remote execution preferences in the desktop settings.
5. Open a project folder or clone a repo from the UI to begin.

Open a terminal and, if you trust the source, run the install script provided by Anthropic (this is the typical recommended convenience option). Example (paraphrased):

```
# macOS / Linux / WSL (example convenience installer)
curl -fsSL https://claude.ai/install.sh | bash
```

Alternatively, if you prefer Homebrew on macOS:

```
brew install --cask claude-code
```

### Installation: Windows

WSL：

1. Install WSL (Ubuntu is common) and set up a clean WSL environment. Resolve PATH and interop issues so the desktop app’s WSL integration can access the distro.
2. Install Git and any language runtimes in WSL that Claude might need for local runs (node, python, etc.).
3. Install or run the desktop app on Windows, point it to your WSL project directory (or launch the desktop app inside WSL if supported), and follow the same OAuth flow.

PowerShell example (paraphrased):

```
# PowerShell (example convenience installer)
irm https://claude.ai/install.ps1 | iex
```

CMD example (paraphrased):

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

## How do I use Claude Code on Desktop in daily practice?

### What are the recommended session-creation patterns?

Short independent tasks vs long-running refactors

- For **short, scoped tasks** (bugfix, single-file change, tiny refactor), create a session per task and let Claude produce a focused commit. Review and merge promptly.
- For **long-running efforts** (large refactors, feature development), consider creating a session that checkpoints frequently and uses the desktop UI’s progress controls to steer or pause work. Keep sessions on feature branches to avoid accidental merges.

Maintain a `CLAUDE.md` or a prompt template in your repo to standardize how sessions should be prompted (context, tests to run, style rules). This practice reduces variability and helps Claude produce consistent results across sessions. Many teams store standard prompts or guardrails in repo metadata to ensure predictable agent behavior.

### Launching and naming a session

1. Open the desktop app and select or clone a repository.
2. Click “New Session” (or equivalent) and give the session a descriptive name (e.g., `bugfix/cs-142` or `add-tests-login`). Naming helps you distinguish simultaneous sessions in the UI.
3. Choose **local** or **remote** execution mode, pick a target branch (or let the agent create a branch in a new worktree), and start the session. The app creates a dedicated Git worktree for the session automatically.

### Steering the agent: prompts and tasks

- Use **clear, scoped prompts**. Example: “Find the failing unit test for `AuthService` and create a fix that preserves existing public API; run tests and report results.”
- For incremental tasks, ask Claude to generate a plan first (a short checklist), then request the specific code changes step by step. Incremental progress reduces hallucination risk and makes diffs easier to review. Anthropic recommends this approach in best practices.

### Watching progress and interacting

The desktop UI shows action logs and diffs as the agent works. You can pause a session, change instructions, or cancel a running job. When the agent proposes edits, the UI surfaces file diffs and an explanation of what changed. Approve, edit, or reject the proposed diffs before commit.

### Commit, branch, and PR flows

Once you approve changes, the desktop app can commit into the session’s worktree branch. From there you can push to origin and open a pull request through the UI (if you’ve authorized GitHub access). Each session’s branch remains isolated until you merge, which keeps human review simple.

## How does Git isolation and multi-session parallelism actually work?

### Git worktrees: the isolation mechanism

Anthropic’s desktop uses Git **worktrees** to create per-session copies of a repository’s working tree tied to separate branches. Worktrees are lighter than full clones — they share the same `.git` metadata where appropriate but provide independent working directories so concurrent edits won’t conflict or leak across sessions. The desktop places these automatically created worktrees in a configurable directory (default `~/.claude-worktrees`). This design enables safe concurrency for agentic operations.

### Why worktrees vs clones

Worktrees are faster to create and easier to correlate with the same underlying Git history, while still providing the filesystem separation required to avoid cross-session contamination. For most workflows this is preferable to multiple full clones; however, if you need full, isolated runtime environments with different dependencies, a separate clone or container might still be desirable.

### Coordination and conflict handling

Because each session works in an isolated branch/worktree, conflicts are minimized. If two sessions independently change the same logical code and both are merged into the same target branch later, normal Git merge conflict handling will apply — which is the correct point for human review and resolution. Anthropic’s model intentionally surfaces commits as reviewable PRs, keeping humans in the merge loop.

## Common troubleshooting steps and limitations

### If a session fails to start or hangs

- Confirm repository access tokens are valid and not rate-limited.
- Check local disk space and permissions for the worktrees directory (e.g., `~/.claude-worktrees`).
- Review desktop app logs for error messages; the app usually exposes a diagnostics view or log file.

### If sessions contaminate each other

- Confirm the desktop app is creating separate worktrees (inspect the `~/.claude-worktrees` directory or the worktree location set in app preferences).
- If you see shared state, ensure you are using the latest desktop preview or consult Anthropic’s docs—this release specifically addresses session isolation.

### If ignored files aren’t available to sessions

Add the filenames to your `.worktreeinclude` configuration (or the desktop UI equivalent) so the app copies required ignored files (e.g., `.env`) into each worktree securely. Avoid storing secrets in, or exposing them from, worktrees without proper secrets management.

## Conclusion

Claude Code’s desktop preview represents a meaningful evolution in how agentic coding tools fit into developer workflows: it keeps the speed and expressiveness of AI agents while solving several practical coordination problems developers face when multiple agents need to operate on the same codebase. Whether you adopt it for single-developer productivity or to coordinate multiple agent tasks across a team, understanding Git worktrees, `.worktreeinclude`, and the distinction between local vs. web sessions will make your first week with the desktop preview far more productive.

Ready to use Claude Code cli? consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions.

Developers can access [Claude Opus 4.5 API](https://www.cometapi.com/claude-opus-4-5-api/) etc through CometAPI, [the latest model version](https://www.cometapi.com/pricing/) is always updated with the official website. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Free trial of Claude opus 4.5](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-use-claude-code-on-desktop/](https://www.cometapi.com/how-to-use-claude-code-on-desktop/).*
