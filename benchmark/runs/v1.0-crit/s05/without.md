# Review: Shakshuka recipe screen

You've built a clean, readable screen with a clear structure. Here's what works and what to fix, most important first.

## What works
- **Clear hierarchy.** Hero, title, meta, Ingredients, Steps is the order people expect for a recipe.
- **A consistent palette.** The warm yellow, orange and tomato red fit the food, and the teal section bars contrast well with them.
- **Readable body text.** The ingredient and step text is dark on an off-white background, and the line spacing is comfortable.
- **Numbered steps and bulleted ingredients.** The list types suit the content.

## Problems to fix

1. **The hero image is a placeholder.** Two circles don't show the dish, and a recipe screen sells itself with a photo of the food. Use a real photo, or an illustration that actually looks like shakshuka (a pan with eggs in sauce). If you can't get one, a simple pan-and-eggs drawing is better than abstract circles.

2. **The back arrow and heart are hard to see.** The white "<" is small and sits on a bright yellow background, so it has very low contrast. The heart is a thin black outline that doesn't match it. Fixes:
   - Make both icons the same style and size.
   - Put each in a semi-transparent circular button (about 40 px) so they stay visible on any image.
   - Make the touch targets at least 44×44 px. The current icons are too small to tap comfortably.

3. **The meta row is too faint.** The "30 min · Medium · 2 servings · 4.8" text is small, light grey and sits close to the title. These are key facts for a cook. Darken the text, increase its size to about 14 px, and add more space above it. The icons are also inconsistent: some are emoji (🔥, 👥) and others are plain glyphs (⏱, ★). Pick one icon set.

4. **The floating "+" button has no clear meaning.** Does it add to a shopping list, start cooking, or save the recipe? A bare "+" doesn't say. Use a label or a more specific icon, for example "Start cooking". It also overlaps the end of the content, so add bottom padding so the last step never hides behind it.

5. **The section headers are heavy.** The full-width teal bars with white caps compete with the title. Try a lighter treatment, such as colored text with a thin underline, so the title stays the loudest element. Also check white-on-teal contrast. It looks borderline, and you can test it with a contrast checker (aim for 4.5:1).

6. **The title is large and centered while everything else is left-aligned.** Mixing the two looks slightly off. Left-align the title to match the lists, or center more of the content. Also, "With Feta And Fresh Herbs" is over-capitalized. Use sentence case: "Spicy tomato shakshuka with feta and fresh herbs".

7. **The ingredients list is cramped and unclear.** Several items are crammed onto one line ("1 tsp cumin, 1 tsp paprika, chili flakes", "1 onion, 2 garlic cloves"). Give each ingredient its own line, and put the quantity in bold or a separate column so people can scan it while cooking.

8. **The steps are dense.** Add more space between steps, and consider bolding the key times ("10 minutes"). Making each step number a small circle would also help.

## Smaller polish
- The phone frame has a lot of empty space under the steps. That's fine, but the layout will need to scroll properly with longer content.
- Use a single typeface family. The title looks like a different font from the body.
- Keep the left margins identical: the section headers, bullets and steps are slightly misaligned.

## Priority order
1. Real image
2. Visible, larger back and heart buttons
3. Clearer meta row and FAB
4. Lighter section headers
5. One ingredient per line

Fixing just the first three would noticeably improve the screen. If you'd like, I can mock up a revised version or explain how to check contrast.
