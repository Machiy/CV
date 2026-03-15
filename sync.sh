#!/bin/bash

# Simple sync script to push updates to GitHub
# Usage: ./sync.sh "Your commit message"

COMMIT_MSG=$1
if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="Update CV: $(date +'%Y-%m-%d %H:%M:%S')"
fi

echo "--- Syncing CV project to GitHub ---"

# Step 1: Add all changes (respecting .gitignore)
git add .

# Step 2: Commit changes
echo "Committing: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

# Step 3: Push to main branch (or the default branch)
echo "Pushing to GitHub..."
git push origin main

echo "--- Sync Complete ---"
