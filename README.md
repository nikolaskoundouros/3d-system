# 3d-system: Nick's 3D work in one place

The entry point for any agent picking up Nick's 3D work: Blender characters (the mom from "My Mom Cracked The Dinosaur"), live Blender on rented RunPod GPU pods, the real-mouse cursor, the OpenCV clip analyzer and the camera work. Written 16 Nov 2026.

**Start here:** `handoffs/CURRENT-mom-character-HANDOFF.md`. It is a copy of `notes/HANDOFF.md` in the mom-character repo, which is the live version. It says what to read, what to run first, what is broken, and the task list.

## What is in this repo
| Folder | What |
|---|---|
| `handoffs/` | Every 3D handoff: the current one, the 15 Nov hair handoff, the weekend progress report (16 Nov), and the Zack clip and Art of War 3D handoffs from Oct and Nov. |
| `conversations/` | 20 full Blender chats (Oct to Nov 2026). Each folder has `transcript.md` (readable; tool output cut to 4,000 characters), `raw.jsonl.gz` (every line of the chat, images removed) and `subagents/` where the chat had helpers. Secrets are replaced by `[REDACTED]`. |
| `skills/` | The 3D Claude skills: `blender`, `blender-hair`, `live-blender` (with `cursor-recipe.md`), `clip-analyzer`, `camera-moves`, `learning-loop`, `zack-clip`. |
| `memory/` | 67 memory notes: the 3D ones, plus Nick's standing rules on how to work. `MEMORY.md` is the index. |
| `work-folders/` | Two chat temp folders the mom hair scripts still read from, saved before a reboot wipes them. `hair-session-e53bbed9/` holds masks `vm/`, analysis `ana/`, `scan/` and more. `fork-session-f3d1b7da/` holds the live tools' work, the hair tutorial frames and pod sync copies. |
| `box-home/` | Loose scripts from the box's home folder (`funnel_*.sh`, `limited.py`, `tee_remake`, `plotpointe-live` tools, small COLMAP solve outputs). `systemd/` has the pod-guard unit files. |
| `reference/` | The reference clip and its transcript. Private: it is someone else's video. |
| `tools/export_conversations.py` | Re-exports chats into `conversations/` the same way: images out, secrets blanked. |
| `setup.sh` | Puts every repo at the path the scripts expect, and installs the skills and memory. |

## The repos (all private, GitHub account nikolaskoundouros)
Scripts use absolute paths, so each repo must sit at its path. The box's home is also `/Users/nick`.

| Repo | Path on the Mac | Path on the box | What it does |
|---|---|---|---|
| `mom-character` | `~/Desktop/mom-character` | `~/Desktop/mom-character` | Mom hair build scripts, matched cameras, outlines, scoring loop, cursor harness, blend copies, results log |
| `render-desk` | `~/Desktop/render-desk` | `~/Desktop/render-desk` | `bin/workbench` (rent, push, run, pull and stop a GPU pod), the render desk, `tools/pod_guard.py` (10-minute idle stop) |
| `blender-funnel` | `~/Projects/blender-funnel` | `~/Desktop/blender-funnel` | Character and scene pipeline (recipes, run 021 reference shots, camera moves) |
| `clip-analyzer` | `~/Projects/clip-analyzer` | not used (box too small) | OpenCV clip analyzer page on port 8570: motion, faces, sound, captions, COLMAP camera solve tools |
| `plotpointe-animate` | `~/Projects/plotpointe-animate` | tools copied to `~/plotpointe-live` | PlotPointe Animate page: live Blender in the browser |
| `zoom-game` | `~/Projects/zoom-game` | not used | Zoom-game prototype (Nick: "this looks really average") |
| `3d-system` | `~/Projects/3d-system` | anywhere | This repo |

## Not in any repo (secrets and machine setup), by design
- **Pod keys:** `~/.config/render-desk/render.env` on the box holds `RUNPOD_API_KEY` and `RUNPOD_SSH_KEY`, plus spend caps. Never commit it. `render-desk/install/render.env.example` shows the shape.
- **ssh keys:** the box's `~/.ssh/id_ed25519` reaches the pods. The Mac reaches the box as `ssh nick@37.27.148.115`.
- **Pod guard:** `/etc/systemd/system/pod-guard.{service,timer}` (copies in `box-home/systemd/`). Off switch: `POD_GUARD=0` in `/etc/pod-guard.env`.
- **Blender connector:** the `blender` MCP server in the box's `~/.claude.json`, with port 9876 tunnelled to the pod by `mom-character/live/pod_live.sh`.
- **Blender manual:** offline in `~/Documents/blender-manual` on the box (2,453 pages), searched with `bman "words"`.
- **Big regenerable outputs:** COLMAP images and databases (`~/solve_*` on the box), per-frame render PNGs, analyzer `clips/`, `work/` and `exports/`.

## Working rules in one breath
- **Costs need Nick's go:** renting a pod (about $0.89/h) and any paid generation. Never end a turn with a pod billing unless he knows.
- **No Blender on the Mac.**
- **Script everything:** write every live setting into a script before the turn ends.
- **Compare properly:** at matched cameras, pixel by pixel.
- **Research before each step.**
- **Don't stop to ask after every pass;** show results.
- **Writing:** no em or en dashes.

The full rules are in `memory/` and the skills.
