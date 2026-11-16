---
name: clip-analyzer
description: Nick's OpenCV clip analyzer (~/Projects/clip-analyzer, page on port 8570). Reads any reference or render clip frame by frame - camera moves (2D and 3D labels, whips, cuts), lighting, sounds, burned-in captions, who is on screen and how big, words lined up with the camera - and solves a real 3D camera path with COLMAP on the box. Use whenever a reference clip has to be studied, a render has to be compared with its reference, or Nick says "analyse", "clip analyzer", "camera moves of", "what does the camera do", "solve the camera".
argument-hint: [clip path, or clip id under clips/]
---

# Clip analyzer

Built with Nick on 14-15 Nov 2026 to study "My Mom Cracked The Dinosaur" for the run 021 Blender remake.
Everything runs on the Mac except the COLMAP solve (box). Blender is never involved here.
Every command below was run on 15 Nov 2026 and worked (numbers in brackets are what it printed that day).

## The page
- Start: preview_start name `clip-analyzer` (launch.json), or `PORT=8570 python3 ~/Projects/clip-analyzer/server.py`.
- Upload a clip on the page: it runs voice split, sound, captions, scan, build_data by itself.
- The player shows the clip with the label of every frame, move list, arrows (flow), sound on/off and stems.
- Verdict buttons save to `clips/<id>/feedback.jsonl` (`{"clip","start","label","verdict","correct"}`).
  Nothing tunes from them yet: read them and turn each one into a check (skill `learning-loop`).
- Off switches: `CLIP_UPLOAD=0` refuses uploads, `CLIP_SOUND=0` skips voice split, sound and captions.
- Gate: `./verify.sh` (synthetic 3D moves, upload, off switch, sound, captions) ["all checks passed"]. Never edit
  verify.sh, checks/ or program.md.

## Run it by hand on a new clip
Make `clips/<id>/clip.mp4` (the file must be called clip), then, from ~/Projects/clip-analyzer:

| step | command | writes | what it means |
|---|---|---|---|
| 1 motion | `python3 scan.py clips/<id>/clip.mp4 clips/<id> [--band T,B,L,R] [--no-mask]` | scan.csv, flow.json | per frame: zoom, pan, tilt, roll, whip, cut, 3D travel and parallax, light. Band = caption strip to ignore, default 0.70,0.80 of height [3 s slice: 90 frames, track 77 %, whip 18 %, lost 6 %] |
| 2 moves | `python3 build_data.py clips/<id>` | data.json | smoothed label per frame, list of moves, whips, summary (the page loads this) |
| 3 faces | `python3 onscreen.py clips/<id> [--every N]` | onscreen.json | per frame: main character (largest face), every face box, shot size ECU / CU / MED / WIDE. Characters are numbered by screen time, not named |
| 4 names | write `clips/<id>/names.json` `{"1": "mom", "2": "boy"}` | names.json | who each character number is. Done by eye or by vote against an answer key (step 8) |
| 5 captions | `python3 captions.py clips/<id> [--band T,B,L,R]` | captions.json | each burned-in caption: start, length, words (Apple's text reader via ocr.js) [8 captions on the slice] |
| 6 voice split | `~/.venvs/demucs/bin/demucs --two-stems vocals -n htdemucs -d cpu -o <work> <mix.wav>` then ffmpeg to `clips/<id>/stems/no_vocals.m4a` | stems/ | lets sound.py hear effects without the voice. The page does this on upload |
| 7 sound | `python3 sound.py clips/<id> [FPS]` | sound.json, spectrogram.png | whoosh / crack / thud / hit with times, loudness per frame |
| 8 words vs camera | `python3 script_align.py clips/<id>` (`LAG=0.25` s default) | script.json + printed checks | per caption: who is on screen, how big, which move, cut or whip near it; each rule against chance |
| 9 score faces | `python3 checks_onscreen_score.py clips/<id>` | printed | onscreen.json against `onscreen_truth.txt` (by-eye answer key) |

`label_sound.py` (AudioSet tagger, demucs venv) exists but heard nothing useful on the dino clip; it is not in the pipeline.

## How far to trust each reading (measured on the dino clip, 15 Nov 2026)
- Who is on screen: right 142 of 175 answer-key frames (81 %). Shot size: exact 56 %, within one step 95 %.
  Misses are mostly "face there, detector saw none" (mom 11, boy 7).
- Shot-size cut-offs (ECU >= 0.40, CU 0.20-0.40, MED 0.09-0.20 of frame height) were fitted on this one clip:
  confirm on a second clip before trusting them.
- Words vs camera on the dino clip: quoted lines are close-ups 73 % of 44 captions vs 41 % by chance; "mom" words
  show mom 61 % vs 46 %; prop words show no face or wide 71 % vs 38 %.
- 3D labels (dolly, truck, orbit, lens zoom) are proven on synthetic clips (verify.sh). On real footage they flicker:
  use them as hints, and use the COLMAP solve for any real 3D camera path.
- Copying 2D readings straight into a Blender camera gave a flat, jittery camera (run 021). Don't.

## Real 3D camera path: COLMAP on the box
Scripts in `tools/camera_solve/` (README there). pycolmap 4.2.1 + OpenCV in the box venv `/Users/nick/venvs/colmap`
on root@37.27.148.115. Run as nick, memory-capped, never on the Mac:

```
# frames at 540x960 as f0000.png... in DIR/images, a mask per frame DIR/masks/f0000.png.png (white = use, caption band black)
systemd-run --uid=nick --gid=nick -p MemoryMax=2G -p WorkingDirectory=WORKDIR --unit=solve-X \
  /bin/sh -c "/Users/nick/venvs/colmap/bin/python solve_shot_free_lens.py DIR > solve.log 2>&1"
```
- `solve_shot_free_lens.py DIR`: one shot, lens solved. Prints frames solved, reprojection error, and for frames 20+
  the orbit angle round the point every view looks at. Writes DIR/path.json (camera centre and rotation per frame).
  The 55-frame and frame-20 numbers are the dino opening shot's: change them for another shot.
- `solve_all_shots.py WORK VIDEO`: every shot with the lens fixed (961.4 px at 540x960, the dino opening shot's).
  Shot frame ranges are hard-coded for the dino clip: take a new clip's cuts from data.json first.
- `solve_masked_people.py`: people masked too. Failed on dino 1.9-4.1 s (blur, 55 % masked).
- `orbit_round_subject.py DIR`: how far the camera goes round the subject (points on the subject's hair).
- Compare scripts (`compare_*.py`, `score_move_versions.py`) still hold run 021 paths: fix paths before reuse.
- Dino results (14 Nov): opening shot S1 55 of 55 frames, 0.79 px, lens 36.1 mm; camera round the boy over frames
  9-48 = 93.3 deg (ours later 91.8 deg). Shots S2-S11 (runs/021-reference-shots/solved/report.json): 8 of 10 got
  some frames solved, from 2 of 26 (S9) to 55 of 55 (S10); S2 (9 frames) and S4 (5 frames) did not solve.
  Results and lessons: ~/Projects/blender-funnel/runs/021-reference-shots/review.md.
- Rerun 15 Nov (proof of these commands): solve_shot_free_lens.py on frames 0-54 gave 55 of 55, 0.796 px again
  (box, 6 min, 374 MB peak). orbit_round_subject.py on it printed fixed ranges (frames 9-54: +57.8 deg round the boy);
  its per-3-frame steps add to about 96 deg over frames 9-48. The script as saved does not print 9-48, so the
  93.3 deg is not reproduced exactly. COLMAP runs can differ a little: report the run you made, with its date.

## Showing results to Nick
Reference and ours as two separate videos (never side by side or stacked), an every-frame sheet, and the analyzer's
numbers for both. See skill `camera-moves`, section "Show Nick".
