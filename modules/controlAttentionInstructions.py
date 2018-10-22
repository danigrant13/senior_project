from psychopy import visual
from lib.utils import proceedOrQuit

controlText1 = "You will now begin the 2nd Practice Trial"

controlText2 = """
Your task for the 2nd practice trial is the same as it was during the \
1st practice trial, except it will be somewhat longer. It will take a total of two minutes to complete.
"""

controlText3 = """
In addition, you will answer a few more questions about each image on the screen.

Please take a moment to locate the SHIFT key.
"""

spaceText = "Press the SPACE key to advance to the the 2nd Practice Trial"

def run(context):
    win = context['window']

    controlStim1 = visual.TextStim(win, controlText1, pos=[0, 0.5], height=0.06, wrapWidth=1.5)
    controlStim2 = visual.TextStim(win, controlText2, pos=[0, 0.2], height=0.06, wrapWidth=1.5)
    controlStim3 = visual.TextStim(win, controlText3, pos=[0, -0.1], height=0.06, wrapWidth=1.5)
    spaceTextStim = visual.TextStim(win, spaceText, pos=[0, -0.8], height=0.06, wrapWidth=1.5)

    controlStim1.draw()
    controlStim2.draw()
    controlStim3.draw()
    spaceTextStim.draw()
    win.flip()
    proceedOrQuit(win)

    return context
