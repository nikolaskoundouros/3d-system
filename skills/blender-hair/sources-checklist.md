# Sources checklist for hair (15 Nov 2026)

Rule of use (Nick, 15 Nov: "i also sent you articles and blender docs. why didnt you use everything?"): every source is a checklist, not a
quote bank. Before each pass, go down this table, apply the open rules or reject them in writing with a reason. Status checked 15 Nov
against results.tsv and hair2_locks.py. "read" means I read it first-hand; the tutorial rows rest on the hair-research page plus two
re-checked frames and transcript lines.

## Blender 5.3 manual (offline copy on the box: bman -p <path>); pod runs 5.2.2
| Rule | Status | Evidence / why not |
|---|---|---|
| Guides by hand, Interpolate Hair Curves (Poisson Disk) | NOT USED | modifier inputs cannot be set from Python in 5.2.2 (properties.inputs empty). Not tried: a wrapper node group built in Python with the values inside it |
| Clump / Curl / Braid + one Create Guide Index Map | NOT USED | same reason; my children + clump factor are a hand-made stand-in |
| Roll Hair Curves for curled-under ends | EMULATED in code | node itself not used |
| Smooth / Frizz / Hair Curves Noise / Blend / Straighten / Trim / Shrinkwrap Hair Curves | NOT USED | Shrinkwrap would replace my clear_surface push-out |
| Set Hair Curve Profile (width root to tip) | EMULATED | per-point radius |
| Curves sculpt brushes (Add, Comb, Puff, Pull Tips, Density) | TRIED | Add worked by mouse; Comb did not respond |
| Principled Hair: Huang, aspect 0.65-0.9, no Coat, roughness not too low, Random Color/Roughness | USED | strand materials |
| Hair Dynamics (closed collider only) | NOT USED | needs a closed body collider; shirt is open |
| Deform Curves on Surface (carry hair onto the posed body) | NOT DONE YET | hair is built in rest pose; needed before any posed shot |
| Curve geometry: bevel object, Fill Caps, Taper Object, Factor Start/End | PARTLY | bevel object used; Taper Object and Factor Start/End not used |

## yelzkizi articles (hair cards in Blender, read 15 Nov)
| Rule | Status | Evidence / why not |
|---|---|---|
| Scalp base under everything, no gaps | USED | Hair2_Cap (dark cap, ear/face free) |
| Layers: inner (broad, opaque), mid, outer (smaller), stray strands | USED | locks (inner), strands (outer), floating strands (stray) |
| Opaque roots, wispy tips, vary lengths | PARTLY | tips fade, lengths vary; roots not made opaque |
| Abrupt card edges show as lines: fade tips, randomize edges | USED | tip taper/transparency, staggered ends |
| Perfectly mirrored hair looks unnatural: break symmetry | PARTLY | random target jitter; the left and right sides are still near-mirror |
| Flat card normals look stripy: edit normals to head shape | N/A for strands | open for ribbons |
| Hair floating above scalp / clipping: cards just below scalp, shrinkwrap | PARTLY | clear_surface 7 mm; ribbons now 3 mm inside the strands |
| Too few cards = gappy/webbed, too many = moire; 50-200 cards | DIFFERENT | ~900 ribbons + ~100k strands (offline render, not game cards) |
| MAIN METHOD: flat strips with a strand alpha texture | NOT USED | never tried; it is exactly the smooth, soft-sheet look of the reference |
| Colour: grayscale + tint, mask for darker roots | USED | ombre via Hair Info Intercept |

## Tutorial "Hair With Curves" (Blender 2.79; frames 2:36 and 18:01 re-checked)
| Rule | Status |
|---|---|
| One curve per lock, shared grooved bevel | USED |
| Width and tilt per point | USED (tilt random; the tutorial aligns tilt to the scalp at the back: NOT done) |
| Noise along the lock drives colour and bump; root gradient | USED |
| Tips dissolve via gradient x noise into Transparent | USED |
| Floating strands as separate curves | USED |
| Mirror modifier for the back of the head | NOT USED (and the article says break symmetry) |
| Build layers so curves lie on top of each other | USED |

## Measured checks (new, 15 Nov): scripts scan_render.py + patchscan.py
Ribbons showing through strands and skin showing, per 40 px patch, over five hi-res views (top, crown, back, ear, front). Run after every pass.
Before to after (ribbon % of hair pixels): back 19.3 to 5.3, ear 17.8 to 3.6, crown 6.5 to 2.6, top 1.5 to 0.4.
