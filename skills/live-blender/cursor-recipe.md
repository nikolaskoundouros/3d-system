# Cursor (real mouse) in Curves Sculpt: verified recipe

Written 15 Nov 2026 by the cursor session, from runs on two pods (Blender 5.2.2, RTX 4090, Xvfb :99 1920x1080, VirtualGL `-d egl`, no window manager). Pod 1 (first runs), pod 2 (re-run the same evening after the first pod was stopped, fresh Blender).
Project files: `~/Desktop/mom-character/scripts/cursor_harness.py`, `harness.sh`, `cursor_evlog.py`, `cursor_shot.sh`; rows in `results.tsv`.

## Why it "did not work" (both causes were in our harness, not in Blender)
1. **No drag was ever sent.** `harness.sh` ran `eval live/drag.sh $ARGS` over ssh. The remote shell strips the quotes, eval re-splits, and the 31 points became 31 separate strokes (move, wait 0.15 s, press, release). An event logger inside Blender showed 31 LEFTMOUSE PRESS events, one per move. Add acts on a single click, so it "worked"; every brush that needs motion did nothing. Fix: pass all points as ONE single-quoted argument and do not use `eval`:
   `ssh box "cd ~/Desktop/mom-character && STEP=0.06 live/drag.sh '$POINTS'"`. After the fix the log shows exactly 1 press.
2. **The hair was not under the brush.** The test strands were built in world coordinates (x about 6) while `TestHair` is parented to `TestSphere` at x=6 (identity parent inverse), so world = 6 + local put them at x about 12, off screen. A screen grab mid-stroke showed the brush circle and no strands. Fix: build the strand points LOCAL to the sphere (`root = v * 0.12`). General rule: strand positions are in the hair object's space; if it has a parent, add the parent's transform.

3. **A fresh Blender shows the splash / Quick Setup dialog and it swallows the mouse.** On pod 2 every brush returned 0 until the dialog was dismissed. Evidence: the event logger saw all 32 moves, the press and the release pass through (nothing consumed them, so no stroke started), and a screen grab showed the Quick Setup dialog and no brush circle. Fix: on a new Blender, before any stroke, `xdotool mousemove 300 300; xdotool key Escape` (Escape closes it without changing settings), then a screen grab should show the brush circle.

## Steps that worked (one command: `scripts/harness.sh "<Brush name>"`)
1. Build fresh `TestSphere` (radius 0.12 at x=6) and `TestHair` (300 strands, 10 points each, 0.30 m long, local coordinates), front orthographic view, view location (6, 0, 0.25), distance 1.6. Rebuild before EVERY brush: an earlier brush moves the strands and ruins the next measurement.
2. Select `TestHair`, `bpy.ops.object.mode_set(mode="SCULPT_CURVES")`, inside `temp_override(window, area, region)`.
3. Activate the brush: `bpy.ops.brush.asset_activate(asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-curve_sculpt.blend/Brush/<name>')`. Brush size 120 px (`brush.size` and `unified_paint_settings.size`), strength 1.0.
4. Screen point from Blender: X = region.x + mx, Y = window.height - (region.y + my) (`location_3d_to_region_2d`). Stroke here: 789,619 to 912,619 (about 123 px, starting on the sphere surface), 31 points, `STEP=0.06` s between points.
5. ONE held drag: `xdotool mousemove` to the first point, wait 0.15 s, `mousedown 1`, `mousemove` through the rest, `mouseup 1` (`live/drag.sh "x,y x,y ..."`, one argument). No `windowactivate` first (the first press after it is swallowed).
6. Wait 4 s, leave the mode (`mode_set(mode="OBJECT")`), THEN read the positions and compare with a copy taken before the stroke.

## Numbers (fresh hair each run, settings above; points moved > 0.5 mm of 3,000)
| Brush | Falloff | Pod 1 | Pod 2 (same harness, run twice where noted) |
|---|---|---|---|
| Comb | PROJECTED | 900 moved, max 15.21 cm | 915 moved, max 15.9 cm |
| Comb | SPHERE (the fresh default) | not run | 58 moved, max 10.28 cm |
| Pull Tips | SPHERE | 33, max 2.45 cm | 3, max 0.2 cm (twice, identical) |
| Smooth (wavy strands) | SPHERE | 27, max 0.57 cm | 27, max 0.57 cm |
| Puff | SPHERE | 52, max 0.24 cm | 52, max 0.24 cm |
| Pinch | SPHERE | 43, max 1.27 cm | 57, max 1.36 cm (twice, identical) |
| Delete | SPHERE | 300 -> 284 curves | 300 -> 284 curves |
| Slide (strands with surface UVs) | SPHERE | 0 (no surface UVs) | 920 moved, max 52.11 cm |
| Add | SPHERE | click only (earlier) | one held drag: 300 -> 306 curves |
Comb needs PROJECTED falloff for a big effect: set `brush.falloff_shape = "PROJECTED"` (harness: `FALLOFF=PROJECTED harness.sh Comb`). Pull Tips and Pinch differ between the two pods (33 vs 3, 43 vs 57) and I do not know why; on one pod they repeat exactly. Smooth, Puff, Delete are identical on both. All brushes respond (> 0.5 mm) except that Pull Tips on pod 2 moves only 3 points (0.2 cm) with this short stroke.

## Slide needs surface UVs
Slide did nothing on strands without `surface_uv_coordinate`. Set it by hand (harness `SURFACE_UV=1`: nearest face by BVH, UV by `mathutils.interpolate.poly_3d_calc` over the polygon loop UVs, a FLOAT2 attribute on the CURVE domain) and Slide moved 920 points. Do NOT use `bpy.ops.curves.snap_curves_to_surface` in the shared live Blender: the live Blender exited right after that call on 15 Nov (cause unproven).

## What did NOT matter (shown by the runs)
- Step pause 0.06 s versus 0.1 s: same Pull Tips result.
- Reading after leaving the mode: needed, and we did it, but it was not the cause.
- Pod-side mouse delivery: it was fine all along (`xdotool` positions and presses reached Blender).
- A ffmpeg screen grab taken mid-stroke (`ffmpeg -f x11grab`, about 0.5 s) did not disturb the stroke.

## Not tested, so not known
- Every brush on the real hair layers (434k and 34k points). Earlier "0 moved" results there came from the single-click bug, so they are not evidence either way.
- Software versus GPU drawing, VNC viewer attached or not, mode entered through the UI menu, toolbar tool set: none were varied (pod 2 ran GPU-drawn with no viewer attached and worked).
- Why Pull Tips and Pinch differ between the pods.
- Pod 2's default scene still had Camera, Cube and Light; the harness does not touch them.

## Tools for debugging
- `scripts/cursor_evlog.py MODE="start"/"dump"`: a pass-through modal operator that logs events Blender sees (events the stroke handler consumes do not show; that is itself a sign the stroke is running).
- `scripts/cursor_shot.sh "x,y x,y ..."` (run on the box): the same held drag with screen grabs mid-stroke and after release, to `/root/live_snaps/cs_mid.png` and `cs_end.png`; pull with `workbench pull /root/live_snaps DIR`.
