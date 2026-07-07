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
[![Python](https://img.shields.io/pypi/pyversions/klyro?style=for-the-badge&color=0A0A0A&labelColor=0A0A0A&logo=python&logoColor=white)](https://pypi.org/project/klyro/)
[![License](https://img.shields.io/badge/Apache_2.0-0A0A0A?style=for-the-badge&logo=apache&logoColor=white)](LICENSE)
[![Version](https://img.shields.io/badge/v1.0.3-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RavindraTirlangi/Klyro/releases/tag/v1.0.3)
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
/model flash        → Gemini 2.5 Flash
/model r1           → DeepSeek R1
/model groq-llama   → Groq (ultra-fast)
/model list         → see all options
```

</td>
</tr>
</table>

---

## 🧠 Supported Models

Switch models inside Klyro using `/model <alias>`:

<table>
<thead><tr><th>Provider</th><th>Alias</th><th>Model</th></tr></thead>
<tbody>
<tr><td rowspan="3"><b>Anthropic</b></td><td><code>claude</code> / <code>sonnet</code></td><td>claude-sonnet-4-6 ⭐ latest</td></tr>
<tr><td><code>opus</code></td><td>claude-opus-4-7 — most capable</td></tr>
<tr><td><code>haiku</code></td><td>claude-haiku-4-5 — fastest</td></tr>
<tr><td rowspan="3"><b>OpenAI</b></td><td><code>4o</code></td><td>gpt-4o ⭐ recommended</td></tr>
<tr><td><code>4o-mini</code></td><td>gpt-4o-mini — cheapest</td></tr>
<tr><td><code>o1</code> / <code>o3-mini</code></td><td>reasoning models</td></tr>
<tr><td rowspan="3"><b>Google</b></td><td><code>gemini</code></td><td>gemini-2.5-pro ⭐ recommended</td></tr>
<tr><td><code>flash</code></td><td>gemini-2.5-flash — fast & cheap</td></tr>
<tr><td><code>flash-lite</code></td><td>gemini-2.5-flash-lite</td></tr>
<tr><td rowspan="2"><b>DeepSeek</b></td><td><code>deepseek</code></td><td>deepseek-chat (v3)</td></tr>
<tr><td><code>r1</code></td><td>deepseek-reasoner — best reasoning</td></tr>
<tr><td rowspan="3"><b>Mistral</b></td><td><code>mistral</code></td><td>mistral-large-latest</td></tr>
<tr><td><code>codestral</code></td><td>codestral-latest — code specialist</td></tr>
<tr><td><code>pixtral</code></td><td>pixtral-large — vision</td></tr>
<tr><td rowspan="4"><b>Ollama (local)</b></td><td><code>llama</code> / <code>llama3.2</code></td><td>ollama/llama3.2 — no API key</td></tr>
<tr><td><code>qwen</code></td><td>ollama/qwen2.5-coder</td></tr>
<tr><td><code>phi4</code></td><td>ollama/phi4</td></tr>
<tr><td><code>devstral</code></td><td>ollama/devstral — code expert</td></tr>
<tr><td rowspan="2"><b>xAI</b></td><td><code>grok</code> / <code>grok3</code></td><td>xai/grok-3-beta</td></tr>
<tr><td><code>grok3-mini</code></td><td>xai/grok-3-mini-beta</td></tr>
<tr><td rowspan="3"><b>Groq</b></td><td><code>groq-llama</code></td><td>llama-3.3-70b-versatile — ultra-fast</td></tr>
<tr><td><code>groq-mixtral</code></td><td>mixtral-8x7b-32768</td></tr>
<tr><td><code>groq-gemma</code></td><td>gemma2-9b-it</td></tr>
<tr><td rowspan="4"><b>OpenRouter (free)</b></td><td><code>llama-free</code></td><td>llama-3.1-8b-instruct:free</td></tr>
<tr><td><code>deepseek-free</code></td><td>deepseek-r1-0528:free</td></tr>
<tr><td><code>gemma-free</code></td><td>gemma-3-27b-it:free</td></tr>
<tr><td><code>qwen-free</code></td><td>qwen3-235b-a22b:free</td></tr>
<tr><td><b>AWS Bedrock</b></td><td><code>bedrock-claude</code></td><td>anthropic.claude-3-5-sonnet-v2</td></tr>
<tr><td><b>Azure OpenAI</b></td><td><code>azure-gpt4o</code></td><td>azure/gpt-4o</td></tr>
<tr><td><b>Cohere</b></td><td><code>command</code></td><td>cohere/command-r-plus</td></tr>
</tbody>
</table>

> Run `/model list` inside Klyro to see all 90+ aliases.

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
| **`/model <name>`** | Switch the main LLM mid-session — run `/model list` to browse all 90+ aliases |
| **`/models <query>`** | Search for supported models matching a query string |
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
git tag v1.0.3
git push origin v1.0.3
```

See [CHANGELOG.md](CHANGELOG.md) for full version history.

---

## 📄 License

Apache License 2.0 — see [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ · [PyPI](https://pypi.org/project/klyro/) · [GitHub](https://github.com/RavindraTirlangi/Klyro) · [Changelog](CHANGELOG.md)

</div>
