from psychopy import visual
from lib.utils import proceedOrQuit

# Colors in RGB
black = (0, 0, 0)
grey = (217, 217, 217)
red = (255, 0, 0)
green = (169, 209, 142)

age1introGame = """ \
Now, we will describe Task #2 \
"""

pressSpace = "Press the SPACE key to continue reading the instructions."

summaryText = """
In Task #2, you will again be presented with a screen surrounded by four photos of previous participants. \
They will be labeled A, B, C, and D. In addition, you will be given a letter designation, 'E', ]
to indicate you are a player in this game.{}
     The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

summaryText2 = """
In Task #2, each player (including you) will be allotted $5.00 each in their personal bank.{}
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

def screen1(win):
    summary = visual.TextStim(win, summaryText, pos=[0, 0],height=0.07,wrapWidth=1.7)
    layout = visual.ImageStim(win, image='layout.bmp', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])

    summary.draw()
    layout.draw()
    pressSpaceStim.draw()
    win.flip()
    proceedOrQuit(win)

def screen2(win):
    pressSpaceStim = visual.TextStim(win, pressSpace, height=0.06, pos=[0, -0.7], wrapWidth=1.7)
    summary = visual.TextStim(win, summaryText2, pos=[0, 0],height=0.07,wrapWidth=1.7)
    layout = visual.ImageStim(win, image='layout.bmp', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])

    summary.draw()
    layout.draw()
    pressSpaceStim.draw()
    win.flip()
    proceedOrQuit(win)

def screen3(win, textStim):
    pressSpaceStim = visual.TextStim(win, pressSpace, height=0.06, pos=[0, -0.7], wrapWidth=1.7)
    visual.TextStim(win, title, pos=[0,0.85],height=0.1,wrapWidth=1.5),
    textStim.setText(gameRoles)
    textStim.draw()
    pressSpaceStim.draw()
    win.flip()    














\

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



    for page in pages:
        __drawPage(win, page, imageList, markerList, textBoxes)
        proceedOrQuit(win)
    return context

