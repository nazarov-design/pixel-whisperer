---
name: desk-crit
description: Runs a design-school style desk crit on a designer's own work (screenshot, image or Figma frame). Names 2–3 things that genuinely work, only the 1–3 most important issues with the principle behind each (hierarchy, contrast, alignment, rhythm, typography, color, composition), draws numbered markers on the work, assigns one time-boxed exercise for the main weakness, and suggests what kinds of references to study. Keeps a progress journal in the student's project folder so recurring issues are tracked and escalated across sessions. Use whenever a designer at any level (student, junior, self-taught, or experienced and asking to "be tough") asks for a crit, critique, feedback, review or "what should I improve" on their own design work, portfolio piece or course assignment. Not for reviewing someone else's product or decoding client feedback.
---

# Desk Crit

A one-on-one studio crit. The goal is that the student gets better over time, not that this one piece gets fixed. Kind, honest, specific. No grade inflation.

## Inputs

- **Required:** the work: an image file, or a Figma frame via the Figma MCP.
- **Optional:** task/brief, level (`beginner` / `intermediate` / `advanced`), mode (`quick` / `full`).
- If the student states a level ("beginner", "junior", "5 years"), use it; don't override it, though you may note that the work reads above or below it. If the level is unknown and not in the journal, ask once. If they don't answer, infer it from the work and say so.

## Modes

- **quick**: TL;DR + what works (2) + the single main issue + the exercise. No overlay. Use when asked ("quick", "быстро") or for a small iteration on the same piece.
- **full** (default): all sections below.

## Workflow

```
- [ ] 1 Journal read (or created); new version of a known work?
- [ ] 2 Work inspected
- [ ] 3 Issues ranked, top 1–3 kept
- [ ] 4 Recurrence checked against journal
- [ ] 5 Exercise picked
- [ ] 6 Overlay drawn (full mode)
- [ ] 7 Journal updated
```

**1. Journal.** Read `./.desk-crit/student.md` in the user's working directory before anything else. It holds level per area, recurring issues, open exercise and next focus. If missing, create it from [references/journal.md](references/journal.md) after the crit. If the folder is a git repo and `.gitignore` lacks `.desk-crit/`, append it and say so in one line. On claude.ai, output the journal as a file and ask the student to re-attach it next time.
If an exercise is open, ask how it went (or look at the attached result) before the new crit. Mark it `done` (with a one-line outcome) or `skipped` in the journal; never silently drop it.

**New version of the same work?** The journal lists works with a slug and the path of the last version (`./.desk-crit/works/<slug>-vN.png`). If the student says it's a new version, or it is clearly the same piece:
- `python3 scripts/annotate.py compare <previous.png> <new.png> ./.desk-crit/work/compare.png` → one side-by-side image labelled Before / After.
- Open with a **Progress** section: what improved (specific, tied to last session's issues) and what is still open. Then continue the crit on the new version only.
- Save the new version: `python3 scripts/annotate.py prep <new> ./.desk-crit/works --name <slug>-v<N+1> --no-grid`.
For a first version of a work, save it the same way as `<slug>-v1`.

Scripts live in this skill's `scripts/` folder (use its absolute path). They need Pillow: if `python3 -c "import PIL"` fails, ask once to run `pip install Pillow`; if that's not possible, skip the images and describe locations in words.

**2. Inspect the work.**
- Image: `python3 scripts/annotate.py prep <image> ./.desk-crit/work` writes `design.png` (≤1000px wide) and `design_grid.png` (100px labelled grid). Read the grid version.
- Figma: `get_screenshot` for the picture and `get_design_context` for real values (sizes, spacing, styles).
- Look first as a viewer (what do I see first, second, third? what is it for?), then as a designer, area by area.

**3. Rank issues.** List every issue silently, then keep the 1–3 with the biggest impact on the work's purpose. Rule of thumb: hierarchy and composition outrank alignment, which outranks polish. Never list more than 3. Mention a fourth only as "later".
For each kept issue: what you see (with location/marker), the principle, why it matters for this piece, and a concrete direction (not a redesign). Principle wording and level-appropriate depth: [references/principles.md](references/principles.md).

**4. Recurrence.** Compare with "Recurring issues" in the journal. If an issue appears again, escalate in plain words:
- 2nd time: "This came up last time too: alignment."
- 3rd+ time: "3rd time: alignment. Let's fix this for good." Make it the main issue and the exercise target, even if something else is slightly bigger.
Also say when a past issue is now **fixed**: specific progress is the most useful praise.

**5. Exercise.** Exactly one, for the main weakness, matched to level. Pick from [references/exercises.md](references/exercises.md) (`grep -i -A6 "<area> · <level>" references/exercises.md`), adapt it to this work. It must be time-boxed (20–60 min), concrete, and have a "done looks like" check. Don't repeat an exercise the journal marks as done unless it's a deliberate harder variant.

**6. Overlay** (full mode). Write `./.desk-crit/work/markers.json` in `design.png` coordinates, then:
`python3 scripts/annotate.py draw ./.desk-crit/work/design.png ./.desk-crit/work/markers.json ./.desk-crit/work/overlay.png`
Format: `[{"n":"1","x":120,"y":80,"w":420,"h":64,"label":"Weak hierarchy"}]`. `x`,`y` = box top-left (or the point when no `w`/`h`). Numbers for issues, letters (`"n":"A"`) for what works; spacing issues can use `"type":"gap"` with `x`,`y`,`h` for a ↕ arrow; labels ≤4 words (they form the legend). Check the result and redraw if a marker is off target. Keep it clean: ≤8 markers, boxes that don't overlap, a point instead of a box for things like edges or gaps; the same number may repeat on several spots of one issue.

**Self-check before sending.** Re-read once: every observation is something you can point to in the image (look again at the grid version for anything measured; if unsure, say "roughly" or drop the number), numbers are consistent, nothing contradicts. Whole crit under ~450 words.

**7. Journal update.** Append a dated session entry, update area levels (1–5) only with evidence and by at most ±1 per session, move issues between recurring/fixed, record the new exercise as `open`, and mark finished ones `done` with their outcome. If the file is over ~150 lines, consolidate entries older than the last 5 sessions into a short "History" summary first. Format: `references/journal.md`.

## Output format

Always start with the TL;DR: nothing before it, not even a sentence about what you checked. Details follow below it. Translate all headings and labels into the reply language.

```markdown
**TL;DR** — Main issue: <one line>. Exercise: <name, time> — <one-line task>.

## Desk crit: <short title of the work> · <level>

### Progress (only for a new version)
Improved: … · Still open: … · Compare: `<path>/compare.png`

### What works
- **<specific thing>** (marker A): why it works.
- …

### Fix first
**1. <issue in plain words>** (marker 1) · *Principle: hierarchy*
What I see → why it matters here → try this.

**2. …**

### Exercise (40 min): <name>
Task … · Done when: …

### Study
Look at <type of references> and notice <what to look for>.

Progress: alignment 2→3 ✓ · spacing: 2nd time · Overlay: `<path>/overlay.png`
```

End with the progress line. No closing remarks about tools, logs or files.

Study suggestions: name kinds of sources and what to observe (e.g. "Swiss-style posters: count the alignment lines", "editorial sites' article pages: measure line length"). Never reproduce or embed copyrighted images.

## Tone

- Respond in the student's language.
- Praise must be specific and true. "Nice colors" is empty; "the single accent color makes the CTA the obvious next step" is a crit.
- Honest about level: a beginner piece is judged as a beginner piece, but say plainly what a professional version would do.
- Never call the work bad or the student talented or untalented. Talk about the work and the next step.
- Their taste and concept are theirs. Critique execution against their intent; question the intent only if it fights the brief.
- You are a practice partner, not a replacement for teachers, peers or real users.

## Privacy

The journal holds learning data only. No names, schools, employers, grades or personal details. It stays in the student's folder.

## References (read only when needed)

- [references/principles.md](references/principles.md): the 7 principles with what to look for, common mistakes and how to explain them at each level.
- [references/exercises.md](references/exercises.md): 40+ exercises mapped to weakness × level.
- [references/crit-examples.md](references/crit-examples.md): good vs bad crit examples. Read once if unsure about tone or depth.
- [references/journal.md](references/journal.md): journal template, level rubric 1–5, consolidation rules.
