# AOW move to 3d-system: paused 2026-11-05 ~18:30 (Nick: "lets continue this later because im currently working")

Resume word: "Resume 3d-system move". Goal: the AOW 3D work runs with Nick's Mac closed.

## Done (each checked on the box)
- One box left: 3d-system (37.27.148.115, Hetzner CX23, EUR 6.53/mo, renamed in console + hostname). clip-a deleted by Nick.
- Step 1: aow-modules (5.4G), outfit-pilot, spiti, render-desk copied to /Users/nick/Desktop on the box (rsync twice, exit 0).
- Step 2: ~/.venvs/ytdlp (2026.10.26) and ~/.venvs/whisper (CPU torch) built; whisper small, small.en, medium.en copied
  (large-v3-turbo left on the Mac: 3.2 GB RAM). tools/blender_slot.sh got one line on Mac + box: no Blender binary -> POD_ONLY.
- Step 3: ~/.claude CLAUDE.md, agents, skills, hooks, memory (-Users-nick) copied; settings merged (box backup in
  ~/.claude/backups/pre-aow-2026-11-05; the nick-oc log hook dropped). Handoff 2026-11-05-aow-merged.md copied.
- Step 4: Nick started tmux "aow" on the box (claude 2.1.295, Opus 5.5, auto mode, Remote Control active,
  claude.ai/code/session_01CDvtC7THUSZfDt5yxbu62E). It is idle, no brief sent yet.

## Stopped here
- Step 5/6 NOT done: a Mac Claude session (about 1 h old at 18:25, likely the AOW main chat) was running the king hair
  remake on the pod (pod hoeun2kr81rbhb, L4). Freezing the Mac copy would break it. Nick's pick pending; my pick:
  let it finish, then final rsync Mac -> box, then chmod -R a-w ~/Desktop/aow-modules ~/Desktop/outfit-pilot on the Mac
  (undo: chmod -R u+w), then send "Resume AOW hair remakes" to the box session for the next try (~$1, his go given for one test).
- Before the final sync, check the Mac run finished: `ps ax | grep pod_run`, `workbench status`.

## Open, for Nick
- Spiti on the phone needs a door (Tailscale or domain + login). Not decided.
- Remote Control showing images on the phone: not verified.
- Box Claude cannot self-update (npm prefix not writable by nick).
- Workbench spend cap is per machine until the Mac is frozen.
- hooks/gate.py rule 14 forwards approvals to clip-a, which no longer exists (Mac and box).
Notes: side-session notes run-without-mac-2026-11-05.md; memory boxes-taken-down-2026-11-05.md.

## 2026-11-06 parallel test on the box (asked by the General discussion session: no freeze, no writes to the Mac)
- Sync: a full mirror of ~/Desktop/aow-modules does NOT fit. It is 22 GB on the Mac now (mp4 7.2 GB, png 4.5 GB, webm 0.6 GB);
  the box disk is 38 GB. I stopped the full rsync at 12 GB, then copied only what the tests read (tools, lib, checks, recipes,
  docs, learn/V-oUcWd3mMU, the checker's case folders, no videos). Box after: 14 GB aow-modules, 7.9 GB free.
- checks/test_pass_check.py: first FAILED on the box (no cv2). Installed the Mac's exact versions into the box's system Python
  (apt python3-pip; pip --break-system-packages --ignore-installed numpy 2.4.4, opencv-python-headless 5.0.0.93, pillow 12.2.0).
  Then PASS, all 11 verdicts, output diff against the Mac's run: identical (every measured number). 37.5 s on the box vs 15.6 s Mac.
- Pod try: from learn/V-oUcWd3mMU, T_TRY=9 ../../tools/blender_slot.sh -b --factory-startup --python research/learn/remake.py --
  review/learn/raw_9_box.png. blender_slot saw no Blender -> POD_ONLY -> workbench up rented its own pod (RTX 4090, EU-RO-1 config),
  81 s wall, then I took it down: 0.03 h, $0.02. raw_9_box.png and raw_9_box_rgba.png vs the Mac's raw_9.png / raw_9_rgba.png:
  0 pixels differ (mean 0.0000, max 0). Side by side: ~/AgencyOS/handoffs/2026-11-06-box-vs-mac-raw9.png.
- Breaks or differs: (1) disk, above. (2) pod_run.py SETUP still links HumGen: "cp: cannot stat /workspace/humgen/userpref.blend"
  on a pod without the network volume; harmless, and HumGen is scrapped. (3) pod_run pulls work/ and logs an rsync error when the
  folder has no work/ (harmless). (4) Box render.env is the 9 Oct one: DAILY 20, MONTHLY 40, workbench day cap default 6; the
  Mac's are 100/300/100 until 9 Nov. Spend state is per machine. (5) Box uses its own ~/.ssh/id_ed25519; RunPod accepted it.
- Nothing was written to the Mac except this handoff and the scratchpad.
- 2026-11-06 later, on Nick's "make space ... whatever we dont use remove": cleared pip/apt caches (+1.1 GB), then on his
  "Yes, delete HumGen" removed /Users/nick/Documents/HumGen3D and ~/hg from the box (Mac copy kept). 11 GB free.
  Full aow-modules copy (exit 0): box 23 GB of work, disk 34 of 38 GB, 1.7 GB FREE (96%). Dry run after: 295 files (214 MB)
  newer on the Mac (the learners keep writing). The box is effectively full; next space needs Nick's call (videos 7.8 GB or more disk).
