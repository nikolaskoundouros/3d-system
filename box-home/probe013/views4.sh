#!/bin/bash
# One shape test from the clip-matched views: muscle 0.8, wider neck, scaled sleeves, lower hem, soft fold texture.
cd /Users/nick/probe013/run
rm -f SHAPE_DONE
systemd-run --quiet --scope -p MemoryMax=2600M -p MemorySwapMax=2G --uid=nick --setenv=HOME=/Users/nick \
  --setenv=HAIR=0 --setenv=SETTLE=0 --setenv=VIEWS=ref00,ref58,back,side --setenv=OUT=/Users/nick/probe013/run/views4.png \
  "--setenv=SLIDERS={\"age\": 0.27, \"weight\": 0.35, \"muscle\": 0.8, \"height\": 0.5}" \
  --setenv=TEE_RGB=0.72,0.66,0.54 --setenv=HEM_CUT=1 --setenv=TEE_SUBDIV=2 --setenv=NORMAL_STRENGTH=1.0 \
  --setenv=PANT_FOLDS=0.0 --setenv=SHOE_BLEND=MIX --setenv=LOOSE_BELLY=0.03 --setenv=LOOSE_CHEST=0.025 \
  --setenv=LOOSE_SLEEVE=0.0 --setenv=SLEEVE_SCALE=1.15 --setenv=NECK_OPEN=1.3 --setenv=NECK_DOWN=0.06 --setenv=NECK_R=0.09 --setenv=HEM_DROP=0.03 \
  --setenv=WAIST=-0.04 --setenv=CHEST=0.02 \
  nice -n 5 /Users/nick/funnel-env/venv/bin/python -u outfit_probe.py 640 960 24 > log_views4.txt 2>&1
grep "^SHAPE\|^NORMAL\|^HEM\|^CHEST" log_views4.txt
grep -A4 Traceback log_views4.txt
touch SHAPE_DONE
