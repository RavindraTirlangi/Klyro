---
parent: Configuration
nav_order: 20
description: Using a .env file to store LLM API keys for klyro.
---

# Config with .env

You can use a `.env` file to store API keys and other settings for the
models you use with klyro.
You can also set many general klyro options
in the `.env` file.

Klyro will look for a `.env` file in these locations:

- Your home directory.
- The root of your git repo.
- The current directory.
- As specified with the `--env-file <filename>` parameter.

If the files above exist, they will be loaded in that order. Files loaded last will take priority.

{% include keys.md %}

## Sample .env file

Below is a sample `.env` file, which you
can also
[download from GitHub](https://github.com/RavindraTirlangi/Klyro/blob/main/klyro/website/assets/sample.env).

<!--[[[cog
from klyro.args import get_sample_dotenv
from pathlib import Path
text=get_sample_dotenv()
Path("klyro/website/assets/sample.env").write_text(text)
cog.outl("```")
cog.out(text)
cog.outl("```")
]]]-->
```
##########################################################
# Sample klyro .env file.
# Place at the root of your git repo.
# Or use `klyro --env <fname>` to specify.
##########################################################

#################
# LLM parameters:
#
# Include xxx_API_KEY parameters and other params needed for your LLMs.
# See https://klyro.chat/docs/llms.html for details.

## OpenAI
#OPENAI_API_KEY=

## Anthropic
#ANTHROPIC_API_KEY=

##...

#############
# Main model:

## Specify the model to use for the main chat
#KLYRO_MODEL=

########################
# API Keys and settings:

## Specify the OpenAI API key
#KLYRO_OPENAI_API_KEY=

## Specify the Anthropic API key
#KLYRO_ANTHROPIC_API_KEY=

## Specify the api base url
#KLYRO_OPENAI_API_BASE=

## (deprecated, use --set-env OPENAI_API_TYPE=<value>)
#KLYRO_OPENAI_API_TYPE=

## (deprecated, use --set-env OPENAI_API_VERSION=<value>)
#KLYRO_OPENAI_API_VERSION=

## (deprecated, use --set-env OPENAI_API_DEPLOYMENT_ID=<value>)
#KLYRO_OPENAI_API_DEPLOYMENT_ID=

## (deprecated, use --set-env OPENAI_ORGANIZATION=<value>)
#KLYRO_OPENAI_ORGANIZATION_ID=

## Set an environment variable (to control API settings, can be used multiple times)
#KLYRO_SET_ENV=

## Set an API key for a provider (eg: --api-key provider=<key> sets PROVIDER_API_KEY=<key>)
#KLYRO_API_KEY=

#################
# Model settings:

## List known models which match the (partial) MODEL name
#KLYRO_LIST_MODELS=

## Specify a file with klyro model settings for unknown models
#KLYRO_MODEL_SETTINGS_FILE=.klyro.model.settings.yml

## Specify a file with context window and costs for unknown models
#KLYRO_MODEL_METADATA_FILE=.klyro.model.metadata.json

## Add a model alias (can be used multiple times)
#KLYRO_ALIAS=

## Set the reasoning_effort API parameter (default: not set)
#KLYRO_REASONING_EFFORT=

## Set the thinking token budget for models that support it. Use 0 to disable. (default: not set)
#KLYRO_THINKING_TOKENS=

## Verify the SSL cert when connecting to models (default: True)
#KLYRO_VERIFY_SSL=true

## Timeout in seconds for API calls (default: None)
#KLYRO_TIMEOUT=

## Specify what edit format the LLM should use (default depends on model)
#KLYRO_EDIT_FORMAT=

## Use architect edit format for the main chat
#KLYRO_ARCHITECT=

## Enable/disable automatic acceptance of architect changes (default: True)
#KLYRO_AUTO_ACCEPT_ARCHITECT=true

## Specify the model to use for commit messages and chat history summarization (default depends on --model)
#KLYRO_WEAK_MODEL=

## Specify the model to use for editor tasks (default depends on --model)
#KLYRO_EDITOR_MODEL=

## Specify the edit format for the editor model (default: depends on editor model)
#KLYRO_EDITOR_EDIT_FORMAT=

## Only work with models that have meta-data available (default: True)
#KLYRO_SHOW_MODEL_WARNINGS=true

## Check if model accepts settings like reasoning_effort/thinking_tokens (default: True)
#KLYRO_CHECK_MODEL_ACCEPTS_SETTINGS=true

## Soft limit on tokens for chat history, after which summarization begins. If unspecified, defaults to the model's max_chat_history_tokens.
#KLYRO_MAX_CHAT_HISTORY_TOKENS=

#################
# Cache settings:

## Enable caching of prompts (default: False)
#KLYRO_CACHE_PROMPTS=false

## Number of times to ping at 5min intervals to keep prompt cache warm (default: 0)
#KLYRO_CACHE_KEEPALIVE_PINGS=false

###################
# Repomap settings:

## Suggested number of tokens to use for repo map, use 0 to disable
#KLYRO_MAP_TOKENS=

## Control how often the repo map is refreshed. Options: auto, always, files, manual (default: auto)
#KLYRO_MAP_REFRESH=auto

## Multiplier for map tokens when no files are specified (default: 2)
#KLYRO_MAP_MULTIPLIER_NO_FILES=true

################
# History Files:

## Specify the chat input history file (default: .klyro.input.history)
#KLYRO_INPUT_HISTORY_FILE=.klyro.input.history

## Specify the chat history file (default: .klyro.chat.history.md)
#KLYRO_CHAT_HISTORY_FILE=.klyro.chat.history.md

## Restore the previous chat history messages (default: False)
#KLYRO_RESTORE_CHAT_HISTORY=false

## Log the conversation with the LLM to this file (for example, .klyro.llm.history)
#KLYRO_LLM_HISTORY_FILE=

##################
# Output settings:

## Use colors suitable for a dark terminal background (default: False)
#KLYRO_DARK_MODE=false

## Use colors suitable for a light terminal background (default: False)
#KLYRO_LIGHT_MODE=false

## Enable/disable pretty, colorized output (default: True)
#KLYRO_PRETTY=true

## Enable/disable streaming responses (default: True)
#KLYRO_STREAM=true

## Set the color for user input (default: #00cc00)
#KLYRO_USER_INPUT_COLOR=#00cc00

## Set the color for tool output (default: None)
#KLYRO_TOOL_OUTPUT_COLOR=

## Set the color for tool error messages (default: #FF2222)
#KLYRO_TOOL_ERROR_COLOR=#FF2222

## Set the color for tool warning messages (default: #FFA500)
#KLYRO_TOOL_WARNING_COLOR=#FFA500

## Set the color for assistant output (default: white)
#KLYRO_ASSISTANT_OUTPUT_COLOR=white

## Set the color for the completion menu (default: terminal's default text color)
#KLYRO_COMPLETION_MENU_COLOR=

## Set the background color for the completion menu (default: terminal's default background color)
#KLYRO_COMPLETION_MENU_BG_COLOR=

## Set the color for the current item in the completion menu (default: terminal's default background color)
#KLYRO_COMPLETION_MENU_CURRENT_COLOR=

## Set the background color for the current item in the completion menu (default: terminal's default text color)
#KLYRO_COMPLETION_MENU_CURRENT_BG_COLOR=

## Set the markdown code theme (default: default, other options include monokai, solarized-dark, solarized-light, or a Pygments builtin style, see https://pygments.org/styles for available themes)
#KLYRO_CODE_THEME=default

## Show diffs when committing changes (default: False)
#KLYRO_SHOW_DIFFS=false

###############
# Git settings:

## Enable/disable looking for a git repo (default: True)
#KLYRO_GIT=true

## Enable/disable adding .klyro* to .gitignore (default: True)
#KLYRO_GITIGNORE=true

## Enable/disable the addition of files listed in .gitignore to Klyro's editing scope.
#KLYRO_ADD_GITIGNORE_FILES=false

## Specify the klyro ignore file (default: .klyroignore in git root)
#KLYRO_KLYROIGNORE=.klyroignore

## Only consider files in the current subtree of the git repository
#KLYRO_SUBTREE_ONLY=false

## Enable/disable auto commit of LLM changes (default: True)
#KLYRO_AUTO_COMMITS=true

## Enable/disable commits when repo is found dirty (default: True)
#KLYRO_DIRTY_COMMITS=true

## Attribute klyro code changes in the git author name (default: True). If explicitly set to True, overrides --attribute-co-authored-by precedence.
#KLYRO_ATTRIBUTE_AUTHOR=

## Attribute klyro commits in the git committer name (default: True). If explicitly set to True, overrides --attribute-co-authored-by precedence for klyro edits.
#KLYRO_ATTRIBUTE_COMMITTER=

## Prefix commit messages with 'klyro: ' if klyro authored the changes (default: False)
#KLYRO_ATTRIBUTE_COMMIT_MESSAGE_AUTHOR=false

## Prefix all commit messages with 'klyro: ' (default: False)
#KLYRO_ATTRIBUTE_COMMIT_MESSAGE_COMMITTER=false

## Attribute klyro edits using the Co-authored-by trailer in the commit message (default: True). If True, this takes precedence over default --attribute-author and --attribute-committer behavior unless they are explicitly set to True.
#KLYRO_ATTRIBUTE_CO_AUTHORED_BY=true

## Enable/disable git pre-commit hooks with --no-verify (default: False)
#KLYRO_GIT_COMMIT_VERIFY=false

## Commit all pending changes with a suitable commit message, then exit
#KLYRO_COMMIT=false

## Specify a custom prompt for generating commit messages
#KLYRO_COMMIT_PROMPT=

## Perform a dry run without modifying files (default: False)
#KLYRO_DRY_RUN=false

## Skip the sanity check for the git repository (default: False)
#KLYRO_SKIP_SANITY_CHECK_REPO=false

## Enable/disable watching files for ai coding comments (default: False)
#KLYRO_WATCH_FILES=false

########################
# Fixing and committing:

## Lint and fix provided files, or dirty files if none provided
#KLYRO_LINT=false

## Specify lint commands to run for different languages, eg: "python: flake8 --select=..." (can be used multiple times)
#KLYRO_LINT_CMD=

## Enable/disable automatic linting after changes (default: True)
#KLYRO_AUTO_LINT=true

## Specify command to run tests
#KLYRO_TEST_CMD=

## Enable/disable automatic testing after changes (default: False)
#KLYRO_AUTO_TEST=false

## Run tests, fix problems found and then exit
#KLYRO_TEST=false

############
# Analytics:

## Enable/disable analytics for current session (default: random)
#KLYRO_ANALYTICS=

## Specify a file to log analytics events
#KLYRO_ANALYTICS_LOG=

## Permanently disable analytics
#KLYRO_ANALYTICS_DISABLE=false

## Send analytics to custom PostHog instance
#KLYRO_ANALYTICS_POSTHOG_HOST=

## Send analytics to custom PostHog project
#KLYRO_ANALYTICS_POSTHOG_PROJECT_API_KEY=

############
# Upgrading:

## Check for updates and return status in the exit code
#KLYRO_JUST_CHECK_UPDATE=false

## Check for new klyro versions on launch
#KLYRO_CHECK_UPDATE=true

## Show release notes on first run of new version (default: None, ask user)
#KLYRO_SHOW_RELEASE_NOTES=

## Install the latest version from the main branch
#KLYRO_INSTALL_MAIN_BRANCH=false

## Upgrade klyro to the latest version from PyPI
#KLYRO_UPGRADE=false

########
# Modes:

## Specify a single message to send the LLM, process reply then exit (disables chat mode)
#KLYRO_MESSAGE=

## Specify a file containing the message to send the LLM, process reply, then exit (disables chat mode)
#KLYRO_MESSAGE_FILE=

## Run klyro in your browser (default: False)
#KLYRO_GUI=false

## Enable automatic copy/paste of chat between klyro and web UI (default: False)
#KLYRO_COPY_PASTE=false

## Apply the changes from the given file instead of running the chat (debug)
#KLYRO_APPLY=

## Apply clipboard contents as edits using the main model's editor format
#KLYRO_APPLY_CLIPBOARD_EDITS=false

## Do all startup activities then exit before accepting user input (debug)
#KLYRO_EXIT=false

## Print the repo map and exit (debug)
#KLYRO_SHOW_REPO_MAP=false

## Print the system prompts and exit (debug)
#KLYRO_SHOW_PROMPTS=false

#################
# Voice settings:

## Audio format for voice recording (default: wav). webm and mp3 require ffmpeg
#KLYRO_VOICE_FORMAT=wav

## Specify the language for voice using ISO 639-1 code (default: auto)
#KLYRO_VOICE_LANGUAGE=en

## Specify the input device name for voice recording
#KLYRO_VOICE_INPUT_DEVICE=

#################
# Other settings:

## Never prompt for or attempt to install Playwright for web scraping (default: False).
#KLYRO_DISABLE_PLAYWRIGHT=false

## specify a file to edit (can be used multiple times)
#KLYRO_FILE=

## specify a read-only file (can be used multiple times)
#KLYRO_READ=

## Use VI editing mode in the terminal (default: False)
#KLYRO_VIM=false

## Specify the language to use in the chat (default: None, uses system settings)
#KLYRO_CHAT_LANGUAGE=

## Specify the language to use in the commit message (default: None, user language)
#KLYRO_COMMIT_LANGUAGE=

## Always say yes to every confirmation
#KLYRO_YES_ALWAYS=

## Enable verbose output
#KLYRO_VERBOSE=false

## Load and execute /commands from a file on launch
#KLYRO_LOAD=

## Specify the encoding for input and output (default: utf-8)
#KLYRO_ENCODING=utf-8

## Line endings to use when writing files (default: platform)
#KLYRO_LINE_ENDINGS=platform

## Specify the .env file to load (default: .env in git root)
#KLYRO_ENV_FILE=.env

## Enable/disable suggesting shell commands (default: True)
#KLYRO_SUGGEST_SHELL_COMMANDS=true

## Enable/disable fancy input with history and completion (default: True)
#KLYRO_FANCY_INPUT=true

## Enable/disable multi-line input mode with Meta-Enter to submit (default: False)
#KLYRO_MULTILINE=false

## Enable/disable terminal bell notifications when LLM responses are ready (default: False)
#KLYRO_NOTIFICATIONS=false

## Specify a command to run for notifications instead of the terminal bell. If not specified, a default command for your OS may be used.
#KLYRO_NOTIFICATIONS_COMMAND=

## Enable/disable detection and offering to add URLs to chat (default: True)
#KLYRO_DETECT_URLS=true

## Specify which editor to use for the /editor command
#KLYRO_EDITOR=

## Print shell completion script for the specified SHELL and exit. Supported shells: bash, tcsh, zsh. Example: klyro --shell-completions bash
#KLYRO_SHELL_COMPLETIONS=

############################
# Deprecated model settings:

## Use claude-3-opus-20240229 model for the main chat (deprecated, use --model)
#KLYRO_OPUS=false

## Use anthropic/claude-3-7-sonnet-20250219 model for the main chat (deprecated, use --model)
#KLYRO_SONNET=false

## Use claude-3-5-haiku-20241022 model for the main chat (deprecated, use --model)
#KLYRO_HAIKU=false

## Use gpt-4-0613 model for the main chat (deprecated, use --model)
#KLYRO_4=false

## Use gpt-4o model for the main chat (deprecated, use --model)
#KLYRO_4O=false

## Use gpt-4o-mini model for the main chat (deprecated, use --model)
#KLYRO_MINI=false

## Use gpt-4-1106-preview model for the main chat (deprecated, use --model)
#KLYRO_4_TURBO=false

## Use gpt-3.5-turbo model for the main chat (deprecated, use --model)
#KLYRO_35TURBO=false

## Use deepseek/deepseek-chat model for the main chat (deprecated, use --model)
#KLYRO_DEEPSEEK=false

## Use o1-mini model for the main chat (deprecated, use --model)
#KLYRO_O1_MINI=false

## Use o1-preview model for the main chat (deprecated, use --model)
#KLYRO_O1_PREVIEW=false
```
<!--[[[end]]]-->
