# core/english.rpy
# English helper text that players (or parents) can turn on and off in
# Preferences → 英文 English. Shared by every grade.
#
# In any text — dialogue, narration, screens — wrap the English part in {en}...{/en}:
#
#     mc "這是什麼書？{en}\n(What book is this?){/en}"
#
# When the setting is off, everything inside the tag disappears (put the "\n"
# inside the tag so no blank line is left behind). In screens, English that is a
# separate text element can test `persistent.show_english` directly.

# On by default: Grade 1 readers may need the help. Players can turn it off.
default persistent.show_english = True

init python:

    def _en_tag(tag, argument, contents):
        """{en}...{/en}: keep the contents only while English is shown."""
        return contents if persistent.show_english else [ ]

    config.custom_text_tags["en"] = _en_tag
