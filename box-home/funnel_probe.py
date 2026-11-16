"""Probe for run 014: the same scene setup as runs/014-sewn-pants/pants.py, but it prints sizes
and the time of every step and every simulated frame, and renders nothing.
Usage: python funnel_probe.py <frames>"""
import os
import sys
import time

T = time.time()
def say(*a):
    print(f"[{time.time() - T:7.1f} s]", *a, flush=True)

sys.path.insert(0, "/Users/nick/Desktop/blender-funnel")
import bpy  # noqa: E402
from recipes import cloth, human, looks, materials, panels, stage  # noqa: E402
say("imports done")

FRAMES = int(sys.argv[1]) if len(sys.argv) > 1 else 6
S = looks.CURLY_BOY_SLIDERS
scene = stage.new_scene()
base_verts = human.morphed_base(**S)
boy = human.build_human(scene, name="Boy", skin="young_caucasian_male", hair=None, eyes="green",
                        outfit=("shoes05",), collider=True, **S)
say("body built")
col = next(o for o in [boy] + list(boy.children_recursive) if o.name == "Boy_collider")
cloth.make_collider(col, thickness=0.004)
say("collider:", len(col.data.vertices), "verts,", len(col.data.polygons), "faces")
for o in [boy] + list(boy.children_recursive):
    if o.type == "MESH":
        mods = [m.type for m in o.modifiers]
        say(f"  mesh {o.name}: {len(o.data.vertices)} verts, modifiers {mods}")

mat = materials.fabric((0.012, 0.035, 0.17), name="Pants", thread=0.0008, on="object", sheen=0.25)
pants, pinfo = panels.build_trousers(scene, base_verts, name="Pants", material=mat, room=0.03, gap=0.035)
say("pants panels:", pinfo)
mod = cloth.add_cloth(pants, fabric="cotton", spare=-0.05, resolution=0, quality=10,
                      self_distance=float(os.environ.get("SD", 0.015)), sewing_force=20.0)
cs = next(m for m in pants.modifiers if m.type == "CLOTH")
cs.settings.effector_weights.gravity = 0.0
cs.collision_settings.collision_quality = int(os.environ.get("CQ", 15))
cs.settings.quality = int(os.environ.get("Q", 10))
cs.collision_settings.use_self_collision = os.environ.get("SELF", "1") == "1"
if os.environ.get("NOBODY") == "1":
    col.modifiers.remove(next(m for m in col.modifiers if m.type == "COLLISION"))
say("pants modifiers:", [m.type for m in pants.modifiers],
    "| quality", cs.settings.quality, "| collision quality", cs.collision_settings.collision_quality,
    "| self collision", cs.collision_settings.use_self_collision, "| self distance", cs.collision_settings.self_distance_min)
scene.frame_start, scene.frame_end = 1, FRAMES
cs.point_cache.frame_start, cs.point_cache.frame_end = 1, FRAMES
for f in range(1, FRAMES + 1):
    t0 = time.time()
    scene.frame_set(f)
    say(f"frame {f}: {time.time() - t0:.1f} s")
say("DONE")
