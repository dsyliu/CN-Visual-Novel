# core/grades.rpy
# The list of grades, the grade-select screen, and the lesson-select screen.
# The main menu's Start button opens grade_select (see `navigation` in screens.rpy).
# A grade card opens lesson_select for that grade; a lesson card starts the game there.
#
# To add a grade: add an entry to GRADES, then create gradeN/main.rpy with
# `label gN_start` and `define gN_lessons` (see grade1/main.rpy). The card becomes
# playable as soon as that label exists; until then it shows 即將推出 (coming soon).

define GRADES = [
    {"id": "g1", "title": "第一冊", "subtitle": "Grade 1", "label": "g1_start"},
    {"id": "g2", "title": "第二冊", "subtitle": "Grade 2", "label": "g2_start"},
]

init python:

    def grade_lessons(g):
        """The lesson list of grade g (its gradeN/main.rpy defines `<id>_lessons`)."""
        return getattr(store, g["id"] + "_lessons", [])

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
                    action ShowMenu("lesson_select", g)
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

# One card per lesson. A lesson is playable when its label exists; the game
# starts at that lesson and goes on through the later lessons.
screen lesson_select(g):

    tag menu

    use game_menu(g["title"] + "・" + _("選一課")):

        vbox:
            spacing 20

            textbutton "← 選擇年級{en} (grades){/en}":
                id "back_to_grades"
                text_size 32
                action ShowMenu("grade_select")

            vpgrid:
                cols 4
                spacing 24
                ysize 740
                draggable True
                mousewheel True
                scrollbars "vertical"

                for i, l in enumerate(grade_lessons(g)):
                    $ ready = renpy.has_label(l["label"])

                    button:
                        id "lesson_{:02d}".format(i + 1)
                        xysize (318, 260)
                        background Frame(Solid("#fff8e8"), 20, 20)
                        hover_background Frame(Solid("#ffe9b8"), 20, 20)
                        insensitive_background Frame(Solid("#d8d2c4"), 20, 20)
                        action Start(l["label"])
                        sensitive ready

                        fixed:
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 6
                                text l["title"]:
                                    size 52 xalign 0.5
                                    color ("#c0392b" if ready else "#8a8478")
                                if persistent.show_english:
                                    text l["subtitle"]:
                                        size 24 xalign 0.5
                                        color ("#6a5a3a" if ready else "#8a8478")
                                for c in l["chants"]:
                                    text c:
                                        size 28 xalign 0.5
                                        color ("#3a3020" if ready else "#8a8478")
                            # Not built yet: a small tag in the top corner.
                            if not ready:
                                text "即將推出" size 20 color "#8a8478" xalign 1.0 yalign 0.0 xoffset -10 yoffset 6
