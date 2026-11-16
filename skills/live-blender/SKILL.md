---
name: live-blender
description: A real, open Blender with a screen on the RunPod workbench pod, worked three ways without writing code - Claude through the Blender MCP connector, a real mouse (xdotool strokes for sculpt, grab, comb, add hair), and PlotPointe's Animate page (Blender in the browser, buttons, chat). Use whenever Blender work needs to be seen or done by hand, for brushes that only work with a mouse, when Nick says "live Blender", "open Blender", "show me in Blender", "use the mouse", or for PlotPointe's live Blender page. Blender never runs on the Mac.
argument-hint: [what to do in the live Blender]
---

# Live Blender

Built 12-14 Nov 2026: PlotPointe's page (12-13 Nov) and the mom hair chat's mouse work (14 Nov). Memory
`blender-live-on-pod.md` holds the measured details; `plotpointe.md` holds the page's history.

## Before anything
- It costs money: workbench pods cost $0.59 to $1.19 an hour (rates in the Mac ledger, 15 Nov). Say the cost and get Nick's "go" before `workbench up`.
  The monthly spend cap was used up on 15 Nov (-$6.52): only Nick raises it.
- Blender never runs on the Mac (8 GB). The pod is started with `~/Desktop/render-desk/bin/workbench up`
  (from the box, hold `flock /tmp/aow-wb-up.lock` around status + up: two runs once rented two pods).
- Idle stop: `pod-guard.timer` on the 3D System box terminates a workbench pod 10 min after the last command when
  it is not busy (Nick, 15 Nov: "after 10 idle minutes please shut the pod down"). Commands that count: every
  workbench run/push/pull and every connector command (start_live.py below). Off: `POD_GUARD=0` in /etc/pod-guard.env.
- Before ending any turn with the pod up: stop it (`workbench down`) or tell Nick in one line it is billing.
- Write every setting that worked into a script file before the turn ends: live-only changes die with the pod.

## Files (all in this skill's `scripts/`, saved 15 Nov from the mom hair chat)
| file | runs where | what it does |
|---|---|---|
| `blender_mcp.py` | pod, inside Blender | the MCP for Blender add-on (protocol 16, from the uvx package `mcp-for-blender`) |
| `start_live.py` | pod, `--python` | installs and enables the add-on, starts its server on 127.0.0.1:9876, restarts it if it stops, and writes ~/.wb_last_use on every connector command |
| `live_tools.py` | pod, `exec(open(...).read())` | `snap(path)` viewport picture drawn off-screen, `shoot(tag)` four Cycles GPU head views to /root/live_snaps, `view_on(obj)`, `screen_xy(point)` screen pixel for the mouse, `ctx()`. Kept in `bpy.app.driver_namespace` (the connector's namespace does not persist) |
| `drag.sh` | Mac | `drag.sh "x1,y1 x2,y2 ..." [stroke2 ...]`: real mouse strokes in the pod's screen with xdotool, through `workbench run`. `STEP=` sets the pause between points |
| `sim.py` | pod | steps a simulation from frame A to B, stops if Blender passes 12 GB |
| `pullcmp.sh`, `compare.py`, `flowmap.py`, `rebuild_live.py`, `live_dyn.py` | mom hair project | pull the four head views and put the reference above ours; hair flow map; rebuild mom and her particle hair. Their paths still point at the mom hair chat's scratchpad (`/private/tmp/.../f3d1b7da.../scratchpad`): they break when that folder is cleared |

## Start a live Blender (the connector + mouse way)
1. `workbench up`, then `workbench push ~/.claude/skills/live-blender/scripts` (same absolute path on the pod).
2. For the mouse and a GPU viewport: on the pod `apt-get install -y xdotool` and VirtualGL 3.1.5 (.deb from the
   VirtualGL GitHub releases).
3. Start in the background (the `workbench run` stays open while Blender is open):
   `workbench run "cd ~/.claude/skills/live-blender/scripts && xvfb-run --auto-servernum -s '-screen 0 1920x1080x24 +extension GLX' /opt/VirtualGL/bin/vglrun -d egl \$BLENDER --python start_live.py"`
   Without VirtualGL: `LIBGL_ALWAYS_SOFTWARE=1 xvfb-run ...` (software drawing; mouse sculpt needs the GPU one).
   Write `--auto-servernum`, never `-a`, and never print the bare word "blender " next to `-a`: the gate hook reads it
   as a Mac animation render.
4. Tunnel: `ssh -f -N -L 127.0.0.1:9876:127.0.0.1:9876` to the pod target in `~/.local/share/render-desk/workbench.json`.
5. The `blender` MCP tools in Claude now drive it (`get_scene_info`, `execute_blender_code`). The connector's `look`
   fails remotely: use `snap()` or `shoot()` and `workbench pull /root/live_snaps DIR`.

## Working it without code
- **Curves sculpt by mouse: read `cursor-recipe.md` first** (15 Nov: the harness sent 31 clicks instead of one held drag and built the strands off screen; fixed, Comb/Pull Tips/Smooth/Puff/Pinch/Delete measured).
- **Mouse** (proven 14 Nov per memory `blender-live-on-pod.md`, not re-run 15 Nov): hair Add grew 1,160 hairs from 3 drags; Comb moved 516 tips about 6 cm; mesh sculpt
  Draw, Grab and Smooth work with the GPU viewport. Screen pixel from Blender: X = region.x + mx,
  Y = window.height - (region.y + my), or `screen_xy(point)`. Never activate the window before a batch of strokes:
  the first press after it is swallowed as a focus click.
- **Brushes by script** also work (sculpt `brush_stroke` for Draw only, particle Comb): enter the mode in one call,
  stroke in the next, read the result only after leaving the mode. Grab, Smooth and the curves sculpt brushes (Add,
  Comb, Pull Tips: Snake Hook is called Pull Tips in 5.2) need the real mouse on the GPU-drawn screen (vglrun, never
  with LIBGL_ALWAYS_SOFTWARE).
- The mom's last live hair settings (gloss, lower-hair finish) were never written to a file and died with the pod
  (mom hair chat, 15 Nov): a live result exists only once it is in a script.
- **Never** `bpy.ops.wm.read_factory_settings` (blender-funnel `stage.new_scene`) in a live session: it unloads the
  add-on and crashed Blender. Empty the scene instead. `bpy.context.window` is None in connector calls: use
  `bpy.context.window_manager.windows[0]`.

## PlotPointe's Animate page (Blender in the browser, buttons, chat)
Project `~/Projects/plotpointe-animate` (preview server `plotpointe-animate`, port 8575). Live tools in `tools/live/`:
- `pod_start.sh <minutes> <save dir> <shots.json> <first shot> [key file]`: real Blender on a VNC screen (port 6080,
  noVNC) plus `pp_live.py`'s door (port 6081). `PP_BACKEND=vulkan` draws on the GPU (checked 13 Nov: RTX 4090),
  `opengl` = software. Blender is killed after <minutes>.
- `box_run.sh <minutes> <first shot>`: on the box as nick after `workbench up`; pushes tools and scenes, runs
  pod_start.sh, pulls the animator's saves back to /Users/nick/plotpointe-live/saves once a minute.
  Each pull counts as use for the pod guard, so the pod lives until <minutes> ends, then 10 more idle minutes.
- `pp_live.py` buttons: `POST /tool?name=` face, camera_view, bones, play, frame, shading, undo, move, rotate,
  scale, focus. `GET /open?shot=`, `GET /status`, `POST /run?step=` (model build step, session key), `POST /say`
  and `/reply` (chat). Work file per shot, numbered copy every 30 s when changed.
- `router.py` (plain commands and a small Claude choose tools, never code) and `model.py` (wait, step, working,
  say, look) run on the Mac through the tunnel (`PP_API`, default http://127.0.0.1:8577).
- Recipe that ran 13 Nov (save-back worked, all four navy scenes opened): `workbench up` under the lock, on the box
  `python3 ~/limited.py <s> bash /Users/nick/plotpointe-live/tools/box_run.sh <minutes> dock`, box tunnel
  16080/16081 to pod 6080/6081, Mac tunnel 8576/8577, `data/live.js` with `shots` + `api`.
- The box copy `/Users/nick/plotpointe-live/tools/pp_live.py` (28,368 bytes) is about 40 min older than the
  project copy (29,211 bytes, 13 Nov), and box_run.sh sends the box copy. Copy the project's over first, after
  checking the diff.
- Never restart or edit the live `aow-bot` without Nick's go.

## Proven on 15 Nov 2026 vs not
- Proven: the last-use hook in start_live.py (stand-in add-on: a command writes ~/.wb_last_use and its result passes
  through; loading twice does not wrap twice). The pod guard reads that file (box tests 16/16).
- Not run on 15 Nov (no pod: spend cap used up): the start, tunnel, mouse and PlotPointe recipes above. They ran on
  12-14 Nov as written in memory. Run the start once on the next pod and fix this section if anything changed.
