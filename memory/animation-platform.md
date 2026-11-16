---
name: animation-platform
description: "Nick's planned animation-only agent platform (4 Nov 2026): Claude-only, Pavlos-style one-job subagents; script, VO, music and an AI-image storyboard come from the scriptwriters; goal is to cut a short from 4 days"
metadata:
  node_type: memory
  type: project
  originSessionId: 91146be5-61d4-4e07-8155-c742ca960e21
  modified: 2026-11-04T09:38:25.550Z
---

Nick, 4 Nov 2026: "i want to build a pavlos style system with only claude, not chatgpt. so sub agents that each have one
specific function." Then: "this will only be for animation. so we have the script, we have the music, but we are
responsible for the animation process. currently it takes 4 days for a single animated short. thats too long." And: "the
scriptwriters also give the animators a story board with ai images etc too."

**Why:** 4 days per short is too long; the animators only own the animation.
**How to apply:** build on [[agent-builder]] (Pavlos harness, enforcer, hand-written checks), show agents in [[spiti]],
one agent at a time, plan agreed with Nick first. Draft chain (not agreed): storyboard reader, character builder, set
builder, animator, still checker, motion checker, Nick approve, renderer, assembler. Open: Nick is getting a real
storyboard sample; still unknown whether Zack's clip stays a reference beside the boards; where the 4 days go is not
measured (dandruff notes hint at character fix rounds, not rendering). Related: [[zack-clip-skill]], [[clip-gate]].

**4 Nov, later.** Channel is The Art of War (youtube.com/@theartofwarrr/shorts), not Zack. Nick wants max modularity
("outfits are ready, but environment still needs work, we dont need to run the whole blender scene all over"): each
domain its own .blend linked into shots, only changed shots re-run. Reference downloaded: King Louis 25 barrel
(VhkPinAit5A, 24.3 s, 3 hard cuts at 6.9/8.3/22.1 s) at ~/Desktop/aow-refs/king-louis-25-barrel. Nick swapped out the
Zack-only domains (biology, x-ray dissolves, Zack blue) for: crowds, blood and gore, hit and fall motion, tracers, motion
blur whips, in-scene info text, brand placement, city exteriors, macro detail; plus from thumbnails weapons, period
costume, masks, restraints, faces, fibre, snow, multi-character staging, captions. "we need to build each and every one
pavlos way." He wants learning built in: "for clothing we get some youtube tutorials, download sketchfab assets and
analyze them etc."

**4 Nov, evening.** Nick: "we have to find a way to run 10,20,30 blenders at the same time with our agents to create the clips. and these sub agents should be doing research when they arent actively working." Scale target: "the job of 400 editors" cannot run on his Mac. Checked live 4 Nov: both Hetzner boxes are 2 CPU / 3 GB, no GPU (clip-a disk full), so they cannot be the farm. Outfit pilot ~/Desktop/outfit-pilot: try1 body shell (banned), try2 sewn+draped, try3 uses knowledge/outfit.md (19 sourced techniques from 3 tutorials in ~/Desktop/aow-refs/outfit-research). Nick: "the reference is the only thing that does" matter, his view does not. Boots get their own builder (modelled, not draped). New yt-dlp in ~/.venvs/ytdlp (brew cannot build on macOS 14).
**4 Nov, night.** Modules at ~/Desktop/aow-modules/{volley-gun,attic,king-uniform,boots}, each: refs/, knowledge/<m>.md (research agent, sourced), hand-written checks/ (planted pass/fail tested), verify.sh, builder. tools/blender_slot.sh caps the Mac at 3 Blenders (one outfit build = 1.06 GB peak, 80 s). Nick's rule: where the reference shows it, the reference wins over history (gun = 24 barrels, 2 rows of 12, flintlocks; attic = beams/planks/plaster). My try1 "4 differences" were wrong about the waistcoat (it is woven, high-closing, small stand collar); a fresh reference checker caught it. Face agent is next in the queue. Compute: both Hetzner boxes are CX23; RunPod (key + volume hnzc5aunxc EU-RO-1) is the only bought compute that scales.
**5 Nov 00:40, night run results.** Matched pending Nick (verify + locked look boxes, re-run by me): outfit 11/11, attic 17/17, boots 9/9, king uniform 15/15; gun 9/9 but its close-up cameras are being refit; faces (~/Desktop/aow-modules/faces, HumGen presets, runs on Mac only) paused for his review. Log: ~/Desktop/aow-modules/decisions.md. What worked: research agent then builder per module; tools/look_check.py with fixed boxes in checks/look_boxes.json (the same part in ref and still, ref read live, tol 15); fresh checkers for shape, but only adopt a shape finding after I see it in a full-size side by side (checkers flip-flopped on collars, walls and trousers). Blender runs on the RunPod workbench first (tools/blender_slot.sh, pod_run.py), then the Mac. My own mistakes tonight: wrong ruling from a crop (king collar), coordinates read off a half-size sheet, estimated clock times (now from `date`).
