---
name: clip-analyzer
description: "Clip analyzer at ~/Projects/clip-analyzer (port 8570, launch name clip-analyzer): upload a clip, per-frame camera motion (2D + 3D labels), whips, lighting; video plays with the analysis in sync; feedback buttons save verdicts"
metadata:
  type: project
---

Built 14 Nov 2026 with Nick for studying reference clips for Blender remakes (first clip: "My Mom Cracked The Dinosaur").
`scan.py` (OpenCV, every frame, caption band masked) -> `build_data.py` -> `web/index.html` served by `server.py`
(127.0.0.1:8570). `./verify.sh` = 19 checks (ten known 3D camera moves on a synthetic clip, upload off switch
`CLIP_UPLOAD=0`, upload pipeline, feedback save). Clips live in `clips/<id>/` (gitignored).

Sound (added 14 Nov): demucs voice split (~/.venvs/demucs, model re-downloaded with Nick's ok), `sound.py` finds whoosh / crack / hit / thud by signal shape on the no-voice track, `captions.py` reads burned-in captions with Apple's text reader through `ocr.js` (osascript; the Swift compiler on this Mac is broken). The AudioSet tagger (`label_sound.py`) heard nothing useful on this clip and is not in the pipeline. `CLIP_SOUND=0` skips the sound steps.

State on 14 Nov: 3D labels (dolly, truck, orbit, lens zoom) are proven on synthetic clips only; on real footage they
are unverified and flicker. Feedback verdicts are saved to `clips/<id>/feedback.jsonl` but nothing tunes from them yet.
Nick's old 1/6 s analysis (sound, captions, sheets; see [[stimulus-every-sixth]]) is not merged in yet. Nothing committed.
Research on stronger 3D tools (ViPE, MegaSaM, COLMAP) was done by a subagent and is not verified first-hand.
Related: [[blender-engine]], [[reuse-nicks-tools-first]].
