**TL;DR** — round 2 of 3
1. Make the hero the one focal point: H1 ~44 → 60px, CTA to a saturated accent, and swap the grey wireframe for a real, larger product screenshot. · 2. Add air only between sections and around the hero, and keep the feature cards untouched. · 3. The pricing page is a new request outside the brief, so quote it separately.
Reply: "Thanks! We'll make the headline and product screenshot bigger, add a stronger accent and more space between sections, and keep the feature cards as they are. A pricing page is a separate piece of work, so I'll send a short estimate for it."

## Decode — flowdesk-landing

| # | Client said | Likely meaning (confidence) | Change |
|---|---|---|---|
| 1 | "boring, doesn't pop" | a) no focal point, palette all grey-slate, CTA is a pale grey button (55%) | H1 ~44 → ~60px, weight up one step. CTA grey (~2.5:1) → one saturated accent (≥4.5:1), used on CTA and a few highlights only. |
|   |  | b) flat, placeholder imagery (30%) | Replace the grey wireframe with a real product UI shot. |
|   |  | c) uniform section rhythm (15%) | Give the testimonial band an accent or dark background (unverified, needs Q1). |
| 2 | "more modern" | a) heavy gray type, low contrast, little scale contrast (45%) | Body text slate → darker, H1:body ratio ~2.6 → ~3.5:1. Keep the Inter-style sans. |
|   |  | b) wants a current look: gradient, bento, large type (35%) | Add one trendy element (e.g. subtle accent gradient behind the screenshot) on the existing base. |
|   |  | c) unclear (20%) | Ask Q1. |
| 3 | "more air" | a) more space between and around blocks (60%) | Section padding ~100 → ~140px. Hero ends ~600 and cards sit on a tight ~120px gap. Raise gaps around the cards. Keep the card internals. |
|   |  | b) less content competing (40%) | Give the subhead a max width of ~480px and drop it to 2 lines. |
| 4 | "headline bigger" | a) larger H1, ~3 lines, still left-aligned (80%) | ~44 → ~60px. Wider text column (~520px). |
| 5 | "screenshot bigger" | a) hero visual larger, full-bleed to the right edge (65%) | ~400×280 → ~560×400px, allowed to bleed past the container. Fill it with real UI, not grey placeholder bars. |
|   |  | b) show more detail (35%) | Add an overlapping second panel (e.g. a reply card). |
| 6 | "pricing page too" | new request, not in the brief (one landing page) | Out of scope. See Scope. (Nav already has a "Pricing" link, so decide where it points meanwhile.) |

**Facts used:** H1 ~44px, ~3 lines · subhead ~17px · CTA grey fill, white text, ~2.5:1 · screenshot ~400×280, empty grey placeholder · hero-to-features gap ~120px · palette all slate/grey, no accent · cards ~270×195 · testimonial ~22px, small attribution

### Keep as is
- A: Feature cards (client loves them). Don't change their layout or copy. Only add space around them (#3).
- B: Testimonial copy and the clean layout. Restyle the band only if Q1 says so.

### Conflicts
- #3 "more air" vs #4/#5 "bigger headline and screenshot": the hero has to fit one first screen. Suggest: grow H1 and screenshot, and put the air between sections, not inside the hero. Show it at 1440×900 to check the CTA stays above the fold.
- #1 "pop" vs #3 "air": a bold accent and a lot of whitespace can coexist if the accent is used sparingly. Avoid adding more decoration to get "modern".
- Mobile: "bigger screenshot" will stack under the H1, so the CTA would fall below the fold. Suggest H1 ~36px and a cropped screenshot on mobile.

### Ask the client (max 3)
1. "Modern" like A (bolder color and big type) or B (more depth: gradients, overlapping panels)? I can mock both for the hero.
2. Do you have a real product screenshot to use in the hero, or should I design a clean UI mock?
3. For the pricing page: a separate quote, or a pricing section on the landing page instead?

### Reply
**Friendly:** Thanks, and great to hear you like the feature cards! For this round we'll make the headline and product screenshot bigger, add a stronger accent color so the first screen stands out, and add more space between sections. The feature cards stay as they are. Two quick questions: should "modern" lean more towards bold color (A) or depth, like overlapping panels (B)? And do you have a real product screenshot we can use? The pricing page is a great idea. It goes beyond the current brief (one landing page), so I'll send a short separate estimate once this round is done. Does that work?

**Firm:** Thanks for the feedback. This round I'll enlarge the headline and screenshot, strengthen the accent color and add space between sections, keeping the feature cards. To keep the first screen balanced, the extra space goes between sections, not in the hero. A pricing page is a new piece of work outside our brief, so I'll quote it separately and focus this round on the changes above.

### Scope
Round 2 of 3 · 5 items in scope (#1–5), 1 new request (#6, pricing page) → scope message included in both drafts. Round 3 will be the last included one, so ask the client to gather all remaining comments into it.

Ledger: `.feedback-decoder/flowdesk-landing.md` (round 1 wasn't recorded, so I started at round 2; correct it if needed). The folder isn't a git repo, so no `.gitignore` change.
Overlay: `.feedback-decoder/work/overlay.png`. I redrew it after moving marker 4, but I haven't re-checked that image.
