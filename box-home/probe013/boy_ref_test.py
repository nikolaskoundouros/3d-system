"""One still of the boy built with look="ref", to check the recipe port. Usage: python boy_ref_test.py OUT.png [taubin]"""
import os, sys, time
sys.path.insert(0, "/Users/nick/Desktop/blender-funnel")
import bpy
from recipes import camera, characters, color, lighting, render, stage, world
t0 = time.time()
scene = stage.new_scene()
taubin = int(sys.argv[2]) if len(sys.argv) > 2 else 6
boy, _ = characters.curly_boy(scene, hair_children=20000, hang={"SHIRT_TAUBIN": taubin})
print("BUILD", round(time.time() - t0, 1), "s", flush=True)
world.sky_world(scene, sun_elevation_deg=40.0, sun_rotation_deg=220.0, strength=0.006)
mid = stage.empty_at(scene, "Mid", (0.0, 0.0, 0.85))
lighting.three_point(scene, mid, (-0.6, -3.5, 1.2), key_power=260.0, fill_ratio=0.35, rim_ratio=1.2, distance=3.5, key_size=1.8)
color.set_view(scene, "AgX", look="Medium High Contrast")
scene.cycles_curves.shape = "THICK"
render.cycles_cpu(scene, width=360, height=540, samples=12)
camera.camera_at(scene, (0.08, -1.05, 1.35), stage.empty_at(scene, "Aim", (0.0, 0.0, 1.15)), lens=55.0)
render.render_to(scene, sys.argv[1])
print("DONE", round(time.time() - t0, 1), "s", flush=True)
