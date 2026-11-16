---
name: daily-budget
description: Daily spend budget in the gate hook: Higgsfield 20 credits, ElevenLabs 5000 credits per day without asking; known prices only
metadata:
  type: feedback
---

Nick 2026-10-13: "lets put a daily budget for elevenlabs and higgsfield so you can work freely". gate.py rule 13 +
~/.claude/hooks/budget.json (higgsfield 20, Nick 2026-10-14 "lets just do 20 credits a day for higgsfield"; elevenlabs 5000, my proposal). Covered without a yes:
Higgsfield gpt_image_2_5 at default quality/size with no reference media (0.25 each) and ElevenLabs speech
(about 1.05 credits per character per take, measured: 84 chars 83.99, 640 chars 671.93). Other models, video,
voice design, or past the cap still need his yes. Running total in ~/.claude/hooks/state/spend-YYYY-MM-DD.json.
Before: ElevenLabs creative_* tools were not gated at all. Backup gate.py.bak-2026-10-13. Tested with temp state.
Still tell him what was spent, with the ledger figure.

Related: [[approval-before-3d-generation]], [[[other project]-sol-template]]
