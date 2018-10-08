from psychopy import visual
from lib.utils import proceedOrQuit

controlText = """\
Now you are about to begin the second practice trial.

This trial will be almost exactly the same as the last practice trial.
However, you will answer a few questions about each image on the screen.


Please take this moment to locate the SHIFT key on the keyboard.


When ready, press the SPACE key to begin the trial\
"""

def run(context):
    win = context['window']

    textStim = visual.TextStim(win, controlText, pos=[0, 0.3], height=0.06, wrapWidth=1.5)

    textStim.draw()
    win.flip()
    proceedOrQuit(win)

    return context
