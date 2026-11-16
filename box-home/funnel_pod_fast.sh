#!/bin/bash
# funnel_pod_inner.sh: runs ON THE POD. Installs what blender-funnel needs and runs its own checks. Nothing is rendered beyond those checks.
set -u
R=/Users/nick/Desktop/blender-funnel
W=/root/funnel
mkdir -p "$W"
t() { echo; echo "### [$(date +%H:%M:%S)] $*"; }

t "machine"
echo "cores: $(nproc)"; free -g | sed -n 2p
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>&1 | head -2
python3 --version
df -h /workspace | tail -1

t "uv (package installer) from PyPI"
python3 -m pip install -q uv 2>&1 | tail -2
export UV_CACHE_DIR="$W/uv-cache" UV_PYTHON_INSTALL_DIR="$W/python" UV_LINK_MODE=copy

t "python 3.13 environment"
python3 -m uv venv --python 3.13 "$W/venv" 2>&1 | tail -3
PY="$W/venv/bin/python"
"$PY" --version

t "pip install -r requirements.txt"
python3 -m uv pip install --python "$PY" -r "$R/requirements.txt" 2>&1 | tail -6

t "import bpy"
if ! "$PY" -c "import bpy; print('bpy', bpy.app.version_string)" 2>"$W/imp.err"; then
  tail -3 "$W/imp.err"
  t "import failed: installing display libraries, then retrying"
  apt-get update -qq >/dev/null 2>&1
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq libxrender1 libxi6 libxkbcommon0 libsm6 libice6 libgl1 libegl1 libxfixes3 libxxf86vm1 libgomp1 libx11-6 libxext6 >/dev/null 2>&1
  echo "apt rc: $?"
  "$PY" -c "import bpy; print('bpy', bpy.app.version_string)" 2>&1 | tail -3
fi

t "tools/fetch_assets.sh"
cd "$R" && bash tools/fetch_assets.sh 2>&1 | tail -6

t "tests/check_recipes.py"
cd "$R" && ( time "$PY" tests/check_recipes.py ) 2>&1 | tail -45
echo "CHECK_RC=${PIPESTATUS[0]}"

t "graphics cards Blender can see (read only)"
"$PY" - <<'EOF' 2>&1 | tail -8
import bpy
try:
    p = bpy.context.preferences.addons["cycles"].preferences
    for kind in ("OPTIX", "CUDA"):
        try:
            p.compute_device_type = kind
            p.get_devices()
            print(kind, [d.name for d in p.devices])
        except Exception as e:
            print(kind, "not available:", e)
except Exception as e:
    print("cycles preferences not reachable:", e)
EOF

t "sizes"
du -sh "$W" "$R/assets" 2>/dev/null
t "done"
