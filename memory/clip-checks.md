---
name: clip-checks
description: "~/Desktop/clip-checks: machine checks for the Zack clips (pacing meter, mix check, detail compare) calibrated on Nick's verdicts, plus the clip-reviewer agent and its 40-case bench; built 2026-10-06."
metadata:
  node_type: memory
  type: project
  originSessionId: 6d168762-61ef-4d14-9020-9cfd3ffc7c96
  modified: 2026-10-06T15:11:51.834Z
---

~/Desktop/clip-checks (newproject layout, verify.sh passes with 4 real checks). checks/pacing_meter.py flags camera holds
over 1 s and static stretches (thresholds set so the v3 stitches preview flags 9.7-16.7 s and every locked sequence is
clean); checks/mix_check.py measures the bed under speech from the final mix (stitches: voice 11.1 dB over, floor 8);
checks/detail_compare.py scores a still against bank/ (locked HQ frames). ~/.claude/agents/clip-reviewer.md runs them,
then looks, never fixes. bench/cases.tsv holds 40 files Nick judged with his words (10 PASS, 24 FAIL, 6 PARTIAL).

**Why:** Nick decided (6 Oct) against 15 agents: one reviewer plus checks, next node only if his correction count drops.
**How to apply:** run the checks on every preview before sending; score the reviewer on the bench before trusting it.
Handoff: ~/AgencyOS/handoffs/2026-10-06-clip-checks.md. Related: [[zack-clip-skill]], [[stitches-clip]], [[review-bench]].
