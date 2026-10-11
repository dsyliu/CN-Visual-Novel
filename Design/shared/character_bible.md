# Character Design Bible

Fixed look for every recurring character, shared by all grades. **Never vary these
tokens** between images — paste them into every prompt for that character.

- Prompt settings, style prefix, and negatives: `comfyui_generation_guide.md`.
- Story roles and personalities: `Design/grade1/story_bible.md` §3.
- Once a character has approved art, that sprite is the visual source of truth;
  the tokens below describe it.
- Signature colors match each character's name color in `Huafu/game/core/characters.rpy`.

---

## Characters with approved art

### 明明 Ming Ming — protagonist (shy → brave)
```
a 6-year-old Chinese boy, round soft face, short black hair with one small
cowlick, big dark brown eyes, light blue short-sleeve collared shirt,
navy-blue shorts, white sneakers, small red backpack
```
Personality read: gentle, a little timid. Signature color: blue (#3f7fc1).
Art: `Huafu/game/images/chars/mingming.png` (shy), `mingming_smile.png` (happy).

### 友友 Youyou — first friend (sunny, loud)
```
a 6-year-old Chinese boy, lively, slightly messy short black hair, big bright
smile, rosy cheeks, orange-yellow t-shirt, green shorts, white sneakers
```
Signature color: orange (#e0962f).
Art: `Huafu/game/images/chars/youyou.png` (waving).

### 小五 Little Five — the magic squirrel guide
```
a small cute cartoon red squirrel, big sparkly eyes, fluffy curled tail,
tiny paws, friendly expression, storybook mascot, holding up its little paws
```
Signature color: brown (#b5703a). Must read as cute, never realistic/rodent-scary.
Art: `Huafu/game/images/chars/wu_squirrel.png`.

---

## Characters still to design

These designs are drafts. Lock them (and add their art paths above) once the
first approved sprite exists.

### 中中 Zhongzhong — second friend (calm, clever)
```
a 6-year-old Chinese boy, calm gentle face, neat short straight black hair with
a tidy side part, round black glasses, small thoughtful smile, green polo shirt,
khaki shorts, white sneakers, holding a small sketchbook
```
Seed: **1083328916370374** (KSamplerAdvanced `noise_seed`, `control_after_generate`
= fixed). Reuse it for every 中中 pose.
Signature color: green (#54a85a). First needed: Lesson 2 (end of 握握手); he talks
from Lesson 3. Full prompt: `Design/grade1/art_lesson02.md`. In-game he is a
placeholder until `Huafu/game/images/chars/zhongzhong.png` exists.

### 老師 Teacher — warm guide
```
a warm young Chinese woman, hair in a low bun, soft cardigan, holding a
picture book, kind smile
```
Signature color: purple (#9b59b6). First needed: Lesson 3 (拍拍手).
In-game she is still a placeholder (`teacher_ph` in `core/images.rpy`).

---

## Keeping characters consistent

- Fix a **seed** per character and keep its exact appearance tokens above. Write the
  seed under the character here (read it from the original PNG: drag it onto the
  ComfyUI canvas — the node's number after a `randomize` run is the *next* seed).
- Use the same checkpoint for every asset.
- For real production, train a small **LoRA** per character (15–20 images).
- Always render characters on a **plain flat background** so they cut out cleanly.
- Keep each approved original + its ComfyUI workflow `.json` in `ArtSource/`.
