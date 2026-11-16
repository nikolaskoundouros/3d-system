#!/bin/bash
# Three muscle levels, rendered from the two reference-matched views, no hair, 432x640.
cd /Users/nick/probe013/run
rm -f MUSCLE_DONE
for M in 0.5 0.65 0.8; do
  systemd-run --quiet --scope -p MemoryMax=2600M -p MemorySwapMax=2G --uid=nick --setenv=HOME=/Users/nick \
    --setenv=HAIR=0 --setenv=SETTLE=0 --setenv=VIEWS=ref00,ref58 --setenv=OUT=/Users/nick/probe013/run/muscle_$M.png \
    "--setenv=SLIDERS={\"age\": 0.27, \"weight\": 0.35, \"muscle\": $M, \"height\": 0.5}" \
    --setenv=TEE_RGB=0.72,0.66,0.54 --setenv=HEM_CUT=1 --setenv=NO_NORMALMAP=1 --setenv=TEE_SUBDIV=2 \
    --setenv=PANT_FOLDS=0.0 --setenv=SHOE_BLEND=MIX --setenv=LOOSE_BELLY=0.05 --setenv=LOOSE_CHEST=0.03 \
    --setenv=LOOSE_SLEEVE=0.03 --setenv=WAIST=-0.04 --setenv=CHEST=0.02 \
    nice -n 5 /Users/nick/funnel-env/venv/bin/python -u outfit_probe.py 432 640 16 > log_muscle_$M.txt 2>&1
  echo "muscle $M done $(date +%H:%M:%S)"
  grep -A4 Traceback log_muscle_$M.txt
done
touch MUSCLE_DONE
