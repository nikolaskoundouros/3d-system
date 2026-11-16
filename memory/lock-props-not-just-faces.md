---
name: lock-props-not-just-faces
description: "Continuity in a shot sequence covers nails, jewellery, wardrobe and props, not just faces; lock a canonical frame and reference it in every shot"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1e82da2d-8351-47a3-bde8-e2408e83d303
  modified: 2026-09-25T07:11:45.383Z
---

**TRIGGER: any multi-shot sequence, before the first batch.**

Nick's rule, given 2026-09-25 on "The Keys": every recurring detail has to match
across frames, not just the character's face. Nails, polish colour, rings,
bracelets, coat, bag, the bottle on the table. He spotted two hands that were
supposed to be the same woman and had different nail colour, different rings and
different bracelets.

**Why:** a face that matches makes the audience trust the cut, and then one wrong
ring breaks it harder than a wrong face would, because it reads as carelessness
rather than style. He called this out unprompted twice in one session, first on a
character and then on props, so it is not a one-off note.

**How to apply:** before generating ANY shot in a sequence, pick the canonical
frame for each element, save it as a reference Element, and pass it as
`image_references` on every single shot that contains it. Never generate a second
frame of anything recurring from text alone. Where a prompt describes a prop,
name its exact colour and form every time rather than relying on the model to
remember. Then look at the finished frames side by side and check the small
things before showing him.

See [[higgsfield-cartoon-pipeline]] and [[triple-check-before-showing]].

**Blocking counts too, and it is now a hard check.** A close-up of one person
delivering a line to somebody who is not in the frame reads as talking to
themselves. Cost 4 credits on The Keys, 2026-09-28. `gate.py` rule 5 now denies
any `generate_video` whose prompt has a spoken line unless the prompt carries
`IN FRAME: <everyone visible>` naming two or more people, or says ALONE /
MONOLOGUE / VOICEOVER / ON THE PHONE on purpose. Test:
`~/.claude/hooks/tests/test-dialogue-listener.py`.

**The animation pass is where the likeness actually goes, not the stills.**
2026-09-28, The Keys. The stills held Jacob's face; the `seedance_2_0_mini` clip
re-rendered him with a sparser beard, a narrower face and thinner eyebrows, and
Nick spotted it when I had already called the clip good. The video model also
does not preserve the start frame's palette, so grading a still is wasted: his
skin came back 25 points cooler in one clip than in the other from identical
graded frames.

**So every clip goes through `~/AgencyOS/videos/the-keys/tools/checkclip.py`
before Nick sees it.** One frame per second, skin tone measured per second
against the canonical frame with a drift flag, and a face strip with the
canonical frame first so the likeness is judged against it rather than from
memory. Tone is then fixed with `tools/skinlock_video.py`, which grades the
rendered frames, never the still. Judge the clip, never the frame it started from.
