---
name: pod-idle-10-min-stop
description: "Nick 15 Nov 2026 \"after 10 idle minutes please shut the pod down\": no pod may sit idle; the stop must not depend on the Mac."
metadata:
  node_type: memory
  type: feedback
  originSessionId: a3dc1fd1-1e29-443f-acf0-49dc9d39846e
  modified: 2026-11-15T07:48:48.403Z
---

Nick, 15 Nov 2026 (after a pod ran idle overnight, 16.06 h, $14.29, used up the month's spend cap): "after 10 idle minutes please shut the pod down".

**Why:** the workbench's 10-minute idle stop never fired. The other chat's live Blender ran inside `workbench run`, whose keepalive marks the pod in use every 5 minutes, and the backstop watchdog runs on the Mac, which slept (lid closed). Details in [[blender-live-on-pod]].

**How to apply:**
- Before ending any turn with a pod up: stop it, or say in one line that it is billing and why.
- A live Blender session counts as idle when nobody has sent it a command for 10 minutes; it does not keep the pod alive.
- ENFORCED 15 Nov 2026 (Nick's go on the design): `pod-guard.timer` on the 3D System box (root@37.27.148.115) runs `~/Desktop/render-desk/tools/pod_guard.py` as nick every 60 s (MemoryMax 150M). It lists every workbench-* pod on the RunPod account (Mac- or box-started), ssh's in, and terminates when ~/.wb_last_use is 10+ min old and the pod is not busy (GPU < 10 %, CPU < 0.5 core), or the pod is 5+ h old, or unreachable 15 min. Off switch: `POD_GUARD=0` in /etc/pod-guard.env (proved: logs "off", touches nothing). Log: box ~/.local/share/render-desk/pod-guard.log. Tests: `python3 tools/pod_guard_test.py` (16/16 on the box).
- workbench.py (Mac and box, identical, backups workbench.py.bak-2026-11-15) now writes ~/.wb_last_use on the pod on every run/push/pull, and `up` adds the box's ssh key to each new pod. Not committed.
- PROVEN on a real pod 15 Nov 2026: the mom-character chat's pod tient5ud71lup2 (box-started, $0.89/h) was read every minute ("idle 2 min" ... "idle 10 min") and terminated at 11:14:42 EAT, "idle 11 min (gpu 0 %, cpu 0.00 cores)"; RunPod then listed 0 pods. The box's workbench.json still said up afterwards (its cost is logged at the next `workbench up` as "found dead"). The idle-CPU of a live Blender is not measured yet (threshold 0.5 core is a guess). A live Blender must write ~/.wb_last_use on each connector command (start_live.py hook), or the guard stops it 10 min after the last workbench command.
- Shutting down a pod someone else's chat holds: take it down when it has been idle 10+ minutes and tell that chat.
