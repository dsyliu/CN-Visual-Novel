# core/images.rpy
# Shared images: character sprites and props that appear in more than one grade.
# Grade-specific backgrounds and props go in gradeN/images.rpy.
#
# Naming: Ren'Py image names are global, and the first word is the "tag" (a new
# image with the same tag replaces the old one on screen). Shared images use
# plain names; grade images put the grade in the second word or the name, e.g.
# "bg g1_gate" or "g1_squirrel_token" — never "g1 ..." as the tag.

## Character sprites -----------------------------------------------------------

# 明明 the protagonist — full body, ~900px tall. Two expressions.
image mingming       = Transform("images/chars/mingming.png", zoom=0.781)
image mingming smile = Transform("images/chars/mingming_smile.png", zoom=0.781)
image youyou         = Transform("images/chars/youyou.png", zoom=0.765)   # ~900px tall
# 小五 the squirrel guide — scaled to ~600px tall (a little guide character).
image wu squirrel    = Transform("images/chars/wu_squirrel.png", zoom=0.913)
# 老師 has no art yet.
image teacher_ph     = Placeholder("woman", text="老師")

## Props -----------------------------------------------------------------------

# The glowing magic book 《念一念》.
image book = Transform("images/props/book.png", zoom=0.655)   # ~480px tall
