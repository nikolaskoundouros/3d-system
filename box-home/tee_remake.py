"""Remake of the pro T-shirt from "Noob vs PRO Realistic Clothes in Blender" (owner-supplied short).

Steps as seen in the video (frames read 1 per second, panels at full size, 13 Nov 2026):
  0:06-0:11  cube flattened, loop cuts: 3 across (header "Cuts: 3") and 3 down -> 4 x 4 grid on the front
  0:12-0:14  top-row side faces extruded along normals, header "Shrink/Fatten: 0.4290 m" -> sleeves
  0:15-0:22  bottom faces deleted (open hem), middle top faces deleted (neck), V notch at the front
  0:23-0:24  Ctrl+2 / Ctrl+3: Subdivision Surface, level 3, before the cloth
  0:25-0:49  a second object shaped to sit inside the collar, with Subdivision 2 -> Collision (0:52)
  0:54-0:59  Cloth on the shirt: Quality Steps 5, rest default; Self Collisions on, friction 5, distance 0.015 m
  1:02       played: the shirt hangs from the collar piece
  1:08-1:11  at frame 54 the modifiers are applied, then Subdivision (viewport 1, render 2) on top
Sizes of the box and of the collar piece are NOT shown in the video; the numbers below marked EST are mine.
Usage: python tee_remake.py <out_dir>
"""
import math
import os
import sys
import time

import bpy  # must come first: the bpy module provides bmesh
import bmesh

OUT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else sys.argv[1]
os.makedirs(OUT, exist_ok=True)
T0 = time.time()
def say(*a):
    print(f"[{time.time() - T0:7.1f} s]", *a, flush=True)

W, H, D = 1.40, 1.50, 0.36          # EST: shirt box width, height, depth (m)
SLEEVE = 0.429                       # video 0:13
COLS, ROWS = 4, 4                    # video 0:07-0:11

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

# ---- the shirt box: a closed box built as quads on a COLS x ROWS front/back grid
bm = bmesh.new()
xs = [-W / 2 + W * i / COLS for i in range(COLS + 1)]
zs = [H * j / ROWS for j in range(ROWS + 1)]
ys = (-D / 2, D / 2)
grid = {}
def v(x, y, z):
    key = (round(x, 5), round(y, 5), round(z, 5))
    if key not in grid:
        grid[key] = bm.verts.new(key)
    return grid[key]
def quad(a, b, c, d):
    return bm.faces.new((a, b, c, d))
faces = {}
for j in range(ROWS):
    for i in range(COLS):
        faces[("front", i, j)] = quad(v(xs[i], ys[0], zs[j]), v(xs[i + 1], ys[0], zs[j]), v(xs[i + 1], ys[0], zs[j + 1]), v(xs[i], ys[0], zs[j + 1]))
        faces[("back", i, j)] = quad(v(xs[i + 1], ys[1], zs[j]), v(xs[i], ys[1], zs[j]), v(xs[i], ys[1], zs[j + 1]), v(xs[i + 1], ys[1], zs[j + 1]))
    faces[("left", j)] = quad(v(xs[0], ys[1], zs[j]), v(xs[0], ys[0], zs[j]), v(xs[0], ys[0], zs[j + 1]), v(xs[0], ys[1], zs[j + 1]))
    faces[("right", j)] = quad(v(xs[-1], ys[0], zs[j]), v(xs[-1], ys[1], zs[j]), v(xs[-1], ys[1], zs[j + 1]), v(xs[-1], ys[0], zs[j + 1]))
for i in range(COLS):
    if i in (1, 2):
        continue                                          # neck: middle top faces deleted (0:18)
    faces[("top", i)] = quad(v(xs[i], ys[0], zs[-1]), v(xs[i + 1], ys[0], zs[-1]), v(xs[i + 1], ys[1], zs[-1]), v(xs[i], ys[1], zs[-1]))
# bottom faces are never made: open hem (0:16-0:17)

# sleeves: extrude the top-row side faces outwards by SLEEVE, then delete the end caps (open cuffs)
for side, sgn in (("left", -1), ("right", 1)):
    f = faces[(side, ROWS - 1)]
    ret = bmesh.ops.extrude_face_region(bm, geom=[f])
    new_verts = [e for e in ret["geom"] if isinstance(e, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, verts=new_verts, vec=(sgn * SLEEVE, 0.0, 0.0))
    cap = [e for e in ret["geom"] if isinstance(e, bmesh.types.BMFace)]
    bmesh.ops.delete(bm, geom=[f] + cap, context="FACES_ONLY")

# V notch at the front of the neck (0:20): lower the front-top middle vertex
mid = min((vv for vv in bm.verts if abs(vv.co.y - ys[0]) < 1e-4 and abs(vv.co.z - zs[-1]) < 1e-4), key=lambda vv: abs(vv.co.x))
mid.co.z -= 0.14                     # EST notch depth
bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
me = bpy.data.meshes.new("Shirt")
bm.to_mesh(me); bm.free()
shirt = bpy.data.objects.new("Shirt", me)
scene.collection.objects.link(shirt)
for p in me.polygons:
    p.use_smooth = True
sub = shirt.modifiers.new("Subdivision", "SUBSURF"); sub.levels = 3; sub.render_levels = 3   # 0:23 Ctrl+3
say("shirt base:", len(me.vertices), "verts,", len(me.polygons), "faces")

# ---- collar piece: a rounded flat oval inside the shoulders, under the smoothed shirt's top (EST size).
# Placed from the subdivided shirt itself: the first try (0.84 m wide, from the box numbers) let the
# shirt slide through, because subdivision pulls the shoulders in and down.
dg0 = bpy.context.evaluated_depsgraph_get()
sv = [vv.co.copy() for vv in shirt.evaluated_get(dg0).data.vertices]
inner_top = min(c.z for c in sv if abs(c.x) < 0.45 and abs(c.y) < 0.06 and abs(c.x) > 0.22 and c.z > H * 0.7)
half_depth = min(abs(c.y) for c in sv if abs(c.x) < 0.4 and c.z > H * 0.5 and c.z < H * 0.8)
say(f"smoothed shirt: top over the shoulders z={inner_top:.3f}, half depth={half_depth:.3f}, bounds z {min(c.z for c in sv):.3f}..{max(c.z for c in sv):.3f}")
CH = float(os.environ.get("CH", 0.05))
CZ = inner_top - 0.035 - CH
CW = float(os.environ.get("CW", 0.52))          # half width
# video 0:49: the collar piece is a cube with a Subdivision modifier (levels 2), then Collision (0:52)
bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0.0, 0.0, CZ))
collar = bpy.context.object
collar.name = "CollarPiece"
collar.scale = (CW, half_depth - 0.04, CH)     # EST size, just inside front and back
say(f"collar piece: centre z={CZ:.3f}, size {2 * CW:.2f} x {2 * (half_depth - 0.04):.2f} x {2 * CH:.2f} m (cube + subdivision 2)")
bpy.ops.object.transform_apply(scale=True)
csub = collar.modifiers.new("Subdivision", "SUBSURF"); csub.levels = csub.render_levels = 2
collar.modifiers.new("Collision", "COLLISION")
collar.collision.thickness_outer = float(os.environ.get("TO", 0.02))

# ---- cloth, as on the panels at 0:54-0:59
cloth = shirt.modifiers.new("Cloth", "CLOTH")
cs = cloth.settings
cs.quality = 5
cc = cloth.collision_settings
cc.use_self_collision = True
cc.self_friction = 5.0
cc.self_distance_min = 0.015
cc.collision_quality = int(os.environ.get("CQ", cc.collision_quality))
say("cloth: quality", cs.quality, "mass", round(cs.mass, 3), "tension", cs.tension_stiffness, "shear", cs.shear_stiffness,
    "bending", cs.bending_stiffness, "| collision quality", cc.collision_quality, "| self", cc.use_self_collision, cc.self_distance_min)
dg = bpy.context.evaluated_depsgraph_get()
ev = shirt.evaluated_get(dg)
say("shirt simulated mesh:", len(ev.data.vertices), "verts")

# ---- look: grey clay like the tutorial viewport
mat = bpy.data.materials.new("Clay"); mat.use_nodes = True
b = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
b.inputs["Base Color"].default_value = (0.62, 0.62, 0.62, 1.0); b.inputs["Roughness"].default_value = 0.8
shirt.data.materials.append(mat)
world = bpy.data.worlds.new("W"); scene.world = world; world.use_nodes = True
bg = next(n for n in world.node_tree.nodes if n.type == "BACKGROUND")
bg.inputs["Color"].default_value = (0.05, 0.05, 0.05, 1.0); bg.inputs["Strength"].default_value = 1.0
bpy.ops.object.light_add(type="AREA", location=(-2.5, -3.0, 3.0)); key = bpy.context.object
key.data.energy = 900; key.data.size = 3.0
key.rotation_euler = (math.radians(50), 0, math.radians(-40))
bpy.ops.object.light_add(type="AREA", location=(3.0, -1.5, 1.5)); fill = bpy.context.object
fill.data.energy = 250; fill.data.size = 3.0
fill.rotation_euler = (math.radians(70), 0, math.radians(60))
bpy.ops.object.camera_add(location=(-2.6, -4.6, 1.6)); cam = bpy.context.object
scene.camera = cam
tgt = bpy.data.objects.new("Aim", None); scene.collection.objects.link(tgt); tgt.location = (0, 0, 0.65)
con = cam.constraints.new("TRACK_TO"); con.target = tgt; con.track_axis = "TRACK_NEGATIVE_Z"; con.up_axis = "UP_Y"
cam.data.lens = 45
scene.render.engine = "CYCLES"; scene.cycles.device = "CPU"; scene.cycles.samples = 48; scene.cycles.use_denoising = True
scene.render.resolution_x, scene.render.resolution_y = 720, 960
scene.view_settings.view_transform = "AgX"
collar.hide_render = True

def shoot(name):
    scene.render.filepath = os.path.join(OUT, name)
    bpy.ops.render.render(write_still=True)
    say("saved", name)

scene.frame_start, scene.frame_end = 1, 54
cloth.point_cache.frame_start, cloth.point_cache.frame_end = 1, 54
scene.frame_set(1)
if not (os.environ.get("NOSHOT") or os.environ.get("SKIP1")): shoot("tee_step1_shape.png")
for f in range(2, 55):
    t = time.time(); scene.frame_set(f)
    if f % 6 == 0 or f in (2, 3):
        zz = [vv.co.z for vv in shirt.evaluated_get(bpy.context.evaluated_depsgraph_get()).data.vertices]
        say(f"frame {f}: {time.time() - t:.1f} s, shirt z {min(zz):.2f}..{max(zz):.2f}")

# 1:08-1:11: apply at frame 54, then Subdivision viewport 1 / render 2 on top
dg = bpy.context.evaluated_depsgraph_get()
final = bpy.data.meshes.new_from_object(shirt.evaluated_get(dg))
shirt.modifiers.clear()
shirt.data = final
for p in final.polygons:
    p.use_smooth = True
top = shirt.modifiers.new("Subdivision", "SUBSURF"); top.levels = 1; top.render_levels = 2
shirt.data.materials.clear(); shirt.data.materials.append(mat)
say("draped mesh:", len(final.vertices), "verts")
if os.environ.get("NOSHOT"):
    say("DONE"); sys.exit(0)
shoot("tee_step2_draped.png")
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "tee_remake.blend"))
say("DONE")
