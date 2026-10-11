"""Make the game's fonts small enough for the web build.

The full Noto Sans TC fonts (tools/fonts/, ~16 MB each) also hold Simplified
Chinese, Japanese, and Korean glyphs the game never uses. This keeps:
  - the 5,401 common Traditional Chinese characters (Big5 level 1, 常用字)
    + bopomofo and Big5 symbols
  - Latin letters incl. pinyin tone marks, punctuation, arrows, simple symbols
  - every character that appears in the game's .rpy files
and writes the result to Huafu/game/fonts/ (~4 MB each).

Run again after adding a rare character to the scripts (one outside Big5
level 1); otherwise the game shows an empty box for it. tools/deploy_web.sh runs
this script before every web build.

Usage:  python tools/subset_fonts.py
Needs:  pip install fonttools
"""

import pathlib

from fontTools import subset

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "fonts"
DST = ROOT / "Huafu" / "game" / "fonts"
FONTS = ["NotoSansTC-Regular.otf", "NotoSansTC-Bold.otf"]

RANGES = [
    (0x0020, 0x007E),  # ASCII
    (0x00A0, 0x024F),  # Latin-1 + Latin Extended-A/B (pinyin: à ǐ ǚ …)
    (0x2000, 0x206F),  # general punctuation (— … ‘ ’ “ ”)
    (0x2190, 0x21FF),  # arrows (→)
    (0x25A0, 0x25FF),  # geometric shapes
    (0x2600, 0x26FF),  # misc symbols (★)
    (0x2700, 0x27BF),  # dingbats (✓)
    (0x3000, 0x303F),  # CJK punctuation (、。「」《》)
    (0x3100, 0x312F),  # bopomofo (注音)
    (0xFF00, 0xFFEF),  # full-width forms (，！？～)
]


def big5_common_chars():
    """Big5 symbols (A140–A3BF) + level-1 common hanzi (A440–C67E)."""
    chars = set()
    for lead in range(0xA1, 0xC7):
        trails = list(range(0x40, 0x7F))
        if lead != 0xC6:
            trails += list(range(0xA1, 0xFF))
        for trail in trails:
            try:
                chars.add(bytes([lead, trail]).decode("big5"))
            except UnicodeDecodeError:
                pass
    return chars


def script_chars():
    """Every character used in the game's scripts."""
    chars = set()
    for path in (ROOT / "Huafu" / "game").rglob("*.rpy"):
        chars.update(path.read_text(encoding="utf-8"))
    return {c for c in chars if c.isprintable()}


def main():
    chars = big5_common_chars() | script_chars()
    for lo, hi in RANGES:
        chars.update(chr(cp) for cp in range(lo, hi + 1))
    unicodes = sorted(ord(c) for c in chars)

    DST.mkdir(parents=True, exist_ok=True)
    for name in FONTS:
        options = subset.Options()
        options.layout_features = ["*"]
        options.name_IDs = ["*"]
        options.notdef_outline = True
        font = subset.load_font(str(SRC / name), options)
        subsetter = subset.Subsetter(options)
        subsetter.populate(unicodes=unicodes)
        subsetter.subset(font)
        out = DST / name
        subset.save_font(font, str(out), options)
        print(f"{name}: {(SRC / name).stat().st_size / 1e6:.1f} MB -> {out.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
