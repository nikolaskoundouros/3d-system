---
name: pod-guard-before-every-run
description: "RunPod workbench hands out slow cards and pods without the HumGen drive; check the card, the drive and put a time limit on every run"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 790abea7-31fc-4731-b1fb-ea1c5aa4cbdc
  modified: 2026-11-11T16:46:40.374Z
---

On 2026-11-11 (king head and outfit session, faces/king18) Nick asked: "how do we make sure we never get stuck on slow pods? this costs money and time."

What happened that day, measured first-hand:
- `~/Desktop/render-desk/bin/workbench up` takes whatever card is free. 4090 pods rendered five 256-sample close ups in about a minute; RTX 4000 Ada pods needed 3 minutes for one 16-sample close up of the same scene (roughly ten times slower, pod CPU included). A run sat 14 minutes with no output before I noticed.
- Three of four pods in one stretch started WITHOUT the network volume, so without HumGen (render desk falls back to "no volume: this data centre was empty").
- A `workbench up` that is interrupted leaves a half set up pod (no rsync); it needs down and up again.

**Why:** dead starts and stalled runs cost about 0.3 USD and well over half an hour that day, and Nick watches both.

**How to apply:** right after `workbench up`, read the card name in its last line and, when the job needs HumGen, run `faces/king18/probe_pod.py` (a few seconds). Wrap every `pod_run.py` call in a hard time limit (a small subprocess wrapper that kills the process group; macOS has no `timeout`). On a slow card either cut samples and shots or say so and wait, never just let it run. Never chain long runs in one foreground command; use a background script. The lasting fix (allowed-card list, max minutes per run, refuse a pod without the volume) belongs in render desk and `tools/pod_run.py`, which are shared tools: it needs Nick's go (asked 2026-11-11, not yet answered).
