# Changelog

All notable changes to Klyro are documented here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).  
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.0.4] — 2026-07-07

### ✨ UI Improvements
- **Dropdown Suggestions:** Changed slash command and filename auto-completions from a multi-column grid/box to a modern vertical dropdown menu (`CompleteStyle.COLUMN`), which makes it much cleaner and easier to read.

---

## [1.0.3] — 2026-07-07

### 🧹 Code Cleanup & Refactoring
- **Removed duplicate slash commands:** Deleted `/quit` (use `/exit`) and `/edit` (use `/editor`) to clean up redundant command aliases.
- **Fixed duplicate model command method:** Removed the duplicate `cmd_model` method from `commands.py`.
- **Disabled noisy workflows:** Disabled inherited `pre-commit`, `docker-build-test`, `ubuntu-tests`, and `windows-tests` GitHub Actions that don't apply to Klyro, leaving only the PyPI publish pipeline active.

---

## [1.0.2] — 2026-07-07

### ✨ New Features

#### `/model` Slash Command
- **`/model`** — show the current active model with quick usage hints
- **`/model list`** — display a full, organized list of all supported providers and their aliases, grouped by:
  - Anthropic Claude, OpenAI GPT, Google Gemini, DeepSeek, Mistral, Meta Llama (Ollama), xAI Grok, Groq, Cohere, OpenRouter (free tier), AWS Bedrock, Azure OpenAI
- **`/model <alias>`** — instantly switch models mid-session without restarting (e.g. `/model flash`, `/model r1`, `/model groq-llama`)
- **`/model <full-name>`** — switch using any full LiteLLM model string (e.g. `/model ollama/phi4`, `/model openrouter/google/gemini-pro-1.5`)

#### 90+ Model Aliases Added
All aliases work with the `/model` command. New providers and shortcuts:

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

### 🐛 Bug Fixes
- Fixed startup banner showing "CogniCLI" instead of "KLYRO" — replaced with proper Unicode block-letter logo
- Fixed Windows PATH not including the Python Scripts directory — `klyro` command now works directly after install
- Fixed README showing a hardcoded username in PATH example — now shows generic instructions with a helper command

### 📄 Documentation
- Updated README slash commands table to include `/model`
- Updated Windows PATH instructions with a command to auto-detect the correct Scripts folder
- Updated publishing section to clarify `setuptools_scm` dynamic versioning from git tags

---

## [1.0.1] — 2026-07-06

### ✨ New Features
- **`/stats` command** — reports current model name, last message cost, and total session cost
- **`/export [filename]` command** — exports the full chat history to a Markdown file (defaults to `klyro-export.md`)
- **`/web <url>` command** — scrapes a web page using Playwright and adds its content to the chat context
- **Auto-model detection** — Klyro detects available API keys at startup and selects the best model automatically:
  - Local Ollama running → uses it with no API key required
  - Cloud API keys found → picks the best available cloud model
  - No keys → offers OpenRouter setup
- **KLYRO banner** — custom ASCII art startup banner with version number and tagline

### 🐛 Bug Fixes
- Fixed duplicate `cmd_web` definition causing test failures
- Fixed `.gitignore` entries referencing `aider` instead of `klyro`
- Fixed CI workflow guards and formatting

### 🔧 Internal
- Renamed all internal package references from `aider` → `klyro`
- Configured OIDC Trusted Publishing for PyPI via GitHub Actions
- Removed duplicate PyPI release workflow

---

## [0.1.0] — 2026-07-05

### 🚀 Initial Release

Klyro is a fork of [Aider](https://github.com/Aider-AI/aider), fully rebranded and extended as an AI pair programming tool for the terminal.

#### Core Features
- **Multi-model support** via [LiteLLM](https://github.com/BerriAI/litellm) — works with OpenAI, Anthropic, Google, Ollama, and 100+ providers
- **Whole-file and diff-based editing modes** — Klyro proposes and applies code changes directly
- **Git integration** — auto-commits every change with a descriptive message
- **Repository map** — builds a semantic map of your codebase using tree-sitter AST analysis
- **Automatic linting** — runs your linter after every edit and feeds errors back to the model
- **Context management** — intelligently manages the token window to stay within model limits
- **Voice input support** (`/voice`) — speak your requests instead of typing
- **Image input support** — pass screenshots or diagrams directly to vision-capable models
- **Slash commands**: `/add`, `/drop`, `/diff`, `/undo`, `/tokens`, `/help`, `/git`, `/run`, `/clear`, `/ls`, `/map`
- **Configuration file** — `.klyro.conf.yml` in your project root for persistent settings
- **Environment variable support** — `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OLLAMA_API_BASE`, etc.
- **OpenRouter integration** — auto-detects OpenRouter and guides setup if no other keys are found
- **Windows, macOS, Linux** support

#### Package
- Published to [PyPI](https://pypi.org/project/klyro/) as `klyro`
- Entry point: `klyro` CLI command
- Requires Python 3.10–3.14

---

[1.0.4]: https://github.com/RavindraTirlangi/Klyro/compare/v1.0.3...v1.0.4
[1.0.3]: https://github.com/RavindraTirlangi/Klyro/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/RavindraTirlangi/Klyro/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/RavindraTirlangi/Klyro/compare/v0.1.0...v1.0.1
[0.1.0]: https://github.com/RavindraTirlangi/Klyro/releases/tag/v0.1.0
