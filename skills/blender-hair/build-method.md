# Hair build method, from scratch (written 15 Nov 2026)

Used by /blender-hair for a new head. Each step names the manual page it comes from (paths under the Blender 5.3 manual,
read first-hand on 15 Nov from the offline copy on the box: `bman -p <path>`), the mode and tool, the setting, the check against
the reference, and the line we record. "Manual says" is quoted or paraphrased from that page. "My plan" is my choice and is
tuned and recorded, never presented as the manual's. The manual has no section numbers, so pages are cited by path.

Pod runs Blender 5.2.2, manual is 5.3. The same pages exist on docs.blender.org under 5.2 (HTTP 200, 15 Nov), but that does not
prove the nodes exist in 5.2.2: step 0 checks on the pod. Pull Tips is Snake Hook in the manual.

## The loop at every step (Nick, 15 Nov)
Try the step, put 4 views beside the reference, list every difference. Match: next step. No match: find out why, read the
page again. Still unclear: write the problem alone, research how to solve that problem, try again. Every try is one row in
~/Desktop/mom-character/results.tsv: `date <tab> step + exact change <tab> reference check <tab> result (worked / didn't, why)`.

## Plan: five separate Empty Hair objects (my plan, so each part is tested and recorded alone)
Top, Bangs, Pieces (face framing), Lower, Bun. Each has its own guides, modifiers and material.

## Step 0. Setup and checks (once per pod)
- Page `modeling/curves_new/primitives` (Empty Hair): adds an empty curves object, "Assigns the active object as the Surface",
  parents to it, adds a Geometry Nodes modifier to deform the curves on the surface. Select the head mesh, add Empty Hair.
- Page `modeling/curves_new/properties`: set Surface UV Map on the curves object (needed by Interpolate Hair Curves).
- Page `sculpt_paint/curves_sculpting/introduction`: "Curves Sculpt tools only use the original mesh of the surface object and
  don't take its modifiers into account". So groom with the head in REST pose. Header: Use Sculpt Collision on ("Prevents the curve
  segments from passing through the Surface Object"). Mirror: my plan X on for Top, Lower, Bangs; off for Bun.
- Check on the pod (connector, read only): do node groups for Interpolate, Curl, Braid, Roll, Hair Dynamics exist in 5.2.2?
  Does the head have a closed body mesh for collision? Is Principled Hair "Huang" there?
- Tool for brushes: real mouse (drag.sh). One test stroke of each brush we have not proven (Puff, Pull Tips, Pinch, Smooth).
Record: version, which nodes exist, which brushes responded.

## Step 1. Top guides (Curves Sculpt Mode, object Top)
1. Add Curves (`brushes/add_curves`): "Count" curves per click, Curve Length, Points per Curve, Curve Radius. Roots follow the
   surface normal. My plan: few guides first (start about 40, tuned), roots in a band from the hairline back over the crown.
2. Comb Curves (`brushes/comb_curves`): moves control points, keeps segment length; Curve Falloff is "tip to root" so roots stay.
   Stroke from the hairline back and up toward the bun (the green arrows in refs/flow_traced.jpg).
3. Puff Curves (`brushes/puff_curves`): "Makes the curves stand up", aligns with the surface normal, points never move closer to
   the root. Dab at the crown for lift (reference 18.0 s and 37.5 s show a lifted crown).
4. Snake Hook (Pull Tips) (`brushes/snake_hook_curves`): extends a curve only by its tip. Use to bring tips to the bun position.
5. Smooth Curves (`brushes/smooth_curves`): makes neighbouring segments "more parallel".
6. Add Curves again with Interpolate Length / Shape / Point Count on (`brushes/add_curves`): new curves follow nearby guides, "already combed".
   Density Brush (`brushes/density_curves`): Density Mode Auto, Distance Min sets root spacing.
Check: flow matches the green arrows; crown lift matches 18.0 s. Record: Count, guide number, which brush strokes, what moved.

## Step 2. Top dense hair (modifier on Top)
Page `modeling/geometry_nodes/hair/generation/interpolate_hair_curves`: the node fills dense hair from guides. Settings: Distribution
Method Poisson Disk (even spacing), Density, Density Mask (paint where hair grows), Interpolation Guides (how many nearest guides),
Distance to Guides, Follow Surface Normal, Resting Surface (on, because Deform Curves on Surface comes after), Seed. Output Guide Index.
Then Set Hair Curve Profile (`hair/write/set_hair_curve_profile`) for root to tip thickness. Cycles Curves Shape 3D Curves.
Check: coverage and flow at 4 views. Record: density number, Interpolation Guides, Distance to Guides.

## Step 3. Sheen (material on Top)
Page `render/shader_nodes/shader/hair_principled` (checked word for word against the saved page).
- Model Huang, Aspect Ratio in 0.65 to 0.9 (manual: Caucasian), needs curve normals (curves hair has them, particle hair does not).
- Roughness: manual (Chiang) says too low looks "almost metallic" with fireflies; too high is Lambertian. Old baseline was 0.13.
  My plan: test ladder 0.13, 0.25, 0.4, 0.6, one render each, same light. The video's 0.42 to 0.64 was an Anisotropic BSDF on
  thick ribbon locks, not this shader: not a target, only a reminder that low was wrong.
- Coat is for fur ("Simulate a shiny coat of fur"): 0. Random Roughness small.
Check: broad soft sheen band like reference 18.0 s and 37.5 s, no thin white streaks. Record: model, aspect ratio, each roughness and its look.

## Step 4. Colour
Same page: Color Parametrization Melanin Concentration (blonde about Melanin 0.25 at Redness 1 per the page; brown 0.75). Honey on top,
darker roots and underside: my plan a Hair Info or position gradient driving Melanin, plus Random Color for strand variety.
Check: back and underside darker than top (35.0 s, 62.0 s). Record: melanin, redness, gradient, random color.

## Step 5. Bangs and platinum streaks (object Bangs)
Same as step 1 and 2 with the part near the centre, guides combed down and out to the cheekbones (reference 64.5 s, 55.5 s).
RESEARCH GAP: the manual pages above do not say how to make 2 to 3 chunky lighter streaks. Idea to test (not verified):
mark a few guides, carry the mark through Interpolate Hair Curves via Guide Index, read it in the shader to lighten them. Selection
Paint (`brushes/selection_paint`) paints curve masks. If that fails: separate small Empty Hair object for streaks with its own material.
Record: which method, result.

## Step 6. Bun (object Bun), two ways, compare both to reference 62.0 s and 35.0 s
- A, locks (video, 2.79): 6 to 10 paths, shared grooved bevel, twist per point (research chat's reading, two frames re-checked).
- B, manual nodes: Braid Hair Curves (`hair/guides/braid_hair_curves`: Factor, Subdivision, Braid Start, Radius, Frequency =
  how tightly strands wrap, Thickness, Flare, Hair Tie) or Curl Hair Curves (`hair/guides/curl_hair_curves`: wraps curves around
  guide curves; Subdivision higher = smoother, Radius, Frequency, Curl Start). Both want a Guide Map: Create Guide Index Map
  (`hair/guides/create_guide_index_map`), one map shared by every guide node.
Check: reads as a small dark twisted knot high on the back of the crown. Record: A or B, numbers, which looked closer and why.

## Step 7. Lower half and face-framing pieces (objects Lower, Pieces)
Add Curves, Comb straight down to the collar; Grow/Shrink (`brushes/grow_shrink_curves`) for length; Cut Curves
(`brushes/cut_curves`, Strength "creates a hairstyle that is less uniform"); Pinch (`brushes/pinch_curves`) for separated ends.
Ends: Roll Hair Curves (`hair/deformation/roll_hair_curves`): Roll Length (from the tip), Roll Radius, Roll Direction (axis), Retain Overall
Shape, Subdivision; inward at the back, outward on the front pieces (reference 72.5 s, 35.0 s). Clump and Curl share one Create Guide
Index Map. Smooth Hair Curves and Hair Curves Noise for finish.
Optional drape: Hair Dynamics (`modeling/geometry_nodes/simulation/hair_dynamics`): experimental, closed-mesh colliders only, Substeps
under 20, raise Constraint Iterations, Residual error 1 or less. Her shirt is an open mesh: use the body.
Check: 35.0 s back and 72.5 s three-quarter. Record: roll numbers, what the ends did.

## Step 8. Crown wisps, then pose
A few extra Add Curves strands plus Frizz Hair Curves / Hair Curves Noise at low Factor (`hair/deformation/frizz_hair_curves`).
Pose: Deform Curves on Surface (`modeling/geometry_nodes/curve/operations/deform_curves_on_surface`): needs surface_uv_coordinate and
rest_position; if the body has Subdivision Surface set UV Smooth to None. Snap to Deformed Surface or Snap to Nearest Surface after changes.
Check: the 4 clip poses. Record: what moved wrong.

## After the build
Settings that worked go into a script in ~/Desktop/mom-character/scripts. One line per lesson goes into SKILL.md "Learned".
