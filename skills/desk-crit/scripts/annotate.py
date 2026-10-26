#!/usr/bin/env python3
"""Image helpers for design feedback: prepare, annotate, compare.

  prep    IN OUTDIR [--name design] [--max 1000] [--crop Y0:Y1] [--no-grid]
          Downscale to <=1000px wide. Writes <name>.png and <name>_grid.png
          (100px labelled grid for reading coordinates).
  draw    IN MARKERS.json OUT [--accent #FF2D6F] [--title TEXT] [--no-legend]
          Numbered circular markers, optional boxes, legend strip at the bottom.
          MARKERS.json: [{"n":"1","x":120,"y":80,"w":420,"h":64,"label":"Bolder H1"}]
          x/y = box top-left (or the marked point when w/h are absent), in IN's pixels.
          Numbers = changes/issues (filled accent); letters = keep / what works (outlined).
          "kind":"scope" = out-of-scope request (amber). "type":"gap" with x,y,h = vertical
          dimension arrow for spacing (no box).
  compare BEFORE AFTER OUT [--labels Before After]
          One side-by-side image for version-to-version progress.

Requires Pillow (`pip install Pillow`).
"""
import argparse
import json
import os
import re
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageStat
except ImportError:
    sys.exit("Pillow is missing. Install it with: pip install Pillow")

MAX_WIDTH = 1000          # keeps vision token cost low while text stays legible
TALL_WARNING = 2400       # taller images cost many tokens; suggest --crop
SS = 2                    # supersampling factor for anti-aliased shapes
BLANK_STDDEV = 10         # luminance spread below this = empty background
BOX_PAD = 6               # breathing room between a box and the element it frames
DEFAULT_ACCENT = "#FF2D6F"  # hot pink: rare in UI palettes, so markers never blend in
SCOPE_COLOR = (224, 138, 0)  # amber for out-of-scope requests
INK = (24, 24, 27)
MUTED = (113, 113, 122)
STRIP_BG = (250, 250, 249)
HAIRLINE = (228, 228, 231)

FONT_CANDIDATES = {
    "bold": [
        ("~/Library/Fonts/Inter-SemiBold.otf", 0), ("/Library/Fonts/Inter-SemiBold.otf", 0),
        ("/usr/share/fonts/truetype/inter/Inter-SemiBold.ttf", 0),
        ("/System/Library/Fonts/HelveticaNeue.ttc", 1), ("/System/Library/Fonts/Helvetica.ttc", 1),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 0),
        ("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 0),
        ("C:/Windows/Fonts/segoeuib.ttf", 0), ("C:/Windows/Fonts/arialbd.ttf", 0),
    ],
    "regular": [
        ("~/Library/Fonts/Inter-Medium.otf", 0), ("/Library/Fonts/Inter-Medium.otf", 0),
        ("/usr/share/fonts/truetype/inter/Inter-Medium.ttf", 0),
        ("/System/Library/Fonts/HelveticaNeue.ttc", 0), ("/System/Library/Fonts/Helvetica.ttc", 0),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 0),
        ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 0),
        ("C:/Windows/Fonts/segoeui.ttf", 0), ("C:/Windows/Fonts/arial.ttf", 0),
    ],
}
_font_cache = {}


def font(weight, size):
    key = (weight, size)
    if key in _font_cache:
        return _font_cache[key]
    for path, index in FONT_CANDIDATES[weight]:
        path = os.path.expanduser(path)
        if os.path.exists(path):
            try:
                f = ImageFont.truetype(path, size, index=index)
                break
            except OSError:
                continue
    else:
        try:
            f = ImageFont.load_default(size=size)  # Pillow >= 10.1
        except TypeError:
            f = ImageFont.load_default()
    _font_cache[key] = f
    return f


def hex_rgb(value):
    value = value.lstrip("#")
    if len(value) != 6:
        sys.exit(f"Accent must be a 6-digit hex color, got #{value}")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def load(path):
    if not os.path.exists(path):
        sys.exit(f"Image not found: {path}")
    img = Image.open(path)
    img.load()
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[-1])
        return bg
    return img.convert("RGB")


def fit_width(img, max_w):
    if img.width <= max_w:
        return img
    h = round(img.height * max_w / img.width)
    return img.resize((max_w, h), Image.LANCZOS)


# ---------------------------------------------------------------- prep

def cmd_prep(a):
    img = load(a.input)
    if a.crop:
        try:
            y0, y1 = (int(v) for v in a.crop.split(":"))
        except ValueError:
            sys.exit("--crop expects Y0:Y1 in source pixels, e.g. --crop 0:1800")
        img = img.crop((0, max(0, y0), img.width, min(img.height, y1)))
    img = fit_width(img, a.max)
    os.makedirs(a.outdir, exist_ok=True)
    out = os.path.join(a.outdir, f"{a.name}.png")
    img.save(out, optimize=True)
    if a.no_grid:
        print(f"{out}  {img.width}x{img.height}px")
        return

    grid = img.convert("RGBA")
    layer = Image.new("RGBA", grid.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    f = font("regular", 11)
    line = (0, 150, 255, 90)
    for x in range(100, grid.width, 100):
        d.line([(x, 0), (x, grid.height)], fill=line, width=1)
    for y in range(100, grid.height, 100):
        d.line([(0, y), (grid.width, y)], fill=line, width=1)
    for x in range(100, grid.width, 100):
        for y in range(0, grid.height, 500):
            _grid_tag(d, (x + 2, y + 2), str(x), f)
    for y in range(100, grid.height, 100):
        for x in range(0, grid.width, 500):
            _grid_tag(d, (x + 2, y + 2), str(y), f)
    Image.alpha_composite(grid, layer).convert("RGB").save(
        os.path.join(a.outdir, f"{a.name}_grid.png"), optimize=True)
    print(f"{out}  {img.width}x{img.height}px  (grid: {a.name}_grid.png, lines every 100px)")
    if img.height > TALL_WARNING:
        print(f"Note: {img.height}px tall. For detail, prep sections separately with --crop Y0:Y1.")


def _grid_tag(d, xy, text, f):
    l, t, r, b = d.textbbox(xy, text, font=f)
    d.rectangle((l - 2, t - 1, r + 2, b + 1), fill=(0, 120, 255, 200))
    d.text(xy, text, font=f, fill=(255, 255, 255, 255))


# ---------------------------------------------------------------- draw

def cmd_draw(a):
    base = load(a.input)
    if base.width > MAX_WIDTH:
        sys.exit(f"{a.input} is {base.width}px wide. Run `prep` first so coordinates match.")
    try:
        with open(a.markers, encoding="utf-8") as fh:
            markers = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Cannot read markers JSON: {e}")
    if not isinstance(markers, list) or not markers:
        sys.exit("Markers JSON must be a non-empty list of objects.")
    for i, m in enumerate(markers):
        if "x" not in m or "y" not in m or "n" not in m:
            sys.exit(f"Marker {i} needs n, x, y. Got: {m}")
        m["n"] = str(m["n"])

    accent = hex_rgb(a.accent)
    W, H = base.width, base.height
    for m in markers:
        # out-of-scope items get the second color so they read as "not this round"
        m["_color"] = SCOPE_COLOR if m.get("kind") == "scope" else accent
    canvas = base.resize((W * SS, H * SS), Image.LANCZOS).convert("RGBA")

    # boxes: outline only (a tint would distort the colors being critiqued)
    rects = []
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    for m in markers:
        if m.get("type") == "gap":
            _gap_arrow(ld, m, m["_color"])
            continue
        if m.get("w") and m.get("h"):
            # pad so the stroke never touches the element; keep it inside the image
            x0, y0 = max(m["x"] - BOX_PAD, 3), max(m["y"] - BOX_PAD, 3)
            x1 = min(m["x"] + m["w"] + BOX_PAD, W - 3)
            y1 = min(m["y"] + m["h"] + BOX_PAD, H - 3)
            rects.append((x0, y0, x1, y1))
            m["_rect"] = (x0, y0, x1, y1)
            r = 6 * SS
            ld.rounded_rectangle((x0 * SS, y0 * SS, x1 * SS, y1 * SS), r,
                                 outline=(255, 255, 255, 230), width=5 * SS)
            ld.rounded_rectangle(((x0 + 1) * SS, (y0 + 1) * SS, (x1 - 1) * SS, (y1 - 1) * SS), r,
                                 outline=m["_color"] + (255,), width=2 * SS)
    canvas = Image.alpha_composite(canvas, layer)

    # markers sit outside their box, never on content: try above, left, right, below
    radius = 15
    placed = []
    gray = base.convert("L")
    for m in markers:
        m["_c"] = _place(m, rects, placed, radius, W, H, gray)
        placed.append(m["_c"])

    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    for m in markers:
        cx, cy = m["_c"]
        rr = (radius + 3) * SS
        sd.ellipse((cx * SS - rr, cy * SS - rr + 2 * SS, cx * SS + rr, cy * SS + rr + 2 * SS),
                   fill=(0, 0, 0, 70))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(3 * SS)))

    d = ImageDraw.Draw(canvas)
    for m in markers:
        _marker(d, m["_c"][0] * SS, m["_c"][1] * SS, radius * SS, m["n"], m["_color"], SS)

    out = canvas.resize((W, H), Image.LANCZOS).convert("RGB")
    if not a.no_legend:
        out = _with_legend(out, markers, a.title)
    out.save(a.output, optimize=True)
    print(f"{a.output}  {out.width}x{out.height}px, {len(markers)} markers")


def _gap_arrow(d, m, color):
    """Vertical dimension arrow for spacing notes: x, y = top end, h = length."""
    x, y0, y1 = m["x"] * SS, m["y"] * SS, (m["y"] + m["h"]) * SS
    head, tick = 9 * SS, 12 * SS
    for width, fill in ((6 * SS, (255, 255, 255, 230)), (2 * SS, color + (255,))):
        d.line([(x, y0 + SS), (x, y1 - SS)], fill=fill, width=width)
        for yy in (y0, y1):
            d.line([(x - tick, yy), (x + tick, yy)], fill=fill, width=width)
    for yy, s in ((y0, 1), (y1, -1)):
        d.polygon([(x, yy + s * 2 * SS), (x - head * 0.6, yy + s * head * 1.3),
                   (x + head * 0.6, yy + s * head * 1.3)], fill=color + (255,))
    m["_rect"] = (m["x"] - 14, m["y"], m["x"] + 14, m["y"] + m["h"])


def _blank(gray, cx, cy, r):
    """True when the spot is plain background, so a marker there hides no content."""
    box = (int(cx - r - 3), int(cy - r - 3), int(cx + r + 3), int(cy + r + 3))
    return ImageStat.Stat(gray.crop(box)).stddev[0] < BLANK_STDDEV


def _place(m, rects, placed, r, W, H, gray):
    gap = 6
    if m.get("type") == "gap":
        x0, y0, x1, y1 = m["_rect"]
        mid = (y0 + y1) / 2
        cands = [(x1 + r + gap, mid), (x0 - r - gap, mid)]
    elif "_rect" in m:
        x0, y0, x1, y1 = m["_rect"]
        cands = [(x0 + r, y0 - r - gap), (x0 - r - gap, y0 + r), (x0 + r, y1 + r + gap),
                 (x1 + r + gap, y0 + r), (x1 - r, y0 - r - gap), (x1 - r, y1 + r + gap),
                 (x0 - r - gap, y1 - r), (x1 + r + gap, y1 - r)]
    else:
        cands = [(m["x"], m["y"])]

    def ok(cx, cy):
        if not (r + 3 <= cx <= W - r - 3 and r + 3 <= cy <= H - r - 3):
            return False
        if any((cx - px) ** 2 + (cy - py) ** 2 < (2 * r + 4) ** 2 for px, py in placed):
            return False
        # must not sit inside any framed element
        return not any(bx0 - r < cx < bx1 + r and by0 - r < cy < by1 + r
                       for bx0, by0, bx1, by1 in rects)

    for cx, cy in cands:  # best: free of boxes and markers, on empty background
        if ok(cx, cy) and _blank(gray, cx, cy, r):
            return cx, cy
    for cx, cy in cands:
        if ok(cx, cy):
            return cx, cy
    cx, cy = cands[0]  # crowded: clamp the first choice and nudge sideways
    cx = min(max(cx, r + 3), W - r - 3)
    cy = min(max(cy, r + 3), H - r - 3)
    for _ in range(20):
        if all((cx - px) ** 2 + (cy - py) ** 2 >= (2 * r + 4) ** 2 for px, py in placed):
            break
        cx = min(cx + 2 * r + 4, W - r - 3)
    return cx, cy


EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D]")


def clean_label(text):
    # label fonts have no emoji glyphs; drop them instead of drawing tofu boxes
    return re.sub(r"\s+", " ", EMOJI.sub("", text)).strip(" ,;:-") or "—"


def _is_keep(label):
    return label.isalpha()


def _marker(d, cx, cy, r, label, accent, scale):
    ring = 3 * scale
    d.ellipse((cx - r - ring, cy - r - ring, cx + r + ring, cy + r + ring), fill=(255, 255, 255))
    if _is_keep(label):
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255),
                  outline=accent, width=round(2.5 * scale))
        color = accent
    else:
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=accent)
        color = (255, 255, 255)
    size = round(r * (1.0 if len(label) == 1 else 0.8))
    f = font("bold", size)
    d.text((cx, cy + scale * 0.5), label, font=f, fill=color, anchor="mm")


def _with_legend(img, markers, title):
    pad, gap, r = 20, 22, 11
    f = font("regular", 14)
    tf = font("bold", 13)
    probe = ImageDraw.Draw(img)
    items, seen = [], set()
    for m in markers:
        if m["n"] in seen:  # one marker number may point at several places; list it once
            continue
        seen.add(m["n"])
        text = clean_label(str(m.get("label", "")))
        if m.get("kind") == "scope" and "scope" not in text.lower():
            text += " · out of scope"
        tw = probe.textlength(text, font=f)
        items.append((m["n"], text, 2 * r + 8 + tw, m["_color"]))

    rows, row, x = [], [], pad
    title_w = probe.textlength(title, font=tf) + gap if title else 0
    x += title_w
    for it in items:
        if row and x + it[2] > img.width - pad:
            rows.append(row)
            row, x = [], pad
        row.append(it)
        x += it[2] + gap
    rows.append(row)

    row_h = 32
    strip_h = pad * 2 + row_h * len(rows) - (row_h - 2 * r - 6)
    out = Image.new("RGB", (img.width, img.height + strip_h), STRIP_BG)
    out.paste(img, (0, 0))
    big = out.crop((0, img.height, img.width, out.height)).resize(
        (img.width * SS, strip_h * SS), Image.LANCZOS)
    d = ImageDraw.Draw(big)
    d.line([(0, 0), (big.width, 0)], fill=HAIRLINE, width=SS)
    fs = font("regular", 14 * SS)
    tfs = font("bold", 13 * SS)
    y = pad + r + 3
    for i, row in enumerate(rows):
        x = pad
        if i == 0 and title:
            d.text((x * SS, y * SS), title, font=tfs, fill=MUTED, anchor="lm")
            x += title_w
        for n, text, w, color in row:
            _marker(d, (x + r) * SS, y * SS, r * SS, n, color, SS * 0.75)
            d.text(((x + 2 * r + 8) * SS, y * SS), text, font=fs, fill=INK, anchor="lm")
            x += w + gap
        y += row_h
    strip = big.resize((img.width, strip_h), Image.LANCZOS)
    out.paste(strip, (0, img.height))
    return out


# ---------------------------------------------------------------- compare

def cmd_compare(a):
    left, right = load(a.before), load(a.after)
    pad, gap, label_h = 24, 24, 44
    panel_w = (MAX_WIDTH - 2 * pad - gap) // 2
    left, right = (im.resize((panel_w, round(im.height * panel_w / im.width)), Image.LANCZOS)
                   for im in (left, right))
    h = max(left.height, right.height)
    W = pad * 2 + gap + panel_w * 2
    H = pad + label_h + h + pad
    out = Image.new("RGB", (W * SS, H * SS), (244, 244, 242))
    d = ImageDraw.Draw(out)
    f = font("bold", 14 * SS)
    for i, (im, text) in enumerate(((left, a.labels[0]), (right, a.labels[1]))):
        x = pad + i * (panel_w + gap)
        tw = d.textlength(text, font=f) / SS
        fill = INK if i == 0 else hex_rgb(a.accent)
        d.rounded_rectangle(((x) * SS, pad * SS, (x + tw + 24) * SS, (pad + 28) * SS),
                            14 * SS, fill=fill)
        d.text(((x + 12) * SS, (pad + 14) * SS), text, font=f, fill=(255, 255, 255), anchor="lm")
        d.rounded_rectangle(((x - 1) * SS, (pad + label_h - 1) * SS,
                             (x + panel_w + 1) * SS, (pad + label_h + im.height + 1) * SS),
                            4 * SS, outline=HAIRLINE, width=SS)
    out = out.resize((W, H), Image.LANCZOS)
    out.paste(left, (pad, pad + label_h))
    out.paste(right, (pad + panel_w + gap, pad + label_h))
    out.save(a.output, optimize=True)
    print(f"{a.output}  {W}x{H}px")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("prep")
    s.add_argument("input"); s.add_argument("outdir")
    s.add_argument("--name", default="design")
    s.add_argument("--max", type=int, default=MAX_WIDTH)
    s.add_argument("--crop")
    s.add_argument("--no-grid", action="store_true", help="skip the grid copy (e.g. when archiving a version)")
    s.set_defaults(fn=cmd_prep)

    s = sub.add_parser("draw")
    s.add_argument("input"); s.add_argument("markers"); s.add_argument("output")
    s.add_argument("--accent", default=DEFAULT_ACCENT)
    s.add_argument("--title", default="")
    s.add_argument("--no-legend", action="store_true")
    s.set_defaults(fn=cmd_draw)

    s = sub.add_parser("compare")
    s.add_argument("before"); s.add_argument("after"); s.add_argument("output")
    s.add_argument("--labels", nargs=2, default=["Before", "After"])
    s.add_argument("--accent", default=DEFAULT_ACCENT)
    s.set_defaults(fn=cmd_compare)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
