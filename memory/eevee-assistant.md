---
name: eevee-assistant
description: "Eevee, the voice assistant at ~/AgencyOS/eevee (port 4730) - her two-mode design, and the ElevenLabs voice upgrade Nick approved on 2026-08-13 but deferred."
metadata: 
  node_type: memory
  type: project
  originSessionId: 3781bdba-5dbc-4fba-9b2c-2c2460208a42
  modified: 2026-08-13T09:08:12.367Z
---

Eevee replaced JARVIS as the assistant Nick talks to out loud. Built 2026-08-12 at
`~/AgencyOS/eevee/` (server.js + public/index.html), port 4730, launched with `/eevee`.
The older JARVIS console still exists at `~/AgencyOS/console/` on 4720 and both can run at once;
they share the task board at `~/AgencyOS/console/tasks.json`.

**The design that matters: two modes, hard separated.**
Conversation runs `claude -p` with read-only tools, so she cannot write or run anything while
talking. To do something she emits a fenced `eevee-action` JSON block, which the interface renders
as an approval card. Only Nick's click or spoken "yes" spawns a second `claude -p` with Write, Edit
and Bash, in a cwd forced under `~`. Do not give the conversation mode write access; the separation
is the whole point, and it is the same reason [[show-before-approve]] exists.

**PENDING, approved but deferred (2026-08-13):** wire ElevenLabs as a second voice engine with the
macOS `say` voice as fallback when no key is present. Needs an API key on disk for the standalone
node server (it cannot reach session MCP tools). Cache audio per line so repeated phrases cost
nothing. Reason: the macOS voice sounds robotic, and Nick's Mac has zero Premium or Enhanced voices
installed, so `say` is stuck on the legacy compact Samantha until he downloads one from
System Settings, Accessibility, Spoken Content, Manage Voices.

**Known limit, already told to Nick:** browser speech recognition is transcription, not speaker
identification. Any voice in the room can command her, and Chrome sends that audio to Google.
A real voiceprint lock is a separate build he has not asked for yet.
