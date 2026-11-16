---
name: clip-box
description: ~/Desktop/clip-box keeps every Hetzner box change for the clip session (Telegram in/out, boot unit, spend guard) as exact copies; ./verify.sh (25 checks) fails on any drift.
metadata:
  type: project
---

Built 2026-10-07 on Nick's ask: "lets make sure the changes stay in tact. it is important to nail the process so my
editor can use the box too". box/<path> mirrors /<path> on root@46.62.230.121 byte for byte; checks/box.py also checks
services (clod, clip-bridge, claude-clip enabled at boot), Clod's sandbox unchanged, Telegram in from inside Clod's
sandbox, the reply hook (sends only from tmux session `clip`, silent elsewhere, TG_DRY=1 dry run), render-desk on the box
== the Mac's, and the GPU cap code not writable by nick. A planted drift failed it (tested). claude-clip.service runs
`claude --continue` in tmux at boot (cold and warm paths tested on dummy sessions; claude -p under systemd as nick works).
2026-10-08: second session `robbery` (bank money, ~/Desktop/bank-money copied to the box, brief refs/brief_2026-10-08.md).
Nick started it himself: the auto-mode classifier blocks me from creating an always-on auto-mode Claude ("Create Unsafe
Agents"), even after his "yes its safe" in chat; it has NO boot unit, so after a reboot he reruns the ssh tmux command.
Telegram texts starting with "robbery" go to it (clip-bridge target()), replies come back as "Claude (robbery)".
Editor access is NOT set up: waiting on Nick's answers (own Claude login, own Telegram, GPU budget). See [[clod-home]] [[render-desk]].

2026-10-13: third session `[other project]` ([other project] films, ~/Desktop/[other project]-brand copied to the box, handoff BOX.md):
clip-bridge SESSIONS + target() and tg-stop-hook LABEL gained '[other project]'; start script /Users/nick/start-[other project].sh
(Nick runs it; no boot unit). Playwright venv at /Users/nick/.venvs/film. Freed disk 99% -> 86% on Nick's "delete
whatever is not necessary": acid-reflux sim caches (3.0G), /var/tmp/moved-from-tmp-2026-10-09 test blends (1.3G),
apt cache, journal to 50M. verify.sh PASS after. My earlier claim "the box has no claude login" was stale (clod-home note).
