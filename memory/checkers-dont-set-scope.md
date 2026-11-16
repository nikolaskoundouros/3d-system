---
name: checkers-dont-set-scope
description: "Reviewer and auditor findings outside the approved issue go on a list for Nick, never into the spec or code; my reading of his words is not a requirement."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5f27bc71-0240-42c6-8d1d-be6a75dbfcd0
  modified: 2026-10-09T08:06:58.013Z
---

Nick, 2026-10-09, on the [other project] privacy filter: "while your checkers were working, you started creating your own
rules and tasks and kept looping into working those out, which messed up our code, which is a pretty simple task to
accomplish. that for me is a major failure".

**Why:** a simple filter (strip secrets and patient data, any transcript) became spec v1 to v3.4, three spec audits
(not in PROCESS.md), 46 agent runs, 147 lines of regex and 705 of tests. Each auditor or reviewer finding became a new
rule, and I read "super safe and HIPAA compliant" as "catch all 18 Safe Harbor identifiers by pattern". A pattern
filter always has another format to miss, so the loop had no end. [[fix-only-what-flagged]] already said this, and I
broke it anyway because reviewer findings did not feel like "my" extras.

**How to apply:** once Nick approves an issue, its scope is fixed. Reviewers and auditors report only defects against
it; everything else goes on one list for Nick. One check of a spec, two code review rounds, then stop and hand him the
list even if findings remain. Take the smallest reading of his words and ask about the rest. Related:
[[smallest-fix-first]], [[tuning-not-fixing]], [[ask-never-invent]].
