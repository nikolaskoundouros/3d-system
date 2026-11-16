# Splinters v4/v5 handoff (updated 2026-10-17 afternoon)

## What this session is doing
Nick asked for a new Splinters preview clip ("dont stop until you give me a new preview clip", then "what are you
waiting for? go") after rejecting v3 ("what the fuck is this finger? also why is there a character in our clip? ...
try not to create your own theories and problems"). v4 copies Zack's shots onto Nick's locked VO (vo_final.wav, 20.12 s)
and invents nothing. Every set is built by script on the Mac with stills against Zack's frames; the clip gate on clip-a
must pass basics, motion, details, claude, sent; then Nick types "approve" and the preview renders.

## Decisions (with why)
- VO onto Zack's shots, nothing added (Nick's rule, in the zack-clip skill "Copy Zack, invent nothing"; synced to
  /opt/clip-gate/process.md md5 9e76148a by Nick on 17 Oct; brief re-run = seq 3).
- Hand: HumGen man masked to hand + forearm + olive cuff; post = Poly Haven dark_wood (CC0, on disk) greyed to Zack.
  A procedural wood attempt looked worse and was reverted (smallest fix first).
- World light off on hand and surface sets (blue tinted wood and skin); Zack's blue as a gradient background.
- After 3 basics FAILs (#2, #4, #5) Nick got gate6_sheet.jpg and an A/B ask (keep iterating vs he judges / loosens the
  bar). No answer yet; fast fixes continue meanwhile.

## Files (Mac scratchpad /private/tmp/claude-501/-Users-nick/6d168762-61ef-4d14-9020-9cfd3ffc7c96/scratchpad/splinters/)
- build_hand.py (on moved_from_clipa/finger_v2.blend), build_surface.py (on blend/scalp_c4.blend), build_section.py +
  anim_section.py, edit_v5.py (cut, 619 frames), mix_v5.py, still.py, pack_blend.py, make_basics.py, make_sheet.py,
  render_gate7.sh, run_motion_v4.sh, run_gate_v5.sh. Old versions saved as *_nN.py.
- Pass 7 blends: blend/hand_n21.blend, blend/surf_n22.blend, blend/sec_n18a.blend; stills -> gate7/.
- clip-a ~/Desktop/splinters: blend/{hand,surface,section}_v4.blend (pass 6 packed), gate/v5/stills + basics.json,
  tools/, review/run_gate_v5.sh (basics -> pod motion -> motion -> waits for gate/v5/details.json -> details -> claude
  -> sheet -> sent). Disk ~1.6 GB free.
- Zack analysis page: ~/Desktop/splinters-analysis/zack_visual_analysis.html.

## Rules stated this session
"try not to create your own theories and problems"; analysis "on the visuals. detailed ... textures, the uv maps, the
skin quality, the biology details, the fabrics of the clothes, the lighting, everything needs to be perfect";
"dont stop until you give me a new preview clip"; "what are you waiting for? go".

## Open loops
1. BLOCKER for Nick (asked 17 Oct ~15:08): basics #6 FAILED (pass 8, 22 findings) and the gate is deadlocked: verdicts
   #2, #5, #6 end with "stills cannot verify transitions, provide a captioned playback", but the pod refuses the motion
   render until basics passes. His pick: (1) motion test before basics (root change; my pick), (2) he judges basics from
   ~/Desktop/splinters-analysis/splinters_pass8_sheet.jpg, (3) keep iterating.
2. Pass 9 (hand_n25, surf_n24, sec_n20a) rendering to gate9/ + trans9 (24 stills incl. 2 transition mid-points); then
   pack_blend.py -> pack/*_v4.blend, copy to clip-a blend/ (md5), stills -> gate/v5/stills, crops via render_details8.sh
   (edit blend names) -> gate/v5/crops, basics.json from make_basics.py, relaunch review/run_gate_v5.sh.
3. After sent: Nick sees the sheet, types "approve"; preview at PCT ~67 / SPP ~24 on the pod with edit_v5/mix_v5.

## Resume line
Resume Splinters: read ~/AgencyOS/handoffs/2026-10-16-splinters-v4.md and continue from open loop 1.
