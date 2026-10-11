# CN-Visual-Novel

A Chinese-language visual novel built with Ren'Py, with art generated via ComfyUI (SDXL). One game holds every grade; the player picks a grade on the start menu. The Ren'Py project is `Huafu/`; Grade 1 content lives under `Huafu/game/grade1/` (see `docs/adr/0001-single-game-multiple-grades.md`).

## Running

Ren'Py SDK: `C:\Users\dsyli\Downloads\renpy-8.5.3-sdk\renpy.exe`

- Play: `renpy.exe <repo>/Huafu`
- Lint: `renpy.exe <repo>/Huafu lint`
- Smoke test (plays Grade 1 Lesson 1 end to end): `renpy.exe <repo>/Huafu test smoke`

## Agent skills

### Issue tracker

Issues and specs live as local markdown files under `.scratch/<feature-slug>/`, not GitHub Issues. The code is on GitHub at `dsyliu/CN-Visual-Novel` (`origin`, branch `main`). See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context: `CONTEXT.md` at the root plus `docs/adr/`. Existing narrative and art design docs live in `Design/` (`shared/` and one folder per grade). See `docs/agents/domain.md`.
