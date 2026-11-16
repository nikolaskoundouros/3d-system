p = "/Users/nick/probe013/run/outfit_probe.py"
s = open(p).read()
old = 'CUT = {"thigh": 0.088, "knee": 0.074, "ankle": 0.062,'
assert s.count(old) == 1, "cut line not found"
s = s.replace(old, 'CUT = {"thigh": float(os.environ.get("PANT_THIGH", 0.088)), "knee": float(os.environ.get("PANT_KNEE", 0.074)), '
                   '"ankle": float(os.environ.get("PANT_ANKLE", 0.062)),')
open(p, "w").write(s); print("pants cut switchable")
