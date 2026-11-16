---
name: approval-before-3d-generation
description: "Always get explicit approval before running generate_3d (and any paid re-gen); these spend the user's credits"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c24a4314-f2ed-45fe-862a-727106b3dbeb
  modified: 2026-07-29T20:45:05.486Z
---

Never call `generate_3d` (or re-run a paid image/3D generation) without the user's explicit "yes" first. The pipeline gate is: generate the nano-banana image → show it to the user → WAIT for explicit approval → only then convert to 3D. Same gate before any re-generation.

**Why:** Each `generate_3d` call spends real credits on the user's account. In the vault-room session I fired 6 meshes (gold bars, deposit wall, cash x2, cart x2) straight from images without pausing — the user was rightly angry ("you keep generating 3d models without my approval").

**How to apply:** Treat nano-banana image generation as the approval checkpoint. Present the still, stop, and ask. Do not batch image→3D in one motion. Preferred flow for environments: nano-banana concept of the whole scene first, approve, then build asset-by-asset, each 3D conversion gated. See [[machine-and-render-workflow]] and [[zackd-corpus-breakdowns]].

**STANDING EXCEPTION (2026-07-29): the overnight factory.** Nick authorized the [[zackd-overnight-factory]] scheduled task to auto-generate WITHOUT per-asset approval, capped at 100 credits per nightly run (about 2 mesh conversions plus their image tries). Inside that task only: 3 nano-banana image tries to pick the best, then ONE generate_3d on the winner, and it must stop and queue to NEEDS_YOU if the next paid call would cross 100. This exception is scoped to that scheduled run only. In any normal interactive session the per-yes rule above still holds.
