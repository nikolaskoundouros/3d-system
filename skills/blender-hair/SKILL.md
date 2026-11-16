---
name: blender-hair
description: Everything learned so far about making hair in Blender for Nick's characters, so a new head does not start from scratch. The craft that applies to any character (guides then Interpolate Hair Curves, curl and clump, ends, the Principled Hair shader, Hair Dynamics, brush limits), the 2.79 "locks" method from the Hair With Curves video, what the hair-cards article adds, the mom's project state and what went wrong, and what is still unverified. Use for any hair groom, hairstyle, bun, bangs, hair shader or hair sim, and when Nick types /blender-hair.
argument-hint: [which hair job]
---

# /blender-hair

Run /blender first (tools, rules, pod cost). This page holds the hair craft only.
**To build a head: follow `build-method.md` in this folder** (step by step: manual page, mode, tool, setting, reference
check, and the line to record in the project's results.tsv). Started 15 Nov 2026, not yet run on a pod.
Checked 15 Nov 2026. The pod runs Blender 5.2.2, the manual notes are from the 5.3 manual: names can differ, check on the pod.

## Craft that applies to any character
Source: ~/Desktop/mom-character/notes/blender-manual-hair.md and blender-manual-materials.md (Blender 5.3 manual, read 15 Nov).
Offline manual on the box: `bman "words"`. Quotes marked [checked] I compared myself against the saved page
~/Projects/hair-research/manual/hair_principled.html on 15 Nov; the rest are as the notes give them.

**The pro flow the manual describes**
1. Few guide curves, shaped by hand in Curves Sculpt mode (mouse, see /blender). Header option Use Sculpt Collision
   keeps segments out of the surface. Add Curves with Interpolate Shape adds strands already combed like neighbours.
2. Interpolate Hair Curves fills the dense hair from the guides; Distribution Method Poisson Disk keeps spacing even;
   Density Mask or Mask Texture paints where hair grows.
3. Then Clump, Curl, Noise, Frizz, Smooth, Set Hair Curve Profile.
4. Optional Hair Dynamics node (geometry nodes, XPBD, marked experimental) for gravity drape.
5. Cycles Curves Shape: 3D Curves, "for accurate results when viewing curves close up".

**Curl and clump.** Curl Hair Curves has a Subdivision input; higher is smoother. At 1 on about 17-point strands the
curls came out coarse and ribbon-like (14 Nov). Build one guide map with Create Guide Index Map and feed the same Guide Index
to Clump and Curl.

**Ends.** Roll Hair Curves "coils or curls the tips of hair curves, rolling them inward or outward": Roll Length,
Roll Radius, Roll Depth, Roll Taper, Subdivision, Retain Overall Shape, Preserve Length. Built for curled-under ends.

**Shader (Principled Hair).**
- Chiang Roughness [checked]: "Too low values will smoothen the hair to the point of looking almost metallic, making
  glints look like Fireflies". Coat [checked]: "Simulate a shiny coat of fur", so not for human hair.
- Huang model [checked]: Aspect Ratio recommended "0.65~0.9 for Caucasian hair" (0.8~1 Asian, 0.5~0.65 African); its major
  axis follows the curve normal, "not supported in legacy particle hair". So Huang needs curves hair, not particle hair.

**Hair Dynamics.** Only closed-mesh colliders; open meshes "can lead to sudden jumping". Keep Substeps below 20 and raise
Constraint Iterations; check Residual error (1 or less is good). A shirt or collar that is an open mesh will jump.

**Brushes and posed bodies.** Curves Sculpt tools "only use the original mesh of the surface object" and ignore its
modifiers. Groom on the rest body, then carry the hair onto the pose with Deform Curves on Surface; use Snap to Deformed
Surface or Snap to Nearest Surface after changes.

## The 2.79 locks method (video "Blender Tutorial - Hair With Curves", 20:40)
Source: ~/Projects/hair-research/page/hair_research.html, evidence in ~/Projects/hair-research/video (1 frame per second,
whisper transcript, key overlay). I re-checked two frames and the transcript lines myself: 2:36 (Blender v2.79, Ctrl+T tilt
-43.6, Bevel Object BezierCircle) and 18:01 (Anisotropic BSDF GGX roughness 0.635, anisotropy 0.800, rotation 0.247, mix
0.387; Principled subsurface 0.100). The rest below is the research chat's reading, not re-checked by me.
- It is Blender 2.79 Path curves with a Bezier Circle as bevel. It is not the Curves hair object and shows no brushes.
- One lock = one path plus the shared bevel; width with Alt+S and twist with Ctrl+T per point, then copy and rotate round the
  3D cursor; editing the shared bevel grooves every lock at once.
- Shading along each lock: curve setting Use UV for mapping, a Noise texture driving Bump and a colour ramp, a gradient that
  darkens roots, ends mixed with a Transparent BSDF so tips break into strands.
- Every setting is a number, so it can be written as code.

## The hair-cards article (yelzkizi.org, 27 Apr 2025)
Game-engine hair cards. Its own FAQ says the Principled Hair BSDF is for strand hair, not cards. Only three things carry
to Cycles strands (research chat's reading): an opaque under-layer for volume, small per-lock colour shifts (about 5 %),
thin pieces at the hairline. Full text: ~/Projects/hair-research/article/text.md.

## Two ways to build a groom (Nick decides per job)
| | A: locks in code (video) | B: guides by mouse then Interpolate (manual) |
|---|---|---|
| Good for | the bun and twisted knots, a solid under-layer | the flowing top, bangs, lower length |
| How | path per lock + shared bevel, numbers in a script | Add, Comb, Pull Tips on guides, Interpolate Hair Curves |
| Catch | old 2.79 idea, needs a 5.2 test | needs the mouse and the GPU-drawn screen |
Research chat's pick for the mom's bun: A. Manual notes' pick for the rest: B. Not tried yet on the mom.

## Project pointer: the mom (~/Desktop/mom-character, git)
Read notes/HANDOFF.md first: it holds the HOLD (no pod jobs until Nick says the research is done) and the run order.
Look Nick saw last (render w3, 14 Nov), his open notes: ends should curl more; darker and more contrasty than her honey;
top sheen is thin streaks where hers is broad and soft; bun is a smooth ball where hers is a twisted knot.
Not on the mom yet, each from the notes: raise roughness from 0.13, Coat back to 0 (finish_hair.py sets 0.16), Huang
Aspect Ratio about 0.75, Roll Hair Curves for the ends, one guide map for clump and curl, locks for the bun, under-layer.

Nick, 15 Nov 2026: "you need to start our hair from scratch since we have more ways of figuring it out". The mom's hair is
rebuilt new from the reference and this page. The old mom_hair.py, rebuild_live.py and finish_hair.py are a record of what
went wrong, not a base. Body and outfit (mom.py) stay.

## To verify (not confirmed by me)
- Anisotropic BSDF versus Glossy in 5.2; whether Use UV for mapping on curves still exists in 5.2 (pod test).
- Names that may differ between the 5.3 manual and the 5.2.2 pod (Pull Tips versus Snake Hook).
- Whether roughness went to 0.09 live on 14 Nov (the notes say so, finish_hair.py has 0.13, never saved).
- Which parameter set made render w3: live-blender/scripts/rebuild_live.py has N_TOP 60000, N_BANG 9000; the mom-character
  copy has N_TOP 20000, N_BANG 3500 (the research page says w3 had 60,000 and 9,000).

## Learned (add one line per job: what, source, date)
- 2026-11-15, mom hair, pod Blender 5.2.2 (source: ~/Desktop/mom-character/results.tsv): a viewer on the pod screen (x11vnc + noVNC, tunnel pod to box to Mac, browser pane) made the mouse register Add strokes and lets Nick watch live. Comb by xdotool did not move strands (unknown why). The Interpolate Hair Curves modifier's inputs cannot be set from Python in 5.2.2. Building guides and dense strands in DATA is instant (build under 1 s, 4 Cycles views 7.6 s, full loop 18 s); scripts hair2_*.py in the project. Reference hair is smooth broad locks, so strand clouds look wrong: the tutorial's locks method is the next test.
- 2026-11-15, mom hair: the tutorial's LOCKS method works in 5.2.2 as DATA (NURBS curve per lock, shared bevel object with grooves, radius and tilt per point; script hair2_locks.py, 187 locks, loop 16 s) and fits her smooth reference far better than strand clouds. First numbers (width 0.0125, flat bevel) looked like wooden slats; width 0.0085, bevel y-scale 0.48, wavy lower locks, a side layer to cover the scalp fixed that. When a brush fails, switch to locks, not to strands. Open: seam ring where top meets lower, crown lift, pale colour, front flick. Source: results.tsv.
- 2026-11-15, mom hair: the tutorial's SHADING was the missing half of the locks method (source: video 12:25 to 17:19, frames 14:18 and 14:21; results.tsv L6). Per lock: noise stretched along it (UV x runs along a bevelled curve in 5.2) drives colour AND a Bump (0.46, distance 0.002), a gradient darkens roots, gradient x noise into a ramp mixes in a Transparent BSDF so tips break up. Without it locks look like wooden slats. Crown lift 0.026 made a cone, 0.011 is right. Open: stepped ridge where top meets lower (thinning side-lock roots did not fix it), floating strands on top (video 9:40, article layering) not tried.
- 2026-11-15, hands: real keys work in Edit Mode on the pod: select a point by code, then `xdotool key alt+s`, move the mouse, click (width 0.01048 to 0.01312, results.tsv). Use hands for finishing a few locks (Alt+S width, Ctrl+T twist, G move), code for bulk. Layers from the article (base, middle, outer, stray; stagger edges) and floating strands (video 9:52) are in hair2_locks.py. Nick's rule: go back to this research at every step and say plainly what was code and what was by hand.
- 2026-11-15, seam: it was flat square lock ENDS (caps), found by zooming the live rendered view, not by guessing. Manual modeling/curves/properties/geometry: Fill Caps seals tube ends; radius per control point (Alt+S in Edit Mode) shapes them. Hand test: `xdotool key alt+s`, `xdotool type 0.35`, Return scaled two selected root points exactly 0.35x. Fix for all locks: thin roots (x0.35 over the first 18%) and base-layer ends tapering to a point; base colour must stay close to the top hair or it shows as dark leaves. Source: results.tsv L10, L11.
- 2026-11-15, softness (results.tsv L12): taper bangs/pieces from 50-55% of their length to a point, taper lower tips from 70%, vary hem lengths, shrink the bun spiral to a point plus a few tight core locks (no hollow centre), and feather lock EDGES with alpha (1-|sin(2 pi V)| plus noise, max with the tip mask; V runs around a bevelled lock). A friend's review is a hint, not a spec: check each point against the current render and our references first (the outward tip flip contradicted our reference notes and was skipped).
- 2026-11-15, REAL-HAIR LOOK (results.tsv L13 to L15): locks alone never read as hair; the article's layering did: locks = opaque underlayer, then fine strands on top (hair curves following each lock path, Principled Hair Huang aspect 0.75 rough 0.32, Random Color 0.14, melanin about 0.34 top / 0.42 lower for golden honey, +5 mm outward, random strand length 0.8 to 1.0 so ends stagger), streaks as their own pale strand group. Strand layer must be built from the lock paths (store paths in lock(), resample to equal point counts), never from separate guides.
- 2026-11-15, visibility and speed: a live path-traced viewport of hair never looks clean, so Nick could not see progress there. Show each pass on a self-refreshing board instead (python3 -m http.server on the snaps folder, board.html polls latest.jpg every 1.5 s, the loop script copies each compare to latest.jpg) in a second browser tab. Machine time per pass is about 16 to 18 s; the rest is the agent re-reading, thinking and patching, so batch several fixes per pass and avoid shape/syntax errors (each cost a full loop). Top strand roughness 0.46 gives a broader sheen than 0.32.
- 2026-11-15, FINAL DRAFT L19 (results.tsv): full pipeline = hair2_body.py (body) -> hair2_locks.py (locks as underlayer + base layer + side layer + bun + floating strands + fine outer strand layer, all from stored lock paths). Process that worked: crop reference beside the last result, list diffs per feature, check article/manual/tutorial for each, batch 4 to 5 fixes per pass, render, repeat; a .blend copy via save_as_mainfile(filepath=..., copy=True) so nothing open is overwritten. Open: temple/hairline flat strand tops, broader gloss on top, straighter hem than hers, ear tuck.
- 2026-11-15, CHECKING PROCESS (Nick: "if i can see those changes, why cant you?"): I missed forehead clumps and side wings because I judged against my own feature checklist at sheet size. Before every pass: crop and enlarge the SAME region of the reference and our render side by side (front/forehead, sides, back, bun, hem) and list the differences from the pixels. Ombre: Principled Hair melanin = base - ombre*Hair Info Intercept (lighter tips, as in her back view). Source: results.tsv L21 to L24.
- 2026-11-15, DIRECTION (Nick: "check it from the root of her head... hers orbit upwards first and then go down"): hair does not run straight down a surface. Build each front lock from its ROOT: a 3-point Bezier from the scalp at the part (control point up 0.03-0.04 and forward 0.05-0.07), ending at brow/cheekbone, then push every point 8 mm clear of the skin with closest_point_on_mesh. Same up-and-out-then-down arc for face-framing pieces and front lower locks. Always compare the flow direction from the root in the reference, not only where the ends land. Source: results.tsv L25, L26.
- 2026-11-15, SIDES (Nick: "the sides of her hair are directed into the bun"): the side hair is a band swept back and up into the bun with the ear left free; hanging hair starts only at ear height or behind the ear. Lower locks must not start at the crown on the sides (they cover the swept band). The ear is only about 72 to 108 degrees wide (a 66 to 122 gap also removed hair behind the ear). Hair above the ear needs its own locks that run back above the ear and drop behind it (Lock_Ear_*, ray_polar points, 8 mm clear of the skin); thin-rooted side locks alone leave a bare patch. Also: a silently skipped ray (lock not built) removed a whole strand group, so clamp random ends to the face width and skip empty groups with a message. Source: results.tsv L27 to L30.
- 2026-11-15, POD IDLE GUARD: it terminates the pod after 10 minutes with no connector command, even mid-session while the agent only thinks, crops or writes (it did at 14:09). The live scene and the viewer die with it; scripts and .blend copies on the Mac survive. Send a cheap command (for example a print) at least every 5 minutes while working, and save a copy (save_as_mainfile(filepath, copy=True)) after every good pass. `workbench push` with no pod up silently rents a new one. Recovery: pod_live.sh under `flock /tmp/aow-wb-up.lock`, then hair2_body.py, hair2_setup.py, loop3.sh; viewer: x11vnc + websockify on the pod, box tunnel via a small script (a pkill -f in an ssh one-liner kills its own shell), Mac tunnel to box:6080, navigate the browser tab, dismiss the Blender splash with xdotool (mouse move, Escape).
- 2026-11-15, BANGS (L31, L32): her bangs end at the CHEEKBONE (reference analysis), sweep diagonally from the part, and thin clumps fall over the forehead from the part with a V gap; ends outboard of the eye so the eyes stay visible.
- 2026-11-15, ONE MASS (Nick: "think of her hair as one connected clump of hair, not different groups"): do NOT build top / side / lower as separate groups, their boundaries show as seams. Spread roots over the whole scalp (polar grid + crown grid) and give each strand a path blended continuously between "swept back into the bun" and "hanging": P = (1-w)*hang + w*bun, w = smoothstep across the half-up line (about ear-top height, z 1.588 over 0.026). Roots at the ear hang behind it; hang length is shorter toward the front (jaw at the sides, longest at the back); strands aim at ORDERED targets on the bun so they converge without crossing; never push strands off the neck/shoulder mesh (they wrap round the collar). Material by weight bucket with ombre so colour is continuous. Source: results.tsv L33 to L35, script hair2_locks.py FIELD block.
- 2026-11-15, SOURCES AS A CHECKLIST (Nick: "i also sent you articles and blender docs. why didnt you use everything?"): go down sources-checklist.md before every pass; each rule is applied or rejected in writing. MEASURE with scan_render.py + patchscan.py (ribbon % and skin % per 40 px patch over 5 hi-res views), never only the 432 px contact sheet. Real hair is 0.05 to 0.1 mm thick (radius about 0.00003 to 0.00005): strands at 0.00016 looked like bristles. A "bald spot" can be a flat ribbon showing through the strands, not skin: test locks and skin as separate magenta passes.
- 2026-11-15, MATCHED CAMERAS (Nick: "add images of the reference in our blender... we have multiple angles"): compare only at the SAME camera. refs/cams.json + scripts/ref_overlay.py give one camera per reference frame with her frame as the background (solvePnP on ear/chin/eye/nose landmarks; four planar face points flip, so constrain with a guess or the eye spacing). scripts/fit_side.py renders hair only (everything else is_holdout) and prints silhouette IoU vs her hair polygon; use it as the loop metric. Numbers taken at mismatched angles (widths, directions) are invalid. Her side silhouette: our hair is too big (surplus mostly at the back and the dome) and hair that hugs the body scored better than hair with a gap.
- 2026-11-15, COLOUR: judge colour against SEVERAL frames, not two. Her bun equals her hair colour in every frame (lit L 41.7 vs 42.3; dark 11.3 vs 11.3). Principled Hair melanin cannot reach her golden chroma (a 14, b 25): use parametrization COLOR (direct RGB, root to tip via Hair Info Intercept) and close the loop on Lab per band. Cycles transparent bounces must be about 32 for transparent ribbon edges.
- 2026-11-15, SYSTEM TOOLS (Nick: "build a depth tool, fix the cursor, build a detailed outline tool... the goal is a system which doesnt need me"): scripts/outline_auto.py (+ view_masks.py) = automatic hair mask per reference frame, seeded from our own render at the matched camera and GrabCut; scripts/fit_side.py + fit.sh + viz.py = one-command silhouette score and live board; scripts/cursor_harness.py + harness.sh = test every curve brush by mouse on a clean object. Findings: outline good at the side, limited by camera accuracy elsewhere (back/front cameras are guesses: fix them first); the pod's files come from the BOX copy of the project, so anything new (npy masks, scripts) must be scp'd to the box before `workbench push`; zsh does not word-split unquoted variables (call each config explicitly); never put a comment mid-line in generated one-liners. Cursor: Comb, Pull Tips, Puff, Pinch, Delete move nothing by mouse even on a clean test object; Add works only on a direct scalp click.
