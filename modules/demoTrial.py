from psychopy import visual
from lib.utils import proceedOrQuit

welcomeText = "Welcome to the experiment!"

intro = """
There are two tasks in this experiment: Task #1 & Task #2.

You will see a series of faces in these tasks. These faces \
are previous participants who currently attend CU Boulder and \
had a picture taken during their session like you just did.

In Task #2, you will be paired up with four of these previous participants \
and will have the chance to make decisions with real money that can impact \
yourself and them.
"""

beginWithGame1 = "First, we will describe Task #1"
pressSpace_task1 = "Press the SPACE key to begin instructions for Task #1."

pressSpace = "Press the SPACE key to continue."

summaryText = """
In Task #1, you will be presented with a steady stream of letters at the center of the screen \
surrounded by 4 photos (of previous participants) which will periodically rotate 180 degrees and \
sometimes change to a mirror image.{}
     The basic layout of the trial will look like this:{}
""".format('\n\n', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

instructions1Text = 'You have two tasks during this part of the experiment:'

instructions2Text = """
1. Press the SHIFT key when the letter at the center of the screen is a VOWEL.
       (e.g., press SHIFT when the letter 'a' appears, but not the letter 'f')

2. Each time an image rotates, there is a small chance that it will change to its mirror image. 
    At the end of the experimental trial, you will be asked how many image changes there were 
    during trial.
"""

instructions3Text = """The photo above will demonstrate what you are looking for each \
time a photo rotates. 

        Press the SPACE key to watch the image rotate and change to a new image.\
"""

instructions3Alt = """\
Can you find what is changing in the image?

                    Press the SPACE key to watch the image rotate and change to a new image.\
"""

instructions3Answer = """\
ANSWER: Pay attention to the man\'s eyebrows.
  
The image flips 180 degrees while rotating.

Press the SPACE key to continue.
"""

screen4Text = """\
Some image changes you will be looking for may be difficult to detect.

You must pay close attention to the images to successfully detect them!

                There are three more things you should know:

1. Not every trial of task #1 will have an image change, some will 
    have no image changes, and some will have multiple image changes.

2. when an image DOES change, it will only ever do so while it is rotating. 
    So, the best way to detect if an image changed is to check right after 
    each rotation.

3.  Keep a mental note of which image(s) change(s), and how many times 
     it changes during the trial. We will ask you about this at the end 
     of the trial!
"""

def __welcomeAndSummary(win):
    pressSpaceStim = visual.TextStim(win, pressSpace, height=0.06, pos=[0, -0.8], wrapWidth=1.7)
    welcome = visual.TextStim(win, welcomeText, height = 0.1)
    welcome.draw()
    pressSpaceStim.draw()
    win.flip()
    proceedOrQuit(win)

    introStim = visual.TextStim(win, intro, wrapWidth=1.7, height=0.10)
    introStim.draw()
    pressSpaceStim.draw()
    win.flip()
    proceedOrQuit(win)
    
    pressSpaceStim_task1 = visual.TextStim(win, pressSpace_task1, height=0.06, pos=[0, -0.8], wrapWidth=1.7)

    beginStim = visual.TextStim(win, beginWithGame1, wrapWidth=1.7, height=0.10, bold=True)
    beginStim.draw()
    pressSpaceStim_task1.draw()
    win.flip()
    proceedOrQuit(win)

    summary = visual.TextStim(win, summaryText, pos=[0, 0],height=0.07,wrapWidth=1.7)
    layout = visual.ImageStim(win, image='layout.bmp', mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])

    summary.draw()
    layout.draw()
    pressSpaceStim.draw()
    win.flip()
    proceedOrQuit(win)

# instruction screen intro
def screenIntro(win, textStim):
    textStim.setText(intro)
    textStim.draw()
    win.flip()

# instruction screen 4
def screen4(win, textStim):
    pressSpaceStim = visual.TextStim(win, pressSpace, height=0.06, pos=[0, -0.8], wrapWidth=1.7)
    textStim.setText(screen4Text)
    textStim.draw()
    pressSpaceStim.draw()
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
        visual.TextStim(win, instructions2Text, pos=[0,0.50],height=0.06,wrapWidth=1.5),
        visual.TextStim(win, instructions3Text, pos=[0,-0.65],height=0.06,wrapWidth=1.5),
    ]
    
    rotateSpeed = context['options']['speed']
    screenStim = visual.TextStim(win, screen4Text, pos=[0, 0], height=0.08, wrapWidth=1.5)
    pressSpaceStim = visual.TextStim(win, pressSpace, height=0.06, pos=[0, -0.8], wrapWidth=1.7)

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
    pressSpaceStim.draw()
    proceedOrQuit(win)

    gettingInput = True
    while gettingInput:
        __rotateDemoImage(win, demoPic, rotateSpeed, demoPicA, instructions)

        drawInstructions(win, instructions, demoPic)

        #wait for key press -- abort on escape
        input = proceedOrQuit(win)
        if 'space' in input:
            gettingInput = False


    screen4(win, screenStim)
    input = proceedOrQuit(win)

    return context
