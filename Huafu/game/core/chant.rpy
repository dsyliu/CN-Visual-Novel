# core/chant.rpy
# 念一念 karaoke reader, shared by every lesson in every grade.
# Shows the whole chant; the line being read is large & bright, the rest dim.
# A full-screen click button advances one line at a time, then returns.
#
# Usage:
#     call play_chant("第一課・上山找老虎", [
#         ("一二三四五，上山找老虎，", "English gloss"),
#         ...
#     ], voice="audio/grade1/voice/l01_1")
#
# English glosses show only while Preferences → 英文 English is on (core/english.rpy).
#
# Voice (optional): with voice="<prefix>", line N plays <prefix>_NN.ogg
# (e.g. audio/grade1/voice/l01_1_01.ogg for line 1) on the voice channel when the
# line comes up. Missing files are skipped, so voice can be added line by line.
# Any extension that core/audio.rpy accepts works (.ogg, .opus, .mp3, …).

init python:

    def play_chant_line(voice, n):
        """Play the voice file for chant line n (1-based), if it exists."""
        if not voice:
            return
        f = _find_audio("{}_{:02d}.ogg".format(voice, n))
        if f:
            renpy.music.play(f, channel="voice", loop=False)

screen chant_screen(title, lines, voice=None):
    modal True
    zorder 50

    default idx = 0

    on "show" action Function(play_chant_line, voice, 1)

    # Full-screen click-to-advance. The frame/text below are non-focusable, so
    # clicks anywhere fall through to this button.
    button:
        id "chant_advance"
        xfill True
        yfill True
        background "#000000aa"
        padding (0, 0)
        action [Function(play_sfx, "audio/sfx/sfx_page.ogg"),
                If(idx < len(lines) - 1,
                   [SetScreenVariable("idx", idx + 1),
                    Function(play_chant_line, voice, idx + 2)],
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
                    if i == idx and line[1] and persistent.show_english:
                        text line[1] size 26 color "#9a8d76" xalign 0.5

    text ("→ 點一下繼續{en} (tap to continue){/en}" if idx < len(lines) - 1
          else "→ 點一下完成{en} (tap to finish){/en}"):
        size 24 color "#ddddddcc" xalign 0.5 yalign 0.95

label play_chant(title, lines, voice=None):
    call screen chant_screen(title, lines, voice)
    $ renpy.music.stop(channel="voice")
    return
