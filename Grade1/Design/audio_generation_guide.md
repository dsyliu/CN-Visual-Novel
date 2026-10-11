# Audio Generation Guide — Music & SFX

How to produce the game's audio and where it goes. Music = **Suno** (online);
SFX = free CC0 libraries. All files drop into `Grade1/game/audio/`.

> The in-game loader (`audio.rpy`) accepts **.ogg / .mp3 / .wav / .opus / .flac**
> and only plays a track if the file exists — so add them in any order, any of
> those formats, named by the **base names** below (extension doesn't matter).

---

## MUSIC — Suno (https://suno.com)

### Workflow
1. **Custom Mode.**
2. **Toggle "Instrumental" ON** ← critical (no vocals under dialogue).
3. Paste a prompt below into the **Style** box; leave the lyrics box empty.
4. Generate → pick the better of the 2 takes → **Download → MP3**.
5. Rename to the base name and drop into `Grade1/game/audio/`.

### The 4 tracks

**`theme_main`** — title screen / main menu (warm welcome)
```
gentle warm children's storybook theme, soft piano, glockenspiel, light pizzicato
strings, magical wonder, cozy and inviting, instrumental, slow 80 bpm, loopable
```

**`bgm_gentle`** — lonely first day / wistful classroom
```
tender wistful solo piano with soft strings, gentle and a little lonely but hopeful,
slow and emotional, children's film score, instrumental, 70 bpm, loopable
```

**`bgm_magic`** — the glowing book / library
```
whimsical curious music, twinkling celesta and music box, light harp glissando,
sense of wonder and discovery, sparkly, instrumental, medium 90 bpm, loopable
```

**`bgm_playful`** — mountain world + counting game
```
cheerful bouncy children's game music, playful xylophone and pizzicato strings,
light hand percussion, fun and energetic, instrumental, upbeat 110 bpm, loopable
```

### Where each plays (already wired in the game)
| Track | Scene |
|---|---|
| theme_main | title card + main menu |
| bgm_gentle | gate opening (lonely) + classroom 我的朋友在哪裡 (wistful) |
| bgm_magic | library / glowing book |
| bgm_playful | mountain world + squirrel counting game |

---

## SFX — free CC0 libraries (NOT Suno)

Suno makes songs, not short blips. Grab one-shot effects from:
- **Kenney.nl** (free game SFX packs — ideal for UI/tap/success)
- **Pixabay** (sound effects), **Freesound.org** (filter to CC0), **Mixkit**

### The 5 effects (base names + what to search)
| Base name | Plays when | Search terms |
|---|---|---|
| `sfx_tap` | tapping a squirrel | "pop", "bubble", "soft click", "blip" |
| `sfx_correct` | all five squirrels found | "success", "correct", "kids win chime" |
| `sfx_page` | advancing a chant line | "page turn", "paper flip" |
| `sfx_sparkle` | the magic book appears | "sparkle", "magic shimmer", "twinkle" |
| `sfx_star` | lesson-complete stars | "reward", "star ding", "level complete" |

Keep them short (well under 1s for tap; 1–2s for chimes). `.ogg` or `.wav` both fine.

---

## ⚠️ Licensing — read before building all audio on this

- **Suno free tier = non-commercial.** This game is educational and may be
  distributed/sold → use a **paid Suno plan (Pro/Premier)** for commercial rights,
  or swap to royalty-free music (Pixabay, incompetech CC-BY, Free Music Archive).
- **SFX:** prefer **CC0** (no attribution needed). CC-BY is fine but you must
  credit creators in the game's credits.

---

## Looping (optional polish)

Suno tracks are ~2 min songs, not seamless loops. Ren'Py loops the whole file, so
a small seam may be audible on restart (usually fine for ambient BGM). To make a
clean loop: open in **Audacity** (free), find a musical phrase boundary, trim
start/end to matching points, export. Ask and I'll give exact Audacity steps.

---

## Volume balancing

SFX often come louder than music. If needed, per-sound volume can be set in
`audio.rpy` (e.g. `renpy.sound.play(f, volume=0.6)`). Tell me which are too loud.

---

## Quick test
Generate **`theme_main`** first, drop the MP3 in `game/audio/`, relaunch → it
should play on the title screen. If that works, the whole pipeline works; add the
rest at your own pace.
