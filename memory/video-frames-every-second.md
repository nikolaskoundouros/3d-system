---
name: video-frames-every-second
description: "When analyzing any video Nick sends, extract and look at one frame for EVERY second, never sampled (not every 20s); redo if sampled"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3530636c-3370-4ce4-9f50-4f3879f7ef63
  modified: 2026-09-17T14:48:35.470Z
---

Video analysis rule: extract one frame per second (`ffmpeg -vf fps=1`) and look at every one, alongside the transcript. Sampling (I used one frame per 20 seconds on 2026-09-17) is not allowed; Nick said "the rule is every single second" and had both videos redone.

**Why:** on-screen text (prompt cards, tweets, lower thirds, terminal output) often shows for only a few seconds and carries detail the speech does not.

**How to apply:** frames at 640px, tiled 16 per sheet (4x4, 480px tiles) with a mm:ss label burned in via PIL (homebrew ffmpeg has no drawtext); fan sheets out to parallel viewer agents that must open every sheet in order and list the sheets opened. Get captions with yt-dlp when the video is on YouTube.

Related: [[triple-check-before-showing]], [[verify-before-asserting]]

Not enough for fast cuts (Nick, 2026-10-10, Base44): shots shorter than a second fall between 1 fps frames and cut
detectors merge them. Base44's first 1.62 s holds 8 shots and 7 people, including a posed pair I missed. Read every frame
(24 fps) of any section with sub-second cuts before mapping it.
