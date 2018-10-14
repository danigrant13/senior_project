from psychopy import visual
from lib.utils import proceedOrQuit

introText = """\
Now you are about to begin the main experiment.

Please take this moment to locate the SHIFT key on the keyboard.

When ready, press the SPACE key to begin the trial\
"""

def run(context):
    win = context['window']

    textStim = visual.TextStim(win, introText, pos=[0, 0.3], height=0.06, wrapWidth=1.5)

    textStim.draw()
    win.flip()
    proceedOrQuit(win)

    return context
