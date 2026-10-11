# core/voice.rpy
# Automatic voice for dialogue, shared by every grade.
#
# Every say line has a Ren'Py identifier: <label>_<hash>, e.g. g1_lesson01_5d3f1e2a.
# If a file named after that identifier exists, it plays with the line:
#     lines under a gN_ label -> audio/gradeN/voice/dialogue/<id>.ogg
#     anything else           -> audio/voice/dialogue/<id>.ogg
# The identifier changes when the line's text changes, so edited lines go silent
# until their voice is generated again (tools/gen_voice.py).
#
# Chant voice is separate: see core/chant.rpy.

init python:

    import re as _re

    def _auto_voice(tlid):
        m = _re.match(r"g(\d+)_", tlid)
        if m:
            return "audio/grade{}/voice/dialogue/{}.ogg".format(m.group(1), tlid)
        return "audio/voice/dialogue/{}.ogg".format(tlid)

    config.auto_voice = _auto_voice
