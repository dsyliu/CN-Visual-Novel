# grade1/lesson01.rpy
# 第一課 — 上山找老虎 + 我的朋友在哪裡
# Opening cutscene of Grade 1 + Lesson 1's two chants.
# Chant voice is optional: drop files in game/audio/grade1/voice/ named
# l01_1_01.ogg, l01_1_02.ogg … (chant 1) and l01_2_01.ogg … (chant 2); they play
# automatically. English glosses are wrapped in {en}…{/en} (core/english.rpy).

label g1_lesson01:

    ## ── OPENING CUTSCENE — 第一天 (The First Day) ──────────────────────────
    scene bg g1_gate with fade
    $ play_bgm("audio/bgm/bgm_gentle.ogg")
    $ prequeue_bgm("audio/bgm/bgm_magic.ogg")     # library is next
    show mingming at center
    with dissolve

    narrator "開學了。第一天。{en}\n(The first day of school.){/en}"
    mc_think "好多人……我不認識他們。{en}\n(So many people… I don't know any of them.){/en}"

    narrator "下課了。明明一個人走進圖書館。{en}\n(At recess, Ming Ming wanders alone into the library.){/en}"

    scene bg g1_library with fade
    $ play_bgm("audio/bgm/bgm_magic.ogg")
    $ prequeue_bgm("audio/bgm/bgm_playful.ogg")   # mountain is next
    show book at center:
        zoom 1.0 yalign 0.45
    with dissolve
    $ play_sfx("audio/sfx/sfx_sparkle.ogg")

    narrator "書架上，有一本書在發光。《念一念》。{en}\n(On the shelf, a book is glowing: 'Niàn Yi Niàn'.){/en}"
    mc "這是什麼書？{en}\n(What book is this?){/en}"

    # 明明 opens the book — out tumbles a squirrel.
    show wu squirrel at right:
        yalign 1.0
    with dissolve
    wu "一、二、三、四、五！"
    mc "你……你會說話？{en}\n(You… you can talk?){/en}"

    narrator "小松鼠拉住明明的手，把他拉進書裡。{en}\n(The little squirrel grabs his hand and pulls him into the book.){/en}"

    ## ── L1.1 — 上山找老虎 ────────────────────────────────────────────────
    scene bg g1_mountain with fade
    $ play_bgm("audio/bgm/bgm_playful.ogg")
    $ prequeue_bgm("audio/bgm/bgm_gentle.ogg")    # classroom reprise is next
    show wu squirrel at left:
        yalign 1.0
    with dissolve

    wu "這是山上。我們來找老虎！{en}\n(This is the mountain. Let's find the tiger!){/en}"

    # play the chant (karaoke reader); voice files: audio/grade1/voice/l01_1_01.ogg …
    call play_chant("第一課・上山找老虎", [
        ("一二三四五，上山找老虎，", "1 2 3 4 5, up the mountain to find the tiger,"),
        ("老虎找不到，看見小松鼠。", "No tiger to be found — but I see little squirrels."),
        ("松鼠有幾隻？一二三四五。", "How many squirrels? 1 2 3 4 5."),
    ], voice="audio/grade1/voice/l01_1")

    wu "老虎找不到……可是有好多松鼠！你來數一數。{en}\n(No tiger… but so many squirrels! You count them.){/en}"

    # the interactive counting game (minigames/tap_count.rpy)
    call tap_count("bg g1_mountain", "g1_squirrel_token",
                   [(0.16, 0.46), (0.36, 0.66), (0.54, 0.50), (0.72, 0.64), (0.86, 0.44)],
                   "上山找老虎：數一數松鼠！",
                   hint="Tap each squirrel and count: 一 二 三 四 五",
                   done_text="太棒了！松鼠有五隻！ ✓")

    mc "一、二、三、四、五……松鼠有五隻！{en}\n(1, 2, 3, 4, 5… there are five squirrels!){/en}"
    show mingming smile at right:
        yalign 1.0
    with dissolve
    narrator "明明笑了。這是他今天第一次笑。{en}\n(Ming Ming laughs — the first time all day.){/en}"

    ## ── L1.2 — 我的朋友在哪裡 ────────────────────────────────────────────
    narrator "書頁自己翻了。一個詞亮了起來：朋友。{en}\n(The page turns by itself. One word lights up: 'friends'.){/en}"
    mc_think "朋友……我沒有朋友。{en}\n(Friends… I don't have any friends.){/en}"

    scene bg g1_classdoor with fade
    $ play_bgm("audio/bgm/bgm_gentle.ogg")
    with dissolve

    call play_chant("第一課・我的朋友在哪裡", [
        ("一二三四五六七，", "1 2 3 4 5 6 7,"),
        ("我的朋友在哪裡？", "Where are my friends?"),
        ("在這裡，在這裡，", "Here they are, here they are,"),
        ("我的朋友在這裡。", "My friends are right here."),
    ], voice="audio/grade1/voice/l01_2")

    # The question lands on the player — but no friend is here yet…
    narrator "「你的朋友在哪裡？」{en}\n('Where are YOUR friends?'){/en}"

    show youyou at right with dissolve
    yo "喂——！"
    narrator "一個小朋友對著明明招手——可是上課了，他被帶走了。{en}\n(A boy waves at Ming Ming — but class starts, and he's swept away.){/en}"
    hide youyou with dissolve

    mc_think "我的朋友……在哪裡？{en}\n(Where… are my friends?){/en}"
    narrator "（別急。慢慢來。）{en}\n(Don't worry. Take your time.){/en}"

    ## ── Reward ───────────────────────────────────────────────────────────
    $ play_sfx("audio/sfx/sfx_star.ogg")
    call screen lesson_complete(3, "你學會了：一～七、松鼠、老虎、朋友")

    return
