# core/reward.rpy
# Lesson-complete star card, shared by every lesson in every grade.
#
# Usage:
#     $ play_sfx("audio/sfx/sfx_star.ogg")
#     call screen lesson_complete(3, "你學會了：...")

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
            textbutton "繼續 →":
                id "lesson_continue"
                xalign 0.5
                text_size 38
                action Return(True)
