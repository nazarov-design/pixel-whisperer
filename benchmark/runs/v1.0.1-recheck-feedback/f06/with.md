**TL;DR**: round 1 of 3
1. Keep HOT and -10% and make them bigger, but give each card one badge only, so the page stops looking like it's shouting.
2. Cut the colour noise: red only for badges and Search, three card buttons become one main button plus two quiet ones, and the price goes navy.
3. Trim the nav and the minor badges (NEW, EXCLUSIVE).

Reply: "Thanks, this is clear. We'll make HOT and -10% bigger and give them more room, and calm down everything around them so the page feels more trustworthy."

## Decode: real-estate-listings

| # | Client said | Likely meaning (confidence) | Change |
|---|---|---|---|
| 1 | "looks like a spam site" | a) Too many loud signals at once (55%): 4 badge types, red price, red badges, red Search, 3 differently coloured buttons per card | One badge per card. Red only for badges and Search. Price red → navy (#0B2545-ish, same as the header). |
| | | b) Weak trust cues (30%): grey placeholder images, emoji icons, "HOT!" with an exclamation mark | "HOT!" → "HOT". Real photos if available. Emoji → simple line icons. |
| | | c) Dense nav and tiny text (15%) | Nav 8 items → 5, with "Call us" as the one highlighted item. |
| 2 | "make it cleaner" | a) Too many colours and boxes (50%): navy, teal, yellow and red buttons and badges together | DETAILS = solid navy. CALL and SAVE → outline or text style. Drop teal and yellow from the buttons. |
| | | b) Uneven rhythm (30%): badge edges don't line up (EXCLUSIVE ends ~8px short of NEW), card text sits ~12px from the card edge | Align all badges to a 12px inset. Use one spacing scale (8/16/24). |
| | | c) Dead space (20%): the filters panel is empty below Gym, and ~300px of grey sits below the cards | Make the sidebar sticky or shorten it. Add pagination or a footer. |
| 3 | "HOT and -10% badges bigger" | a) Wants more visibility for the offers (75%) | Badge ~11px → 14px text, height ~17 → 28px. Both in one style, top-left. |
| | | b) Wants them kept at all costs (25%) | Same as a). |

**Facts used:** badges ~11px text, ~17px tall, 4 types (HOT!, NEW, -10%, EXCLUSIVE) in red and yellow · price red ~18px · 3 card buttons in navy, teal and yellow · nav ~13px, 8 items · placeholder grey images · empty area below the cards.

### Keep as is
- A: card structure (image, price, title, specs, actions). The hierarchy is already readable, so don't restructure it for #2.
- B: the search bar. It's clear and well placed, so the only change there is a calmer Search colour (still red, as it's one of the two places red stays).

### Conflicts
- **#1 vs #3**: bigger badges make the page louder, but the goal is quieter and more trustworthy. Suggested resolution: bigger but fewer. Each card shows one badge (HOT or -10%), in one shape and one red, with NEW and EXCLUSIVE moved to small text next to the title. Offer a quick A/B: A = this plan, B = the current four badges, only bigger.
- Badge size ~28px high is a reasonable ceiling. Beyond that they cover the photo and look like ads.
- The claim that badges "convert" is the sales team's belief, not data. If you can, ask whether there's any A/B evidence. Don't argue it with them.

### Ask the client (max 3)
1. Can a card show only one badge (the strongest), or is a HOT and -10% combination essential? See markers 1 and 2.
2. Do you have real property photos, or are these placeholders until launch?
3. Which nav items matter most to the sales team? Markers 5.

### Reply (English)
**Friendly:** Thanks, this is really helpful. We'll make the HOT and -10% badges bigger and easier to spot, and at the same time tidy the page so it feels more trustworthy: fewer colours on each card, one clear main button, and a lighter menu. One quick question: can each listing show a single badge, or do you need HOT and -10% together on some? And are the photos final, or placeholders for now? Round 2 will have all of this.

**Firm:** We'll make HOT and -10% bigger. To keep the page from looking like spam, we also need to reduce the other loud elements (extra badges, red prices, three coloured buttons). Bigger badges on a busier page would make the "spam" impression stronger, not weaker. We'll show this in round 2. Please tell us whether each listing can carry one badge and whether the photos are final.

### Scope
Round 1 of 3 · 2 items, both in scope, 0 new requests.

Overlay: `.feedback-decoder/work/overlay.png`
Ledger: `.feedback-decoder/real-estate-listings.md`
