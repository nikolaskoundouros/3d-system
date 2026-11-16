"""Hooks tee_hang.apply into the probe copy of outfit.py, right before the render settings."""
p = "/Users/nick/probe013/run/outfit_probe.py"
s = open(p).read()
anchor = "render.cycles_cpu(scene, width=W, height=H, samples=SAMPLES)\n"
assert s.count(anchor) == 1, "render anchor not found once"
if "tee_hang" not in s:
    hook = '''if env("HANG", 0):   # probe: reshape the shirt like the reference (tee_hang.py, no simulation)
    sys.path.insert(0, HERE)
    import tee_hang  # noqa: E402
    _marks = sculpt.landmarks(human.to_blender(base_verts))
    _kids = list(boy.children_recursive)
    tee_hang.apply(scene, next(o for o in _kids if o.name == "Boy_tee"), boy if boy.type == "ARMATURE" else None,
                   body, [o for o in _kids if o.name in ("Boy_pants", "Boy_stripe")],
                   float(_marks["chest"][2]), TEE, env)
'''
    s = s.replace(anchor, hook + anchor)
    open(p, "w").write(s)
print("hang hook ready")
