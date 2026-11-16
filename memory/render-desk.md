---
name: render-desk
description: "Editor's self-serve Blender render page, live at render.nofilter.com.cy on the Hetzner box, renting RunPod GPUs per job."
metadata:
  node_type: memory
  type: project
  originSessionId: 6d168762-61ef-4d14-9020-9cfd3ffc7c96
  modified: 2026-10-04T20:00:30.505Z
---

~/Desktop/render-desk. The editor uploads a .blend or .zip at
https://render.nofilter.com.cy (one password, `bin/renderdesk password` sets it) and
downloads the finished mp4. Built 2026-09-27 so Nick's editor can render without him.

- Lives on the Hetzner box as `render-desk.service`, port 8630 (8620 is [[genesis-platform]]),
  behind the same Caddy as the nofilter tenant sites. Deploy is `deploy/ship.sh`, secrets
  are pushed once by `deploy/configure.sh` and never overwritten.
- Rents a RunPod GPU per job and destroys it in a `finally` block. Network volume
  `hnzc5aunxc` is in EU-RO-1, which had capacity in only 1 of the first 4 jobs, so the
  job usually falls back to renting without it anywhere (losing resume). Capacity has
  turned up in CA-MTL-1, US-NC-1 and EU-RO-1; the ledger records which, per job.
- Blender ships **no** FFmpeg encoder (checked: official macOS 5.1.2, homebrew, and the
  Linux build on a pod all refuse `file_format='FFMPEG'`), so an external ffmpeg is
  required. Get it from apt, not a static download: that alone cut a job from 5.3 to
  1.6 minutes.
- Blender never runs on the box: 4 GB RAM shared with client sites, so the rented GPU
  inspects the scene before the first frame. The box only does the free checks.
- RunPod REST **v1 retires 15 Nov 2026**; this targets v2 at api.runpod.io/v2. Their
  Cloudflare rejects the default urllib user agent with a 403 that reads exactly like a
  bad API key.
- `bin/renderdesk cost --clips 25 --seconds 35` projects the monthly bill from real
  measured renders. Finding that number is why it was built.
- `./verify.sh` is the gate: 58 checks. See [[no-deploy-without-go]] and
  [[new-project-structure]].
- 2026-10-02 lesson: H.264 needs even width AND height. A 33% preview of 1080x1920 is 356x633, the pod's ffmpeg
  wrote a 0-byte mp4, the desk then deleted the frames on the volume and locally: a $0.42, 34-min render lost.
  Use 25% (270x480) or 50% (540x960). Also: `render` uses the file's active scene and needs scene.camera even for
  a VSE edit scene (add a placeholder camera); a scene strip keeps its own Cycles samples/device, so set them on
  the strip's scene. Heart clip measured: 2.9 s/frame at 356x633, 8 samples, RTX 4090 $0.74/hr.
- 2026-10-03 lessons (ingrown hair): ONE JOB AT A TIME. Every `render` starts by sweeping all desk pods, so parallel
  jobs kill each other within seconds (3 of 4 died); queue them (gpu/run_op1_seq.sh in ~/Desktop/ingrown-hair). The
  active scene of a stills/edit file should itself be CYCLES with device GPU: with an EEVEE stills scene the log said
  'uses its own device' and stills took 43 s each; with a Cycles edit scene frames took 1.6 s (CPU fallback likely, unverified). Scenes cannot start below frame 0: shift actions instead.
  Measured: his HumGen shots 1.6 to 3 s/frame at 540x960, 16 samples; a 5-still job is about 5 min door to door.
- 2026-10-04 incident: the web desk (editor uploads) and local `bin/renderdesk render` share ONE RunPod account, and
  every job start sweeps ALL desk pods, so local jobs and the editor's web jobs kill each other. A manual
  `sweep_orphans()` from the Mac killed the editor's live job `08_Cerebral_Blockage` (Nick told). Before any manual
  sweep or local render: list RunPod pods and leave any pod whose job is not ours; never sweep blind.

2026-10-06 (Nick's go: "set up the cloud gpu and parallel jobs"): bin/workbench = an always-on RunPod GPU for previews and
stills (up | push | run | pull | down; pod name workbench-*, never swept; watchdog stops it after 30 idle min or 10 h; cost
logged as job "workbench"). Desk sweep now kills only renderdesk- pods older than MAX_JOB_MINUTES + 60 (birth tag -t<epoch>
in the name), so jobs run in parallel (tested: two at once, both delivered). verify.sh PASS. Not committed; NOT deployed to
the box yet (needs Nick's go): until then the box's editor jobs still sweep every desk pod.
2026-10-07 (Nick: "this all process is very inefficient"): bin/live + scripts/bserve.py = one Blender kept open on the
workbench; jobs run in the open session (run_script, stills, visible, overlaps, revert, save). Measured: v10 build 5 s
(was ~4 min chain), 10 stills 38 s (was ~20 s per still with reloads), round trip 46 s. workbench run now keeps the pod
alive during long commands. Not committed.
2026-10-07 guardrails (after a $9.59 failed day): IDLE_MINUTES 10, MAX_HOURS 5, WORKBENCH_DAY_CAP_USD 6 (config, refuses up
and stops the pod), atomic+locked state writes and a watchdog that survives a bad read, bin/live pulls every "SAVED x.blend"
back. Tested: `bin/workbench up` refused with today's cap used. Not committed; not deployed to the desk box.
