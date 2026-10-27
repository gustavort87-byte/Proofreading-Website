#!/usr/bin/env bash
# Build _site/ and publish it to GitHub Pages through the gh-pages branch.
# Usage, from Proofreading/:  bash _tools/publish.sh
set -euo pipefail
cd "$(dirname "$0")/.."
python -I _tools/build_site.py
tmp="$(mktemp -d)"
trap 'git worktree remove --force "$tmp" 2>/dev/null || true' EXIT
git fetch -q origin gh-pages 2>/dev/null || true
if git show-ref -q --verify refs/remotes/origin/gh-pages; then
  git worktree add -q -B gh-pages "$tmp" origin/gh-pages
else
  git worktree add -q --detach "$tmp"
  git -C "$tmp" checkout -q --orphan gh-pages
fi
git -C "$tmp" rm -q -rf --ignore-unmatch .
cp -r _site/. "$tmp/"
printf '* -text\n' > "$tmp/.gitattributes"
git -C "$tmp" add -A
if git -C "$tmp" diff --cached --quiet; then echo "Nothing new to publish."; exit 0; fi
git -C "$tmp" commit -q -m "Publish audits ($(git rev-parse --short HEAD))"
git -C "$tmp" push -q origin gh-pages
echo "Published: https://gustavort87-byte.github.io/Proofreading-Website/"
