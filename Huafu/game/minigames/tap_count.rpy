# minigames/tap_count.rpy
# "Tap & count" mini-game, shared by every grade.
# Tokens sit on a background; the player taps each one and the running count is
# shown big in Chinese (一, 二, 三…). When every token is tapped, the game returns.
# First used by Grade 1 Lesson 1 (count the five squirrels on tiger mountain).
#
# Usage:
#     call tap_count("bg g1_mountain", "g1_squirrel_token",
#                    [(0.16, 0.46), (0.36, 0.66), ...],   # token centres (0–1)
#                    "上山找老虎：數一數松鼠！",
#                    hint="Tap each squirrel and count: 一 二 三 四 五",
#                    done_text="太棒了！松鼠有五隻！ ✓")

default tap_found = []   # token indices, in the order the player tapped them

init python:

    def tap_token(i, total):
        if i not in tap_found:
            tap_found.append(i)
            play_sfx("audio/sfx/sfx_tap.ogg")
            if len(tap_found) == total:
                play_sfx("audio/sfx/sfx_correct.ogg")

screen tap_count_screen(bg, token, positions, title, hint="", done_text="", hold=1.3):
    modal True
    zorder 50
    add bg

    $ total = len(positions)

    vbox:
        xalign 0.5
        ypos 0.05
        spacing 6
        text title size 50 color "#27431f" xalign 0.5
        if hint:
            text hint size 26 color "#3a5a30" xalign 0.5

    # Big running total in the centre-top.
    text cn_num(len(tap_found)):
        size 150 color "#e0962f"
        outlines [(5, "#5a3a10", 0, 0)]
        xpos 0.5 xanchor 0.5 ypos 0.17

    for i, pos in enumerate(positions):
        button:
            id "tap_{}".format(i)
            xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5
            action Function(tap_token, i, total)
            sensitive (i not in tap_found)
            vbox:
                spacing 2
                # tapped tokens fade out and show their count number
                if i in tap_found:
                    add token alpha 0.4
                    text cn_num(tap_found.index(i) + 1):
                        size 52 color "#ffe08a" xalign 0.5
                        outlines [(3, "#5a3a10", 0, 0)]
                else:
                    add token

    if len(tap_found) >= total:
        if done_text:
            text done_text:
                size 46 color "#1f6b1f" xalign 0.5 ypos 0.87
                outlines [(3, "#ffffff", 0, 0)]
        timer hold action Return(True)

label tap_count(bg, token, positions, title, hint="", done_text="", hold=1.3):
    $ tap_found = []
    call screen tap_count_screen(bg, token, positions, title, hint, done_text, hold)
    return
