# Art Prompt Pack — Lesson 1
### Assets needed to replace every Placeholder in the L1 vertical slice

This pack covers **exactly** what Lesson 1 renders today, plus a few optional
extras for the next lessons. Each entry gives: the in-game image name, the file
to produce, size, and ready-to-paste prompts for **Midjourney** and **SDXL**.

> **Style decision (default): soft children's picture-book.**
> Age-appropriate for Grade 1, warm and non-scary. If you'd rather go
> **anime-chibi**, swap the STYLE ANCHOR below and add `--niji 6` in Midjourney
> (or a Pony/Illustrious model in SDXL). Everything else stays the same.

---

## 0. The two anchors (paste these into *every* prompt)

**STYLE ANCHOR** (keeps all images visually consistent):
```
soft children's picture-book illustration, warm gouache-and-watercolor style,
rounded friendly shapes, gentle clean outlines, soft ambient lighting,
cheerful pastel palette, cozy wholesome mood, storybook depth, high detail
```

**NEGATIVE** (SDXL `negative_prompt`; for Midjourney use `--no text,watermark`):
```
text, letters, words, watermark, signature, logo, photorealistic, 3d render,
scary, dark, horror, gore, harsh shadows, deformed, extra limbs, extra fingers,
mutated hands, lowres, blurry, jpeg artifacts, ugly, creepy
```

**CONSISTENCY (read this — it's the whole game):**
- **Midjourney:** generate one clean front-view of each character first, upscale
  it, then in every later prompt add `--cref <image_url> --cw 90` to lock the
  character, and a shared `--sref <style_image_url>` to lock the style.
- **SDXL:** fix a **seed** per character, keep the exact appearance tokens below,
  and for real production train a tiny **LoRA** per character (15–20 images).
  Use the same model checkpoint for every asset.
- Always render characters on a **plain flat background** so they cut out cleanly.

---

## 1. CHARACTER DESIGN BIBLE (fixed — never vary these)

### 明明 Ming Ming — protagonist (shy → brave)
```
a 6-year-old Chinese boy, round soft face, short black hair with one small
cowlick, big dark brown eyes, light blue short-sleeve collared shirt,
navy-blue shorts, white sneakers, small red backpack
```
Personality read: gentle, a little timid. Signature color: blue (#3f7fc1).

### 友友 Youyou — first friend (sunny, loud)
```
a 6-year-old Chinese boy, lively, slightly messy short black hair, big bright
smile, rosy cheeks, orange-yellow t-shirt, green shorts, white sneakers
```
Signature color: orange (#e0962f).

### 小五 Little Five — the magic squirrel guide
```
a small cute cartoon red squirrel, big sparkly eyes, fluffy curled tail,
tiny paws, friendly expression, storybook mascot, holding up its little paws
```
Signature color: brown (#b5703a). Must read as cute, never realistic/rodent-scary.

### (optional, for later lessons)
- **中中 Zhongzhong** — calm boy, neat short black hair, green polo shirt, khaki
  shorts, glasses optional. Color green (#54a85a).
- **老師 Teacher** — warm young Chinese woman, hair in a low bun, soft cardigan,
  holding a picture book, kind smile. Color purple (#9b59b6).

---

## 2. BACKGROUNDS  ·  1920×1080, no characters, no text

Produce at `--ar 16:9`, upscale, export **1920×1080 PNG/JPG**.

### `bg gate` → `game/images/bg_gate.png`
School gate, the lonely first-day mood.
- **MJ:** `STYLE ANCHOR, the front gate of a friendly Chinese elementary school, autumn morning, golden light, a few orange leaves drifting, low brick wall, welcoming entrance, empty foreground, soft focus background --ar 16:9 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, front gate of a cheerful Chinese elementary school, warm autumn morning sunlight, falling orange leaves, brick wall, empty path in foreground, wide establishing shot, no people`

### `bg library` → `game/images/bg_library.png`
Quiet library; one shelf will hold the glowing book.
- **MJ:** `STYLE ANCHOR, a cozy children's school library interior, tall warm wooden bookshelves, soft afternoon light through a window, a reading nook, calm and quiet, one shelf catching a faint magical glow, empty foreground --ar 16:9 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, cozy children's library interior, warm wooden bookshelves full of colorful books, soft window light, quiet magical atmosphere, faint glow on one shelf, no people`

### `bg mountain` → `game/images/bg_mountain.png`
The book-world; also the backdrop of the squirrel counting game (keep the
center-and-lower area uncluttered so squirrels and the big number read clearly).
- **MJ:** `STYLE ANCHOR, a rolling green storybook mountain in daytime, gentle grassy slopes, a winding little path, a few cartoon trees and bushes, bright blue sky with fluffy clouds, cheerful and open, lots of open space in the lower center --ar 16:9 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, rolling green cartoon mountain, sunny day, gentle grassy hill, winding path, scattered round trees and bushes, bright blue sky, fluffy clouds, wide open foreground space, no characters`

### `bg classdoor` → `game/images/bg_classdoor.png`
Classroom doorway, used during 我的朋友在哪裡.
- **MJ:** `STYLE ANCHOR, the open doorway of a warm elementary classroom seen from the hallway, colorful drawings on the wall, soft daylight, inviting, slightly wistful mood, empty hallway foreground --ar 16:9 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, open doorway of a cheerful elementary school classroom viewed from hallway, children's drawings pinned on walls, warm daylight, cubbies, empty foreground, no people`

---

## 3. CHARACTER SPRITES  ·  transparent PNG, full body

Render **on a flat pale background**, then remove it (see §6). Target a tall
canvas (`--ar 2:3`), final height ~**1200 px**, full body with a little headroom.
Front-facing, feet visible, neutral standing unless noted.

### `mingming` (default, shy) → `game/images/mingming.png`
- **MJ:** `STYLE ANCHOR, full body, <明明 design tokens>, standing slightly hunched, shy nervous expression, hands gripping backpack straps, looking down a little, front view, plain pale background --ar 2:3 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, full body character sprite, <明明 design tokens>, shy nervous expression, hands holding backpack straps, standing, front view, plain flat pale-grey background, centered`

### `mingming smile` → `game/images/mingming_smile.png`
(He laughs after the counting game — add this 2nd expression.)
- **MJ:** `STYLE ANCHOR, full body, <明明 design tokens>, happy genuine smile, relaxed confident posture, front view, plain pale background --ar 2:3 --cref <mingming_url> --cw 90 --no text,watermark`
- **SDXL:** *(same tokens, same seed as mingming)* `...happy bright smile, relaxed posture, arms a little open...`

### `youyou` (waving) → `game/images/youyou.png`
- **MJ:** `STYLE ANCHOR, full body, <友友 design tokens>, waving one hand high, big friendly grin, energetic stance, front view, plain pale background --ar 2:3 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, full body character sprite, <友友 design tokens>, waving hand, big grin, energetic, front view, plain flat pale background, centered`

### `wu squirrel` → `game/images/wu_squirrel.png`
- **MJ:** `STYLE ANCHOR, full body, <小五 design tokens>, standing on hind legs, one paw raised pointing, cheerful, front view, plain pale background --ar 2:3 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, cute cartoon red squirrel mascot, <小五 design tokens>, standing on hind legs, pointing with one paw, cheerful, front view, plain flat pale background`

---

## 4. PROPS & GAME ELEMENTS  ·  transparent PNG

### `book` (the glowing 《念一念》) → `game/images/book.png`
- **MJ:** `STYLE ANCHOR, a closed magical storybook standing upright, warm golden glow and tiny sparkles around the edges, ornate friendly cover, no readable text on cover, plain dark background for compositing --ar 2:3 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, a magical glowing storybook, golden light and sparkles, ornate cover, upright, no text, plain black background`

### `squirrel_token` (the tappable squirrel in the counting game) → `game/images/squirrel_token.png`
Reuse 小五's design but a simple, icon-like single pose (~300×300, transparent).
Optionally make **two** files: `squirrel_token.png` (idle) and
`squirrel_token_found.png` (happy/waving) for tap feedback.
- **MJ:** `STYLE ANCHOR, a single cute cartoon red squirrel sitting, simple clean icon, front view, plain background, centered --ar 1:1 --cref <小五_url> --cw 90 --no text,watermark`
- **SDXL:** `STYLE ANCHOR, cute cartoon red squirrel icon, sitting, simple, front view, flat background, centered`

---

## 5. WIRING THE ART INTO THE GAME

1. Put files in `game/images/` with the names above.
2. In `characters.rpy`, **replace the Placeholder lines** with real paths:
   ```renpy
   image bg gate     = "images/bg_gate.png"
   image bg library  = "images/bg_library.png"
   image bg mountain = "images/bg_mountain.png"
   image bg classdoor = "images/bg_classdoor.png"

   image mingming       = "images/mingming.png"
   image mingming smile = "images/mingming_smile.png"
   image youyou         = "images/youyou.png"
   image wu squirrel    = "images/wu_squirrel.png"
   image book           = "images/book.png"
   ```
   *(Tip: a file literally named `game/images/bg gate.png` auto-registers as image
   `bg gate` with no define needed — but explicit lines are clearer to maintain.)*
3. To use the new smile: in `lesson1.rpy`, after the counting game, change
   `show mingming` → `show mingming smile`.
4. For the counting game art, in `mechanics.rpy` swap the placeholder squirrel
   `frame{text "鼠"}` for `add "images/squirrel_token.png"` (idle) /
   `squirrel_token_found.png` (when `i in sq_found`). I can do this edit for you
   once the files exist.

---

## 6. POST-PROCESSING

- **Backgrounds:** just resize to exactly **1920×1080**.
- **Sprite transparency:** if your tool doesn't output alpha, run `rembg`:
  ```bash
  pip install rembg
  rembg i mingming_raw.png mingming.png
  ```
  (Midjourney: add `--no background` helps; or generate on solid magenta and key
  it out.) Trim empty margins; keep feet near the bottom of the canvas.
- **Sprite height:** scale so a standing child is ~80–90% of the 1080 frame
  height; the engine shows them at `at center` / `at right`.

---

## 7. PRIORITY ORDER (if generating incrementally)

1. `bg mountain` + `wu squirrel` + `squirrel_token` → the counting game is the
   showpiece, do it first.
2. `mingming` (shy) + `mingming smile` + `book` → the opening cutscene.
3. `bg gate`, `bg library`, `bg classdoor` → remaining backdrops.
4. `youyou` → the closing hook.

Generate the **whole set with one shared `--sref` / one checkpoint+seed family**
so they look like one book. Lock 明明 and 小五 first — they recur in every lesson.
