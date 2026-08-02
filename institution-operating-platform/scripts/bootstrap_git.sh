#!/usr/bin/env bash
set -euo pipefail

git init
git branch -M main
git add .
git commit -m "[Foundation] Establish Institution Operating Platform repository"

echo "Local Git repository initialized. Add the GitHub remote before pushing."
