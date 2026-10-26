**TL;DR** — round 1 of 2
1. Modernise the type and details, keeping the palette · 2. Menu text → 16px with contrast of at least 4.5:1, single column on mobile · 3. Logo modestly bigger (A/B) · 4. Online ordering is a new request, so quote it separately.
Reply: "Thanks! We'll keep the colours and cozy feel, freshen the look, and make the menu much easier to read on phones. Online ordering is a great idea, but it's outside our current brief, so I'll send a separate estimate."

## Decode: coffee-site

| # | Client said | Likely meaning (confidence) | Change |
|---|---|---|---|
| 1.1 | "a bit old-fashioned… more modern but still cozy" | a) Dated type and details (55%): Georgia-style serif everywhere, double-rule dividers, white photo-frame border, centred stacked header | Keep the serif for H1 and logo only. Use a clean sans for nav, body, menu and buttons. Remove the double rules and the white image frame. Switch the ghost CTA to a solid fill: #594531 with cream text is ~7.5:1 (the outline button is ~3.4:1). Round the image corners to ~12px. |
| | | b) Flat and sparse, with a placeholder-looking hero (30%): the image is a generic circle graphic | Replace it with a real photo. Ask for photos; see Q1. |
| | | c) Header feels heavy and traditional (15%) | Left-align the logo with the nav on the same row. Cut the header from ~160px to ~90px tall. |
| 1.2 | "The menu is hard to read on my phone" | a) Low contrast (50%): items are #A08F7E on #EADBC8 = ~2.3:1, and prices are the same | Item text → #594531 (~7:1 on the panel). Prices bold. Both pass 4.5:1. |
| | | b) Too small (35%): items are ~12px | Items ~12 → 16px, row height ~23 → 40px (tap-friendly), line-height 1.5 |
| | | c) Three columns squashed on a phone (15%) | Mobile: one column, category headers sticky, panel padding ~16px. Not verified: I only have the desktop frame. |
| 1.3 | "add online ordering" | New request (90%) | Not in the brief. Don't build it. Offer a stopgap inside this round: an "Order ahead" button linking to an existing tool, if the client has one. |
| 1.4 | "logo should be bigger" | a) The partner wants more brand presence (60%): the logo is ~32px type, about the same visual weight as the H1 | Logo ~32 → ~44px. Keep it left-aligned in the new header so it gains presence without a taller header. |
| | | b) Client pride only (40%) | Offer A/B: A = ~40px, B = ~48px, so they can choose. Remind them the headline sells and the logo signs. |

**Facts used:** Logo ~32px serif, #5A4632 (7.4:1) · H1 ~34px (7.5:1) · hero body ~16px, #8C7B6B on #F3E9DC (3.4:1) · tagline and about text, same 3.4:1 · menu items ~12px, 2.3:1 · CTA outline, 3.4:1 · only the desktop frame is seen (mobile not seen).

Contrast numbers are estimated from sampled pixels.

### Keep as is
- A: the cream and brown palette, which the client loves. Every change above reuses it, so don't introduce new hues.
- Warm, personal copy ("keep the corner armchairs free").
- The three-category menu structure on desktop.

### Conflicts
- **#1.1 vs #1.2.** "More modern" could lead to lighter, thinner text, which would worsen the menu readability. Resolve it by making modern come from the sans type, whitespace and solid buttons, never from paler text.
- **#1.4 vs #1.1.** A bigger logo and a lighter, airier header pull in opposite directions. Left-aligning the logo with the nav solves both.
- **Body text outside the menu.** Hero, about and tagline text sit at 3.4:1, below 4.5:1. I'd darken them to ~#6B5846 in the same pass.

### Ask the client (max 3)
1. Do you have real photos (shopfront, coffee, pastries) we can use in place of the illustration?
2. Logo: A (a bit bigger) or B (clearly bigger)? I can show both.
3. For ordering: is there a tool you already use (e.g. a delivery app) that we could link to for now?

### Reply
**Friendly:** Thanks for the great feedback! We'll keep the colours you love and make the site feel fresher with cleaner text and simpler details, while keeping it cozy. The menu will get larger, darker text and a single-column layout on phones. I'll show two logo sizes so you and your partner can pick. Online ordering is a lovely idea, but it goes beyond our current brief (homepage and menu), so I'll send a separate estimate once this round is done. Do you have real photos of the shop we can use? I'll send the updated designs by [date].

**Firm:** Thanks for the feedback. In this round I'll modernise the look while keeping your colours, make the menu readable on phones, and show two logo sizes. Online ordering is a new piece of work outside the current brief, so I'll quote it separately rather than add it here. Please send any photos you'd like used.

### Scope
Round 1 of 2 · #1.1, #1.2 and #1.4 are in scope · #1.3 online ordering is a new request (scope message included in the replies above) · 1 round left after this one, so ask them to gather all remaining comments for round 2.

Overlay: `./.feedback-decoder/work/overlay.png`
Ledger: `.feedback-decoder/coffee-site.md`

The folder isn't a git repo, so there's no `.gitignore` to update.
