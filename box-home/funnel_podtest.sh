#!/bin/sh
# funnel_podtest.sh: ONE pod test for ~/Desktop/blender-funnel, pod alive at most about 15 minutes (Nick's go, 2026-11-13).
# Starts a pod only if none is up, pushes the repo, runs funnel_pod_inner.sh under a hard limit, then ALWAYS destroys the pod.
WB="$HOME/Desktop/render-desk/bin/workbench"; export WB
LOG="$HOME/funnel_podtest.log"
T0=$(date +%s)
{
  date +%H:%M:%S
  export WB_NO_BLENDER=1          # this repo brings its own Blender (bpy 5.3.0); skip the 5.2.2 bootstrap
  # one lock around "is a pod up?" and "start one" (12 Nov: two runs rented two pods)
  flock /tmp/aow-wb-up.lock sh -c '
    if "$WB" status 2>&1 | tail -1 | grep -q "WB up"; then echo "ALREADY_UP: a pod is running that this test did not start"; exit 9; fi
    python3 "$HOME/limited.py" 420 "$WB" up'
  UPRC=$?
  echo "UPRC=$UPRC"
  if [ "$UPRC" = 9 ]; then echo "Nothing started, nothing stopped."; date +%H:%M:%S; echo FINISHED; exit 9; fi
  if [ "$UPRC" = 0 ]; then
    "$WB" status 2>&1 | tail -1
    "$WB" push "$HOME/Desktop/blender-funnel"; echo "PUSH_REPO_RC=$?"
    "$WB" push "$HOME/funnel_pod_inner.sh"; echo "PUSH_SCRIPT_RC=$?"
    LEFT=$((840 - ($(date +%s) - T0)))
    echo "run limit: $LEFT s"
    if [ "$LEFT" -gt 120 ]; then
      python3 "$HOME/limited.py" "$LEFT" "$WB" run "bash $HOME/funnel_pod_inner.sh"
      echo "RUN_RC=$?"
    else
      echo "RUN_SKIPPED: the pod took too long to come up"
    fi
  fi
  "$WB" status 2>&1 | tail -1
  "$WB" down 2>&1 | tail -2
  "$WB" status 2>&1 | tail -1
  echo "pod budget used: $(( $(date +%s) - T0 )) s"
  date +%H:%M:%S
  echo FINISHED
} > "$LOG" 2>&1
