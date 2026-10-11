# grade1/lesson02.rpy
# 第二課 — 一棵樹上十樣果 + 握握手
# Snack time: Ming Ming steps into the fruit-tree world, counts ten fruits (六→十),
# then shares fruit with 友友 and makes his first friend with a handshake.
# Voice: chants use audio/grade1/voice/l02_1_NN / l02_2_NN; the fruit names use
# l02_fruit_NN (all made by tools/gen_voice.py). English glosses are in {en}…{/en}.
# Art still missing shows as placeholders (Design/grade1/art_lesson02.md).

# Shake-the-tree step: tap anywhere to shake the tree. Shows the shakes so far.
screen g1_shake_tree(n):
    modal True
    zorder 50

    button:
        id "shake_tree"
        xfill True
        yfill True
        background None
        action Return(True)

    vbox:
        xalign 0.5
        ypos 0.05
        spacing 6
        text "搖一搖樹！" size 70 color "#fff3d6" xalign 0.5 outlines [(4, "#5a3a10", 0, 0)]
        if persistent.show_english:
            text "Tap the tree three times to shake it!" size 28 color "#fff3d6" xalign 0.5:
                outlines [(2, "#5a3a10", 0, 0)]

    if n:
        text cn_num(n):
            size 150 color "#e0962f"
            outlines [(5, "#5a3a10", 0, 0)]
            xpos 0.5 xanchor 0.5 ypos 0.2

label g1_lesson02:

    ## ── L2.1 — 一棵樹上十樣果 ───────────────────────────────────────────────
    scene bg g1_classroom with fade
    $ play_bgm("audio/bgm/bgm_gentle.ogg")
    $ prequeue_bgm("audio/bgm/bgm_playful.ogg")   # fruit tree is next
    show mingming at center
    with dissolve

    narrator "下課了。小朋友都在吃點心。{en}\n(Recess. All the children are eating a snack.){/en}"
    mc_think "我沒有點心……{en}\n(I don't have a snack…){/en}"

    narrator "明明打開了《念一念》。{en}\n(Ming Ming opens 'Niàn Yi Niàn'.){/en}"
    $ play_sfx("audio/sfx/sfx_sparkle.ogg")
    show wu squirrel at right:
        yalign 1.0
    with dissolve
    wu "明明，你看！好多水果！{en}\n(Ming Ming, look! So much fruit!){/en}"
    narrator "小五拉著明明，跳進了書裡。{en}\n(Little Five takes his hand, and they jump into the book.){/en}"

    scene bg g1_fruit_tree with fade
    $ play_bgm("audio/bgm/bgm_playful.ogg")
    show wu squirrel at left:
        yalign 1.0
    with dissolve

    wu "一棵樹上，有好多水果！我們來念一念！{en}\n(One tree, so much fruit! Let's read it aloud!){/en}"

    call play_chant("第二課・一棵樹上十樣果", [
        ("一二三四五，六七八九十，", "1 2 3 4 5, 6 7 8 9 10,"),
        ("一棵樹上十樣果，", "One tree with ten kinds of fruit —"),
        ("你說稀奇不稀奇？", "Isn't that amazing?"),
        ("蘋果、香蕉、葡萄、", "Apples, bananas, grapes,"),
        ("橘子、番茄、桃子、", "Tangerines, tomatoes, peaches,"),
        ("杏子、木瓜、", "Apricots, papayas,"),
        ("李子、梨。", "Plums, and pears."),
    ], voice="audio/grade1/voice/l02_1")

    wu "我們來搖一搖樹！{en}\n(Let's shake the tree!){/en}"
    hide wu with dissolve

    # Shake the tree three times; then the fruit falls.
    $ g1_shakes = 0
    while g1_shakes < 3:
        call screen g1_shake_tree(g1_shakes)
        $ g1_shakes += 1
        $ play_sfx("audio/sfx/sfx_rustle.ogg")
        with hpunch

    # The ten fruits fall; tap each one to count and hear its name.
    call tap_count("bg g1_fruit_tree", ["g1_fruit_" + f[0] for f in G1_FRUITS],
                   [(0.12, 0.47), (0.31, 0.46), (0.50, 0.48), (0.69, 0.46), (0.88, 0.47),
                    (0.12, 0.71), (0.31, 0.70), (0.50, 0.72), (0.69, 0.70), (0.88, 0.71)],
                   "一棵樹上十樣果：數一數！",
                   hint="Tap each fruit: count 一 to 十 and hear its name",
                   done_text="太棒了！一棵樹上十樣果！ ✓",
                   labels=["蘋果", "香蕉", "葡萄", "橘子", "番茄", "桃子", "杏子", "木瓜", "李子", "梨"],
                   voice="audio/grade1/voice/l02_fruit", drop=True)

    show wu squirrel at left:
        yalign 1.0
    with dissolve
    mc "六、七、八、九、十……十樣水果！{en}\n(6, 7, 8, 9, 10… ten kinds of fruit!){/en}"
    narrator "小五吃了好多水果。明明拿了一個蘋果。{en}\n(Little Five stuffs itself with fruit. Ming Ming picks up one apple.){/en}"

    scene bg g1_classroom with fade
    $ play_bgm("audio/bgm/bgm_gentle.ogg")
    show mingming at center
    show g1_fruit_apple at Transform(xalign=0.64, yalign=0.6)
    with dissolve
    narrator "明明回到了教室。他的手上，有一個真的蘋果！{en}\n(Ming Ming is back in the classroom. In his hand is a real apple!){/en}"
    hide g1_fruit_apple with dissolve

    ## ── L2.2 — 握握手 ──────────────────────────────────────────────────────
    show mingming at left with move
    show youyou at right with dissolve
    yo "我有香蕉。給你！{en}\n(I have a banana. For you!){/en}"
    mc "謝謝……我有蘋果。給你！{en}\n(Thank you… I have an apple. For you!){/en}"
    yo "我叫友友。你呢？{en}\n(I'm Youyou. And you?){/en}"
    mc "我……我叫明明。{en}\n(I… I'm Ming Ming.){/en}"
    yo "明明！我們來念一念：握握手！{en}\n(Ming Ming! Let's say a chant: Shake Hands!){/en}"

    $ play_bgm("audio/bgm/bgm_playful.ogg")
    call play_chant("第二課・握握手", [
        ("一二三，握握手。", "1 2 3, shake hands."),
        ("四五六，點點頭。", "4 5 6, nod your head."),
        ("七八九，大步走。", "7 8 9, take big steps."),
        ("十百千，走圓圈。", "10, 100, 1000, walk in a circle."),
    ], voice="audio/grade1/voice/l02_2")

    yo "你來做一做！{en}\n(Now you do it!){/en}"

    # Pick the action for each line; solving a round replays that chant line.
    call pick_one("bg g1_classroom", "握握手：做一做！", [
        ("一二三，" + PICK_BLANK + "。", ["握握手", "點點頭", "大步走"], 0),
        ("四五六，" + PICK_BLANK + "。", ["大步走", "點點頭", "走圓圈"], 1),
        ("七八九，" + PICK_BLANK + "。", ["握握手", "走圓圈", "大步走"], 2),
        ("十百千，" + PICK_BLANK + "。", ["點點頭", "走圓圈", "握握手"], 1),
    ], hint="Pick the words that finish each line.",
       voice="audio/grade1/voice/l02_2", done_text="都對了！ ✓")

    # The first handshake.
    show mingming smile at left
    with dissolve
    show mingming smile:
        ease 0.8 xalign 0.32
    show youyou:
        ease 0.8 xalign 0.68
    pause 0.8
    narrator "一二三，握握手。明明和友友握了握手。{en}\n(1, 2, 3, shake hands. Ming Ming and Youyou shake hands.){/en}"
    mc_think "我有一個朋友了。{en}\n(I have a friend now.){/en}"

    # 友友 sees 小五 — and 中中 at the next desk looks over.
    show wu squirrel at Transform(xalign=0.5, yalign=0.72, zoom=0.6)
    with dissolve
    yo "哇！你的書會動！{en}\n(Wow! Your book moves!){/en}"
    hide wu with dissolve
    hide mingming
    hide youyou
    show zhongzhong at right
    with dissolve
    narrator "旁邊的一個小朋友，也看了過來。{en}\n(A boy at the next desk looks over, too.){/en}"
    zh "那是什麼？{en}\n(What is that?){/en}"

    ## ── Reward ───────────────────────────────────────────────────────────
    $ play_sfx("audio/sfx/sfx_star.ogg")
    call screen lesson_complete(3, "你學會了：六～十、十樣水果、握握手、點點頭")

    return
