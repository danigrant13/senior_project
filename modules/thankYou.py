from psychopy import visual
from lib.utils import proceedOrQuit

thankYou = "Thank you for taking part in this experiment!"
spaceBar = "When you are ready, press the SPACE key to close the program."

def run(context):
    win = context['window']

    thankYouStim = visual.TextStim(win, thankYou, pos=[0, 0.1], height=0.10, wrapWidth=1.5)
    spaceBarStim = visual.TextStim(win, spaceBar, pos=[0, -0.6], height=0.06, wrapWidth=1.5)

    thankYouStim.draw()
    spaceBarStim.draw()
    win.flip()
    proceedOrQuit(win)

    return context
