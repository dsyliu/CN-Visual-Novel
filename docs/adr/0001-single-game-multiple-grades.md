# 0001 — One game holds every grade

- Status: accepted
- Date: 2026-10-10

## Context

The game started as a Grade 1 project (`Grade1/` was the whole Ren'Py project).
More grades will follow, starting with Grade 2. The user wants players to open one
game and choose which grade to play from the start menu, not install a separate
game per grade.

## Decision

- One Ren'Py project, `Huafu/`, holds every grade.
- The main menu's Start button opens a grade-select screen (`core/grades.rpy`).
  Each grade is an entry in `GRADES`; its card becomes playable once its
  `gN_start` label exists, and shows 即將推出 (coming soon) until then.
- Code shared by every grade lives in `game/core/` and `game/minigames/`.
  Each grade gets its own folder, `game/gradeN/`.
- Ren'Py labels, screens, images, and `default` variables are global, so
  everything specific to a grade carries a grade prefix:
  - labels and screens: `g1_lesson01`, `g1_start`
  - images: `bg g1_mountain`, `g1_squirrel_token` — the grade goes in the name,
    never as the first word (the image tag), or grade images would replace each
    other on screen
  - variables and persistent data: `g1_...`, `persistent.g1_...`
- Design docs, source text, and art originals live outside the Ren'Py project
  (`Design/`, `References/`, `ArtSource/`) so builds never include them.

## Consequences

- Adding a grade = add a `GRADES` entry + a `gradeN/` folder with `main.rpy`.
- Shared systems (chant reader, reward card, mini-games) are written once and
  must stay free of any one grade's art or names; they take those as arguments.
- Saved games refer to labels by name. Renaming a label after release breaks
  saves made inside it, so grade prefixes were applied before any real players.
