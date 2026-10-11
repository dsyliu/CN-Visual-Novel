# grade1/main.rpy
# Grade 1 (第一冊) entry points and lesson list.
# Each lesson is in its own grade1/lessonNN.rpy. The lessons are chained in order:
# Ren'Py runs on from one label into the next, so starting at g1_start_02 plays
# Lesson 2, then Lesson 3, and so on.

# The lesson-select screen (core/grades.rpy) shows one card per entry. A card is
# playable once its "label" exists. To add a lesson: write lessonNN.rpy, then add
# `label g1_start_NN:` + `call g1_lessonNN` at its place in the chain below.
define g1_lessons = [
    {"title": "第一課", "subtitle": "Lesson 1", "chants": ["上山找老虎", "我的朋友在哪裡"], "label": "g1_start"},
    {"title": "第二課", "subtitle": "Lesson 2", "chants": ["一棵樹上十樣果", "握握手"], "label": "g1_start_02"},
    {"title": "第三課", "subtitle": "Lesson 3", "chants": ["拍拍手", "一年有幾個月"], "label": "g1_start_03"},
    {"title": "第四課", "subtitle": "Lesson 4", "chants": ["我有十個手指頭", "畫張畫"], "label": "g1_start_04"},
    {"title": "第五課", "subtitle": "Lesson 5", "chants": ["小人兒上大山", "晚上"], "label": "g1_start_05"},
    {"title": "第六課", "subtitle": "Lesson 6", "chants": ["媽媽的生日", "起得早"], "label": "g1_start_06"},
    {"title": "第七課", "subtitle": "Lesson 7", "chants": ["紅花和白花", "下雨了"], "label": "g1_start_07"},
    {"title": "第八課", "subtitle": "Lesson 8", "chants": ["大風和大雨", "來猜拳"], "label": "g1_start_08"},
    {"title": "第九課", "subtitle": "Lesson 9", "chants": ["一粒米"], "label": "g1_start_09"},
    {"title": "第十課", "subtitle": "Lesson 10", "chants": ["猴子穿新衣"], "label": "g1_start_10"},
    {"title": "第十一課", "subtitle": "Lesson 11", "chants": ["五官和雙手", "口說好話"], "label": "g1_start_11"},
    {"title": "第十二課", "subtitle": "Lesson 12", "chants": ["小狗和小雞", "雪人怎麼不見了"], "label": "g1_start_12"},
    {"title": "第十三課", "subtitle": "Lesson 13", "chants": ["小嘴巴", "鏡子"], "label": "g1_start_13"},
    {"title": "第十四課", "subtitle": "Lesson 14", "chants": ["比一比"], "label": "g1_start_14"},
    {"title": "第十五課", "subtitle": "Lesson 15", "chants": ["什麼是朋友"], "label": "g1_start_15"},
    {"title": "第十六課", "subtitle": "Lesson 16", "chants": ["我和我的朋友"], "label": "g1_start_16"},
]

label g1_start:

    # Title card (only when starting from Lesson 1).
    scene black with fade
    $ play_bgm("audio/bgm/theme_main.ogg")
    $ prequeue_bgm("audio/bgm/bgm_gentle.ogg")    # warm the opening track before Lesson 1
    centered "{size=90}{color=#ffd98a}華府{/color}{/size}\n\n{size=36}華府中文學校・第一冊{/size}{en}\n{size=28}Grade 1 — A Reading Adventure{/size}{/en}"
    with dissolve

    # Act 1, Lesson 1 (also contains the game's opening cutscene).
    call g1_lesson01

label g1_start_02:
    # Lesson 2: fruit tree + first friend (友友).
    call g1_lesson02

    # More lessons will be chained here as they're built:
    # label g1_start_03:
    #     call g1_lesson03
    # ...

    return
