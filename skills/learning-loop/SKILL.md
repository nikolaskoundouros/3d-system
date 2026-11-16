---
name: learning-loop
description: How a check is learned and kept in Nick's work - a by-eye answer key, an automatic detector scored against it, the score recorded, then trust or fix; analysis by synthesis (render versions, analyse them like the reference, keep the closest); verdict buttons; every correction from Nick becomes a check written by someone other than the builder. Use whenever a detector, analyzer reading or render has to be trusted, when Nick corrects something, when choosing between versions, or when he says "learn", "make it a check", "how good is it", "score it".
---

# Learning loop

From the run 021 work (14-15 Nov 2026, clip analyzer and blender-funnel) and Nick's check rules (Oct 2026).
Nothing here is trusted because it sounds right: a reading is trusted when its score against Nick's eye is known.

## 1. Answer key by eye, detector scored against it
1. Sample the clip at a fixed step (dino: one frame every 0.5 s, `ffmpeg -vf fps=2`), make timed contact sheets.
2. Write the key by eye, one line per sample, with the vocabulary at the top. Real one: `~/Projects/clip-analyzer/clips/dino/onscreen_truth.txt`
   (`time subject size`, subject boy / mom / guard / both / prop / skeleton, size ECU / CU / MED / WIDE; 175 samples).
   Whoever writes the key never tunes the detector against it in the same breath.
3. Run the detector, then the scorer: `python3 checks_onscreen_score.py clips/dino` prints the score, the confusion
   table and the most common misses. Dino, 15 Nov: subject right 142/175 (81 %), shot size exact 79/141 (56 %),
   within one step 134/141 (95 %); top miss: a face there and the detector saw none (mom 11, boy 7).
4. Record it: one line in the project's `results.tsv` (`date  change  metric  result`).
5. Trust or fix. Show Nick the number and the misses; he says whether it is good enough. To fix, change the detector,
   rerun the scorer, keep the change only if the score went up (the project's program.md loop: better keep,
   not better revert). Fitted on one clip means "fitted": confirm on a second clip with its own key before trusting.

## 2. Analysis by synthesis: make versions, read them like the reference, keep the closest
Never judge a render by how its settings look. Render it, run the SAME analysis on the render as on the reference,
compare numbers on the same frames.
- Real example, opening shot of the dino clip (review.md, 14 Nov): camera driven by 2D readings made 0 of 55 orbit
  frames. Camera solved with COLMAP from the reference, put on our boy, rendered, then solved again with COLMAP on
  our render: camera round the boy 91.8 deg vs 93.3 deg in the reference (frames 9-48); the analyzer reads 13 of
  the reference's 15 orbit frames as orbit in ours (0 before); boy's hair height median 1.00 of the reference.
- Several versions of one move: `~/Projects/clip-analyzer/tools/camera_solve/score_move_versions.py RUN OUT` cuts each
  version's stretch into its own clip, runs scan.py + build_data.py on each, and prints per version: sideways speed
  curve match, average gap, whip frames, zoom curve match, plus a sheet with every frame (reference on top). The
  three-version tune of the "over" to "rope" move (2.73-4.13 s) is written (`~/funnel_021_mt.sh`) but not run: it
  needs a pod, and the spend cap was used up on 15 Nov.
- Keep the closest by the numbers, then show Nick the reference and the winner (skill `camera-moves`, "Show Nick").
  The numbers choose among versions; Nick's eye decides whether the winner is good.

## 3. Verdicts on the analyzer page
The clip analyzer page (skill `clip-analyzer`) saves each verdict button press to `clips/<id>/feedback.jsonl`
(`clip, start, label, verdict, correct`). Nothing learns from it by itself (none recorded yet on 15 Nov). Each verdict
is a line for the answer key of that reading: add it to the key, rescore, record.

## 4. Every correction from Nick becomes a check
- Quote his words exactly. Turn them into one measurable rule.
- The check is written by someone other than the builder: the `clip-check-writer` agent (it never touches the scene
  or the build). Nick, 8 Oct (memory `tuning-not-fixing.md`): the same agent "was adjusting the test until its own work passed".
- Before it counts: it FAILS on every frame he flagged and PASSES on a frame that is right. Both runs shown verbatim.
- Locking: clip-check-writer submits to the project's `checks-submit/`; the root locker that made them read-only ran on
  clip-a, which was deleted on 5 Nov. Until a new lock exists, a submitted check is "written, not locked": say so, and
  Nick moves it into `checks/` (agents never edit verify.sh, checks/ or program.md).
- A rule counts only when it is in the file the worker reads AND something mechanical enforces it
  (memory `rules-are-gates.md`). Until then say "rule written, not yet enforced".
- Out-of-scope findings from any check go on a list for Nick, never fixed on the side (memory `checkers-dont-set-scope.md`).

## 5. The loop, one line each
key by eye -> detector -> score -> record -> Nick decides trust or fix -> fix only if the score rises -> his next
correction -> new check (fails on his frames, passes on a good one) -> back to the start.
