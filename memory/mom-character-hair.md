---
name: mom-character-hair
description: "The mom from 'My Mom Cracked The Dinosaur' as a Blender character (~/Desktop/mom-character, git); hair research done 15 Nov 2026, rebuild not run; two script copies disagree"
metadata:
  node_type: memory
  type: project
  originSessionId: e53bbed9-cca3-49b0-bf6a-b54722760597
  modified: 2026-11-15T09:45:14.246Z
---

Project `~/Desktop/mom-character` (also on the box), run 021 in ~/Projects/blender-funnel. Read `notes/HANDOFF.md` first: run order, last look
(render w3, 14 Nov), Nick's open notes (ends should curl more; darker than her honey; thin streak sheen vs her broad soft sheen;
bun a smooth ball vs her twisted knot). `./verify.sh` (scripts check only) exited 0 on 15 Nov 2026.

Hair research (15 Nov 2026): ~/Projects/hair-research (page, 1 fps frames, transcript, article text) and mom-character/notes/blender-manual-*.md.
All of it is condensed in the skill `blender-hair`; [[blender-skills-library]] explains the skill plan.

HOLD (HANDOFF, 15 Nov): no pod jobs until Nick says the research is finished. Pod ~$0.89/h; monthly spend cap was used up 15 Nov, only Nick raises it
([[blender-live-on-pod]], [[pod-guard-before-every-run]]). On 15 Nov `workbench status` said "WB down".

**DECISION 15 Nov 2026 (Nick): "you need to start our hair from scratch since we have more ways of figuring it out".** Hair is rebuilt new from the
reference + skill `blender-hair`; old mom_hair.py / rebuild_live.py / finish_hair.py are history, body and outfit (mom.py) stay. Process is the loop in skill `blender`
(read reference, dig research, try, compare each step, diagnose and re-research on a miss). The script-copy conflict below is therefore mostly moot for hair.

**Open conflicts found 15 Nov (not resolved):** `rebuild_live.py` differs between ~/.claude/skills/live-blender/scripts (N_TOP 60000, N_BANG 9000, the w3 values per the research page)
and mom-character/scripts (20000, 3500); `start_live.py` is newer in the skill folder (guard on every connector command). live-blender SKILL.md says the gloss settings were
never saved, but mom-character/scripts/finish_hair.py holds them (roughness 0.13, Coat 0.16; 0.09 was live-only).
**How to apply:** before a rebuild, pick one copy as truth with Nick; keep generic tools in live-blender, mom files in the project.

**STATE 16 Nov 2026 (checkpoint):** best mean silhouette IoU 0.794 (side 0.821, 3/4 0.768), blend copy `blend/blendpull/mom_hair_L42.blend`, pod DOWN, live Blender scene lost (rebuild from scripts). Back camera solved, back outline pending. Cursor brushes verified on a test object (Comb 900 of 3000 points) but not yet applied to the real hair. Resume: read `~/AgencyOS/handoffs/2026-11-15-mom-hair.md`. Rules from Nick: [[system-that-doesnt-need-nick]], [[hair-process-research-every-step]].
