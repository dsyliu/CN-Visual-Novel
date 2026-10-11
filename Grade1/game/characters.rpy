# characters.rpy
# Character definitions and placeholder art for the Grade 1 visual novel.
# Art is intentionally Placeholder() so the game runs before real assets exist.
# Replace each Placeholder with "images/<name>.png" when art is ready.

## Speaking characters ---------------------------------------------------------

define mc      = Character("明明", who_color="#3f7fc1")   # 言立明 — protagonist / player
define yo      = Character("友友", who_color="#e0962f")   # 林友友 — first friend
define zh      = Character("中中", who_color="#54a85a")   # 江禾中 — second friend
define teacher = Character("老師", who_color="#9b59b6")   # 老師
define wu      = Character("小五", who_color="#b5703a")   # 小松鼠 — magic book guide

# Narration (no name box) and Ming Ming's inner thoughts.
define narrator = Character(None, what_color="#f4ecd8")
define mc_think = Character("明明", what_italic=True, who_color="#3f7fc1", what_color="#cfe0f0")

## Placeholder backgrounds -----------------------------------------------------
## Placeholder("bg", ...) draws a labeled stand-in background at 1920x1080.

# Real art is scaled to fill the 1920x1080 screen (fit="cover" = no distortion).
image bg gate      = Transform("images/bg_gate.png", xysize=(1920, 1080), fit="cover")
image bg mountain  = Transform("images/bg_mountain.png", xysize=(1920, 1080), fit="cover")
image bg library   = Transform("images/bg_library.png", xysize=(1920, 1080), fit="cover")
image bg classdoor = Transform("images/bg_classdoor.png", xysize=(1920, 1080), fit="cover")

## Placeholder character sprites ----------------------------------------------

# 明明 the protagonist — full body, ~900px tall. Two expressions.
image mingming       = Transform("images/mingming.png", zoom=0.781)
image mingming smile = Transform("images/mingming_smile.png", zoom=0.781)
image youyou      = Transform("images/youyou.png", zoom=0.765)   # ~900px tall
image teacher_ph  = Placeholder("woman", text="老師")
# 小五 the squirrel guide — scaled to ~600px tall (a little guide character).
image wu squirrel = Transform("images/wu_squirrel.png", zoom=0.913)
# Counting-game token reuses 小五's art, scaled small (~150px tall).
image squirrel_token = Transform("images/squirrel_token.png", zoom=0.228)

## The glowing magic book 《華府》.
image book = Transform("images/book.png", zoom=0.655)   # ~480px tall
