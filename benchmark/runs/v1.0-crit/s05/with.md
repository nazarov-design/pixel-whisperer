**TL;DR** — Main issue: the small grey info row (time, difficulty, servings, rating) is too faint to read. Exercise: Contrast checker sweep, 20 min. Test every text colour on your screen against its background and fix anything below the minimum ratio.

## Desk crit: Recipe detail screen · beginner

I judged your level from the work, since you didn't say. Tell me if that's wrong.

### What works
- **The title** (marker A): it's bold, dark and large, so it's clearly the first text you read. The dark blue-green on white is easy on the eyes.
- **The warm palette** (marker B): the yellow, orange and tomato red feel like the dish. The teal bars and the red button give you a cool/warm contrast without extra colours.
- **The basic structure**: the image is on top, then the title, ingredients and steps. That order is the one a cook needs. The numbered steps and bulleted ingredients are the right list types.

### Fix first
**1. The info row is nearly invisible** (marker 1) · *Principle: contrast*
- **What I see:** "30 min · Medium · 2 servings · 4.8" is tiny, light grey on white, and the icons are even paler.
- **Why it matters:** on a recipe screen, cooking time and difficulty are what someone checks first, so the least readable text on the page is the most useful. Light grey on white probably falls below the 4.5:1 minimum for small text.
- **Try this:** darken the grey to about #555 or darker and raise the size by 2–3 px. Keep the row quieter than the title, but make it readable.

**2. The teal bars are louder than the content** (marker 2) · *Principle: hierarchy*
- **What I see:** "INGREDIENTS" and "STEPS" are white text on full-width saturated bars. They're the heaviest shapes after the image, and they pull your eye away from the title.
- **Why it matters:** section labels should help you find your place, not compete with the title or the content.
- **Try this:** swap the bar for a coloured label with no fill, and keep a thin line or extra space above it. The title is also centred while everything below is left-aligned, so try left-aligning it too.

**3. The top icons don't match** (marker 3) · *Principle: contrast*
- **What I see:** the back arrow is small and white on yellow, so it's hard to see. The heart is black and bigger. They look like they belong to different sets.
- **Why it matters:** white on that yellow is low contrast, and these are the main controls on the screen.
- **Try this:** use one colour and one stroke weight for both, in dark ink or inside a small white circle. Make the tap area about 44 px.

Later: the "+" button doesn't say what it does (add to a list? start cooking?). The steps are also packed tighter than the ingredients, so give them more line spacing.

### Exercise (20 min): Contrast checker sweep
**Task:** use any free contrast checker (search "WebAIM contrast checker"). Write down the colour pair and ratio for every text and icon on this screen. Then fix the ones that fail.
**Done when:** all body text is at least 4.5:1, large text and icons are at least 3:1, and you have a before/after list of the ratios.

### Study
Look at recipe apps and food-blog article pages. Notice how they show time and servings (usually dark, medium-sized text with clear icons) and how little decoration they put around section headings.

Progress: first session, so I started a journal. Contrast is flagged as a recurring-issue watch. Overlay: `.desk-crit/work/overlay.png`. I left the journal in `.desk-crit/student.md`. This folder isn't a git repo, so nothing needed ignoring.
