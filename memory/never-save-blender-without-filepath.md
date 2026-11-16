---
name: never-save-blender-without-filepath
description: Never call bpy.ops.wm.save_mainfile() without an explicit filepath over the MCP bridge; it overwrites whatever Nick has open.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7567e469-b7e2-47ee-adb7-f893ae7d70b9
  modified: 2026-08-07T10:03:36.846Z
---

Over the Blender MCP bridge, ALWAYS pass an explicit filepath: `bpy.ops.wm.save_mainfile(filepath=...)`. Never the bare call.

**Why:** on 2026-08-07 a bare `save_mainfile()` intended for the sofa file wrote to `~/Downloads/main file.blend`, the characters file Nick actually had open, baking in viewport changes meant for a different scene (Material Preview + scene world/lights + overlays off). It looked to him like two new bugs (purple characters, slow playback) that were really one bad write plus a pre-existing condition it exposed.

Also: `bpy.ops.wm.open_mainfile()` over the bridge wipes bpy.data mid-script and leaves `bpy.context.screen` as None. Iterate `bpy.data.screens` instead of `bpy.context.screen`, and never assume the file you targeted is the file that is loaded. Verify with `bpy.data.filepath` before any write.

**How to apply:** before any save, print `bpy.data.filepath` and confirm it is the intended file. Prefer building headless via `Blender -b --python` and only using the live session for viewing. Do not save Nick's open file without asking; leave changes in-session and tell him to Cmd+S. See [[no-rendering-without-permission]] and [[machine-and-render-workflow]].
