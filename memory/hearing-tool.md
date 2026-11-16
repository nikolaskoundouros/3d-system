---
name: hearing-tool
description: "I can now \"hear\" audio via ~/Desktop/[other project]-brand/tools/hear.py (AudioSet tagger, 527 sound labels); use it on every reference and every mix"
metadata:
  node_type: memory
  type: reference
  originSessionId: 2e25bc24-e09d-4389-9ce0-a02eb50a60e9
  modified: 2026-10-20T09:36:23.274Z
---

Built 2026-10-20 after Nick: "why cant you hear audio? we need to fix that!" (I missed the ambulance siren in his
Keep thinking reference at 15 to 17 s, and the line "there's never been a worse time" at 19.1 s).

`~/.venvs/demucs/bin/python ~/Desktop/[other project]-brand/tools/hear.py <video|audio> [--step 0.5 --win 1.0 --top 3 --json f]`
prints, per window, the top AudioSet labels (MIT/ast-finetuned-audioset, runs free on the Mac) and the level in dB.
Run it on the demucs stems too (vocals / other) to separate voice from effects. Speech-to-text is
~/.venvs/whisper/bin/whisper on the vocals stem.

**How to apply:** before describing any reference's sound, and on every generated sound effect before placing it
(ElevenLabs effects came back wrong about half the time on 2026-10-20: a "clock" read as a door, "wind" as water).
Related: [[stimulus-every-sixth]], [[analyze-means-analyze]].
