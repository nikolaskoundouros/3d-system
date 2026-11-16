#!/bin/sh
# pod_with_humgen.sh: make sure the workbench pod has the HumGen network volume; swap pods (at most 6 tries) until one does.
WB=~/Desktop/render-desk/bin/workbench
flock /tmp/aow-wb-up.lock sh -c "
for n in 1 2 3 4 5 6; do
  $WB status 2>&1 | tail -1 | grep -q \"WB up\" || $WB up 2>&1 | tail -2
  if $WB run \"test -d /workspace/humgen/HumGen3D && echo HAS_HUMGEN\" 2>&1 | grep -q HAS_HUMGEN; then echo \"try \$n: pod has HumGen\"; $WB status 2>&1 | tail -1; exit 0; fi
  echo \"try \$n: no HumGen on this pod, swapping\"; $WB down 2>&1 | tail -1; sleep 30
done
echo GAVE_UP; exit 1"
