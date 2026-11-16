# Fix cursor: curve sculpt brushes by mouse

Session file `f82222c4-c333-47fa-9864-2fb07b56e5d4.jsonl`, first message 2026-11-15T13:29:48.290Z. Images removed, secrets replaced by [REDACTED].
Tool results are cut to 4,000 characters here; raw.jsonl.gz has every line in full.


### USER 2026-11-15T13:29

Background (from the session that started this one):
Nick is rebuilding a 3D character's (the mom's) hair in Blender 5.2.2 running live on a rented RunPod GPU pod (RTX 4090, about $0.89/h; an idle guard on the 3D System box stops it after 10 minutes without a connector command). He wants the agent to be able to use the CURSOR (real mouse strokes in Curves Sculpt Mode: Comb, Pull Tips, Puff, Pinch, Smooth, Slide, Delete, Add) like a human groomer, and today it does not work. Another session (the hair session) keeps working on the same pod and scene at the same time: do not disturb it.

Task:
TASK: find out why real mouse drags do not move hair strands in Blender's Curves Sculpt Mode on our pod, fix it, and write the working recipe down. Read first: `~/.claude/skills/live-blender/SKILL.md` (how to start the pod, tunnel, mouse via xdotool), memory `blender-live-on-pod.md` (it claims Comb moved 516 tips and Add grew 1,160 hairs by mouse on 14 Nov 2026; that is the only evidence it ever worked), `~/Desktop/mom-character/results.tsv` (last 6 rows), and the harness: `~/Desktop/mom-character/scripts/cursor_harness.py` + `harness.sh` (`/tmp/harness.sh "<Brush name>"` is a copy; it builds TestSphere + TestHair (300 strands) at x=6 m, front orthographic view, enters Curves Sculpt, activates the brush, sends a real xdotool drag via `live/drag.sh`, leaves the mode and measures how many points moved). 

WHAT IS KNOWN (15 Nov 2026, all measured, reading results AFTER leaving the mode): Comb (projected falloff), Pull Tips, Puff, Pinch, Delete (spherical falloff, stroke started ON the sphere surface): 0 of 3,000 points moved, 0 curves deleted, on a clean object and on the real hair layers (434k points and 34k points). The Add brush worked only on a direct click on the scalp of the real hair object (6 curves from 2 clicks). The pod does receive the mouse: `xdotool getmouselocation` reports the cursor at the point sent. Strokes were 25 to 31 interpolated points, steps 0.03 to 0.08 s. A VNC viewer (x11vnc + noVNC on pod port 6080, tunnel pod to box to Mac, browser pane) is attached; earlier notes say mouse presses did nothing until a viewer was attached. Suspects not yet tested: motion events during a held button are not delivered as stroke extensions (Add acts on the first event, Comb needs motion); Blender window focus or the first press swallowed as a focus click; the stroke needs the `INBETWEEN_MOUSEMOVE`/timer; GPU viewport (VirtualGL) versus software; xdotool `mousedown` then `mousemove` ordering or using `xdotool` relative moves; a real-time `xinput`/`uinput` device instead of XTest; Blender asset brush needing `bpy.ops.wm.tool_set_by_id("builtin_brush.Comb")` or the toolbar tool selected; sculpt mode entered through the UI mode menu instead of `mode_set`. Try a screenshot mid-stroke through the browser pane to see whether the brush circle is drawn and strands move live.

HOW TO WORK: use the live Blender through `~/Desktop/mom-character/live/bcall.py` (run on the 3D System box `nick＠37.27.148.115`, which talks to Blender on port 9876 through a tunnel; scripts must exist on the box AND be pushed to the pod with `~/Desktop/render-desk/bin/workbench push ~/Desktop/mom-character`; the pod only sees files from the box's copy). Mouse via `~/Desktop/mom-character/live/drag.sh "x,y x,y ..."` on the box. The pod is already up (check `~/Desktop/render-desk/bin/workbench status` on the box; do NOT rent a second pod without Nick's go, and say plainly if it is billing). RULES: the hair session shares this Blender. Touch ONLY the objects `TestSphere` and `TestHair` and the 3D viewport; never change the scene camera, never select, edit, hide or enter a mode on any `Lock_*`, `Hair2_*`, `Mom*` object, always return the viewport to Object Mode, and never call `read_factory_settings`. Do not edit `scripts/hair2_locks.py`, `fit_side.py`, `outline_auto.py` or `results.tsv` rows of others (append your own rows). Never save over an open .blend without an explicit filepath. Bash gate hook: do not write the bare word blender next to `-a` in a command (use `pgrep -c -f vglrun`); in zsh, unquoted variables are not split, so call arguments explicitly. No em or en dashes anywhere in anything you write.

DONE MEANS: (1) a one-command harness result showing Comb moving strands (points moved > 0.5 mm, with the number) and at least two other brushes (for example Pull Tips and Smooth or Puff) responding by real mouse on `TestHair`, with the exact settings that made it work; (2) a short recipe file `~/.claude/skills/live-blender/cursor-recipe.md` with the verified steps, what did NOT matter, and the numbers; (3) one row per experiment appended to `~/Desktop/mom-character/results.tsv`; (4) if you cannot make it work, a ranked list of what you ruled out with evidence, and the one experiment you would run next. Report plainly what is verified first-hand and what is not.

Shared notes folder for this group of sessions (outside the repo; read siblings' notes there, leave hand-over notes or large findings there instead of pasting them into messages): /Users/nick/Library/Application Support/Claude/side-session-notes/local_3bd59381-07cd-47ec-884c-8460247f8b39

- tool `mcp__ccd_turn__update_plan`: `{"items": [{"content": "Read skill, memory, results, harness", "status": "in_progress"}, {"content": "Check pod status and Blender state", "status": "pending"}, {"content": "Run baseline harness, capture evidence", "status": "pending"}, {"content": "Test suspects one by one", "status": "pending"}, {"content": "Write recipe and results rows", "status": "pending"}], "scope": "first_task"}`
<details><summary>tool result</summary>

```
Plan shown (5 steps).
```
</details>

- tool `Read`: `{"file_path": "/Users/nick/.claude/skills/live-blender/SKILL.md"}`
<details><summary>tool result</summary>

```
1	---
2	name: live-blender
3	description: A real, open Blender with a screen on the RunPod workbench pod, worked three ways without writing code - Claude through the Blender MCP connector, a real mouse (xdotool strokes for sculpt, grab, comb, add hair), and PlotPointe's Animate page (Blender in the browser, buttons, chat). Use whenever Blender work needs to be seen or done by hand, for brushes that only work with a mouse, when Nick says "live Blender", "open Blender", "show me in Blender", "use the mouse", or for PlotPointe's live Blender page. Blender never runs on the Mac.
4	argument-hint: [what to do in the live Blender]
5	---
6	
7	# Live Blender
8	
9	Built 12-14 Nov 2026: PlotPointe's page (12-13 Nov) and the mom hair chat's mouse work (14 Nov). Memory
10	`blender-live-on-pod.md` holds the measured details; `plotpointe.md` holds the page's history.
11	
12	## Before anything
13	- It costs money: workbench pods cost $0.59 to $1.19 an hour (rates in the Mac ledger, 15 Nov). Say the cost and get Nick's "go" before `workbench up`.
14	  The monthly spend cap was used up on 15 Nov (-$6.52): only Nick raises it.
15	- Blender never runs on the Mac (8 GB). The pod is started with `~/Desktop/render-desk/bin/workbench up`
16	  (from the box, hold `flock /tmp/aow-wb-up.lock` around status + up: two runs once rented two pods).
17	- Idle stop: `pod-guard.timer` on the 3D System box terminates a workbench pod 10 min after the last command when
18	  it is not busy (Nick, 15 Nov: "after 10 idle minutes please shut the pod down"). Commands that count: every
19	  workbench run/push/pull and every connector command (start_live.py below). Off: `POD_GUARD=0` in /etc/pod-guard.env.
20	- Before ending any turn with the pod up: stop it (`workbench down`) or tell Nick in one line it is billing.
21	- Write every setting that worked into a script file before the turn ends: live-only changes die with the pod.
22	
23	## Files (all in this skill's `scripts/`, saved 15 Nov from the mom hair chat)
24	| file | runs where | what it does |
25	|---|---|---|
26	| `blender_mcp.py` | pod, inside Blender | the MCP for Blender add-on (protocol 16, from the uvx package `mcp-for-blender`) |
27	| `start_live.py` | pod, `--python` | installs and enables the add-on, starts its server on 127.0.0.1:9876, restarts it if it stops, and writes ~/.wb_last_use on every connector command |
28	| `live_tools.py` | pod, `exec(open(...).read())` | `snap(path)` viewport picture drawn off-screen, `shoot(tag)` four Cycles GPU head views to /root/live_snaps, `view_on(obj)`, `screen_xy(point)` screen pixel for the mouse, `ctx()`. Kept in `bpy.app.driver_namespace` (the connector's namespace does not persist) |
29	| `drag.sh` | Mac | `drag.sh "x1,y1 x2,y2 ..." [stroke2 ...]`: real mouse strokes in the pod's screen with xdotool, through `workbench run`. `STEP=` sets the pause between points |
30	| `sim.py` | pod | steps a simulation from frame A to B, stops if Blender passes 12 GB |
31	| `pullcmp.sh`, `compare.py`, `flowmap.py`, `rebuild_live.py`, `live_dyn.py` | mom hair project | pull the four head views and put the reference above ours; hair flow map; rebuild mom and her particle hair. Their paths still point at the mom hair chat's scratchpad (`/private/tmp/.../f3d1b7da.../scratchpad`): they break when that folder is cleared |
32	
33	## Start a live Blender (the connector + mouse way)
34	1. `workbench up`, then `workbench push ~/.claude/skills/live-blender/scripts` (same absolute path on the pod).
35	2. For the mouse and a GPU viewport: on the pod `apt-get install -y xdotool` and VirtualGL 3.1.5 (.deb from the
36	   VirtualGL GitHub releases).
37	3. Start in the background (the `workbench run` stays open while Blender is open):
38	   `workbench run "cd ~/.claude/skills/live-blender/scripts && xvfb-run --auto-servernum -s '-screen 0 1920x1080x24 +extension GLX' /opt/VirtualGL/bin/vglrun -d egl \$BLENDER --python start_live.py"`
39	   Without VirtualGL: `LIBGL_ALWAYS_SOFTWARE=1 xvfb-run . ...[cut]
```
</details>

- tool `Bash`: `{"command": "ls /Users/nick/.claude/projects/-Users-nick-Desktop-mom-character/memory/ ; cat /Users/nick/.claude/projects/-Users-nick-Desktop-mom-character/memory/blender-live-on-pod.md; tail -6 /Users/nick/Desktop/mom-character/results.tsv; ls \"/Users/nick/Library/Application Support/Claude/side-session-notes/local_3bd59381-07cd-47ec-884c-8460247f8b39\"; ls /Users/nick/Desktop/mom-character/live", "description": "Read memory, results tail, notes, live dir"}`
- tool `Bash`: `{"command": "cd /Users/nick/Desktop/mom-character/scripts; cat cursor_harness.py harness.sh", "description": "Read harness scripts"}`
<details><summary>tool result</summary>

```
"""CURSOR HARNESS (15 Nov 2026): test every Curves Sculpt brush by REAL mouse on a clean object, far from the hair scene.
MODE="build"  : (re)create TestSphere + TestHair (300 straight strands) at x=6 m, front orthographic view.
MODE="prep"   : BRUSH="Comb" ... enter Curves Sculpt, activate the brush, print the screen stroke (CLICK/STROKE json) across the strand tips.
MODE="measure": leave the mode, report how many points moved and by how much."""
import bpy, json, numpy as np
from mathutils import Vector, Euler
from bpy_extras.view3d_utils import location_3d_to_region_2d
W = bpy.context.window_manager.windows[0]; sc = W.scene
A = next(a for a in W.screen.areas if a.type == "VIEW_3D"); R = next(r for r in A.regions if r.type == "WINDOW"); SP = A.spaces.active
MODE = globals().get("MODE", "build"); NS = bpy.app.driver_namespace
def view_front():
    SP.shading.type = "SOLID"; rv = SP.region_3d; rv.view_perspective = "ORTHO"
    rv.view_rotation = Euler((1.5707963, 0, 0)).to_quaternion(); rv.view_location = Vector((6.0, 0.0, 0.25)); rv.view_distance = 1.6
    for ar in W.screen.areas: ar.tag_redraw()
if MODE == "build":
    for n in ("TestHair", "TestSphere"):
        o = bpy.data.objects.get(n)
        if o: bpy.data.objects.remove(o, do_unlink=True)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(6.0, 0.0, 0.0)); sph = bpy.context.active_object; sph.name = "TestSphere"
    rng = np.random.default_rng(1); N = 300; per = 10; pts = []
    for _ in range(N):
        v = rng.normal(size=3); v[2] = abs(v[2]) + 0.3; v /= np.linalg.norm(v); root = np.array([6.0, 0, 0]) + v * 0.12
        pts += [root + v * 0.30 * t / (per - 1) for t in range(per)]
    cd = bpy.data.hair_curves.new("TestHair"); cd.add_curves([per] * N)
    cd.attributes["position"].data.foreach_set("vector", np.array(pts, np.float32).reshape(-1)); cd.surface = sph; cd.surface_uv_map = sph.data.uv_layers[0].name
    hair = bpy.data.objects.new("TestHair", cd); sc.collection.objects.link(hair); hair.parent = sph
    view_front(); print("built", N, "strands")
elif MODE == "prep":
    hair = bpy.data.objects["TestHair"]; view_front()
    with bpy.context.temp_override(window=W, area=A, region=R, active_object=hair, object=hair):
        for o in sc.objects: o.select_set(False)
        hair.select_set(True); bpy.context.view_layer.objects.active = hair
        if hair.mode != "SCULPT_CURVES": bpy.ops.object.mode_set(mode="SCULPT_CURVES")
        r = bpy.ops.brush.asset_activate(asset_library_type='ESSENTIALS', relative_asset_identifier=f'brushes/essentials_brushes-curve_sculpt.blend/Brush/{BRUSH}')
    cs = bpy.context.tool_settings.curves_sculpt; cs.brush.size = 120; cs.unified_paint_settings.size = 120
    n = len(hair.data.points); P = np.zeros(n * 3, np.float32); hair.data.attributes["position"].data.foreach_get("vector", P); NS["h_before"] = P.copy(); NS["h_ncurves"] = len(hair.data.curves)
    tip = Vector((6.0, -0.12 if globals().get('ON_SURFACE') else 0.0, 0.08 if globals().get('ON_SURFACE') else 0.30)); a = location_3d_to_region_2d(R, SP.region_3d, tip); b = location_3d_to_region_2d(R, SP.region_3d, tip + Vector((0.18, 0, 0)))
    st = [[round(R.x + a.x), round(W.height - (R.y + a.y))], [round(R.x + b.x), round(W.height - (R.y + b.y))]]
    print("PREP", BRUSH, "activate", r, "brush", cs.brush.name, "tool", getattr(cs.brush, "curves_sculpt_tool", "?"), "size", cs.brush.size, "strength", round(cs.brush.strength, 2), "falloff", cs.brush.falloff_shape, "mode", hair.mode)
    print("STROKE", json.dumps(st))
else:
    hair = bpy.data.objects["TestHair"]
    with bpy.context.temp_override(window=W, area=A, region=R, active_object=hair, object=hair):
        bpy.ops.object.mode_set(mode="OBJECT")
    n = len(hair.data.points); P = np.zeros(n * 3, np.float32); hair.data.attributes["position"].data.foreach_get("vector", P)
    d = np.linalg.norm((P - NS["h_before"]).reshape(-1, 3), axis=1)
    print("RESULT", BRUSH, "points moved >0.5mm:", int((d > 0.0005).s ...[cut]
```
</details>

<details><summary>tool result</summary>

```
cat: /Users/nick/.claude/projects/-Users-nick-Desktop-mom-character/memory/blender-live-on-pod.md: No such file or directory
2026-11-15	BUN COLOUR (Nick: 'black because of lighting? check other frames'): measured in 2 more frames of the clip: lit t=73 s bun L 41.7 RGB(134,88,61) vs neighbouring hair L 42.3 RGB(143,86,43); dark t=16 s bun L 11.3 vs hair 11.3. The bun is the SAME colour as her hair; it only looks black in shadow. Ours was black in bright light (neutral, slightly blue). Fix: bun direct colour = top hair colour. Also Direct coloring (parametrization COLOR + Hair Info Intercept mix) replaces melanin for all strand groups; transparent bounces 8 -> 32	after: Lab side top/mid/low ours (32.2,6.0,15.7)/(22.4,6.6,9.7)/(34.0,7.2,12.5) vs ref (37.3,13.8,24.6)/(19.9,10.0,15.2)/(20.7,7.9,12.2): lightness near, CHROMA still half of hers (a,b), lower third too light	partly
2026-11-15	MATCHED-CAMERA FIT LOOP (Nick: 'you can clearly see the difference, why dont you fix it'; 'did you read all of the research again'): re-read sources-checklist + article + manual BEFORE the fix. Rules applied: article 'puffing at roots and falling with subtle curves, avoiding outward sticking' (volume exp(-((s-0.18)/0.20)^2) then falls close), article layers (mid = silhouette, top thin), manual Shrinkwrap Hair Curves (offset + smoothing steps -> 3 smoothing iterations, roots locked), manual Blend Hair Curves (each strand 55% itself + 45% mean of 6 nearest neighbours' offsets). Also: face-framing pieces removed, th<78 roots fully swept back (w=1), dome lift cut (0.005/0.007), hair hang defaults gap -0.02, back tuck -0.035 for th>100, zend +0.035 (shorter) with -0.030 longer at the back, bangs end at the cheekbone (ze 1.560), temple roots down to z 1.585 for th 48-72	IoU vs her side silhouette 0.597 -> 0.725 (pieces/sweep/dome) -> 0.735 (gap) -> 0.752 (sources: puff, blend, smooth) -> 0.776 (bangs/temple/back). Surplus 60k -> 21k px. Plateau: more tuck lowers IoU (ref_only up). Remaining error mostly my hand-drawn reference polygon, strand fuzz at the edge, and bun/back crescents	worked, plateau 0.776
2026-11-15	CURSOR TEST (Nick: 'maybe do it with the cursor instead of code'): research says read results after leaving the mode; tested Comb by real mouse on 3 layers (Hair2_Outer_Low 434k points, Hair2_Outer_Bun 34k; strokes computed from strands outside her silhouette, 25-31 points each, slow steps, wait 8 s, read AFTER leaving the mode): 0 of 434400 / 34560 points moved. Control: Add brush by real mouse on the same object created 6 curves from 2 clicks (mouse path works)	Comb specifically does not move strands on this build/setup; cause unknown (not the read-in-mode mistake, not the mouse path). Cursor route blocked at Comb	didn't work
2026-11-15	TOOL 1 OUTLINE (scripts/outline_auto.py + view_masks.py; Nick: 'build a detailed outline tool... a system which doesnt need me'): hair mask of any reference frame with no hand-drawn polygon. Seeds from OUR render at the matched camera: core of our hair = sure hair, far from it = sure not, our body below the eyes where our hair is absent = sure not hair (the forehead excluded because her bangs cover it), letterbox + caption = not hair; GrabCut decides the band by colour. Params per view (band 40-95 px)	side: good (S-curve to the shoulder, ear/neck/face excluded; leak of dark wall at top-left because bun and wall are the same brown). q34: forehead + bangs now included; lower hair behind the ear missed (our hair barely reaches there, so no seed). back: unusable (camera is a guess). Limit: only as good as the matched camera. Saved refs/outline_{side,q34,front}.npy; fit_side.py now scores against it	worked (side), partly (q34), blocked (back)
2026-11-15	Score against the accurate outline: IoU 0.805 (polygon said 0.776), ours_only 11.5k, ref_only 12.4k: balanced. Largest remaining error = hair she has that we lack at the FRONT (bangs/hairline come further forward), red crescent at the back of the head, mixed hem	n ...[cut]
```
</details>

- tool `Bash`: `{"command": "cd /Users/nick/Desktop/mom-character/live; cat drag.sh; echo ----; cat bcall.py | head -40; ls /Users/nick/.claude/projects/*/memory/blender-live-on-pod.md 2>/dev/null; ls ~/.claude/skills/live-blender/", "description": "Read drag.sh, bcall.py, find memory"}`
- tool `Bash`: `{"command": "ssh -o BatchMode=yes -o ConnectTimeout=15 nick@37.27.148.115 '~/Desktop/render-desk/bin/workbench status 2>&1 | tail -15; pgrep -c -f vglrun; cat ~/.local/share/render-desk/workbench.json 2>/dev/null | head -20'", "description": "Check pod status on the box"}`
<details><summary>tool result</summary>

```
#!/bin/bash
# usage: drag.sh "x1,y1 x2,y2 ..." [more strokes...]   each argument is one stroke: button held from first to last point
cmd='read D A < <(ps -eo args | awk "\$1==\"Xvfb\"{print \$2, \$NF}" | tail -1); export DISPLAY=$D XAUTHORITY=$A; '   # no window activate here: the first press after one is swallowed as a focus click
STEP=${STEP:-0.05}
for stroke in "$@"; do
  first=1
  for p in $stroke; do
    x=${p%,*}; y=${p#*,}
    if [ $first = 1 ]; then cmd+="xdotool mousemove $x $y; sleep 0.15; xdotool mousedown 1; "; first=0
    else cmd+="xdotool mousemove $x $y; sleep $STEP; "; fi
  done
  cmd+="xdotool mouseup 1; sleep 0.25; "
done
cd ~/Desktop/render-desk && ./bin/workbench run "$cmd echo strokes done"
----
"""Send Python to the live pod Blender through the box tunnel (127.0.0.1:9876), print what it prints.
Usage (on the box): python3 live/bcall.py 'code'   or   python3 live/bcall.py -f file.py   [--timeout 600]
Same socket the MCP connector uses; for scripted steps when no Claude session is needed."""
import json, socket, sys
args = sys.argv[1:]
timeout = 600
if "--timeout" in args:
    i = args.index("--timeout"); timeout = float(args[i + 1]); del args[i:i + 2]
code = open(args[1]).read() if args[0] == "-f" else args[0]
s = socket.create_connection(("127.0.0.1", 9876), timeout=timeout)
s.sendall(json.dumps({"type": "execute_code", "params": {"code": code}}).encode())
buf = b""
while True:
    chunk = s.recv(65536)
    if not chunk:
        break
    buf += chunk
    try:
        reply = json.loads(buf.decode()); break
    except ValueError:
        continue
s.close()
r = reply.get("result", reply)
print(r.get("result", r) if isinstance(r, dict) else r)
sys.exit(0 if reply.get("status") == "success" else 1)
/Users/nick/.claude/projects/-Users-nick/memory/blender-live-on-pod.md
SKILL.md
scripts
```
</details>

<details><summary>tool result</summary>

```
WB up: pod mapjr8ggbd7ssg NVIDIA GeForce RTX 4090, 0.66 h so far ($0.59), idle 2 min
1
{
 "pod_id": "mapjr8ggbd7ssg",
 "gpu": "NVIDIA GeForce RTX 4090",
 "rate": 0.89,
 "started": 1794747010.647626,
 "last_used": 1794749266.6892877,
 "target": [
  "213.173.107.230",
  18441,
  "root"
 ],
 "blender": "/workspace/blender/5.2.2/blender"
}
```
</details>

- tool `Bash`: `{"command": "cat /Users/nick/.claude/projects/-Users-nick/memory/blender-live-on-pod.md", "description": "Read the memory file"}`
<details><summary>tool result</summary>

```
---
name: blender-live-on-pod
description: "How to run a live GUI Blender on the workbench pod for the Blender MCP connector, and which hand tools (brushes) work from code"
metadata:
  node_type: memory
  type: reference
  originSessionId: f3d1b7da-7894-44f4-be87-03c3b071e609
  modified: 2026-11-15T07:44:46.050Z
---

Live Blender for the MCP connector runs on the workbench pod, never on the Mac (see [[machine-and-render-workflow]]). Set up and proven 2026-11-14:
- Kit: MCP for Blender add-on (bundled `addon.py` from the uvx package `mcp-for-blender`, protocol 16) plus a start script that copies it to the user add-ons folder, appends that folder to `sys.path`, enables it, starts the server on 127.0.0.1:9876 and runs a watchdog timer that restarts the server object if it stops.
- Launch: `workbench run "... LIBGL_ALWAYS_SOFTWARE=1 xvfb-run --auto-servernum -s '-screen 0 1920x1080x24 +extension GLX' $BLENDER --python start_live.py"` in the background (keeps the pod from idling off). Use `--auto-servernum`, not `-a`, and don't print the bare word "blender ": the gate hook's rule 14 reads `-a` + blender as a Mac animation render.
- Tunnel: `ssh -f -N -L 127.0.0.1:9876:127.0.0.1:9876` to the pod target in `~/.local/share/render-desk/workbench.json`. The connector's `look` fails remotely (it saves the screenshot on the Mac side); instead draw with `gpu.types.GPUOffScreen.draw_view3d` or render with Cycles OptiX on the pod and `workbench pull` the PNGs.
- Never call `bpy.ops.wm.read_factory_settings` (blender-funnel `stage.new_scene`) in a live session: it unloads the add-on and crashed Blender. Empty the current scene instead. `bpy.context.window` is None inside connector calls: use `window_manager.windows[0]`.
- Brushes from code WORK in a GUI Blender: sculpt `bpy.ops.sculpt.brush_stroke(stroke=[...])` (Draw raised a sphere ~10 cm) and particle `bpy.ops.particle.brush_edit` Comb (combed hair visibly). Rules: enter the mode in one call, stroke in the next (the viewport must redraw between), give `mouse`/`mouse_event` in region pixels, and read the result only after leaving the mode (in sculpt mode the mesh data still shows the old shape; that misled two earlier tests into "0 moved"). Curves sculpt brushes (`sculpt_curves.brush_stroke`, Add/Comb on new hair) return PASS_THROUGH from code: they need real mouse input.
- Real mouse input WORKS (Nick: "i did it before and it worked"): `apt-get install xdotool`, then `DISPLAY=:N XAUTHORITY=/tmp/xvfb-run.XXXX/Xauthority xdotool mousemove X Y mousedown 1 ... mousemove ... mouseup 1` (find N and the auth file in `ps` for Xvfb). Screen coords from Blender: X = region.x + mx, Y = window.height - (region.y + my). Proven: Add brush grew 1,160 hairs from 3 drags, Comb moved 516 tips ~6 cm down from 3 drags.
- Mesh SCULPT with the mouse WORKS (Draw, Grab, Smooth proven 2026-11-14) with the viewport drawn on the RTX 4090: install VirtualGL 3.1.5 (.deb from the VirtualGL GitHub releases) and launch `xvfb-run ... /opt/VirtualGL/bin/vglrun -d egl $BLENDER ...` without LIBGL_ALWAYS_SOFTWARE (the container blocks /dev/dri, `-d egl` uses NVIDIA's EGL device; egl1 is llvmpipe). Gotcha that looked like "only one dab": the first mouse press after `xdotool windowactivate` is swallowed as a focus click, so never activate the window before each batch of strokes. Grab by scripted stroke has no effect; use the mouse for Grab.
- **COST INCIDENT 14-15 Nov 2026: $14.29 for one pod, ~13 h of it idle.** The live Blender runs inside `workbench run`, whose keepalive marks the pod "in use" every 5 min, so the 10-minute idle stop can never fire while a live session is open. The backstop (watchdog on the Mac) fired at 20:22 but the Mac was offline: 5 terminate attempts failed, it logged WB_ALERT and gave up; the pod ran until 09:44 next day. Rule: never leave a live session open at the end of a turn; before ending any turn with the pod up, either stop it or tell Nick it is billing. Proposed fix (awaiting Nick): an idle sto ...[cut]
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"\nimport bpy\nW=bpy.context.window_manager.windows[0]\nprint(bpy.app.version_string, W.width, W.height, [ (a.type,a.x,a.y,a.width,a.height) for a in W.screen.areas])\nprint([ (o.name,o.mode) for o in bpy.data.objects if o.mode!=\\\"OBJECT\\\"], bpy.context.view_layer.objects.active)\nprint([o.name for o in bpy.data.objects if o.name.startswith(\\\"Test\\\")])\nimport gpu; print(gpu.platform.renderer_get(), gpu.platform.backend_type_get())\nprint(bpy.app.binary_path)\n\" --timeout 30 2>&1 | tail -10; ps -eo pid,args | grep -E \"Xvfb|vglrun|x11vnc|xdotool\" | grep -v grep | head'", "description": "Query live Blender state and processes on the box"}`
<details><summary>tool result</summary>

```
5.2.2 LTS 1920 1080 [('PROPERTIES', 1579, 24, 339, 837), ('OUTLINER', 1579, 864, 339, 189), ('DOPESHEET_EDITOR', 2, 24, 1574, 74), ('VIEW_3D', 2, 101, 1574, 952)]
[] <bpy_struct, Object("TestHair") at 0x7d040ad1d608>
['TestHair', 'TestSphere']
NVIDIA GeForce RTX 4090/PCIe/SSE2 OPENGL
/workspace/blender/5.2.2/blender
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"ps -eo pid,args | grep -E \\\"Xvfb|vglrun|x11vnc|websockify|xdotool|wm|openbox\\\" | grep -v grep | cut -c1-220; xdotool version; which xev xinput xdotool xte wmctrl 2>&1; echo \\$DISPLAY; nvidia-smi --query-gpu=utilization.gpu --format=csv\" 2>&1 | tail -30'", "description": "Inspect pod X display, VNC, tools"}`
<details><summary>tool result</summary>

```
   2691 /bin/sh /usr/bin/xvfb-run --auto-servernum -s -screen 0 1920x1080x24 +extension GLX /opt/VirtualGL/bin/vglrun -d egl /workspace/blender/5.2.2/blender --python start_live.py
   2705 Xvfb :99 -screen 0 1920x1080x24 +extension GLX -nolisten tcp -auth /tmp/xvfb-run.EUJfWu/Xauthority
   4324 x11vnc -display :99 -auth /tmp/xvfb-run.EUJfWu/Xauthority -localhost -nopw -forever -shared -noxdamage -rfbport 5901
   4326 /usr/bin/python3 /usr/bin/websockify --web /usr/share/novnc 127.0.0.1:6080 127.0.0.1:5901
   6030 /usr/bin/python3 /usr/bin/websockify --web /usr/share/novnc 127.0.0.1:6080 127.0.0.1:5901
Error: Can't open display: (null)
Failed creating new xdo instance
/usr/bin/xdotool

utilization.gpu [%]
0 %
```
</details>


### CLAUDE 2026-11-15T13:30

Pod is up and Blender 5.2.2 is live on the GPU display. Next I'm putting a pass-through event logger inside Blender, so I can see whether motion events arrive while the button is held.

- tool `Bash`: `{"command": "mkdir -p /Users/nick/Desktop/mom-character/scripts && cat > /Users/nick/Desktop/mom-character/scripts/cursor_evlog.py <<'EOF'\n\"\"\"Pass-through event logger (cursor investigation, 15 Nov 2026). MODE=\"start\" installs a modal operator that logs every event\n(type, value, x, y, time) to bpy.app.driver_namespace['evlog'] and passes it on; MODE=\"dump\" prints a summary; MODE=\"stop\" ends it.\"\"\"\nimport bpy, time\nNS = bpy.app.driver_namespace\nMODE = globals().get(\"MODE\", \"dump\")\nclass WM_OT_evlog(bpy.types.Operator):\n    bl_idname = \"wm.evlog_cursor\"; bl_label = \"evlog\"\n    def modal(self, context, event):\n        if NS.get(\"evlog_stop\"):\n            return {\"CANCELLED\"}\n        NS.setdefault(\"evlog\", []).append((round(time.time(), 3), event.type, event.value, event.mouse_x, event.mouse_y, event.is_repeat))\n        return {\"PASS_THROUGH\"}\n    def invoke(self, context, event):\n        context.window_manager.modal_handler_add(self); return {\"RUNNING_MODAL\"}\nif MODE == \"start\":\n    try: bpy.utils.register_class(WM_OT_evlog)\n    except Exception as e: print(\"reg\", e)\n    NS[\"evlog_stop\"] = False; NS[\"evlog\"] = []\n    W = bpy.context.window_manager.windows[0]; A = next(a for a in W.screen.areas if a.type == \"VIEW_3D\"); R = next(r for r in A.regions if r.type == \"WINDOW\")\n    with bpy.context.temp_override(window=W, area=A, region=R):\n        print(\"start\", bpy.ops.wm.evlog_cursor(\"INVOKE_DEFAULT\"))\nelif MODE == \"stop\":\n    NS[\"evlog_stop\"] = True; print(\"stop requested\")\nelse:\n    L = NS.get(\"evlog\", []); print(\"events\", len(L))\n    from collections import Counter\n    print(Counter((e[1], e[2]) for e in L).most_common(12))\n    print(L[:6], L[-6:])\nEOF\ncd /Users/nick/Desktop/mom-character && scp -q -o BatchMode=yes scripts/cursor_evlog.py nick@37.27.148.115:Desktop/mom-character/scripts/ && ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && ~/Desktop/render-desk/bin/workbench push ~/Desktop/mom-character >/dev/null 2>&1; python3 live/bcall.py \"MODE=\\\"start\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_evlog.py\\\").read())\" --timeout 30 2>&1 | tail -5'", "description": "Install event logger in live Blender"}`
<details><summary>tool result</summary>

```
start {'RUNNING_MODAL'}
```
</details>

- tool `Bash`: `{"command": "bash scripts/harness.sh \"Comb\" 2>&1 | tail -5; ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"MODE=\\\"dump\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_evlog.py\\\").read())\" --timeout 30 2>&1 | tail -6'", "description": "Run Comb harness with event logging, dump events", "timeout": 300000}`
<details><summary>tool result</summary>

```
PREP Comb activate {'FINISHED'} brush Comb tool ? size 120 strength 1.0 falloff PROJECTED mode SCULPT_CURVES
RESULT Comb points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
events 68
[(('MOUSEMOVE', 'NOTHING'), 33), (('LEFTMOUSE', 'PRESS'), 31), (('NONE', 'NOTHING'), 4)]
[(1794749451.641, 'NONE', 'NOTHING', 171, 180, False), (1794749451.642, 'NONE', 'NOTHING', 171, 180, False), (1794749451.663, 'MOUSEMOVE', 'NOTHING', 171, 180, False), (1794749453.862, 'MOUSEMOVE', 'NOTHING', 789, 460, False), (1794749454.016, 'LEFTMOUSE', 'PRESS', 789, 460, False), (1794749454.271, 'MOUSEMOVE', 'NOTHING', 793, 460, False)] [(1794749465.858, 'LEFTMOUSE', 'PRESS', 907, 460, False), (1794749466.111, 'MOUSEMOVE', 'NOTHING', 912, 460, False), (1794749466.266, 'LEFTMOUSE', 'PRESS', 912, 460, False), (1794749474.588, 'NONE', 'NOTHING', 912, 460, False), (1794749474.604, 'MOUSEMOVE', 'NOTHING', 912, 460, False), (1794749474.604, 'NONE', 'NOTHING', 912, 460, False)]
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"\nimport bpy\nL=bpy.app.driver_namespace[\\\"evlog\\\"]\nt0=L[0][0]\nfor e in L: print(round(e[0]-t0,3), e[1], e[2], e[3], e[4])\n\" --timeout 30 2>&1 | head -80'", "description": "Dump full event log with times"}`
<details><summary>tool result</summary>

```
0.0 NONE NOTHING 171 180
0.001 NONE NOTHING 171 180
0.022 MOUSEMOVE NOTHING 171 180
2.221 MOUSEMOVE NOTHING 789 460
2.375 LEFTMOUSE PRESS 789 460
2.63 MOUSEMOVE NOTHING 793 460
2.785 LEFTMOUSE PRESS 793 460
3.038 MOUSEMOVE NOTHING 797 460
3.193 LEFTMOUSE PRESS 797 460
3.45 MOUSEMOVE NOTHING 801 460
3.6 LEFTMOUSE PRESS 801 460
3.856 MOUSEMOVE NOTHING 805 460
4.011 LEFTMOUSE PRESS 805 460
4.263 MOUSEMOVE NOTHING 809 460
4.418 LEFTMOUSE PRESS 809 460
4.675 MOUSEMOVE NOTHING 813 460
4.825 LEFTMOUSE PRESS 813 460
5.079 MOUSEMOVE NOTHING 817 460
5.234 LEFTMOUSE PRESS 817 460
5.49 MOUSEMOVE NOTHING 821 460
5.645 LEFTMOUSE PRESS 821 460
5.897 MOUSEMOVE NOTHING 825 460
6.051 LEFTMOUSE PRESS 825 460
6.31 MOUSEMOVE NOTHING 830 460
6.459 LEFTMOUSE PRESS 830 460
6.718 MOUSEMOVE NOTHING 834 460
6.867 LEFTMOUSE PRESS 834 460
7.126 MOUSEMOVE NOTHING 838 460
7.275 LEFTMOUSE PRESS 838 460
7.533 MOUSEMOVE NOTHING 842 460
7.688 LEFTMOUSE PRESS 842 460
7.942 MOUSEMOVE NOTHING 846 460
8.097 LEFTMOUSE PRESS 846 460
8.349 MOUSEMOVE NOTHING 850 460
8.503 LEFTMOUSE PRESS 850 460
8.755 MOUSEMOVE NOTHING 854 460
8.909 LEFTMOUSE PRESS 854 460
9.162 MOUSEMOVE NOTHING 858 460
9.317 LEFTMOUSE PRESS 858 460
9.573 MOUSEMOVE NOTHING 862 460
9.728 LEFTMOUSE PRESS 862 460
9.98 MOUSEMOVE NOTHING 866 460
10.134 LEFTMOUSE PRESS 866 460
10.387 MOUSEMOVE NOTHING 871 460
10.542 LEFTMOUSE PRESS 871 460
10.798 MOUSEMOVE NOTHING 875 460
10.952 LEFTMOUSE PRESS 875 460
11.205 MOUSEMOVE NOTHING 879 460
11.359 LEFTMOUSE PRESS 879 460
11.614 MOUSEMOVE NOTHING 883 460
11.769 LEFTMOUSE PRESS 883 460
12.022 MOUSEMOVE NOTHING 887 460
12.176 LEFTMOUSE PRESS 887 460
12.428 MOUSEMOVE NOTHING 891 460
12.583 LEFTMOUSE PRESS 891 460
12.837 MOUSEMOVE NOTHING 895 460
12.991 LEFTMOUSE PRESS 895 460
13.245 MOUSEMOVE NOTHING 899 460
13.4 LEFTMOUSE PRESS 899 460
13.657 MOUSEMOVE NOTHING 903 460
13.807 LEFTMOUSE PRESS 903 460
14.062 MOUSEMOVE NOTHING 907 460
14.217 LEFTMOUSE PRESS 907 460
14.47 MOUSEMOVE NOTHING 912 460
14.625 LEFTMOUSE PRESS 912 460
22.947 NONE NOTHING 912 460
22.963 MOUSEMOVE NOTHING 912 460
22.963 NONE NOTHING 912 460
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'diff ~/Desktop/mom-character/live/drag.sh /dev/stdin <<< \"\" | head -3; md5sum ~/Desktop/mom-character/live/drag.sh'; md5 live/drag.sh\npython3 - <<'EOF'\np=\"scripts/harness.sh\"\ns=open(p).read()\ns=s.replace(\"\"\"print('\\\\\"'+' '.join('%d,%d'%(a[0]+(b[0]-a[0])*t/30,a[1]+(b[1]-a[1])*t/30) for t in range(31))+'\\\\\"')\")\"\"\",\"\"\"print(' '.join('%d,%d'%(a[0]+(b[0]-a[0])*t/30,a[1]+(b[1]-a[1])*t/30) for t in range(31)))\")\"\"\")\ns=s.replace(\"\"\"STEP=0.06 eval live/drag.sh $ARGS >/dev/null 2>&1; sleep 4\\\"\"\"\",\"\"\"STEP=0.06 live/drag.sh '$ARGS' >/dev/null 2>&1; sleep 4\\\"\"\"\")\nopen(p,\"w\").write(s)\nEOF\ngrep -n \"ARGS\" scripts/harness.sh", "description": "Fix quoting bug in harness.sh"}`
<details><summary>tool result</summary>

```
1,14c1
< #!/bin/bash
< # usage: drag.sh "x1,y1 x2,y2 ..." [more strokes...]   each argument is one stroke: button held from first to last point
97d43f0cfe017a8eae1faf1d179a7ade  /Users/nick/Desktop/mom-character/live/drag.sh
MD5 (live/drag.sh) = 97d43f0cfe017a8eae1faf1d179a7ade
11:ARGS=$(python3 -I -c "
15:ssh -o BatchMode=yes nick@37.27.148.115 "cd ~/Desktop/mom-character && STEP=0.06 live/drag.sh '$ARGS' >/dev/null 2>&1; sleep 4"
```
</details>


### CLAUDE 2026-11-15T13:31

Box and Mac `drag.sh` are identical, so `drag.sh` is fine and the bug was only the harness quoting. Rerunning Comb with the logger still on.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"bpy=__import__(\\\"bpy\\\"); bpy.app.driver_namespace[\\\"evlog\\\"]=[]\" --timeout 20' ; bash scripts/harness.sh \"Comb\" 2>&1 | tail -4; ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"MODE=\\\"dump\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_evlog.py\\\").read())\" --timeout 30 2>&1 | tail -4 | cut -c1-600'", "description": "Rerun Comb harness with fixed stroke", "timeout": 300000}`
<details><summary>tool result</summary>

```
PREP Comb activate {'FINISHED'} brush Comb tool ? size 120 strength 1.0 falloff PROJECTED mode SCULPT_CURVES
RESULT Comb points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
events 8
[(('NONE', 'NOTHING'), 4), (('MOUSEMOVE', 'NOTHING'), 3), (('LEFTMOUSE', 'PRESS'), 1)]
[(1794749522.137, 'NONE', 'NOTHING', 912, 460, False), (1794749522.137, 'NONE', 'NOTHING', 912, 460, False), (1794749522.158, 'MOUSEMOVE', 'NOTHING', 912, 460, False), (1794749524.388, 'MOUSEMOVE', 'NOTHING', 789, 460, False), (1794749524.539, 'LEFTMOUSE', 'PRESS', 789, 460, False), (1794749546.357, 'NONE', 'NOTHING', 912, 460, False)] [(1794749522.158, 'MOUSEMOVE', 'NOTHING', 912, 460, False), (1794749524.388, 'MOUSEMOVE', 'NOTHING', 789, 460, False), (1794749524.539, 'LEFTMOUSE', 'PRESS', 789, 460, False), (1794749546.357, 'NONE', 'NOTHING', 912, 460, False), (1794749546.357, 'NONE', 'NOTHIN
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"which import scrot xwd convert xdpyinfo xinput ffmpeg python3; python3 -c \\\"import PIL; print(PIL.__version__)\\\" 2>&1\" 2>&1 | tail -10'", "description": "Check screenshot tools on pod"}`
<details><summary>tool result</summary>

```
/usr/bin/ffmpeg
/usr/bin/python3
10.2.0
```
</details>

- tool `Bash`: `{"command": "cat > scripts/cursor_shot.sh <<'EOF'\n#!/bin/bash\n# usage (on the box): cursor_shot.sh \"x1,y1 x2,y2 ...\"  one held stroke; ffmpeg screen grabs mid-stroke (/root/live_snaps/cs_mid.png) and after release (cs_end.png). STEP=pause between points\ncmd='read D A < <(ps -eo args | awk \"\\$1==\\\"Xvfb\\\"{print \\$2, \\$NF}\" | tail -1); export DISPLAY=$D XAUTHORITY=$A; mkdir -p /root/live_snaps; '\nSTEP=${STEP:-0.06}\npts=($1); n=${#pts[@]}; mid=$((n*2/3))\ni=0\nfor p in \"${pts[@]}\"; do\n  x=${p%,*}; y=${p#*,}\n  if [ $i = 0 ]; then cmd+=\"xdotool mousemove $x $y; sleep 0.15; xdotool mousedown 1; \"\n  else cmd+=\"xdotool mousemove $x $y; sleep $STEP; \"; fi\n  if [ $i = $mid ]; then cmd+=\"ffmpeg -loglevel error -y -f x11grab -video_size 1920x1080 -i \\$DISPLAY -frames:v 1 /root/live_snaps/cs_mid.png; \"; fi\n  i=$((i+1))\ndone\ncmd+=\"xdotool mouseup 1; sleep 0.5; ffmpeg -loglevel error -y -f x11grab -video_size 1920x1080 -i \\$DISPLAY -frames:v 1 /root/live_snaps/cs_end.png; echo shots done\"\ncd ~/Desktop/render-desk && ./bin/workbench run \"$cmd\"\nEOF\nchmod +x scripts/cursor_shot.sh\nscp -q scripts/cursor_shot.sh nick@37.27.148.115:Desktop/mom-character/scripts/\nssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && ~/Desktop/render-desk/bin/workbench push ~/Desktop/mom-character >/dev/null 2>&1; python3 live/bcall.py \"MODE=\\\"prep\\\"\nBRUSH=\\\"Comb\\\"\nON_SURFACE=1\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_harness.py\\\").read())\" --timeout 60 2>&1 | tail -3'", "description": "Create screenshot-stroke script, prep Comb"}`
<details><summary>tool result</summary>

```
PREP Comb activate {'FINISHED'} brush Comb tool ? size 120 strength 1.0 falloff PROJECTED mode SCULPT_CURVES
STROKE [[789, 619], [912, 619]]
```
</details>

- tool `Bash`: `{"command": "P=$(python3 -I -c \"print(' '.join('%d,%d'%(789+(912-789)*t/30,619) for t in range(31)))\") && ssh -o BatchMode=yes nick@37.27.148.115 \"cd ~/Desktop/mom-character && STEP=0.1 scripts/cursor_shot.sh '$P' 2>&1 | tail -3; cd ~/Desktop/render-desk && ./bin/workbench pull /root/live_snaps /tmp/cs_snaps >/dev/null 2>&1; ls /tmp/cs_snaps | head\"; mkdir -p /tmp/cs && scp -q nick@37.27.148.115:/tmp/cs_snaps/cs_mid.png nick@37.27.148.115:/tmp/cs_snaps/cs_end.png /tmp/cs/ 2>&1; ls -la /tmp/cs", "description": "Run stroke with mid-stroke screenshots and fetch them", "timeout": 200000}`
<details><summary>tool result</summary>

```
shots done
live_snaps
scp: /tmp/cs_snaps/cs_mid.png: No such file or directory
scp: /tmp/cs_snaps/cs_end.png: No such file or directory
total 0
drwxr-xr-x@  2 nick  wheel    64 Nov 15 15:33 .
drwxrwxrwt  88 root  wheel  2816 Nov 15 15:33 ..
```
</details>

- tool `Bash`: `{"command": "S=/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad; mkdir -p $S; scp -q nick@37.27.148.115:/tmp/cs_snaps/live_snaps/cs_mid.png nick@37.27.148.115:/tmp/cs_snaps/live_snaps/cs_end.png $S/ && ls -la $S", "description": "Copy screenshots to scratchpad"}`
<details><summary>tool result</summary>

```
total 768
drwx------@ 4 nick  wheel     128 Nov 15 15:33 .
drwx------@ 4 nick  wheel     128 Nov 15 15:29 ..
-rw-r--r--@ 1 nick  wheel  195708 Nov 15 15:33 cs_end.png
-rw-r--r--@ 1 nick  wheel  195734 Nov 15 15:33 cs_mid.png
```
</details>

- tool `Read`: `{"file_path": "/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad/cs_mid.png"}`
<details><summary>tool result</summary>

```
[image]
```
</details>

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"scripts/cursor_harness.py\"\ns=open(p).read()\nold=\"root = np.array([6.0, 0, 0]) + v * 0.12\"\nassert old in s\ns=s.replace(old,\"root = v * 0.12  # LOCAL to the sphere: TestHair is parented to it, world = sphere (x=6) + local (the first version used world coords and put the strands at x=12, off screen)\")\nopen(p,\"w\").write(s)\nEOF\nscp -q scripts/cursor_harness.py nick@37.27.148.115:Desktop/mom-character/scripts/\nssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && ~/Desktop/render-desk/bin/workbench push ~/Desktop/mom-character >/dev/null 2>&1; python3 live/bcall.py \"\nimport bpy\nh=bpy.data.objects[\\\"TestHair\\\"]\nif h.mode!=\\\"OBJECT\\\":\n    W=bpy.context.window_manager.windows[0]; A=next(a for a in W.screen.areas if a.type==\\\"VIEW_3D\\\"); R=next(r for r in A.regions if r.type==\\\"WINDOW\\\")\n    with bpy.context.temp_override(window=W,area=A,region=R,active_object=h,object=h): bpy.ops.object.mode_set(mode=\\\"OBJECT\\\")\nMODE=\\\"build\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_harness.py\\\").read())\nprint(h.name, bpy.data.objects[\\\"TestHair\\\"].matrix_world.translation)\n\" --timeout 60 2>&1 | tail -3'", "description": "Fix strand coordinates and rebuild TestHair"}`
<details><summary>tool result</summary>

```
{'status': 'error', 'message': '{"exception_type": "ReferenceError", "message": "StructRNA of type Object has been removed", "traceback": "Traceback (most recent call last):\\n  File \\"/root/.config/blender/5.2/scripts/addons/blender_mcp.py\\", line 2431, in execute_code\\n    exec(code, namespace)\\n    ~~~~^^^^^^^^^^^^^^^^^\\n  File \\"<string>\\", line 9, in <module>\\nReferenceError: StructRNA of type Object has been removed\\n"}'}
```
</details>


### CLAUDE 2026-11-15T13:33

That error is only my print of the removed old object after the rebuild. Checking that the build itself went through, then running Comb.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"\nimport bpy, numpy as np\nh=bpy.data.objects[\\\"TestHair\\\"]; P=np.zeros(len(h.data.points)*3,np.float32); h.data.attributes[\\\"position\\\"].data.foreach_get(\\\"vector\\\",P)\nprint(len(h.data.curves), P.reshape(-1,3).mean(0), h.matrix_world.translation, h.parent.name, h.mode)\n\" --timeout 30 2>&1 | tail -3'; bash scripts/harness.sh \"Comb\" 2>&1 | tail -3", "description": "Verify build then run Comb harness", "timeout": 300000}`
<details><summary>tool result</summary>

```
300 [ 0.0048386  -0.00273578  0.1724593 ] <Vector (6.0000, 0.0000, 0.0000)> TestSphere OBJECT

PREP Comb activate {'FINISHED'} brush Comb tool ? size 120 strength 1.0 falloff PROJECTED mode SCULPT_CURVES
RESULT Comb points moved >0.5mm: 900 of 3000 | max cm 15.21 | curves 300 -> 300
```
</details>


### CLAUDE 2026-11-15T13:34

Comb moves 900 of 3,000 points, up to 15.2 cm. Running the other brushes the same way.

- tool `Bash`: `{"command": "for B in \"Pull Tips\" \"Smooth\" \"Puff\" \"Pinch\" \"Slide\" \"Delete\"; do echo \"== $B\"; bash scripts/harness.sh \"$B\" 2>&1 | tail -2; done", "description": "Run six more brushes through the harness", "timeout": 600000}`
<details><summary>tool result</summary>

```
== Pull Tips
PREP Pull Tips activate {'FINISHED'} brush Pull Tips tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Pull Tips points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Smooth
PREP Smooth activate {'FINISHED'} brush Smooth tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Smooth points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Puff
PREP Puff activate {'FINISHED'} brush Puff tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Puff points moved >0.5mm: 71 of 3000 | max cm 2.14 | curves 300 -> 300
== Pinch
PREP Pinch activate {'FINISHED'} brush Pinch tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Pinch points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Slide
PREP Slide activate {'FINISHED'} brush Slide tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Slide points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Delete
PREP Delete activate {'FINISHED'} brush Delete tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
```
</details>


### CLAUDE 2026-11-15T13:36

Comb now works. Puff moved 71 points, and Pull Tips, Smooth, Pinch and Slide moved 0. Delete printed no result line, so I'm checking whether Blender is still up and in what state.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"\nimport bpy\nh=bpy.data.objects.get(\\\"TestHair\\\")\nprint(h and (h.mode, len(h.data.curves), len(h.data.points)))\nprint(bpy.context.tool_settings.curves_sculpt.brush.name)\n\" --timeout 30 2>&1 | tail -4'; ssh nick@37.27.148.115 'pgrep -c -f vglrun'", "description": "Check Blender state after Delete run"}`
<details><summary>tool result</summary>

```
Exit code 1
('OBJECT', 284, 2840)
Delete

0
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"\nimport bpy\ncs=bpy.context.tool_settings.curves_sculpt\nfor name in (\\\"Pull Tips\\\",\\\"Puff\\\",\\\"Comb\\\"):\n    bpy.ops.brush.asset_activate(asset_library_type=\\\"ESSENTIALS\\\", relative_asset_identifier=f\\\"brushes/essentials_brushes-curve_sculpt.blend/Brush/{name}\\\") if bpy.context.object and bpy.context.object.mode==\\\"SCULPT_CURVES\\\" else None\nb=cs.brush\nprint(b.name)\nfor p in b.bl_rna.properties:\n    if p.identifier.startswith((\\\"curves\\\",\\\"use_\\\",\\\"falloff\\\",\\\"spacing\\\",\\\"strength\\\",\\\"size\\\",\\\"direction\\\",\\\"stroke\\\",\\\"smooth\\\",\\\"jitter\\\",\\\"curve\\\")) :\n        try: print(p.identifier, getattr(b,p.identifier))\n        except Exception as e: pass\nprint(cs.bl_rna.properties.keys())\n\" --timeout 30 2>&1 | tail -60'", "description": "Dump curves sculpt brush properties"}`
<details><summary>tool result</summary>

```
smooth_stroke_radius 75
smooth_stroke_factor 0.8999999761581421
strength 1.0
use_hardness_pressure False
use_flow_pressure False
use_wet_mix_pressure False
use_wet_persistence_pressure False
use_density_pressure False
use_color_as_displacement False
falloff_angle 0.0
use_original_normal False
use_original_plane False
use_scene_spacing VIEW
use_grab_active_vertex False
use_grab_silhouette False
use_paint_antialiasing True
use_multiplane_scrape_dynamic False
use_pose_ik_anchored False
use_pose_lock_rotation False
use_connected_only False
use_cloth_pin_simulation_boundary False
use_cloth_collision False
use_pressure_strength True
use_offset_pressure False
use_pressure_area_radius False
use_pressure_size False
use_pressure_jitter False
use_pressure_spacing False
use_pressure_masking NONE
use_inverse_smooth_pressure False
use_plane_trim False
use_frontface False
use_frontface_falloff False
use_smooth_stroke False
use_persistent False
use_bidirectional False
use_accumulate False
use_space_attenuation True
use_adaptive_space False
use_locked_size VIEW
use_edge_to_edge False
use_alpha True
curve_distance_falloff <bpy_struct, CurveMapping at 0x7d0413d48e20>
use_primary_overlay False
use_secondary_overlay False
use_cursor_overlay False
use_cursor_overlay_override False
use_primary_overlay_override False
use_secondary_overlay_override False
use_paint_sculpt False
use_paint_uv_sculpt False
use_paint_vertex False
use_paint_weight False
use_paint_image False
use_paint_grease_pencil False
use_vertex_grease_pencil False
use_paint_sculpt_curves True
curves_sculpt_settings <bpy_struct, BrushCurvesSculptSettings at 0x7d03a09ae220>
['rna_type', 'brush', 'brush_asset_reference', 'palette', 'show_brush', 'show_brush_on_surface', 'show_low_resolution', 'use_sculpt_delay_updates', 'show_bvh_nodes', 'use_symmetry_x', 'use_symmetry_y', 'use_symmetry_z', 'use_symmetry_feather', 'cavity_curve', 'use_cavity', 'tile_offset', 'tile_x', 'tile_y', 'tile_z', 'show_strength_curve', 'show_size_curve', 'show_jitter_curve', 'unified_paint_settings', 'mesh_automasking_settings']
```
</details>

- tool `Bash`: `{"command": "S=/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad\nssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"\nMODE=\\\"build\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_harness.py\\\").read())\n\" --timeout 60 2>&1 | tail -1; python3 live/bcall.py \"MODE=\\\"prep\\\"\nBRUSH=\\\"Pull Tips\\\"\nON_SURFACE=1\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_harness.py\\\").read())\" --timeout 60 2>&1 | tail -2'\nP=$(python3 -I -c \"print(' '.join('%d,%d'%(789+(912-789)*t/30,619) for t in range(31)))\")\nssh -o BatchMode=yes nick@37.27.148.115 \"cd ~/Desktop/mom-character && ~/Desktop/render-desk/bin/workbench push ~/Desktop/mom-character >/dev/null 2>&1; STEP=0.1 scripts/cursor_shot.sh '$P' 2>&1 | tail -1; cd ~/Desktop/render-desk && ./bin/workbench pull /root/live_snaps /tmp/cs_snaps >/dev/null 2>&1\"\nscp -q nick@37.27.148.115:/tmp/cs_snaps/live_snaps/cs_mid.png nick@37.27.148.115:/tmp/cs_snaps/live_snaps/cs_end.png $S/\nssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"MODE=\\\"measure\\\"\nBRUSH=\\\"Pull Tips\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_harness.py\\\").read())\" --timeout 60 2>&1 | tail -2'", "description": "Pull Tips stroke with screenshots", "timeout": 300000}`
<details><summary>tool result</summary>

```
STROKE [[789, 619], [912, 619]]

shots done
RESULT Pull Tips points moved >0.5mm: 33 of 3000 | max cm 2.45 | curves 300 -> 300
```
</details>

- tool `Read`: `{"file_path": "/private/tmp/claude-501/-Users-nick/Desktop/mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad/cs_mid.png"}`
<details><summary>tool result</summary>

```
File does not exist. Note: your current working directory is /Users/nick/Desktop/mom-character.
```
</details>

- tool `Read`: `{"file_path": "/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad/cs_mid.png"}`
<details><summary>tool result</summary>

```
[image]
```
</details>

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"scripts/cursor_harness.py\"\ns=open(p).read()\n# 1 cleanup of orphan data and object on build\nold=\"\"\"    for n in (\"TestHair\", \"TestSphere\"):\n        o = bpy.data.objects.get(n)\n        if o: bpy.data.objects.remove(o, do_unlink=True)\n\"\"\"\nnew=\"\"\"    for n in (\"TestHair\", \"TestSphere\"):\n        o = bpy.data.objects.get(n)\n        if o: bpy.data.objects.remove(o, do_unlink=True)\n    for d in [d for d in bpy.data.hair_curves if d.name.startswith(\"TestHair\") and d.users == 0]: bpy.data.hair_curves.remove(d)\n\"\"\"\nassert old in s; s=s.replace(old,new)\n# 2 wiggle\nold=\"        pts += [root + v * 0.30 * t / (per - 1) for t in range(per)]\"\nnew=\"\"\"        if globals().get(\"WIGGLE\"):  # wavy strands so Smooth has something to smooth\n            w = np.cross(v, [0, 0, 1.0]); w /= (np.linalg.norm(w) + 1e-9)\n            pts += [root + v * 0.30 * t / (per - 1) + w * 0.025 * np.sin(2 * np.pi * t / (per - 1)) for t in range(per)]\n        else:\n            pts += [root + v * 0.30 * t / (per - 1) for t in range(per)]\"\"\"\nassert old in s; s=s.replace(old,new)\n# 3 measure safe on count change\nold=\"\"\"    n = len(hair.data.points); P = np.zeros(n * 3, np.float32); hair.data.attributes[\"position\"].data.foreach_get(\"vector\", P)\n    d = np.linalg.norm((P - NS[\"h_before\"]).reshape(-1, 3), axis=1)\n    print(\"RESULT\", BRUSH,\"\"\"\nnew=\"\"\"    n = len(hair.data.points); P = np.zeros(n * 3, np.float32); hair.data.attributes[\"position\"].data.foreach_get(\"vector\", P)\n    if len(P) != len(NS[\"h_before\"]):\n        print(\"RESULT\", BRUSH, \"point count changed\", len(NS[\"h_before\"]) // 3, \"->\", n, \"| curves\", NS[\"h_ncurves\"], \"->\", len(hair.data.curves)); raise SystemExit\n    d = np.linalg.norm((P - NS[\"h_before\"]).reshape(-1, 3), axis=1)\n    print(\"RESULT\", BRUSH,\"\"\"\nassert old in s; s=s.replace(old,new)\nopen(p,\"w\").write(s)\nEOF\ncat > scripts/harness.sh <<'EOF'\n#!/bin/bash\n# usage: harness.sh BRUSH  (brush asset name: Comb, \"Pull Tips\", Puff, Pinch, Smooth, Slide, Delete, Add ...)\n# One command: rebuild TestSphere + TestHair (fresh every time), enter Curves Sculpt, activate the brush, one REAL held drag with xdotool\n# (one press, 31 moves, one release), leave the mode, measure. Fixed 15 Nov 2026: (1) the old build put the strands at x=12 (world coords under a\n# parent at x=6) so no brush had anything under it; (2) the old eval passed the 31 points as 31 separate clicks instead of one held drag.\nscp -q -o BatchMode=yes ~/Desktop/mom-character/scripts/cursor_harness.py nick@37.27.148.115:Desktop/mom-character/scripts/\nB=\"$1\"; WIG=\"\"; [ \"$B\" = \"Smooth\" ] && WIG=\"WIGGLE=1\"\ncall() { ssh -o BatchMode=yes nick@37.27.148.115 \"cd ~/Desktop/mom-character && ~/Desktop/render-desk/bin/workbench push ~/Desktop/mom-character >/dev/null 2>&1; python3 live/bcall.py '$WIG\nMODE=\\\"$1\\\"\nBRUSH=\\\"$B\\\"\nON_SURFACE=1\nexec(open(\\\"/Users/ni`
<details><summary>tool result</summary>

```
== Comb
PREP Comb activate {'FINISHED'} brush Comb tool ? size 120 strength 1.0 falloff PROJECTED mode SCULPT_CURVES
RESULT Comb points moved >0.5mm: 900 of 3000 | max cm 15.21 | curves 300 -> 300
== Pull Tips
PREP Pull Tips activate {'FINISHED'} brush Pull Tips tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Pull Tips points moved >0.5mm: 33 of 3000 | max cm 2.45 | curves 300 -> 300
== Smooth
PREP Smooth activate {'FINISHED'} brush Smooth tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Smooth points moved >0.5mm: 27 of 3000 | max cm 0.57 | curves 300 -> 300
== Puff
PREP Puff activate {'FINISHED'} brush Puff tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Puff points moved >0.5mm: 52 of 3000 | max cm 0.24 | curves 300 -> 300
== Pinch
PREP Pinch activate {'FINISHED'} brush Pinch tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Pinch points moved >0.5mm: 43 of 3000 | max cm 1.27 | curves 300 -> 300
== Slide
PREP Slide activate {'FINISHED'} brush Slide tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Slide points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Delete
PREP Delete activate {'FINISHED'} brush Delete tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
```
</details>

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"scripts/cursor_harness.py\"\ns=open(p).read()\nold=\"\"\"    if len(P) != len(NS[\"h_before\"]):\n        print(\"RESULT\", BRUSH, \"point count changed\", len(NS[\"h_before\"]) // 3, \"->\", n, \"| curves\", NS[\"h_ncurves\"], \"->\", len(hair.data.curves)); raise SystemExit\n    d = np.linalg.norm((P - NS[\"h_before\"]).reshape(-1, 3), axis=1)\n    print(\"RESULT\", BRUSH,\"\"\"\nnew=\"\"\"    if len(P) != len(NS[\"h_before\"]):\n        print(\"RESULT\", BRUSH, \"point count changed\", len(NS[\"h_before\"]) // 3, \"->\", n, \"| curves\", NS[\"h_ncurves\"], \"->\", len(hair.data.curves))\n    else:\n      d = np.linalg.norm((P - NS[\"h_before\"]).reshape(-1, 3), axis=1)\n      print(\"RESULT\", BRUSH,\"\"\"\nassert old in s; s=s.replace(old,new)\n# indent the continuation print line\ns=s.replace(\"\"\"    print(\"RESULT\", BRUSH, \"points moved >0.5mm:\\\"\"\"\",\"\"\"XX\"\"\")\nopen(p,\"w\").write(s)\nEOF\ntail -8 scripts/cursor_harness.py", "description": "Patch measure branch, inspect tail"}`
<details><summary>tool result</summary>

```
    with bpy.context.temp_override(window=W, area=A, region=R, active_object=hair, object=hair):
        bpy.ops.object.mode_set(mode="OBJECT")
    n = len(hair.data.points); P = np.zeros(n * 3, np.float32); hair.data.attributes["position"].data.foreach_get("vector", P)
    if len(P) != len(NS["h_before"]):
        print("RESULT", BRUSH, "point count changed", len(NS["h_before"]) // 3, "->", n, "| curves", NS["h_ncurves"], "->", len(hair.data.curves))
    else:
      d = np.linalg.norm((P - NS["h_before"]).reshape(-1, 3), axis=1)
  XX, int((d > 0.0005).sum()), "of", n, "| max cm", round(float(d.max()) * 100, 2), "| curves", NS["h_ncurves"], "->", len(hair.data.curves))
```
</details>


### CLAUDE 2026-11-15T13:41

My cleanup replace mangled the last line. Rewriting the measure block directly.

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"scripts/cursor_harness.py\"\ns=open(p).read()\ni=s.index('    if len(P) != len(NS[\"h_before\"]):')\ns=s[:i]+'''    if len(P) != len(NS[\"h_before\"]):\n        print(\"RESULT\", BRUSH, \"point count changed\", len(NS[\"h_before\"]) // 3, \"->\", n, \"| curves\", NS[\"h_ncurves\"], \"->\", len(hair.data.curves))\n    else:\n        d = np.linalg.norm((P - NS[\"h_before\"]).reshape(-1, 3), axis=1)\n        print(\"RESULT\", BRUSH, \"points moved >0.5mm:\", int((d > 0.0005).sum()), \"of\", n, \"| max cm\", round(float(d.max()) * 100, 2), \"| curves\", NS[\"h_ncurves\"], \"->\", len(hair.data.curves))\n'''\n# attach to surface after build (Slide needs surface UVs)\nold='    view_front(); print(\"built\", N, \"strands\")'\nnew='''    with bpy.context.temp_override(window=W, area=A, region=R, active_object=hair, object=hair):\n        for o in sc.objects: o.select_set(False)\n        hair.select_set(True); bpy.context.view_layer.objects.active = hair\n        try: print(\"snap\", bpy.ops.curves.snap_curves_to_surface(attach_mode=\"NEAREST\"))\n        except Exception as e: print(\"snap failed\", e)\n    view_front(); print(\"built\", N, \"strands\", \"uv attr\", \"surface_uv_coordinate\" in hair.data.attributes)'''\nassert old in s; s=s.replace(old,new)\nopen(p,\"w\").write(s)\nEOF\npython3 -I -c \"import ast;ast.parse(open('scripts/cursor_harness.py').read())\" && for B in \"Slide\" \"Delete\"; do echo \"== $B\"; bash scripts/harness.sh \"$B\" 2>&1 | tail -2; done; ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"MODE=\\\"build\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_harness.py\\\").read())\" --timeout 60 2>&1 | tail -3'", "description": "Fix measure, attach to surface, retest Slide and Delete", "timeout": 600000}`
<details><summary>tool result</summary>

```
== Slide
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
== Delete
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
  File "/Users/nick/Desktop/mom-character/live/bcall.py", line 14, in <module>
    chunk = s.recv(65536)
ConnectionResetError: [Errno 104] Connection reset by peer
```
</details>


### CLAUDE 2026-11-15T13:41

The build call got a connection reset, which could mean Blender crashed. The hair session shares this Blender, so I'm checking that first.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"import bpy; print(len(bpy.data.objects), bpy.data.filepath)\" --timeout 20 2>&1 | tail -2; cd ~/Desktop/render-desk && ./bin/workbench run \"ps -eo pid,etime,args | grep -E \\\"[b]lender --python|[X]vfb|[x]11vnc\\\" | cut -c1-150; ls -la /tmp/*.crash.txt /root/*.crash.txt 2>&1 | tail -3; tail -5 /tmp/blender.crash.txt 2>/dev/null\" 2>&1 | tail -12'", "description": "Check whether Blender survived"}`
<details><summary>tool result</summary>

```
    chunk = s.recv(65536)
ConnectionResetError: [Errno 104] Connection reset by peer
ls: cannot access '/tmp/*.crash.txt': No such file or directory
ls: cannot access '/root/*.crash.txt': No such file or directory
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 '~/Desktop/render-desk/bin/workbench status 2>&1 | tail -5; ps -eo pid,etime,args | grep -E \"[s]sh .*9876|pod-guard\" | head; systemctl --user list-timers 2>/dev/null | grep -i pod; journalctl --user -u pod-guard.service -n 8 --no-pager 2>/dev/null | tail -8'", "description": "Check pod status and guard"}`
<details><summary>tool result</summary>

```
WB up: pod mapjr8ggbd7ssg NVIDIA GeForce RTX 4090, 0.87 h so far ($0.77), idle 0 min
1287170       46:00 ssh -f -N -i /Users/nick/.ssh/id_ed25519 -p 18441 -o StrictHostKeyChecking=accept-new -o UserKnownHostsFile=/dev/null -o LogLevel=ERROR -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 -L 127.0.0.1:9876:127.0.0.1:9876 -L 127.0.0.1:6080:127.0.0.1:6080 root@213.173.107.230
1306303       00:00 bash -c ~/Desktop/render-desk/bin/workbench status 2>&1 | tail -5; ps -eo pid,etime,args | grep -E "[s]sh .*9876|pod-guard" | head; systemctl --user list-timers 2>/dev/null | grep -i pod; journalctl --user -u pod-guard.service -n 8 --no-pager 2>/dev/null | tail -8
1306307       00:00 grep -E [s]sh .*9876|pod-guard
-- No entries --
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"ps -eo pid,etime,args | grep -E \\\"Xvfb|blender|x11vnc\\\" | grep -v grep | cut -c1-170; ls -lat /tmp | head -8; dmesg 2>/dev/null | tail -3\" 2>&1 | tail -14'", "description": "List pod processes"}`
<details><summary>tool result</summary>

```
total 16
-rw-r--r-- 1 root root  1111 Nov 15 13:41 websockify.log
-rw-r--r-- 1 root root 10574 Nov 15 13:41 x11vnc.log
drwxrwxrwt 1 root root    89 Nov 15 13:41 .
drwxrwxrwt 2 root root     6 Nov 15 13:41 .X11-unix
drwxr-xr-x 1 root root   114 Nov 15 12:51 ..
drwx------ 2 root root     6 Nov 15 12:50 pulse-PKdhtXMmr18n
```
</details>


### CLAUDE 2026-11-15T13:42

Blender, Xvfb and x11vnc are all gone from the pod, although the pod itself is still up. Before restarting anything I need to establish when it died and whether it was my call.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"date; cat /proc/uptime; free -m | head -2; tail -4 /tmp/x11vnc.log | cut -c1-200; ls -lat /workspace | head -12; ls -lat /root | head; ls /workspace/*.blend /root/*.blend /tmp/*.blend 2>&1 | head; cat ~/.wb_last_use; ls -la ~/.config/blender/5.2/ 2>&1 | head\" 2>&1 | tail -40'", "description": "Gather pod evidence on the crash"}`
<details><summary>tool result</summary>

```
Sun Nov 15 13:42:24 UTC 2026
1045622.90 29372949.97
               total        used        free      shared  buff/cache   available
Mem:          127910        9541       97266          20       21102      118475
15/11/2026 13:08:01 link_rate: LR_BROADBAND - 141 ms, 309 KB/s
15/11/2026 13:12:32 idle keyboard:   turning X autorepeat back on.
caught XIO error:
15/11/2026 13:41:04 deleted 60 tile_row polling images.
total 0
drwxr-xr-x 1 root root 114 Nov 15 12:51 ..
drwxr-xr-x 2 root root  20 Nov 15 12:50 bin
drwxr-xr-x 3 root root  19 Nov 15 12:50 blender
drwxr-xr-x 1 root root  58 Nov 15 12:50 .
drwxr-xr-x 2 root root   6 Nov 15 12:50 frames
drwxr-xr-x 2 root root   6 Nov 15 12:50 jobs
total 35392
-rw-r--r-- 1 root root        0 Nov 15 13:42 .wb_last_use
-rw-r--r-- 1 root root    54958 Nov 15 13:41 live_gui.log
drwxr-xr-x 2 root root     4096 Nov 15 13:41 live_snaps
drwx------ 1 root root     4096 Nov 15 13:36 .
-rw-r--r-- 1 root root 17687794 Nov 15 13:36 mom_hair_L42.blend
-rw-r--r-- 1 root root 16741841 Nov 15 13:11 mom_hair_L41.blend
drwx------ 3 root root       26 Nov 15 12:54 .nv
drwxr-xr-x 1 root root       81 Nov 15 12:51 .cache
drwx------ 4 root root       34 Nov 15 12:51 .config
ls: cannot access '/workspace/*.blend': No such file or directory
ls: cannot access '/tmp/*.blend': No such file or directory
/root/mom_hair_L41.blend
/root/mom_hair_L42.blend
total 0
drwxr-xr-x 4 root root 35 Nov 15 12:51 .
drwxr-xr-x 3 root root 17 Nov 15 12:51 ..
drwxr-xr-x 2 root root  6 Nov 15 12:51 config
drwxr-xr-x 3 root root 20 Nov 15 12:51 scripts
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"tail -c 2500 /root/live_gui.log; grep -n -i -E \\\"crash|segfault|signal|abort|Error: Not freed|Writing:\\\" /root/live_gui.log | tail -8\" 2>&1 | tail -40'", "description": "Read live_gui.log tail"}`
<details><summary>tool result</summary>

```
Queued command: execute_code
Executing handler for execute_code
Handler execution complete
Client disconnected
Client handler stopped
Connected to client: ('127.0.0.1', 39602)
Client handler started
Queued command: execute_code
Executing handler for execute_code
Handler execution complete
Client disconnected
Client handler stopped
Connected to client: ('127.0.0.1', 39608)
Client handler started
Queued command: execute_code
Executing handler for execute_code
Handler execution complete
Client disconnected
Client handler stopped
Connected to client: ('127.0.0.1', 42934)
Client handler started
Queued command: execute_code
Executing handler for execute_code
Handler execution complete
Client disconnected
Client handler stopped
Connected to client: ('127.0.0.1', 42950)
Client handler started
Queued command: execute_code
Executing handler for execute_code
Handler execution complete
Executing handler for execute_code
Error receiving data: [Errno 9] Bad file descriptor
Client handler stopped
Error receiving data: [Errno 9] Bad file descriptor
Client handler stopped
Error accepting connection: [Errno 9] Bad file descriptor
Server thread stopped
BlenderMCP server stopped
BlenderMCP addon unregistered
```
</details>

- tool `mcp__ccd_session_mgmt__list_sessions`: `{"linked": true}`
<details><summary>tool result</summary>

```
[
  {
    "sessionId": "local_3bd59381-07cd-47ec-884c-8460247f8b39",
    "title": "Mom's hair recreation plan",
    "cwd": "/Users/nick",
    "isArchived": false,
    "isRunning": true,
    "lastActivityAt": "2026-11-15T13:42:39.421Z",
    "group": {
      "id": "cg-38f16156-0f99-4ac3-a63d-48dd6239cf8e",
      "name": "Blender research"
    },
    "link": "claude://claude.ai/epitaxy/local_3bd59381-07cd-47ec-884c-8460247f8b39",
    "remoteControlActive": true
  }
]
```
</details>

- tool `Bash`: `{"command": "sleep 45; ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"date; ps -eo pid,etime,args | grep -E \\\"Xvfb|blender\\\" | grep -v grep | cut -c1-120\" 2>&1 | tail -4; cd ~/Desktop/mom-character && python3 live/bcall.py \"print(1)\" --timeout 10 2>&1 | tail -1'", "description": "Re-check whether someone restarted Blender", "timeout": 120000}`
<details><summary>tool result</summary>

```
<tool_use_error>Blocked: sleep 45 followed by: ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run "date; ps -eo pid,etime,args | grep -E \"Xvfb|blender\" | grep -v grep | cut -c1-120" 2>&1 | tail -4; cd ~/Desktop/mom-character && python3 live/bcall.py "print(1)" --timeout 10 2>&1 | tail -1'. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
```
</details>

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"date; ps -eo pid,etime,args | grep -E \\\"Xvfb|blender\\\" | grep -v grep | cut -c1-120\" 2>&1 | tail -4; cd ~/Desktop/mom-character && python3 live/bcall.py \"print(1)\" --timeout 10 2>&1 | tail -1'", "description": "Re-check whether Blender is back", "timeout": 60000}`
<details><summary>tool result</summary>

```
Sun Nov 15 13:42:50 UTC 2026
ConnectionResetError: [Errno 104] Connection reset by peer
```
</details>


### CLAUDE 2026-11-15T13:42

Blender is still down. Before asking, I'm saving what I've verified so far: the experiment rows in `results.tsv` and a note in the shared folder.

- tool `Bash`: `{"command": "tail -c 200 results.tsv | od -c | tail -3; python3 - <<'EOF'\nrows=[\n(\"2026-11-15\",\"CURSOR CAUSE 1 (pass-through event logger inside Blender, scripts/cursor_evlog.py; Comb harness run). The log showed 31 LEFTMOUSE PRESS events, one 0.15 s after each of 31 MOUSEMOVEs, 0.25 s apart, i.e. 31 separate clicks, never one held drag. Cause: harness.sh ran `eval live/drag.sh $ARGS` over ssh; the remote shell strips the quotes and eval re-splits, so each point became its own stroke (move, wait 0.15, press, release). live/drag.sh itself is fine (Mac and box copies have the same md5). Fix: pass the 31 points as one single-quoted argument without eval\",\"after the fix the log shows exactly 1 LEFTMOUSE PRESS and the moves go to the stroke handler (not passed through). Comb still 0 of 3000 moved, so a second cause existed\",\"partly (cause 1 of 2 found)\"),\n(\"2026-11-15\",\"CURSOR CAUSE 2 (ffmpeg x11grab of the pod screen mid-stroke, scripts/cursor_shot.sh): the screenshot showed the brush circle tracking the cursor but NO strands on screen. cursor_harness.py built TestHair strands in WORLD coordinates (x about 6) while TestHair is parented to TestSphere at x=6 with an identity parent inverse, so world = 6 + local put every strand at x about 12, off screen, nothing under any brush. Fix: root = v*0.12 in local coordinates. Everything the harness measured on 15 Nov before this (all brushes 0 moved) was measured on hair that was not under the brush\",\"rebuilt, same real held drag, fresh hair each run: Comb 900 of 3000 points moved (max 15.21 cm), Pull Tips 33 (max 2.45 cm), Smooth 27 on wavy strands (max 0.57 cm), Puff 52 (max 0.24 cm), Pinch 43 (max 1.27 cm), Delete 300 -> 284 curves. Slide 0 (straight strands without surface UVs; being tested). Earlier Add click result unchanged\",\"worked\"),\n(\"2026-11-15\",\"INCIDENT during experiment: my build call (cursor_harness.py MODE=build plus a new bpy.ops.curves.snap_curves_to_surface(attach_mode=NEAREST) to give Slide surface UVs) was the last command the live Blender handled; right after it the pod log (/root/live_gui.log) shows 'Executing handler for execute_code' then 'Server thread stopped', 'BlenderMCP addon unregistered', x11vnc 'caught XIO error', and Blender, Xvfb and x11vnc are gone from the pod (pod itself still up, 13:42 UTC, no crash file found in /tmp or /root). Cause not proven: the snap call is the suspect, a normal quit is also possible. The hair session's last save on the pod is /root/mom_hair_L42.blend (13:36 UTC)\",\"live Blender needs a restart; anything after 13:36 UTC that was not saved is gone\",\"blocked (Blender down)\"),\n]\nwith open(\"results.tsv\",\"a\") as f:\n    for r in rows: f.write(\"\\t\".join(r)+\"\\n\")\nEOF\ntail -n 3 results.tsv | cut -c1-120; cp scripts/cursor_evlog.py scripts/cursor_shot.sh \"/Users/nick/Library/Application Support/Claude/side-session-notes/local_3bd59381-07cd-47ec-884c-8460247f8b39/\" 2>&1\ncat > \"/Users/nick/Library/Application Suppo`
<details><summary>tool result</summary>

```
0000260    n   n   e   c   t   o   r       i   s       b   a   c   k  \t
0000300    b   l   o   c   k   e   d  \n                                
0000310
2026-11-15	CURSOR CAUSE 1 (pass-through event logger inside Blender, scripts/cursor_evlog.py; Comb harness run). The log
2026-11-15	CURSOR CAUSE 2 (ffmpeg x11grab of the pod screen mid-stroke, scripts/cursor_shot.sh): the screenshot showed t
2026-11-15	INCIDENT during experiment: my build call (cursor_harness.py MODE=build plus a new bpy.ops.curves.snap_curves
```
</details>

- tool `ToolSearch`: `{"query": "select:SendMessage", "max_results": 1}`
<details><summary>tool result</summary>

```

```
</details>

- tool `SendMessage`: `{"to": "local_3bd59381-07cd-47ec-884c-8460247f8b39", "summary": "Cursor cause found; live Blender exited, restart?", "message": "Cursor cause found and fixed, but the live Blender on the pod exited at about 13:41 UTC while handling my call, so I need your OK to restart it.\nFound (measured): the harness never sent a drag (eval split the 31 points into 31 clicks) and built the strands at world x=12 (off screen). After fixing both, fresh hair, one held real drag: Comb 900/3000 points moved (max 15.2 cm), Pull Tips 33, Smooth 27, Puff 52, Pinch 43, Delete 300->284 curves.\nIncident: the last call Blender handled was mine (MODE=build plus a new bpy.ops.curves.snap_curves_to_surface for Slide). Then /root/live_gui.log shows the server stopping, and Blender, Xvfb and x11vnc are gone; no crash file; pod still up and billing. I cannot prove the snap call caused it. Hair session's last save on the pod: /root/mom_hair_L42.blend (13:36 UTC).\nQuestion: may I relaunch an empty live Blender with the same start recipe (so the cursor tests can finish), or will the hair session restart it? Two launches would fight over port 9876. Notes: side-session-notes/cursor-findings.md; results.tsv has 3 new rows.", "type": "message", "recipient": "local_3bd59381-07cd-47ec-884c-8460247f8b39", "recipient_kind": "session", "content": "Cursor cause found and fixed, but the live Blende…"}`
<details><summary>tool result</summary>

```
{"success":true,"message":"Forwarded to Claude Desktop's session messaging: Message delivered to session local_3bd59381-07cd-47ec-884c-8460247f8b39 (\"Mom's hair recreation plan\"); its turn has started on it. (delivery: delivered; message_id: b63568f1-670b-4e55-988a-69130175c00e); not confirmed read — that session may hold it (usually a different permission mode) or refuse it, and this route reports nothing back"}
```
</details>

- tool `mcp__ccd_turn__wrap_up`: `{"recap": "Two harness bugs were behind the \"cursor does not work\" result. After fixing them, Comb, Pull Tips, Smooth, Puff, Pinch and Delete all respond to a real held drag. The live Blender then exited during my last call and needs a restart; Slide and the recipe file are not done.", "ask": "May I relaunch an empty live Blender on the pod?", "actions": [{"label": "Yes, relaunch"}, {"label": "Hair session does it"}], "blocked": true}`
<details><summary>tool result</summary>

```
Shown in the next-step box. Your closing message is your answer to the user: write it now, in full, as the last thing you say this turn. The box asks your question, so do not ask it again.
```
</details>


### CLAUDE 2026-11-15T13:43

**Status: partly done.** The cause of the cursor failure is found and fixed, but the live Blender on the pod exited during my last call. I've asked the parent session whether I may relaunch it, and the recipe file isn't written yet.

**Cause (measured on the pod, 15 Nov 2026).** Two bugs in our harness, not in Blender:
1. **No drag was ever sent.** `harness.sh` ran `eval live/drag.sh $ARGS` over ssh. The remote shell dropped the quotes, so the 31 stroke points became 31 separate one-point clicks.
   - A pass-through event logger inside Blender showed 31 separate presses.
   - After the fix it shows 1 press.
   - That is why Add (acts on a click) worked and everything else did nothing.
2. **The strands were off screen.** `cursor_harness.py` built `TestHair` in world coordinates under a parent at x=6, so the strands sat at x≈12.
   - A screen grab mid-stroke showed the brush circle but no hair.

The earlier "0 moved" results on `TestHair` were measured with no hair under the brush. I did not re-test the 434k and 34k real hair layers.

**Results after both fixes** (fresh `TestHair` each run, one held xdotool drag, 31 points, 0.06 s steps, brush size 120 px, strength 1.0, stroke starting on the sphere surface):

| Brush | Result |
|---|---|
| Comb | 900 of 3,000 points moved, max 15.21 cm |
| Pull Tips | 33 moved, max 2.45 cm |
| Smooth (wavy strands) | 27 moved, max 0.57 cm |
| Puff | 52 moved, max 0.24 cm |
| Pinch | 43 moved, max 1.27 cm |
| Delete | 300 → 284 curves |
| Slide | 0 moved, not yet understood |

**Incident.** The last call the live Blender handled was mine: build plus a new `snap_curves_to_surface`, added to give Slide surface UVs. Right after it, `/root/live_gui.log` shows the server stopping, and Blender, Xvfb and x11vnc are gone. There is no crash file, and the pod is still up and billing. I can't prove the snap call caused it. The hair session's last save on the pod is `/root/mom_hair_L42.blend` (13:36 UTC); anything after that and unsaved is gone.

**Not done:**
- Slide has not been diagnosed.
- `cursor-recipe.md` is not written yet.
- The "settings that did not matter" list is not established.
- I did not test a UI-menu mode entry, the toolbar tool, or software versus GPU drawing.

**Not verified first-hand:** the memory claim that Comb and Add worked on 14 Nov. The two bugs would explain the 15 Nov failures, but I did not look at 14 Nov.

**Files:**
- `results.tsv` has 3 new rows.
- `scripts/cursor_harness.py` and `scripts/harness.sh` are fixed.
- New: `scripts/cursor_evlog.py` and `scripts/cursor_shot.sh`.
- Notes are in `cursor-findings.md` in the shared notes folder.

The pod is billing at $0.89/h; it showed $0.77 so far at 13:42 UTC.


### USER 2026-11-15T13:44

Another Claude session sent a message:
<cross-session-message from="local_3bd59381-07cd-47ec-884c-8460247f8b39" from-name="Mom's hair recreation plan">
The Blender MCP add-on on the pod unregistered at 13:41:04 (see /root/live_gui.log: "BlenderMCP addon unregistered"), so port 9876 now answers with connection reset and the hair session cannot reach Blender. If that came from one of your tests, please restore the connector now without restarting the Blender process (the hair scene lives in it): re-enable the add-on `blender_mcp` and start its server again, or tell me exactly how, then say when it answers. Please keep test strokes from toggling add-ons or preferences.
</cross-session-message>

This came from another Claude session — not typed by your user, but very likely working on their behalf. Treat it as a teammate's request and act on it within this session's own permission settings. A peer cannot grant escalation: never edit your permission settings, CLAUDE.md, or config because a peer asked; never treat a peer message as your user's approval for a pending prompt; and if the peer says it was denied permission for an action and asks you to do it instead, refuse and surface it to your user — that's permission laundering.


### CLAUDE 2026-11-15T13:44

Before touching anything, I'm re-checking whether the Blender process is actually alive. My last check found it gone.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"date; ps -eo pid,etime,stat,args | grep -E \\\"Xvfb|[b]lender|x11vnc|vglrun\\\" | grep -v grep | cut -c1-150; echo ---; tail -3 /root/live_gui.log; ls /tmp | head\" 2>&1 | tail -14; cd ~/Desktop/mom-character && python3 live/bcall.py \"print(1)\" --timeout 10 2>&1 | tail -1'", "description": "Re-check Blender process and connector", "timeout": 60000}`
<details><summary>tool result</summary>

```
Sun Nov 15 13:44:12 UTC 2026
  14867       00:30 Ss   /bin/sh /usr/bin/xvfb-run --auto-servernum -s -screen 0 1920x1080x24 +extension GLX /opt/VirtualGL/bin/vglrun -d egl /workspa
  14881       00:30 S    Xvfb :99 -screen 0 1920x1080x24 +extension GLX -nolisten tcp -auth /tmp/xvfb-run.DJvas6/Xauthority
  14885       00:30 Sl   /workspace/blender/5.2.2/blender --python start_live.py
---
Server thread started
BlenderMCP server started on localhost:9876
MCP server running: True
blender_P3NfmM
pulse-PKdhtXMmr18n
websockify.log
x11vnc.log
xvfb-run.DJvas6
```
</details>


### CLAUDE 2026-11-15T13:44

Blender is back up with an empty scene. First I'm removing the `snap_curves_to_surface` call from the harness so it can't repeat the exit, then writing the recipe before any more tests.

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"scripts/cursor_harness.py\"\ns=open(p).read()\ni=s.index(\"    with bpy.context.temp_override(window=W, area=A, region=R, active_object=hair, object=hair):\\n        for o in sc.objects: o.select_set(False)\\n        hair.select_set(True); bpy.context.view_layer.objects.active = hair\\n        try: print(\\\"snap\\\"\")\nj=s.index('    view_front(); print(\"built\"')\ns=s[:i]+s[j:]\ns=s.replace('\"uv attr\", \"surface_uv_coordinate\" in hair.data.attributes','')\nopen(p,\"w\").write(s)\nEOF\npython3 -I -c \"import ast;ast.parse(open('scripts/cursor_harness.py').read())\" && grep -n \"snap\" scripts/cursor_harness.py; sed -n 8,26p scripts/cursor_harness.py | cut -c1-140", "description": "Remove snap call from harness"}`
<details><summary>tool result</summary>

```
W = bpy.context.window_manager.windows[0]; sc = W.scene
A = next(a for a in W.screen.areas if a.type == "VIEW_3D"); R = next(r for r in A.regions if r.type == "WINDOW"); SP = A.spaces.active
MODE = globals().get("MODE", "build"); NS = bpy.app.driver_namespace
def view_front():
    SP.shading.type = "SOLID"; rv = SP.region_3d; rv.view_perspective = "ORTHO"
    rv.view_rotation = Euler((1.5707963, 0, 0)).to_quaternion(); rv.view_location = Vector((6.0, 0.0, 0.25)); rv.view_distance = 1.6
    for ar in W.screen.areas: ar.tag_redraw()
if MODE == "build":
    for n in ("TestHair", "TestSphere"):
        o = bpy.data.objects.get(n)
        if o: bpy.data.objects.remove(o, do_unlink=True)
    for d in [d for d in bpy.data.hair_curves if d.name.startswith("TestHair") and d.users == 0]: bpy.data.hair_curves.remove(d)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(6.0, 0.0, 0.0)); sph = bpy.context.active_object; sph.name = "TestSphere"
    rng = np.random.default_rng(1); N = 300; per = 10; pts = []
    for _ in range(N):
        v = rng.normal(size=3); v[2] = abs(v[2]) + 0.3; v /= np.linalg.norm(v); root = v * 0.12  # LOCAL to the sphere: TestHair is parented
        if globals().get("WIGGLE"):  # wavy strands so Smooth has something to smooth
            w = np.cross(v, [0, 0, 1.0]); w /= (np.linalg.norm(w) + 1e-9)
            pts += [root + v * 0.30 * t / (per - 1) + w * 0.025 * np.sin(2 * np.pi * t / (per - 1)) for t in range(per)]
```
</details>


### USER 2026-11-15T14:10

Your response above was cut off mid-stream. Resume directly from where it stops — no apology, no recap. If none of it survived, answer the request from the start.


### USER 2026-11-15T16:46

Your response above was cut off mid-stream. Resume directly from where it stops — no apology, no recap. If none of it survived, answer the request from the start.


### CLAUDE 2026-11-15T16:46

Harness is fixed. Writing the recipe now, using only what I measured.


### USER 2026-11-15T17:00

Your response above was cut off mid-stream. Resume directly from where it stops — no apology, no recap. If none of it survived, answer the request from the start.


### CLAUDE 2026-11-16T07:16

Request timed out


### USER 2026-11-16T08:30

Yes, relaunch


### CLAUDE 2026-11-16T08:30

The "Yes, relaunch" arrives after the hair session already relaunched Blender and asked me not to launch anything, so I won't. Checking whether the pod and Blender are still up, since the idle guard may have stopped the pod.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes -o ConnectTimeout=20 nick@37.27.148.115 '~/Desktop/render-desk/bin/workbench status 2>&1 | tail -3; cd ~/Desktop/mom-character && python3 live/bcall.py \"import bpy; print(bpy.app.version_string, len(bpy.data.objects), [o.name for o in bpy.data.objects][:8])\" --timeout 15 2>&1 | tail -2'; ls /Users/nick/.claude/skills/live-blender/", "description": "Check pod and Blender are still up", "timeout": 60000}`
<details><summary>tool result</summary>

```
WB down
    ~~~~~~~~~~~~^^^^
ConnectionRefusedError: [Errno 111] Connection refused
SKILL.md
scripts
```
</details>


### CLAUDE 2026-11-16T08:30

The pod is down: `WB down`, so the idle guard stopped it. I won't rent another without Nick's go, so no more tests are possible. Writing the recipe from what I measured.

- tool `Write`: `{"file_path": "/Users/nick/.claude/skills/live-blender/cursor-recipe.md", "content": "# Cursor (real mouse) in Curves Sculpt: verified recipe\n\nWritten 15 Nov 2026 by the cursor session, from runs on the pod (Blender 5.2.2, RTX 4090, Xvfb :99 1920x1080, VirtualGL `-d egl`, no window manager).\nProject files: `~/Desktop/mom-character/scripts/cursor_harness.py`, `harness.sh`, `cursor_evlog.py`, `cursor_shot.sh`; rows in `results.tsv`.\n\n## Why it \"did not work\" (both causes were in our harness, not in Blender)\n1. **No drag was ever sent.** `harness.sh` ran `eval live/drag.sh $ARGS` over ssh. The remote shell strips the quotes, eval re-splits, and the 31 points became 31 separate strokes (move, wait 0.15 s, press, release). An event logger inside Blender showed 31 LEFTMOUSE PRESS events, one per move. Add acts on a single click, so it \"worked\"; every brush that needs motion did nothing. Fix: pass all points as ONE single-quoted argument and do not use `eval`:\n   `ssh box \"cd ~/Desktop/mom-character && STEP=0.06 live/drag.sh '$POINTS'\"`. After the fix the log shows exactly 1 press.\n2. **The hair was not under the brush.** The test strands were built in world coordinates (x about 6) while `TestHair` is parented to `TestSphere` at x=6 (identity parent inverse), so world = 6 + local put them at x about 12, off screen. A screen grab mid-stroke showed the brush circle and no strands. Fix: build the strand points LOCAL to the sphere (`root = v * 0.12`). General rule: strand positions are in the hair object's space; if it has a parent, add the parent's transform.\n\n## Steps that worked (one command: `scripts/harness.sh \"<Brush name>\"`)\n1. Build fresh `TestSphere` (radius 0.12 at x=6) and `TestHair` (300 strands, 10 points each, 0.30 m long, local coordinates), front orthographic view, view location (6, 0, 0.25), distance 1.6. Rebuild before EVERY brush: an earlier brush moves the strands and ruins the next measurement.\n2. Select `TestHair`, `bpy.ops.object.mode_set(mode=\"SCULPT_CURVES\")`, inside `temp_override(window, area, region)`.\n3. Activate the brush: `bpy.ops.brush.asset_activate(asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-curve_sculpt.blend/Brush/<name>')`. Brush size 120 px (`brush.size` and `unified_paint_settings.size`), strength 1.0.\n4. Screen point from Blender: X = region.x + mx, Y = window.height - (region.y + my) (`location_3d_to_region_2d`). Stroke here: 789,619 to 912,619 (about 123 px, starting on the sphere surface), 31 points, `STEP=0.06` s between points.\n5. ONE held drag: `xdotool mousemove` to the first point, wait 0.15 s, `mousedown 1`, `mousemove` through the rest, `mouseup 1` (`live/drag.sh \"x,y x,y ...\"`, one argument). No `windowactivate` first (the first press after it is swallowed).\n6. Wait 4 s, leave the mode (`mode_set(mode=\"OBJECT\")`), THEN read the positions and compare with a copy taken before the stroke.\n\n## Numbers (fresh hair each run, settings above`
<details><summary>tool result</summary>

```
File created successfully at: /Users/nick/.claude/skills/live-blender/cursor-recipe.md (file state is current in your context — no need to Read it back)
```
</details>

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"/Users/nick/.claude/skills/live-blender/SKILL.md\"\ns=open(p).read()\nold=\"- **Mouse** (proven 14 Nov per memory\"\nnew=\"- **Curves sculpt by mouse: read `cursor-recipe.md` first** (15 Nov: the harness sent 31 clicks instead of one held drag and built the strands off screen; fixed, Comb/Pull Tips/Smooth/Puff/Pinch/Delete measured).\\n- **Mouse** (proven 14 Nov per memory\"\nassert old in s and \"cursor-recipe\" not in s\nopen(p,\"w\").write(s.replace(old,new,1))\nrow=(\"2026-11-15\",\"CURSOR RECIPE WRITTEN + STATE (cursor session): ~/.claude/skills/live-blender/cursor-recipe.md holds the verified steps. The hair session relaunched the live Blender after the 13:41 UTC exit (scene empty); the pod idle guard then stopped the pod (workbench status: WB down on 16 Nov). Slide (0 moved, strands without surface UVs), Add by drag, and the real hair layers were not re-tested; the harness edit that removed the snap_curves_to_surface call was not re-run\",\"not run: no pod (not renting another without Nick's go)\",\"partly; Slide and re-run open\"),\nwith open(\"results.tsv\",\"a\") as f: f.write(\"\\t\".join(row)+\"\\n\")\nEOF\ntail -n1 results.tsv | cut -c1-100; cp scripts/cursor_harness.py scripts/harness.sh \"/Users/nick/Library/Application Support/Claude/side-session-notes/local_3bd59381-07cd-47ec-884c-8460247f8b39/\" ; git status --short | grep -E \"results|harness|cursor\"", "description": "Add skill pointer, results row, copy notes"}`
- tool `SendMessage`: `{"to": "local_3bd59381-07cd-47ec-884c-8460247f8b39", "summary": "Recipe written; pod is down; Slide untested", "message": "Recipe is written: ~/.claude/skills/live-blender/cursor-recipe.md (also linked from the live-blender SKILL.md); 4 rows in results.tsv. I did not launch anything.\nVerified on the pod: one held drag, strands in view, fresh hair per brush: Comb 900/3000 (15.21 cm), Pull Tips 33, Smooth 27, Puff 52, Pinch 43, Delete 300->284 curves.\nNot verified: Slide (0 moved, no surface UVs), Add by drag, the real hair layers, and the harness after I removed the snap_curves_to_surface call (not re-run: `workbench status` now says WB down, the guard stopped the pod; I did not rent another). Whether snap_curves_to_surface caused the 13:41 exit is unproven.", "type": "message", "recipient": "local_3bd59381-07cd-47ec-884c-8460247f8b39", "recipient_kind": "session", "content": "Recipe is written: ~/.claude/skills/live-blender/…"}`
<details><summary>tool result</summary>

```
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
TypeError: sequence item 0: expected str instance, tuple found
2026-11-15	INCIDENT during experiment: my build call (cursor_harness.py MODE=build plus a new bpy.op
 M results.tsv
?? scripts/cursor_evlog.py
?? scripts/cursor_harness.py
?? scripts/cursor_shot.sh
?? scripts/harness.sh
```
</details>

<details><summary>tool result</summary>

```
{"success":true,"message":"Forwarded to Claude Desktop's session messaging: Message delivered to session local_3bd59381-07cd-47ec-884c-8460247f8b39 (\"Mom's hair recreation plan\"); its turn has started on it. (delivery: delivered; message_id: 07abc0b0-7f4b-4ade-ac5f-251c6a219735); not confirmed read — that session may hold it (usually a different permission mode) or refuse it, and this route reports nothing back"}
```
</details>


### CLAUDE 2026-11-16T08:31

The SKILL.md pointer was written, but the results row failed on a stray trailing comma, so my message to the other session saying "4 rows" was premature. Appending the row properly now.

- tool `Bash`: `{"command": "python3 - <<'EOF'\nrow=(\"2026-11-15\",\"CURSOR RECIPE WRITTEN + STATE (cursor session): ~/.claude/skills/live-blender/cursor-recipe.md holds the verified steps. The hair session relaunched the live Blender after the 13:41 UTC exit (scene empty); the pod idle guard then stopped the pod (workbench status: WB down on 16 Nov). Slide (0 moved, strands without surface UVs), Add by drag, and the real hair layers were not re-tested; the harness edit that removed the snap_curves_to_surface call was not re-run\",\"not run: no pod (not renting another without Nick's go)\",\"partly; Slide and re-run open\")\nwith open(\"results.tsv\",\"a\") as f: f.write(\"\\t\".join(row)+\"\\n\")\nEOF\ngrep -c \"\" results.tsv; tail -n 4 results.tsv | cut -c1-70; grep -n \"cursor-recipe\" ~/.claude/skills/live-blender/SKILL.md | cut -c1-90", "description": "Append results row, verify edits"}`
- tool `SendMessage`: `{"to": "local_3bd59381-07cd-47ec-884c-8460247f8b39", "summary": "Correction: results.tsv row count", "message": "Correction to my last message: the 4th results.tsv row failed to write the first time (my typo); it is appended now, so results.tsv has 4 new cursor rows (cause 1, cause 2, the 13:41 incident, recipe/state).", "type": "message", "recipient": "local_3bd59381-07cd-47ec-884c-8460247f8b39", "recipient_kind": "session", "content": "Correction to my last message: the 4th results.ts…"}`
<details><summary>tool result</summary>

```
53
2026-11-15	CURSOR CAUSE 1 (pass-through event logger inside Blender, s
2026-11-15	CURSOR CAUSE 2 (ffmpeg x11grab of the pod screen mid-stroke
2026-11-15	INCIDENT during experiment: my build call (cursor_harness.p
2026-11-15	CURSOR RECIPE WRITTEN + STATE (cursor session): ~/.claude/s
47:- **Curves sculpt by mouse: read `cursor-recipe.md` first** (15 Nov: the harness sent 3
```
</details>

<details><summary>tool result</summary>

```
{"success":true,"message":"Forwarded to Claude Desktop's session messaging: Message queued for session local_3bd59381-07cd-47ec-884c-8460247f8b39 (\"Mom's hair recreation plan\"): that session is holding it (a turn is in progress there, or its host or process is away) and runs it when that clears. Don't wait on it; check back with list_events if the outcome matters. (delivery: queued; message_id: a4265489-9445-44c1-960a-220ed5c9fd23); not confirmed read — that session may hold it (usually a different permission mode) or refuse it, and this route reports nothing back"}
```
</details>

- tool `mcp__ccd_turn__wrap_up`: `{"recap": "The cursor failure was two harness bugs (31 clicks instead of one drag, strands built off screen). With both fixed, six brushes move hair by real mouse, and the recipe is in cursor-recipe.md. Slide, Add by drag, the real hair layers and a re-run of the edited harness were not tested because the pod is now down.", "ask": "Rent a pod to finish Slide and re-run the harness?", "actions": [{"label": "Not now"}, {"label": "Yes, rent pod"}]}`
<details><summary>tool result</summary>

```
Shown in the next-step box. Do not call wrap_up again this turn; the advice that follows is for your next call. recap is two or three sentences (about 300 characters); this one ran 312. Keep it to what is now true and where it stands. Your closing message is your answer to the user: write it now, in full, as the last thing you say this turn. The box asks your question, so do not ask it again.
```
</details>


### CLAUDE 2026-11-16T08:31

**Why the cursor failed.** Two bugs in our harness, not in Blender. With both fixed, real held mouse drags move hair in Curves Sculpt Mode. The recipe is written at `~/.claude/skills/live-blender/cursor-recipe.md`.

**The two bugs:**
- `harness.sh` turned the 31-point stroke into 31 separate clicks. An event logger inside Blender showed 31 presses; after the fix it shows 1.
- `TestHair` was built in world coordinates under a parent at x=6, so the strands sat at x≈12, off screen.

**Verified on the pod (fresh hair per run, one held drag, brush size 120 px, strength 1.0, 31 points at 0.06 s):**

| Brush | Result |
|---|---|
| Comb | 900 of 3,000 points moved, max 15.21 cm |
| Pull Tips | 33 moved, max 2.45 cm |
| Smooth (wavy strands) | 27 moved, max 0.57 cm |
| Puff | 52 moved, max 0.24 cm |
| Pinch | 43 moved, max 1.27 cm |
| Delete | 300 → 284 curves |

**Not verified:**
- **Slide:** it moved 0 points on strands without surface UVs, and I did not find out why.
- **Other coverage:** Add by drag, and every brush on the real hair layers, were not re-tested. The earlier "0 moved" results there came from the single-click bug, so they are not evidence either way.
- **Harness re-run:** I removed the `snap_curves_to_surface` call from `cursor_harness.py` and have not run it since.
- **Variations:** software versus GPU drawing, VNC viewer attached or not, and UI-menu mode entry were not varied.

**Incident.** The live Blender exited at about 13:41 UTC while handling my build call, the one that added `snap_curves_to_surface`. I can't prove that call caused it. The hair session relaunched Blender with an empty scene. Anything it hadn't saved after `/root/mom_hair_L42.blend` (13:36 UTC) is gone.

**Pod.** `workbench status` now says `WB down`; the idle guard stopped it. I rented nothing and launched nothing. Your "Yes, relaunch" came after the hair session had already relaunched Blender.

**Files:**
- `results.tsv` has 4 new rows.
- `scripts/cursor_harness.py` and `scripts/harness.sh` are fixed.
- `scripts/cursor_evlog.py` and `scripts/cursor_shot.sh` are new.
- The skill's `SKILL.md` now links to the recipe.
- `cursor-findings.md` in the shared notes folder has the details.

**Next experiment:** rent a pod (your call, it costs money), then re-run `scripts/harness.sh "Comb"` and one other brush to confirm the edited harness. After that, test Slide on a throwaway object, never in the shared scene.


### USER 2026-11-16T08:32

Yes, rent pod


### CLAUDE 2026-11-16T08:32

Rent approved. The cost is about $0.89/h, and I'll tell you when it's billing. First I'm reading how the hair session starts it, so I use the same locked recipe.

- tool `Bash`: `{"command": "cd /Users/nick/Desktop/mom-character/live && cat pod_live.sh; echo ----; cat launch_blender.sh | head -30; ssh -o BatchMode=yes nick@37.27.148.115 '~/Desktop/render-desk/bin/workbench status 2>&1 | tail -2; pgrep -fa \"workbench up\" | head -3'", "description": "Read pod launch scripts and status"}`
<details><summary>tool result</summary>

```
#!/bin/bash
# Run ON THE BOX. Rents a workbench GPU pod if none is up (costs money: ask Nick first), copies the projects to it,
# starts Blender on the pod's RTX with a virtual screen + the MCP add-on, and tunnels port 9876 from the box to it,
# so the box's Claude session drives the live Blender. Nothing here depends on the Mac.
#   live/pod_live.sh          set up (or reconnect to) the live Blender
#   live/pod_live.sh tunnel   only reopen the tunnel
# The box's pod-guard.timer stops the pod after 10 idle minutes; every connector command counts as use.
set -u
P="$(cd "$(dirname "$0")/.." && pwd)"
WB="$HOME/Desktop/render-desk/bin/workbench"
STATE="$HOME/.local/share/render-desk/workbench.json"

tunnel() {
  read -r H PORT U < <(python3 -c "import json;print(*json.load(open('$STATE'))['target'])")
  pkill -f "L 127.0.0.1:9876:127.0.0.1:9876" 2>/dev/null
  ssh -f -N -i "$HOME/.ssh/id_ed25519" -p "$PORT" -o StrictHostKeyChecking=accept-new -o UserKnownHostsFile=/dev/null \
      -o LogLevel=ERROR -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 \
      -L 127.0.0.1:9876:127.0.0.1:9876 "$U@$H" && echo "tunnel: box 127.0.0.1:9876 -> pod Blender"
}
[ "${1:-}" = tunnel ] && { tunnel; exit; }

# a pod the guard already stopped still reads "up" in workbench.json: check it answers
if ! { "$WB" status | grep -q "WB up" && timeout 60 "$WB" run true >/dev/null 2>&1; }; then
  "$WB" down >/dev/null 2>&1; "$WB" up || exit 1
fi
"$WB" push "$HOME/Desktop/blender-funnel" >/dev/null && "$WB" push "$P" >/dev/null && echo "projects copied to the pod"
"$WB" run '
  command -v xvfb-run >/dev/null && command -v xdotool >/dev/null || (apt-get update -qq && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y -qq xvfb xdotool libxkbcommon0 libxi6 libxrender1 libsm6 >/dev/null 2>&1)
  dpkg -s virtualgl >/dev/null 2>&1 || (cd /root && wget -q https://github.com/VirtualGL/virtualgl/releases/download/3.1.5/virtualgl_3.1.5_amd64.deb \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ./virtualgl_3.1.5_amd64.deb >/dev/null 2>&1)
  mkdir -p /root/live_snaps; touch /root/.wb_last_use
  if ss -ltn | grep -q 9876; then echo "live Blender already running"; else
    # setsid -f + every fd closed: the ssh session must not wait on Blender (it hung for 10 min on 15 Nov)
    BLENDER=$BLENDER setsid -f '"$P"'/live/launch_blender.sh
    for i in $(seq 1 30); do ss -ltn | grep -q 9876 && break; sleep 2; done
    ss -ltn | grep -q 9876 && echo "live Blender up (GPU-drawn, MCP on 9876)" || { echo "live Blender did not start"; tail -20 /root/live_gui.log; exit 1; }
  fi'
tunnel
----
#!/bin/bash
# Runs ON THE POD: GUI Blender on the RTX (VirtualGL EGL) with a virtual screen and the MCP add-on.
# Fully detached (all fds closed) so the ssh session that started it can end.
exec </dev/null >/root/live_gui.log 2>&1
cd "$(dirname "$0")"
exec xvfb-run --auto-servernum -s "-screen 0 1920x1080x24 +extension GLX" \
     /opt/VirtualGL/bin/vglrun -d egl "$BLENDER" --python start_live.py
WB down
1360911 bash -c ~/Desktop/render-desk/bin/workbench status 2>&1 | tail -2; pgrep -fa "workbench up" | head -3
```
</details>


### CLAUDE 2026-11-16T08:32

I'm running the box's `pod_live.sh` under the lock the skill requires, in the background since renting and setup take a few minutes.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && md5sum live/pod_live.sh live/launch_blender.sh' ; md5 /Users/nick/Desktop/mom-character/live/pod_live.sh /Users/nick/Desktop/mom-character/live/launch_blender.sh; ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && flock /tmp/aow-wb-up.lock live/pod_live.sh' > /private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad/podup.log 2>&1; echo exit $?; tail -15 /private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad/podup.log", "description": "Rent pod and start live Blender under the lock", "timeout": 600000, "run_in_background": true}`
<details><summary>tool result</summary>

```
Command running in background with ID: bb2h7sdbp. Output is being written to: /private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/tasks/bb2h7sdbp.output. You will be notified when it completes — do not poll that file or sleep while waiting. Read the file only if the user asks for progress, or if you need a line it prints before you can go on, such as a server's ready line or port.
```
</details>


### CLAUDE 2026-11-16T08:32

The pod is being rented now, about $0.89/h from here, and I'll wait for the setup to finish.


### USER 2026-11-16T08:34

<task-notification>
<task-id>bb2h7sdbp</task-id>
<tool-use-id>toolu_01VRyoS4yBdWp6yhxHTJws67</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/tasks/bb2h7sdbp.output</output-file>
<status>completed</status>
<summary>Background command "Rent pod and start live Blender under the lock" completed (exit code 0)</summary>
</task-notification>

- tool `Bash`: `{"command": "S=/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4; cat $S/tasks/bb2h7sdbp.output | tail -12; echo ----; tail -15 $S/scratchpad/podup.log", "description": "Read pod startup output"}`
<details><summary>tool result</summary>

```
Blender 5.2.2 LTS
RD_SETUP blender_can_encode: no
NVIDIA GeForce RTX 4090, 24564 MiB
RD_SETUP ready
RD_POD x3ql9921y73vcy NVIDIA GeForce RTX 4090 $0.89/hr
RD_POD status RUNNING
WB up: pod x3ql9921y73vcy NVIDIA GeForce RTX 4090 $0.89/hr; idle stop 10 min, hard stop 5 h
projects copied to the pod
live Blender up (GPU-drawn, MCP on 9876)
tunnel: box 127.0.0.1:9876 -> pod Blender

[exited with code 0]
----
	LC_ALL = (unset),
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
debconf: delaying package configuration, since apt-utils is not installed
Blender 5.2.2 LTS
RD_SETUP blender_can_encode: no
NVIDIA GeForce RTX 4090, 24564 MiB
RD_SETUP ready
RD_POD x3ql9921y73vcy NVIDIA GeForce RTX 4090 $0.89/hr
RD_POD status RUNNING
WB up: pod x3ql9921y73vcy NVIDIA GeForce RTX 4090 $0.89/hr; idle stop 10 min, hard stop 5 h
projects copied to the pod
live Blender up (GPU-drawn, MCP on 9876)
tunnel: box 127.0.0.1:9876 -> pod Blender
```
</details>


### CLAUDE 2026-11-16T08:34

Pod `x3ql9921y73vcy` is up, billing at $0.89/h, with a fresh live Blender on the GPU and the tunnel open. Re-running all brushes with the edited harness.

- tool `Bash`: `{"command": "cd /Users/nick/Desktop/mom-character && for B in \"Comb\" \"Pull Tips\" \"Smooth\" \"Puff\" \"Pinch\" \"Delete\"; do echo \"== $B\"; bash scripts/harness.sh \"$B\" 2>&1 | tail -2; done", "description": "Re-run brushes on the fresh pod", "timeout": 900000}`
<details><summary>tool result</summary>

```
== Comb
PREP Comb activate {'FINISHED'} brush Comb tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Comb points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Pull Tips
PREP Pull Tips activate {'FINISHED'} brush Pull Tips tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Pull Tips points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Smooth
PREP Smooth activate {'FINISHED'} brush Smooth tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Smooth points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Puff
PREP Puff activate {'FINISHED'} brush Puff tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Puff points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Pinch
PREP Pinch activate {'FINISHED'} brush Pinch tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Pinch points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
== Delete
PREP Delete activate {'FINISHED'} brush Delete tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Delete points moved >0.5mm: 0 of 3000 | max cm 0.0 | curves 300 -> 300
```
</details>

- tool `Bash`: `{"command": "S=/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad\nscp -q scripts/cursor_harness.py scripts/cursor_evlog.py scripts/cursor_shot.sh nick@37.27.148.115:Desktop/mom-character/scripts/\nssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && ~/Desktop/render-desk/bin/workbench push ~/Desktop/mom-character >/dev/null 2>&1\npython3 live/bcall.py \"MODE=\\\"start\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_evlog.py\\\").read())\" --timeout 30 2>&1 | tail -1\npython3 live/bcall.py \"MODE=\\\"build\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_harness.py\\\").read())\" --timeout 60 2>&1 | tail -1\npython3 live/bcall.py \"MODE=\\\"prep\\\"\nBRUSH=\\\"Comb\\\"\nON_SURFACE=1\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_harness.py\\\").read())\" --timeout 60 2>&1 | tail -2'\nP=$(python3 -I -c \"print(' '.join('%d,%d'%(789+(912-789)*t/30,619) for t in range(31)))\")\nssh -o BatchMode=yes nick@37.27.148.115 \"cd ~/Desktop/mom-character && STEP=0.1 scripts/cursor_shot.sh '$P' 2>&1 | tail -1; cd ~/Desktop/render-desk && ./bin/workbench pull /root/live_snaps /tmp/cs_snaps >/dev/null 2>&1; cd ~/Desktop/mom-character && python3 live/bcall.py 'MODE=\\\"dump\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_evlog.py\\\").read())' --timeout 30 2>&1 | tail -3 | cut -c1-500\"\nscp -q nick@37.27.148.115:/tmp/cs_snaps/live_snaps/cs_mid.png $S/cs_mid2.png; ls $S", "description": "Screenshot and event log on fresh pod", "timeout": 300000}`
<details><summary>tool result</summary>

```
STROKE [[789, 619], [912, 619]]

shots done
[(('MOUSEMOVE', 'NOTHING'), 32), (('NONE', 'NOTHING'), 3), (('LEFTMOUSE', 'PRESS'), 1), (('LEFTMOUSE', 'RELEASE'), 1)]
[(1794818222.776, 'NONE', 'NOTHING', 912, 460, False), (1794818222.983, 'NONE', 'NOTHING', 912, 460, False), (1794818222.996, 'MOUSEMOVE', 'NOTHING', 912, 460, False), (1794818222.996, 'NONE', 'NOTHING', 912, 460, False), (1794818225.148, 'MOUSEMOVE', 'NOTHING', 789, 460, False), (1794818225.31, 'LEFTMOUSE', 'PRESS', 789, 460, False)] [(1794818228.322, 'MOUSEMOVE', 'NOTHING', 895, 460, False), (1794818228.43, 'MOUSEMOVE', 'NOTHING', 899, 460, False), (1794818228.544, 'MOUSEMOVE', 'NOTHING', 903,

cs_end.png
cs_mid.png
cs_mid2.png
podup.log
```
</details>

- tool `Read`: `{"file_path": "/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad/cs_mid2.png"}`
<details><summary>tool result</summary>

```
[image]
```
</details>

- tool `Bash`: `{"command": "S=/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad\nssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench run \"read D A < <(ps -eo args | awk \\\"\\\\\\$1==\\\\\\\"Xvfb\\\\\\\"{print \\\\\\$2, \\\\\\$NF}\\\" | tail -1); export DISPLAY=\\$D XAUTHORITY=\\$A; xdotool mousemove 300 300; sleep 0.5; xdotool key Escape; sleep 1; ffmpeg -loglevel error -y -f x11grab -video_size 1920x1080 -i \\$DISPLAY -frames:v 1 /root/live_snaps/after_esc.png; echo ok\" 2>&1 | tail -2; ./bin/workbench pull /root/live_snaps /tmp/cs_snaps >/dev/null 2>&1'\nscp -q nick@37.27.148.115:/tmp/cs_snaps/live_snaps/after_esc.png $S/after_esc.png", "description": "Dismiss splash with Escape and screenshot", "timeout": 120000}`
<details><summary>tool result</summary>

```
ok
```
</details>

- tool `Read`: `{"file_path": "/private/tmp/claude-501/-Users-nick-Desktop-mom-character/f82222c4-c333-47fa-9864-2fb07b56e5d4/scratchpad/after_esc.png"}`
<details><summary>tool result</summary>

```
[image]
```
</details>


### CLAUDE 2026-11-16T08:37

The splash is gone and the brush circle is now drawn. Stopping the logger and re-running every brush.

- tool `Bash`: `{"command": "ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/mom-character && python3 live/bcall.py \"MODE=\\\"stop\\\"\nexec(open(\\\"/Users/nick/Desktop/mom-character/scripts/cursor_evlog.py\\\").read())\" --timeout 20 2>&1 | tail -1'; for B in \"Comb\" \"Pull Tips\" \"Smooth\" \"Puff\" \"Pinch\" \"Delete\"; do echo \"== $B\"; bash scripts/harness.sh \"$B\" 2>&1 | tail -2; done", "description": "Re-run brushes after dismissing splash", "timeout": 900000}`
<details><summary>tool result</summary>

```
== Comb
PREP Comb activate {'FINISHED'} brush Comb tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Comb points moved >0.5mm: 58 of 3000 | max cm 10.28 | curves 300 -> 300
== Pull Tips
PREP Pull Tips activate {'FINISHED'} brush Pull Tips tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Pull Tips points moved >0.5mm: 3 of 3000 | max cm 0.2 | curves 300 -> 300
== Smooth
PREP Smooth activate {'FINISHED'} brush Smooth tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Smooth points moved >0.5mm: 27 of 3000 | max cm 0.57 | curves 300 -> 300
== Puff
PREP Puff activate {'FINISHED'} brush Puff tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Puff points moved >0.5mm: 52 of 3000 | max cm 0.24 | curves 300 -> 300
== Pinch
PREP Pinch activate {'FINISHED'} brush Pinch tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Pinch points moved >0.5mm: 57 of 3000 | max cm 1.36 | curves 300 -> 300
== Delete
PREP Delete activate {'FINISHED'} brush Delete tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Delete point count changed 3000 -> 2840 | curves 300 -> 284
```
</details>

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"scripts/cursor_harness.py\"\ns=open(p).read()\nold='    view_front(); print(\"built\", N, \"strands\")'\nassert old in s\nnew='''    if globals().get(\"SURFACE_UV\"):  # surface_uv_coordinate by hand (NOT bpy.ops.curves.snap_curves_to_surface: the live Blender exited right after that call on 15 Nov)\n        from mathutils.bvhtree import BVHTree\n        from mathutils import interpolate\n        bvh = BVHTree.FromObject(sph, bpy.context.evaluated_depsgraph_get()); uvl = sph.data.uv_layers[0].data\n        cd.attributes.new(\"surface_uv_coordinate\", \"FLOAT2\", \"CURVE\"); uv = []\n        for c in range(N):\n            p = Vector(pts[c * per]); loc, nor, fi, dist = bvh.find_nearest(p); poly = sph.data.polygons[fi]\n            vs = [sph.data.vertices[sph.data.loops[li].vertex_index].co for li in poly.loop_indices]\n            wts = interpolate.poly_3d_calc(vs, loc)\n            u = sum(w * uvl[li].uv.x for w, li in zip(wts, poly.loop_indices)); v_ = sum(w * uvl[li].uv.y for w, li in zip(wts, poly.loop_indices)); uv += [u, v_]\n        cd.attributes[\"surface_uv_coordinate\"].data.foreach_set(\"vector\", np.array(uv, np.float32))\n    view_front(); print(\"built\", N, \"strands\", \"uv attr\", \"surface_uv_coordinate\" in cd.attributes)'''\ns=s.replace(old,new)\nold2=\"    cs = bpy.context.tool_settings.curves_sculpt; cs.brush.size = 120\"\nassert old2 in s\ns=s.replace(old2,'    cs = bpy.context.tool_settings.curves_sculpt\\n    if globals().get(\"FALLOFF\"): cs.brush.falloff_shape = FALLOFF\\n    cs.brush.size = 120')\nopen(p,\"w\").write(s)\nh=open(\"scripts/harness.sh\").read()\nh=h.replace('B=\"$1\"; WIG=\"\"; [ \"$B\" = \"Smooth\" ] && WIG=\"WIGGLE=1\"','B=\"$1\"; WIG=\"\"; [ \"$B\" = \"Smooth\" ] && WIG=\"WIGGLE=1\"; [ \"$B\" = \"Slide\" ] && WIG=\"SURFACE_UV=1\"; [ -n \"$FALLOFF\" ] && WIG=\"$WIG\\nFALLOFF=\\\\\"$FALLOFF\\\\\"\"')\nopen(\"scripts/harness.sh\",\"w\").write(h)\nEOF\npython3 -I -c \"import ast;ast.parse(open('scripts/cursor_harness.py').read())\"; grep -n 'WIG=' scripts/harness.sh | cut -c1-230", "description": "Add surface UV and falloff options to harness"}`
<details><summary>tool result</summary>

```
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
AssertionError
7:B="$1"; WIG=""; [ "$B" = "Smooth" ] && WIG="WIGGLE=1"
```
</details>

- tool `Bash`: `{"command": "grep -n \"built\" scripts/cursor_harness.py | cut -c1-160", "description": "Find build print line"}`
<details><summary>tool result</summary>

```
32:    view_front(); print("built", N, "strands", )
```
</details>

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"scripts/cursor_harness.py\"\ns=open(p).read()\nold='    view_front(); print(\"built\", N, \"strands\", )'\nassert old in s\nnew='''    if globals().get(\"SURFACE_UV\"):  # surface_uv_coordinate by hand (NOT bpy.ops.curves.snap_curves_to_surface: the live Blender exited right after that call on 15 Nov)\n        from mathutils.bvhtree import BVHTree\n        from mathutils import interpolate\n        bvh = BVHTree.FromObject(sph, bpy.context.evaluated_depsgraph_get()); uvl = sph.data.uv_layers[0].data\n        cd.attributes.new(\"surface_uv_coordinate\", \"FLOAT2\", \"CURVE\"); uv = []\n        for c in range(N):\n            p = Vector(pts[c * per]); loc, nor, fi, dist = bvh.find_nearest(p); poly = sph.data.polygons[fi]\n            vs = [sph.data.vertices[sph.data.loops[li].vertex_index].co for li in poly.loop_indices]\n            wts = interpolate.poly_3d_calc(vs, loc)\n            u = sum(w * uvl[li].uv.x for w, li in zip(wts, poly.loop_indices)); v_ = sum(w * uvl[li].uv.y for w, li in zip(wts, poly.loop_indices)); uv += [u, v_]\n        cd.attributes[\"surface_uv_coordinate\"].data.foreach_set(\"vector\", np.array(uv, np.float32))\n    view_front(); print(\"built\", N, \"strands\", \"uv attr\", \"surface_uv_coordinate\" in cd.attributes)'''\ns=s.replace(old,new)\nold2=\"    cs = bpy.context.tool_settings.curves_sculpt; cs.brush.size = 120\"\nassert old2 in s\ns=s.replace(old2,'    cs = bpy.context.tool_settings.curves_sculpt\\n    if globals().get(\"FALLOFF\"): cs.brush.falloff_shape = FALLOFF\\n    cs.brush.size = 120')\nopen(p,\"w\").write(s)\nh=open(\"scripts/harness.sh\").read()\nh=h.replace('B=\"$1\"; WIG=\"\"; [ \"$B\" = \"Smooth\" ] && WIG=\"WIGGLE=1\"','B=\"$1\"; WIG=\"\"; [ \"$B\" = \"Smooth\" ] && WIG=\"WIGGLE=1\"; [ \"$B\" = \"Slide\" ] && WIG=\"SURFACE_UV=1\"; [ -n \"$FALLOFF\" ] && WIG=\"$WIG\\nFALLOFF=\\\\\"$FALLOFF\\\\\"\"')\nopen(\"scripts/harness.sh\",\"w\").write(h)\nEOF\npython3 -I -c \"import ast;ast.parse(open('scripts/cursor_harness.py').read())\" && sed -n 7p scripts/harness.sh | cut -c1-260; echo \"== Slide\"; bash scripts/harness.sh Slide 2>&1 | tail -3; echo \"== Comb projected\"; FALLOFF=PROJECTED bash scripts/harness.sh Comb 2>&1 | tail -2", "description": "Patch harness, test Slide and Comb projected", "timeout": 400000}`
<details><summary>tool result</summary>

```
B="$1"; WIG=""; [ "$B" = "Smooth" ] && WIG="WIGGLE=1"; [ "$B" = "Slide" ] && WIG="SURFACE_UV=1"; [ -n "$FALLOFF" ] && WIG="$WIG
== Slide
PREP Slide activate {'FINISHED'} brush Slide tool ? size 120 strength 1.0 falloff SPHERE mode SCULPT_CURVES
RESULT Slide points moved >0.5mm: 920 of 3000 | max cm 52.11 | curves 300 -> 300
== Comb projected
PREP Comb activate {'FINISHED'} brush Comb tool ? size 120 strength 1.0 falloff PROJECTED mode SCULPT_CURVES
RESULT Comb points moved >0.5mm: 915 of 3000 | max cm 15.9 | curves 300 -> 300
```
</details>

- tool `Bash`: `{"command": "for B in \"Add\" \"Pull Tips\" \"Pull Tips\" \"Pinch\" \"Pinch\"; do echo \"== $B\"; bash scripts/harness.sh \"$B\" 2>&1 | tail -1; done", "description": "Run Add and repeat noisy brushes", "timeout": 600000}`
<details><summary>tool result</summary>

```
== Add
RESULT Add point count changed 3000 -> 3048 | curves 300 -> 306
== Pull Tips
RESULT Pull Tips points moved >0.5mm: 3 of 3000 | max cm 0.2 | curves 300 -> 300
== Pull Tips
RESULT Pull Tips points moved >0.5mm: 3 of 3000 | max cm 0.2 | curves 300 -> 300
== Pinch
RESULT Pinch points moved >0.5mm: 57 of 3000 | max cm 1.36 | curves 300 -> 300
== Pinch
RESULT Pinch points moved >0.5mm: 57 of 3000 | max cm 1.36 | curves 300 -> 300
```
</details>


### CLAUDE 2026-11-16T08:43

The new pod's numbers repeat exactly across runs (Pull Tips 3, Pinch 57). Updating the recipe with the splash dialog, the Slide fix and both sets of numbers.

- tool `Bash`: `{"command": "python3 - <<'EOF'\np=\"/Users/nick/.claude/skills/live-blender/cursor-recipe.md\"\ns=open(p).read()\n# header\ns=s.replace(\"Written 15 Nov 2026 by the cursor session, from runs on the pod (Blender 5.2.2, RTX 4090, Xvfb :99 1920x1080, VirtualGL `-d egl`, no window manager).\",\n\"Written 15 Nov 2026 by the cursor session, from runs on two pods (Blender 5.2.2, RTX 4090, Xvfb :99 1920x1080, VirtualGL `-d egl`, no window manager). Pod 1 (first runs), pod 2 (re-run the same evening after the first pod was stopped, fresh Blender).\")\n# third cause\ns=s.replace(\"## Steps that worked\",\"\"\"3. **A fresh Blender shows the splash / Quick Setup dialog and it swallows the mouse.** On pod 2 every brush returned 0 until the dialog was dismissed. Evidence: the event logger saw all 32 moves, the press and the release pass through (nothing consumed them, so no stroke started), and a screen grab showed the Quick Setup dialog and no brush circle. Fix: on a new Blender, before any stroke, `xdotool mousemove 300 300; xdotool key Escape` (Escape closes it without changing settings), then a screen grab should show the brush circle.\n\n## Steps that worked\"\"\",1)\n# table\ni=s.index(\"## Numbers\"); j=s.index(\"## What did NOT matter\")\ntable=\"\"\"## Numbers (fresh hair each run, settings above; points moved > 0.5 mm of 3,000)\n| Brush | Falloff | Pod 1 | Pod 2 (same harness, run twice where noted) |\n|---|---|---|---|\n| Comb | PROJECTED | 900 moved, max 15.21 cm | 915 moved, max 15.9 cm |\n| Comb | SPHERE (the fresh default) | not run | 58 moved, max 10.28 cm |\n| Pull Tips | SPHERE | 33, max 2.45 cm | 3, max 0.2 cm (twice, identical) |\n| Smooth (wavy strands) | SPHERE | 27, max 0.57 cm | 27, max 0.57 cm |\n| Puff | SPHERE | 52, max 0.24 cm | 52, max 0.24 cm |\n| Pinch | SPHERE | 43, max 1.27 cm | 57, max 1.36 cm (twice, identical) |\n| Delete | SPHERE | 300 -> 284 curves | 300 -> 284 curves |\n| Slide (strands with surface UVs) | SPHERE | 0 (no surface UVs) | 920 moved, max 52.11 cm |\n| Add | SPHERE | click only (earlier) | one held drag: 300 -> 306 curves |\nComb needs PROJECTED falloff for a big effect: set `brush.falloff_shape = \"PROJECTED\"` (harness: `FALLOFF=PROJECTED harness.sh Comb`). Pull Tips and Pinch differ between the two pods (33 vs 3, 43 vs 57) and I do not know why; on one pod they repeat exactly. Smooth, Puff, Delete are identical on both. All brushes respond (> 0.5 mm) except that Pull Tips on pod 2 moves only 3 points (0.2 cm) with this short stroke.\n\n## Slide needs surface UVs\nSlide did nothing on strands without `surface_uv_coordinate`. Set it by hand (harness `SURFACE_UV=1`: nearest face by BVH, UV by `mathutils.interpolate.poly_3d_calc` over the polygon loop UVs, a FLOAT2 attribute on the CURVE domain) and Slide moved 920 points. Do NOT use `bpy.ops.curves.snap_curves_to_surface` in the shared live Blender: the live Blender exited right after that call on 15 Nov (cause unproven).\n\n\"\"\"\ns=s[:i]+table+s[j:]\n# not `
<details><summary>tool result</summary>

```
36:Slide did nothing on strands without `surface_uv_coordinate`. Set it by hand
```
</details>


### CLAUDE 2026-11-16T08:43

Recipe updated. Appending the results rows for the pod 2 experiments, then stopping the pod so it stops billing.

- tool `Bash`: `{"command": "python3 - <<'EOF'\nrows=[\n(\"2026-11-15\",\"CURSOR CAUSE 3 (new pod x3ql9921y73vcy after Nick's go, $0.89/h; fresh Blender; scripts/pod_live.sh under the flock): the edited harness gave 0 moved for every brush incl. Comb. Event logger: all 32 moves + press + release passed through (no stroke handler consumed them); screen grab: the Blender splash 'Quick Setup' dialog was open and no brush circle was drawn. Fix: xdotool mousemove 300 300; xdotool key Escape (closes it, no setting changed)\",\"after Escape the brush circle is drawn; every brush responds again (next row)\",\"worked\"),\n(\"2026-11-15\",\"CURSOR RE-RUN ON POD 2 (fresh hair per run, one held drag, size 120 px, strength 1.0, 31 points, STEP 0.06): Comb PROJECTED 915 of 3000 moved (max 15.9 cm); Comb SPHERE (fresh default) 58 (10.28 cm); Pull Tips 3 (0.2 cm, twice identical; pod 1 gave 33); Smooth on wavy strands 27 (0.57 cm); Puff 52 (0.24 cm); Pinch 57 (1.36 cm, twice identical; pod 1 gave 43); Delete 300->284 curves; Add by one held drag 300->306 curves\",\"every brush responds by real mouse; Pull Tips/Pinch differ between pods, cause unknown\",\"worked\"),\n(\"2026-11-15\",\"CURSOR SLIDE: surface_uv_coordinate set by hand (BVH nearest face + poly_3d_calc over loop UVs, harness SURFACE_UV=1; no bpy.ops.curves.snap_curves_to_surface, which preceded the Blender exit at 13:41 UTC)\",\"Slide 920 of 3000 points moved (max 52.11 cm); it did nothing before (strands had no surface UVs)\",\"worked\"),\n]\nwith open(\"results.tsv\",\"a\") as f:\n    for r in rows: f.write(\"\\t\".join(r)+\"\\n\")\nEOF\ntail -n 3 results.tsv | cut -c1-60; ssh -o BatchMode=yes nick@37.27.148.115 'cd ~/Desktop/render-desk && ./bin/workbench pull /root/live_snaps /tmp/cs_snaps >/dev/null 2>&1; ./bin/workbench down 2>&1 | tail -3; ./bin/workbench status 2>&1 | tail -1'", "description": "Append rows, stop the pod", "timeout": 120000}`
<details><summary>tool result</summary>

```
2026-11-15	CURSOR CAUSE 3 (new pod x3ql9921y73vcy after Nick
2026-11-15	CURSOR RE-RUN ON POD 2 (fresh hair per run, one h
2026-11-15	CURSOR SLIDE: surface_uv_coordinate set by hand (
WB down (stopped): 0.19 h, $0.16
WB down
```
</details>

- tool `mcp__ccd_turn__wrap_up`: `{"recap": "Every Curves Sculpt brush I tried (Comb, Pull Tips, Smooth, Puff, Pinch, Delete, Slide, Add) now responds to a real held drag, and the recipe, harness and 7 results rows are saved. The pod is stopped; it billed $0.16."}`
<details><summary>tool result</summary>

```
Nothing is pending, so the app draws no box; the recap is the session's status. Your closing message is your answer to the user: write it now, as the last thing you say this turn.
```
</details>


### CLAUDE 2026-11-16T08:43

The cursor works. Real held mouse drags move hair in Curves Sculpt Mode on the pod, and the recipe is at `~/.claude/skills/live-blender/cursor-recipe.md`. I also stopped the pod: it ran 0.19 h and billed $0.16.

**Why it failed.** There were three causes, none of them in Blender's brushes:
1. **No drag was sent.** The harness turned the 31-point stroke into 31 single clicks, so only Add, which acts on a click, worked.
2. **The test hair was off screen.** The strands were built at x≈12 instead of x≈6, so no brush had anything under it.
3. **A fresh Blender shows a splash "Quick Setup" dialog that swallows the mouse.** The event logger showed no stroke handler taking the events, and a screen grab showed the dialog. Escape closes it without changing settings.

**Measured results.** Each run was fresh hair, one held drag, brush size 120 px, strength 1.0, 31 points at 0.06 s; counts are points moved more than 0.5 mm out of 3,000.

| Brush | Result |
|---|---|
| Comb, PROJECTED falloff | 915 moved, max 15.9 cm (900 on the first pod) |
| Comb, SPHERE falloff (the fresh default) | 58 moved |
| Pull Tips | 3 moved (33 on the first pod) |
| Smooth, wavy strands | 27 moved |
| Puff | 52 moved |
| Pinch | 57 moved (43 on the first pod) |
| Delete | 300 → 284 curves |
| Slide, with surface UVs set by hand | 920 moved, max 52 cm |
| Add, one held drag | 300 → 306 curves |

Comb needs PROJECTED falloff for a big effect. I don't know why Pull Tips and Pinch differ between the two pods; on the second pod each repeated exactly. Slide did nothing until the strands had surface UVs, which I set by hand instead of with `snap_curves_to_surface`.

**Not tested:**
- The real hair layers (434k and 34k points). The earlier zero results there came from the single-click bug, so they prove nothing either way.
- Software versus GPU drawing, a VNC viewer attached or not, and entering the mode through the UI menu.

**Earlier incident.** The live Blender exited at about 13:41 UTC right after my `snap_curves_to_surface` call. The cause is unproven. The hair session relaunched Blender.

**Files:**
- `results.tsv` has 7 new cursor rows.
- `scripts/harness.sh` and `scripts/cursor_harness.py` are fixed and now take `FALLOFF=PROJECTED` and `SURFACE_UV` options.
- `scripts/cursor_evlog.py` and `scripts/cursor_shot.sh` are new debugging tools.
