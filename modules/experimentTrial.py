import random
from modules import attentionChangeQuiz, attentionTask, attentionTaskFeedback, \
                    experimentalAttentionIntro, gatherRatings
from lib.runner import go

subModules = [
    experimentalAttentionIntro,
    attentionTask,
    gatherRatings,
]

def run(context):
    trialImages = context['trialImages']
    for index, image in enumerate(trialImages):
        context['imageList'][index].setImage(image)

    possible_targets = [0, 1, 2, 3]
    context['target'] = random.choice(possible_targets)
    context['nonTargetList'] = [x for x in possible_targets if x != context['target']]
    context['numberOfChanges'] = 0
    context['changeProb'] = 0.5
    context['attentionDuration'] = context['options']['blockLength']

    context['trialNum'] = 1

    return go(subModules, context)
