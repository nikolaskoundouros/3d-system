---
name: camera-moves
description: Re-create a reference clip's camera moves in Blender - read the reference (clip analyzer), solve its real 3D camera path (COLMAP), then build our camera from move buttons built round our own subjects (push, pull out, orbit, crane, whip, reveal, orbit_flyback_arc) with four built-in checks; and how to show the result to Nick (two separate videos, every-frame sheets, numbers against the reference). Use for any remake whose camera must match a reference, for "camera moves", "match the camera", "orbit like the reference", and before showing Nick any camera work.
---

# Camera moves

From run 021 (14-15 Nov 2026): "My Mom Cracked The Dinosaur" re-made with the boy and his mom.
Code: `~/Projects/blender-funnel/recipes/camera_moves.py` and `runs/021-reference-shots/build.py` (Mac and box copies
identical on 15 Nov; not committed). Results and lessons: `runs/021-reference-shots/review.md`.

## What run 021 found (review.md, 14 Nov)
- Driving the camera straight from the analyzer's 2D numbers: zoom curve correlation 0.86, pan 0.93, all 9 big
  zooms the right way, but 0 of 55 orbit frames: an orbit cannot come from 2D readings.
- The reference's moves curve round their subject. COLMAP solve of the opening shot put on our boy: camera round
  the boy 91.8 deg vs the reference's 93.3 deg (frames 9-48).
- Measured on 15 Nov from the saved camera paths: driven camera 14 frames fully still, buttons 0; the move test's
  first part turns +229 deg round the pair (setting 230).
- Still wrong on 14 Nov: whips (36 reference whip frames, 2 read in ours: too little blur, hard cuts), the push at
  5.87-6.7 s (+84.9 % reference vs +30.1 % ours, cause not found), the S10 pull back passing behind the boy's head.

## The order of work
1. Read the reference with skill `clip-analyzer` (scan + build_data; captions + onscreen + script_align for who the
   camera is on when each line is said).
2. Solve the real 3D path of each shot with COLMAP on the box (skill `clip-analyzer`, "Real 3D camera path").
   Short shots can't solve their own lens: fix it at the long shot's value.
3. Build the camera from buttons round OUR subject, timing and amounts taken from steps 1-2. A button never copies
   the reference's raw path into our room: our room and people are a different size and place.
4. Check (below), render on the pod, analyse the render exactly like the reference, compare (skill `learning-loop`).
5. Show Nick (below).

## The buttons (`recipes/camera_moves.py`)
Each returns one (eye, rotation, lens) per frame round a subject point. Defaults measured on the dino reference:
| button | default from the reference |
|---|---|
| `push(target, az, el, d0, d1, n, slows, aim_to)` | push in +289 % in 0.77 s (4.07 s); with d1 > d0 it is the pull out (-68 % in 0.33 s at 0.00 s) and with `aim_to` the reveal (-77 % in 1.03 s, aim slides to a second subject) |
| `orbit(target, az0, el0, d0, n, angle=92, rise=0.17, slows)` | about 92 deg round the subject, rising 17 % of its distance, over 1.3 s, slowing at 23 % and 75 % and nearly stopping at 92-100 % |
| `crane(target, az, el0, el1, d0, d1, n, aim_to)` | size -29 % with the view tilting up, camera rising (11.3 s) |
| `whip(eye, aim0, aim1, n)` | one fast eased turn, about 0.1 s |
| `hold(target, az, el, dist, n, drift)` | never fully still: a small drift |
| `orbit_flyback_arc(boy, mom, wide_eye, wide_aim, ...)` | "over" to "rope" (2.73-4.13 s): whip orbit round the pair (angle 230 default, by eye), fly back to a wide spot, arc in round Mom 33 deg closing to 0.46 (COLMAP 3.53-3.97 s) |
Helpers: `distance_for(size)` (ECU / CU / MED / WIDE to metres), `distance_for_pair(a, b)` (two people fit a 9:16
frame), `progress(n, floor, slows)` (eased, never stopped). Lens 36.1 mm (the reference's solved lens).

`check_states(scene, states, subject, see_through=CHARACTER_NAMES)` runs the four checks and fixes what it can:
1 camera inside geometry: moved in front of the hit (characters don't count: over-the-shoulder is a choice);
2 subject inside 45 % of the frame width from centre; 3 never still (1 mm or 0.05 deg a frame);
4 too close: nothing within 10 cm of the lens (counted, not fixed: change the plan).

## build.py switches (environment)
Runs on the pod with the `bpy` module (never on the Mac): see `~/funnel_021_inner6.sh` for the exact pod setup
(uv venv, requirements.txt, apt libraries, `tools/fetch_assets.sh`) and `~/limited.py` for the hard time limit.
`python runs/021-reference-shots/build.py W H SAMPLES` with:
- `MODE=stills` (default, one picture per shot), `anim` (+ `FRAMES=a-b`), `path` (no render: every frame's camera to
  OUT/camera_path.json, for checks; 303 frames for 0-302)
- `BUTTONS=1` camera from the buttons plan (per shot, checks printed as `BUTTONS <shot>: ... checks`)
- `SOLVED=solved_s1.json` opening shot on the COLMAP path (`SOLVED_SCALE`, `SOLVED_FRONT`)
- `SOLVED_DIR=solved` later shots on their COLMAP paths where `solved/<shot>/path.json` exists
- `MOVETEST=1` the "over" to "rope" button over frames 82-124 with `MT_ANGLE`, `MT_D`, `MT_EL`, `MT_ARC`, `MT_SHUTTER`
  (versions: `~/funnel_021_mt.sh` A 230/1.3/-12/0.5, B 270/1.3/-12/0.5, C 270/1.0/-18/1.0; not run, needs a pod)
- `DEVICE=gpu`, `HAIR` (children, 30000), `OUT`, `SMOOTH`, `ROLL` (0: the roll reading tilted horizons), `EXPOSURE`

## Show Nick
- Reference and ours as **two separate videos**, same frames, same length: never side by side, never stacked.
  Example: `runs/021-reference-shots/review/buttons_10s_v2/1_reference_0-10s.mp4` and `2_ours_0-10s.mp4`.
- An **every-frame sheet** of the move (reference row above ours), e.g. `review/moves/reference_over_to_rope_every_frame.jpg`;
  for a 10 s stretch a sheet every 1/3 s (`tools/camera_solve/compare_0_10s.py` in the clip analyzer).
- The **numbers** of both from the same analysis: per move zoom and pan amounts, orbit degrees round the subject,
  frames read as orbit or whip, with the reference's number next to ours.
- Send each file with SendUserFile and wait for his verdict (memory `show-before-approve.md`). Before he sees a still
  made from a reference, list every difference yourself (memory `compare-to-reference-after-stills.md`).
- Each check that ran on it, and what was not checked, in one line each.
