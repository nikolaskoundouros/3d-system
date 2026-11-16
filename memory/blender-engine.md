---
name: blender-engine
description: "Blender platform at ~/Desktop/blender-engine (8520): Clip Studio runs a clip through Nick's rulebook (Claude login, render desk GPU, 3 gates, every step visible) plus the 3D viewer; ChatGPT not connected yet"
metadata:
  node_type: memory
  type: project
  originSessionId: f8f7c83a-96a5-4f30-b0f3-511f0eda2ca7
  modified: 2026-10-02T12:29:20.972Z
---

Restored 2026-10-02 from `My Drive/Nick-AE/Desktop-2026-09-24/blender-engine` (archived there 24 Sept) to ~/Desktop/blender-engine; git started that day (main = restored code, branch `studio` = the build). Nick's ask: "connects to my claude, chatgpt and renderer to get clips out fast with high quality... able to look at through all the steps".

- **Clip Studio** at `/`: a run = one clip through the rulebook (server/rulebook.json, copied word for word from ~/Desktop/3d-clip-rulebook.html by tools/import_rulebook.py): plan every second, gate 1, per sequence assets/environment/motion (builder writes Blender Python, retried on error), stills from the three.js viewer in headless Chrome (no Blender render) checked against reference + 30 rules with a fix loop, gate 2 (draft/full, the paid go), render on the live render desk via its own /login, chunked /upload, /api/state, gate 3. Missing assets stop the run (props never from blocks).
- Models: Claude via `claude -p --safe-mode --tools ""` with stream-json images and --json-schema (his login, not billed). Roles default planner/reviewer opus, builder fable. The old viewer Edit panel uses the login too.
- Desk password read from ~/.config/render-desk/render.env; live sign-in + /api/state verified 2026-10-02. A resumed render never re-uploads (pending_render).
- `./verify.sh` = rulebook match + checks/unit.py + checks/e2e.py (real Blender, Chrome, ffmpeg; fake claude + fake desk), ~55 s. `tools/demo.py` (launch.json `clip-studio-demo`, 8521) shows the page with fakes for free.
- 3D viewer at `/viewer` (deep link ?p=&v=). Stitches projects copied back too (projects/ is gitignored).

Open (2026-10-02): Nick to pick ChatGPT route (Codex CLI with his ChatGPT login, or an OpenAI API key), and give a go for the first paid draft render through the desk.

Related: [[render-desk]], [[genesis-platform]], [[machine-and-render-workflow]], [[no-rendering-without-permission]]
