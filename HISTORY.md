# Release History

---

### v1.0.6 - 2026-07-08

#### UI — Textual TUI Upgrade

- **Replaced prompt_toolkit TUI with Textual 8.x:** The opt-in `--tui` mode now uses a proper split-pane terminal application built on [Textual](https://textual.textualize.io/) — the same framework that powers tools like `pgcli` and `harlequin`.
- **Split-pane layout:** Scrollable chat history occupies the top panel; the input bar is always pinned to the bottom — no more screen clearing on every prompt.
- **Animated thinking indicator:** A `⣾ Thinking…` spinner appears in the status bar the moment the LLM starts and disappears automatically when the response arrives. Zero conflicts with the terminal renderer.
- **Token counter in status bar:** Sent/received token counts (`↑ 598  ↓ 99`) are parsed from output and shown persistently in the bottom-right status bar.
- **Model name in header:** The active model is displayed in the Textual Header subtitle — properly padded, never overflows the terminal edge.
- **Markdown rendering:** Assistant responses are rendered as Rich Markdown with `monokai` code highlighting inside the scrollable log.
- **Thread-safe bridge:** `TuiInputOutput` bridges Klyro's synchronous codebase to Textual's async event loop via `threading.Event` — no asyncio changes required anywhere else.
- **`io.py` and `main.py` untouched:** Only `klyro/tui.py` was rewritten. All existing `InputOutput` functionality is preserved as the backend.

#### Dependencies

- Added `textual>=8.0` to `requirements.in`.

---

### v1.0.5 - 2026-07-08

#### UI Improvements
- **Modern slash palette polish:** Refined the slash command palette with darker command-palette styling, clearer selected-row contrast, and styled command descriptions.
- **Inline prompt status:** Moved shortcut/model status out of the terminal-bottom toolbar and into the prompt area below the chat, closer to Antigravity-style terminal layout.
- **Windows-safe prompt hints:** Replaced fragile special-character shortcut hints with safer prompt text for more reliable rendering in Windows terminals.
- **Readable assistant output:** Changed the default assistant response color from blue to white for better readability on dark terminals.
- **Cleaner prompt line:** Removed the above-prompt status strip and placed the model indicator on the right side of the prompt line.
- **Cleaner thinking output:** Modified the thinking block formatting to use icons (💭 and 💡) instead of text and stopped appending the thinking content to the display stream, keeping the chat interface clean and distraction-free.

#### Release
- Published the follow-up UI polish release after `1.0.4`.

---

### v1.0.4 - 2026-07-08

#### New Features
- **Antigravity-style slash command palette:** Slash command completions now show command names with short descriptions sourced from each command's docstring.
- **Experimental TUI mode:** Added opt-in `--tui` support with a header panel, transcript buffer, file summary, framed prompt surface, and model/status footer.

#### UI Improvements
- **Slash command hints:** The prompt footer now switches to command palette hints while typing `/`, showing navigation, selection, completion, and close controls.
- **Reusable command metadata:** Added a command metadata helper so the classic prompt and TUI can share the same slash command names and descriptions.

#### Reliability & Bug Fixes
- **Model switching state:** `/model` now preserves the current weak/editor model configuration and explicit edit format when switching main models.
- **DeepSeek reasoning cleanup:** DeepSeek R1/reasoner model settings now strip `<think>` reasoning content correctly.
- **Repo map filtering:** Repo maps now ignore Python bytecode and `__pycache__` files.
- **Windows command execution:** Fixed PowerShell command wrapping so simple commands like `echo Hello, World!` preserve their output.
- **Optional dependency resolution:** Restored Python-version-specific NumPy, SciPy, and scikit-learn constraints across optional extras.

---

### v1.0.3 — 2026-07-07

#### New Features
- **Auto-Add Files in Slash Commands:** Commands like `/code`, `/ask`, and `/architect` now parse filenames in their prompt arguments (e.g. `/code edit main.py`) and automatically add them to the chat context if they exist in the git repository.
- **Escape Multiline Mode:** Pressing `Enter` on a slash command starting with `/` on the first line (such as `/multiline-mode` or `/exit`) will now execute immediately, even if multiline mode is enabled, preventing users from getting trapped.
- **Documented Shortcuts:** Added a comprehensive guide on all slash commands and Emacs keyboard shortcuts directly to the README.

#### UI Improvements
- **Dropdown Suggestions:** Changed slash command and filename auto-completions from a multi-column grid/box to a modern vertical dropdown menu (`CompleteStyle.COLUMN`), which makes it much cleaner and easier to read.

#### Reliability & Bug Fixes
- **Ollama Connection Warning:** Caught local Ollama missing model errors gracefully, directing you to run `ollama pull <model>` and exiting cleanly rather than entering an infinite connection retry loop.
- **Reasoning Effort Check:** Added compatibility check for reasoning effort levels against active models to raise a friendly warning rather than crashing.
- **Graceful Prompt Cancellation:** Pressing `Ctrl+C` inside any interactive query (like opening URLs or checking release notes) now outputs `Prompt cancelled.` and returns safely to the prompt rather than quitting Klyro entirely.

#### Code Cleanup & Refactoring
- **Removed duplicate slash commands:** Deleted `/quit` (use `/exit`) and `/edit` (use `/editor`) to clean up redundant command aliases.
- **Fixed duplicate model command method:** Removed the duplicate `cmd_model` method from `commands.py`.
- **Disabled noisy workflows:** Disabled inherited `pre-commit`, `docker-build-test`, `ubuntu-tests`, and `windows-tests` GitHub Actions that don't apply to Klyro, leaving only the PyPI publish pipeline active.

---

### v1.0.2 — 2026-07-07

#### New Features

**`/model` Slash Command**
- `/model` — show the currently active model with quick usage hints
- `/model list` — display a full organized list of all supported providers and aliases
- `/model <alias>` — switch models instantly mid-session without restarting (e.g. `/model flash`, `/model r1`)
- `/model <full-name>` — switch using any full LiteLLM model string (e.g. `/model ollama/phi4`)

**90+ New Model Aliases Added**

| Alias | Model |
|---|---|
| `claude` / `sonnet` / `sonnet4` | `claude-sonnet-4-6` (latest Sonnet) |
| `opus` / `opus4` | `claude-opus-4-7` (most capable Claude) |
| `haiku` / `haiku4` | `claude-haiku-4-5` (fastest Claude) |
| `claude3.7` | `claude-3-7-sonnet-20250219` |
| `claude3-opus` | `claude-3-opus-20240229` |
| `claude3-sonnet` | `claude-3-5-sonnet-20241022` |
| `4o` | `gpt-4o` |
| `4o-mini` | `gpt-4o-mini` |
| `o1` / `o1-mini` / `o1-preview` | OpenAI o1 reasoning family |
| `o3-mini` | `o3-mini` |
| `gpt5` / `gpt5-pro` | `gpt-5.5` / `gpt-5.5-pro` |
| `gemini` / `gemini-pro` | `gemini/gemini-2.5-pro` |
| `flash` / `gemini-flash` | `gemini/gemini-2.5-flash` |
| `flash-lite` | `gemini/gemini-2.5-flash-lite` |
| `gemini-1.5-pro` / `gemini-1.5-flash` | Gemini 1.5 family |
| `deepseek` / `deepseek-v3` | `deepseek/deepseek-chat` |
| `r1` / `deepseek-r1` | `deepseek/deepseek-reasoner` (best reasoning) |
| `r1-lite` | DeepSeek R1 free via OpenRouter |
| `mistral` / `mistral-large` | `mistral/mistral-large-latest` |
| `mistral-small` / `mistral-medium` | Mistral size variants |
| `codestral` | `mistral/codestral-latest` |
| `pixtral` | `mistral/pixtral-large-latest` |
| `llama` / `llama3` / `llama3.2` | `ollama/llama3.2` (local) |
| `llama3.3` / `llama4` | Meta Llama 3.3 / 4 via Ollama |
| `codellama` | `ollama/codellama` |
| `qwen` / `qwen2.5` | `ollama/qwen2.5-coder` |
| `phi4` / `phi3` | Microsoft Phi family via Ollama |
| `gemma` / `gemma3` | `ollama/gemma3` |
| `devstral` | `ollama/devstral` |
| `deepseek-ollama` | `ollama/deepseek-r1` (local) |
| `grok` / `grok3` | `xai/grok-3-beta` |
| `grok3-mini` | `xai/grok-3-mini-beta` |
| `grok2` | `xai/grok-2-latest` |
| `groq-llama` / `groq-llama3` | `groq/llama-3.3-70b-versatile` (ultra-fast) |
| `groq-mixtral` | `groq/mixtral-8x7b-32768` |
| `groq-gemma` | `groq/gemma2-9b-it` |
| `command` / `command-r-plus` | `cohere/command-r-plus` |
| `command-r` / `command-a` | Cohere Command family |
| `llama-free` | `openrouter/meta-llama/llama-3.1-8b-instruct:free` |
| `gemma-free` | `openrouter/google/gemma-3-27b-it:free` |
| `deepseek-free` | `openrouter/deepseek/deepseek-r1-0528:free` |
| `qwen-free` | `openrouter/qwen/qwen3-235b-a22b:free` |
| `quasar` / `optimus` | OpenRouter featured models |
| `bedrock-claude` | AWS Bedrock Claude 3.5 Sonnet |
| `bedrock-llama` / `bedrock-titan` | AWS Bedrock Llama / Titan |
| `azure-gpt4o` / `azure-gpt4` | Azure OpenAI deployments |
| `together-llama` / `together-mixtral` | Together AI hosted models |

#### Bug Fixes
- Fixed startup banner showing "CogniCLI" instead of "KLYRO" — replaced with proper Unicode block-letter logo
- Fixed Windows PATH not including the Python Scripts directory — `klyro` command now works directly after install without `python -m klyro`
- Fixed README showing a hardcoded username in the PATH example — now shows generic instructions with a helper command

#### Documentation
- Updated README slash commands table to include `/model`
- Updated Windows PATH instructions with a command to auto-detect the correct Scripts folder
- Updated publishing section to clarify `setuptools_scm` dynamic versioning from git tags
- Added `CHANGELOG.md` with full release notes

---

### v1.0.1 — 2026-07-06

#### New Features
- **`/stats` command** — reports current model name, last message cost, and total session cost
- **`/export [filename]` command** — exports the full chat history to a Markdown file (defaults to `klyro-export.md`)
- **`/web <url>` command** — scrapes a web page using Playwright and adds its content to the chat context
- **Auto-model detection** — Klyro detects available API keys at startup and selects the best model automatically:
  - Local Ollama running → uses it with no API key required
  - Cloud API keys found → picks the best available cloud model
  - No keys → offers guided OpenRouter setup
- **KLYRO startup banner** — custom ASCII art banner with version number and tagline

#### Bug Fixes
- Fixed duplicate `cmd_web` definition causing test failures
- Fixed `.gitignore` entries referencing older config instead of `klyro`
- Fixed CI workflow guards and formatting

#### Internal
- Renamed all internal package references to `klyro`
- Configured OIDC Trusted Publishing for PyPI via GitHub Actions
- Removed duplicate PyPI release workflow

---

### v0.1.1 — 2026-07-05

- Initial public release of Klyro.
- Added ASCII startup banner for custom branding.
- Added `/web` command for scraping websites into the chat context.
- Added `/export` command for saving chat history.
- Added auto-detection for local Ollama instances (bypassing cloud logins).
- Added `/stats` command to track message/session costs.
- Fully automated PyPI release pipeline via GitHub Actions.

#### Supported Models
- **Local Models**: Full, seamless support for Ollama and open-weights models (DeepSeek Reasoner R1, Llama 3, Qwen, etc.). Auto-detection enabled to pull your locally running instances directly without API keys.
- **Anthropic**: Support for the Claude 4 generation including Claude 4.6 Sonnet, 4.7 Opus, and 4.5 Haiku.
- **OpenAI**: Support for the new GPT-5.5, GPT-5.5 Pro, GPT-4o, and o3 reasoning models.
- **Google**: Support for Gemini 3 Pro Preview, Gemini 2.5 Flash, and Gemini Experimental.
- **Other**: Out-of-the-box support for xAI Grok 3 Beta and various OpenRouter models.

#### New Architecture
- Re-architected core chat handling loop for improved token caching and history truncation.
- Brand new theming engine supporting dynamic terminal color styling.
