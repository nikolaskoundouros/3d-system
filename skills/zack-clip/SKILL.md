---
name: zack-clip
description: How Nick makes a Zack D. Films remake in Blender with Claude, as he ran it in the heart, ingrown hair and stitches chats (2 to 6 Oct 2026). His rules in his own words, the order of work (script, stills, one sequence at a time, final on the desk) and the tools that exist. Use for any new clip, any "resume <clip>", and any 3D explainer video. The skill is the spec. Add no rule he did not give.
argument-hint: [clip topic, or "resume <clip>"]
---

# Zack clip

Built from Nick's own messages in the chat that made the heart, ingrown hair and stitches clips. Every quote below is his.
Reference project with the whole pipeline: ~/Desktop/stitches (tools/, refs/, CLAUDE.md, review/). Memory rules apply on top.

## How the clips run (Nick, 9 to 10 Oct 2026)
- Together, one clip per session: "when we start with analysis, VO, stills, and run a few checks and iterations together
  the process is smooth and when we do a clip at a time. but as soon as i tried automating and putting the things on the
  desk and let them run, we fucked the whole thing up".
- Each clip has its own box and its own GPU: "each clip needs its own cpu and gpu and should not depend on my laptop".
  clip-a runs on 46.62.230.121, clip-b on 37.27.148.115 (4 GB each, swap on); each rents its own pod with
  ~/Desktop/render-desk/bin/workbench. Video encodes and 1080p compositing run on the pod, not on the box.
- Nick talks to the session directly from his phone (Remote Control). No relays, no Telegram.
- Never move past a step he has not locked: "you broke the process. why? we were still doing the fade".

## Which model does what (Nick, 15 Oct 2026)
"i want the first analysis spec, ideation etc. to be done with opus5.5 extra and then run it through astra also at high
for the details etc. then continue with claude."
- Analysis, spec, ideation: Claude Opus 5.5 at extra-high effort (`--model claude-opus-5-5 --effort xhigh`).
- Then the same spec through GPT-6-Astra at high for the details (on clip-a: `~/.local/bin/codex exec -m gpt-6-astra
  -c model_reasoning_effort="high"`, signed in with Nick's ChatGPT plan).
- Then Claude carries on with the build. Each is its own session; the subscriptions are never pooled behind a script.

## Checkpoints: the clip gate (Nick, 16 Oct 2026)
Splinters preview v3 ("bro this is absolutely horrible") broke because every check was voluntary and the builder judged its
own work. Nick: "first is the analysis. that needs to be fed into the model we're working with. then after the stills, the
model should check the basics. then the details. then the motion. then we send to claude for more checks. then you give
me the still render and then i say approve for you to go to the preview render" ... "you can take even two hours if you
need to if that means a better outcome. the process has to be bulletproof though. also build a something that enforces
the checks." Agreed: motion before details; the builder never checks itself; his approval typed in chat ("b").
- Order, enforced on clip-a by `clip-gate` (reviewer service clip-gated, user clipgate, which alone holds the second
  Claude and ChatGPT logins): analysis -> basics -> motion -> details -> claude -> sent -> approved.
  analysis: Opus 5.5 xhigh then Astra high write the brief (ledger/<clip>/brief/); every later check scores against it.
  basics / motion / details: Astra high. claude: second Claude, Opus 5.5 xhigh. sent: the still render for Nick.
  approved: Nick's own chat message starting "approve" (the gate.py hook forwards it; "approve final" for a final).
- Each stage: write a manifest (blends by absolute path, stills with their seconds and Zack's matching seconds, the rough
  motion mp4, full-size crops with Zack's matching second and region), `clip-gate submit CLIP STAGE manifest.json`, then
  `clip-gate wait CLIP STAGE`. A FAIL lists findings with second, place and fix: fix them all, then start again at
  basics. Any change to a .blend after a pass also starts again at basics.
- The GPU tool refuses a moving-picture render unless the gate clears those exact .blend files: a rough motion test
  (PCT <= 30, SPP <= 8) needs basics; a preview needs Nick's approval; a final needs "approve final". Render commands
  name every .blend by absolute path; scenes are built, pulled home, reviewed, and only then rendered.
- `clip-gate status CLIP` shows where a clip stands. Nothing reaches Nick before claude PASS except the still render the
  gate records as sent.

## Copy Zack, invent nothing (Nick, 16 Oct 2026)
After the Splinters v3 preview showed a thumbs-up hand on grey stripes and a panicking face that Zack never has:
"bro what the fuck is this finger? also why is there a character in our clip? do the analysis step by step. try not to
create your own theories and problems. thats why it is taking so long". Then, on the analysis: "i want the analysis on
the visuals. detailed" and "see the textures, the uv maps, the skin quality, the biology details, the fabrics of the
clothes, the lighting, everything needs to be perfect".
So every beat of our clip uses one of Zack's shots; where our words differ from his, use his nearest shot. Add nothing
he does not show: no characters, extra effects, extra arrows or story beats of our own.

## What Nick is after
- Order of attention: "what i care about is the motion, the pacing, the feel, the colors". Details nobody sees at playback wait.
- Movement: "we need movement and camera action every 0.7-1s. with zooms, orbits etc."; "when we highlight red part, we zoom and
  orbit to the red part". A stretch where nothing happens makes viewers "churn" (he flagged a 5 s hold and a 3 s hold).
- Focus: the thing being talked about is lit and solid: "the muscle and the tissue need to light up and not be translucent".
- Detail: "this looks very mediocre. there is absolutely no detail" is a fail; "the biology has to be way more detailed".
  Biology lives inside the real wound or organ, never floating on a backdrop: "shouldnt they be in the leg wound we already have?"
- Look: Zack's light blue behind cutaways ("for background use the zack light blue"), his captions, his beat ("i love the way his heartbeats").
- Truth: check the biology before building it (the scar stays for weeks, so the ending shows it).
- Loops: where the story allows, the last second returns to the opening framing ("riding the bike so then we can loop the beginning").
- Texture at full quality before the final: "do you remember how in the heart clip we basically had to go over and over until we
  got the HQ version of the heart?"

## What irritates him
- Waiting blind: "updates?", "how long until the stills are ready?". Give an ETA when a render starts and a line when it lands.
- Fix-and-rerender loops: "you cannot keep making mistakes and rerendering. it is taking too much time."
- Renders he did not ask for: "with what rule did you decide to run the full render?" Flagged is not approved.
- Not knowing what changed: "did they change and need rerendering i didnt understand". Say which sequences changed and whether
  what he is about to see is current.
- Dead time: "can we work on something else while this is rendering?" Keep something moving that does not need Blender.
- Slow change loops: "why does it take so long to make these changes? i dont understand!!!" A change plus its check stills
  must take about a minute: work in the live session (Step 5), never rebuild the scene or reopen the file per still.

## Step 1. Pick the clip: remakes only
- "we only do zack d clips that already exist since our system heavily relies on comparing what zack does, doing it and then
  altering it a bit."
- Scan and scripts: ~/Desktop/zack-shorts (data/top30_scripts.json, scripts/scripts.md, shot breakdowns in scripts/remakes.md).
  He wants Zack's script beside ours: "i would need to also have zacks script there too so i can review both".
- Download the reference with yt-dlp ("always download without asking its ok"). One frame per second, looked at with the
  transcript. Beat timings into refs/beats.json.

## Step 2. Script and VO: Nick owns them
- Draft on Zack's structure; Nick cuts: "this is fluff, we dont want fluff at all"; "no full stops either, so i would use
  connectives such as and etc." A small change of story is fine (he moved the opening to a fall).
- Save his final wording exactly. He records the VO himself (ElevenLabs). Cut the dead pauses (tools/tighten_vo.py), play the
  versions back as voice notes in the chat, he picks ("the tight one is perfect!"). Word timings (tools/vo_words.py) drive
  shots, captions and sfx. An approved VO is never re-paced.

## Step 3. Project
- Start with ~/AgencyOS/bin/newproject. CLAUDE.md states the reference, the way of working, and what needs Nick (desk renders,
  deletions, publishing, paid generation).
- Copy the pipeline from ~/Desktop/stitches/tools: edit_list.py (the cut: file, frames, camera, dissolves), build_*.py (every
  scene built by script, headless), sheet.py + sheet_compose.py (stills sheet with seconds and the words spoken),
  render_preview.py + join_preview.py + seq.sh (one sequence as a low-quality mp4 with mix and captions), sfx_synth.py,
  audio_mix.py, captions.py, make_final.py + gpu/prepare_final.sh + gpu/run_final.sh + assemble.py (desk finals),
  spent.py + desk_pods.py (budget and pod checks), sky.py (Zack's sky behind a transparent render).
- refs/review_checklist.md: what reviewers fail (hands hold grips, sitting rests on the seat, scale, Zack look, captions, mix).
  The builder never reviews its own work.
- Characters: HumGen (he has the asset folder). Props and sets: Sketchfab and Poly Haven (keys on the Mac).
- 8 GB Mac: one Blender at a time, headless. Cycles everywhere (EEVEE hid the real look). Scenes with 4k skin maps fault the
  GPU and go on the CPU.

## Step 3b. Compare every still before anything else (Nick, 2026-10-08)
"lets go by comparing every single still again. this should be the first step of the process right after the VO and zack
analysis." Right after the VO and the Zack analysis, a word sheet: our frame at each key word beside Zack's frame at his
matching word (acid reflux: tools/word_sheet.py). Go through it pair by pair with Nick: what Zack shows, what we show, the
difference, the fix. The fixes go into the shot plan; no Blender work starts before this pass.

## Step 4. Build: stills before anything moves
- Design first, together, right after the VO: "design our sequences right after the vo together, then you make the stills in
  blender, and then we start making the sequences." A one-page shot list on his word timings (second, his words, what is on
  screen, camera move, Zack's frame at that second) is locked before any Blender work; taste calls are made on paper.
- Shot plan from Zack's beats and the word timings. Every spoken beat shows literally when it is said.
  "the script isnt connected to the graphics which is the biggest lesson today. the script needs to come first, everything
  around it designed around the script." The table (refs/shotplan.md: time, his words, the literal event, the camera) is
  locked on his word before any Blender work; a new idea goes into the table first, never straight into a render.
- Motion before detail: a low-quality motion test of the whole clip on his VO (one camera journey, dissolves to the man,
  no hard cuts) checked against Zack's file and locked before any look, simulation or glow work. The bar is not camera
  speed (measured: our failing v15 moved as much as Zack): it is a visible change in the subject on every key word, centred
  push-ins and pull-outs, eased moves, nothing frozen while words are spoken, X-ray dissolves between the man and his
  anatomy (Zack never hard-cuts). On the acid
  reflux clip the looks were perfected first and the clip still read as static ("as a user, i would scroll away").
- Small test before anything expensive: a liquid simulation runs a 10-second low-resolution test with a measured pass
  (liquid where it should be, nothing outside) before a full bake; a render longer than 5 minutes renders 3 frames first.
  Four full bakes failed on 2026-10-07 on things a small test showed in seconds.
- Spend: the GPU tool stops at WORKBENCH_DAY_CAP_USD ($6 a day, his to raise) and after 10 idle minutes; switch it off while
  talking. Infrastructure changes are tried on a dummy first, never switched on under a running GPU (the new 5 h cap killed
  one and lost its work). Every saved scene comes back from the GPU automatically (bin/live).
- Stills sheet with seconds, "from beginning till end so i can direct you with next changes", Zack's frame at the same second
  beside ours. "show me the still sheet so we can decide together."
- After every still, before he sees it: "after you make the stills, i need you to analyze to see if the reference is the
  same." Ours beside the reference at the same size and framing, part by part (body shape, where edges sit on landmarks such
  as the navel, materials, light); write down every difference and fix them all in one go: "if you spot problems, fix them in one go". Name only
  what needs someone else. He should not be the one spotting them (2026-10-12: he found a leaner waist, a band over the
  navel and a different fabric that I had missed, then saw me list differences and fix only some).
  Three checks on every character still, also his (2026-10-12): muscularity ("our guy is a bit skinnier. look at the
  references pecks and waist"); joints within their natural range ("look at the degrees of freedom of his wrist. our one
  looks weird"), wrist, elbow and neck measured, no kinks; and the fine detail, the part he cares about most: "the details
  of his hand. the nerves, the pinkish pigment in the fingernails, the bones that show. thats what makes zack great. the
  attention to detail." Crop ours and Zack's hand, face and skin at the same size and go through veins, tendons, knuckle
  bones, creases, nail colour, hair.
- The loop, in his words (2026-10-13): "do the work -> check in blender with reference -> iterate and loop this until you are
  happy with the result based on the rules. then you render the still, we check together and start iterating again if
  necessary." My checks run on quick low-sample renders of the part being fixed (the viewport does not show hair, skin
  colour or light as the render does); the proper still is rendered once, for him. "i thought the process was about you
  checking the stills as many times as necessary to get me the best result possible."
- "dont render any video, lets finish with the stills first." Nothing renders, preview or final, without his word.
- He often sends a picture of what he means; match it. Fix what he flags, smallest fix, show the fixed still.
  Only what he flags: "i only want you to fix the things i tell you". Other faults get one line, never a fix.
- Lock on his word ("ok lock him and lets continue") and move on.
- Measure, never guess: anything placed on the actor (teeth, tongue, throat, skull, props in his hands) is positioned from his
  own bones and mesh, with the numbers printed. Guessed offsets cost three loops each on the acid reflux x-ray.

## Every note Nick gives (agreed 2026-10-08: "ok go. this sounds good")
Why: on 2026-10-08 one note took an hour: the same 5-minute liquid test ran 10 times, one setting changed each round, and
the settings were in the builder's own new check. Nick: "blender changes usually take 5 minutes while you spend hours".
1. Method first. The note gets a row in the shot plan: what changes, the method, and how long one change takes to show.
   Over about a minute per change needs a reason; an effect that cannot go wrong by design beats one that must be policed
   (acid shaped from the stomach's inside, a ring attached to the tube). Simulation only for short moments where physics is
   the point (the splash), after a 10-s test.
2. The check comes first and from someone else: a separate checker agent writes it from Nick's words; it must fail on the
   frames he flagged and pass on a correct one; then it is locked (on the box: checks-submit/ -> checks/locked/, root-owned).
   The builder only runs it. A builder who thinks a check is wrong tells Nick; it never edits it.
3. At most 3 attempts per problem, each naming a different cause, never a new value of the same setting. Then stop: send
   Nick a still and what is blocking. bin/live enforces it (LIVE_ISSUE, refuses the 4th run until a still was sent).
4. Nick sees it live: "i just want real time monitoring while you work in blender". Every new still goes to him in this
   session as soon as it exists (SendUserFile), never through Telegram or another agent. One note at a time, in one
   Blender session; no helper agents opening Blenders of their own (8 Oct: 7 Blenders on one GPU crashed 3 renders).
   A note is done when its check passes and he has seen the still.
5. For now Nick directs from raw stills (2026-10-08, acid reflux and robbery, until he says otherwise): "for the first
   couple of clips, i want you to show me all the stills so i can direct the agent to do work faster instead of having to
   run multiple checks before showing me." Every still goes to him as soon as it exists, marked unchecked; checks still run
   but never hold a still back; his direction comes before the next attempt.

## Step 5. Preview: one sequence at a time
- A sequence is a stretch of the cut. tools/seq.sh NAME FIRST LAST renders only that stretch (Cycles, preview size) and joins
  it with its slice of the mix and the captions.
- "once i have the preview i can tell you exactly what we need to change." Act on his notes for that sequence only; "cant we
  just render the changed scenes first?" Never re-render the whole clip while he is present.
- Fast loop: ~/Desktop/render-desk/bin/live start BLEND JOBS_DIR opens the scene once on the cloud GPU; bin/live do JOBS_DIR
  job.py [dirs to pull] runs a change in that open session (build scripts via run_script(), stills via stills()). A change
  plus 10 stills: about 45 s (it was 12-15 min).
- The gate, before anything reaches him: the clip-reviewer agent on full-size frames every 0.25 s and on the moving clip,
  plus measured checks in the live session: visible(hero, frames) for the thing the story follows (the bite), overlaps(a, b)
  for hands, props and face. Contact sheets find frames; they never pass them. No known defect goes out (fix it or ask);
  "update now" gets a text status, never an unchecked file. He found 9 mistakes in an unchecked preview on 2026-10-07.
- The loop is mine, not his: "i think you need the checker to happen in real time and correct the blender run as it is
  happening until we perfect it ... i prefer you spend 3-4 hours checking, iterating analyzing, rather than neeeding my time".
  Every change runs the gate at once; fix and repeat alone until it passes; only then show him.
- Each sequence locks on his "i love this" or similar. Only after all are locked comes the final.
- Overnight or when he is away: batch work at preview level is fine, inside the budget he set; "if you have any questions the
  better thing to do is look at what zack did".

## Step 6. Sound and captions: at the preview stage
- Music loud and energetic, but "the music is too loud" is a fail: the voice sits clearly above it (stitches mix: about 12 dB).
- Sfx from the subject ("since we are talking about a beating heart, maybe we find respective sfx"), low, never fighting the song.
- Captions are Zack's: "take a look at his clip to see where he places them and how they look, also their zoom"; "max 2 words
  shown at the same time"; a subtle pop-in zoom "like the wisemind caption zoom". Hand-set the word groups on clauses.
- So the final is assembly only: the same joiner, mix and captions as the previews.

## Step 7. Final
- Before the desk: full-quality stills of the detailed shots (HQ=1 with tools/sheet.py: 100 percent, simplify off). Fix what
  shows only at full size (faceted granules, plastic membranes, a glow that flattens texture).
- Say what has not been previewed since it changed; he decides whether to preview it or judge it in the final.
- On his explicit go only: gpu/prepare_final.sh, then gpu/run_final.sh <jobs> (all desk jobs at once, one GPU each,
  stops at the cap). Previews and stills run on the cloud GPU: ~/Desktop/render-desk/bin/workbench up | push | run | pull | down
  (stops itself after 30 idle minutes; 1.4 to 3.6 s a 540 px still on the 4090 vs about a minute on the Mac). Budget: the cap he gives (stitches: $7, stop at $6). tools/spent.py reads the desk
  ledger (~/.local/share/render-desk/ledger.tsv); he asks "how much did we spend on rendering?".
- Chat does not touch a running render; heavy Blender work on the Mac and sleeping the Mac do.
- tools/assemble.py NAME writes review/NAME_captions.mp4 and _phone.mp4. Look at it frame by frame before sending. Send both.

## Step 8. Checkpoint
- /checkpoint after every locked sequence and before leaving (~/AgencyOS/handoffs/DATE-topic.md); lessons go to memory.
  "resume <clip>" starts from the handoff, never from re-explaining.
