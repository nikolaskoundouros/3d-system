#!/bin/sh
# run_asset.sh <project> <tag> <spec>: like run_ship.sh for any folder under ~/Desktop/aow-modules; several may run at once on the same pod (one per folder)
P="$1"; TAG="$2"; SPEC="$3"; SCRIPT="${4:-build_sea.py}"; LOG="$HOME/asset_$(echo "$P" | tr / _)_$TAG.log"
[ -e /tmp/aow-blender-slots/POD_ONLY ] || { echo "POD_ONLY flag missing" > "$LOG"; exit 3; }
{ date +%H:%M:%S
  # one run at a time decides whether a pod is needed, and holds the lock until the pod is fully set up (12 Nov: two runs
  # both found no pod and rented two; one run also pushed into a pod that was still being set up)
  flock /tmp/aow-wb-up.lock sh -c "~/Desktop/render-desk/bin/workbench status 2>&1 | tail -1 | grep -q \"WB up\" || ~/Desktop/render-desk/bin/workbench up 2>&1 | tail -3"
  python3 ~/limited.py 1500 python3 ~/Desktop/aow-modules/tools/pod_run.py ~/Desktop/aow-modules/$P -b --python "$SCRIPT" -- "$TAG" "review/$SPEC"
  echo "RC=$?"; date +%H:%M:%S; echo FINISHED; } > "$LOG" 2>&1
