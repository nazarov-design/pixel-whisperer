**TL;DR** — Main issue: the white text and light-on-light elements disappear against the pale glass card. Exercise: Contrast checker sweep, 20 min. Log the contrast ratio of every text and button against what sits behind it.

## Desk crit: Glassmorphism login · beginner–intermediate (inferred, you didn't say)

### What works
- **The card itself** (marker A). The rounded corners, thin light border and generous padding give a convincing frosted-panel shape, and its centered, portrait proportions suit a login.
- **The input fields** (marker B). They're the most solid, readable shapes on the card, and the dark placeholder text is legible. The two fields share identical widths and left edges, so the form column looks tidy.
- **The background gradient.** The coral-to-lavender sweep has enough colour variation to make a glass effect believable, and it stays in one warm-to-cool family.

### Fix first
**1. White text and controls are too faint** (marker 1) · *Principle: contrast*
The title, subtitle, "Remember me", "Forgot password?", "or continue with" and the Google, Apple and Facebook buttons are all white or near-white on a pale pink card. The social buttons are almost invisible, and the small helper text is a strain to read. Glass only works when the content has more contrast than the blur behind it. Two ways to fix it:
- **Darken the text.** Use a deep plum or near-black at about 80–90% opacity for the title and helper text. Don't rely on white.
- **Tint the card.** Add a slightly darker or more saturated fill, or a subtle shadow, so the white elements stand out.

Aim for 4.5:1 on small text and 3:1 on the large title. Give the social buttons a visible border or a stronger fill so they read as buttons.

**2. The LOGIN button doesn't lead** (marker 2) · *Principle: hierarchy*
The one action that matters is a white bar with small lilac text. It's about as visible as the inputs above it, and the lilac text is low-contrast on white. The first thing the eye should find is the next step. Try a solid, saturated fill, such as a deep purple that pulls from the gradient's bottom corner, with white text at 16px or larger. Then it's clearly the loudest element on the card.

**3. The bottom of the card is cramped** (marker 3) · *Principle: rhythm*
"Don't have an account? Sign up" sits only about 8px under the social buttons, but the other groups have 25–40px between them. The same tight gap separates the title from its subtitle. Pick a spacing scale, for example 8 / 16 / 24 / 32. Use small gaps inside a group and larger ones between groups. Give the sign-up link about 24px of space and make "Sign up" a visibly different colour or weight.

*Later:* the "Remember me" checkbox is tiny, and a visible focus state on the inputs would help.

### Exercise (20 min): Contrast checker sweep
Open a contrast checker. Sample each text colour and the colour behind it, and list the ratios for the title, subtitle, helper text, LOGIN, social labels and sign-up link. Adjust each failing item until all small text reaches 4.5:1 and the title reaches 3:1.
**Done when:** you have a before/after list of ratios and a revised design where nothing needs squinting.

### Study
Look at well-regarded glassmorphism UI such as OS control panels and widget cards. Notice what they do to keep text readable: darker or tinted fills, strong text colours, and one clearly saturated primary button. Then squint at your own screen and see which element you find first.

Progress: first session, so no history yet. Overlay: `.desk-crit/work/overlay.png`

**Journal not saved:** my write to `.desk-crit/student.md` was blocked by a permissions prompt, so no progress journal exists yet. This crit is recorded nowhere except this chat. I did save a copy of your design at `.desk-crit/works/login-v1.png`. If you allow the journal write, I'll record this session, including the contrast issue and the open exercise, so the next crit can track it.
