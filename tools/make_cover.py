#!/usr/bin/env python3
"""Build the README cover: client message → annotated design → reply draft.

Usage: python3 tools/make_cover.py OVERLAY.png OUT.png
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
from annotate import DEFAULT_ACCENT, HAIRLINE, INK, MUTED, SS, font, hex_rgb  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

W = 1600
PAD = 48
GAP = 48            # space between panels, holds the arrow
SIDE = 336          # width of the message and reply panels
BG = (244, 244, 242)
ACCENT = hex_rgb(DEFAULT_ACCENT)

CLIENT = "Looks clean but too safe… make it pop, and can we add a pricing page?"
REPLY = ("Thanks, glad the clean look works for you! I'll make the headline and the product "
         "screenshot bolder and bring in one confident accent color, so the page pops without "
         "losing its calm. The feature cards stay as they are. The pricing page goes beyond our "
         "one-page brief, so I'll send a separate estimate after this round.")


def wrap(d, text, f, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        test = (line + " " + w).strip()
        if d.textlength(test, font=f) <= width:
            line = test
        else:
            lines.append(line)
            line = w
    lines.append(line)
    return lines


def pill(d, x, y, text, fill):
    f = font("bold", 15 * SS)
    tw = d.textlength(text, font=f) / SS
    d.rounded_rectangle((x * SS, y * SS, (x + tw + 28) * SS, (y + 32) * SS), 16 * SS, fill=fill)
    d.text(((x + 14) * SS, (y + 16) * SS), text, font=f, fill=(255, 255, 255), anchor="lm")


def card(canvas, box, radius=18):
    x0, y0, x1, y1 = box
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0 * SS, (y0 + 6) * SS, x1 * SS, (y1 + 6) * SS),
                                         radius * SS, fill=(0, 0, 0, 28))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10 * SS)))
    ImageDraw.Draw(canvas).rounded_rectangle((x0 * SS, y0 * SS, x1 * SS, y1 * SS), radius * SS,
                                             fill=(255, 255, 255), outline=HAIRLINE, width=SS)


def arrow(d, x, y):
    c = (170, 170, 176)
    d.line([((x - 14) * SS, y * SS), ((x + 12) * SS, y * SS)], fill=c, width=3 * SS)
    d.polygon([((x + 18) * SS, y * SS), ((x + 6) * SS, (y - 9) * SS), ((x + 6) * SS, (y + 9) * SS)], fill=c)


def main(overlay_path, out_path):
    mid_w = W - 2 * PAD - 2 * SIDE - 2 * GAP
    ov = Image.open(overlay_path).convert("RGB")
    ov = ov.resize((mid_w, round(ov.height * mid_w / ov.width)), Image.LANCZOS)
    top = PAD + 56
    H = top + ov.height + PAD
    canvas = Image.new("RGBA", (W * SS, H * SS), BG + (255,))
    d = ImageDraw.Draw(canvas)

    x_left, x_mid = PAD, PAD + SIDE + GAP
    x_right = x_mid + mid_w + GAP
    pill(d, x_left, PAD, "1  Client says", INK)
    pill(d, x_mid, PAD, "2  feedback-decoder", ACCENT)
    pill(d, x_right, PAD, "3  You send", INK)

    # panel 1: chat bubble with a tail
    fm = font("regular", 23 * SS)
    lines = wrap(d, CLIENT, fm, (SIDE - 56) * SS)
    bh = 40 + len(lines) * 33 + 44
    by = top + 60
    card(canvas, (x_left, by, x_left + SIDE, by + bh), 22)
    d = ImageDraw.Draw(canvas)
    d.polygon([((x_left + 34) * SS, (by + bh - 1) * SS), ((x_left + 26) * SS, (by + bh + 22) * SS),
               ((x_left + 62) * SS, (by + bh - 1) * SS)], fill=(255, 255, 255))
    for i, ln in enumerate(lines):
        d.text(((x_left + 28) * SS, (by + 34 + i * 33) * SS), ln, font=fm, fill=INK)
    d.text(((x_left + 28) * SS, (by + bh - 30) * SS), "Client · round 2 of 3",
           font=font("regular", 14 * SS), fill=MUTED)

    # panel 2: annotated design
    card(canvas, (x_mid - 1, top - 1, x_mid + mid_w + 1, top + ov.height + 1), 10)
    canvas.paste(ov.resize((ov.width * SS, ov.height * SS), Image.LANCZOS), (x_mid * SS, top * SS))
    d = ImageDraw.Draw(canvas)

    # panel 3: reply draft excerpt
    fr = font("regular", 18 * SS)
    rlines = wrap(d, REPLY, fr, (SIDE - 56) * SS)
    rh = 64 + len(rlines) * 28 + 92
    ry = top + (ov.height - rh) // 2
    card(canvas, (x_right, ry, x_right + SIDE, ry + rh))
    d = ImageDraw.Draw(canvas)
    d.text(((x_right + 28) * SS, (ry + 34) * SS), "Reply draft · friendly",
           font=font("bold", 15 * SS), fill=ACCENT, anchor="lm")
    for i, ln in enumerate(rlines):
        d.text(((x_right + 28) * SS, (ry + 60 + i * 28) * SS), ln, font=fr, fill=INK)
    tx, ty = x_right + 28, ry + rh - 50
    ft = font("regular", 13 * SS)
    for tag in ("+ firm version", "+ scope note"):
        tw = d.textlength(tag, font=ft) / SS
        d.rounded_rectangle((tx * SS, ty * SS, (tx + tw + 20) * SS, (ty + 28) * SS), 14 * SS,
                            outline=HAIRLINE, width=SS, fill=(250, 250, 249))
        d.text(((tx + 10) * SS, (ty + 14) * SS), tag, font=ft, fill=MUTED, anchor="lm")
        tx += tw + 28

    arrow(d, x_mid - GAP // 2, by + bh // 2)
    arrow(d, x_right - GAP // 2, ry + rh // 2)

    canvas.resize((W, H), Image.LANCZOS).convert("RGB").save(out_path, optimize=True)
    print(f"{out_path}  {W}x{H}px")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
