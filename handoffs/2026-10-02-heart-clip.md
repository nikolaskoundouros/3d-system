# Heart clip: checkpoint log (2 Oct 2026)

## What this session is doing
Continuing the 22 s, 9:16 heart explainer in Blender from the R24 package, scene by scene, using the order in
~/Desktop/CLAUDE_HANDOFF.txt. Nick asked for: fixes first, a checkpoint after every scene, and live progress
(work happens in the open Blender window over the MCP bridge; viewport stills only, no rendering).

## Decisions made
- R25 beat is the base: 62 BPM, strength 0.95, raised-cosine squeeze (rise 28%, release 50%, rest 22%). Why: the handoff's recommended first candidate; R24's 75 BPM jab was rejected as tacky. Nick did not reject R25 and said "start on the fixes".
- Beat drivers rewritten as Blender simple expressions (floor instead of %, pow-free). Why: Blender's 256-char driver limit, and the R24 expressions were not simple expressions.
- Apex poke-through fixed by trimming the last 10 points (39 to 48) of two curves: "Right atrium through valve to right ventricle" (04 Connected circulation) and "R21 blood volume • Right atrium through valve to right ventri" (14 Dense procedural blood). Why: a camera ray check showed every outside-the-heart hit came from those points, at all 22 beat peaks; after trimming, 0 hits at all 22 peaks and at rest. The 60 follow-path cells still resolve.
- Left for Scene B: around edit 4.8 to 6 s (geometry frames 535 to 571), a few still keyframed cells ("RBC • Right atrium through valve to right ventricle • NN", 05 Blood cell flow, keys only from frame 601) show through the back wall during R24's 360 orbit. Why: Scene B replaces that camera move; recheck after.

## Files
- Source (untouched): /Users/nick/Desktop/heart-r24/Heart_Revision_24_Live_Review.blend
- R25 beat candidate: /Users/nick/Desktop/heart-r24/Heart_R25_Beat_Candidate.blend
- Working file (open in Blender): /Users/nick/Desktop/heart-r24/Heart_R26_work.blend
- Checkpoint 1: /Users/nick/Desktop/heart-r24/Heart_R26_cp1_beat_tube_fix.blend
- Checkpoint 2: /Users/nick/Desktop/heart-r24/Heart_R26_cp2_sceneB_camera_chambers.blend
- Checkpoint 3: /Users/nick/Desktop/heart-r24/Heart_R26_cp3_chamber_orbits.blend (review/checkpoint3_chamber_orbits.png)
- Narration (from burned-in captions, 6 fps): review/caps_sheet_0..3.png; side-by-sides: review/side_by_side_current.png, side_by_side_cp2.png
- Tools: /Users/nick/Desktop/heart-r24/tools/ (make_beat_candidate.py, measure_beat.py, inspect_*.py)
- Review images: /Users/nick/Desktop/heart-r24/review/ (R25_beat_comparison.png, checkpoint1_apex_fix.png)

## Rules stated this session
- Checkpoint after every scene; Nick wants to watch progress live in Blender.
- (Standing) no local rendering; new versions go to new filenames; save only with explicit filepaths.

## Facts to keep straight
- The zip is NOT the package the handoff describes: no Heart_Full_Project.blend, no Zack reference clip, no R23 baseline, no Tools/ folder.
- Local Blender is 5.1.2; the R24 file was saved by 4.5. GPU-server compatibility of 5.1-saved files is unchecked.
- Time map: geometry frame = 391 + 30 x seconds; edit frame = 1 + 30 x seconds. Heart root never moves; the camera orbits.
- Each checkpoint .blend is about 216 MB; 20 GB free on 2 Oct.

## Checkpoint 2 (Scene B) done
- Camera geometry frames 463 to 616 rebuilt: eased push to an upright close-up on the left chamber (3.0 to 5.2 s, "muscle and tissue contracting nonstop"), pull back to a front whole-heart view by 5.7 s, slow drift to 7.5 s, then R24's existing pullback. 18 deg camera roll eases in at 2.4 s and out by 9.5 s so the heart reads upright. Quaternion sign continuity checked across 391 to 1056.
- Chamber glows rekeyed (peak 0.65): upper_left 5.55 s, upper_right 6.05 s, lower_left 6.65 s, lower_right 7.15 s, fading 7.6 to 8.6 s into the flow cue. Matches the original edit's order and spacing.
- Nick (2026-10-02): "what i care about is the motion, the pacing, the feel, the colors"; only 45 min left to finish the clip.

## Checkpoint 3 (chamber orbits) done
- Nick: "the most important thing is the zooms and camera angles to give it the constant movement. so when we highlight red part, we zoom and orbit to the red part, when the green one, we turn and zoom to the green etc."
- Camera geometry frames 547 to 631 rebuilt as one Hermite spline: arrives at green 5.73 s, cyan 6.27 s, magenta 6.87 s, violet 7.4 s (each about 0.2 s after its glow starts), orbit 22 to 29 deg toward the chamber's side, push to dist 1.45 to 1.6, then hands off with matching velocity into R24's pullback at 8.0 s. Never stops (min speed about 0.9 units/s).

## Open loops
- Same chase-the-highlight camera for the later chamber cues: "your upper right chamber" (10.7 to 12.0 s, glow_upper_left already ramps at 10.5 s) and "the upper left chamber" (18.35 to 19.35 s).
- Colors: ours reads orange and yellow on the outer wall with whitish cut faces; the original is red with a pink cut face and cream fat beads on teal. Viewport preview only; not checked in a render.
- Then C, D, E, F, G as in CLAUDE_HANDOFF.txt section 4.

## Reference changed (2026-10-02, after checkpoint 3)
- Nick: the right reference is ~/Downloads/Heart_Revision_21_Complete (1).mp4 (270x480, 25 fps, 22.16 s), not clip_5; "we focused on the shining ventricles", the work so far will still be used.
- Split into 11 scenes, silent clips in ~/Desktop/heart-r24/reference_r21/scenes/ (01_human_intro 0.0-0.8 ... 11_back_to_human 21.4-22.16).
- Blender crashed out of memory (36.6 GB) from a 400+ frame viewport-capture loop; the 9-21 s camera pass done after checkpoint 3 was lost (not saved). Checkpoint 3 is intact.
- GPU desk works for this project: tools/make_draft.py builds gpu/pkg (edit scene active, placeholder camera, Cycles 12 samples + denoise, GPU), zip, then `bin/renderdesk render <zip>` from ~/Desktop/render-desk. First run stopped by Nick before rendering: pod c6rl2oixjsc9fc, RTX 4090 $0.74/hr, 3.3 min, $0.04, terminated.

## R27 (base = R22), 2026-10-02 evening
- Nick: R22 is the base (matches R21 in approved scenes 1,2,4,5,6). Rules: camera action every 0.7-1 s; power graphic on "power"; rotation+color chamber move at "left chamber"; CNS removed; violet not gold.
- /Users/nick/Desktop/heart-r24/r27/Heart_R27_work.blend built by tools/make_r27.py from the untouched R22 package: 22 CNS objects hidden; scene 3 (2.0-7.6 s) camera + one-chamber-at-a-time glows (green 2.3, cyan 3.1, magenta 3.8, violet 4.5), see-through from 5.3, punch-in + shockwave ring at 6.0-6.65, tilt up at 6.9, hand-off to R22 at 7.6; all changed controls land on R22 values by 7.8 s.
- Storyboard: review/R27_scene3_storyboard.png (GPU stills, $0.04). Problems seen: ring leaves frame within ~0.1 s; blood inside the heart and the burst out are not visible at 540x960.
- GPU stills tool: tools/make_stills.py -- OUT SAMPLES PCT t1,t2,... (one contiguous frame per time).

## R27b, 2026-10-02 18:13
- Nick: rings "more subtle, ripple effect" -> three faint rings 0.1 s apart (tools/make_r27b.py); heart now turns see-through on "power" (6.0 s), not 5.3 s.
- r27/Heart_R27b_work.blend (R27 kept). Stills: review/R27b_power_ripple.png and review/R21_vs_R27b_every_second.png ($0.11).
- Fixed the render desk cost log (~/.local/share/render-desk/ledger.tsv, backup .bak-2026-10-02): header was missing data_centre/render_seconds, so cost was read from seconds_per_frame and the $20/day cap tripped. Now $0.50 spent today. Code fix in ledger.append (migrate header) offered, not done.

## R27c, 2026-10-02 evening
- Nick: cut the word "going" (cut 19.40-19.90 s, 15 frames; clip now 21.67 s); 7 s position + translucency disliked; 7.5-14.5 looked identical (churn); 17-20 needs work; "make sure they are vivid... zooms and camera movement there to support engagement".
- tools/make_r27c.py (from R27b): story keys after the cut shifted -15 frames (beat drivers and cell animation untouched, so no pop); narration split into two strips; closing image and 3D end moved up; one Hermite camera path 6.45-20.0 s following the blood route (aorta, upper right chamber, down to lower right, pulmonary trunk, lungs, back via pulmonary vein, upper left, lower left, aorta); see-through only on "keep your blood flowing" (7.5), solid squeeze on "muscles contracting" (8.7-9.75); glows full strength on their words.
- Preview without GPU: review/R27c_preview_10fps.mp4 (viewport frames + cut narration) and review/R27c_full_clip_every_half_second.png. Fastest camera moment 34 u/s at 19.8-20.0 s (into R22's body pullback).

## R27d, 2026-10-02 late evening
- Nick: scene 3 camera less abrupt, heart beating like Zack's; grain question; at "to fill it up with oxygen" zoom into the blood and move toward the lungs; cut the vessel close-up.
- tools/make_r27d.py (from R27c): 97 beat drivers -> 62 BPM raised-cosine simple expression, phase offset 15.76 so squeezes peak at 6.15 s ("power"), 9.04 s ("muscles"), 19.68 s (ejection); scene 3 camera offsets halved; macro MOVIE strip muted (not deleted); camera rides beside 'Pulmonary artery • continuous 1' 14.55-16.2 s then into the lung, then follows the pulmonary vein back; 260 lung-artery cells get material 'R27d • lung-bound cells blue to red' (colour by |x|: blue near the heart, red past x 1.08).
- Grain = all 133 materials use DITHERED transparency + one viewport sample; final Cycles render is unaffected. Preview recipe: DITHERED for opaque parts, BLENDED (in memory only, never saved) for see-through parts; BLENDED hides the cutaway interior on the solid heart.
- Preview: review/R27d_preview_10fps.mp4 + review/R27d_full_clip_every_half_second.png. Watch-outs: 8-13 s and 17-19 s busy with vessels around the see-through heart; dive into the artery at 14.3-14.55 s is fast (about 24 units/s).

## R27e/R27f, 2026-10-02 night
- Nick: 8-10 s movement disliked; "everything is translucent"; subject must be focused and lit, not see-through; heart must beat from the beginning like Zack's. Zack's clip now at ~/Desktop/heart-r24/reference_zack/zack.mp4 (29.7 s); sheet reference_zack/zack_sheet.png.
- Measured first-hand: Zack's beat period 0.967 s (62 BPM, autocorrelation of 6-10 s close-up). Zack keeps the heart SOLID throughout, colours one chamber, shows blood as blue/red blobs inside the chambers, no vessel network.
- Bug found: all 161 squeeze shape keys had slider_max 1.0, so every hard beat above 1.0 was clipped (since R27). R27f uncaps to 2.0, beat 1.3 (R24's tested value), hard beats 1.75 on power/muscles/ejection.
- R27e (tools/make_r27e.py): see-through only 7.5-8.75 s (blood flowing), 13.45-17.95 s (lungs and return), 20 s on; new control muscle_glow drives wall emission 0.22+mg*(0.45+1.4*squeeze), on 8.7-10.15 s; calm camera 7.3-10.4 s (max 2.4 u/s).
- Preview: review/R27f_preview_10fps.mp4, review/R27f_full_clip_every_half_second.png. Measuring the beat headless needs bpy.context.window.scene = heart scene, otherwise driver results read 0.

## R27g/R27h, 2026-10-02 night
- Nick: no ring; heart beats harder on "power is necessary"; at 0:08 "keep the blood flowing" flow out over the whole body; at 0:14 highlight the lungs.
- tools/make_r27g.py: 3 ripple rings hidden; hard beats at 6.15 and 7.12 s (1.85), 9.05 s, 19.68 s; camera 7.3-9.6 s pulls out to the end-of-clip body framing (dist 17.4 at 8.0 s) and back to 1.7 by 9.6 s (max 32 u/s); peripheral_flow, systemic_detail, systemic_front 0->11, context_reveal 0.9 during 7.55-9.15 s; new control lung_glow adds opacity + pink emission to 4 lung materials.
- tools/make_r27h.py: lung glow only 13.45-14.5 s (inside the lung it washed the frame pink).
- Current file: r27/Heart_R27h_work.blend. Preview: review/R27h_preview_10fps.mp4 + sheet. tools/build_preview.py FLIPDIR NAME builds sheet + 10 fps frames.

## Zack beat analysis (measured 2026-10-02 from ~/Desktop/How The Heart Pumps Blood 🤨.mp4, 30 fps)
- Method: OpenCV feature tracking, per-frame similarity scale, camera trend removed with a 29-frame moving average; same method on our heart with the camera locked (viewport frames, geo 391-451). Data: reference_zack/zack_scale.json, ours_beat.json.
- Rate: 0.93-1.07 s per beat in all four shots (59-64 BPM). Ours 0.968 s: matches.
- Shape: per beat one fast move (0.15-0.2 s) and one slower (0.5-0.8 s), no flat pause. Whole-heart shot 10.53-10.80 s, frame by frame: the fast move is the squeeze, whole outline shrinks toward its centre, then refills slowly. Close-up direction ambiguous (camera push + motion blur).
- Size: about 6-9% per beat where the camera is steady; readings with colour changes or pushes are unreliable. Ours locked: about 1.5-3.5%. Ours also has a ~0.3 s flat rest and mostly shortens top to bottom.
- Files: review/beat_zack_vs_ours.mp4, reference_zack/zack_frame_by_frame.png.

## R27i/R27j: Zack's beat, 2026-10-02 night
- Nick: "i love the way his heartbeats".
- tools/make_r27i.py: 97 drivers -> amp*(.5-.5*cos(2*pi*min(P/.42,P/1.58+.367089))), offset 17.79 (peaks unchanged at 6.15/7.12/9.05/19.68 s): squeeze 21% of the beat, refill 79%, no pause. Strength 1.5, hard beats 2.05. Root scale/location drivers shrink the 88 heart parts ~3.5% (4.8% on hard beats) toward C=(0.14,0.26,0.05)-ish so vessel joins move under 2 cm.
- Two hidden clamps found and fixed: squeeze keys slider_max 1.0 (fixed R27f) and contraction_strength property max 1.5 (fixed R27i). Hard beats in R27f-h were therefore capped at 1.5.
- Measured, camera locked, glows muted in memory: 0.967 s per beat, 7.7% size swing, squeeze 0.23 s. Zack: 0.93-1.07 s, about 6-9%, squeeze about 0.2 s.
- Attachment check at 2.05 (6.15 s): vessel joins fine; a few chamber blood cells show past the wall at the tip for a frame or two, close-up only (left alone). review/attach_check.png.
- tools/make_r27j.py: heart solid through "power is necessary to"; see-through starts at 7.5 s.
- Current file: r27/Heart_R27j_work.blend. Previews: review/R27j_preview_10fps.mp4, sheet, review/beat_zack_vs_ours_new.mp4.

## R27k: cells outside the heart, 2026-10-02 night
- Nick spotted blood cells below the apex. Cause: R22 base still had the long 'Right atrium through valve to right ventricle' route (R26's fix was on R24). tools/make_r27k2.py trims path + blood-volume tube to 35 points; 60 follow-path cells stay inside.
- Check method (no scipy in Blender): dump.py exports heart verts + intracardiac blood objects every 3 frames to npz; system python tests against the heart's convex hull. Before: 62 objects outside, up to 14 cm. After: 0 cells; only the tube's entry end touches by 4-11 mm on beat peaks.
- Beat comparison (same tracker, camera locked): size 7.3% ours vs 6.9% Zack, rate equal; Zack rocks about 1.5 deg per beat, ours 0.2 deg; Zack's sideways/up-down motion does not repeat with the beat (camera). Nick still says the beat "needs a bit more work": asked him what.
- Current file: r27/Heart_R27k_work.blend.

## R27l: walls squeeze inward + top first, 2026-10-02 late night
- Nick: "the walls should squeeze inward like his. it also feels like the heart is squeezed in two places".
- Existing 'Ventricular squeeze' was mostly apex shortening (1.8 cm axial, <0.7 cm inward, nothing in the top half).
- tools/make_r27l.py adds two shape keys to all 88 heart parts from one shared field in root space (heart long axis by PCA, apex at negative h):
  'R27 • ventricle walls inward' (lower heart, inward move k*r*exp(-(r/0.28)^2), k 0.30, max 3.6 cm, inner walls ~2.3x the outer surface) on the beat;
  'R27 • atria squeeze' (upper heart, k 0.20, max 2.2 cm) 6 frames (0.2 s) earlier. Zack's top-before-bottom lag measured 0.2-0.33 s but noisy (corr 0.26-0.39).
- Measured with camera locked: whole heart swing 10.5% (Zack 6.9-8.6%), bottom 16.9%, top 6.3%; top-first lag shows only ~0.06 s in tracking because the top region also carries the ventricle base.
- Checks: vessel joins fine at the hardest squeeze (review/attach_check_l.png); cells outside: one cell <1 cm for 3 frames on hard beats; tube entry at the right atrium up to 3 cm (vein entering, accepted).
- Muting glow fcurves for clean captures does not always take; glows sometimes stay on in captures (unresolved, cosmetic for tests).
- Current file: r27/Heart_R27l_work.blend. Previews: review/R27l_preview_10fps.mp4, sheet, review/beat_zack_vs_ours_walls.mp4.

## Next action
Nick reviews R27l (walls + two-place beat). Open offer: Zack-style blood blobs inside a solid heart for the two chamber moments.

## Resume line
Resume heart clip: read ~/AgencyOS/handoffs/2026-10-02-heart-clip.md and continue from the next action.
