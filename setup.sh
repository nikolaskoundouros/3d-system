#!/bin/bash
# Put Nick's 3D repos at the paths their scripts expect, and install the 3D skills and memory.
# Safe to re-run: clones only what is missing, never overwrites an existing skill or memory file
# (pass --force to overwrite skills and memory from this repo). Needs git access to github.com/nikolaskoundouros.
#   ./setup.sh            on the Mac
#   ./setup.sh box        on the 3D System box (blender-funnel goes to ~/Desktop, no clip-analyzer)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
WHERE="${1:-mac}"; FORCE=""; [ "${2:-}" = "--force" ] || [ "${1:-}" = "--force" ] && FORCE=1
[ "$WHERE" = "--force" ] && WHERE=mac
GH="https://github.com/nikolaskoundouros"

clone() {  # repo path
  if [ -d "$2/.git" ]; then echo "have  $2"; else git clone -q "$GH/$1.git" "$2" && echo "clone $2"; fi
}
clone mom-character      "$HOME/Desktop/mom-character"
clone render-desk        "$HOME/Desktop/render-desk"
if [ "$WHERE" = box ]; then
  clone blender-funnel   "$HOME/Desktop/blender-funnel"
else
  clone blender-funnel   "$HOME/Projects/blender-funnel"
  clone clip-analyzer    "$HOME/Projects/clip-analyzer"
  clone plotpointe-animate "$HOME/Projects/plotpointe-animate"
  clone zoom-game        "$HOME/Projects/zoom-game"
fi

mkdir -p "$HOME/.claude/skills" "$HOME/.claude/projects/-Users-nick/memory"
for s in "$HERE"/skills/*/; do
  n=$(basename "$s")
  if [ -e "$HOME/.claude/skills/$n" ] && [ -z "$FORCE" ]; then echo "have  skill $n"; else cp -R "$s" "$HOME/.claude/skills/" && echo "skill $n"; fi
done
M="$HOME/.claude/projects/-Users-nick/memory"
for f in "$HERE"/memory/*.md; do
  n=$(basename "$f"); [ "$n" = MEMORY.md ] && continue
  if [ -e "$M/$n" ] && [ -z "$FORCE" ]; then :; else cp "$f" "$M/$n"; grep -qF "($n)" "$M/MEMORY.md" 2>/dev/null || grep -F "($n)" "$HERE/memory/MEMORY.md" >> "$M/MEMORY.md"; echo "memory $n"; fi
done
echo "done. Secrets are not in git: see README.md, 'Not in any repo'."
