---
name: motion-match-reference
description: "When rebuilding a reference animation, measure its motion per second and match it; never leave holds frozen"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2e25bc24-e09d-4389-9ce0-a02eb50a60e9
  modified: 2026-10-12T11:33:09.003Z
---

Nick, 2026-10-12, on the [other project] Figma film: "study how much movement happens from second 40-56 and then compare with
our one. you will see our flaws instantly. our one barely has any motion which makes it look static."

**Why:** my look check matched picture beats and brightness, but not motion between beats. Figma moved on every
other frame of every second (about 50% of frames); ours froze in holds (0% at 50 s, 3% at 42 s).

Then (same day, on the 38 s collage): "no motion here. generally a rule should be that we always have motion".

**How to apply:** every second of every video always has motion, not only where the reference moves. for any rebuild of a reference, measure per-second motion (share of frames with a mean
frame-to-frame change above 1 grey level, and the mean change) for both, before showing Nick. Holds keep moving:
slow pushes, breathing shapes, sprouting elements, tiles that keep changing, artwork that recedes or sways.

Related: [[references-carry-weight]], [[[other project]-figma-film]], [[build-up-every-second]]
