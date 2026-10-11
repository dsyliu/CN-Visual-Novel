# 0002 — English helper text is a setting; chants have voice

- Status: accepted
- Date: 2026-10-10

## Context

The story bible said English glosses were for the designer only, but Lesson 1
showed English under every line. Young readers (and their parents) may need the
English; stronger readers should be able to read Chinese only. This is a reading
game, so hearing each chant line read aloud also matters.

## Decision

**English is a player setting.** Preferences → 英文 English → Show English
(`persistent.show_english`, on by default).
- In any text, English goes inside a custom text tag: `"中文{en}\n(English){/en}"`.
  The tag (`core/english.rpy`) removes its contents when the setting is off.
- Screens with English as a separate element test `persistent.show_english`
  (the chant reader's gloss line, the counting game's hint, grade-card subtitles).
- Do not write English outside `{en}` in player-facing text.

**Chant lines have voice.** `call play_chant(title, lines, voice="<prefix>")`
plays `<prefix>_NN.ogg` (line N, 2 digits) on the voice channel as each line
comes up. Convention: `audio/gradeN/voice/lLL_C_NN.ogg` — lesson LL, chant C,
line NN, e.g. `audio/grade1/voice/l01_1_01.ogg`. Missing files are skipped.
Voice for ordinary dialogue is not decided yet.

## Consequences

- Every new lesson writes its glosses with `{en}` from the start.
- Ren'Py test selectors read text before custom tags run, so tests cannot check
  hidden English by searching the screen; they check the tag function instead.
- Voice can be produced later (recorded or TTS) and dropped in line by line,
  with no code change.
