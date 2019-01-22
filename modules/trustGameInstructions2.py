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
In Task #2, you will again be presented with a screen surrounded by four photos of previous 
                                participants. They will be labeled A, B, C, and D.{}
The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryText2 = """
In Task #2, each participant (including you) will be allotted $5.00 each in their personal bank.{}
The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

title = """ 
There are two roles in this task:
 First Mover & Second Movers"""

gameRoles = """
    1. You will be the First Mover.

    2. You will choose how much money, if any, to send to the other participants 
       (Second Mover). You can give as little as $0.00 or as much as $5.00 
       (in $0.25 increments), to the other participants in total.

    3. Any money you send will be multiplied by three and placed in the chosen 
       participant's account. In a follow-up session, they will be given the chance 
       to send some, none, or all of that money back to you.
"""

transitiontext = """ Now, let's walk you through a demonstration as if you are First Mover."""

summaryTextA = """
 First, you will be asked if you would like to send any money to any of the other participants or
keep the money for yourself. You can send as much or as little of your $5.00 as you would like
                                       to any combination of the other participants.{}
The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryTextB = """
Say you chose to send money to participant A by pressing the 'A' key. You then choose how 
                             much to send pressing the 'Up' arrow on the keyboard. 
                                      In this example, you decide to give $1.00. {}
The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryTextC = """ 
In this case, because you have chosen to send participant A $1.00, this sent money is multiplied 
 by 3 to equal $3.00 and added to A's account. So, participant A receives $5.00 + $3.00 = $8.00. 
                                                   Your account now has $4.00.{}
The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryTextD = """
 Then, you will be asked if you would like to send money to any of the other participants. In this 
                   example, you choose 'y' for Yes in order to send to another participant.{}
The basic layout of the trial will look like this:{}
""".format('\n\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryTextE = """
    Now, you choose other participants to send money to. In this case, you choose participant B.{}
The basic layout of the trial will look like this:{}
""".format('\n\n\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryTextF = """
You decide to send participant B $2.00, which is multiplied by 3 to equal $6.00 and added to B's 
                              account to total to $11.00. Your account now has $2.00.{}
The basic layout of the trial will look like this:{}
""".format('\n\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryTextG = """
Next, you will again be asked if you would like to send money to any of the other participants. 
               This will repeat until you select 'n' for No. In this example, you select 'n'. {}
The basic layout of the trial will look like this:{}
""".format('\n\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryTextH = """
You will then be asked to confirm you choices are final. In this case, you choose 'y' for Yes.{}
The basic layout of the trial will look like this:{}
""".format('\n\n\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryTextI = """
In a future session, participants A, B, C, and D will be given a chance to send some, none, or all of their earnings
from this session back to you. Say that both participant A and participant B choose to send back half of what they
  received from you. Participant A received $3.00 and sends back $1.50. Participant B received $6.00 and sends
 back $3.00. Because you did not send any money to participants C and D in this example, they cannot send you
        any money back. In total, you receive $4.50 back to be added to you current $2.00, for a total of $6.50.
                                           The screen below shows the final account balances. {}
The basic layout of the trial will look like this:{}
""".format('\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryText3 = """
          You, the First Mover, will be surrounded by a RED BOX.
A GREEN BOX will indicate the participant you choose to give money.{}
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
            visual.ImageStim(win, image='trustDemo1.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],     

        [
            pressSpaceStim,
            visual.TextStim(win, summaryText2, pos=[0, 0],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='trustDemo2.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim_fin,
            visual.TextStim(win, title, pos=[0, 0.8],height=0.1,wrapWidth=1.7),
            visual.TextStim(win, gameRoles, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, transitiontext, pos=[0, 0],height=0.07,wrapWidth=1.7)
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextA, pos=[0, 0.05],height=0.07,wrapWidth=1.7),                                    #working here
            visual.ImageStim(win, image='demoPicA.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextB, pos=[0, 0.05],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='demoPicB.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextC, pos=[0, 0.05],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='demoPicC.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextD, pos=[0, 0.05],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='demoPicD.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextE, pos=[0, 0.05],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='demoPicE.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextF, pos=[0, 0.05],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='demoPicF.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextG, pos=[0, 0.05],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='demoPicG.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextH, pos=[0, 0.05],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='demoPicH.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryTextI, pos=[0, 0.15],height=0.06,wrapWidth=1.7),
            visual.ImageStim(win, image='demoPicI.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ],
        [
            pressSpaceStim,
            visual.TextStim(win, summaryText3, pos=[0, 0.7],height=0.07,wrapWidth=1.7),
            visual.ImageStim(win, image='trustDemo3.jpg', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])
        ]

    ]
    for page in pages:
        for stim in page:
            stim.draw()
        win.flip()
        proceedOrQuit(win)

    return context
