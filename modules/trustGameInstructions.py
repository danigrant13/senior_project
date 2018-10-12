from psychopy import visual
from lib.utils import proceedOrQuit

# Colors in RGB
black = (0, 0, 0)
grey = (217, 217, 217)
red = (255, 0, 0)
green = (169, 209, 142)

startingDollars = "$ 5.00"

page1Section1 = """\
Next you are going to play a game with the previus participants \
that may proceed in a future study session later this semester.
"""
page1Section2 = """
In this game, there are two roles:
First Mover & Second Mover
"""
page1Section3 =  """
You and the other participants will be randomly assigned to \
one of these two roles. The role you are assigned will determine \
the kinds of actions you can perform in the game.
"""

page2Section1 = """
At the beginning of the game
we are going to put {} in
each player's account.
""".format(startingDollars)

proceedInstructions = """
Press the SPACE bar to move on the
next part of the instructions
"""

page3Section1 = """
The First Mover (red box) will be given the
opportunity to pay as little as $0.00 or as
much as $5.00, or any amount in between
(in $0.25 increments), to the other players
in alphabetical order. The amount sent to
other players will be a factor of three times
the amount the First Mover pays.
(in this example player B is the first mover)
"""

firstMoveBreakdown = """
In this case, the First Mover (red box)
gave Player A (green box) ${0} which
which was multiplied by 3 to yield ${1}

${1} + ${2} = ${3}
"""

page4Section1 = firstMoveBreakdown.format("1.00", "3.00", "5.00", "8.00")

page4Section2 = "So, $8.00 is placed in Player A's bank."

page5Section1 = firstMoveBreakdown.format("0.00", "0.00", "5.00", "5.00")

page5Section2 = "No money is placed in Player C's bank."

page6Section1 = firstMoveBreakdown.format("0.25", "0.75", "5.00", "5.75")

page6Section2 = "So, $5.75 is placed in Player A's bank."

page7Section1 = firstMoveBreakdown.format("2.00", "6.00", "5.00", "11.00")

page7Section2 = "So, $5.75 is placed in Player A's bank."

page8Section1 = """
Once the First Mover's choice has been
confirmed, the decision will be sent to
the Second Mover. The Second Mover
(red box) will be given the opportunity to
return as little as $0.00 and as much as
the amount they received from the First
Mover ($3.00 in this example) or any
amount in between (in $0.25 increments),
back to the First Mover (green box).
"""

page9Section1 = """
The Second Mover (red box) can only
return up to the amount they
received ($3.00 in this example). The
Second Mover will not be able to return
any of the $5.00 they started with in
their account.
"""

page9Section2 = """
The amount sent to the First Mover
(green box) will NOT be multiplied by 3,
it will simply be placed directly into
the First Mover's account.
(Second Mover is Player A in this example)
"""

secondMoveBreakdown = """
In this case, the Second Mover (red box)
returned ${0} to the First Mover (green box)

${0} + ${1} = ${2}
"""

page10Section1 = secondMoveBreakdown.format("2.00", "1.75", "3.75")

page10Section2 = "So, $3.75 is placed in Player B's bank."

page11Section1 = """
This pattern will continue on until the rest
of the players (D, C, and you) have been
Second Mover.
"""

page12Section1 = """
If you are chosen as First Mover, you
will go through the players in
alphabetical order to decide how much or
little money you choose to trust them with.
"""

page13Section1 = """
You will press the UP ARROW key or
DOWN ARROW key to increase and
decrease the amount.
"""

page13Section2 = "Now let's practice!"

def gameTextBoxes(win):
    return [
      [
        visual.Rect(win,fillColorSpace='rgb255',width=0.3, height=0.2,fillColor=black,pos=[-0.58,0.33],lineColor=None),
        visual.Rect(win,fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey, pos=[-0.58,0.33],lineColor=None),
        visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[-0.58,0.33], height=0.1)
      ],
      [
        visual.Rect(win, fillColorSpace='rgb255',width=0.3,height=0.2,fillColor=black,pos=[0.58,0.33],lineColor=None),
        visual.Rect(win, fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey,pos=[0.58,0.33],lineColor=None),
        visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[0.58,0.33], height=0.1)
      ],
      [
        visual.Rect(win,fillColorSpace='rgb255',width=0.3,height=0.2,fillColor=black,pos=[-0.58,-0.33],lineColor=None),
        visual.Rect(win,fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey,pos=[-0.58,-0.33],lineColor=None),
        visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[-0.58,-0.33], height=0.1)
      ],
      [
        visual.Rect(win,fillColorSpace='rgb255',width=0.3,height=0.2,fillColor=black,pos=[0.58,-0.33],lineColor=None),
        visual.Rect(win,fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey, pos=[0.58,-0.33],lineColor=None),
        visual.TextStim(win, startingDollars, colorSpace='rgb255',color=black,pos=[0.58,-0.33],height=0.1)
      ],
      [
          visual.Rect(win,fillColorSpace='rgb255',width=0.3,height=0.2,fillColor=black, pos=[0,-0.7], lineColor=None),
          visual.Rect(win,fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey, pos=[0, -0.7], lineColor=None),
          visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[0, -0.7], height=0.1)
      ]
    ]

def __drawBoard(win, imageList, markerList, textBoxes):
    for index in range(4):
        imageList[index].draw()
        markerList[index].draw()
        for tb in textBoxes[index]:
            tb.draw()
    textBoxes[-1][0].draw()
    textBoxes[-1][1].draw()
    textBoxes[-1][2].draw()


def __setTextBoxAmounts(textBoxes, amounts):
    count = len(amounts)
    if count == 0:
        return None
    for index in range(count):
        textBoxes[index][2].setText(amounts[index])

def __setPrimaryMover(textBoxes, newMover):
    if newMover == None:
        return None
    textBoxes[newMover][0].setFillColor(red, colorSpace='rgb255')

def __setMoverTarget(textBoxes, newTarget):
    if newTarget == None:
        return None
    textBoxes[newTarget][0].setFillColor(green, colorSpace='rgb255')

def __clearMovers(textBoxes):
    for box in textBoxes:
        box[0].setFillColor(black, colorSpace='rgb255')

def __drawMovers(textBoxes, moverTuple):
    __clearMovers(textBoxes)
    __setPrimaryMover(textBoxes, moverTuple[0])
    __setMoverTarget(textBoxes, moverTuple[1])

def __drawPage(win, page, imageList, markerList, textBoxes):
    if page[0]:
        __drawMovers(textBoxes, page[1])
        __setTextBoxAmounts(textBoxes, page[2])
        __drawBoard(win, imageList, markerList, textBoxes)
    for textStim in page[3]:
        textStim.draw()
    win.flip()

def run(context):
    win = context['window']
    imageList = context['imageList']
    markerList = context['markerList']

    textBoxes = gameTextBoxes(win)

    pages = [
        (False, (None, None), [], [
            visual.TextStim(win, page1Section1, pos=[0,0.3],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page1Section2, height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page1Section3, pos=[0,-0.3],height=0.06,wrapWidth=1.5)
        ]),
        (True, (None, None), [], [
            visual.TextStim(win, page2Section1, pos=[0,0.3],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (1, None), ["$ 5.00", "$ 5.00", "$ 5.00", "$ 5.00", "$ 5.00"], [
            visual.TextStim(win, page3Section1, pos=[0,0.3],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (1, 0), ["$ 8.00", "$ 4.00", "$ 5.00", "$ 5.00", "$ 5.00"], [
            visual.TextStim(win, page4Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page4Section2, pos=[0,0],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (1, 2), ["$ 8.00", "$ 4.00", "$ 5.00", "$ 5.00", "$ 5.00"], [
            visual.TextStim(win, page5Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page5Section2, pos=[0,0],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (1, 3), ["$ 8.00", "$ 3.75", "$ 5.00", "$ 5.75", "$ 5.00"], [
            visual.TextStim(win, page6Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page6Section2, pos=[0,0],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (1, 4), ["$ 8.00", "$ 1.75", "$ 5.00", "$ 5.75", "$ 11.00"], [
            visual.TextStim(win, page7Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page7Section2, pos=[0,0],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (0, 1), ["$ 8.00", "$ 1.75", "$ 5.00", "$ 5.75", "$ 11.00"], [
            visual.TextStim(win, page8Section1, pos=[0,0.3],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (0, 1), ["$ 8.00", "$ 1.75", "$ 5.00", "$ 5.75", "$ 11.00"], [
            visual.TextStim(win, page9Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page9Section2, pos=[0,0],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (0, 1), ["$ 6.00", "$ 3.75", "$ 5.00", "$ 5.75", "$ 11.00"], [
            visual.TextStim(win, page10Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page10Section2, pos=[0,0],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (0, 1), ["$ 6.00", "$ 3.75", "$ 5.00", "$ 5.75", "$ 11.00"], [
            visual.TextStim(win, page11Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (None, None), ["$ 5.00", "$ 5.00", "$ 5.00", "$ 5.00", "$ 5.00"], [
            visual.TextStim(win, page12Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (4, None), ["$ 5.00", "$ 5.00", "$ 5.00", "$ 5.00", "$ 5.00"], [
            visual.TextStim(win, page13Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page13Section2, pos=[0,0],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ])
    ]

    for page in pages:
        __drawPage(win, page, imageList, markerList, textBoxes)
        proceedOrQuit(win)
    return context
