from psychopy import visual
from lib.utils import proceedOrQuit

screen1Text = """\
You will now begin the main part of the experiment.

Your task in this part of the experiment is going to be just the same as it was \
during the practice trials. The experiment consists of a series of 1 trials just like the \
practice trials that you completed, except somewhat longer. They will take a total of \
approximately 30 minutes to complete.

The only difference here is that on these trials you will be awarded a certain amount of POINTS \
based on your performance each trial. Your goal is to gain as many points as possible over the \
course of the experiment.

On the next screen we will explain the point scoring system in more detail.



Press the SPACE key to advance to the next screen and continue reading the instructions.\
"""

screen2Text = """



***Points for the vowel task:***

The points earned for the vowel task are based on the total number of correct responses \
(responses that cause the green check mark to appear) and incorrect responses (responses that \
cause the red X to appear) that you make.

First the number of incorrect responses that you make is multiplied by 2.

Then the number of points that you earn from the vowel task is the proportion of correct \
responses to total responses, scaled from 0 points to 50 points.

For example, if you made 10 correct responses and 5 incorrect responses, your proportion of \
correct responses would be 10 / (10 + 5*2) = 0.5, so you would earn 25 out of 50 points for the \
vowel task.



Press the SPACE key to continue reading the instructions.\
"""

screen3Text = """

***Points for the image change task:***

The points earned for the image change task are based on whether you correctly answered whether \
or not there were any image changes during the trial, and if there were, whether you correctly \
identified the image that changed and also gave the correct number of total image changes.

The exact numbers of points earned for each possible response are listed in the table below:{0}\
Press the SPACE key to continue reading the instructions.'
""".format('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


screen4Text = """



At the end of each trial, the points that you earn on both the SHIFT TASK and the IMAGE CHANGE \
TASK are added together to give the total number of points earned on that trial. Both tasks \
award a maximum of 50 points each. So the maximum number of points that you can earn on each trial
is 100 points.

Only by being as accurate as possible on both the VOWEL TASK and the IMAGE CHANGE TASK can you \
maximize the amount of points that you earn. No other strategy (like strategically only \
answering "Yes" or always answering "No" on the image change task) will give you the most points.



When you are ready, press the SPACE key to finish the instructions and advance to the trial.\
"""

def __drawScreen(win, stims):
    for stim in stims:
        stim.draw()
    win.flip()

def run(context):
    win = context['window']

    screens = [
        [visual.TextStim(win, screen1Text, pos=[0, 0],height=0.06,wrapWidth=1.6)],
        [visual.TextStim(win, screen2Text, pos=[0, 0],height=0.06,wrapWidth=1.6)],
        [
            visual.TextStim(win, screen3Text, pos=[0, 0],height=0.06,wrapWidth=1.6),
            visual.ImageStim(
                win,
                image='changePoints.bmp',
                mask=None,
                units='norm',
                pos=[-.1, -0.25],
                size=[0.88, 1]
            )
        ],
        [visual.TextStim(win, screen4Text, pos=[0, 0],height=0.06,wrapWidth=1.6)]
    ]

    currentScreen = 0
    numScreens = len(screens)

    while currentScreen < numScreens:
        __drawScreen(win, screens[currentScreen])
        input = proceedOrQuit(win, keys=['escape', 'lshift', 'space'])
        if input == ['lshift']:
            if currentScreen > 0: currentScreen -= 1
        if input == ['space']:
            currentScreen += 1

    return context
