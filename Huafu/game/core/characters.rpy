# core/characters.rpy
# Speaking characters, shared by every grade.
# Sprite and prop images live in core/images.rpy (shared) and gradeN/images.rpy.

## Speaking characters ---------------------------------------------------------

define mc      = Character("明明", who_color="#3f7fc1")   # 言立明 — protagonist / player
define yo      = Character("友友", who_color="#e0962f")   # 林友友 — first friend
define zh      = Character("中中", who_color="#54a85a")   # 江禾中 — second friend
define teacher = Character("老師", who_color="#9b59b6")   # 老師
define wu      = Character("小五", who_color="#b5703a")   # 小松鼠 — magic book guide

# Narration (no name box) and Ming Ming's inner thoughts.
define narrator = Character(None, what_color="#f4ecd8")
define mc_think = Character("明明", what_italic=True, who_color="#3f7fc1", what_color="#cfe0f0")
