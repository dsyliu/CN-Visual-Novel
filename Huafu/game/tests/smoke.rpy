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
        # Main menu plays the theme (via play_bgm, so at the balanced volume).
        assert eval (renpy.music.get_playing("music") or "").endswith("theme_main.ogg") timeout 3.0
        click "Start"
        pause until screen "grade_select"
        assert eval not renpy.has_label("g2_start")   # Grade 2 card is "coming soon"
        click id "grade_g1"

        advance until "開學了"
        assert "The first day of school"
        # Dialogue voice (core/voice.rpy) plays with the line.
        assert eval (renpy.music.get_playing("voice") or "").endswith("g1_lesson01_9a41abed.ogg") timeout 3.0
        # While voice plays, the music dips (core/audio.rpy).
        assert eval renpy.audio.audio.get_channel("music").context.secondary_volume == config.emphasize_audio_volume timeout 3.0

        # L1.1 上山找老虎 — chant, then count the five squirrels.
        advance until screen "chant_screen"
        # Chant voice (core/chant.rpy) plays line 1.
        assert eval (renpy.music.get_playing("voice") or "").endswith("l01_1_01.ogg") timeout 3.0
        click id "chant_advance"
        assert eval (renpy.music.get_playing("voice") or "").endswith("l01_1_02.ogg") timeout 3.0
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
