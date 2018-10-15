from psychopy import visual
from lib.utils import proceedOrQuit

screen5Text = """
                        You will now complete two PRACTICE trials.

The purpose of these practice trials is to help you become familiar with the experimental \
procedure. After the practice trials you will begin the main experimental trial.

Remember your two tasks:

    1. Press the SHIFT key when the letter in the center of the screen is a 
        VOWEL.

    2. Keep track of how many times any image changes over the course of 
        the trial.
"""
practiceText1 = """\
About to begin practice trial

Please take this moment to locate the SHIFT key on the keyboard.
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

    textStim1 = visual.TextStim(win, practiceText1, pos=[0, 0], height=0.06, wrapWidth=1.5)
    textStim2 = visual.TextStim(win, practiceText2, pos=[0, -0.9], height=0.06, wrapWidth=1.5)

    textStim1.draw()
    textStim2.draw()
    win.flip()
    proceedOrQuit(win)

    return context
