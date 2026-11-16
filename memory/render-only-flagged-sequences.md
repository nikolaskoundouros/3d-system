---
name: render-only-flagged-sequences
description: "When Nick is present, work sequence by sequence and re-render only the sequences he flags from the last full preview."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 6d168762-61ef-4d14-9020-9cfd3ffc7c96
  modified: 2026-10-06T12:15:00.721Z
---

When Nick is back and can check by hand: (1) work sequence by sequence, his OK on each before the next; (2) re-render
only the sequences he flags from the last full preview, never the whole clip and never sequences he did not ask to change.
Full renders only after every sequence is approved.

**Why:** 2026-10-06 stitches clip: I re-rendered the whole clip, then started rendering the sewing sequence unasked;
Nick: "once i have the preview i can tell you exactly what we need to change ... we can only do specific sequences."
Whole-clip renders on the 8 GB Mac cost hours and redo work he already approved.

**How to apply:** after sending a full preview, wait for his per-sequence notes; render just those ranges (stitches:
tools/seq.sh NAME FIRST LAST). A flagged sequence is not a go to render: send its stills and wait for his OK first
(2026-10-06 he asked "with what rule did you decide to run the full render?" when I rendered seq4 on my own judgement).
Long local renders need run_in_background with timeout 7200000: the default 30 min limit killed seq4 at 153/273 frames. Overnight / when he is away, batch work is still fine. Related: [[show-before-approve]],
[[no-rendering-without-permission]], [[stitches-clip]].
