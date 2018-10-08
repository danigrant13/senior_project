from psychopy import visual
from lib.utils import proceedOrQuit

practiceText1 = """\
About to begin practice trial

Please take this moment to locate the SHIFT key on the keyboard.
"""

practiceText2 = "When ready, press the SPACE key to begin the trial"

def run(context):
    win = context['window']

    textStim1 = visual.TextStim(win, practiceText1, pos=[0, 0], height=0.06, wrapWidth=1.5)
    textStim2 = visual.TextStim(win, practiceText2, pos=[0, -0.9], height=0.06, wrapWidth=1.5)

    textStim1.draw()
    textStim2.draw()
    win.flip()
    proceedOrQuit(win)

    return context
