"""Export Claude Code chat transcripts into this repo: images removed, secrets blanked.
Usage: python3 tools/export_conversations.py SECRETS_FILE OUT_DIR TRANSCRIPT.jsonl [TRANSCRIPT.jsonl ...]
SECRETS_FILE: one known secret value per line (kept outside the repo). Each transcript becomes
OUT_DIR/<date>_<title>/transcript.md (readable) + raw.jsonl.gz (every line, images removed) + subagents/*.jsonl.gz."""
import gzip, json, os, re, sys

PATTERNS = [
    r"rpa_[A-Za-z0-9]{20,}", r"sk-ant-[A-Za-z0-9_\-]{20,}", r"\bsk-[A-Za-z0-9]{32,}",
    r"gh[pousr]_[A-Za-z0-9]{30,}", r"github_pat_[A-Za-z0-9_]{30,}", r"xox[abpr]-[A-Za-z0-9\-]{10,}",
    r"AKIA[0-9A-Z]{16}", r"AIza[0-9A-Za-z_\-]{35}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----",
]
KV = re.compile(r"(?i)((?:api[_-]?key|access[_-]?token|auth[_-]?token|secret|password|bearer)[\"']?\s*[=:]?\s*[\"']?)([A-Za-z0-9_\-\.]{20,})")

# Names of Nick's non-Blender work and his account names, blanked so this repo holds only the Blender projects.
# One regex per line in ~/.config/3d-system/blank-names.txt (kept outside the repo on purpose).
_NAMES = os.path.expanduser("~/.config/3d-system/blank-names.txt")
OTHER = re.compile("(?i)" + "|".join(l.strip() for l in open(_NAMES) if l.strip())) if os.path.exists(_NAMES) else None
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@(gmail|googlemail|icloud|me|outlook|hotmail|yahoo|[a-z0-9-]+)\.[a-z.]+", re.I)
# App context bolted onto every chat (skill lists, injected instructions, raw API request copies): not the conversation.
DROP_TYPES = {"api-request-blob"}
DROP_ATTACHMENTS = {"skill_listing", "instructions", "deferred_tools_delta", "mcp_instructions_delta", "agent_listing_delta"}

def load_secrets(path):
    return sorted({l.strip() for l in open(path) if len(l.strip()) >= 12}, key=len, reverse=True)

def redact(s, secrets):
    for v in secrets:
        if v in s: s = s.replace(v, "[REDACTED]")
    for p in PATTERNS: s = re.sub(p, "[REDACTED]", s)
    s = KV.sub(lambda m: m.group(1) + "[REDACTED]", s)
    s = EMAIL.sub("[email]", s)
    return OTHER.sub("[other project]", s) if OTHER else s

def dropped(d):
    if d.get("type") in DROP_TYPES: return True
    a = d.get("attachment")
    return d.get("type") == "attachment" and isinstance(a, dict) and a.get("type") in DROP_ATTACHMENTS

def strip_images(o):
    if isinstance(o, dict):
        if o.get("type") == "base64" and "data" in o:
            return {**o, "data": f"[image removed, {len(o['data'])} base64 chars]"}
        return {k: strip_images(v) for k, v in o.items()}
    if isinstance(o, list): return [strip_images(x) for x in o]
    if isinstance(o, str) and len(o) > 100000 and re.fullmatch(r"[A-Za-z0-9+/=\s]+", o[:2000]):
        return f"[binary blob removed, {len(o)} chars]"
    return o

def text_of(c, limit):
    if isinstance(c, str): return c[:limit] + (" ...[cut]" if len(c) > limit else "")
    out = []
    for x in c or []:
        if not isinstance(x, dict): continue
        if x.get("type") == "text": out.append(x["text"])
        elif x.get("type") == "image": out.append("[image]")
    s = "\n".join(out)
    return s[:limit] + (" ...[cut]" if len(s) > limit else "")

def export(src, out_root, secrets):
    title, first, lines, md = None, None, [], []
    with open(src, errors="replace") as f:
        for line in f:
            try: d = json.loads(line)
            except Exception: continue
            t = d.get("type")
            if t == "custom-title": title = d.get("customTitle") or title
            elif t == "ai-title" and not title: title = d.get("aiTitle")
            first = first or d.get("timestamp")
            if dropped(d): continue
            d = strip_images(d)
            lines.append(redact(json.dumps(d, ensure_ascii=False), secrets))
            m = d.get("message") or {}; c = m.get("content"); ts = (d.get("timestamp") or "")[:16]
            side = " (subagent)" if d.get("isSidechain") else ""
            if t == "user":
                if isinstance(c, list) and any(isinstance(x, dict) and x.get("type") == "tool_result" for x in c):
                    for x in c:
                        if isinstance(x, dict) and x.get("type") == "tool_result":
                            md.append(f"<details><summary>tool result{side}</summary>\n\n```\n{text_of(x.get('content'), 4000)}\n```\n</details>\n")
                else:
                    md.append(f"\n### USER {ts}{side}\n\n{text_of(c, 20000)}\n")
            elif t == "assistant":
                for x in c or []:
                    if not isinstance(x, dict): continue
                    if x.get("type") == "text" and x["text"].strip(): md.append(f"\n### CLAUDE {ts}{side}\n\n{x['text']}\n")
                    elif x.get("type") == "tool_use":
                        md.append(f"- tool `{x.get('name')}`: `{json.dumps(x.get('input'), ensure_ascii=False)[:3000]}`")
    sid = os.path.basename(src)[:-6]
    slug = re.sub(r"[^a-z0-9]+", "-", (title or sid).lower()).strip("-")[:60]
    d = os.path.join(out_root, f"{(first or '0000-00-00')[:10]}_{slug}_{sid[:8]}")
    os.makedirs(d, exist_ok=True)
    with gzip.open(os.path.join(d, "raw.jsonl.gz"), "wt") as g: g.write("\n".join(lines) + "\n")
    with open(os.path.join(d, "transcript.md"), "w") as g:
        g.write(redact(f"# {title or sid}\n\nSession file `{sid}.jsonl`, first message {first}. Images removed, secrets replaced by [REDACTED].\n"
                       "Tool results are cut to 4,000 characters here; raw.jsonl.gz has every line in full.\n\n" + "\n".join(md), secrets))
    subdir = os.path.join(os.path.dirname(src), sid, "subagents")
    if os.path.isdir(subdir):
        os.makedirs(os.path.join(d, "subagents"), exist_ok=True)
        for s in sorted(os.listdir(subdir)):
            if not s.endswith(".jsonl"): continue
            out = []
            for line in open(os.path.join(subdir, s), errors="replace"):
                try:
                    j = json.loads(line)
                    if not dropped(j): out.append(redact(json.dumps(strip_images(j), ensure_ascii=False), secrets))
                except Exception: pass
            with gzip.open(os.path.join(d, "subagents", s + ".gz"), "wt") as g: g.write("\n".join(out) + "\n")
    return d

if __name__ == "__main__":
    secrets = load_secrets(sys.argv[1])
    for src in sys.argv[3:]:
        print(export(src, sys.argv[2], secrets))
