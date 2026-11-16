p = "/Users/nick/probe013/run/outfit_probe.py"
s = open(p).read()
a = 'views["ref00"] = ((0.10, -1.55, top * 0.86), (0.0, 0.0, top * 0.72), 55.0)'
b = 'views["ref58"] = ((0.95, -2.35, top * 0.95), (0.0, 0.0, top * 0.62), 50.0)'
assert s.count(a) == 1 and s.count(b) == 1
s = s.replace(a, 'views["ref00"] = ((0.08, -1.05, top * 0.90), (0.0, 0.0, top * 0.78), 55.0)')
s = s.replace(b, 'views["ref58"] = ((0.70, -1.45, top * 0.98), (0.0, 0.0, top * 0.70), 50.0)')
open(p, "w").write(s); print("views moved closer")
