---
name: clip-gate
description: The enforced checkpoints for every clip (Nick 2026-10-16 after Splinters v3 "absolutely horrible"): clip-gate on clip-a, reviewer service, GPU tool refuses unreviewed renders.
metadata:
  type: project
---

Nick, 2026-10-16: "the process has to be bulletproof though. also build a something that enforces the checks." Why it
broke (my diagnosis, he agreed): every checkpoint was voluntary and I was builder and judge; under time pressure I
skipped the checks and passed my own work. Order: analysis -> basics -> motion -> details -> claude -> sent -> approved
(motion before details and builder-never-checks-itself were my changes; he agreed; approval option b = his chat message).

Built 2026-10-16: /opt/clip-gate (clip_gate.py CLI, gated.py service, checklists/, process.md = skill copy) and
/srv/clip-gate (spool 1733, ledger readable not writable by nick, work); user clipgate owns ~/.claude-b and ~/.codex logins
(moved out of nick's home at install); render-desk renderdesk/clipgate_check.py hooked into workbench.run and live do;
gate.py rule 14 forwards Nick's "approve..." and denies forged approvals and Mac renders. Source: session scratchpad
clipgate/ and clip-a ~/clipgate-stage (install.sh, SHA256SUMS, test_gate.sh). Limits: a deliberate bypass (editing the
Mac hook, ssh to a pod directly) is still possible; it stops skipping, not lying.
Related: [[clip-funnel]], [[splinters-clip]], [[zack-clip-skill]], [[autonomous-check-loop]].
