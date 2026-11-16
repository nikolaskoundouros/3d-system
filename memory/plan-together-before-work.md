---
name: plan-together-before-work
description: "On [other project] code, never start building, running agents or changing files until Nick and I have discussed the architecture and agreed a plan."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5f27bc71-0240-42c6-8d1d-be6a75dbfcd0
  modified: 2026-10-09T09:28:45.211Z
---

Nick, 2026-10-09: "we need to discuss the code architecture and functionality together and you should never start
working by yourself until we reach a plan and agreement"; earlier the same day: "in the beginning until we figure out
the cleanest process possible you should not do things yourself".

**Why:** the privacy filter grew from a simple task into 853 lines because I and the checkers set the scope alone
([[checkers-dont-set-scope]]).

**How to apply:** discuss first, in chat, a few bullets at a time ([[spec-in-chat-bullets]]); build only what is agreed,
in the agreed files, after his explicit go. Agreed so far (9 Oct): 9 product boundaries; lint rules L1 to L8 (his
"yes" to the list: no own tests, named files only, size cap, no tuning loops, no new work in disguise, named exports
plus repo-wide duplicate check, nothing unused, mutation check). Proposed, not yet answered: code boundaries C1 to C3,
stones S1 to S3. Nothing built.

**Lint rules first, always** (Nick, 2026-10-12: "always lint rules first. always always always"): before any building
step, the lint checks that guard it exist and run. Timeline he set: week 1 connect (done), week 2 build and test
(heavy testing Fri to Sun), week 3 guardrails and tests.

**Boundary changes, 2026-10-12:** B1 is now "it changes Jira only with the asker's approval, never on its own"
(Nick, for a pilot this week). B9 under discussion: Nick finds it redundant because we must pilot often; proposed
split = pilots to a small named group after safety checks pass, wider use after the full bench. Vincenzo questions
added: Slack to the preview (or production) for the pilot; a Jira write token or the Rovo admin setting.
