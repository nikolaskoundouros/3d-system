---
name: no-em-dashes
description: "Standing law - no em/en dashes in any deliverable, ever; use hyphens or restructure"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 05aa2051-09c3-4fad-9900-01a6869ab197
  modified: 2026-07-26T05:45:13.693Z
---

Nick bans em dashes and en dashes in every deliverable (docs, reports, content, code comments). A PostToolUse hook (~/.claude/hooks/emdash-check.py) blocks writes containing them.

**Why:** House style law; em dashes also read as AI-generated tells in client content.

**How to apply:** Write with plain hyphens ("word - word") or restructure the sentence. Subagent-written files bypass the hook, so sweep any agent-produced deliverables with a dash-replace pass before calling work done. Related: [[fresh-start-blender]].
