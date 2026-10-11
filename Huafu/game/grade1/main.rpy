# grade1/main.rpy
# Grade 1 (第一冊) entry point. The grade-select menu starts here.
# Chains the lessons in order; each lesson is in its own grade1/lessonNN.rpy.

label g1_start:

    # Title card.
    scene black with fade
    $ play_bgm("audio/bgm/theme_main.ogg")
    $ prequeue_bgm("audio/bgm/bgm_gentle.ogg")    # warm the opening track before Lesson 1
    centered "{size=90}{color=#ffd98a}華府{/color}{/size}\n\n{size=36}華府中文學校・第一冊{/size}{en}\n{size=28}Grade 1 — A Reading Adventure{/size}{/en}"
    with dissolve

    # Act 1, Lesson 1 (also contains the game's opening cutscene).
    call g1_lesson01

    # More lessons will be chained here as they're built:
    # call g1_lesson02
    # ...

    return
