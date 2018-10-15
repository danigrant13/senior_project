from psychopy import visual
from lib.utils import proceedOrQuit

# Colors in RGB
black = (0, 0, 0)
grey = (217, 217, 217)
red = (255, 0, 0)
green = (169, 209, 142)

age1introGame = """ \
Now, we will describe Game #2 \
"""

pressSpace = "Press the SPACE key to continue reading the instructions."

summaryText = """
In Game #2, you will again be presented with a screen surrounded by four photos of previous participants. \
They will be labeled A, B, C, and D. In addition, you will be given a letter designation, 'E', ]
to indicate you are a player in this game.{}
     The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryText2 = """
In Game #2, each player (including you) will be allotted $5.00 each in their personal bank.{}
     The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

title = """ \
There are two roles in this game:
First Mover & Second Mover"""

gameRoles = """
The First Mover is randomly selected among all the participants

The first mover chooses which of the other four participants they would like to play the trust game with

the first mover is given the opportunity to give as little as $0.00 or as much as $5.00, or any amount in between (in $0.25 increments), so their participant of choice

The money given to the chosen participant will be multiplied by three and placed in the chosen participant's bank
"""

gameRoles2 = """ 
One the first mover has finished deciding how much to allot \
to the chosen participant, the first mover will be given the \
chance to choose a different participant to play the trust game with

This cycle will continue until the first mover is satisfied with the \
choices he has made about money allotted (or not) during the first round
"""

gameRoles3 = """ 
After the First Mover's turn is over, the Second Mover will be randomly \
chosen from one of the four other participants

The Second Mover will be given the opportunity to return as \
little as $0.00 and as much as they received, or any amount in \
between (in $0.25 increments), back to the First Mover

The Second mover CANNOT give any of the original $5.00 \
placed in their account at the beginning of the game
"""

summaryText3 = """
During the game, a RED BOX will indicate First Mover, \
while a GREEN BOX will indicate Second Mover.{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def run(context):
    win = context['window']
    pressSpaceStim = visual.TextStim(win, pressSpace, height=0.06, pos=[0, -0.8], wrapWidth=1.7)
    pages = [
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
            pressSpaceStim,
            visual.TextStim(win, title, pos=[0, 0.8],height=0.1,wrapWidth=1.7),
            visual.TextStim(win, gameRoles, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, title, pos=[0, 0.8],height=0.1,wrapWidth=1.7),
            visual.TextStim(win, gameRoles2, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, title, pos=[0, 0.8],height=0.1,wrapWidth=1.7),
            visual.TextStim(win, gameRoles3, pos=[0, 0],height=0.07,wrapWidth=1.7)
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
