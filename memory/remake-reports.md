---
name: remake-reports
description: "every tutorial remake gets an HTML report on Nick's Desktop, plus a daily performance scoreboard; where they live and how they are fed"
metadata:
  node_type: memory
  type: project
  originSessionId: 91146be5-61d4-4e07-8155-c742ca960e21
  modified: 2026-11-05T19:13:54.492Z
---

Nick, 2026-11-05: "for every tutorial i want a remake report html on my desktop to check them in the morning. and i want you to track your performance so we get better every day."

- Pages: ~/Desktop/remake-reports/ (index.html, <id>.html, performance.html), built by ~/Desktop/aow-modules/tools/remake_report.py from the remake folders only.
- Inputs: learn/<id>/report.json (learner), learn/audits.jsonl (coordinator's own check of each pass), learn/verdicts.jsonl (Nick's verdicts, recorded when he gives them), learn/mistakes.jsonl (every caught mistake + lesson), learn/performance.jsonl (one row per day).
- Every morning: record Nick's verdicts in verdicts.jsonl, rebuild, compare with yesterday's row.

**Why:** Nick checks remakes from the pages, not from chat, and wants a measurable "better every day".
**How to apply:** audit every pass from pass.png and the try in lib/INDEX.md (not the newest file); log my own mistakes too. Related: [[remakes-no-try-limit]], [[picture-with-every-ask]].
