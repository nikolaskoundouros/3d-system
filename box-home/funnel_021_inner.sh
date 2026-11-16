#!/bin/bash
# funnel_021_inner.sh: runs ON THE SHARED POD. Uses the other chat's /root/bpyenv; writes only inside /Users/nick/run021-repo.
set -u
START=$(date +%s)
LIMIT=${1:-1500}
MODE=${2:-anim}
R=/Users/nick/run021-repo
PY=/root/bpyenv/bin/python
t() { echo; echo "### [$(date +%H:%M:%S)] $*"; }
t "setup"
"$PY" -c "import bpy; print('bpy', bpy.app.version_string)" 2>&1 | tail -1
nvidia-smi --query-gpu=name,memory.total,utilization.gpu --format=csv,noheader 2>&1 | head -2
cd "$R"
if [ ! -e assets ]; then
  if [ -d /Users/nick/Desktop/blender-funnel/assets/system ]; then ln -s /Users/nick/Desktop/blender-funnel/assets assets && echo "assets: linked to the other chat's copy";
  else bash tools/fetch_assets.sh 2>&1 | tail -1; fi
fi
LEFT=$((LIMIT - $(date +%s) + START))
if [ "$MODE" = stills ]; then
  t "run 021 stills: one per shot, 270x480, 16 samples, GPU, limit ${LEFT}s"
  ( time MODE=stills DEVICE=gpu HAIR=30000 OUT=$R/runs/021-reference-shots/out/stills python3 /Users/nick/limited.py "$LEFT" "$PY" runs/021-reference-shots/build.py 270 480 16 ) 2>&1 | grep -v "Fra:\|Rendered \|Sample \|Synchroniz\|Updating\|Loading\|Waiting\|Warning\|use_nodes" | tail -30
  ls runs/021-reference-shots/out/stills | wc -l
else
  t "run 021: frames 0-378, 360x640, 24 samples, GPU, limit ${LEFT}s"
  ( time MODE=anim FRAMES=0-378 DEVICE=gpu HAIR=30000 python3 /Users/nick/limited.py "$LEFT" "$PY" runs/021-reference-shots/build.py 360 640 24 ) 2>&1 | grep -v "Fra:\|Rendered \|Sample \|Synchroniz\|Updating\|Loading\|Waiting\|Warning\|use_nodes" | tail -30
fi
ls runs/021-reference-shots/out/frames | wc -l
t "done"
