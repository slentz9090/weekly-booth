"""Link preview cards, 1200x630.

Built from the same constants the pages use, so a preview can never contradict
the page it links to. Change an award here and on the page or not at all.
"""
import os

from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "og")
FONTS = "/usr/share/fonts/truetype/dejavu"
COND_B = os.path.join(FONTS, "DejaVuSansCondensed-Bold.ttf")
SANS = os.path.join(FONTS, "DejaVuSans.ttf")
SANS_B = os.path.join(FONTS, "DejaVuSans-Bold.ttf")

BG = "#0b0e13"
PANEL = "#171d27"
GOLD = "#ffcf7a"
BLUE = "#8fbcff"
TX = "#e6eaf0"
MUT = "#9aa4b2"

CARDS = {
    "dlffl-week-3.png": {
        "league": "Dewart Lake FFL",
        "week": "Week 3 · 2026",
        "accent": GOLD,
        "headline": "Scott Howard Has Played Doug Fields 13 Times And Lost All 13",
        "owner": "Owner of the Week · Scott Reisert, 160.76",
        "worst": "Worst Owner · Casey Couture, 76.18",
    },
    "foh-week-3.png": {
        "league": "Friends of Herb",
        "week": "Week 3 · 2026",
        "accent": BLUE,
        "headline": "Matt Davis Asked A Robot Who To Start And Lost By 0.76",
        "owner": "Owner of the Week · Michael Turner, 138.24",
        "worst": "Worst Owner · Ryan Kelly, 54.52",
    },
}


def wrap(draw, text, font, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        t = (line + " " + w).strip()
        if draw.textlength(t, font=font) <= width:
            line = t
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def card(name, spec):
    im = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 1200, 8], fill=spec["accent"])
    d.rectangle([64, 470, 1136, 566], fill=PANEL)

    f_kicker = ImageFont.truetype(SANS_B, 26)
    f_league = ImageFont.truetype(COND_B, 46)
    f_head = ImageFont.truetype(COND_B, 74)
    f_small = ImageFont.truetype(SANS, 25)

    d.text((64, 62), "THE WEEKLY BOOTH", font=f_kicker, fill=MUT)
    d.text((64, 104), spec["league"], font=f_league, fill="#ffffff")
    wk_w = d.textlength(spec["week"], font=f_kicker)
    d.text((1136 - wk_w, 70), spec["week"], font=f_kicker, fill=spec["accent"])

    lines = wrap(d, spec["headline"], f_head, 1072)
    y = 196
    for ln in lines[:4]:
        d.text((64, y), ln, font=f_head, fill=TX)
        y += 84

    d.text((88, 486), spec["owner"], font=f_small, fill=spec["accent"])
    d.text((88, 524), spec["worst"], font=f_small, fill=MUT)
    d.text((64, 588), "Gil Prather and Boomer Latour · slentz9090.github.io/weekly-booth",
           font=ImageFont.truetype(SANS, 22), fill=MUT)

    path = os.path.join(OUT, name)
    im.save(path, "PNG", optimize=True)
    print("wrote", path, os.path.getsize(path), "bytes,", len(lines), "headline lines")


if __name__ == "__main__":
    for n, s in CARDS.items():
        card(n, s)
