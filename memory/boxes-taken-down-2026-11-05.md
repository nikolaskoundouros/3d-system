---
name: boxes-taken-down-2026-11-05
description: "On Nick's go (2026-11-05, \"take down all of them except humgen\", OC too) every site, service, timer, cron and Claude session on clip-a and clip-b was stopped; undo list on clip-a /root/takedown-2026-11-05.txt."
metadata:
  node_type: memory
  type: project
  originSessionId: 26296b6a-d94f-4d53-aa60-c74dc41a2aad
  modified: 2026-11-05T14:41:20.470Z
---

Nick, 2026-11-05: "take down all of them except humgen now", then about nick-oc: "ok i dont need that. put it down too".
Done the same day (checked after: only ssh listens on clip-a; koxynos, lazarou, nofilter, studio and render .nofilter.com.cy give no answer):
- clip-a (46.62.230.121): disabled + stopped caddy, nofilter@koxynos/lazarou/staging-koxynos, studio@usclient, render-desk, clod,
  clip-bridge, claude-clip, clip-gated, check-locker, 4 nofilter timers; nick-oc cron lines commented "#TAKENDOWN"; tmux killed.
  Undo list with prior states: /root/takedown-2026-11-05.txt. Service DATA kept (/opt/nofilter, /opt/studio, /opt/clod, /srv/clip-gate, /opt/nick-oc).
  Deleted (each had a Drive copy in Nick-AE/Archive-2026-10-08 or -09): bank-money, acid-reflux, stitches, zack-shorts, robbery zip;
  plus render-desk 4-needs-a-fix (4 GB failed jobs), baraka-room; journal to 50M. Disk 36G -> 19G used.
- clip-b (37.27.148.115): tmux Claude killed; small clip folders and clips inbox deleted. Kept: Documents/HumGen3D, hg (HumGen zip).
- dandruff, splinters (clip-a) and hero (clip-b) had no other copy; deleted on Nick's "Yes, delete them" the same day. After: clip-a 13G used / 23G free, clip-b 11G used / 26G free.
So [[clip-box]], [[clod-home]], [[render-desk]], [[clip-gate]] and the Telegram bridge describe things that are now OFF; clip-box verify.sh will fail.
Plan in progress: AOW work moves to clip-b ([[machine-and-render-workflow]]); phone link needs a new way since the bridge is off.
Rename (Nick 2026-11-05: "this is something new. we should rename it to 3D System"): clip-b (37.27.148.115) hostname set to `3d-system`
(hostnamectl + /etc/hosts). cloud-init has preserve_hostname: false, so it reverts on reboot unless the server is also renamed
`3d-system` in the Hetzner console (Nick's step; I have no Hetzner access). Call it "3D System" from now on, not clip-b.
Hetzner console (project trial-run, id 15662014), done via Claude in Chrome on Nick's go: server #169530450 renamed `3d-system` (so the hostname now survives reboots).
Both servers were CX23, 2 vCPU / 4 GB / 40 GB, EUR 6.53/mo each (console price). clip-a = server #161929966 "ubuntu-4gb-hel1-2"; its Delete tab was opened for Nick to click himself (permanent wipe).
clip-a DELETED by Nick in the Hetzner console 2026-11-05 (checked after: server list shows only 3d-system, project resources 6 -> 3, ssh to 46.62.230.121 times out). The undo list and all clip-a data are gone. Telegram bridge, Clod, render desk, clip-gate, nick-oc, client sites no longer exist anywhere.
Move to 3d-system paused 2026-11-05 ~18:30 after steps 1-4; resume word "Resume 3d-system move", state in ~/AgencyOS/handoffs/2026-11-05-3d-system-move.md.
