from modules import attentionChangeQuiz, attentionTask, attentionTaskFeedback, \
                    practiceAttentionInstructions

from lib.runner import go

subModules = [
    practiceAttentionInstructions,
    attentionTask,
    attentionChangeQuiz,
    attentionTaskFeedback
]

def run(context):
    practiceImages = context['practiceImages']
    imageList = context['imageList']
    for index, image in enumerate(practiceImages[:4]):
        imageList[index].setImage(image)

    context['target'] = 0
    context['changeSide1'] = practiceImages[0]
    context['changeSide2'] = practiceImages[-1]
    context['nonTargetList'] = [1, 2, 3]
    context['numberOfChanges'] = 2
    context['changeProb'] = __changeProb(context)
    context['attentionDuration'] = context['options']['practiceLength']

    context['trialNum'] = 0

    return go(subModules, context)

def __changeProb(context):
    duration = context['options']['blockLength']
    rotateMin = context['options']['rotateMin']
    rotateMax = context['options']['rotateMax']
    rotateSpeed = context['options']['speed']
    numberOfChanges = context['numberOfChanges']
    return ((duration/((rotateMin+rotateMax)/2.0))/4.0-numberOfChanges)/(duration/((rotateMin+rotateMax)/2))
