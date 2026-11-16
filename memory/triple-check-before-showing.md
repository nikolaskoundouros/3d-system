---
name: triple-check-before-showing
description: "STANDING RULE (Nick, 2026-08-17): always double or triple check before giving him anything; one measurement is never evidence; frame review AND video review are both mandatory"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: fb751d85-21c6-4d16-9f9a-a0509e4a1e49
  modified: 2026-10-07T10:56:50.281Z
---

**Nick, 2026-08-17: "make sure that you add a fact that you should always
double or even triple check before you give me something. also frame review
and also video review?"**

**Why:** one session produced THREE broken versions before a good one (seam
teleport +91 to -998 %/s, wrong end framing, luma 116 vs Zack's ~72), a
PUBLISHED DECODE that was flat wrong (I credited the camera for a beat the
SUBJECT was carrying), and a near-miss false diagnosis. Four measurement
methods lied in that one session:
- cv2 frame SEEKING returns duplicate frames -> fake near-zero motion
- optical flow SATURATES on crash zooms -> under-reads violent moves
- optical flow BREAKS on parallax + a large moving subject (residual 10-16)
- optical flow BREAKS on repetitive untextured lattices (reads ~0 on a camera
  that is provably moving)
He also had to ASK for video review, because I kept sending frame strips that
hid the very motion he was judging.

**How to apply, every time:**
1. **Never trust one measurement.** Cross-check with an independent method. In
   Blender the CAMERA MATRICES are ground truth; pixel measurement is a
   cross-check that can be OVERRULED, never the primary evidence.
2. **Read frames sequentially, never seek.**
3. **A gate built on a bad measurement is worse than no gate.** When a gate and
   the frames disagree, re-derive the gate rather than obeying it.
4. **BOTH reviews before showing: FRAMES (composition, framing, luma, clipping)
   AND VIDEO (side by side vs reference, normal speed AND slowed).** Frames
   hide motion; video hides detail.
5. **Rebuild twice and confirm determinism** when the output is generated.
6. State plainly what was checked, what failed, what is still uncertain. Lead
   with breaks. Never "looks great" without the evidence.

Enforced in code: `~/Desktop/zackd/blender/campresets/verify.py` runs 3 passes
(analytic / frames / video) and 3 checks (determinism / cross-method / human
artifacts) and prints DO NOT SHOW until all clear. Baked as LAW 0.17.

Related: [[blender-camera-presets]], [[skill-of-comparison]],
[[show-before-approve]], [[verify-before-asserting]], [[frequent-visual-checks]].
**TRIGGER: before showing Nick ANY deliverable.**

## Merged from send-final-only (2026-09-19)


**Nick, 2026-08-17: "always send me final versions. if you see that something
is off, fix it first."**

**Why:** I kept sending work I had already spotted problems in, then asking
"fix the last two numbers first?" That wastes his attention twice: once to
look at something I knew was wrong, once to answer a question I could answer
myself. If I can see the defect, fixing it is my job, not a decision for him.

**How to apply:**
- If I notice ANY defect before sending, fix it, re-verify, then send.
- Never ask "should I fix X first?" when X is a known flaw. Just fix it.
- Never send a deliverable with a caveat that amounts to "this is wrong but
  here it is anyway".
- Sending is the LAST step, after the fix and after I have looked at it
  myself (R1 of the campresets ruleset).
- Only surface a limitation when it is genuinely not fixable by me, or when
  fixing it needs a decision only he can make (taste, scope, spend).
- The reply that accompanies a final version states what it IS, not a list of
  things still pending.

**Broken again 2026-10-07 (acid reflux v09 opening):** under "update now" I sent a preview judged from 180 px contact
sheets, skipped the clip-reviewer, and listed known defects as caveats. Nick found 9 profound mistakes (burger through
his face, teeth floating off the skull, bite vanishing inside the closed tube, crystal-shard splash...). "Update now" is
a request for a TEXT status, never for an unchecked file. Contact sheets are for finding frames, not for passing them.

Pairs with [[triple-check-before-showing]] (verify before showing) and
[[show-before-approve]] (send it and wait for his verdict). This rule governs
WHAT gets sent: only the finished thing.
