# Phrasebook: vague client feedback → meanings → fixes

Search it, don't read it whole: `grep -i -A8 "<word>" phrasebook.md`. Aliases include common Russian, German and Spanish forms. Meanings are listed in typical order of likelihood; always re-rank against what the design actually shows. Fixes are starting points; take real values from the design.

## Contents
1. Energy: pop, boring, flat, wow, bold (E1–E8)
2. Premium: expensive, cheap, elegant, luxury (P1–P7)
3. Modern: dated, fresh, young, techy (M1–M6)
4. Clean & air: busy, cluttered, simple, empty (C1–C7)
5. Trust: serious, professional, credible (T1–T6)
6. Readability & clarity: hard to read, confusing, can't find (R1–R6)
7. Friendly & warm: playful, human, cozy (F1–F6)
8. Emphasis & size: bigger logo, stand out, too loud (S1–S7)
9. Color: don't like the color, too dark, more colorful (K1–K6)
10. Gut feeling & layout: something's off, unbalanced (G1–G6)
11. Conversion: won't click, sell, urgency (V1–V4)

Universal checks before decoding anything: (a) squint test: what are the first 3 things the eye hits? (b) type scale ratio H1:body; (c) CTA contrast ratio; (d) spacing consistency; (e) number of colors / fonts in use.

---

## 1. Energy

### E1 "make it pop"
Aliases: pop more, doesn't pop, stand out, punchy, «чтобы цепляло», «не цепляет», «сделайте ярче», "mehr Pep", "que destaque"
Means: 1) no clear focal point; 2) muted/low-contrast palette; 3) flat, no imagery or depth.
Check: is there one element clearly dominant? CTA contrast? Is the palette mostly greys?
Fixes: one dominant element (H1 ×1.3–1.5 or hero image); CTA in a saturated accent ≥4.5:1; one accent color used ≤10% of area; real imagery instead of placeholders.
Avoid: making everything louder at once; that kills the focal point again.

### E2 "it's boring" / "feels flat"
Aliases: dull, bland, lifeless, «скучно», «пресно», «плоско», "langweilig", "aburrido"
Means: 1) uniform rhythm (every section same height/layout); 2) no contrast in scale; 3) no imagery/personality.
Check: are all sections the same structure? Is the type scale flat (ratio <1.5 between levels)?
Fixes: vary section rhythm (one full-bleed, one split, one dense); increase scale contrast (H1:body ≥3:1); add one signature element (illustration, photo, bold color block).

### E3 "needs more energy" / "more dynamic"
Aliases: more dynamic, more movement, «динамичнее», «больше движения», "dynamischer"
Means: 1) everything centered and symmetric; 2) static horizontal bands; 3) wants motion/animation.
Fixes: asymmetric layout (text left, visual bleeding right); diagonal or overlapping elements; suggest one subtle motion (hover, scroll reveal), ask if animation is in scope.

### E4 "I want a wow effect"
Aliases: wow, impressive, «вау-эффект», «чтобы ахнули», "Wow-Effekt"
Means: 1) hero is weak, first screen forgettable; 2) wants a signature visual; 3) comparing with an award site they saw.
Fixes: rework only the first screen: oversized type or one striking image; ask for the reference they have in mind (closed: "more like A or B?").
Scope: often a new request disguised as a tweak; check the brief.

### E5 "make it exciting" / "more fun"
See also F2. Means: target audience younger than the design implies, or palette too corporate.
Fixes: brighter secondary color, rounder shapes (radius 4→12px), more playful copy; ask which audience segment.

### E6 "too static"
Means: 1) wants animation; 2) grid too rigid. Fixes: break the grid once per page; propose micro-interactions; confirm animation scope.

### E7 "needs more life" / "feels empty of people"
Aliases: «нет жизни», «мёртвый», "leblos"
Means: 1) no human imagery; 2) no real content (placeholders, lorem); 3) cold palette.
Fixes: real photos with people / real product use; real copy; warm one neutral (cool grey → warm grey).

### E8 "make it bolder"
Aliases: stronger, more confident, «смелее», «жирнее», "mutiger", "más atrevido"
Means: 1) type weight too light; 2) timid scale; 3) safe colors.
Fixes: headline weight 400–500 → 700; H1 size up one step; larger color blocks; fewer, bigger elements.

## 2. Premium

### P1 "look more premium" / "more expensive"
Aliases: high-end, «дороже», «премиальнее», «чтобы выглядело дорого», "hochwertiger", "más premium"
Means: 1) too many elements competing; 2) cheap-looking details (default shadows, gradients, stock icons, clip-art); 3) cramped spacing; 4) generic typography.
Check: count of colors, fonts, shadow styles; spacing between sections; image quality.
Fixes: remove 30% of elements; increase whitespace (section padding +30–50%); restrained palette (1 neutral family + 1 accent); refined type (high-contrast serif or well-tracked sans, uppercase labels +8% tracking); high-quality imagery with consistent treatment.
Avoid: gold color by default; it often reads cheaper.

### P2 "feels cheap"
Aliases: «дёшево», «колхоз», «как шаблон», "billig", "barato"
Means: 1) inconsistent details (radii, shadows, icon styles mixed); 2) low-quality or stock imagery; 3) too many effects; 4) default fonts.
Fixes: one radius, one shadow, one icon set; replace or crop stock images; strip effects; type pairing change.

### P3 "more luxurious"
Means: wants slower, quieter, larger: big imagery, very generous spacing, small elegant text, dark or warm neutral palette.
Fixes: hero image full-bleed; body 16→15px with more line height; uppercase micro-labels; reduce number of CTAs to one.

### P4 "more elegant" / "sophisticated"
Aliases: «элегантнее», «изящнее», "eleganter"
Means: 1) heavy weights and thick strokes; 2) crowded; 3) loud colors.
Fixes: lighter weights for display, thinner dividers (2→1px), muted palette, more whitespace, better alignment discipline.

### P5 "classy" / "stylish"
Same family as P1/P4. Ask for one brand they consider classy, as a closed question with two options.

### P6 "like Apple" / "like <famous brand>"
Aliases: «как у Apple», «как у Тинькофф»
Means: usually not "copy them" but: big product imagery, lots of white space, one message per screen, very short copy.
Fixes: one idea per section, product shot as hero, cut copy by half. Clarify: which page of theirs? Do not copy assets.

### P7 "less template-y" / "looks like a template"
Aliases: «шаблонно», «как у всех», "wie ein Template"
Means: 1) default component library look; 2) generic stock imagery; 3) predictable hero-features-testimonials layout.
Fixes: one custom signature element (illustration style, custom type treatment, unusual grid); brand-specific imagery; rewrite generic headings.

## 3. Modern

### M1 "make it more modern"
Aliases: contemporary, up to date, «современнее», «посовременнее», "moderner", "más moderno"
Means: 1) dated typography (Times/Georgia body, Comic, script); 2) dated effects (bevels, heavy shadows, textures, double borders); 3) dense layouts; 4) small type.
Check: fonts, decoration, body size, line length, spacing.
Fixes: modern grotesque or neo-grotesque for UI text; body ≥16px; remove ornamental borders; flatter surfaces with subtle depth; more whitespace; larger headlines.
Keep: the brand's warmth or personality, if the client likes it; modern ≠ cold.

### M2 "feels dated" / "old-fashioned"
Aliases: outdated, «устарело», «как в 2010», «старомодно», "altmodisch", "anticuado"
Means: same as M1, plus: centered everything, small images, decorative separators, skeuomorphic buttons.
Fixes: left-aligned text blocks, larger imagery, simple buttons with solid fill.

### M3 "fresher" / "more fresh"
Aliases: «свежее», "frischer"
Means: 1) palette muddy/desaturated; 2) too much dark; 3) visually heavy.
Fixes: lighter backgrounds, cleaner accent (higher saturation, slightly cooler), more air.

### M4 "trendy" / "like what's in now"
Means: references to current trends (bento grids, big type, gradients, 3D). Ask for an example; trends age fast. Suggest one trendy element on a timeless base.

### M5 "younger" / "for a younger audience"
Aliases: «моложе», «для молодёжи», "jünger"
Fixes: bolder color, bigger type, more casual copy, playful shapes, mobile-first layout. Check the brief's audience first; a conflict is common.

### M6 "more techy" / "more innovative"
Aliases: «технологичнее», «инновационнее»
Means: product UI not shown; generic imagery; soft palette.
Fixes: show real product UI; precise grid; mono or geometric accents; darker or high-contrast palette option.

## 4. Clean & air

### C1 "make it cleaner"
Aliases: clean, tidy, «чище», «почище», «аккуратнее», "aufgeräumter", "más limpio"
Means: 1) inconsistent alignment; 2) too many elements/colors; 3) uneven spacing; 4) borders and boxes everywhere.
Check: count alignment lines; count distinct spacing values; count boxes/borders.
Fixes: snap to fewer alignment lines; spacing scale (8/16/24/32/48/80); remove borders where whitespace can separate; fewer colors.

### C2 "more air" / "more whitespace"
Aliases: breathing room, «больше воздуха», «дышать», "mehr Luft", "más aire"
Means: 1) tight internal spacing in components; 2) small gaps between groups; 3) line height too tight; 4) too much content.
Fixes: line height 1.3→1.5 for body; group gaps ×1.5; cut content; increase side margins.
Conflict watch: often paired with "make things bigger" (see G-conflicts); resolve by cutting content.

### C3 "too busy" / "too cluttered"
Aliases: noisy, overloaded, «перегружено», «каша», «много всего», "überladen", "recargado"
Means: 1) too many competing focal points; 2) too many styles; 3) too much content above the fold.
Fixes: one primary action per screen; demote secondary items (size, color); move content below the fold or to other pages; reduce styles.

### C4 "simpler" / "minimal"
Aliases: «проще», «минималистичнее», "einfacher", "más simple"
Means: fewer things, not smaller things. Fixes: remove decorations, merge similar sections, shorten copy, reduce palette to neutrals + 1 accent.

### C5 "too empty" / "too much white"
Aliases: «пусто», «пустовато», "zu leer"
Means: 1) whitespace not purposeful (elements floating, no grouping); 2) content too small for canvas; 3) wants more info.
Fixes: bigger content, tighter grouping with larger gaps between groups; add a visual anchor; do not just fill space.

### C6 "less noise"
Same as C3. Usually: background patterns, gradients, too many icons, decorative lines.

### C7 "too much going on on mobile"
Aliases: «на телефоне каша»
Means: desktop layout squashed; too many columns; small tap targets.
Fixes: single column, stacked sections, tap targets ≥44px, hide secondary content behind disclosure.

## 5. Trust

### T1 "more trustworthy" / "more serious"
Aliases: credible, reliable, «солиднее», «больше доверия», «серьёзнее», "vertrauenswürdiger", "más confiable"
Means: 1) playful details (rounded fonts, emoji, cartoon icons, bright gradients) for a money/health/legal topic; 2) no proof (reviews, logos, numbers, licences); 3) inconsistent UI.
Fixes: calmer palette (navy/deep green/neutral + one accent); neutral typography; add proof elements (licence, guarantee, real numbers); consistent components; key numbers large and clear.
Keep: friendliness in copy if it's the brand voice.

### T2 "more professional"
Aliases: «профессиональнее», «по-взрослому», "professioneller"
Means: inconsistency (spacing, alignment, styles) more than style. Fixes: grid discipline, consistent components, tighter copy, real content.

### T3 "corporate but not boring"
A built-in tension: confirm which side matters more (closed question). Fixes: neutral base + one bold brand color used confidently; strong photography; disciplined grid.

### T4 "looks scammy" / "feels unsafe"
Aliases: «как лохотрон», «подозрительно», "unseriös"
Means: urgency patterns, too many CTAs, low-quality images, missing company info.
Fixes: remove fake urgency, add company details, security badges only if real, calm CTAs.

### T5 "more credible numbers" / "numbers get lost"
Aliases: «цифры теряются»
Fixes: key numbers as large display type with labels; tabular figures; consistent decimal alignment.

### T6 "more solid" / "stable"
Means: thin weights, floating elements, low contrast. Fixes: heavier weights for headings, defined containers, stronger contrast, aligned edges.

## 6. Readability & clarity

### R1 "hard to read"
Aliases: can't read, «не читается», «тяжело читать», "schwer lesbar", "difícil de leer"
Means: 1) low contrast (<4.5:1); 2) small size (<16px body web, <14px UI); 3) long lines (>80 chars); 4) tight line height; 5) text over images/patterns.
Fixes: concrete numbers: body 14→16px, contrast to ≥4.5:1, line length 60–75 characters, line height 1.5, scrim behind text on images.

### R2 "text is too small"
Fixes: scale up the whole type ramp, not one element; check mobile separately.

### R3 "too much text" / "nobody will read this"
Aliases: «много букв», «простыня», "zu viel Text"
Fixes: cut copy by 30–50%; split into scannable chunks with subheads; bullets; pull key fact into a heading. Copywriting may be out of scope; flag.

### R4 "I can't find X"
Means: X lacks visual weight or is in an unexpected place. Fixes: move X to a standard location; increase its weight; add it to nav.

### R5 "it's confusing"
Aliases: unclear, «непонятно», «запутанно», "verwirrend"
Means: 1) unclear hierarchy (what first?); 2) unclear purpose (what is this page for?); 3) ambiguous labels.
Fixes: one headline that states the value; a clear primary action; plain-language labels. Ask: "Confusing which part: what we offer, or what to do next?"

### R6 "the eye doesn't know where to go"
Means: no hierarchy. Fixes: decide reading order 1-2-3; scale and contrast follow that order; remove competing accents.

## 7. Friendly & warm

### F1 "friendlier" / "warmer"
Aliases: «дружелюбнее», «теплее», "freundlicher", "más cálido"
Fixes: warm neutrals (cool grey → warm grey/cream); rounder radii; human photos; conversational copy; softer accent.

### F2 "more playful" / "fun"
Aliases: «веселее», «игривее», "verspielter"
Fixes: illustration or shapes; brighter secondary palette; playful microcopy. Check brief audience; conflicts with trust topics.

### F3 "more human"
Fixes: real people photography, first-person copy, team faces, handwritten or friendly details used sparingly.

### F4 "cozy"
Fixes: warm palette, textures used sparingly, softer contrast (not low contrast for text), rounded type, natural imagery.

### F5 "too cold" / "sterile"
Aliases: «холодно», «стерильно», "zu kühl"
Means: pure white + grey + blue. Fixes: warm one neutral, add a warm accent, add imagery.

### F6 "more approachable"
Fixes: simpler language, larger friendly CTA, less jargon, fewer barriers (fewer form fields).

## 8. Emphasis & size

### S1 "make the logo bigger"
Aliases: «логотип побольше», "Logo größer"
Means: 1) brand not recognized on first screen; 2) client pride, not a design problem.
Fixes: modest increase (e.g. 28→36px height) or brand color in the hero; offer A/B. Explain that the headline sells, the logo signs.

### S2 "make everything bigger"
Aliases: «всё крупнее», "alles größer"
Means: 1) viewed on a large monitor/zoomed out; 2) small type; 3) wants more impact.
Fixes: increase type ramp one step; fewer elements per screen. Conflicts with "more air": resolve by cutting content.

### S3 "make X stand out more"
Fixes: contrast in one dimension (size, color, weight, or space around it), not all four; reduce competing elements nearby.

### S4 "make it more visible"
Same as S3. Ask "visible at which moment: first screen or when scrolling?"

### S5 "put it above the fold"
Means: they fear users won't scroll. Fixes: show a hint of it in the first screen (anchor link, preview), or move if truly primary. Mention scroll is normal; offer evidence-based compromise.

### S6 "it's too loud" / "too aggressive"
Aliases: «кричит», «агрессивно», "zu laut"
Fixes: reduce saturation, reduce number of accent uses, lighter weights, remove ALL CAPS and exclamation marks.

### S7 "less important" / "tone it down"
Fixes: smaller size, lighter color, move down the page. Make sure tone-down doesn't break contrast for text.

## 9. Color

### K1 "I don't like the color"
Aliases: «не нравится цвет», "die Farbe gefällt mir nicht"
Means: 1) personal taste; 2) association with a competitor; 3) wrong mood. Ask which color (closed: "the blue buttons or the beige background?"); show 2 alternatives within brand.

### K2 "more colorful"
Fixes: introduce a secondary accent; colored section backgrounds; colorful imagery. Keep text colors neutral.

### K3 "too dark" / "gloomy"
Aliases: «мрачно», «темно», "zu düster"
Fixes: lighter background or lighter sections alternating; warmer darks; more imagery with light.

### K4 "too bright" / "garish"
Aliases: «кислотно», «аляповато», "zu grell"
Fixes: reduce saturation 15–25%; use bright color for small areas only; add neutrals.

### K5 "more on-brand"
Check brand guidelines in brief. Fixes: brand colors in primary roles, brand typography, brand imagery style.

### K6 "more contrast"
Means: literally contrast (text/background) or visual punch. Fixes: text to ≥4.5:1; stronger value differences between sections.

## 10. Gut feeling & layout

### G1 "something's off" / "doesn't feel right"
Aliases: «что-то не то», «не цепляет, но не знаю почему», "irgendwas stimmt nicht"
Means: usually a fundamentals issue: misalignment, inconsistent spacing, weak hierarchy, or mismatch with the brand mood.
Fixes: audit alignment/spacing first (cheap fixes); then ask 1 closed question about mood with two variants.

### G2 "unbalanced" / "lopsided"
Aliases: «перекошено», «не сбалансировано»
Fixes: check visual weight left vs right; balance a heavy image with a stronger text block or adjust sizes; align to a grid.

### G3 "I'll know it when I see it"
Means: client can't articulate. Fixes: don't decode further; offer 2–3 quick directional variants (mood level, not polish) and ask them to pick.

### G4 "looks like <competitor>"
Fixes: identify the shared element (color, layout, illustration style); change that one thing decisively.

### G5 "make it like the reference"
Clarify which aspect: color, layout, type, imagery. Never copy; translate the quality into this brand.

### G6 "can you try a few options?"
Scope signal. Fixes: offer 2 variants on one variable; count it in the ledger as part of the round.

## 11. Conversion

### V1 "people won't click" / "the button gets lost"
Fixes: CTA contrast ≥4.5:1 and the only saturated element nearby; action-specific label ("Start free trial" not "Submit"); size ≥44px height; whitespace around it.

### V2 "make it sell" / "more conversion"
Fixes: clear value headline; proof near CTA; one primary action; remove distractions. Note: design can't promise conversion numbers.

### V3 "more urgency"
Caution: avoid dark patterns (fake timers). Fixes: real deadlines or limited availability stated plainly.

### V4 "looks like an ad"
Means: banner blindness triggers (badges, starbursts, stock smiles, all caps). Fixes: editorial layout, honest product imagery, calm typography.
