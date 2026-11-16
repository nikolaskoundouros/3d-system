---
name: research-before-execute
description: "STANDING RULE - research the method (web search, docs, the actual tutorial) BEFORE executing, never brute-force by guessing"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a6f3536d-6ad3-4faf-8a74-cb864983e861
  modified: 2026-11-15T08:43:28.826Z
---

Before executing any task, research it first: web search, read the real documentation, watch/read the tutorial properly. Do not improvise settings and iterate blindly.

**Why:** On 2026-08-05 Nick gave me a one-minute Blender cloud tutorial. I pulled its captions and a frame strip, then guessed my way through ~6 full scene renders (roughly 20 minutes and a lot of his paid credits) and still produced bad clouds. I never once ran a web search, never opened the Blender docs on Mesh-to-Volume / Volume Displace, never looked up why EEVEE renders volumes dark. The problem was already solved on the internet; I was brute-forcing it. Same pattern with the eagle: four full scene renders before one cheap isolated test that answered it instantly. His words: "i gave you an easy one minute tutorial but you are completely useless."

**How to apply:**
- Search the web / read docs BEFORE the first execution attempt, not after failures pile up.
- When Nick supplies a reference (tutorial, video, link), study it properly and follow its ACTUAL steps and settings, do not paraphrase from a transcript and improvise.
- Test the smallest isolated case first (seconds) before any expensive full render or full pipeline run. See [[frequent-visual-checks]].
- Verify inputs before using them (I lit a cloud with `hayloft_2k.hdr`, a barn interior, and rendered a barn).
- Research for capability, not for writing documents. See [[no-doc-sprawl]].
- Credits and render time are real costs. See [[machine-and-render-workflow]].

**Again on 2026-11-12 (navy storyboards):** I hand-built ships, sea, foam and clouds over about 20 rounds, measured and reviewed every render, and still stalled (carrier 3 of 10 regions, cruiser 1 of 10). Nick: "i dont think you need them. i just think you need some sort of research on how to do it". The checking loop does not replace knowing the method: research the technique for each look (ocean and foam, volumetric clouds, hard-surface detail and weathering) before the first build, then let the loop tune.

**Third time on 2026-11-14 (the mom's half-up bun):** I wrote my own strand grower, clumping and interpolation and ran 6 four-minute test renders before searching. The search then showed Blender 5.3 on the box already ships ~30 hair node groups (Interpolate, Clump, Curl, Frizz, Noise, Smooth, Set Hair Curve Profile) and that image-to-strands models exist (DiffLocks, non-commercial licence). Nick: "is it still because we're not doing adequate research?" **Blender: the manual comes first** (Nick, 15 Nov: "we can always use the manuals to make stuff right? it could be part of the research"). Before using any Blender tool, node, brush or shader, read its page in https://docs.blender.org/manual/en/latest/ (fetch the page directly; the reader tools miss the text behind ~100k chars of menu). On 15 Nov the manual explained all three 14 Nov failures (curl Subdivision, Chiang roughness/Coat, open colliders). Notes: ~/Desktop/mom-character/notes/blender-manual-hair.md. Offline copy on the 3D System box: `bman "words"` searches all 2,453 pages in 0.25 s, `bman -p <path>` prints one (~/Documents/blender-manual, official 5.3 HTML package, downloaded 15 Nov; re-download blender_manual_html.zip from docs.blender.org/manual/en/latest/ and run `bman --build` for a new version). Before any look or asset: 15 minutes of search (how pros build it, what ships with the tool, ready assets, AI options), then pick a base, then build.
