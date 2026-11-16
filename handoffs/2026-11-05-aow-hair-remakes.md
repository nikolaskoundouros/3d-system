# Art of War 3D parts: paused 2026-11-05 ~14:10 (Nick had to leave)

Resume word: "Resume AOW hair remakes". Coordinator = the clip session ("General discussion").
Everything is on Nick's Mac: ~/Desktop/aow-modules (faces, volley-gun, attic, king-uniform, boots, tools, lib) and
~/Desktop/outfit-pilot. Every decision and mistake is in ~/Desktop/aow-modules/decisions.md (read its tail first).

## Agreed process (Nick: "lets do what you say")
- tools/learning_process.txt: pick, watch, remake the tutorial's own result, library function, tailor, reuse.
- tools/research_rules.txt: use ~/.venvs/ytdlp/bin/yt-dlp (NOT /opt/homebrew/bin/yt-dlp, which gets 403); prove
  every finding on the pod; record in knowledge/learned.jsonl (tools/learned_check.py).
- Finish the two HAIR tutorials end to end (remake, lib function, tailor onto our king and Fieschi, Nick's verdict)
  BEFORE starting the other 19 videos; then 3 at a time.
- Remake steps go in <module>/research/<id>/remake/steps.json (format agreed with the Spiti session:
  n, video_t, title, png, tutorial_png, script, status) plus remake/final.png and research/<id>/final.png.

## Where each stopped (both learners were stopped by me, not crashed)
- King hair (ledger row K8): tutorial n6c9mr6bMKc. Remake try 1 done:
  faces/review/learn/k_n6c9mr6bMKc_remake_1.png, script faces/research/learn_k/remake.py. Reads as real hair
  (Cycles hair curves); too slick, no top volume or texture, fade too light. 4 tries left. steps.json not written yet.
- Fieschi hair (rows F5, F6): tutorial t_OPrQF6mco (video downloaded, frames, transcript, final.png). It had read the
  method from captions and frames and was about to pick a stand-in head on the pod. No remake yet.
- lib/: INDEX.md only, no functions yet.

## State of the parts (round 7, all verify.sh PASS)
- Faces round 7: likeness list king 2/10, Fieschi 3/10 (review/stills/faces_r7_sheet.png). Hair worse; waits for
  the hair remakes. Research round 3 in knowledge/faces.md lines 200 to 212, 300 to 311, 400 to 453.
- Volley gun round 7b: smoothed, bigger lock, bed on the beam; the 13.0 s framing (camera, long beam) still off.
  Open ask to Nick: camera and beam first?
- Attic: done (one light rig). Boots: tab glow kept for now (my pick, no word from Nick). King fringe: matte cords
  right but too pale (4th try waits for his go). Outfit: seat still shows, hem 5.5 cm lower (no word from Nick).

## Infra
- Pod: ~/Desktop/render-desk/bin/workbench up/status/down. Down at 14:10 (this session 1.24 h, $1.10).
- /tmp/aow-blender-slots/POD_ONLY keeps every Blender run on the pod. tools/pod_run.py: GPU (pod_gpu.py), per
  project lock, --python-exit-code, env vars the script reads. HumGen on the pod's network volume /workspace/humgen.
- Spiti (~/Desktop/spiti, port 8560) is its own session; it only reads.

## Next chat (Nick's ask): make the work continue without his Mac.
