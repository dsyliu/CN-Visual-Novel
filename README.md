# 華府 (Huafu)

A visual novel for learning Traditional Chinese, made for the students of 華府中文學校.
Each chant from the class textbook becomes a story scene inside the magic book
《念一念》: the player reads the chant line by line, hears it spoken, and plays a
short game with its words.

**Play in the browser:** https://dsyliu.github.io/CN-Visual-Novel/
(works on computers and tablets; the first load is about 50 MB)

## What is in the game

- One game for every grade. On Start, the player picks the grade (第一冊, …), then
  the lesson. Play goes on from that lesson to the next.
- Grade 1: Lessons 1–2 are done. Lessons 3–16 show 即將推出 (coming soon).
- Every chant line and dialogue line has voice (generated text-to-speech for now).
- English help text can be turned off: Preferences → 英文 English.

## Project layout

| Folder | What it holds |
|---|---|
| `Huafu/` | The Ren'Py project (the game) |
| `Huafu/game/core/` | Code for every grade: characters, images, audio, voice, chant reader, grade and lesson select, reward card |
| `Huafu/game/minigames/` | Shared mini-games (`tap_count`, `pick_one`) |
| `Huafu/game/grade1/` | Grade 1: `main.rpy` (lesson list and order), `lessonNN.rpy`, `images.rpy` |
| `Huafu/game/tests/` | Automated smoke test |
| `Design/` | Story bible, character bible, art and audio guides, per-lesson art lists |
| `References/` | The textbook chant text |
| `ArtSource/` | Original art and ComfyUI workflows (not in the game build) |
| `tools/` | Voice generation, font subsetting, loading picture, web deploy |
| `docs/adr/` | Design decisions |

## Run it

You need the [Ren'Py SDK](https://www.renpy.org/) 8.5.3.

```
renpy.exe Huafu            # play
renpy.exe Huafu lint       # check the scripts
renpy.exe Huafu test smoke # play each lesson end to end automatically
```

Tools (Python 3):

```
pip install edge-tts imageio-ffmpeg fonttools pillow
python tools/gen_voice.py     # make voice files for new or changed lines
bash tools/deploy_web.sh      # build the web version and publish it to GitHub Pages
```

## How it is made

- **Engine:** Ren'Py, with a web build on GitHub Pages.
- **Art:** made locally in ComfyUI with an SDXL (Illustrious/NoobAI) checkpoint. See
  `Design/shared/comfyui_generation_guide.md`. Art not made yet shows as a placeholder.
- **Voice:** edge-tts (Microsoft neural voices), made by `tools/gen_voice.py`.
- **Font:** Noto Sans TC, subset to the characters the game uses.

