The gradient and the frosted card look good, but contrast is the main problem, and it hurts usability.

**What works**
- The coral-to-lavender gradient is soft and suits the glass effect.
- The card proportions, rounded corners and thin light border are well judged.
- The spacing and vertical rhythm are consistent, and the layout is simple and centered.
- The solid white LOGIN button is the clear primary action.

**Main problems**
1. **White text on a pale, translucent card.** This is the biggest issue.
   - The title, subtitle, "Remember me", "Forgot password?", "or continue with" and "Sign up" are white on a light pink-white surface. Contrast is probably around 1.2–1.5:1, against the 4.5:1 WCAG asks for body text.
   - The small text (about 11–12px) is nearly unreadable.
   - Fix: darken the text to a deep plum or charcoal, or make the card more opaque or tinted darker. If you want to keep white text, the glass needs to be darker, for example `rgba(60,30,80,0.25)` with a stronger blur.
2. **The social buttons nearly disappear.** Their white labels on a faint white fill have almost no contrast, and they don't look clickable. Give them a visible border or a stronger fill, a darker label, and ideally their logos.
3. **The LOGIN label is low contrast too.** Light purple on white is about 2.5:1. Use a darker purple, or give the button a solid purple fill with white text.
4. **Placeholders are weak and there are no labels.** The grey placeholders on a near-white field are faint. Placeholders also vanish once the user types, so add visible labels or floating labels.

**Smaller polish**
- The "Remember me" checkbox is tiny, and its hit area looks too small.
- "Forgot password?" and "Sign up" don't look like links. Add an underline or an accent color, and make "Sign up" stand out from the plain text around it.
- The type hierarchy is flat. The title is bold and big, but everything else sits at one small size. Raise the secondary text to at least 13–14px.
- The inputs have no visible edge. A 1px light border would help, along with a clear focus state (not visible here, so make sure you design one).
- The "— or continue with —" dashes are a bit dated. A hairline divider with centered text would look cleaner.
- Add a subtle shadow under the card. Glassmorphism needs something behind the card to blur, and the background is a plain gradient, so the effect barely reads. A few colored blobs or shapes behind the card would show off the frosted blur.
- The card has a lot of empty space around it. That's fine for a login, but the card could be slightly larger, or you could add a logo or icon at the top.

If you only change one thing, fix the text contrast. That one change would make this design a lot stronger.
