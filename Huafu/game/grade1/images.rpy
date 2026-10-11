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

## Lesson 2 --------------------------------------------------------------------
# Art not made yet: placeholders show until the files are added
# (art list and prompts: Design/grade1/art_lesson02.md).

image bg g1_classroom  = Transform(art_or("images/grade1/bg/bg_classroom.png",
                                          Placeholder("bg")),
                                   xysize=(1920, 1080), fit="cover")
image bg g1_fruit_tree = Transform(art_or("images/grade1/bg/bg_fruit_tree.png",
                                          Placeholder("bg")),
                                   xysize=(1920, 1080), fit="cover")

# The ten fruits of 一棵樹上十樣果, in chant order: (file name, 中文, placeholder color).
# Images are "g1_fruit_<name>", each 140px, from images/grade1/props/fruit_<name>.png.
init python:
    G1_FRUITS = [
        ("apple",     "蘋果", "#d64541"),
        ("banana",    "香蕉", "#f2c94c"),
        ("grapes",    "葡萄", "#8e44ad"),
        ("tangerine", "橘子", "#f39c12"),
        ("tomato",    "番茄", "#e74c3c"),
        ("peach",     "桃子", "#f5a6a0"),
        ("apricot",   "杏子", "#f0a845"),
        ("papaya",    "木瓜", "#e67e22"),
        ("plum",      "李子", "#7d3c98"),
        ("pear",      "梨",   "#c5d86d"),
    ]

    def _fruit_placeholder(name, color):
        return Fixed(Solid(color), Text(name, size=44, color="#ffffff", outlines=[(3, "#00000088", 0, 0)],
                                        xalign=0.5, yalign=0.5),
                     xysize=(140, 140))

    for _key, _name, _color in G1_FRUITS:
        renpy.image("g1_fruit_" + _key,
                    Transform(art_or("images/grade1/props/fruit_{}.png".format(_key),
                                     _fruit_placeholder(_name, _color)),
                              xysize=(140, 140), fit="contain"))
