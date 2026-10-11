# minigames/pick_one.rpy
# "Pick the right one" mini-game, shared by every grade.
# Each round shows a prompt with a blank (＿＿＿) and a row of big answer buttons.
# A wrong answer greys out and the player tries again (no penalty). The right
# answer fills the blank, plays the round's voice line, and the next round starts.
# First used by Grade 1 Lesson 2 (握握手: pick the action for each line).
#
# Usage:
#     call pick_one("bg g1_classroom", "握握手：選一選！", [
#         ("一二三，＿＿＿。", ["握握手", "點點頭", "大步走"], 0),   # (prompt, choices, answer)
#         ...
#     ], hint="Pick the words that finish each line.",
#        voice="audio/grade1/voice/l02_2", done_text="都對了！ ✓")
#
# voice="<prefix>": solving round N (1-based) plays <prefix>_NN.ogg. Pointing it at a
# chant's voice prefix replays that chant line, so no new voice files are needed.
# `hint` is English helper text: it shows only while Preferences → 英文 English is on.
# `hold` is how long the solved round stays on screen; keep it longer than the voice line.

define PICK_BLANK = "＿＿＿"

init python:

    def pick_right(voice, n):
        play_sfx("audio/sfx/sfx_correct.ogg")
        play_chant_line(voice, n)

    def pick_wrong():
        play_sfx("audio/sfx/sfx_try_again.ogg")

transform pick_wobble:
    xoffset 0
    linear 0.06 xoffset -14
    linear 0.06 xoffset 14
    linear 0.06 xoffset -8
    linear 0.06 xoffset 0

screen pick_one_screen(bg, title, rounds, hint="", voice=None, done_text="", hold=3.5):
    modal True
    zorder 50
    add bg
    add Solid("#00000044")

    default r = 0           # current round
    default wrong = [ ]     # wrong choices tried in this round
    default solved = False

    $ prompt, choices, answer = rounds[r]
    $ last = (r == len(rounds) - 1)

    vbox:
        xalign 0.5
        ypos 0.05
        spacing 6
        text title size 50 color "#fff3d6" xalign 0.5 outlines [(3, "#5a3a10", 0, 0)]
        if hint and persistent.show_english:
            text hint size 26 color "#fff3d6" xalign 0.5 outlines [(2, "#5a3a10", 0, 0)]

    # Progress: one dot per round.
    hbox:
        xalign 0.5
        ypos 0.2
        spacing 16
        for k in range(len(rounds)):
            text ("●" if k < r or (k == r and solved) else "○"):
                size 34 color "#ffd98a"

    frame:
        xalign 0.5
        ypos 0.3
        background Frame(Solid("#fff8e8"), 20, 20)
        padding (70, 36)
        text (prompt.replace(PICK_BLANK, choices[answer]) if solved else prompt):
            size 80 color ("#1f6b1f" if solved else "#3a2a14")

    hbox:
        xalign 0.5
        ypos 0.6
        spacing 50
        for j, c in enumerate(choices):
            button:
                id "pick_{}".format(j)
                xysize (400, 170)
                background Frame(Solid("#ffd98a"), 16, 16)
                hover_background Frame(Solid("#ffe9b8"), 16, 16)
                insensitive_background Frame(Solid(
                    "#9fd18b" if (solved and j == answer) else "#c8c2b4"), 16, 16)
                sensitive (not solved and j not in wrong)
                if j in wrong:
                    at pick_wobble
                action If(j == answer,
                          [SetScreenVariable("solved", True), Function(pick_right, voice, r + 1)],
                          [SetScreenVariable("wrong", wrong + [j]), Function(pick_wrong)])
                text c:
                    size 64 xalign 0.5 yalign 0.5
                    color ("#8a8478" if j in wrong else "#3a2a14")

    if solved:
        if last and done_text:
            text done_text:
                size 46 color "#1f6b1f" xalign 0.5 ypos 0.87
                outlines [(3, "#ffffff", 0, 0)]
        timer hold action If(last, Return(True),
                             [SetScreenVariable("r", r + 1), SetScreenVariable("wrong", [ ]),
                              SetScreenVariable("solved", False)])

label pick_one(bg, title, rounds, hint="", voice=None, done_text="", hold=3.5):
    call screen pick_one_screen(bg, title, rounds, hint, voice, done_text, hold)
    $ renpy.music.stop(channel="voice")
    return
