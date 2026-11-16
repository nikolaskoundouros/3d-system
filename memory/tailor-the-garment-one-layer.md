---
name: tailor-the-garment-one-layer
description: "Character clothes (navy officer, 12 Nov 2026): reshape the ready-made garment's own mesh in one layer; never lay shells, panels or tubes on top; every still beside the reference before showing"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 646d5d96-3fc1-41f2-ac76-ab4b43da5c4f
  modified: 2026-11-12T17:55:38.208Z
---

Nick, 2026-11-12, navy officer uniform (faces/navy_officer on the 3D System box). He rejected, in order: a smooth shell over the HumGen suit ("it seems that we have two blazers on top of each other", "theres also an extra collar there", "this is a disgrace"), a coat sewn from scratch with cloth simulation ("this is evidence that you arent looking at your work or the reference"), and add-on lapel panels ("i think we dont need a lapel builder, just to change the code of the current lapel right? ... we find the code that makes the clothes and then we tailor it"). He then simplified the brief himself: "just have it single breasted", and approved that ("Yes, use it").

**Why:** anything laid over a garment reads as a second garment at the edges. The ready-made garment already has real lapels, collar, set-in sleeves and fabric texture; moving its own points keeps one layer. My loop is slow and blind (about 3 minutes per look), so large restyles (single to double-breasted) cost many rounds and new faults each.

**How to apply:** for clothes on a ready-made human, start from a plain render of the garment as it ships, beside the reference. Change the garment's own points only (officer_restyle.py: length, flare, slim sleeves, shoulder pad, mirror, overlap, own-lapel widening). HumGen clothes are mesh files, not code: say so plainly. Probe the mesh first (edges, cloth edges, layers: probe_jacket.py) before moving anything. When the reference needs a big structural change, tell Nick the cost up front and offer the simpler cut as the choice ([[challenge-my-calls]]). Put every still beside the reference at the same size and list the differences before showing ([[compare-to-reference-after-stills]]). Smoothing passes must exclude lapels and collars (one ironed his lapel flat).
