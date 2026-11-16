"""Adds two camera views matched to the reference clip to the probe copy of outfit.py."""
p = "/Users/nick/probe013/run/outfit_probe.py"
s = open(p).read()
old = 'names = os.environ.get("VIEWS", "full,side,back,upper").split(",")\n'
assert s.count(old) == 1, "VIEWS line not found once"
if 'views["ref58"]' not in s:
    new = ('# probe: views matched to the reference clip (front close-up at 0:00, three-quarter at 0:58)\n'
           'views["ref00"] = ((0.10, -1.55, top * 0.86), (0.0, 0.0, top * 0.72), 55.0)\n'
           'views["ref58"] = ((0.95, -2.35, top * 0.95), (0.0, 0.0, top * 0.62), 50.0)\n') + old
    s = s.replace(old, new)
    open(p, "w").write(s)
print("views ready")
