from modules import attentionChangeQuiz, attentionTaskFeedback
from lib.runner import go
from psychopy import visual
from lib.utils import proceedOrQuit

subModules = [
    attentionChangeQuiz,
    attentionTaskFeedback,
]

pressSpaceKey = "Press the SPACE key to continue."

transitionControlQuiz = """
                                          You have finished Task #2!

        Next you will answer some questions about one of the groups from Task #1.
"""

transitionExperimentQuiz = """
                                Thank you for answering those questions.

        Next you will answer some questions about one more group from Task #1.
"""
    
def run(context):

    win = context['window']

    transition1 = visual.TextStim(win, transitionControlQuiz, pos=[0, 0.2], height=0.07, wrapWidth=1.5)
    pressSpace = visual.TextStim(win, pressSpaceKey, pos=[0, -0.8], height=0.06, wrapWidth=1.5)

    transition1.draw()
    pressSpace.draw()
    win.flip()
    proceedOrQuit(win)

    context['trialNum'] = 0
    controlImages = context['controlImages']
    for index, image in enumerate(controlImages):
        context['imageList'][index].setImage(image)

    new_context = go(subModules, context)

    transition2 = visual.TextStim(win, transitionExperimentQuiz, pos=[0, 0.2], height=0.07, wrapWidth=1.5)

    transition2.draw()
    pressSpace.draw()
    win.flip()
    proceedOrQuit(win)

    new_context['trialNum'] = 1
    trialImages = context['trialImages']
    for index, image in enumerate(trialImages):
        context['imageList'][index].setImage(image)

    return go(subModules, new_context)
