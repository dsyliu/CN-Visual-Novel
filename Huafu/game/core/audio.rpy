# core/audio.rpy — background-music and sound-effect helpers, shared by every grade.
#
# Put music in  game/audio/bgm/  and sound effects in  game/audio/sfx/  as .ogg
# (preferred) or .mp3/.opus. Grade-specific audio (e.g. chant narration) goes in
# game/audio/gradeN/. play_bgm() only plays a track if the file actually exists,
# so the game runs fine BEFORE you've added any audio — drop the files in and they
# just start working, no code change needed.
#
# Music tracks (filenames are what the game looks for):
#   audio/bgm/theme_main.ogg   — title + main menu (gentle, inviting)
#   audio/bgm/bgm_gentle.ogg   — lonely / emotional beats (gate, classroom)
#   audio/bgm/bgm_magic.ogg    — the glowing book / library (curious, sparkly)
#   audio/bgm/bgm_playful.ogg  — book worlds + mini-games (upbeat, fun)
#
# Sound effects (one-shot, via play_sfx):
#   audio/sfx/sfx_tap.ogg      — tapping a token in a counting game
#   audio/sfx/sfx_correct.ogg  — counting game finished (success chime)
#   audio/sfx/sfx_page.ogg     — advancing a line in the 念一念 chant reader
#   audio/sfx/sfx_sparkle.ogg  — the magic book appears / glows
#   audio/sfx/sfx_star.ogg     — lesson-complete reward stars

init python:

    # Accept whichever audio format you actually saved — so "theme_main.mp3"
    # works even though the code asks for "theme_main.ogg".
    AUDIO_EXTS = [".ogg", ".opus", ".mp3", ".wav", ".flac"]

    def _find_audio(path):
        """Return a loadable audio path, trying common extensions. None if absent."""
        if renpy.loadable(path):
            return path
        base = path
        for ext in AUDIO_EXTS:
            if base.lower().endswith(ext):
                base = base[:-len(ext)]
                break
        for ext in AUDIO_EXTS:
            if renpy.loadable(base + ext):
                return base + ext
        return None

    def play_bgm(filename, fadein=1.0, fadeout=0.5):
        """Loop a music track on the 'music' channel — but only if it exists.
        Short fadeout so the previous track ends promptly with the scene change
        (no lingering overlap); short fadein so the new one isn't abrupt.
        Safe to call with no file yet."""
        f = _find_audio(filename)
        if f:
            renpy.music.play(f, channel="music",
                             loop=True, fadein=fadein, fadeout=fadeout)

    def play_sfx(filename):
        """Play a one-shot sound effect on the 'sound' channel, if it exists.
        Safe to call before the file has been added."""
        f = _find_audio(filename)
        if f:
            renpy.sound.play(f)

    # Use the main theme on the title screen / main menu, only if present
    # (guarded so a missing file never crashes the menu).
    _mm = _find_audio("audio/bgm/theme_main.ogg")
    if _mm:
        config.main_menu_music = _mm

    # ── BGM pre-queue ─────────────────────────────────────────────────────────
    # Call  $ prequeue_bgm("audio/x.ogg")  ONE SCENE BEFORE the scene that plays
    # it. It warms just that track's file cache in a background thread (off the
    # main thread, non-blocking), so by the time play_bgm() actually starts it
    # there's no disk-load hitch — and nothing loads until it's about to be
    # needed (not everything at game start).
    # The web build can't start threads, so there this does nothing; the
    # browser fetches the track when play_bgm() asks for it.
    import threading as _threading

    def prequeue_bgm(filename):
        if renpy.emscripten:
            return
        f = _find_audio(filename)
        if not f:
            return
        def _warm():
            try:
                with renpy.open_file(f) as fh:
                    fh.read()       # pull the bytes into the OS cache, ready to play
            except Exception:
                pass
        _threading.Thread(target=_warm, daemon=True).start()
