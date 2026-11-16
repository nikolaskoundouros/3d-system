---
name: smallest-fix-first
description: "STANDING RULE (Nick, 2026-08-18): stop trying to do too much; when something breaks, make the smallest targeted fix instead of redesigning the whole thing"
metadata:
  type: feedback
---

**Nick, 2026-08-18: "i think the biggest problem is that you try to do too much
and when it breaks somewhere you try to redo the whole thing."**

**Why:** the pattern repeated all session and cost hours.
- grey-box comparison looked wrong -> built an entire scene-spec system
- a measurement lied -> built camtrack, then rewrote camtrack
- the solver oscillated on one added term -> rewrote it as a Jacobian, then
  rewrote it again as a secant
Each rewrite REPLACED something that already worked. The 3-target solver hit
8% error; adding one violence term broke it to 38%, and instead of backing that
one term out I redesigned the solver twice more (Jacobian 49%, secant unfinished).

**How to apply:**
- When something breaks, change the ONE thing that broke. Do not redesign the
  surrounding system.
- If a change makes a metric worse, REVERT IT FIRST, then try a smaller version.
  Never stack a second redesign on top of a failed one.
- Keep the last known-good state and say what it is, out loud, before touching
  anything.
- Prefer one parameter over a new module. Prefer a new module over a new
  architecture. Almost never the architecture.
- Scope creep counts as doing too much: build what was asked, not the general
  system that would also solve it.

Related: [[triple-check-before-showing]], [[triple-check-before-showing]],
[[no-reflexive-agreement]]. **TRIGGER: any time a fix does not work first try.**
