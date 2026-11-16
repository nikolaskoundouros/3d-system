#!/bin/bash
# Two small test renders of the boy (no hair, 320x480): T1 the T-shirt draped in jersey; T2 an older, slimmer build.
cd /Users/nick/probe013/run
rm -f DONE
run() {   # name, then extra --setenv flags
  local name=$1; shift
  systemd-run --quiet --scope -p MemoryMax=2600M -p MemorySwapMax=2G --uid=nick --setenv=HOME=/Users/nick \
    --setenv=HAIR=0 --setenv=VIEWS=full,upper --setenv=OUT=/Users/nick/probe013/run/sheet_$name.png "$@" \
    nice -n 5 /Users/nick/funnel-env/venv/bin/python -u outfit_probe.py 320 480 16 > log_$name.txt 2>&1
  echo "=== $name $(date +%H:%M:%S)"
  grep "^SLIDERS" log_$name.txt
  grep "^STATS" log_$name.txt | grep -o '"settle_seconds": [0-9]*, "hem_z_by_frame": \[[^]]*\]\]'
  grep -A3 Traceback log_$name.txt
}
run jersey --setenv=SETTLE=1 --setenv=SETTLE_FABRIC=jersey --setenv=SELF_DIST=0.005 --setenv=SUBDIV=0 --setenv=QUALITY=5 --setenv=SETTLE_FRAMES=54
run teen_build --setenv=SETTLE=0 '--setenv=SLIDERS={"age": 0.27, "weight": 0.35, "muscle": 0.4, "height": 0.5}'
ls -la /Users/nick/probe013/run/*.png
touch DONE
