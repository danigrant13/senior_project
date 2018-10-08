from modules import attentionChangeQuiz, attentionTask, attentionTaskFeedback, \
                    controlAttentionInstructions, gatherRatings
from lib.runner import go

subModules = [
    controlAttentionInstructions,
    attentionTask,
    gatherRatings,
    attentionChangeQuiz,
    attentionTaskFeedback
]

def run(context):
    controlImages = context['controlImages']
    for index, image in enumerate(controlImages):
        context['imageList'][index].setImage(image)

    # no specific target in the control
    context['target'] = -1
    context['trialNum'] = 0
    context['numberOfChanges'] = 0

    return go(subModules, context)
