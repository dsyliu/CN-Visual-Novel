"""Make the web loading picture (Huafu/web-presplash.jpg) from the game's art.

The web build shows this picture while the game downloads (the Ren'Py web
build picks up web-presplash.* from the project folder). It shows the library
background, the glowing book 《念一念》, and the game title.

Usage:  python tools/make_presplash.py
Needs:  pip install pillow
"""

import pathlib

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = ROOT / "Huafu" / "game" / "images"
FONTS = ROOT / "tools" / "fonts"
OUT = ROOT / "Huafu" / "web-presplash.jpg"

W, H = 1280, 720
TITLE = "華府中文學校"
SUBTITLE = "載入中…  Loading…"


def cover(img, w, h):
    """Scale and centre-crop img to fill w x h."""
    scale = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left, top = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((left, top, left + w, top + h))


def text_centered(draw, y, text, font, fill):
    """Draw text centred on x, with a soft dark outline so it reads on any art."""
    width = draw.textlength(text, font=font)
    draw.text(((W - width) / 2, y), text, font=font, fill=fill,
              stroke_width=max(2, font.size // 18), stroke_fill=(40, 25, 10))


def main():
    # Background: the library, slightly blurred and darkened so the book stands out.
    bg = cover(Image.open(IMAGES / "grade1" / "bg" / "bg_library.png").convert("RGB"), W, H)
    bg = bg.filter(ImageFilter.GaussianBlur(3))
    bg = ImageEnhance.Brightness(bg).enhance(0.7)

    # Warm glow behind the book.
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((W / 2 - 260, H / 2 - 230, W / 2 + 260, H / 2 + 290), fill=200)
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    bg = Image.composite(Image.new("RGB", (W, H), (255, 214, 120)), bg, glow)

    # The glowing book 《念一念》, centred.
    book = Image.open(IMAGES / "props" / "book.png").convert("RGBA")
    bh = 400
    book = book.resize((round(book.width * bh / book.height), bh), Image.LANCZOS)
    bg = bg.convert("RGBA")
    bg.alpha_composite(book, ((W - book.width) // 2, (H - bh) // 2 + 30))

    draw = ImageDraw.Draw(bg)
    text_centered(draw, 40, TITLE, ImageFont.truetype(str(FONTS / "NotoSansTC-Bold.otf"), 76), (255, 230, 160))
    text_centered(draw, H - 85, SUBTITLE, ImageFont.truetype(str(FONTS / "NotoSansTC-Regular.otf"), 34), (255, 248, 232))

    bg.convert("RGB").save(OUT, quality=85, optimize=True)
    print(f"{OUT.relative_to(ROOT)}: {OUT.stat().st_size / 1e3:.0f} KB")


if __name__ == "__main__":
    main()
