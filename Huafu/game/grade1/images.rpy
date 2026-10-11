# grade1/images.rpy
# Grade 1 backgrounds and props. Shared sprites are in core/images.rpy.
# Names carry "g1_" so they never clash with another grade (see core/images.rpy).

## Backgrounds -----------------------------------------------------------------
# Real art is scaled to fill the 1920x1080 screen (fit="cover" = no distortion).

image bg g1_gate      = Transform("images/grade1/bg/bg_gate.png", xysize=(1920, 1080), fit="cover")
image bg g1_mountain  = Transform("images/grade1/bg/bg_mountain.png", xysize=(1920, 1080), fit="cover")
image bg g1_library   = Transform("images/grade1/bg/bg_library.png", xysize=(1920, 1080), fit="cover")
image bg g1_classdoor = Transform("images/grade1/bg/bg_classdoor.png", xysize=(1920, 1080), fit="cover")

## Props -----------------------------------------------------------------------

# Lesson 1 counting-game token reuses 小五's art, scaled small (~150px tall).
image g1_squirrel_token = Transform("images/grade1/props/squirrel_token.png", zoom=0.228)
