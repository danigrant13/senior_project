from psychopy import visual
from lib.utils import proceedOrQuit

# Colors in RGB
black = (0, 0, 0)
grey = (217, 217, 217)
red = (255, 0, 0)
green = (169, 209, 142)


pressSpace_task2 = "Press the SPACE key to continue reading the instructions for Task #2."

pressSpace = "Press the SPACE key to continue."

pressSpace_fin = "Press the SPACE key to finish reading the instructions."

introTask = """ \
Now, we will describe Task #2. \
"""

summaryText = """
In Task #2, you will again be presented with a screen surrounded by four photos of previous participants. \
They will be labeled A, B, C, and D.{}
     The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryText2 = """
In Task #2, each participant (including you) will be allotted $5.00 each in their personal bank.{}
     The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

title = """ \
There are two roles in this task:
First Mover & Second Mover"""

gameRoles = """
1. You will be the First Mover.

2. You will choose how much money, if any, to send to the other participants (Second Mover).
   You can give as little as $0.00 or as much as $5.00 (in $0.25 increments), to the other participants in total.

3. Any money you send will be multiplied by three and placed in the chosen participant's account. In a follow-up \
session, they will be given the chance to send some, none, or all of that money back to you.
"""

summaryText3 = """
During the game, a RED BOX will indicate current Mover, \
while a GREEN BOX will indicate the current receiver.{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def run(context):
    win = context['window']
    pressSpaceStim = visual.TextStim(win, pressSpace, height=0.06, pos=[0, -0.8], wrapWidth=1.7)
    pressSpaceStim_task2 = visual.TextStim(win, pressSpace_task2, height=0.06, pos=[0, -0.8], wrapWidth=1.7)
    pressSpaceStim_fin = visual.TextStim(win, pressSpace_fin, height=0.06, pos=[0, -0.8], wrapWidth=1.7)

    pages = [
        [
            pressSpaceStim_task2,
            visual.TextStim(win, introTask, pos=[0, 0],height=0.1,wrapWidth=1.7),
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryText, pos=[0, 0],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='trustDemo1.jpg', mask=None, units='norm', pos=[0, -0.2], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryText2, pos=[0, 0],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='trustDemo2.jpg', mask=None, units='norm', pos=[0, -0.2], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim_fin,
            visual.TextStim(win, title, pos=[0, 0.8],height=0.1,wrapWidth=1.7),
            visual.TextStim(win, gameRoles, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryText3, pos=[0, 0.7],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='trustDemo3.jpg', mask=None, units='norm', pos=[0, -0.2], size=[0.88, 1.0])
        ]

    ]
    for page in pages:
        for stim in page:
            stim.draw()
        win.flip()
        proceedOrQuit(win)

    return context
