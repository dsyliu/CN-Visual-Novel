#!/usr/bin/env bash
# Build the web version of the game and publish it to GitHub Pages.
#
#   https://dsyliu.github.io/CN-Visual-Novel/
#
# Steps: subset fonts -> loading picture -> Ren'Py web build -> push the build to the `gh-pages`
# branch (replacing what was there; that branch only holds build output) ->
# make sure GitHub Pages serves that branch.
#
# Usage (Git Bash, from anywhere):   bash tools/deploy_web.sh
#        build only, no publish:     bash tools/deploy_web.sh --build-only
# Needs: Ren'Py SDK with web support (set RENPY if not at the default path),
#        python + fonttools, gh (logged in).

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RENPY="${RENPY:-/c/Users/dsyli/Downloads/renpy-8.5.3-sdk/renpy.exe}"
REPO="dsyliu/CN-Visual-Novel"
SDK="$(dirname "$RENPY")"
OUT="$(mktemp -d)/web"
OUT_WIN="$(cygpath -m "$OUT" 2>/dev/null || echo "$OUT")"   # Ren'Py needs a Windows path

echo "== Subsetting fonts"
python "$ROOT/tools/subset_fonts.py"

echo "== Making the loading picture"
python "$ROOT/tools/make_presplash.py"

echo "== Building web version into $OUT"
"$RENPY" "$SDK/launcher" web_build "$ROOT/Huafu" --destination "$OUT_WIN" | tr '\r' '\n' | grep -v "of [0-9]*$" || true
test -f "$OUT/index.html" || { echo "Web build failed: no index.html"; exit 1; }
rm -f "$OUT/index.html.symbols"   # debug symbols, not needed to play
touch "$OUT/.nojekyll"            # serve files as-is (no Jekyll processing)
du -sh "$OUT"

if [[ "${1:-}" == "--build-only" ]]; then
    echo "Build only. Files are in $OUT"
    exit 0
fi

echo "== Publishing to the gh-pages branch"
SRC_COMMIT="$(git -C "$ROOT" rev-parse --short HEAD)"
cd "$OUT"
git init -q -b gh-pages
git config core.autocrlf false   # publish files byte-for-byte
git add -A
git -c user.name="$(git -C "$ROOT" config user.name)" -c user.email="$(git -C "$ROOT" config user.email)" \
    commit -q -m "Web build of $SRC_COMMIT"
git push -q --force "https://github.com/$REPO.git" gh-pages

echo "== Making sure GitHub Pages serves gh-pages"
# GitHub often turns Pages on by itself when gh-pages first appears, so a failed
# create is fine as long as Pages exists afterwards.
if ! gh api "repos/$REPO/pages" >/dev/null 2>&1; then
    gh api -X POST "repos/$REPO/pages" -f "source[branch]=gh-pages" -f "source[path]=/" >/dev/null 2>&1 || true
    sleep 3
    gh api "repos/$REPO/pages" >/dev/null || { echo "GitHub Pages is not enabled"; exit 1; }
fi

echo "Done. In a minute or two the game is at: https://dsyliu.github.io/CN-Visual-Novel/"
