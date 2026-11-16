# Handoff: realistic head replay (TXrdw9RljoI), 2026-11-07 ~10:00 EET

## Goal
Replay his 72:05 head tutorial in Blender step by step until our mesh matches his frames. Send Nick every checkpoint
sheet as it lands. Then, from topics/research7, the body, coat, boot, Rigify, face rig, hair and brows tutorials, plus
Nick's three (BqWYgrXw7Jk, HBCOxIH132M, IEQ7IVPwwQk).

## Where it is
- Folder: ~/Desktop/aow-modules/poc/TXrdw9RljoI (only the replay agent writes here).
- Read first: review/handoff.md (the agent's own state), then review/notes.md (all findings), then review/checkpoints.log.
- Replay reaches 23:28.7 of 72:05. Latest lines in checkpoints.log: 35b, 36, 37, 38. Every row since the move 12 fix is
  CLOSE or MATCH, none OFF.
- RUNNING NOW: agent ab5f6676a9610a539, resumed after a network drop. It is switching every proportional G from 7:00 to
  Blender 4.3.2 (his version) with a result cache, and reissuing sheets 04 to 38 where numbers change. Sheets 26b to
  38b exist on disk with NO log lines yet; nothing from this switch has been sent to Nick. Then trace the
  97/79/261/263 offset (already present at 16:17.5, not the version), then continue from 23:28.7 (next line 39).

## How the loop runs
- Watcher (background shell): waits for a new line in review/checkpoints.log. When it fires: read the line, LOOK at
  the sheet, then SendUserFile it with a short honest caption (counts, medians, any ESTIMATED or SUBSTITUTED move).
  Then restart the watcher. The send gate allows only compare_* names.
- When an agent finishes: check its claims in the files, log to ~/Desktop/aow-modules/decisions.md, then launch a fresh
  agent from review/handoff.md with the standard rules: Blender's own operators; no snapping or tweaking; DRIFT stop
  means find the cause upstream; lines printed by work/cpline.py; 2 to 2.5 pod hours per run; no git; no em dashes;
  rewrite handoff.md before stopping.

## Key findings (all in notes.md)
- His video has hidden jump cuts that hide moves: at 6:57.71 (two moves) and at 12:30.56. Both are ESTIMATED from his
  dots. work/clock/ocr.txt flags possible cuts; check each with the frame-by-frame test before replaying it.
  13:50 and 22:35 were checked and are speed-ups, not cuts.
- Menus run steps that show only in his redo panel (Smooth Vertices, Delete).
- The pod's Blender 5.2.2 differs from his 4.3.2 on connected proportional moves. 4.3.2 is at
  /workspace/blender/4.3.2 on the pod. The F5 lint grant (checks/f5_grants.json, Nick approved) allows that one call.
- ESTIMATED moves: 6:57.72 (x2), 12:30.58, 19:41.92.
- SUBSTITUTED: loop cuts, rips and some slides use bmesh (they crash or misbehave headless); Individual Origins centres;
  symmetry off for Smooth Vertices and extrude moves; the 4.3.2 version for G moves.

## Money and limits
- Pod via ~/Desktop/render-desk/bin/workbench status; about $1 per pod-hour; pods stop when idle.
- Overnight total was under $5.
- 9 Nov: restore pod limits from ~/.config/render-desk/render.env.bak-2026-11-06.

## Other sessions
- Fork local_6322e5fc owns tools/replay_kit, tools/graph, tools/action_logger and poc/O6nTNFOJOjk. Five items wait for
  Nick in ~/AgencyOS/handoffs/2026-11-07-morning.md.

## Update ~10:30: the reissue is logged
Lines 05c to 38b are in checkpoints.log (34 sheets, his Blender 4.3.2 for proportional G). Every row is OFF 0.
05c went from MATCH 4 to MATCH 0, so compare the medians in 05b and 05c. None of these sheets was looked at or sent
to Nick: look at them, then send a few (05c, 23c, 38b). The watcher is not running; restart it.

## Update ~11:30: the reissue agent finished (report checked against the log only)
- Replay still at 23:28.68; next line is 39. Medians old vs new barely moved (a table is in the agent's report; see
  notes.md). Pod fxo5hmtv4jkld8 stopped, 2.32 h, $2.06.
- 05c: medians are unchanged (0.46 to 0.53) but MATCH went 4 to 0, so the "his dots without ours <= 11" part of the
  rule must have flipped (pkauto or vis changes?). Check before sending.
- Proportional R and S are left in 5.2.2 (V43RS=0) on purpose: 5.2.2 fits his frames better there. Edge Slide crashes
  the 4.3.2 child.
- The 4.3.2 cache is built (canonical input, review/op43cache) but not verified. Run once with V43CACHE=verify.
- New ESTIMATED: 6:38.16 for 79 and 88 (his share 0.804 and 0.518, ours 0.878 and 0.575; cause not found; idea: his
  modal G started at size 0.1635). 97 starts at the 10:12.68 Edge Slide; checks still to do.
- The agent's "F5 does not catch the child call" is stale: fixed and granted on 7 Nov (checks/f5_grants.json, 62/62).
- Order: verify cache, then trace 97, then line 39. Send Nick 05c, 23c and 38b after looking at them.

## MOVED 2026-11-07 ~11:45
Everything from ~/Desktop is now in Drive: ~/Library/CloudStorage/[email]/My Drive/Nick-AE/Desktop-2026-11-07/ (aow-modules included). Every ~/Desktop path in this file now lives there. To work on it again, move the folder back to ~/Desktop first (tools use absolute ~/Desktop paths).

Links: ~/Desktop/[other project] and ~/Desktop/aow-modules are symlinks to the Drive copies (hooks in settings.json run scripts there).
