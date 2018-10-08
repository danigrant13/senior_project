from psychopy import visual
from lib.utils import proceedOrQuit

welcomeText = """\
Welcome to the experiment
press the SPACE key to begin.

(Experimenter: press escape to quit.)\
"""

summaryText = """
In this experiment, you will be presented with a steady stream of letters at the center of the \
screen, surrounded by 4 images which will periodically rotate and sometimes change to a new image{}
The basic visual of each trial will be something like this:{}
Press the SPACE key to advance to the next screen and continue reading the instructions.
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

instructions1Text = 'You have two tasks during this experiment:'

instructions2Text ="""\
1. Press the SHIFT key whenever the letter' currently displayed in the center of the screen is a \
VOWEL. For example, you should press the key if the letter "a" appears on the screen, but not the \
letter "f".

2. Each time an image rotates, there is a small chance that it will change to a similar but \
different image. At the end of each experimental trial, you will be asked how many image \
changes there were during the trial.\
"""

instructions3Text = """The above image will demonstrate what you are looking for each \
time an image rotates. Press the SPACE key to watch the image rotate and change to a new image.\
"""

instructions3Alt = """\
To rotate and change the image again, press the BACK key.

Can you find what is changing in the picture above each time the image rotates?
Press the SPACE key to find out...\
"""

instructions3Answer = """\
ANSWER: Pay attention to the man\'s eyebrows.
The image flips 180 degrees while rotating.

Press the BACK key to rotate the image.\
"""

instructions4Text = """
When you have finished reading the instructions on this screen, press the SPACE key to advance to \
the next screen
Don't worry if you don't fully understand both of the tasks yet. We will explain them more on the \
next screen, and you will also get a chance to practice before starting the main experiment.\
"""

screen4Text = """\
Many of the image changes that you will be looking for can be difficult to detect. You must pay \
attention to the images closely to successfully detect the changes.

There are two more things you should know about the image changes.

First, not every trial of the experiment will have an image change. Some trials will have an image \
change, other trials will have no image changes, and some trials will have multiple image changes.

Second, when an image DOES change, it will only ever do so during one of the rotations that occur \
every couple of seconds. So the best way to successfully detect the image changes is to check each \
image after it rotates to see if anything has changed or not. If it has, make a mental note of \
which image it is and how many times it changes over the course of the trial. We will ask you \
about this at the end of each trial.




Press the SPACE key to continue reading the instructions.
"""

screen5Text = """



You will now complete two PRACTICE trials.

The purpose of the practice trials is simply to help you become familiar with the experimental \
procedure. After the practice trials you will begin the main experimental trials.

Remember your two tasks:
    1. Press the SHIFT key when the letter in the center of the screen is a VOWEL.
    2. Keep track of how many times any image changes over the course of the trial.



Press the SPACE key to begin the first practice trial.\
"""

def __welcomeAndSummary(win):
    welcome = visual.TextStim(win, welcomeText)
    welcome.draw()
    win.flip()
    proceedOrQuit(win)

    summary = visual.TextStim(win, summaryText, pos=[0, 0],height=0.06,wrapWidth=1.5)
    layout = visual.ImageStim(win, image='layout.bmp', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])

    summary.draw()
    layout.draw()
    win.flip()
    proceedOrQuit(win)

# instruction screen 4
def screen4(win, textStim):
    textStim.setText(screen4Text)
    textStim.draw()
    win.flip()

# instruction screen 5
def screen5(win, textStim):
    textStim.setText(screen5Text)
    textStim.draw()
    win.flip()

def drawInstructions(win, instructions, demoPic, count=3):
    demoPic.draw()
    for index in xrange(0, count):
        instructions[index].draw()
    win.flip()


def __rotateDemoImage(win, demoPicStim, rotateSpeed, demoPicChange, instructions):
    for x in range(0,361, rotateSpeed):
        demoPicStim.setOri(x)
        if x==180:
            demoPicStim.setImage(demoPicChange)
        drawInstructions(win, instructions, demoPicStim)

def run(context):
    win = context['window']
    demoPicA = 'demo_a.jpg'
    demoPicB = 'demo_b.jpg'
    demoPic = visual.ImageStim(win, image=demoPicA, mask=None, units='norm', pos=[0,-0.1], size=[0.45,0.6])
    instructions = [
        visual.TextStim(win, instructions1Text, pos=[0,0.85],height=0.06,wrapWidth=1.5),
        visual.TextStim(win, instructions2Text, pos=[0,0.50],height=0.06,wrapWidth=1.3),
        visual.TextStim(win, instructions3Text, pos=[0,-0.65],height=0.06,wrapWidth=1.5),
        visual.TextStim(win, instructions4Text)
    ]
    rotateSpeed = context['options']['speed']
    screenStim = visual.TextStim(win, screen4Text, pos=[0, 0], height=0.06, wrapWidth=1.5)

    __welcomeAndSummary(win)

    #display instruction screen 2
    drawInstructions(win, instructions, demoPic)
    proceedOrQuit(win)

    #loop that changes from demo image A to B
    gettingInput = True
    a = True
    while gettingInput:
        __rotateDemoImage(win, demoPic, rotateSpeed, demoPicB, instructions)

        #define instructions screen 3
        instructions[2].setText(instructions3Alt)

        #display instructions screen 1-3
        drawInstructions(win, instructions, demoPic)

        #wait for key press -- if 'escape' pressed close program
        input = proceedOrQuit(win)
        if 'space' in input:
            gettingInput = False

    # introduction screen 3
    instructions[2].setText(instructions3Answer)
    drawInstructions(win, instructions, demoPic)
    proceedOrQuit(win)

    gettingInput = True
    while gettingInput:
        __rotateDemoImage(win, demoPic, rotateSpeed, demoPicA, instructions)

        drawInstructions(win, instructions, demoPic)
        proceedOrQuit(win)

        instructions[-1].draw()
        win.flip()
        proceedOrQuit(win)

        #wait for key press -- abort on escape
        input = proceedOrQuit(win)
        if 'space' in input:
            gettingInput = False

    # cycle through instruction screens
    screens = [screen4, screen5]
    currentScreen = 0
    while currentScreen < 2:
        screens[currentScreen](win, screenStim)
        input = proceedOrQuit(win, keys=['escape', 'lshift', 'space'])
        if input == ['lshift']:
            if currentScreen > 0: currentScreen -= 1
        if input == ['space']:
            currentScreen += 1

    return context
