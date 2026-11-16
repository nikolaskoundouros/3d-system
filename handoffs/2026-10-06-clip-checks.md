# clip-checks (2026-10-06): machine checks + a benched reviewer for the Zack clips

## What this session was doing
After the stitches clip (see 2026-10-06-stitches.md) Nick asked for a repeatable process. Decided together, 6 Oct afternoon:
the process is the skill ~/.claude/skills/zack-clip/SKILL.md (his words, from the transcript). Of the 15 agent roles we
listed, most would be bloat (his own audit: 11 of 72 skills ever used); what pays back now is ONE fresh-context reviewer
plus checks as scripts (Boris: a check, not a prompt). Built in ~/Desktop/clip-checks (newproject template) while the
stitches final rendered on the desk. Stitches folder frozen until the final is delivered.

## Decisions (with why)
- Reviewer as an agent, everything else as scripts: reviewers caught real things in this chat (crash smear, panning push,
  flashing dissolves, zipper swelling, staple suture); the other roles are tools that already exist.
- Thresholds come from Nick's verdicts, not taste: pacing meter must flag the v3 preview's slow biology (9.7-16.7 s, his
  note "the camera movement is a bit too slow") and stay silent on seq1, seq4, seq6 and the heart final. It does.
- Mix check measures the bed UNDER speech from the final mix (voice aligned by envelope, bed power = mix - voice), because
  the raw music stem (-9.1 LUFS) says nothing about the mix. Stitches: voice 11.1 dB over the bed; floor set at 8 (Nick to confirm).
- Detail compare judges at the smaller common size so pixels alone earn no credit; fail only when texture AND edges are
  under 60 percent of a locked reference. Bank seeded with the stitches HQ wound and neutrophil.
- Next node only if the correction count drops on the next clip (this chat: 333 messages from Nick).

## Files
- ~/Desktop/clip-checks/checks/pacing_meter.py, mix_check.py, detail_compare.py (the checks)
- ~/Desktop/clip-checks/verify.sh (4 real checks, passes; awaiting Nick's approval, agents never edit it)
- ~/Desktop/clip-checks/bench/cases.tsv (40 cases: file sent, Nick's verdict PASS/FAIL/PARTIAL, his words), bench/media/
- ~/Desktop/clip-checks/bank/ (locked full-quality stills)
- ~/.claude/agents/clip-reviewer.md (runs the checks, then looks, reports second + place + fix, never fixes)
- ~/.claude/skills/zack-clip/SKILL.md (the process); memory zack-clip-skill.md, clip-checks.md

## Rules Nick stated this afternoon
- Don't touch the running render or the stitches pipeline; if building would affect them, don't build.
- Build only what serves a purpose, not bloat; scripts the user writes himself (the clip scripts) stay his.
- "Graph engineering method" = Boris/Karpathy: one task per node, a checker it cannot edit, peers agree before going up,
  orchestrator loops, only then Nick; no new agent without three repeats.

## Open loops
- Nick to approve verify.sh and the min-gap floor (8 dB).
- Run the reviewer agent on bench/cases.tsv and score agreement with Nick's verdicts (not run yet: nothing executes until
  the stitches final lands). Scorer to write: PASS/FAIL agreement, PARTIAL counts as FAIL.
- Static threshold (change-min 0.01) not calibrated against a verdict yet (no "nothing happening" preview file identified).
- Resume: "Resume clip-checks: read ~/AgencyOS/handoffs/2026-10-06-clip-checks.md and run the reviewer on the bench."
