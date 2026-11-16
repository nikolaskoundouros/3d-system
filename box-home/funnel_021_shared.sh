#!/bin/sh
# funnel_021_shared.sh: run 021 on the pod the other chat rented (shared, Nick's go). Never runs up or down.
WB="$HOME/Desktop/render-desk/bin/workbench"; export WB
MODE=${1:-anim}
LOG="$HOME/funnel_021_$MODE.log"
REPO="$HOME/run021-repo"
OUT="$REPO/runs/021-reference-shots/out"
T0=$(date +%s)
{
  date +%H:%M:%S
  export WB_NO_BLENDER=1
  if ! "$WB" status 2>&1 | tail -1 | grep -q "WB up"; then echo "NO_POD: the shared pod is not up; nothing started"; echo FINISHED; exit 9; fi
  "$WB" status 2>&1 | tail -1
  mkdir -p "$REPO"
  rsync -a --delete --exclude .git --exclude assets --exclude 'runs/*' "$HOME/Desktop/blender-funnel/" "$REPO/"
  mkdir -p "$REPO/runs" && rsync -a --exclude out --exclude out_test "$HOME/Desktop/blender-funnel/runs/021-reference-shots" "$REPO/runs/"
  du -sh "$REPO"
  "$WB" push "$REPO"; echo "PUSH_REPO_RC=$?"
  "$WB" push "$HOME/funnel_021_inner.sh"; echo "PUSH_SCRIPT_RC=$?"
  "$WB" push "$HOME/limited.py"; echo "PUSH_LIMIT_RC=$?"
  python3 "$HOME/limited.py" 1560 "$WB" run "bash $HOME/funnel_021_inner.sh 1500 $MODE"
  echo "RUN_RC=$?"
  mkdir -p "$OUT"
  "$WB" pull "$OUT/" "$OUT/"; echo "PULL_RC=$?"
  "$WB" status 2>&1 | tail -1
  echo "pod time used by this run: $(( $(date +%s) - T0 )) s"
  ls "$OUT/frames" 2>/dev/null | wc -l
  date +%H:%M:%S
  echo FINISHED
} > "$LOG" 2>&1
