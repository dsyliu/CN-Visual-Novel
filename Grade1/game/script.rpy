# script.rpy — entry point.
# Story/characters live in characters.rpy; reusable gameplay in mechanics.rpy;
# each lesson in its own lessonN.rpy. This file just routes the flow.

label start:

    # Title card.
    scene black with fade
    $ play_bgm("audio/theme_main.ogg")
    $ prequeue_bgm("audio/bgm_gentle.ogg")    # warm the opening track before Lesson 1
    centered "{size=90}{color=#ffd98a}華府{/color}{/size}\n\n{size=36}華府中文學校・第一冊{/size}\n{size=28}Grade 1 — A Reading Adventure{/size}"
    with dissolve

    # Act 1, Lesson 1 (also contains the game's opening cutscene).
    call lesson1

    # More lessons will be chained here as they're built:
    # call lesson2
    # ...

    return
