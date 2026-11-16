---
name: hero-character
description: "Bald bearded hero (Zack-style human) on clip-b ~/Desktop/hero: build order of the scripts, latest files, what is left vs Zack's frames."
metadata:
  node_type: memory
  type: project
  originSessionId: 6d168762-61ef-4d14-9020-9cfd3ffc7c96
  modified: 2026-10-12T11:02:05.158Z
---

Zack-style human, built 11 to 12 Oct 2026 on clip-b (37.27.148.115) in `/Users/nick/Desktop/hero` (tools/, data/, blend/, review/), rendered on the RunPod workbench. Zack refs: 10.18 s (hand on stomach) and 23.64 s (hand on throat).

Build order (each script saves a new blend): shorts_v2 -> hero_look (expression keys, salt-and-pepper beard, skin tone) -> apply_hand_detail (painted hand textures from paint_hand.py, bump, arm hair, thicker fingers) -> muscle.py (HumGen livekey deltas as plain data; final mix "G": Chest 1.6, Chest Width -0.5, Back -0.6, Shoulder 0.3, Biceps 0.7, Triceps 0.5, Forearm 0.5, Belly -0.3) -> reload_height (abs + pec lines from abs_export + paint_abs.py) -> pecs.py 12 mm -> pose_fk.py painful|throat -> pose_match.py posed_*.
Latest: hero_bb_look11.blend, hero_pose15_*.blend (12 Oct). Render env: BG_FLAT=1.35 BG_WIN_VIG=0.85,1.2,0.45 BG_CELL=0.27,0.6,0.86, KEYW 690 (+KEYC 1.0,0.68,0.40) painful, 615 throat.

Learned: big lat/waist keys (male_muscular, Waist Thickness) made a bodybuilder caricature; Zack's torso is straight-sided with mass in pecs and arms. Thumb spread must be judged from the middle knuckle to the thumb tip, not from the wrist. Key light "spread" blows out highlights.
Related: [[compare-to-reference-after-stills]], [[zack-clip-skill]].
