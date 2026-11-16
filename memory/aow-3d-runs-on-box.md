---
name: aow-3d-runs-on-box
description: "AOW 3D work runs from the 3D System box (root@37.27.148.115, files under /Users/nick/Desktop), not from the Mac or the Drive folder; Nick expected this on 12 Nov 2026"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 646d5d96-3fc1-41f2-ac76-ab4b43da5c4f
  modified: 2026-11-12T10:09:38.808Z
---

Nick, 2026-11-12, after a day lost to Google Drive freezing on ~/Desktop/aow-modules and the Mac disk at 96 percent: "i thought we emptied everything on drive so the mac has enough space to run, but also why we were using the box...." then "Yes, move to box".

**Why:** the 5 Nov plan ([[boxes-taken-down-2026-11-05]], handoff ~/AgencyOS/handoffs/2026-11-05-3d-system-move.md) was that AOW 3D work runs on the box so the Mac can be closed. A brief from another session told me to work in the Drive folder and I followed it without checking. Drive then froze for hours on exactly the files I had edited that day (read timeouts, "Operation canceled"; a forced restart did not fix it).

**How to apply:** for AOW Blender work, put the project under /Users/nick/Desktop/aow-modules/<project> on the box (ssh root@37.27.148.115, chown -R nick), run as nick: `~/run_ship.sh <tag> <spec>` style scripts started with setsid nohup, which start the pod with ~/Desktop/render-desk/bin/workbench and call tools/pod_run.py with a hard limit (~/limited.py). The box has no GPU and no Blender; pods do the rendering. Pull pictures back with scp for compare sheets. Check the box first (it answered on 12 Nov: 2 CPU, 3 GB RAM, 23 GB free). If a brief says Mac or Drive for this work, ask once before following it ([[challenge-my-calls]]).

State on 12 Nov: tools, checks, lib and navy_ships copied there. The Mac/Drive aow-modules was deleted permanently that afternoon on Nick's order (see [[drive-sync-2026-11-12]]), so the navy officer and dock work is gone; the box copy is the only one.

Parallel runs (12 Nov): two runs that each start a pod raced and rented two (one orphan billed unseen ~45 min). Every script that may start a pod must hold a lock around the status check and `workbench up` (box ~/run_asset.sh uses flock /tmp/aow-wb-up.lock). After any parallel batch, list RunPod pods and compare with `workbench status`; an unrecorded workbench pod is an orphan to report.

Subagent briefs (12 Nov): a research scout I sent out started Blender headless on the Mac to probe settings, because my brief never said not to. Every brief for an agent that might touch Blender must say: never start Blender on the Mac (8 GB); probe on the box's pod or not at all.
