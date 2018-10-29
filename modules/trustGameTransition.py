from psychopy import visual
from lib.utils import proceedOrQuit

pressSpace = "Press the SPACE key to continue."

transitionText = """
You have finished Task #1!

  Next you will do Task #2.
"""

page1 = """                    For Task #2, there are two roles: First Mover & Second Mover.



        1. You will be the First Mover.

        2. The four previous participants will be Second Movers.

        3. Any money you choose to send to the other participants will be multiplied 
            by three. They will be given the opportunity to send you money back if they 
            wish.

        4. You can distribute your $5.00 however you would like, including keeping some 
            or all of it.

"""

def run(context):
    win = context['window']
    pressSpaceStim = visual.TextStim(win, pressSpace, height=0.06, pos=[0, -0.8], wrapWidth=1.7)
    pages = [
        [
            pressSpaceStim,
            visual.TextStim(win, transitionText, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, page1, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ],
    ]
    for page in pages:
        for stim in page:
            stim.draw()
        win.flip()
        proceedOrQuit(win)

    return context
