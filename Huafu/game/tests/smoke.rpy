# tests/smoke.rpy
# Automated smoke tests. Only run from the test command; they do nothing in normal play.
#
# Run from the Ren'Py SDK folder:
#     renpy.exe <path-to>/Huafu test smoke

testsuite smoke:

    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    after testcase:
        # Leave the player's English setting at its default.
        run SetField(persistent, "show_english", True)

    teardown:
        exit

    testcase g1_lesson01:
        description "Start -> 第一冊 -> play Lesson 1 through the reward card (English on)."

        run SetField(persistent, "show_english", True)
        click "Start"
        pause until screen "grade_select"
        assert eval not renpy.has_label("g2_start")   # Grade 2 card is "coming soon"
        click id "grade_g1"

        advance until "開學了"
        assert "The first day of school"

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

    testcase english_off:
        description "With English off, dialogue shows only the Chinese."

        run SetField(persistent, "show_english", False)
        click "Start"
        pause until screen "grade_select"
        click id "grade_g1"

        advance until "開學了"
        # Test selectors read text before custom tags run, so check the {en} tag itself.
        assert eval _en_tag("en", None, [ "x" ]) == [ ]
