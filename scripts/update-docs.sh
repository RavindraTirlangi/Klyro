#!/bin/bash

# exit when any command fails
set -e

if [ -z "$1" ]; then
  ARG=-r
else
  ARG=$1
fi

if [ "$ARG" != "--check" ]; then
  tail -1000 ~/.klyro/analytics.jsonl > klyro/website/assets/sample-analytics.jsonl
  cog -r klyro/website/docs/faq.md
fi

# README.md before index.md, because index.md uses cog to include README.md
cog $ARG \
    README.md \
    klyro/website/index.html \
    klyro/website/HISTORY.md \
    klyro/website/docs/usage/commands.md \
    klyro/website/docs/languages.md \
    klyro/website/docs/config/dotenv.md \
    klyro/website/docs/config/options.md \
    klyro/website/docs/config/klyro_conf.md \
    klyro/website/docs/config/adv-model-settings.md \
    klyro/website/docs/config/model-aliases.md \
    klyro/website/docs/leaderboards/index.md \
    klyro/website/docs/leaderboards/edit.md \
    klyro/website/docs/leaderboards/refactor.md \
    klyro/website/docs/llms/other.md \
    klyro/website/docs/more/infinite-output.md \
    klyro/website/docs/legal/privacy.md
