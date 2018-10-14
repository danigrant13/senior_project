import random
from modules import attentionChangeQuiz, attentionTask, attentionTaskFeedback, \
                    experimentalAttentionIntro, gatherRatings
from lib.runner import go

subModules = [
    experimentalAttentionIntro,
    attentionTask,
    gatherRatings,
    attentionChangeQuiz,
    attentionTaskFeedback,
]

def run(context):
    trialImages = context['trialImages']
    for index, image in enumerate(trialImages):
        context['imageList'][index].setImage(image)

    possible_targets = [0, 1, 2, 3]
    context['target'] = random.choice(possible_targets)
    context['nonTargetList'] = filter(lambda x: x != context['target'], possible_targets)
    context['numberOfChanges'] = 0
    context['changeProb'] = 0.5

    context['trialNum'] = 1

    return go(subModules, context)
