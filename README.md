<div align="center">

```
 ██╗  ██╗██╗  ██╗   ██╗██████╗  ██████╗
 ██║ ██╔╝██║  ╚██╗ ██╔╝██╔══██╗██╔═══██╗
 █████╔╝ ██║   ╚████╔╝ ██████╔╝██║   ██║
 ██╔═██╗ ██║    ╚██╔╝  ██╔══██╗██║   ██║
 ██║  ██╗███████╗██║   ██║  ██║╚██████╔╝
 ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝ ╚═════╝
```

### AI pair programming in your terminal.

[![PyPI version](https://img.shields.io/pypi/v/klyro?style=for-the-badge&color=0A0A0A&labelColor=0A0A0A&logo=pypi&logoColor=white)](https://pypi.org/project/klyro/)
[![Python](https://img.shields.io/badge/Python-3.10+-0A0A0A?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/klyro/)
[![License](https://img.shields.io/badge/Apache_2.0-0A0A0A?style=for-the-badge&logo=apache&logoColor=white)](LICENSE)
[![Version](https://img.shields.io/badge/v1.0.7-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RavindraTirlangi/Klyro/releases/tag/v1.0.7)
[![Changelog](https://img.shields.io/badge/Changelog-orange?style=for-the-badge&logo=readthedocs&logoColor=white)](CHANGELOG.md)

<br/>

**Klyro** talks to your code. You talk to Klyro. <br/>
Works with GPT-4o, Claude, Gemini, DeepSeek, Ollama, Grok, Groq, Mistral — and 100+ more.

<br/>

[**Quick Start**](#-quick-start) · [**Features**](#-features) · [**Models**](#-supported-models) · [**Commands**](#-slash-commands) · [**Config**](#-configuration) · [**Changelog**](CHANGELOG.md)

</div>

---

## ⚡ Quick Start

```bash
pip install klyro
```

Optional features are installed explicitly:

```bash
pip install "klyro[voice]"       # microphone transcription
pip install "klyro[tui]"         # experimental full terminal UI
pip install "klyro[playwright]"  # browser automation
```

```bash
# Run with your API key set
klyro

# Or specify a model directly
klyro --model gpt-4o
klyro --model ollama/llama3.2
klyro --model gemini/gemini-2.5-flash
```

> **Windows:** If `klyro` is not recognized, either run `python -m klyro` or add your Scripts folder to PATH:
> ```bash
> python -c "import sysconfig; print(sysconfig.get_path('scripts', 'nt_user'))"
> ```

**Install from source:**
```bash
git clone https://github.com/RavindraTirlangi/Klyro.git
cd Klyro
pip install -e .
```

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 Smart Model Detection
Auto-detects your environment at startup:
- **Local Ollama running?** Uses it instantly — no API key needed
- **Cloud keys set?** Picks the best available model
- **Nothing configured?** Guides you through OpenRouter setup (free tier available)

</td>
<td width="50%">

### 🗺️ Repository Intelligence
Understands your entire codebase:
- Builds a **repo map** using tree-sitter AST analysis
- Identifies relevant files automatically
- Manages context to stay within token limits

</td>
</tr>
<tr>
<td width="50%">

### ✏️ Precise Code Editing
Applies changes surgically:
- Whole-file and **diff-based** editing modes
- **Auto-lints** after every edit and feeds errors back
- Built-in **git integration** with descriptive auto-commits

</td>
<td width="50%">

### 🔀 Model Switching On-the-Fly
Switch any time without restarting:
```
/model                              → list current provider's models
/model search coder                 → search current provider
/model openrouter/deepseek/deepseek-r1:free
/model ollama/qwen2.5-coder:latest
```

</td>
</tr>
</table>

---

## 🧠 Supported Models

Klyro discovers models from the provider currently in use instead of shipping
a fixed model catalogue:

- **OpenRouter:** models allowed by the authenticated account's preferences,
  privacy settings, and guardrails.
- **Ollama:** models installed on the local machine.
- **Other providers:** current text/chat models registered by LiteLLM.

Run `/model` to see the current provider's models, then switch with the exact
identifier shown. Optional personal aliases can be configured with `--alias`.

---

## 💬 Slash Commands

Klyro provides 43 built-in slash commands to manage your files, models, git repository, and session:

### 📁 File & Context Management
| Command | Description |
|---|---|
| **`/add <file>`** | Add one or more files to the chat context so the AI can read and edit them |
| **`/drop <file>`** | Remove files from the active chat context to free up tokens |
| **`/read-only <file>`**| Add files as read-only (AI can reference them but won't modify them) |
| **`/ls`** | List all files in your project and indicate which are added to the chat |
| **`/clear`** | Clear the conversation history to start fresh |
| **`/reset`** | Drop all files and clear chat history to start completely fresh |
| **`/tokens`** | Report token counts and how much context window is left |
| **`/diff`** | Show a diff of all local changes made in the active session |
| **`/map`** | Print out the current repository map (symbols, functions, files structure) |
| **`/map-refresh`** | Force a manual refresh of the repository map |
| **`/context`** | Enter context mode to view surrounding code context |

### 🛠️ Coding, Testing & Shell
| Command | Description |
|---|---|
| **`/code [prompt]`** | Switch to code editing mode (or run a one-off code edit prompt) |
| **`/ask [prompt]`** | Switch to question/explain mode (or ask a one-off question without editing files) |
| **`/architect [prompt]`**| Switch to planning mode to design changes using two different models |
| **`/chat-mode <mode>`** | Switch the active chat mode (`code`, `ask`, `architect`, or `context`) |
| **`/ok`** | Shortcut for `/code Ok, please go ahead and make those changes.` |
| **`/run <cmd>`** | Run a shell command and optionally add its output to the chat |
| **`/test <cmd>`** | Run a test command and feed any errors/failures back to the AI for fixes |
| **`/lint`** | Run linter/fixer on all in-chat or dirty files |
| **`/editor`** | Open your configured external terminal editor (like vim or nano) to write a prompt |

### 🧠 Model Configuration
| Command | Description |
|---|---|
| **`/model [name]`** | With no name, list models available from the current provider; with a name, switch the main LLM |
| **`/model search <query>`** | Search models available from the current provider |
| **`/editor-model <name>`**| Switch the model used specifically for writing file edits |
| **`/weak-model <name>`** | Switch the model used for minor background tasks (e.g. summaries) |
| **`/reasoning-effort <l/m/h>`**| Set the reasoning depth (`low`, `medium`, `high`) for reasoning models |
| **`/think-tokens <limit>`**| Set the maximum thinking token budget for reasoning models (0 to disable) |

### 🐙 Git Integration
| Command | Description |
|---|---|
| **`/git <command>`** | Run any git command directly from the session |
| **`/commit [message]`** | Commit any unsaved edits made outside of Klyro |
| **`/undo`** | Undo/revert the last git commit made by Klyro |

### 🎙️ Session & Input Helpers
| Command | Description |
|---|---|
| **`/multiline-mode`** | Toggle multiline mode (swaps Enter and Alt+Enter behavior) |
| **`/paste`** | Paste text or clipboard images into the chat session |
| **`/copy`** | Copy the last assistant response to your clipboard |
| **`/copy-context`** | Copy the entire active chat context as Markdown |
| **`/voice`** | Speak your prompt using your microphone (dictation) |
| **`/web <url>`** | Scrape a webpage, convert it to Markdown, and add it to the chat |
| **`/export [file]`** | Export your full chat session history to a Markdown file |
| **`/stats`** | Show model details, last message cost, and total session cost |
| **`/help <question>`** | Ask interactive help questions about using Klyro |
| **`/settings`** | Print out all active settings and config parameters |
| **`/load <file>`** | Load and execute a list of Klyro commands from a text file |
| **`/save <file>`** | Save active files list as a set of `/add` commands to reconstruct session |
| **`/report`** | Report a problem by opening a GitHub Issue |
| **`/exit`** | Exit the Klyro application |

---

## ⌨️ Keyboard Shortcuts

Klyro provides Emacs-style keybindings for prompt editing and history navigation:

### Prompt Editing & Navigation
* `Ctrl + A` : Move cursor to the start of the line.
* `Ctrl + E` : Move cursor to the end of the line.
* `Ctrl + B` : Move cursor back one character.
* `Ctrl + F` : Move cursor forward one character.
* `Ctrl + D` : Delete the character under the cursor.
* `Ctrl + K` : Cut/delete from the cursor to the end of the line.
* `Ctrl + Y` : Paste (yank) text that was previously cut.
* `Ctrl + L` : Clear the terminal screen.

### History Navigation
* `Ctrl + R` : Search backwards through your sent message history.
* `Ctrl + P` / `Ctrl + Up` : Scroll back to previous history entries.
* `Ctrl + N` / `Ctrl + Down` : Scroll forward to next history entries.
* `Up Arrow` : Move cursor up one line inside a multiline message.
* `Down Arrow` : Move cursor down one line inside a multiline message.

### Multiline & Cancellation
* `Alt + Enter` (or `Ctrl + J`) : Submit message in multiline mode.
* `{` on a line by itself : Start a bracket-based multiline prompt.
* `}` on a line by itself : Submit a bracket-based multiline prompt.
* `Ctrl + C` : Abort the current prompt or cancel an interactive question (returns to prompt).

---

## ⚙️ Configuration

Create `.klyro.conf.yml` in your project root:

```yaml
model: ollama/llama3.2   # default model
dark-mode: true
auto-commits: true
```

Or use environment variables:

```bash
# Cloud providers
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GEMINI_API_KEY=...
export DEEPSEEK_API_KEY=...
export MISTRAL_API_KEY=...
export XAI_API_KEY=...
export GROQ_API_KEY=...
export OPENROUTER_API_KEY=sk-or-...

# Local
export OLLAMA_API_BASE=http://localhost:11434
```

---

## 📦 Release

Tagged releases automatically publish to PyPI via GitHub Actions:

```bash
git tag vX.Y.Z
git push origin vX.Y.Z
```

Publishing is gated by tests, package validation, and a clean wheel
install/startup/uninstall smoke test.

See [CHANGELOG.md](CHANGELOG.md) for full version history.

---

## 📄 License

Apache License 2.0 — see [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ · [PyPI](https://pypi.org/project/klyro/) · [GitHub](https://github.com/RavindraTirlangi/Klyro) · [Changelog](CHANGELOG.md)

</div>
