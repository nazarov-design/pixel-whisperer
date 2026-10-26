---
name: feedback-decoder
description: Decodes vague or contradictory client feedback on a design ("make it pop", "feels boring", "more air but bigger") into ranked interpretations with concrete, measurable design changes grounded in what is visible in the design. Flags contradictions and out-of-scope requests, asks at most 3 closed clarifying questions, drafts a reply to the client in the client's language, tracks revision rounds in a local ledger, and can draw numbered markers on the screenshot. Use when a designer shares client comments, revision requests or stakeholder feedback together with a screenshot, mockup or Figma frame, or asks what a client means, how to answer them, or whether a request is out of scope. Works in any language.
---

# Feedback Decoder

Turn client words into a revision plan the designer can act on. You advise the designer; the designer decides and talks to the client. Never present a guess as certainty.

## Inputs

- **Required:** client message(s), verbatim, any language.
- **Strongly recommended:** the design: an image file, or a Figma frame via the Figma MCP.
- **Optional:** brief, agreed number of revision rounds, project slug, mode (`quick` / `full`).

No design? Decode anyway, mark every change `unverified: design not seen`, and ask for a screenshot. Do not block.

## Modes

- **quick**: TL;DR + decode table + one reply draft. No overlay, no references beyond a phrasebook grep. Use when the user says "quick"/"коротко", or the feedback holds ≤2 vague phrases.
- **full** (default otherwise): all six output sections.

## Workflow

Copy this checklist and tick it off:

```
- [ ] 1 Ledger loaded (or created)
- [ ] 2 Design inspected, facts listed
- [ ] 3 Feedback split into atomic items
- [ ] 4 Each item decoded
- [ ] 5 Contradictions checked, keep-as-is list made
- [ ] 6 ≤3 questions, reply drafts
- [ ] 7 Ledger updated
- [ ] 8 Overlay drawn (full mode, image available)
- [ ] 9 Self-check: consistent numbers, no contradictions, length
```

**1. Ledger.** Look for `./.feedback-decoder/<project>.md` in the user's working directory. The project slug describes the work (`fintech-landing`), never a person or company name. If none exists, ask once for the agreed rounds and create it from [references/ledger.md](references/ledger.md). If the folder is a git repo and `.gitignore` lacks `.feedback-decoder/`, append it and say so in one line. On claude.ai (no persistent folder), output the ledger as a file and ask the user to re-attach it next time.

Scripts live in this skill's `scripts/` folder (use its absolute path). They need Pillow: if `python3 -c "import PIL"` fails, ask once to run `pip install Pillow`; if that's not possible, skip the images and describe locations in words.

**2. Inspect the design.** Ground every change in what is actually there.
- Image: `python3 scripts/annotate.py prep <image> ./.feedback-decoder/work` writes `design.png` (≤1000px wide) and `design_grid.png` (100px labelled grid). Read the grid version to estimate positions and sizes.
- Figma frame: use the Figma MCP `get_screenshot` for the picture and `get_design_context` / `get_variable_defs` for real values (font sizes, spacing, colors). Measured values beat estimates.
- Write a short **facts list**: H1 size, body size, CTA color + contrast, section padding, palette, type families, density, imagery. Prefix estimates with `~`.

**3. Split the feedback** into atomic items. Quote each verbatim in the original language. A sentence like "more air but bigger" is two items.

**4. Decode each item.** Run `grep -i -A8 "<key word>" references/phrasebook.md` to see the usual meanings, then judge against the facts list:
- 2–3 interpretations, ranked, with confidence (%, summing to ~100).
- For each: one concrete change with element + from → to values, e.g. "Hero H1 ~40 → 56px", "CTA #9AA4B2 on white (2.4:1) → #1F5BFF (5.1:1)", "section padding 120 → 80px".
- Prefer the smallest change that would test the interpretation.
- Only reference elements that exist. If the top confidence is <50%, say the item needs a question, not a guess.

**5. Contradictions.** Flag conflicts: item vs item ("more air" vs "bigger everything" on a fixed viewport), item vs brief, item vs accessibility (contrast <4.5:1, body <16px on web). Propose one way to resolve each, usually "prioritise X, show Y as variant".

**Keep as is.** List 2–5 things the client praised or did not mention that are working (with marker letters A, B…). Every proposed change must leave these intact; if a change would break one, say so in that row.

**6. Questions and reply.**
- Max 3 questions to the client, closed or visual: "A (bolder type) or B (brighter color)? See markers 1 and 2." Offering two quick variants is often better than a question.
- Reply drafts in the client's language: **friendly** and **firm**. Structure and phrasing in [references/replies.md](references/replies.md). Warm, specific, no jargon, no apologising for good work, no promises about timing or money.

**7. Scope guard.** Compare each item with the brief and the ledger. Mark items `in scope`, `new request`, or `unclear`. If rounds used ≥ agreed, or a new request is significant, add the polite scope-change message from `replies.md`. Update the ledger (append-only round entry).

**8. Overlay** (full mode, image available). Write `./.feedback-decoder/work/markers.json` in `design.png` pixel coordinates and run:
`python3 scripts/annotate.py draw ./.feedback-decoder/work/design.png ./.feedback-decoder/work/markers.json ./.feedback-decoder/work/overlay.png`
Format: `[{"n":"1","x":120,"y":80,"w":420,"h":64,"label":"Bolder H1"}]`. `w`/`h` optional (box around the element); `x`,`y` = box top-left, or the point to mark when no box. Use numbers for changes and letters (`"n":"A"`) for keep-as-is items. Out-of-scope requests: add `"kind":"scope"` (amber, legend says "out of scope"). Spacing changes: `{"n":"4","type":"gap","x":500,"y":510,"h":220}` draws a ↕ dimension arrow instead of a box. Markers are placed outside boxes automatically. Labels ≤4 words; they form the legend strip. Open the result and check every marker sits on its element; fix and redraw if not. Keep it clean: ≤8 markers, boxes that don't overlap, a point instead of a box for things like edges or gaps; the same number may repeat on several spots of one issue. Marker numbers match decode-table rows.

**9. Self-check before sending.** Re-read your draft once:
- Every value is stated once and consistently (facts list = table = reply); no "~46px" in one place and "~56px" in another.
- Each claim about the design is something you actually see; if a measurement is shaky, say "roughly" or drop the number.
- Recommendations don't contradict each other (e.g. where a color stays vs goes).
- Length: under ~500 words plus the reply drafts. Cut repetition, not substance.

## Output format

Keep it scannable. No preamble.

Always start with the TL;DR: nothing before it, not even a sentence about what you checked. Details follow below it. Translate all headings and labels into the reply language.

```markdown
**TL;DR** — round N of M
1. <change> · 2. <change> · 3. <change>
Reply: "<one-line suggested reply in the client's language>"

## Decode — <project>

| # | Client said | Likely meaning (confidence) | Change |
|---|---|---|---|
| 1 | "make it pop" | a) weak focal point (55%) | CTA → #1F5BFF, 5.1:1; H1 40→56px |
|   |               | b) palette too muted (30%) | Accent saturation +20%, keep neutrals |
|   |               | c) lacks imagery (15%) | Ask: see Q1 |

**Facts used:** H1 ~40px · CTA #9AA4B2 (2.4:1) · section padding ~120px

### Keep as is
- A: <what works> — don't touch while doing #1

### Conflicts
- #2 vs #3: … → suggest …

### Ask the client (max 3)
1. A or B? …

### Reply (client's language)
**Friendly:** …
**Firm:** …

### Scope
Round 2 of 3 · 1 new request (#4: blog page, not in brief) → scope message included

Overlay: `<path>/overlay.png`
```

End with the overlay/ledger lines. No closing remarks about tools, logs or files you created along the way.

Quick mode: TL;DR, table, friendly reply only.

## Rules

- Respond to the designer in the designer's language; reply drafts in the client's language.
- Numbers must come from the facts list or be marked `~`. No invented pixel values without a basis.
- Be honest about uncertainty; never claim to know what the client "really" wants.
- Do not mock the client or the designer. Vague feedback is normal.
- Privacy: no names, emails, phone numbers or money amounts in the ledger or any file; write "the client". Keep files in the user's project folder only.
- Images go into context at ≤1000px wide; use `prep` instead of reading full-size files.

## References (read only when needed)

- [references/phrasebook.md](references/phrasebook.md): 60+ vague phrases → usual meanings → fixes, by category. Grep it; don't read it whole.
- [references/replies.md](references/replies.md): reply structure, tone variants, scope-change and round-limit messages.
- [references/ledger.md](references/ledger.md): ledger template and update rules.
