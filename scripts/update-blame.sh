#!/bin/bash

# exit when any command fails
set -e

# Use first argument as version if provided, otherwise default to v1.0.1
VERSION=${1:-v1.0.1}
./scripts/blame.py "$VERSION" --all --output klyro/website/_data/blame.yml
