# mechanics.rpy
# Reusable, lesson-agnostic gameplay pieces:
#   1. play_chant      — karaoke-style 念一念 reader (highlights the current line)
#   2. squirrel_count  — the L1 "tap & count to five" mini-game
#   3. lesson_complete — star reward card
# These are written to be re-used by every lesson.

init python:
    CN_NUM = ["", "一", "二", "三", "四", "五",
              "六", "七", "八", "九", "十"]

    def cn_num(k):
        return CN_NUM[k] if 0 <= k < len(CN_NUM) else str(k)


## 1. 念一念 karaoke reader -----------------------------------------------------
## Shows the whole chant; the line being read is large & bright, the rest dim.
## A full-screen click button advances one line at a time, then returns.
## A `voice` file can later be attached per line (see lesson1.rpy hooks).

screen chant_screen(title, lines):
    modal True
    zorder 50

    default idx = 0

    # Full-screen click-to-advance. The frame/text below are non-focusable, so
    # clicks anywhere fall through to this button.
    button:
        xfill True
        yfill True
        background "#000000aa"
        padding (0, 0)
        action [Function(play_sfx, "audio/sfx_page.ogg"),
                If(idx < len(lines) - 1,
                   SetScreenVariable("idx", idx + 1),
                   Return(True))]

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1600
        background Frame(Solid("#241b12f2"), 40, 40)
        padding (70, 55)

        vbox:
            xalign 0.5
            spacing 14

            text title size 42 color "#ffd98a" xalign 0.5
            null height 12

            for i, line in enumerate(lines):
                vbox:
                    xalign 0.5
                    spacing 2
                    text line[0]:
                        xalign 0.5
                        size (66 if i == idx else 46)
                        color ("#fff3d6" if i == idx else "#b3a489")
                    if i == idx and line[1]:
                        text line[1] size 26 color "#9a8d76" xalign 0.5

    text ("▸ 點一下繼續 (tap to continue)" if idx < len(lines) - 1
          else "▸ 點一下完成 (tap to finish)"):
        size 24 color "#ddddddcc" xalign 0.5 yalign 0.95

label play_chant(title, lines):
    call screen chant_screen(title, lines)
    return


## 2. 數松鼠 counting mini-game -------------------------------------------------

default sq_found = []   # squirrel indices, in the order the player tapped them

init python:
    SQUIRREL_POS = [(0.16, 0.46), (0.36, 0.66), (0.54, 0.40),
                    (0.72, 0.64), (0.86, 0.44)]

    def tap_squirrel(i):
        if i not in sq_found:
            sq_found.append(i)
            play_sfx("audio/sfx_tap.ogg")
            if len(sq_found) == 5:
                play_sfx("audio/sfx_correct.ogg")

screen squirrel_count():
    modal True
    zorder 50
    add "bg mountain"

    vbox:
        xalign 0.5
        ypos 0.05
        spacing 6
        text "上山找老虎：數一數松鼠！" size 50 color "#27431f" xalign 0.5
        text "Tap each squirrel and count: 一 二 三 四 五" size 26 color "#3a5a30" xalign 0.5

    # Big running total in the centre-top.
    text cn_num(len(sq_found)):
        size 150 color "#e0962f"
        outlines [(5, "#5a3a10", 0, 0)]
        xpos 0.5 xanchor 0.5 ypos 0.17

    for i in range(5):
        $ pos = SQUIRREL_POS[i]
        button:
            xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5
            action Function(tap_squirrel, i)
            sensitive (i not in sq_found)
            vbox:
                spacing 2
                # tapped squirrels fade out and show their count number
                if i in sq_found:
                    add "squirrel_token" alpha 0.4
                    text cn_num(sq_found.index(i) + 1):
                        size 52 color "#ffe08a" xalign 0.5
                        outlines [(3, "#5a3a10", 0, 0)]
                else:
                    add "squirrel_token"

    if len(sq_found) >= 5:
        text "太棒了！松鼠有五隻！ ✓":
            size 46 color "#1f6b1f" xalign 0.5 ypos 0.87
            outlines [(3, "#ffffff", 0, 0)]
        timer 1.3 action Return(True)


## 3. Lesson reward ------------------------------------------------------------

screen lesson_complete(stars=3, msg=""):
    modal True
    zorder 60
    add Solid("#000000aa")

    frame:
        xalign 0.5
        yalign 0.5
        background Frame(Solid("#fff8e8"), 40, 40)
        padding (90, 60)

        vbox:
            xalign 0.5
            spacing 22
            text "這一課學完了！" size 56 color "#c0392b" xalign 0.5
            if msg:
                text msg size 32 color "#6a5a3a" xalign 0.5
            hbox:
                xalign 0.5
                spacing 12
                for s in range(stars):
                    text "★" size 96 color "#f1c40f"
            textbutton "繼續 ▸":
                xalign 0.5
                text_size 38
                action Return(True)
