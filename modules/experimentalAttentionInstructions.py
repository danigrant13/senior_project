from psychopy import visual
from lib.utils import proceedOrQuit


screen1Text = """\
                You will now begin the experimental trial.

Your task in this part of the experiment is the same as it was during the 2nd trial.

                Your goal is to be as accurate as possible.









                    Press the SPACE key to continue.
"""

screen2Text = """
"""
screen3Text = """
"""
screen4Text = """
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
