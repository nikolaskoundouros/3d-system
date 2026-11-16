#!/bin/sh
# funnel_pants_run.sh: ONE pod run of blender-funnel run 014 (Nick's go "Yes, render it", 2026-11-13), pod alive at most about 15 minutes.
WB="$HOME/Desktop/render-desk/bin/workbench"; export WB
LOG="$HOME/funnel_pants.log"
OUTDIR="$HOME/Desktop/blender-funnel/runs/014-sewn-pants"
T0=$(date +%s)
{
  date +%H:%M:%S
  export WB_NO_BLENDER=1
  flock /tmp/aow-wb-up.lock sh -c '
    if "$WB" status 2>&1 | tail -1 | grep -q "WB up"; then echo "ALREADY_UP: a pod is running that this run did not start"; exit 9; fi
    python3 "$HOME/limited.py" 420 "$WB" up'
  UPRC=$?
  echo "UPRC=$UPRC"
  if [ "$UPRC" = 9 ]; then echo "Nothing started, nothing stopped."; date +%H:%M:%S; echo FINISHED; exit 9; fi
  if [ "$UPRC" = 0 ]; then
    "$WB" status 2>&1 | tail -1
    "$WB" push "$HOME/Desktop/blender-funnel"; echo "PUSH_REPO_RC=$?"
    "$WB" push "$HOME/funnel_pants_inner.sh"; echo "PUSH_SCRIPT_RC=$?"
    "$WB" push "$HOME/limited.py"; echo "PUSH_LIMIT_RC=$?"
    LEFT=$((840 - ($(date +%s) - T0)))
    echo "run limit: $LEFT s"
    if [ "$LEFT" -gt 180 ]; then
      python3 "$HOME/limited.py" "$LEFT" "$WB" run "bash $HOME/funnel_pants_inner.sh"
      echo "RUN_RC=$?"
      "$WB" pull "$OUTDIR/" "$OUTDIR/"; echo "PULL_RC=$?"
    else
      echo "RUN_SKIPPED: the pod took too long to come up"
    fi
  fi
  "$WB" down 2>&1 | tail -2
  "$WB" status 2>&1 | tail -1
  echo "pod budget used: $(( $(date +%s) - T0 )) s"
  ls -la "$OUTDIR"
  date +%H:%M:%S
  echo FINISHED
} > "$LOG" 2>&1
