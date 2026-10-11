# Art — Grade 1, Lesson 2 (一棵樹上十樣果 + 握握手)

The game already runs with placeholders for every image below. Put a file at its
path and it replaces the placeholder (no code change).

- Settings, positive prefix, negative prompt, upscale, and transparency:
  `Design/shared/comfyui_generation_guide.md` (same as Lesson 1).
- Character looks: `Design/shared/character_bible.md`.
- Keep each original and its workflow `.json` in `ArtSource/`: 中中 (and the 友友
  pose) in `ArtSource/shared/`, backgrounds and fruits in `ArtSource/grade1/`.
  Make the folder if it does not exist yet.

## Every prompt = shared block + the image's own words

**Do not skip this.** Without the prefix and the shared negative, the image comes out
in a different style from 明明 and 友友 (thick ink lines, hard flat colors).

- **POSITIVE** = this prefix, then the image's POSITIVE below:
  ```
  masterpiece, best quality, very aesthetic, absurdres, storybook illustration,
  children's picture book style, soft gouache and watercolor texture,
  soft cel shading, warm pastel palette, gentle soft lighting, clean rounded shapes,
  ```
- **NEGATIVE** = this list, then the image's ADD TO NEGATIVE below:
  ```
  lowres, worst quality, low quality, bad anatomy, bad hands, missing fingers,
  extra digits, fewer digits, jpeg artifacts, signature, watermark, username, text,
  blurry, ugly, deformed, mutated, photorealistic, 3d, realistic, harsh shadows,
  scary, horror, grimdark, nsfw, suggestive, monochrome, greyscale
  ```

## What to make

| # | File | Kind | Size in game | Priority |
|---|---|---|---|---|
| 1 | `Huafu/game/images/chars/zhongzhong.png` | sprite (transparent) | ~900px tall | **first** — new character, recurs all year |
| 2 | `Huafu/game/images/grade1/bg/bg_classroom.png` | background | 1920×1080 | high — used in L2, L3, L4 |
| 3 | `Huafu/game/images/grade1/bg/bg_fruit_tree.png` | background | 1920×1080 | high |
| 4–13 | `Huafu/game/images/grade1/props/fruit_<name>.png` (10 files) | icons (transparent) | 140×140 | high |
| 14 | `Huafu/game/images/chars/youyou_handshake.png` | sprite (optional) | ~900px tall | later |

Fruit file names, in chant order: `fruit_apple` 蘋果, `fruit_banana` 香蕉,
`fruit_grapes` 葡萄, `fruit_tangerine` 橘子, `fruit_tomato` 番茄, `fruit_peach` 桃子,
`fruit_apricot` 杏子, `fruit_papaya` 木瓜, `fruit_plum` 李子, `fruit_pear` 梨.

---

## 1 — `zhongzhong.png` (中中, calm and clever — lock this design)

Batch B settings (832×1216, transparent). Seed **1083328916370374** (fixed; also in
`character_bible.md`) — reuse it for his later poses.
Then copy the final tokens into `character_bible.md` and move him to "approved art".

Full prompts, ready to paste:

**POSITIVE:**
```
masterpiece, best quality, very aesthetic, absurdres, storybook illustration,
children's picture book style, soft gouache and watercolor texture,
soft cel shading, warm pastel palette, gentle soft lighting, clean rounded shapes,
1boy, solo, child, 6 years old, calm gentle face, neat short straight black hair
with a tidy side part, round black glasses, small thoughtful smile, green polo
shirt, khaki shorts, white sneakers, hands holding a small sketchbook in front,
relaxed quiet posture, full body, standing, looking at viewer, simple background,
white background
```
**NEGATIVE:**
```
lowres, worst quality, low quality, bad anatomy, bad hands, missing fingers,
extra digits, fewer digits, jpeg artifacts, signature, watermark, username, text,
blurry, ugly, deformed, mutated, photorealistic, 3d, realistic, harsh shadows,
scary, horror, grimdark, nsfw, suggestive, monochrome, greyscale,
cropped, out of frame, multiple views, messy hair, orange shirt, logo, emblem
```

Check: he must not look like 友友 (messy hair, orange shirt) or 明明 (cowlick, blue
shirt, red backpack). Green shirt + glasses + sketchbook = 中中. He must match their
**style** too: soft watercolor color and thin lines, not thick ink outlines.

---

## 2 — `bg_classroom.png` (real classroom, snack time)

Batch A settings (1344×768 → 1920×1080). Characters stand in the centre and the
text box covers the bottom quarter, so keep the centre plain.

**POSITIVE:**
```
cozy elementary school classroom interior, small wooden desks and chairs, a green
chalkboard, colorful children's drawings on the walls, a window with soft autumn
daylight, a few lunch boxes and snack bags on the desks, warm and friendly,
uncluttered open space in the center, scenery, no humans
```

---

## 3 — `bg_fruit_tree.png` (book world: one tree, ten kinds of fruit)

Batch A settings. This is a **book world** (brighter, storybook fantasy). The ten
fruit icons fall onto the grass in two rows (y = 45–75% of the height), and the
title and big number are at the top centre — keep both areas calm.

**POSITIVE:**
```
one big magical storybook fruit tree on a grassy hill, its wide round leafy crown
hung with many different fruits (apples, bananas, grapes, oranges, tomatoes,
peaches, pears), bright cheerful sunny day, soft blue sky, a wide flat open grassy
meadow in the lower half, paper texture, whimsical fantasy picture book, scenery,
no humans
```
**ADD TO NEGATIVE:** `fruit on the ground, basket, text`

Tip: if the crown fills the whole frame, add `tree on the upper half of the image`.

---

## 4–13 — the ten fruit icons

Batch B settings, but generate at **768×768** (like the squirrel token). One fruit
per image, the same style for all ten (same seed, change only the fruit words).

**POSITIVE template** — replace `<FRUIT>`:
```
a single cute cartoon <FRUIT>, storybook icon, simple clean shape, bold soft
outline, glossy highlight, front view, centered, simple background, white
background, no humans
```
**ADD TO NEGATIVE:** `multiple fruits, basket, plate, knife, cut, sliced, text`

| File | `<FRUIT>` |
|---|---|
| `fruit_apple` | `red apple with one green leaf` |
| `fruit_banana` | `bunch of three yellow bananas` |
| `fruit_grapes` | `bunch of purple grapes` |
| `fruit_tangerine` | `orange tangerine with a small leaf` |
| `fruit_tomato` | `red tomato with a green stem` |
| `fruit_peach` | `pink peach with a leaf` |
| `fruit_apricot` | `small orange-yellow apricot` |
| `fruit_papaya` | `whole yellow-orange papaya` |
| `fruit_plum` | `dark purple plum` |
| `fruit_pear` | `light green pear` |

Check: the ten must be easy to tell apart at 140px. Tomato vs apple and apricot vs
tangerine are the risky pairs — keep the stem and the leaf different.

After: trim the empty margin so each fruit fills its square.

---

## 14 — `youyou_handshake.png` (optional, later)

Now the handshake scene moves 明明 and 友友 together with their normal sprites.
A pose with 友友's hand held out would read better. Reuse 友友's seed.

**POSITIVE:**
```
1boy, solo, child, 6 years old, lively, messy short black hair, big open friendly
smile, rosy cheeks, orange t-shirt, green shorts, white sneakers, holding one hand
out forward for a handshake, side three-quarter view facing left, full body,
standing, simple background, white background
```
Tell me when it exists, and I will use it in the handshake scene.

---

## Optional sound effects

The game plays these if the files exist (`Huafu/game/audio/sfx/`); see
`Design/shared/audio_generation_guide.md`.

| Base name | Plays when | Search terms |
|---|---|---|
| `sfx_rustle` | shaking the fruit tree | "leaves rustle", "bush shake" |
| `sfx_try_again` | a wrong pick in the 握握手 game | "soft boop", "gentle wrong", "cartoon bonk" (soft, not harsh) |
