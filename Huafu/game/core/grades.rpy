# core/grades.rpy
# The list of grades and the grade-select screen.
# The main menu's Start button opens this screen (see `navigation` in screens.rpy).
#
# To add a grade: add an entry to GRADES, then create gradeN/main.rpy with
# `label gN_start`. The card becomes playable as soon as that label exists;
# until then it shows 即將推出 (coming soon).

define GRADES = [
    {"id": "g1", "title": "第一冊", "subtitle": "Grade 1", "label": "g1_start"},
    {"id": "g2", "title": "第二冊", "subtitle": "Grade 2", "label": "g2_start"},
]

screen grade_select():

    tag menu

    use game_menu(_("選擇年級")):

        hbox:
            xalign 0.5
            yalign 0.4
            spacing 50

            for g in GRADES:
                $ ready = renpy.has_label(g["label"])

                button:
                    id "grade_" + g["id"]
                    xysize (380, 440)
                    background Frame(Solid("#fff8e8"), 20, 20)
                    hover_background Frame(Solid("#ffe9b8"), 20, 20)
                    insensitive_background Frame(Solid("#d8d2c4"), 20, 20)
                    action Start(g["label"])
                    sensitive ready

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 18
                        text g["title"]:
                            size 80 xalign 0.5
                            color ("#c0392b" if ready else "#8a8478")
                        if persistent.show_english:
                            text g["subtitle"]:
                                size 32 xalign 0.5
                                color ("#6a5a3a" if ready else "#8a8478")
                        if not ready:
                            text "即將推出{en}\n(coming soon){/en}":
                                size 28 xalign 0.5 text_align 0.5
                                color "#8a8478"
