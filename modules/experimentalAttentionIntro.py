from psychopy import visual
from lib.utils import proceedOrQuit

introText = """





        You are now about to begin the experimental trial.



            Take this moment to locate the SHIFT key.


















                When ready, press the SPACE key to begin.
"""

def run(context):
    win = context['window']

    textStim = visual.TextStim(win, introText, pos=[0, 0.3], height=0.06, wrapWidth=1.5)

    textStim.draw()
    win.flip()
    proceedOrQuit(win)

    return context
