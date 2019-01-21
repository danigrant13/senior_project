from modules import attentionChangeQuiz, attentionTaskFeedback
from lib.runner import go

subModules = [
    attentionChangeQuiz,
    attentionTaskFeedback,
]

def run(context):
    context['trialNum'] = 0
    controlImages = context['controlImages']
    for index, image in enumerate(controlImages):
        context['imageList'][index].setImage(image)

    new_context = go(subModules, context)

    new_context['trialNum'] = 1
    trialImages = context['trialImages']
    for index, image in enumerate(trialImages):
        context['imageList'][index].setImage(image)

    return go(subModules, new_context)
