# grade1/lesson01.rpy
# 第一課 — 上山找老虎 + 我的朋友在哪裡
# Opening cutscene of Grade 1 + Lesson 1's two chants.
# Audio is hooked but optional: drop files in game/audio/grade1/ and uncomment the
# `voice`/`play` lines to enable narration.

label g1_lesson01:

    ## ── OPENING CUTSCENE — 第一天 (The First Day) ──────────────────────────
    scene bg g1_gate with fade
    $ play_bgm("audio/bgm/bgm_gentle.ogg")
    $ prequeue_bgm("audio/bgm/bgm_magic.ogg")     # library is next
    show mingming at center
    with dissolve

    narrator "開學了。第一天。\n(The first day of school.)"
    mc_think "好多人……我不認識他們。\n(So many people… I don't know any of them.)"

    narrator "下課了。明明一個人走進圖書館。\n(At recess, Ming Ming wanders alone into the library.)"

    scene bg g1_library with fade
    $ play_bgm("audio/bgm/bgm_magic.ogg")
    $ prequeue_bgm("audio/bgm/bgm_playful.ogg")   # mountain is next
    show book at center:
        zoom 1.0 yalign 0.45
    with dissolve
    $ play_sfx("audio/sfx/sfx_sparkle.ogg")

    narrator "書架上，有一本書在發光。《念一念》。\n(On the shelf, a book is glowing: 'Niàn Yi Niàn'.)"
    mc "這是什麼書？\n(What book is this?)"

    # 明明 opens the book — out tumbles a squirrel.
    show wu squirrel at right:
        yalign 1.0
    with dissolve
    wu "一、二、三、四、五！"
    mc "你……你會說話？\n(You… you can talk?)"

    narrator "小松鼠拉住明明的手，把他拉進書裡。\n(The little squirrel grabs his hand and pulls him into the book.)"

    ## ── L1.1 — 上山找老虎 ────────────────────────────────────────────────
    scene bg g1_mountain with fade
    $ play_bgm("audio/bgm/bgm_playful.ogg")
    $ prequeue_bgm("audio/bgm/bgm_gentle.ogg")    # classroom reprise is next
    show wu squirrel at left:
        yalign 1.0
    with dissolve

    wu "這是山上。我們來找老虎！\n(This is the mountain. Let's find the tiger!)"

    # play the chant (karaoke reader)
    # To add audio: voice "audio/grade1/l1_1.ogg" before this call, or per-line later.
    call play_chant("第一課・上山找老虎", [
        ("一二三四五，上山找老虎，", "1 2 3 4 5, up the mountain to find the tiger,"),
        ("老虎找不到，看見小松鼠。", "No tiger to be found — but I see little squirrels."),
        ("松鼠有幾隻？一二三四五。", "How many squirrels? 1 2 3 4 5."),
    ])

    wu "老虎找不到……可是有好多松鼠！你來數一數。\n(No tiger… but so many squirrels! You count them.)"

    # the interactive counting game (minigames/tap_count.rpy)
    call tap_count("bg g1_mountain", "g1_squirrel_token",
                   [(0.16, 0.46), (0.36, 0.66), (0.54, 0.40), (0.72, 0.64), (0.86, 0.44)],
                   "上山找老虎：數一數松鼠！",
                   hint="Tap each squirrel and count: 一 二 三 四 五",
                   done_text="太棒了！松鼠有五隻！ ✓")

    mc "一、二、三、四、五……松鼠有五隻！\n(1, 2, 3, 4, 5… there are five squirrels!)"
    show mingming smile at right:
        yalign 1.0
    with dissolve
    narrator "明明笑了。這是他今天第一次笑。\n(Ming Ming laughs — the first time all day.)"

    ## ── L1.2 — 我的朋友在哪裡 ────────────────────────────────────────────
    narrator "書頁自己翻了。一個詞亮了起來：朋友。\n(The page turns by itself. One word lights up: 'friends'.)"
    mc_think "朋友……我沒有朋友。\n(Friends… I don't have any friends.)"

    scene bg g1_classdoor with fade
    $ play_bgm("audio/bgm/bgm_gentle.ogg")
    with dissolve

    call play_chant("第一課・我的朋友在哪裡", [
        ("一二三四五六七，", "1 2 3 4 5 6 7,"),
        ("我的朋友在哪裡？", "Where are my friends?"),
        ("在這裡，在這裡，", "Here they are, here they are,"),
        ("我的朋友在這裡。", "My friends are right here."),
    ])

    # The question lands on the player — but no friend is here yet…
    narrator "「你的朋友在哪裡？」\n('Where are YOUR friends?')"

    show youyou at right with dissolve
    yo "喂——！"
    narrator "一個小朋友對著明明招手——可是上課了，他被帶走了。\n(A boy waves at Ming Ming — but class starts, and he's swept away.)"
    hide youyou with dissolve

    mc_think "我的朋友……在哪裡？\n(Where… are my friends?)"
    narrator "（別急。慢慢來。）\n(Don't worry. Take your time.)"

    ## ── Reward ───────────────────────────────────────────────────────────
    $ play_sfx("audio/sfx/sfx_star.ogg")
    call screen lesson_complete(3, "你學會了：一～七、松鼠、老虎、朋友")

    return
