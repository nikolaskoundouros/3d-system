---
name: pod-day-cap-removed-2026-11-15
description: Nick removed the render-desk WORKBENCH_DAY_CAP_USD on 2026-11-15; do not ask to raise it again; idle stop and 5 h hard stop stay
metadata:
  node_type: memory
  type: feedback
  originSessionId: e65a00e1-a107-4d86-b6ab-a7ab62f8d72f
  modified: 2026-11-15T11:39:37.681Z
---

On 2026-11-15 Nick said "remove the fucking cap and get to work" after a pod run was refused ("today's workbench cap is used", $14.56 of $15, $14.29 of it one overnight pod row booked at 09:44).
I set `WORKBENCH_DAY_CAP_USD=1000` in ~/.config/render-desk/render.env (backup render.env.bak-2026-11-15b). DAILY_SPEND_CAP_USD=20 and MONTHLY_SPEND_CAP_USD=65 were left as they were (day $5.44 and month $18.21 left that day).

**Why:** the cap blocked cheap short runs (~$0.10) because of one forgotten overnight pod; Nick was frustrated that I offered "raise the cap" as an option instead of just doing it when he had already decided.
**How to apply:** do not ask about the workbench day cap again and do not offer it as a choice. The 10-minute idle stop and 5 h hard stop still protect against forgotten pods ([[pod-idle-10-min-stop]]); still put a time limit on every pod run ([[pod-guard-before-every-run]]). If a run is refused by the DAILY or MONTHLY desk cap, say so in one line. Earlier note: [[pod-limits-raised-until-1109]].
