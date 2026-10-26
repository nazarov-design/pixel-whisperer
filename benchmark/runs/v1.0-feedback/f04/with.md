**TL;DR** — round 1 of 3
1. Calm the hero: replace the gradient with a quiet neutral or a photo, and fix the white text. · 2. Cut to one accent colour and one card style, and replace the empty placeholders with real photos. · 3. Add a Teachers section, and keep the schedule table untouched.
Reply: "Thank you, that's a clear direction. We'll quiet the first screen, refine the details so it feels more premium, and add a Teachers section. The schedule stays as it is."

## Decode: homepage-yoga-studio

| # | Client said | Likely meaning (confidence) | Change |
|---|---|---|---|
| 1 | "a bit cheap" | a) Default-looking details (50%): a bright diagonal gradient (1), a text shadow on the H1, grey placeholder boxes (3), and green, orange and outlined boxes all mixed (5) | Gradient → flat warm off-white (~#F6F3EE). Remove the H1 text shadow. One accent only. Pricing: one card style, no orange outlines |
|   | | b) No real imagery (35%): cards 3 are empty, so the page reads as a template | Real photos in the class cards (same crop and treatment). Hero: one full-bleed photo with a soft overlay |
|   | | c) Generic type (15%): bold system sans, ~56px H1 | H1 → light-weight serif or a refined sans, ~56px at weight 300–400, tracked slightly open |
| 2 | "too busy" | a) Too many competing colours and shapes (55%): green nav, gradient, orange CTA, green card titles, orange pricing | Palette → 1 neutral family + 1 muted accent (a deeper sage). CTA and prices use the same accent |
|   | | b) Too much on one screen (30%): 4 cards, a 7-column table and 3 price boxes stacked tightly (~50–60px between sections) | Section padding ~60 → ~120px. Hero height stays ~420 |
|   | | c) Cramped hero text (15%): the tagline touches the H1 and CTA | Fix the vertical rhythm: H1 → tagline 24px, tagline → CTA 40px |
| 3 | "feel calm the moment they land" | a) Hero first impression (60%): a loud gradient, white text on pale yellow-green (2), and a saturated orange CTA (4) | Hero text → dark (~#2B2B2B) on the neutral, or white on a darkened photo (≥4.5:1). CTA → muted accent with ≥4.5:1 |
|   | | b) Nothing quiet to rest on (40%) | One large calm image and less text. A single CTA, which you already have |
| 4 | "show the teachers somewhere" | a) A homepage section (75%): "Teachers" is already in the nav (6) but the page has no section | New section between the classes and the schedule: 3–4 portraits, name, one-line specialty, no bios |
|   | | b) A separate page (25%) | Keep the nav link, add "Meet all teachers" below the section |
| 5 | "Love the schedule table" | Keep it (90%) | Don't restructure it. Only restyle it to the new palette: header → the single accent (muted), keep the grid |

**Facts used:** the page is ~1000px wide. H1 ~46px bold with a shadow, white on a gradient from ~#A8D5BA to ~#F5E3A0. Nav and table header ~#80B880. CTA ~#F4A261 with white text (~2:1, estimated, below 4.5:1). Class cards have grey empty image boxes. Pricing uses orange outlines. There are no photos anywhere. Section gaps are ~50–60px.

### Keep as is
- A: Schedule table. The client loves it, so only recolour it. Don't change its structure or the information it shows (#1, #2 touch its colour only).
- Short, calm copy ("Find your balance", the class descriptions). Don't add text in the new Teachers section, which should be mostly photos.
- Four classes and three prices. The content is fine, and the styling is what needs work.

### Conflicts
- #2 "less busy" vs #4 "add teachers": more content on a page that should feel calmer. Resolve it by adding the section while removing elsewhere (the colour variety, the card boxes, the pricing outlines). Keep it to 3–4 teachers, with no bios.
- "Love the table" vs "too busy": the table is the densest block. Keep its content, but give it space (padding above and below, lighter grid lines) so it reads calmer without changing.
- Accessibility: the hero text and the CTA are both under 4.5:1 right now, so the calming changes also fix this.

### Ask the client (max 3)
1. Do you have photos of the studio and the teachers, or should we use placeholders for now? Photography is the biggest lever for "premium", and there's no way around it.
2. Which of two directions: A (warm neutrals, sand and sage) or B (cool, deep green and white)? I'd offer two quick colour variants in round 2 instead of asking in the abstract.
3. Should the Teachers section show 3–4 names on the homepage, or all teachers?

### Reply (English)
**Friendly:** Thank you, this is really helpful. We'll make the first screen much quieter, with fewer colours and more space, and polish the details so the whole page feels more premium. We'll add a Teachers section too. The schedule table stays as it is, with just a softer look. To do the teachers justice, could you send photos of them (and of the studio, if you have them)? Real photos will do more for "calm and premium" than anything else. We'll also bring two colour options in the next round.
**Firm:** Based on your feedback, round 1 will cover three things: a calmer first screen, a more refined look (one accent colour, real photography, more space), and a new Teachers section. The schedule table stays. To proceed with the teachers section we need photos and names from you. Colour and photo choices can be refined in rounds 2 and 3.

### Scope
Round 1 of 3 · 3 items, all in scope · the Teachers section is a homepage section, not a new page (it's already in the nav), but it depends on content from the client. Ledger: `.feedback-decoder/homepage-yoga-studio.md`.

Overlay: `./benchmark/runs/v1.0-feedback/f04/with/.feedback-decoder/work/overlay.png`

Notes:
- The hero text is hard to see in the overlay because it sits on the gradient, which is the problem in #2.
- The folder isn't a git repo, so I didn't touch a `.gitignore`.
- The bottom of the design may continue past the 1000px-wide screenshot, so I couldn't check the footer.
