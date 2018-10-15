from psychopy import visual
from lib.utils import proceedOrQuit

pressSpace = "Press the SPACE key to continue reading the instructions."

transitionText = """
Thank you for playing Game #1

Next you will play Game #2.
"""

page1Section1 = """
You are going to play Game #2 with the previous participants \
that may proceed in a future study session later this semester.
"""

page1Section2 = """
Remember, in the game, there are two roles that will be randomly assigned:
"""

page1Section3 = "First Mover & Second Mover"

page2Section1 = """
Remember,
Role of the First Mover:
"""

page2Section2 = """
1. The First Mover chooses which participant they want to play the trust game with

2. The First Mover is given the opportunity to give as little as $0.00 or as much as \
$5.00, or any amount in between (in $0.25 increments), to the chosen participant.

3. The money given to the chosen participant will be multiplied by 3 and placed \
in the chosen participant's account
"""

page3Section1 = """
Remember,
Role of the Second Mover:
"""

page3Section2 = """
1. Then Second Mover is randomly chosen among the remaining four participants.

2. The Second Mover may give as little as $0.00 or as much as was alloted to them by \
the First Mover, or any amount in between (in $0.25 increments), to the First Mover.

3. The money given back to the First Mover WILL NOT be multiplied by 3, it will \
simply be placed back in the First Mover's bank.
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
            visual.TextStim(win, page1Section1, pos=[0, 0.4],height=0.07,wrapWidth=1.7),
            visual.TextStim(win, page1Section2, pos=[0, 0.2],height=0.07,wrapWidth=1.7),
            visual.TextStim(win, page1Section3, pos=[0, 0.1],bold=True,height=0.07,wrapWidth=1.7)
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, page2Section1, pos=[0, 0.8],height=0.1,wrapWidth=1.7),
            visual.TextStim(win, page2Section2, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, page3Section1, pos=[0, 0.8],height=0.1,wrapWidth=1.7),
            visual.TextStim(win, page3Section2, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ]
    ]
    for page in pages:
        for stim in page:
            stim.draw()
        win.flip()
        proceedOrQuit(win)

    return context
