---
name: machine-and-render-workflow
description: "Nick's Mac specs, the Blender render-to-Google-Drive workflow, and the RAM constraint that causes lag"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0fd6f7ef-8bdd-45c3-9289-ddb64ba4d5d7
  modified: 2026-11-14T15:43:05.203Z
---

Nick's machine: **Apple M1, 8 cores, 8 GB RAM**, ~60 GB free on a 228 GB internal SSD. The **8 GB RAM is the real bottleneck** - the lag he notices during rendering is mostly RAM pressure, not disk. Advice: don't run Blender and Premiere at once; keep Chrome closed while rendering.

Render workflow he wanted ("render on my drive not my harddisk"):
- Render LOCALLY to `~/BlenderRenders` (never render directly into Google Drive - it uploads each frame live and thrashes CPU/network, making lag worse).
- When done, move finished renders to Google Drive: `~/Library/CloudStorage/[email]/My Drive/Blender Renders/`. Drive is in **Stream mode** (0 B local), so moved files leave the SSD - which frees disk exactly as he wanted.

Blender **Metal GPU is enabled** in prefs (Apple M1 GPU - 7 cores, saved 2026-07-24). Note EEVEE already uses the GPU; the Metal setting mainly matters for Cycles.

Browser-based video renders (headless Chromium + ffmpeg, measured 2026-10-01): pass `--use-angle=metal --enable-gpu --ignore-gpu-blocklist`; the GPU path was about 2x faster per frame than the default software renderer and matched it to under one colour level. Render formats **one after the other, never in parallel**: two 30 s formats at once took 87 min; one at a time took about 10.5 min each.

**Never run Blender on the Mac, not even a live/GUI session** (Nick, 2026-11-14: "we dont run blender on my mac because it makes it slow"). Live Blender for the MCP connector goes on the workbench pod (GUI Blender + MCP add-on under a virtual display, port tunnelled to the Mac); headless work goes to the box or pod. The MCP add-on (MCP for Blender 2.0) is installed in the Mac's Blender 5.1 user add-ons but Blender must stay closed there.

Apps: Blender 5.1.2 and Premiere Pro 2026 + Media Encoder installed. **After Effects is NOT installed.** Plan: learn Blender first, then Premiere (does most zack2-style moves), AE later if needed. See [[blender-lessons]].
