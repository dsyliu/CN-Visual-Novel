# tests/smoke.rpy
# Automated smoke test: main menu -> grade select -> Grade 1 -> Lesson 1 to the end.
# Only runs from the test command; it does nothing in normal play.
#
# Run from the Ren'Py SDK folder:
#     renpy.exe <path-to>/Huafu test smoke

testsuite smoke:

    teardown:
        exit

    testcase g1_lesson01:
        description "Start -> 第一冊 -> play Lesson 1 through the reward card."

        pause until screen "main_menu"
        click "Start"
        pause until screen "grade_select"
        assert eval not renpy.has_label("g2_start")   # Grade 2 card is "coming soon"
        click id "grade_g1"

        # L1.1 上山找老虎 — chant, then count the five squirrels.
        advance until screen "chant_screen"
        click id "chant_advance" until not screen "chant_screen"
        advance until screen "tap_count_screen"
        click id "tap_0"
        click id "tap_1"
        click id "tap_2"
        click id "tap_3"
        click id "tap_4"
        pause until not screen "tap_count_screen"

        # L1.2 我的朋友在哪裡 — chant, then the reward card.
        advance until screen "chant_screen"
        click id "chant_advance" until not screen "chant_screen"
        advance until screen "lesson_complete"
        click id "lesson_continue"
        pause until screen "main_menu"
