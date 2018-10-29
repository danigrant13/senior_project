from psychopy import event, visual
from lib.utils import proceedOrQuit

instructions1 = """
 Press the UP ARROW key or DOWN
ARROW key to increase and decrease
      the amount given to the player.
"""

moveToInstrutions = """
Press the SPACE bar to continue.
"""

spaceBarInstructions = """
Press the SPACE bar to move on to the
           next part of the game.
"""

# Colors in RGB
black = (0, 0, 0)
grey = (217, 217, 217)
red = (255, 0, 0)
green = (169, 209, 142)

startingDollars = "$ 5.00"
step = 0.25
multiplier = 3

selectTargetPrompt = """\
Please select the player you would like to send money to

                                 (A, B, C, or D)
"""

confirmPrompt = """\
Are your choices final?

              (y/n)
"""

continuePrompt = """\
Would you like to send money to anyone else?

                                  (y/n)
"""

playerLetters = ['A', 'B', 'C', 'D']

def drawInstructions(move, instructions):
    if move >= 5:
        return None
    elif move == 1:
        instructions[-1].draw()

    instructions[0].draw()
    if move < 4:
        instructions[1].setText(moveToInstrutions)
    else:
        instructions[1].setText(spaceBarInstructions)
    instructions[1].draw()

def gameTextBoxes(win):
    return [
      [
        visual.Rect(win, fillColorSpace='rgb255', width=0.3, height=0.2,fillColor=black,pos=[-0.58,0.33],lineColor=None),
        visual.Rect(win, fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey, pos=[-0.58,0.33],lineColor=None),
        visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[-0.58,0.33], height=0.1)
      ],
      [
        visual.Rect(win, fillColorSpace='rgb255',width=0.3,height=0.2,fillColor=black,pos=[0.58,0.33], lineColor=None),
        visual.Rect(win, fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey,pos=[0.58,0.33], lineColor=None),
        visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[0.58,0.33], height=0.1)
      ],
      [
        visual.Rect(win,fillColorSpace='rgb255',width=0.3,height=0.2,fillColor=black,pos=[-0.58,-0.33], lineColor=None),
        visual.Rect(win,fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey,pos=[-0.58,-0.33], lineColor=None),
        visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[-0.58,-0.33], height=0.1)
      ],
      [
        visual.Rect(win,fillColorSpace='rgb255',width=0.3,height=0.2,fillColor=black,pos=[0.58,-0.33], lineColor=None),
        visual.Rect(win,fillColorSpace='rgb255',width=0.27,height=0.15,fillColor=grey, pos=[0.58,-0.33], lineColor=None),
        visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[0.58,-0.33], height=0.1)
      ],
      [
          visual.Rect(win, fillColorSpace='rgb255',width=0.3,height=0.2, fillColor=red, pos=[0,-0.7], lineColor=None),
          visual.Rect(win, fillColorSpace='rgb255',width=0.27,height=0.15, fillColor=grey, pos=[0, -0.7], lineColor=None),
          visual.TextStim(win, startingDollars, colorSpace='rgb255', color=black, pos=[0, -0.7], height=0.1)
      ]
    ]

def npcTextBoxes(textBoxes):
    return textBoxes[:4]

def setTextBoxAmount(textBox, amount):
    textBox[2].setText('$ {0:.2f}'.format(amount))

def getTextBoxAmount(textBox):
    return float(textBox[2].text[2:])

def incrementAmount(textBox, targetAmount, mover=False):
    amount = getTextBoxAmount(textBox)
    if mover:
        if amount + step > 5.0:
            return False
        elif targetAmount == 5.0:
            return False
        amount += step
    else:
        amount += (multiplier * step)
    setTextBoxAmount(textBox, amount)
    return True

def decrementAmount(textBox, mover=False):
    amount = getTextBoxAmount(textBox)
    if amount - step < 0.0:
        return False
    if mover:
        amount -= step
    else:
        amount -= (multiplier * step)

    setTextBoxAmount(textBox, amount)
    return True

def setPrimaryMover(textBoxes, prevMover, newMover):
    textBoxes[prevMover][0].setFillColor(black, colorSpace='rgb255')
    textBoxes[newMover][0].setFillColor(red, colorSpace='rgb255')

def setMoverTarget(textBoxes, prevTarget, newTarget):
    textBoxes[prevTarget][0].setFillColor(black, colorSpace='rgb255')
    textBoxes[newTarget][0].setFillColor(green, colorSpace='rgb255')

def clearPlayers(textBoxes):
    for box in textBoxes:
        box[0].setFillColor(black, colorSpace='rgb255')
        box[2].setText(startingDollars)

def drawBoard(win, imageList, markerList, textBoxes, justTarget=None):
    you = visual.TextStim(win, "You", pos=[0, -0.5], height=0.1)
    if justTarget == None:
        for index in range(4):
            imageList[index].draw()
            markerList[index].draw()
            for tb in textBoxes[index]:
                tb.draw()
    else:
        markerList[justTarget].draw()
        imageList[justTarget].draw()
        for tb in textBoxes[justTarget]:
            tb.draw()

    textBoxes[-1][0].draw()
    textBoxes[-1][1].draw()
    textBoxes[-1][2].draw()
    you.draw()
    win.flip()

def __dataHeaders():
    return [
        "1st choice giving money (actual picture name)",
        "How much given to 1st choice (no multiplier)",
        "2nd choice giving money (actual picture name)",
        "How much given to 2nd choice (no multiplier)",
        "3rd choice giving money (actual picture name)",
        "How much given to 3rt choice (no multiplier)",
        "4th choice giving money (actual picture name)",
        "How much given to 4th choice (no multiplier)"
    ]

def __setData(context, giftOrder, textBoxes, pictures):
    values = []
    for index in giftOrder:
        values.append(pictures[index])
        values.append((getTextBoxAmount(textBoxes[index]) - 5.0) / 3)

    context['report']['headers'] += __dataHeaders()
    context['report']['data'] += values

def run(context):
    imageList = context['imageList']
    markerList = context['markerList']
    win = context['window']
    isDemo = context['trustGameDemo']
    textBoxes = gameTextBoxes(win)
    instructions = [
        visual.TextStim(win, instructions1, pos=[0,0.4],height=0.06,wrapWidth=1.5),
        visual.TextStim(win, moveToInstrutions, pos=[0,0.1], height=0.06,wrapWidth=1.5)
    ]
    currentMover = textBoxes[-1]
    prompt = visual.TextStim(win, confirmPrompt, height=0.06)
    players = { 'a': 0, 'b': 1, 'c': 2, 'd': 3 }

    giftOrder = []

    currentTarget = 0
    lastTarget = 0
    stillDeciding = True
    while stillDeciding:
        stillGivingToPlayers = True
        while stillGivingToPlayers:
            prompt.setText(selectTargetPrompt)
            prompt.draw()
            drawBoard(win, imageList, markerList, textBoxes)
            input = proceedOrQuit(win, keys=['escape', 'A', 'B', 'C', 'D', 'a', 'b', 'c', 'd'])
            lastTarget = currentTarget
            currentTarget = players[input[0].lower()]
            moverTarget = textBoxes[currentTarget]
            setMoverTarget(textBoxes, lastTarget, currentTarget)
            drawInstructions(currentTarget, instructions)
            drawBoard(win, imageList, markerList, textBoxes, justTarget=currentTarget)

            collectingAmount = True
            while collectingAmount:
                keys = ['space', 'escape', 'up', 'down']
                moverTargetAmount = getTextBoxAmount(moverTarget)
                input = proceedOrQuit(win, keys = keys)
                if 'up' in input:
                    updateTarget = decrementAmount(currentMover, mover=True)
                    if updateTarget:
                        incrementAmount(moverTarget, moverTargetAmount)
                elif 'down' in input:
                    updateTarget = incrementAmount(currentMover, moverTargetAmount, mover=True)
                    if updateTarget:
                        decrementAmount(moverTarget)
                elif 'space' in input:
                    collectingAmount = False

                drawInstructions(currentTarget, instructions)
                drawBoard(win, imageList, markerList, textBoxes, justTarget=currentTarget)

                if context['collectData']:
                    if currentTarget not in giftOrder:
                        giftOrder.append(currentTarget)
            prompt.setText(continuePrompt)
            prompt.draw()
            drawBoard(win, imageList, markerList, textBoxes, justTarget=currentTarget)
            input = proceedOrQuit(win, keys=['escape', 'y', 'n'])
            if 'n' in input:
                stillGivingToPlayers = False


        prompt.setText(confirmPrompt)
        prompt.draw()
        drawBoard(win, imageList, markerList, textBoxes)
        input = proceedOrQuit(win, keys=['escape', 'y', 'n'])
        if 'y' in input:
            stillDeciding = False

    if context['collectData']:
        __setData(context, giftOrder, textBoxes, [imageStim.image for imageStim in imageList])

    return context
