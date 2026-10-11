# CN-Visual-Novel

A Chinese-language visual novel built with Ren'Py, with art generated via ComfyUI (SDXL). One game holds every grade; the player picks a grade on the start menu. The Ren'Py project is `Huafu/`; Grade 1 content lives under `Huafu/game/grade1/` (see `docs/adr/0001-single-game-multiple-grades.md`).

## Running

Ren'Py SDK: `C:\Users\dsyli\Downloads\renpy-8.5.3-sdk\renpy.exe`

- Play: `renpy.exe <repo>/Huafu`
- Lint: `renpy.exe <repo>/Huafu lint`
- Smoke test (plays each Grade 1 lesson end to end, started from lesson select): `renpy.exe <repo>/Huafu test smoke`
- Voice (TTS for all dialogue + chant lines; only changed lines): `python tools/gen_voice.py` — run after editing any dialogue or chant text
- Publish the web version to GitHub Pages: `bash tools/deploy_web.sh` → https://dsyliu.github.io/CN-Visual-Novel/ (players get it within ~10 minutes; browser cache)

## Writing rules

- English glosses go inside `{en}…{/en}` (players can hide them). See `docs/adr/0002-english-toggle-and-chant-voice.md`.
- Every `call play_chant(...)` gets `voice="audio/gradeN/voice/lLL_C"`.
- Shared mini-games are in `Huafu/game/minigames/` (`tap_count`, `pick_one`); reuse them before making a new one. Spoken words in a mini-game: write `labels=[...]` then `voice="..."`, and `gen_voice.py` makes the files.
- Art not made yet: define the image with `art_or(path, placeholder)` (`core/images.rpy`). The placeholder shows until the file exists.
- The web build runs in a browser: no threads, no subprocesses, keep files small.

## Agent skills

### Issue tracker

Issues and specs live as local markdown files under `.scratch/<feature-slug>/`, not GitHub Issues. The code is on GitHub at `dsyliu/CN-Visual-Novel` (`origin`, branch `main`). See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context: `CONTEXT.md` at the root plus `docs/adr/`. Existing narrative and art design docs live in `Design/` (`shared/` and one folder per grade). See `docs/agents/domain.md`.
