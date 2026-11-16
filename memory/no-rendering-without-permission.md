---
name: no-rendering-without-permission
description: STANDING RULE - never run a Blender render without explicit permission; it cripples the M1/8GB machine. Use live viewport snapshots instead.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a6f3536d-6ad3-4faf-8a74-cb864983e861
  modified: 2026-08-05T13:16:15.098Z
---

RENDERING IS OFF LIMITS unless Nick explicitly says to render. Full renders make his machine really slow and eat his time and credits.

**Why:** On 2026-08-05 I ran ~10 full scene renders (each 2 to 10+ minutes) iterating on clouds and birds by guesswork. A volumetric render was still chewing the CPU after 10 minutes while he was trying to work. His words: "rendering is off limits unless i say so. you make my machine really slow."

**How to apply:**
- Default loop = RESEARCH first (see [[research-before-execute]]), then build the .blend, then show a **viewport snapshot** via the BlenderMCP bridge (`get_viewport_screenshot`), which is nearly free. Open the GUI with `blender <file>.blend` and screenshot it.
- Build scripts should SAVE the .blend and stop. Do not chain a render onto the end by default; gate rendering behind an env var or an explicit ask.
- If a render is genuinely needed, ask first and say how long it will take.
- Kill any running render immediately if he says the machine is slow (`pkill -f <script>.py`).
- Related: [[machine-and-render-workflow]] (M1 / 8GB, RAM is the bottleneck), [[frequent-visual-checks]] (still show visuals often, just cheap ones).
