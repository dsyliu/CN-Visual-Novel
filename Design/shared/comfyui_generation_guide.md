# ComfyUI Generation Guide — Lesson 1 (SDXL)

Generate in two batches because they use two different workflows:
- **Batch A — Backgrounds** (4 images, opaque, 16:9)
- **Batch B — Sprites & props** (6 images, transparent PNG)

Work top-to-bottom within each batch.

> Character looks (appearance tokens, signature colors, designs for 中中 and 老師)
> are in `character_bible.md`. Keep sprite prompts consistent with it.

---

## GLOBAL SETTINGS (same for every image unless noted)

| Setting | Value |
|---|---|
| Checkpoint | An **SDXL illustration** model — Illustrious-XL or NoobAI-XL (anime/storybook). |
| Style LoRA | *(Strongly recommended)* one "storybook / picture-book" SDXL LoRA, weight 0.6–0.8, on **every** image — this is what unifies the look. |
| VAE | sdxl_vae (or checkpoint-baked) |
| Sampler | `euler_ancestral` (Euler a) |
| Scheduler | `normal` |
| Steps | 28 |
| CFG | 5.0 |
| CLIP skip | 2  (Illustrious/NoobAI like clip skip 2) |
| Seed | **Fix one seed per character** (so re-rolls stay on-model). Backgrounds can be random. |

> **If you use a Pony-based checkpoint instead:** CFG 7, and prepend
> `score_9, score_8_up, score_7_up,` to every positive prompt.

**Resolution & upscale (avoid native 1920×1080 — SDXL clones at that size):**
- Backgrounds: generate **1344×768**, then Hires-fix/upscale ×1.43 → **1920×1080**
  (upscaler `4x-UltraSharp`, denoise 0.35).
- Sprites: generate **832×1216**, upscale ×1.5 → ~1248×1824, then trim/resize.

**Transparency (Batch B only):** add the **LayerDiffuse** node set to
*"Only Generate Transparent Image (Attn Injection)"* (needs the SDXL LayerDiffuse
model). No LayerDiffuse? Generate on `white background` and run `rembg` after.

---

## SHARED PROMPT BLOCKS (paste into every image)

**POSITIVE PREFIX** (goes first, before the per-image subject):
```
masterpiece, best quality, very aesthetic, absurdres, storybook illustration,
children's picture book style, soft gouache and watercolor texture,
soft cel shading, warm pastel palette, gentle soft lighting, clean rounded shapes,
```

**NEGATIVE** (use on every image):
```
lowres, worst quality, low quality, bad anatomy, bad hands, missing fingers,
extra digits, fewer digits, jpeg artifacts, signature, watermark, username, text,
blurry, ugly, deformed, mutated, photorealistic, 3d, realistic, harsh shadows,
scary, horror, grimdark, nsfw, suggestive, monochrome, greyscale
```

---

# BATCH A — BACKGROUNDS  (1344×768 → upscale to 1920×1080)

For all four, **add to POSITIVE**: `scenery, no humans, wide shot,`
and **add to NEGATIVE**: `1girl, 1boy, person, people, child, character`
(keeps people out of empty scenes).

### IMAGE 1 — `bg_mountain.png`  *(do first — the counting-game backdrop)*
Keep the lower-center open for squirrels + the big number.
**POSITIVE** (after prefix):
```
rolling green storybook mountain, sunny day, gentle grassy slopes, a winding dirt
path, a few round cartoon trees and bushes, bright blue sky, big fluffy white
clouds, cheerful and open, large empty grassy area in the lower center, scenery,
no humans
```

### IMAGE 2 — `bg_gate.png`
**POSITIVE:**
```
front gate of a friendly Chinese elementary school, autumn morning, golden warm
sunlight, a few orange leaves drifting down, low brick wall, welcoming entrance,
empty path in the foreground, soft focus background, scenery, no humans
```

### IMAGE 3 — `bg_library.png`
**POSITIVE:**
```
cozy children's school library interior, tall warm wooden bookshelves full of
colorful books, soft afternoon light from a window, a reading nook, calm quiet
mood, a faint magical golden glow on one shelf, empty foreground, scenery, no humans
```

### IMAGE 4 — `bg_classdoor.png`
**POSITIVE:**
```
open doorway of a warm elementary classroom seen from the hallway, colorful
children's drawings on the walls, cubbies, soft daylight, inviting but slightly
wistful, empty hallway foreground, scenery, no humans
```

---

# BATCH B — SPRITES & PROPS  (832×1216, transparent via LayerDiffuse)

For all sprites, **add to POSITIVE**: `full body, standing, looking at viewer,
simple background, white background,` and **add to NEGATIVE**: `cropped, out of
frame, multiple views`.

> **Fix a seed per character** and reuse it for that character's other expressions.

### IMAGE 5 — `wu_squirrel.png`  *(小五 the guide — lock this design, it recurs)*
**POSITIVE:**
```
a cute chibi cartoon red squirrel mascot, big sparkly black eyes, fluffy curled
tail, cream-colored belly, tiny paws, standing on hind legs, one paw raised
pointing, cheerful friendly expression, full body, simple background, white background,
no humans
```

### IMAGE 6 — `squirrel_token.png`  *(counting-game icon — reuse 小五's seed)*
Generate at **768×768**. Same squirrel, simpler sitting pose for a small UI token.
**POSITIVE:**
```
a single cute chibi red squirrel mascot, big sparkly eyes, fluffy tail, cream
belly, sitting, front view, simple clean icon, centered, simple background,
white background, no humans
```
*(Optional 2nd file `squirrel_token_found.png`: same but `happy, waving one paw,
eyes closed smiling`.)*

### IMAGE 7 — `mingming.png`  *(明明, shy default — lock this design)*
**POSITIVE:**
```
1boy, solo, child, 6 years old, round soft face, short black hair, single ahoge
cowlick, big dark brown eyes, light blue short sleeve collared shirt, navy blue
shorts, white sneakers, small red backpack, shy nervous expression, looking down
slightly, hands holding backpack straps, full body, standing, simple background,
white background
```

### IMAGE 8 — `mingming_smile.png`  *(明明 happy — REUSE image 7's seed)*
**POSITIVE:**
```
1boy, solo, child, 6 years old, round soft face, short black hair, single ahoge
cowlick, big dark brown eyes, light blue short sleeve collared shirt, navy blue
shorts, white sneakers, small red backpack, happy bright genuine smile, relaxed
confident posture, full body, standing, simple background, white background
```

### IMAGE 9 — `youyou.png`  *(友友, waving — new seed)*
**POSITIVE:**
```
1boy, solo, child, 6 years old, lively, messy short black hair, big open friendly
smile, rosy cheeks, orange t-shirt, green shorts, white sneakers, waving one hand
high, energetic happy stance, full body, standing, simple background, white background
```

### IMAGE 10 — `book.png`  *(the magic 《念一念》 — prop)*
Generate at **896×1152**.
**POSITIVE:**
```
no humans, a single closed magical storybook standing upright, ornate friendly
cover, blank cover with no text, warm golden glowing light and tiny sparkles
around the edges, fantasy children's book, simple background, white background
```
**ADD TO NEGATIVE:** `text, title, letters on cover`

---

## AFTER GENERATING

1. Backgrounds → confirm exactly **1920×1080**, save as `Huafu/game/images/gradeN/bg/<name>.png`.
2. Sprites → confirm transparent alpha, trim empty margins, feet near bottom edge,
   save to `Huafu/game/images/chars/` (characters used in every grade),
   `Huafu/game/images/props/` (shared props), or `Huafu/game/images/gradeN/props/`.
   Keep the untrimmed original + the ComfyUI workflow `.json` in `ArtSource/gradeN/`.
3. Tell me they're in, and I'll swap the Placeholders in `core/images.rpy` / `gradeN/images.rpy` for the
   real files + wire `mingming smile` and the squirrel token into the game.

## Tips
- Generate a **batch of 4** per prompt and pick the best — cheaper than re-rolling one.
- If a child sprite looks too old/tall, add `chibi, cute, 2 heads tall` to positive.
- If the style drifts between images, raise the storybook style-LoRA weight to ~0.85
  and keep the POSITIVE PREFIX identical everywhere.
- Backgrounds sneaking in people? Strengthen negative: `(person:1.4), (people:1.4)`.
