#!/bin/bash
# funnel_pants_inner.sh: runs ON THE POD. Same setup as the passed test (fast local disk), then run 014 sewn pants once.
set -u
R=/Users/nick/Desktop/blender-funnel
W=/root/funnel
mkdir -p "$W"
t() { echo; echo "### [$(date +%H:%M:%S)] $*"; }
export UV_CACHE_DIR="$W/uv-cache" UV_PYTHON_INSTALL_DIR="$W/python" UV_LINK_MODE=copy

t "setup"
python3 -m pip install -q uv 2>&1 | grep -v notice | tail -2
python3 -m uv venv -q --python 3.13 "$W/venv" 2>&1 | tail -2
PY="$W/venv/bin/python"
python3 -m uv pip install -q --python "$PY" -r "$R/requirements.txt" 2>&1 | tail -3
apt-get update -qq >/dev/null 2>&1
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq libxrender1 libxi6 libxkbcommon0 libsm6 libice6 libgl1 libegl1 libxfixes3 libxxf86vm1 libgomp1 libx11-6 libxext6 >/dev/null 2>&1
"$PY" -c "import bpy; print('bpy', bpy.app.version_string)" 2>&1 | tail -1
cd "$R" && bash tools/fetch_assets.sh 2>&1 | tail -1

t "run 014 sewn pants (80 frames, 2 views 432x640, 24 samples, as written)"
cd "$R" && ( time python3 /Users/nick/limited.py 600 "$PY" runs/014-sewn-pants/pants.py ) 2>&1 | grep -v "Fra:\|Rendered \|Sample \|Synchroniz\|Updating\|Loading\|Waiting" | tail -25
ls -la runs/014-sewn-pants/
t "done"
