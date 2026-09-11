<!-- social-ops-fingerprint:d544956a887cda8470d388b33f8e9818e4a94e45cf821cf42e106697840924ff -->
---
title: How to change gemini cli directory
---
# How to change gemini cli directory

![How to change gemini cli directory](https://resource.cometapi.com/blog/uploads/2025/12/how%2520to%2520change%2520gemini%2520cli%2520directory.webp)

Google’s open-source **Gemini CLI**—the terminal-based AI agent that brings Gemini into your shell—has rapidly matured since launch and now supports rich configuration, project context files (`GEMINI.md` / `.gemini`), custom slash commands, and workspace directory controls. The project is actively evolving on GitHub (official repo), has entered public preview with generous quotas, and is being integrated into other developer tools (editor integrations and CI/Actions). But as teams scale, or when you work across drives or restrictive environments (containers, company-managed laptops, Cloud Shell, Windows systems), you’ll quickly bump into a practical question: where does Gemini store its files, and how can you change which directories Gemini reads and writes?

## What is Gemini CLI?

Gemini CLI is Google’s open-source command-line AI agent that brings the power of the Gemini models directly into your terminal. It provides interactive agent capabilities for code assistance, file and project inspection, executing shell commands (with safeguards), and integrating tools such as Google Search, Model Context Protocol (MCP) extensions, and media generation tools shipped with Gemini. The CLI is intended to be lightweight, scriptable, and extensible; it’s available from the official repository and packaged for easy installation.

### Why the directory matters

Gemini CLI stores configuration (for example, `settings.json`), system prompts or context (`GEMINI.md`), cached credentials, telemetry identifiers, and other persistent state inside a `.gemini` directory. Where that directory lives controls:

- which settings the CLI loads (global vs. project-specific),
- what “memory” files the agent will read,
- where credentials are cached (affects login behavior),
- cross-machine or CI reproducibility when you want to provide a custom config repo.

Understanding and (if necessary) changing the directory helps in multi-project workflows, CI, containerized deployments, and teams with centralized config stores.

## Where does Gemini CLI store configuration by default?

By default the CLI uses a `.gemini` directory. For most user installations that resolves to `~/.gemini` (the `.gemini` folder in your home directory). The CLI also supports project-level `.gemini` files (e.g., `.gemini/settings.json` in the project root) which override user settings while you’re operating from that project folder. System-level settings are read from OS-specific locations (for example `/etc/` on Linux or `%PROGRAMDATA%` on Windows) when applicable. Typical paths:

- Linux / macOS: `~/.gemini/` (for example `/home/alice/.gemini` or `/Users/alice/.gemini`).
- Windows: `%USERPROFILE%\.gemini` (e.g., `C:\Users\Alice\.gemini`).
  Inside `.gemini` you’ll typically find `settings.json`, `GEMINI.md`, `commands/`, and local caches. The CLI also reads per-project `.gemini/` folders (project root) for project-level settings.

This default is important: historically the config directory has been hard-coded to `.gemini` in the home directory

---

## How can I change or redirect Gemini CLI’s configuration directory?

There are several practical ways — from the simplest (work in the desired folder) to the more robust (environment variables or filesystem redirects). Choose an approach depending on whether you control the runtime environment (local dev machine vs. CI), which OS you’re on, and whether you prefer a temporary or permanent change.

### 1) Use a project-level `.gemini` (recommended for per-project settings)

If you want per-project settings, create a `.gemini` subdirectory in your project root and place `settings.json`, `GEMINI.md`, and other project files there. Gemini CLI prefers project settings when you run it from that project directory:

```
your-project/├─ .gemini/│  ├─ settings.json│  └─ GEMINI.md└─ src/
```

Start `gemini` while your shell is at `your-project/` and the CLI will pick up `.gemini` files from that tree (it searches upwards to find project context). This is the safest, explicit method for per-project configuration.

### 2) Use documented environment variables (when supported)

The Gemini CLI codebase and docs reference several environment variables used to alter behavior. Some of these are intended for system settings or special file overrides:

- `GEMINI_API_KEY`, `GEMINI_MODEL`, etc. are commonly used for authentication and model choice.
- There are references in the codebase and docs to variables such as `GEMINI_CLI_SYSTEM_SETTINGS_PATH` (used to override system settings path) and constants like `GEMINI_CONFIG_DIR` (the default `.gemini` name used in code). Some community requests and PRs propose adding or honoring a `GEMINI_CONFIG_DIR` environment variable to let users relocate the whole config directory.

**Example (bash / macOS / Linux):**

```
# Temporary for this shell sessionexport GEMINI_CONFIG_DIR="$HOME/custom_gemini_dir"​# Or override system settings path if your install supports it:export GEMINI_CLI_SYSTEM_SETTINGS_PATH="/etc/my-gemini/system.settings.json"​# Then rungemini
```

**PowerShell (Windows):**

```
$env:GEMINI_CONFIG_DIR = 'C:\Users\you\CustomGemini'gemini
```

> Important caveat: as of the latest community discussion and issues, `GEMINI_CONFIG_DIR` has been requested and referenced in code in places — but platform-specific bugs and inconsistent behavior (particularly on Windows) have been reported. That means environment-variable-based redirection may not be uniformly reliable on every platform or release. Check the Gemini CLI release notes and repo issues for your installed version if you rely on this.

### 3) Add directories to Gemini’s workspace inside a session

If you want Gemini to be aware of additional directories (so it can read files as context), there’s an interactive `/directory` command set. For example:

```
/directory add path/to/another/project/directory list
```

This does not move the config directory, but it allows the agent to include files from other directories in its workspace context. This is useful when you want the agent to reference other repositories without changing your global config.

### 4) Create a symlink or filesystem bind (practical workaround)

If the CLI refuses to accept environment overrides or you need a reliable cross-process solution, use a filesystem redirect:

**On Unix/macOS:**

```
# move the original config foldermv ~/.gemini ~/gemini_backup​# create a symlink to your desired locationln -s /path/to/central/gemini-config ~/.gemini
```

**On Windows (PowerShell administrative prompt):**

```
# Move the original directoryMove-Item -Path $env:USERPROFILE\.gemini -Destination C:\GeminiConfigBackup​# Create a junction (administrator)New-Item -ItemType Junction -Path $env:USERPROFILE\.gemini -Target C:\CentralGeminiConfig
```

This approach forces the CLI to read from your desired location without requiring native support in the CLI. Note: symlinks/junctions require appropriate filesystem privileges and may behave differently in container or Windows environments. Use with care. (See “Windows-specific notes” below.)

### 5) Change the effective home directory for the process (container/CI trick)

When running in CI, containers, or ephemeral environments, you can change the `$HOME` (Unix) or `%USERPROFILE%` (Windows) environment variable for the `gemini` process so that its default `~/.gemini` resolves to a path you control:

```
# Run gemini with a custom HOME (bash)HOME=/ci/workspace/you gemini --some-command​# Or in a container DockerfileENV HOME=/app/userRUN mkdir -p /app/user/.geminiCOPY config /app/user/.gemini
```

This is useful for CI reproducibility but be mindful: changing `HOME` can affect other tools and authentication flows (e.g., Google OAuth caches), so constrain this technique to isolated containers or process-level wrappers.

## How can I install and use **Gemini CLI** via **CometAPI**?

Short answer: you have two practical paths — (A) call Gemini models *directly* through CometAPI (recommended and simplest), or (B) make the official **Gemini CLI** talk to CometAPI by either using a Gemini-CLI release that supports a custom base URL (some releases / PRs add this), or by running a tiny local proxy that translates Gemini-CLI requests into CometAPI/OpenAI-style calls.

### What is CometAPI?

[CometAPI](https://www.cometapi.com/) is an API aggregation/gateway that exposes hundreds of third-party models (including Google’s Gemini family) behind an OpenAI-style HTTP API. You sign up, get a bearer API key, then call endpoints such as `https://api.cometapi.com/v1/chat/completions` . CometAPI uses standard bearer tokens in the `Authorization` header.

Why use CometAPI? It offers lower API pricing than the official API to facilitate integration. [Gemini CLI Installation and Usage Guide](https://apidoc.cometapi.com/gemini-cli-installation-and-usage-guide-1280313m0):

### How can I **call Gemini models directly via CometAPI**? (Recommended)

If your goal is simply to use Gemini models and you don’t strictly need Gemini CLI features, calling CometAPI directly is straightforward and reliable.

```
export COMET_KEY="sk-xxxx"​curl -s -X POST "https://api.cometapi.com/v1/chat/completions" \  -H "Authorization: Bearer $COMET_KEY" \  -H "Content-Type: application/json" \  -d '{    "model": "gemini-2.5-pro",    "messages": [      {"role": "system", "content": "You are a helpful assistant."},      {"role": "user", "content": "Summarize the 3 key benefits of unit tests."}    ],    "max_tokens": 300  }' | jq .
```

These direct calls let you integrate CometAPI into scripts, apps, or CI without relying on Gemini CLI.

### Can I make **Gemini CLI** use CometAPI?

Some Gemini CLI versions / PRs add environment variables to override the Gemini API base URL . If your installed gemini supports to configure a custom Gemini base URL + use CometAPI key, you can point it at CometAPI and set the CometAPI key as the GEMINI\_API\_KEY (CLI expects a key variable named GEMINI\_API\_KEY for Gemini API key auth).

Example:

```
# example env — *check your gemini-cli docs for exact var names*export GEMINI_API_KEY="sk-xxxxx"                    # CometAPI keyexport GOOGLE_GEMINI_BASE_URL="https://api.cometapi.com/v1"  # if supportedgemini   # run the CLI; it will use the configured base URL
```

## Troubleshooting: common problems and fixes

### Problem: Gemini can’t see files in another repo

1. Try `gemini --include-directories /path/to/repo` when starting. Or in-session: `/directory add /path/to/repo`.
2. If the repo is on a network mount, check permissions and that the CLI process user can read the files.
3. If you used a symlink to move `.gemini`, verify the CLI follows the symlink for `GEMINI.md` and `settings.json` (some versions do not follow certain symlinks for security).

### Problem: `gemini` fails to create `~/.gemini` on Windows (EPERM)

This typically means your process lacks permission to write to `%USERPROFILE%`. Fixes:

- Run the terminal as Administrator or adjust folder permissions.
- Set a custom config location via symlink or, when supported, via environment variable (watch for future `GEMINI_CONFIG_DIR` support).

### Problem: `cd` doesn’t change working dir inside shell mode

This is an acknowledged issue on some platforms. Recommended: switch to running shell commands from outside the Gemin CLI process or add directories via `/directory add`.

### Problem: CometAPI model names don’t match what I expect

Call the `/v1/models` endpoint and inspect the JSON. Model IDs often contain exact variant strings (e.g., `gemini-2.5-flash-preview-04-17`). Use the exact string in your request.

## Conclusion

Gemini CLI's default design favors sane, discoverable behavior: a global `~/.gemini` for user-level defaults and a project `.gemini` for per-repo overrides. The community has been pushing for more native configurability (explicit environment variables or flags) to make the tool friendlier for multi-user, containerized, and enterprise environments.

How to change the Gemini CLI directory:

Overview: Gemini CLI stores user-wide configuration and context files in a `.gemini` directory (typically `~/.gemini`). You can influence which directory the CLI uses by (1) relying on project-level `.gemini` in the current working directory, (2) using environment variables or CLI options where supported, (3) adding workspace directories inside an interactive session, or (4) using filesystem techniques (symlinks, bind mounts, or changing home/profile variables) when native options are missing.

To begin, explore Gemini models (such as [Gemini 3 Pro](https://www.cometapi.com/gemini-3-pro-api/)) ’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Free trial of gemini models](https://www.cometapi.com/console/login) !

---

*Originally published at [https://www.cometapi.com/how-to-change-gemini-cli-directory/](https://www.cometapi.com/how-to-change-gemini-cli-directory/).*
