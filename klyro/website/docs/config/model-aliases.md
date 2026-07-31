---
parent: Configuration
nav_order: 1000
description: Assign convenient short names to models.
---

# Model Aliases

Model aliases allow you to create shorthand names for models you frequently use. This is particularly useful for models with long names or when you want to standardize model usage across your team.

## Command Line Usage

You can define aliases when launching klyro using the `--alias` option:

```bash
klyro --alias "fast:gpt-4o-mini" --alias "smart:o3-mini"
```

Multiple aliases can be defined by using the `--alias` option multiple times. Each alias definition should be in the format `alias:model-name`.

## Configuration File

Of course,
you can also define aliases in your [`.klyro.conf.yml` file](https://klyro.chat/docs/config/klyro_conf.html):

```yaml
alias:
  - "fast:gpt-4o-mini"
  - "smart:o3-mini"
  - "hacker:claude-3-sonnet-20240229"
```

## Using Aliases

Once defined, you can use the alias instead of the full model name from the command line:

```bash
klyro --model fast  # Uses gpt-4o-mini
klyro --model smart  # Uses o3-mini
```

Or with the `/model` command in-chat:

```
Klyro v0.75.3
Main model: anthropic/claude-3-7-sonnet-20250219 with diff edit format, prompt cache, infinite output
Weak model: claude-3-5-sonnet-20241022
Git repo: .git with 406 files
Repo-map: using 4096 tokens, files refresh
─────────────────────────────────────────────────────────────────────────────────────────────────────
> /model fast

Klyro v0.75.3
Main model: gpt-4o-mini with diff edit format
─────────────────────────────────────────────────────────────────────────────────────────────────────
diff> /model smart

Klyro v0.75.3
Main model: o3-mini with diff edit format
─────────────────────────────────────────────────────────────────────────────────────────────────────
>
```

## Priority

If the same alias is defined more than once, the priority is:

1. Command line aliases (highest priority)
2. Configuration file aliases

Klyro does not ship built-in aliases. Run `/model` to discover exact model
identifiers from the current provider, then define only the personal aliases
you need.
