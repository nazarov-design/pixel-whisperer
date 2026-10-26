**TL;DR** — round 1 of 3
1. Cut the palette to navy + one accent (red stays only for the primary action and the badges) · 2. One primary button per card, the other two become quiet · 3. Make HOT and -10% bigger, but keep only 2 badge types so they stand out
Reply: "Thanks! We'll cut the colors and clutter so the page feels calmer, and make HOT and -10% bigger. Because there will be fewer badges, each one will stand out more."

## Decode: real-estate-listings

| # | Client said | Likely meaning (confidence) | Change |
|---|---|---|---|
| 1 | "looks like a spam site" / "cleaner" | a) Too many competing colors and loud accents (55%) | Page uses navy, red, teal, mustard and the badge yellow. Cut to navy + red. Teal and mustard buttons go. Price red → navy `~#0B2545`. |
| | | b) Repeated, equal-weight elements per card (30%) | 3 buttons in 3 colors → DETAILS filled, CALL and SAVE as outline/text. Badges are limited to HOT and -10% (see #3). |
| | | c) Template feel: gray placeholders, emoji icons, no proof (15%) | Emoji (🛏🛁🚗) → line icons. Real photos. Add an agent or licence line. Check this with a question (Q1). |
| 2 | "looks like spam" (trust) | a) Red price + red HOT + red SEARCH read as an alarm or ad (50%) | Red only for SEARCH/primary and the discount badge. Prices go navy and larger (~20 → 22px, bold). |
| | | b) Crowded nav and no credibility signals (35%) | Nav has 8 items on one line, ~12px gaps. Cut to 5 (Buy, Rent, Sell, Agents, Contact) and move Call us into a phone button. Gap ~12 → 24px. |
| | | c) Missing proof (15%) | Add a licence line or a deals-closed number in the header. Needs client content (Q2). |
| 3 | "HOT and -10% bigger, they convert" | a) Bigger badge itself (70%) | HOT and -10% from ~36×16px / ~9px text to ~56×26px / 13px, 4px radius. |
| | | b) Wants them noticed more (30%) | Same fix. Remove NEW and EXCLUSIVE, or make them plain text labels, so only 2 loud badges remain. |

**Facts used:** header navy · 4 accent colors (red, teal, mustard, yellow) · red used for price, SEARCH and HOT · 3 button colors per card · badges ~36×16px with ~9px text, 4 types · nav 8 items ~13px · emoji icons · gray placeholder images · empty white space below the filters (~300px). All of these are estimates read off the screenshot.

### Keep as is
- A: Navy header and logo: it's the most trustworthy element. Don't touch it while doing #1.
- B: Search bar layout: clear and conventional. Keep its structure; just keep it the only red primary button.
- Card structure (image, price, title, meta): it's good. #1 and #2 only change color and weight.

### Conflicts
- **"Cleaner" vs "bigger badges":** bigger badges add noise if all 4 types grow. Resolution: enlarge only HOT and -10%, and drop or mute NEW and EXCLUSIVE. Showing them is the client's call, so offer it as a before/after.
- **"HOT" itself vs trust:** all-caps "HOT!" with an exclamation mark is a classic spam signal. Try "HOT" without the "!", or "Hot deal". It's a copy change, so check with the client.
- **Badges vs the brief:** inquiries and trust are both goals, so show the bigger badges in a calm palette (see #1) rather than adding more red.

### Ask the client (max 3)
1. Do you have real photos for the listings, or should we keep placeholders for now? (affects #1c)
2. Which proof can we show: licence number, years in business, or deals closed? (#2c)
3. May we drop the "!" from "HOT!" and remove NEW and EXCLUSIVE? Or do you want to keep all 4 badge types? (#3)

### Reply (client's language: English)
**Friendly:** Thanks for the clear feedback! To make the page feel more trustworthy we'll reduce the number of colors, give each listing one clear main button, and tidy the menu. We'll also make the HOT and -10% badges larger. With fewer badge types competing for attention, they'll stand out more. Could you send photos and any proof points (licence, years in business) so we can show them?

**Firm:** We'll take the "spam" feeling as the priority for this round: fewer colors, one main action per card, a calmer menu. HOT and -10% will be larger, and to keep them effective we'd like to limit badges to those two types. Please let us know if you'd rather keep all four.

### Scope
Round 1 of 3 · 2 items, both in scope (no new requests). Ledger created: `./.feedback-decoder/real-estate-listings.md`

Overlay: `./benchmark/runs/v1.0-feedback/f06/with/.feedback-decoder/work/overlay.png`. Markers 1–5 are the changes and A–B are keep-as-is. Marker 5 (NEW badge) sits close to marker 2 on the right card, so check both when you edit.
