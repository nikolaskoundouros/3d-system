p = "/Users/nick/probe013/run/outfit_probe.py"
s = open(p).read()
old = 'EDITS.append(sculpt.clothes(sculpt.scale("neck", 0.075, env("NECK_OPEN", 0.0))))'
assert s.count(old) == 1
s = s.replace(old, 'EDITS.append(sculpt.clothes(sculpt.scale(("neck", (0.0, 0.0, -env("NECK_DOWN", 0.0))), env("NECK_R", 0.075), env("NECK_OPEN", 0.0))))')
open(p, "w").write(s); print("neck centre switchable")
