# Release history

### v0.1.1

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
