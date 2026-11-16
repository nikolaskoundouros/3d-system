# Acid reflux clip + cloud GPU + parallel desk (night of 2026-10-06)

## What this session did
After the stitches final (review/stitches_final_v2_captions.mp4, 22.20 s, $1.56 desk), Nick chose acid reflux as the next clip
(one clip a day, cut the 14-hour day). Built and tested an always-on cloud GPU ("workbench") and parallel desk jobs; set up the
acid reflux project from an outside package; extracted Zack's script and beats; rendered a full side-by-side stills sheet.
Also wrote a ChatGPT version of the process for Nick's editor.

## Decisions (with why)
- Acid reflux over the robber clip (bank-money): biology is our strongest area, the package has the anatomy, actor and pulses.
- Cloud GPU for previews and stills: measured 1.4 to 3.6 s per 540 px still on a RunPod 4090 vs about a minute on the Mac;
  frees the Mac for Nick's Blender. Stops itself after 30 idle min or 10 h; cost goes in the desk ledger (caps count it).
- Parallel desk jobs: the desk now sweeps only pods older than MAX_JOB_MINUTES + 60 (birth time tagged in the pod name).
- Fix only what Nick flags (his rule today, memory fix-only-what-flagged.md); nothing in the acid reflux visuals changed.

## Files
- ~/Desktop/render-desk: renderdesk/providers/runpod.py (age-based sweep, pod_born), scripts/pod_bootstrap.sh (race-safe
  Blender unpack, rsync), NEW renderdesk/workbench.py + bin/workbench. verify.sh PASS. NOT committed, NOT deployed to the box.
- ~/Desktop/stitches/gpu/run_final.sh (now parallel; old one-at-a-time copy gpu/run_final_sequential.sh)
- ~/Desktop/acid-reflux (newproject): from_package/ (copy of the package; original in ~/Desktop/acid-reflux-inbox),
  refs/zack_acid_reflux.mp4, refs/zack_words.json (62 words), refs/beats.md, tools/wb_stills.py, tools/zack_sheet.py,
  review/stills_v0/ (25 stills), review/sheet_v0_zack_vs_package.png. verify.sh PASS.
- ~/Desktop/editor-kit/zack_remake_process_for_chatgpt.md (sent; 17 quotes verified against the transcript)

## Rules Nick stated tonight
- "i only want you to fix the things i tell you. importanrt"
- One clip a day; cut the 14 hours. Scripts are written by Nick.

## Tests run (all passed)
- workbench up / push / run (Blender 5.2.2, OptiX on RTX 4090) / pull / down: $0.08, ledger row written, watchdog exits.
- Two desk jobs started 20 s apart: both rendered and delivered (parA, parB), no sweep: $0.03.
  Their test outputs sit in the editor's Drive folder Nick-AE/render/3-finished/parA_*, parB_* (Nick may delete).

## Open loops
- Needs Nick's go: deploy the desk change to the box (deploy/ship.sh). Until then an editor job started on the box still
  sweeps every desk pod, ours included.
- Needs Nick: spend caps (daily $20, monthly $40; $10.94 spent this month incl. tonight's tests).
- Acid reflux: Nick locks his script (draft + my notes in chat: windpipe -> the tube's lining, "vomit" -> into your mouth),
  records the VO; gives notes on review/sheet_v0_zack_vs_package.png; then sequence by sequence.
- Resume: "Resume acid reflux: read ~/AgencyOS/handoffs/2026-10-06-acid-reflux.md and start from Nick's notes on the sheet."

## Late (23:xx): Nick's twist
- Nick: "a man biting a burger and the bite going down the esophagus etc. also id like the acid to be green and toxicyy".
- Green acid concept: tools/concept_green_acid.py (material only, in memory) -> review/concept_green_acid_v1.png, sent.
- Burger concept: tools/concept_burger.py (procedural burger + IK hand) -> review/concept_burger_v1/v2.png, NOT sent: reads
  wrong (burger floats over the face, flat waiter's hand, stack looks like macarons). Plan: a real burger model (Sketchfab
  via ~/Desktop/stitches/tools/sketchfab_get.py) + a Mixamo eating clip retargeted to the actor (Nick logs in to Mixamo).
  The package's "Food bolus 1/2" (01_Anatomy_Full) becomes the bite going down the tube.
- Cloud GPU down; tonight's workbench total $0.15, desk tests $0.03.

## Overnight (Nick: "add bubbles to the acid, then do the burger. start working with caffeinate with our process")
- caffeinate -dimsu -t 43200 started 23:2x.
- Bubbles: tools/look_acid.py toxic(m, bubbles=True): 3 sizes of Voronoi bubbles (3D; 4D thinned them) rising with the frame,
  bright rims, bump. review/concept_bubbles_v4.png + concept_bubbles_motion_v4.mp4 sent.
- Burger: Sketchfab "Hamburger" by Simal Mai (CC-BY, assets/models/burger_simal/CREDIT.txt; credit needed in the description),
  hand-keyed bite (no Mixamo: needs Nick's login). tools/build_v02.py -> blend/reflux_v02.blend (package copy + green acid +
  burger shot strip in 00_Reflux_Edit; package edit shifted +33 frames, edit 1-788). 3/4 profile from his left, IK hand,
  fingers curled, jaw bite + chew, bite boolean from 0.55 s, camera pushes toward his throat.
- Preview: tools/wb_frames.py + tools/join_open.py (zoom-fade 33-44) -> review/v02_opening_preview.mp4 (4 s, silent) and
  review/v02_opening_sheet.png, sent.
- Known, for Nick to judge (not fixed): push ends on his chin rather than the throat; the bite mark is hard to see (burger
  lowered out of focus); the anatomy's first frames are hazy (the package's own fade-in).
- Next: Nick's notes on bubbles + opening, his script and VO; then re-time everything to the VO and go sequence by sequence.

## 2026-10-07 morning: Nick's notes on the opening, v03
- Nick: "i want him sitting in a macdonalds-like restaurant. its, good but he should be holding it with two hands (check
  mixamo) and we should follow the burger later if that makes sense".
- Mixamo: the browser pane is not logged in (needs Nick); used the stitches clip's Mixamo "Sitting Idle" for the seat pose
  and IK for the two-handed grip instead.
- tools/build_v03.py -> blend/reflux_v03.blend: new scene 03_Burger (full copy of the actor): generic fast-food booth (no
  real brand; Sketchfab CC-BY: booth "2K Textured Diner Booth w/ Table" by Kimbell Whatley recoloured, "Fast Food Set" by
  Ah Xun (its burger removed), "Generic Soda Dispenser" by Glowbox 3D, burger "Hamburger" by Simal Mai), tiled wall with red
  band and yellow stripe, menu glow, seated from his hip joints, both hands gripping with the stitches grip method, camera
  follows the burger up to the bite (near profile), then his chin and throat, zoom-fade into the anatomy.
- Sent review/v03_opening_sheet.png + v03_opening_preview.mp4. Credits needed in the description for all four models.

## 2026-10-07 late morning: HumGen dress (shelved), biology pass v1
- Nick: "why are you not using HumGen though? we have outfits there too." The package actor IS a HumGen human (HG_Body,
  rig with HG props, trousers = HumGen skinny jeans) but its HG flags were stripped. tools/dress_hg.py (Mac, HumGen add-on)
  restores the flags on the 03_Burger copy only and applies outfits/male/Casual/Casual_Weekday.blend (tee + jeans), packs
  textures -> blend/base_dressed.blend (local). tools/build_v08.py = v06 started from it -> reflux_v08.blend (pod only).
  v08 stills: tee fits but skin pokes through at the shoulders, forearm passes through the burger box. Nick then:
  "drop the shirt and all of that, lets get to the biology". Not fixed, shelved.
- Biology (Nick: "work on the biology as well"): tools/bio_v1.py on 01_Anatomy_Full: real lungs (Sketchfab "Realistic Human
  Lungs" by neshallads, split, gap opened), real spine C3-L5 (Sketchfab "The human spinal column" by 3D) right of the
  fibrous band with the package's blue-grey disc material, Zack-colour fibre texture on the band, warm pink glowing tissue
  instead of the cyan grid. Liver model (ElliotSS) tried and dropped (read as a dark bean). Diaphragm downloaded, unused.
  Credits needed in the description: lungs (neshallads), spine (3D). Sheet: review/bio_v1_sheet.png (Zack / before / now).
- Known, not yet fixed: the tube's top ends in mid-air at 0.5 s (package), ribs read as ghostly rings, bottom of frame
  sparser than Zack's intestines.
- Nick's 3 notes on the biology sheet ("connector ... low quality", "looks like poop not the burger", "disconection here"):
  tools/anat_fix_v1.py on reflux_v08_bio1.blend -> reflux_v08_bio2.blend (pod): tube front ends in an elliptic arch (rows
  re-spaced along each column; a rim curve was tried and dropped, it floated off the moving tube); the bite is a chunk cut
  from the burger model (its surface inside an ellipsoid + layer-coloured cut faces sampled from its own texture; boolean
  came out empty, mesh not watertight), follows the old bolus, shown by a driver on the old bolus's hide_render; colon
  extended off frame both sides, small intestine = one continuous curled coil from the colon. Sheet review/bio_v2_fixes.png.
- Reviewer's other findings (glossy salmon lungs, no blue tile, ribs like a spring, spine spikes at the stomach edge) are
  waiting for Nick's word (fix only what he flags).
- Nick (afternoon): yes to the reviewer's four (tools/bio_v3.py: lungs orange-red matte, Zack blue tile at the edges behind
  a fading warm membrane, narrower lung gap + bonier ribs, lumbar processes narrowed); splash (tools/splash_v2.py: jet up
  the tube, 26 drops along the channel, taller crown, darker more toxic acid); bite = chewed clump of 14 torn burger
  pieces (tools/anat_fix_v2.py; v1 single chunk "looks like an emoji"); new opening (tools/xray_v1.py on bio4 ->
  reflux_v09.blend): bite, skin/clothes fade to see-through (copied materials, 02_Character untouched), skull/jaw/C-spine
  from the spine_3d model on head/jaw/neck bones, tongue, glassy throat in front of the vertebrae, bite follows a path down,
  Zack-tile card behind him fades in, shot now 2.2 s, rest of edit +22 frames, package's opening shirtless-man fade removed.
  Preview sent: review/v09_opening_preview.mp4 (4.5 s). Chain: base_dressed -> build_v08 -> bio_v1 -> anat_fix_v2 -> bio_v3
  -> splash_v2 -> xray_v1 (about 4 min on the pod).
- render-desk: workbench run now keeps the pod alive during long commands (a 30+ min run was killed as idle). Not committed.
- Known, not fixed: restaurant shirt skin poke at the shoulders and forearm through the burger box (Nick: drop the shirt).

## 2026-10-07 evening: failure day, guardrails, rebuild plan
- Nick: today was a failure ($9.59, 13 GPU h, 0 finals). Assessment + guardrails: memory clip-day-failure-2026-10-07.md,
  zack-clip skill Step 4, render-desk guardrails (idle 10 min, 5 h, $6/day workbench cap, auto pull-back).
- Script first: refs/shotplan_v2.md (Nick's VO word by word, literal events). Motion test v1 (review/journey1_motion_test.mp4):
  0 cuts, camera median 1.08 px/frame vs Zack 0.91, longest still 0.9 s (Zack 0.6) in the man inserts.
- Built, untested at full size: tools/journey_v2.py (+ live/src/journey2_anat.py, journey2_man.py), tools/fx_v2.py (tube cut
  open, acid column, valve flutter; peristalsis removed: Cast inflated the wall), tools/sim_acid_v3.py (sealed pool, outside
  blocks, pump plate, no hidden sources) not yet run.
- The scene: blend/reflux_v15_graphics.blend (rebuilt by live/src/rebuild_v15.py, now on the Mac).
- Hetzner (root@46.62.230.121): user nick, home /Users/nick, Claude Code 2.1.293, ~/.config/render-desk/render.env (RunPod key,
  own SSH key), project + tools + skills/agents/memory copied. Nick's morning step: ssh nick@46.62.230.121, tmux, claude, log in,
  /remote-control. Telegram: Clod's bot on the box (not yet wired to the clip work).
- Next with the new process: Nick locks shotplan_v2 + motion test v2; then the sealed-acid sims (10-s test first); then stills.
