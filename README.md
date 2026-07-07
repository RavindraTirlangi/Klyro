# Klyro

**AI pair programming in your terminal.**

[![PyPI](https://img.shields.io/pypi/v/klyro?style=flat-square&color=blue)](https://pypi.org/project/klyro/)
[![Python](https://img.shields.io/pypi/pyversions/klyro?style=flat-square)](https://pypi.org/project/klyro/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green?style=flat-square)](LICENSE)

Klyro lets you pair program with LLMs directly from your terminal. Start a new project or work on your existing codebase with an AI that can read, understand, and edit your code.

## Quick Install

```bash
python -m pip install klyro
```

If Windows says `klyro` is not recognized after installation, run it with:

```bash
python -m klyro
```

Or add your Python user Scripts folder to PATH, usually:

```text
C:\Users\SYS\AppData\Roaming\Python\Scripts
```

Install from source:

```bash
git clone https://github.com/RavindraTirlangi/Klyro.git
cd Klyro
python -m pip install -e .
```

## Usage

```bash
# Start Klyro in your project directory
klyro

# Use a specific model
klyro --model gpt-4o

# Use a local Ollama model
klyro --model ollama/llama3.2
```

## Features

### Smart Model Detection

Klyro auto-detects your environment:

- Local Ollama running? Uses it automatically with no API key needed.
- Cloud API keys set? Picks the best available model.
- No keys at all? Offers OpenRouter setup.

### Slash Commands

| Command | Description |
| --- | --- |
| `/stats` | Show model name, last message cost, and total session cost |
| `/web <url>` | Fetch a web page and add its content to the chat context |
| `/export [filename]` | Export chat history to a markdown file |
| `/tokens` | Report token usage for the current chat context |
| `/add <file>` | Add a file to the chat |
| `/drop <file>` | Remove a file from the chat |
| `/diff` | Show the diff of changes made |
| `/undo` | Undo the last change |
| `/help` | Show all available commands |

### Code Editing

- Whole-file and diff-based editing modes
- Automatic linting after every edit
- Built-in git integration with auto-commits

### Repository Intelligence

- Builds a repo map using tree-sitter AST analysis
- Understands your codebase structure and relationships
- Manages context to stay within token limits

## Configuration

Create a `.klyro.conf.yml` in your project root:

```yaml
model: ollama/llama3.2
dark-mode: true
auto-commits: true
```

Or use environment variables:

```bash
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export OLLAMA_API_BASE=http://localhost:11434
```

## Publishing

This project uses GitHub Actions for automated PyPI publishing. To release:

```bash
git tag v1.0.1
git push origin v1.0.1
```

The workflow will automatically build and publish to PyPI.

## License

Apache License 2.0. See [LICENSE](LICENSE) for details.
