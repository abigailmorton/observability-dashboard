#!/bin/bash

set -e

echo

echo "$(date +"%Y-%m-%d %H:%M:%S.%3N")"

# Move to this script’s directory (so cron works anywhere)
cd "$(dirname "$0")"

# Always sync with remote first (handle Actions updates)
git pull --rebase origin main

# Activate venv
source venv/bin/activate

# Generate the dashboard
/home/abby/observability/generate_dashboard.py

# Stage changes if any
git add index.html

# Only commit & push if there are actual changes
if ! git diff --cached --quiet; then
    git commit -m "Local automated dashboard update"
    git push origin main
fi
