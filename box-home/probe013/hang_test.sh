#!/bin/bash
# Reshaped T-shirt test: four views (front close, three-quarter, back, side), 640x960, no hair.
cd /Users/nick/probe013/run
TAG=${1:-hang1}; shift
systemd-run --quiet --scope -p MemoryMax=2600M -p MemorySwapMax=2G --uid=nick --setenv=HOME=/Users/nick \
  --setenv=HAIR=0 --setenv=SETTLE=0 --setenv=VIEWS=ref00,ref58,back,side --setenv=OUT=/Users/nick/probe013/run/$TAG.png \
  "--setenv=SLIDERS={\"age\": 0.27, \"weight\": 0.35, \"muscle\": 0.8, \"height\": 0.5}" \
  --setenv=TEE_RGB=0.72,0.66,0.54 --setenv=HEM_CUT=1 --setenv=NO_NORMALMAP=1 --setenv=TEE_SUBDIV=2 \
  --setenv=PANT_FOLDS=0.0 --setenv=SHOE_BLEND=MIX --setenv=LOOSE_BELLY=0.0 --setenv=LOOSE_CHEST=0.01 \
  --setenv=LOOSE_SLEEVE=0.0 --setenv=WAIST=-0.04 --setenv=CHEST=0.02 --setenv=HANG=1 "$@" \
  nice -n 5 /Users/nick/funnel-env/venv/bin/python -u outfit_probe.py 640 960 16 > log_$TAG.txt 2>&1
grep "^HANG\|^CHEST" log_$TAG.txt
grep -B2 -A6 Traceback log_$TAG.txt
ls -la $TAG.png
