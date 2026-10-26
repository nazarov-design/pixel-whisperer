**TL;DR** — Main issue: white text sits on a pale frosted card, so the title, links and social buttons are hard to read. Exercise: Contrast pass, 30 min. Fix the contrast on this one screen and check each text/background pair against a ratio target.

## Desk crit: Glassmorphism login · beginner–intermediate (inferred, since you didn't say. Tell me if that's off.)

### What works
- **The gradient background** (outside the card): the coral-to-lavender sweep is soft and gives the glass something to blur against. The mood fits the style.
- **The card frame** (marker A): the rounded corners, the thin light border and the generous outer margin look like real glassmorphism. The card is clearly centered and isolated.
- **The input fields** (marker A): they are the most legible elements on the screen. They're consistent in size and radius, evenly spaced, and aligned to one left and right edge.

### Fix first
**1. White text on a light surface** (marker 1) · *Principle: contrast*
What I see → "Welcome Back!", the subtitle, "Remember me", "Forgot password?" and the footer are all white on a pink card that is nearly white. The subtitle and small links are around 11–12px, so they almost vanish. Glass only works when the backdrop behind the text is dark or saturated enough. Here the card sits on the lightest part of the gradient. The card needs a tint, or the text needs to go dark. Try dark text (a deep plum) at about 4.5:1 contrast for body text. Or darken the card fill and the gradient behind it. Also raise the small text to 13–14px.

**2. The actions have no ranking** (marker 2) · *Principle: hierarchy*
What I see → The LOGIN button is white on a near-white card, with lavender text. It is only slightly more visible than the inputs. The Google/Apple/Facebook buttons are nearly invisible, with white labels on a faint white fill. This is the one action the screen exists for, and it doesn't stand out. Give LOGIN a solid, saturated fill, such as the deep purple from the gradient's corner, with white text. Give the social buttons a visible outline and dark text so they read as secondary.

**3. The bottom of the card is cramped** (marker 3) · *Principle: rhythm/spacing*
What I see → "Don't have an account? Sign up" sits about 12px under the social buttons and about 25px above the card edge. The title and subtitle are also tight to each other. The middle of the card is more open than its ends. Add more space above the footer and keep the vertical gaps on a consistent scale (for example 8/16/24/32). This is a later fix, and it's easier once 1 and 2 are done.

### Exercise (30 min): Contrast pass
Duplicate the screen. Pick a contrast checker and test every text/background pair. Note the ratio for each. Change fills and colors until body text hits 4.5:1 and the button label hits at least 4.5:1. Don't touch the layout. Done when: every text element passes, and in a squint test (blur your eyes, or blur the screenshot) you can still find LOGIN first.

### Study
Look at well-made glassmorphism UIs (OS control panels, music-player cards) and notice how the glass is always paired with a darker tint or a darker backdrop. The text is rarely pure white on a light surface. Look at login screens from auth products and notice that there is one filled primary button, and that social options are outlined.

Progress: contrast, 1st time · hierarchy, 1st time · Overlay: `.desk-crit/work/overlay.png`
