---
name: pod-limits-raised-until-1109
description: render-desk spend caps raised to 100/day and 300/month from 2026-11-06 to 2026-11-09 for the remake push; restore after
metadata:
  type: project
---

Nick, 2026-11-06: "for the next few days i would remove the limit so we power up our agents as much as possible."
~/.config/render-desk/render.env: WORKBENCH_DAY_CAP_USD=100, DAILY_SPEND_CAP_USD=100, MONTHLY_SPEND_CAP_USD=300 until 2026-11-09.
Restore from render.env.bak-2026-11-06 (pod 12/day, desk 20/day, 40/month) on 2026-11-09 unless Nick says otherwise.

**Why:** remake and character push; the RunPod balance ([email]) is the real ceiling.
**How to apply:** check the balance before long runs; on or after 2026-11-09 tell Nick the caps are back up for restoring. Related: [[remakes-no-try-limit]].
