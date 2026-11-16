#!/bin/sh
# run_ship.sh <tag> <spec>: start a pod if none is up, render one ship scene with a hard 25 minute limit, log to ~/ship_<tag>.log
TAG="$1"; SPEC="$2"; LOG="$HOME/ship_$TAG.log"
[ -e /tmp/aow-blender-slots/POD_ONLY ] || { echo "POD_ONLY flag missing" > "$LOG"; exit 3; }
{ date +%H:%M:%S; ~/Desktop/render-desk/bin/workbench status 2>&1 | tail -1
  ~/Desktop/render-desk/bin/workbench status 2>&1 | tail -1 | grep -q "WB up" || ~/Desktop/render-desk/bin/workbench up 2>&1 | tail -3
  python3 ~/limited.py 1500 python3 ~/Desktop/aow-modules/tools/pod_run.py ~/Desktop/aow-modules/navy_ships -b --python build_sea.py -- "$TAG" "review/$SPEC"
  echo "RC=$?"; date +%H:%M:%S; echo FINISHED; } > "$LOG" 2>&1
