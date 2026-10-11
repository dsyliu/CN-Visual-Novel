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
#
# Options:
#   token     one image name for all tokens, or a list with one image per token.
#   labels    a list with one word per token (e.g. fruit names). A tapped token
#             shows its word. Without labels, it shows its count number.
#   voice     "<prefix>": tapping token N (1-based, list order) plays <prefix>_NN.ogg
#             on the voice channel. With labels, tools/gen_voice.py makes these
#             files from the labels — write `labels=[...]` and then `voice="..."`.
#   drop      True: tokens fall in from the top, one after another.
#
# `hint` is English helper text: it shows only while Preferences → 英文 English is on.
# Layout: the title and the big count number fill the top of the screen down to
# about y=0.35, and done_text sits at y=0.87. Keep each token's centre between
# y=0.45 and y=0.75 so nothing overlaps. With two rows, keep the rows about 0.24
# apart (a token plus its word is about 210px tall).

default tap_found = []   # token indices, in the order the player tapped them

init python:

    def tap_token(i, total, voice=None):
        if i not in tap_found:
            tap_found.append(i)
            play_sfx("audio/sfx/sfx_tap.ogg")
            if voice:
                f = _find_audio("{}_{:02d}.ogg".format(voice, i + 1))
                if f:
                    renpy.music.play(f, channel="voice", loop=False)
            if len(tap_found) == total:
                play_sfx("audio/sfx/sfx_correct.ogg")

transform tap_drop(delay):
    yoffset -1100
    pause delay
    easein_bounce 0.7 yoffset 0

screen tap_count_screen(bg, token, positions, title, hint="", done_text="", hold=1.3,
                        labels=None, voice=None, drop=False):
    modal True
    zorder 50
    add bg

    $ total = len(positions)

    vbox:
        xalign 0.5
        ypos 0.05
        spacing 6
        text title size 50 color "#27431f" xalign 0.5
        if hint and persistent.show_english:
            text hint size 26 color "#3a5a30" xalign 0.5

    # Big running total in the centre-top.
    text cn_num(len(tap_found)):
        size 150 color "#e0962f"
        outlines [(5, "#5a3a10", 0, 0)]
        xpos 0.5 xanchor 0.5 ypos 0.17

    for i, pos in enumerate(positions):
        $ tok = token[i] if isinstance(token, (list, tuple)) else token
        $ tapped = i in tap_found
        button:
            id "tap_{}".format(i)
            xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5
            action Function(tap_token, i, total, voice)
            sensitive (not tapped)
            if drop:
                at tap_drop(0.15 * i)
            vbox:
                spacing 2
                # Tapped tokens fade out and show their word or count number.
                # The text line is always there, so the token does not move.
                add tok alpha (0.4 if tapped else 1.0) xalign 0.5
                if tapped:
                    text (labels[i] if labels else cn_num(tap_found.index(i) + 1)):
                        size 52 color "#ffe08a" xalign 0.5
                        outlines [(3, "#5a3a10", 0, 0)]
                else:
                    text " " size 52

    if len(tap_found) >= total:
        if done_text:
            text done_text:
                size 46 color "#1f6b1f" xalign 0.5 ypos 0.87
                outlines [(3, "#ffffff", 0, 0)]
        timer hold action Return(True)

label tap_count(bg, token, positions, title, hint="", done_text="", hold=1.3,
                labels=None, voice=None, drop=False):
    $ tap_found = []
    call screen tap_count_screen(bg, token, positions, title, hint, done_text, hold,
                                 labels, voice, drop)
    return
