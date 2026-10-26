**TL;DR**: The main issue is that the three hero visuals look like placeholders and say nothing about money. Exercise (40 min): redraw all three heroes as one system, using real product UI as the hero.

## Desk crit: Finance app onboarding (3 screens) · advanced-intermediate

### What works
- **The headlines** (marker A): bold, tight, left-aligned, two lines at most. They carry the whole flow, and you can follow the story from headlines alone.
- **The primary button** (marker A): full width, a single saturated blue, anchored at the same spot on every screen. The thumb target never moves, and that's the right call.
- **The tinted hero panels:** a different pastel per screen gives the steps a sense of progress without adding any extra UI.

### Fix first
**1. The hero art is decoration, not communication** (marker 1) · *Principle: hierarchy and composition*
- **What I see:** a tilted blue square, a green gradient ball and a padlock. They use three unrelated rendering styles: flat, soft-shadow gradient, and an OS-style 3D emoji. None of them relates to its headline except the padlock, which is the most clichéd option available.
- **Why it matters:** the hero takes about 40% of every screen, and it's the biggest thing the eye lands on. It's the loudest element, and it says the least. "All your accounts in one place" is a visual idea (stacked cards, merged balances), and the blue square doesn't show it. In a portfolio this is the first thing a reviewer reads as "template."
- **Try this:** show the product. Screen 1 could be a few stacked account cards with real balances. Screen 2 could be a budget ring or bar with a category label. Screen 3 could be a biometric prompt or a shield on a card. Use one stroke weight, one corner radius and one palette across all three. Drop the emoji entirely.

**2. Body text is too pale to read** (marker 2) · *Principle: contrast*
- **What I see:** the grey-blue body copy on white looks like roughly 2.8:1 to 3:1, under the 4.5:1 minimum for small text. The "Skip" link, which is the escape hatch, is faint too.
- **Why it matters:** this is a finance app, so trust and legibility are the product. Washed-out copy reads as "unfinished" and fails accessibility review, which a hiring manager may check.
- **Try this:** darken the body to about `#4B5563` or deeper, and check the ratio. Make Skip darker too.

**3. The lower half is unresolved** (marker 3) · *Principle: rhythm and composition*
- **What I see:**
  - There is a dead gap of roughly 100px between the copy and the button on screens 1 and 3.
  - The copy length is uneven. Screen 2 has four lines, and screens 1 and 3 have one or two.
  - The headline starts at y≈357, ≈347 and ≈355 across the three screens, so it jumps when you swipe.
  - "I already have an account" appears only on screen 3. It's tiny, sits tight against the button, and is the same blue as the CTA, so it competes with the button.
- **Why it matters:** the jumping headline is the kind of flaw a reviewer notices when you flip through the screens. A returning user has to wait until the last step to find the login, which is a real product problem too.
- **Try this:** lock the headline to one y-position and trim the copy to about 90 characters each. Move "I already have an account" into a consistent slot, or show it on every screen. Fix the button label too: "Next", "Continue" and "Get started" mix verbs for no reason. Use "Next, Next, Get started", or stay with one.

**Later:** the progress dots are tiny and left-aligned above the headline. "Bank-level security" is marketing boilerplate, and a concrete claim would be stronger.

### Exercise (40 min): Hero system
Task: in 40 minutes, redo the three heroes as one illustration system. Use one stroke weight, one radius, two colors plus a neutral, and real product UI where possible. Then put the old and new screens side by side and flip through them. Done when: a stranger can guess each screen's topic from the hero alone, with the headline covered.

### Study
Look at onboarding flows from fintech apps you admire, and notice how the hero shows a real product moment instead of an abstract shape. Check how they handle login access on step 1 versus step 3.

Progress: first session, no history yet. Overlay: `./.desk-crit/work/overlay.png`. Journal: `./.desk-crit/student.md`.
