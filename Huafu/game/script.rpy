# script.rpy — game entry point.
#
# Layout:
#   core/        shared by every grade: characters, images, audio, chant reader, reward card
#   minigames/   shared, configurable mini-games
#   gradeN/      one folder per grade: images.rpy, main.rpy (label gN_start), lessonNN.rpy
#
# The main menu's Start button opens the grade-select screen (core/grades.rpy),
# which starts a grade at its gN_start label. Everything specific to a grade is
# prefixed with gN_ because Ren'Py labels, screens, and images are global.

# Fallback for anything that starts the game without choosing a grade
# (e.g. Start() with no label). Goes straight to Grade 1.
label start:
    jump g1_start
