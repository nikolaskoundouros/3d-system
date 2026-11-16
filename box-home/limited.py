"""Run a command with a hard time limit: python3 limited.py <seconds> <cmd...>. Exit 124 when it had to be killed."""
import os, signal, subprocess, sys
p = subprocess.Popen(sys.argv[2:], start_new_session=True)
try:
    sys.exit(p.wait(timeout=float(sys.argv[1])))
except subprocess.TimeoutExpired:
    os.killpg(p.pid, signal.SIGKILL)
    print("LIMIT hit after", sys.argv[1], "s", flush=True)
    sys.exit(124)
