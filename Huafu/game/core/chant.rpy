# core/chant.rpy
# 念一念 karaoke reader, shared by every lesson in every grade.
# Shows the whole chant; the line being read is large & bright, the rest dim.
# A full-screen click button advances one line at a time, then returns.
# A `voice` file can later be attached per line (see grade1/lesson01.rpy hooks).
#
# Usage:
#     call play_chant("第一課・上山找老虎", [
#         ("一二三四五，上山找老虎，", "English gloss"),
#         ...
#     ])

screen chant_screen(title, lines):
    modal True
    zorder 50

    default idx = 0

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

    text ("→ 點一下繼續 (tap to continue)" if idx < len(lines) - 1
          else "→ 點一下完成 (tap to finish)"):
        size 24 color "#ddddddcc" xalign 0.5 yalign 0.95

label play_chant(title, lines):
    call screen chant_screen(title, lines)
    return
