# ArtSource

Original, untrimmed art and the ComfyUI workflows that made it. This folder is
outside the Ren'Py project (`Huafu/`), so it never ships with the game.

Why keep these: trimming a sprite for the game strips its PNG metadata, which
holds the seed and prompt. Without the originals, a character can't be
regenerated on-model.

Layout: one folder per grade, plus `shared/` for characters used in every grade.

```
ArtSource/
├── shared/      # 明明, 友友, 小五, the book …
└── grade1/      # Grade 1 backgrounds and props
```

For each asset, keep:
- the original ComfyUI output PNG (metadata intact)
- the workflow `.json` exported from ComfyUI
