Markers sit on their elements.

**TL;DR** — round 1 of 3
1. Grey text: make it lighter in feel, not in contrast. Keep it at 4.5:1 or above and drop the weight and size a notch. · 2. Prices: switch from red to brand navy, and keep red only for badges. · 3. Ask which "grey filter text" the client means.
Reply: "Thanks! We'll soften the filter and secondary text and calm the prices down, while keeping the contrast the AA brief requires. Quick question: do you mean the search-bar fields, the sidebar filters, or the grey details on the cards?"

## Decode — listings-redesign

| # | Client said | Likely meaning (confidence) | Change |
|---|---|---|---|
| 1 | "grey filter text… lighter and smaller, too heavy" | a) Grey secondary text feels heavy: search placeholders (#888, 3.5:1) and card meta (#777, 4.5:1) (50%) | Drop the weight and tighten the size a little. Placeholders → italic-free, 14→13px, colour kept at about #6B6B6B (≥4.5:1). Card meta ~13→12.5px (see conflicts). |
| | | b) The sidebar "Filters" list (#222, ~13px, dense 26px rows) feels heavy (35%) | List text #222 → #4A4A4A (~8.9:1). Weight 400, row gap ~26→30px so it feels lighter without a smaller size. |
| | | c) The whole filter area is too dominant next to the cards (15%) | Remove the white sidebar panel and use the page background. Ask: Q1 |
| 2 | "prices in red look aggressive" | a) The saturated red #E63946 is too alarming for a price (60%) | Price colour → navy #0B2545 (the header colour), keeping the bold weight. Contrast ~14:1. |
| | | b) Red appears everywhere (prices, HOT!, -10%, SEARCH) and adds up to alarm (30%) | Prices navy. SEARCH → navy or teal. Keep red only for the HOT!/-10% badges. |
| | | c) Wants a softer red, not a different colour (10%) | Fallback: #C62F3B (~5.3:1 with white). Offer as a variant only. |

**Facts used:** price #E63946 on white = 4.17:1 (fails AA for text under large size) · SEARCH button white on the same red = 4.17:1 (fails AA) · placeholder #888 = 3.54:1 (fails) · card meta #777 = 4.48:1 (just fails) · sidebar labels #222 = 15.9:1, ~13px · prices ~19px bold. Colours were sampled from pixels. Sizes are `~` estimates.

### Keep as is
- A: Card titles, bold dark, clear hierarchy. Don't lighten them when softening the meta text.
- B: Sidebar labels at ≥4.5:1. They can lose weight but must stay readable.

### Conflicts
- **#1 vs the AA brief.** "Lighter and smaller" pushes the text toward failure. The placeholders and card meta already fail or barely pass, so a literal change would breach the brief. Suggest: the client gets a lighter feel by weight and size, and contrast stays ≥4.5:1. I'd show it as a before/after.
- **#1 vs body size.** Text is already ~12–13px, which is small. I'd avoid going smaller than ~12px, so I'd reduce it by 0–1px at most. Lighter weight and colour carry the effect instead.
- #2 fixes an existing AA problem (the red price, 4.17:1), so it aligns with the brief.

### Ask the client (max 3)
1. Which grey text do you mean: A) search-bar fields, B) sidebar filters, or C) the details under each card title? See marker 1 and marker B.
2. Prices: A) navy like the header, or B) a softer red? (I recommend A.)

### Reply (English)
**Friendly:** Thanks for the feedback! We'll make the filter and secondary text lighter and calmer, and soften the prices so they feel less aggressive. Since the brief asks for WCAG AA, we'll keep enough contrast for readability, so the change comes from weight and tone rather than very pale grey. Two quick questions: which grey text did you mainly mean (the search fields, the sidebar filters, or the card details)? And for prices, would you prefer navy like the header, or a softer red?

**Firm:** We'll lighten the filter text and tone down the prices in this round. The brief requires WCAG AA, so we can lighten the weight and size but not go below the minimum contrast. Please confirm which grey text you mean (search fields, sidebar filters, or card details), and whether you prefer navy or a softer red for prices.

### Scope
Round 1 of 3 · 2 items, both in scope · no new requests. Ledger: `.feedback-decoder/listings-redesign.md`

Overlay: `.feedback-decoder/work/overlay.png`

One extra: the SEARCH button (white on red, 4.17:1) also fails AA and is part of the red the client finds loud. It's worth changing in this round, and I can mention it to them as an accessibility fix.
