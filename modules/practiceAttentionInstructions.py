from psychopy import visual
from lib.utils import proceedOrQuit

screen5Text = """
        You will now complete two PRACTICE trials for Trial #1.



These will get you familiar with the experimental procedure.
After the practice trials, you will begin the main experiment tiral.


Remember your two tasks:

    1. Press the SHIFT key when a VOWEL is at the center of the screen
    2. Keep count of how many times any image changes during each trial
"""

practiceText1 = """\
You are about to begin the first practice trial.

Take a moment to locate the SHIFT key.
"""

practiceText2 = "When ready, press the SPACE key to begin the trial"

# instruction screen 5
def screen5(win, textStim):
    pressSpaceStim = visual.TextStim(win, practiceText2, height=0.06, pos=[0, -0.7], wrapWidth=1.7)
    textStim.setText(screen5Text)
    textStim.draw()
    pressSpaceStim.draw()
    win.flip()

def run(context):
    win = context['window']

    screen5 = visual.TextStim(win, screen5Text, pos=[0, 0.3], height=0.06, wrapWidth=1.5)
    pressSpaceStim = visual.TextStim(win, practiceText2, height=0.06, pos=[0, -0.7], wrapWidth=1.7)

    screen5.draw()
    pressSpaceStim.draw()
    win.flip()
    proceedOrQuit(win)

    textStim1 = visual.TextStim(win, practiceText1, pos=[0, 0], height=0.06, wrapWidth=1.5)
    textStim2 = visual.TextStim(win, practiceText2, pos=[0, -0.9], height=0.06, wrapWidth=1.5)

    textStim1.draw()
    textStim2.draw()
    win.flip()
    proceedOrQuit(win)

    return context
