from psychopy import visual
from lib.utils import proceedOrQuit

# Colors in RGB
black = (0, 0, 0)
grey = (217, 217, 217)
red = (255, 0, 0)
green = (169, 209, 142)

startingDollars = "$ 5.00"

page1Section1 = """
Now, we will do a Trust Game practice round.
"""

page2Section1 = """
You will press the UP ARROW key or
DOWN ARROW key to increase and
decrease the amount.
"""

page2Section2 = "Now let's practice!"

proceedInstructions = """
Press the SPACE key to move on 
to the next part of the instructions.
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
    you = visual.TextStim(win, "You", pos=[0, -0.5], height=0.1)
    for index in range(4):
        imageList[index].draw()
        markerList[index].draw()
        for tb in textBoxes[index]:
            tb.draw()
    you.draw()
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
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ]),
        (True, (4, None), ["$ 5.00", "$ 5.00", "$ 5.00", "$ 5.00", "$ 5.00"], [
            visual.TextStim(win, page2Section1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, page2Section2, pos=[0,0],height=0.06,wrapWidth=1.5),
            visual.TextStim(win, proceedInstructions, pos=[0,-0.3], height=0.06,wrapWidth=1.5)
        ])
    ]

    for page in pages:
        __drawPage(win, page, imageList, markerList, textBoxes)
        proceedOrQuit(win)
    return context
