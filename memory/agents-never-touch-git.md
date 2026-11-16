---
name: agents-never-touch-git
description: "Swarm builders and reviewers must never run git write commands or touch .git; one builder deleted a repo's whole history"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1cdef201-e02c-4564-a595-7173e97089ed
  modified: 2026-09-18T16:59:44.046Z
---

Every builder, reviewer or grunt prompt carries a HARD RULE line: no git write commands (init, add, commit, reset, checkout, stash, rm) and never touch .git. The orchestrator alone stages, runs the gate and commits.

**Why:** 2026-09-18, [other project]-site-partner, step 5. The builder decided the repo "had no git history", ran git init to get vibecheck --staged working, then removed the .git folder, destroying five commits (two of them reviewed steps). No Trash copy, Time Machine not mounted. History was rebuilt from the live source in Drive, and steps 3 to 5 had to land as one commit. Earlier builders had been told to run `git add -A && vibecheck --staged`, which invited them into git.

**How to apply:** builders run `python3 ~/.claude/skills/swarm/vibecheck.py` in unstaged mode only; the orchestrator stages. Take a scratchpad copy of the working tree before any long builder run. Check `git log` right after every builder returns. Proposal for Nick: add this rule to the eng-builder and eng-reviewer agent definitions. Related: [[engineering-swarm]], [[[other project]-site-v2]].
