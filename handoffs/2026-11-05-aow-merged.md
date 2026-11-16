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

## Spiti (merged in from the Spiti session, checked 2026-11-05 ~14:40: ./verify.sh "all passed", 112 checks)
- ~/Desktop/spiti, port 8560 (launch config "spiti"). Only for the 3D platform. It only reads; it never starts agents.
- agents.json: Coordinator + Research, Builder, Reference check, One-offs (roles matched by subagent title);
  modules.json: the 6 modules as tags. [other project] page layout (sidebar + Today), interactive d3 team graph.
- Research page: video cards open a video page (Our Blender remake, The lesson, Analysis). Own analyzer
  analyze_video.py; all 23 research videos analyzed (spiti/analysis/<module>/<id>.json). Nick on it: "i love this!".
- Learned cards read learned.jsonl proof fields (pass/fail/untested, proof_png, target).
- Remake view reads <module>/research/<id>/remake/steps.json (format above); no remake has written steps yet.
- Builder (Builds tab) and Reference check (Checks tab) show pictures from each module's review/.
- Off switches: SPITI_PAGES, SPITI_RESEARCH, SPITI_ANALYZER, SPITI_GRAPH, SPITI_VISUALS, SPITI_TITLES, SPITI_LOGS=1
  shows the hidden text pages.
- Page-by-page fixes with Nick (he picks up to 3 per page): Research and Checks done; NEXT: Builder and Graph pages.
- Parked until Nick says go: the learning loop, the gap list, the daily cycle.
- Nick's standing rule (saved by the Spiti session): finish the current system first, one task at a time; new or
  unrelated asks get a new chat.
- Full history: memory file spiti.md.

## What we need to do (Nick 2026-11-05: merge both chats, continue in a new chat, then create sub chats)
1. Make the work run without Nick's Mac (his last ask before leaving): coordinator, agents, Blender, parts, HumGen
   and the pod key on the Hetzner box (or another always-on host). Plan it with Nick first.
2. Hair remakes end to end (king n6c9mr6bMKc try 1 done; Fieschi t_OPrQF6mco at step 2), then tailor onto our faces.
3. Spiti: Builder and Graph page fixes; show remakes once steps.json exists.
4. Open asks on the parts (gun camera and beam first?, fringe 4th try, boots tab, outfit seat and hem).
Sub chats: one per track above, created from the new main chat with Nick.

## Order set by Nick, 2026-11-05 evening (replaces "What we need to do" above)
1. Remake all downloaded tutorials (about 20: 19 in faces/research, 3 gun, 2 attic, 2 uniform, 2 boots), by topic
   (hair, faces, outfits, environments, props). Each remake is judged beside the tutorial's own final frame, never
   beside the king. Nick approves tutorial picks per topic from a list with final frames. Saved as library functions
   (~/Desktop/aow-modules/lib) and as tutorial pages in Spiti (research/<id>/remake/steps.json).
2. Then try the references again, applying the library to each part.
3. Then redesign the platform.
Memory rule: research-by-topic.md. Process: tools/learning_process.txt (step 1 rewritten by topic).
