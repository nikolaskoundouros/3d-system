"""Probe switches for the T-shirt's shape: wider neck, wider sleeves without the puffed caps,
a lower hem, and the modelled fold texture back at a chosen strength."""
p = "/Users/nick/probe013/run/outfit_probe.py"
s = open(p).read()
anchor = 'if env("CHEST", 0.0):   # probe: a bigger chest'
assert s.count(anchor) == 1, "chest anchor missing"
if "NECK_OPEN" not in s:
    s = s.replace(anchor, '''if env("NECK_OPEN", 0.0):   # probe: widen the neckline (clothing layer only)
    EDITS.append(sculpt.clothes(sculpt.scale("neck", 0.075, env("NECK_OPEN", 0.0))))
if env("SLEEVE_SCALE", 0.0):   # probe: wider sleeves, scaled instead of inflated (no puffed cap)
    EDITS.append(sculpt.clothes(sculpt.scale(("shoulder.L", (0.06, 0.0, -0.03)), 0.12, env("SLEEVE_SCALE", 0.0), mirror=True)))
if env("HEM_DROP", 0.0):   # probe: lower the shirt hem
    EDITS.append(sculpt.clothes(sculpt.grab(("hips", (0.0, 0.0, 0.07)), 0.16, (0.0, 0.0, -env("HEM_DROP", 0.0)))))
print("SHAPE edits", len(EDITS), flush=True)
''' + anchor)
old = '    if env("NO_NORMALMAP", 0):   # probe: drop the modelled fold texture (it shows as blotches)\n'
assert s.count(old) == 1, "normal map anchor missing"
if "NORMAL_STRENGTH" not in s:
    s = s.replace(old, '''    if env("NORMAL_STRENGTH", -1.0) >= 0.0:   # probe: keep the fold texture, at this strength
        for nm in [n for n in tmat.node_tree.nodes if n.type == "NORMAL_MAP"]:
            nm.inputs["Strength"].default_value = env("NORMAL_STRENGTH", 1.0)
            print("NORMAL strength", nm.inputs["Strength"].default_value, flush=True)
''' + old)
open(p, "w").write(s)
print("shape switches ready")
