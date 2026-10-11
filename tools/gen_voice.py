"""Generate voice files for the game with text-to-speech (edge-tts).

Makes one .ogg per line:
  - dialogue: audio/gradeN/voice/dialogue/<line id>.ogg   (played by core/voice.rpy)
  - chants:   <voice prefix>_NN.ogg from each `call play_chant(..., voice="...")`
              (played by core/chant.rpy)
  - words:    <voice prefix>_NN.ogg from each `labels=[...], voice="..."` (e.g. the
              fruit names in a tap_count call; played by minigames/tap_count.rpy)

English inside {en}...{/en} and other text tags are not spoken. A line is only
regenerated when its text or voice settings change (tools/voice_manifest.json).
Dialogue files whose line no longer exists are deleted.

Usage:  python tools/gen_voice.py            (generate what changed)
        python tools/gen_voice.py --force    (regenerate everything)
        python tools/gen_voice.py --dry-run  (only list what would change)
Needs:  pip install edge-tts imageio-ffmpeg
        Ren'Py SDK (set RENPY to renpy.exe if it is not at the default path)

Note: edge-tts uses Microsoft Edge's online read-aloud service, which is not an
official API. The same voices are available officially (with a free tier) from
Azure AI Speech, if the game needs a clear license later.
"""

import argparse
import asyncio
import csv
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

import edge_tts
import imageio_ffmpeg

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROJECT = ROOT / "Huafu"
GAME = PROJECT / "game"
MANIFEST = ROOT / "tools" / "voice_manifest.json"
RENPY = os.environ.get("RENPY", r"C:\Users\dsyli\Downloads\renpy-8.5.3-sdk\renpy.exe")

# Who speaks with which voice. Keys are Character variable names from
# core/characters.rpy, plus "chant" for the 念一念 reader and "word" for single
# words in mini-games.
# Listen in the game and adjust; changed settings regenerate that speaker's lines.
VOICES = {
    "narrator": {"voice": "zh-TW-HsiaoChenNeural", "rate": "-10%", "pitch": "+0Hz"},
    "chant":    {"voice": "zh-TW-HsiaoChenNeural", "rate": "-25%", "pitch": "+0Hz"},
    "word":     {"voice": "zh-TW-HsiaoChenNeural", "rate": "-15%", "pitch": "+0Hz"},
    "mc":       {"voice": "zh-CN-YunxiaNeural",    "rate": "-5%",  "pitch": "+0Hz"},
    "mc_think": {"voice": "zh-CN-YunxiaNeural",    "rate": "-10%", "pitch": "+0Hz"},
    "yo":       {"voice": "zh-CN-YunxiNeural",     "rate": "+5%",  "pitch": "+25Hz"},
    "zh":       {"voice": "zh-TW-YunJheNeural",    "rate": "-5%",  "pitch": "+30Hz"},
    "wu":       {"voice": "zh-CN-XiaoyiNeural",    "rate": "+0%",  "pitch": "+15Hz"},
    "teacher":  {"voice": "zh-TW-HsiaoYuNeural",   "rate": "-5%",  "pitch": "+0Hz"},
}

# Characters that never get voice (title cards etc.).
SILENT = {"centered"}

CJK = re.compile(r"[\u3400-\u9fff\u3100-\u312f]")


def clean(text):
    """The part of a line that should be spoken."""
    text = re.sub(r"\{en\}.*?\{/en\}", "", text, flags=re.S)
    text = re.sub(r"\{[^{}]*\}", "", text)
    text = text.replace("\\n", "").replace("\n", "")
    return text.strip()


def dialogue_jobs():
    """Export the dialogue table from Ren'Py and turn it into jobs."""
    subprocess.run([RENPY, str(PROJECT), "dialogue", "None"], check=True)
    jobs = {}
    with open(PROJECT / "dialogue.tab", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
            who, tlid = row["Character"], row["Identifier"]
            if who in SILENT:
                continue
            if who not in VOICES:
                raise SystemExit(f"No voice set for character '{who}' (line {tlid}). Add it to VOICES.")
            text = clean(row["Dialogue"])
            if not CJK.search(text):
                continue
            m = re.match(r"g(\d+)_", tlid)
            folder = f"audio/grade{m.group(1)}/voice/dialogue" if m else "audio/voice/dialogue"
            jobs[f"{folder}/{tlid}.ogg"] = (text, VOICES[who])
    return jobs


CHANT_CALL = re.compile(r"call\s+play_chant\((.*?)\]\s*,\s*voice\s*=\s*\"([^\"]+)\"\s*\)", re.S)
CHANT_LINE = re.compile(r"\(\s*\"([^\"]*)\"\s*,\s*\"[^\"]*\"\s*\)")


def chant_jobs():
    """Find every play_chant call that has a voice prefix."""
    jobs = {}
    for path in GAME.rglob("*.rpy"):
        for m in CHANT_CALL.finditer(path.read_text(encoding="utf-8")):
            body, prefix = m.groups()
            for n, line in enumerate(CHANT_LINE.findall(body), start=1):
                text = clean(line)
                if CJK.search(text):
                    jobs[f"{prefix}_{n:02d}.ogg"] = (text, VOICES["chant"])
    return jobs


WORD_LIST = re.compile(r"labels\s*=\s*\[(.*?)\]\s*,\s*voice\s*=\s*\"([^\"]+)\"", re.S)
WORD = re.compile(r"\"([^\"]*)\"")


def word_jobs():
    """Find every `labels=[...], voice="..."` word list (mini-game words)."""
    jobs = {}
    for path in GAME.rglob("*.rpy"):
        for m in WORD_LIST.finditer(path.read_text(encoding="utf-8")):
            body, prefix = m.groups()
            for n, word in enumerate(WORD.findall(body), start=1):
                text = clean(word)
                if CJK.search(text):
                    jobs[f"{prefix}_{n:02d}.ogg"] = (text, VOICES["word"])
    return jobs


def key(text, voice):
    return hashlib.sha1(json.dumps([text, voice], ensure_ascii=False, sort_keys=True).encode()).hexdigest()


async def synth(rel, text, voice, sem):
    out = GAME / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    async with sem:
        with tempfile.TemporaryDirectory() as tmp:
            mp3 = pathlib.Path(tmp) / "line.mp3"
            try:
                await edge_tts.Communicate(text, voice["voice"], rate=voice["rate"], pitch=voice["pitch"]).save(str(mp3))
            except edge_tts.exceptions.EdgeTTSException as e:
                print(f"  FAILED {rel}  {text}  ({type(e).__name__})")
                return False
            subprocess.run(
                [imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y", "-i", str(mp3),
                 "-af", "silenceremove=start_periods=1:start_threshold=-50dB",
                 "-ac", "1", "-c:a", "libvorbis", "-q:a", "4", str(out)],
                check=True,
            )
    print(f"  {rel}  {text}")
    return True


async def main():
    sys.stdout.reconfigure(encoding="utf-8")   # Chinese text on a Windows console
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    jobs = {**dialogue_jobs(), **chant_jobs(), **word_jobs()}
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}

    todo = {rel: job for rel, job in jobs.items()
            if args.force or manifest.get(rel) != key(*job) or not (GAME / rel).exists()}
    stale = [rel for rel in manifest if rel not in jobs]

    print(f"{len(jobs)} lines, {len(todo)} to generate, {len(stale)} to delete")
    if args.dry_run:
        for rel in todo:
            print("  +", rel, jobs[rel][0])
        for rel in stale:
            print("  -", rel)
        return

    sem = asyncio.Semaphore(4)
    done = await asyncio.gather(*(synth(rel, text, voice, sem) for rel, (text, voice) in todo.items()))
    failed = {rel for rel, ok in zip(todo, done) if not ok}
    for rel in stale:
        (GAME / rel).unlink(missing_ok=True)
        print(f"  deleted {rel}")

    MANIFEST.write_text(
        json.dumps({rel: key(*job) for rel, job in sorted(jobs.items()) if rel not in failed},
                   indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if failed:
        raise SystemExit(f"{len(failed)} line(s) failed (see FAILED above). Run again to retry them.")


if __name__ == "__main__":
    asyncio.run(main())
