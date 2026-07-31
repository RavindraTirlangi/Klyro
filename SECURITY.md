# Security

## Reporting a vulnerability

Report suspected vulnerabilities privately through GitHub's security advisory
interface. Do not include API keys, prompts, source code, or other sensitive
data in a public issue.

## Shell execution

Klyro invokes a shell only for commands explicitly entered through `/run`, `!`,
or approved model-suggested shell commands. Internal Git and maintenance
operations use argument arrays without a shell.

Review model-suggested commands before approving them. Klyro cannot make an
arbitrary shell command safe.

## TLS verification

TLS certificate verification is enabled by default. `--no-verify-ssl` disables
verification for model-provider traffic for the current process and prints a
warning. Use it only with a trusted development proxy.

## Credentials

Store provider credentials in environment variables or a protected local
configuration file. Never commit `.env` files, API keys, chat histories, or
Klyro cache files.
