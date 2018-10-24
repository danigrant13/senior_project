from psychopy import visual
from lib.utils import proceedOrQuit

def run(context):
    win = context['window']
    trialNum = context['trialNum']

    results = context['attentionResults']
    actualChanges = results['actualChanges']
    target = results['target']
    successes = results['successes']
    mistakes = results['mistakes']

    changeOptions = ['A', 'B', 'C', 'D']
    whichImage = context['changeQuizResults']['whichImage']
    yesNo = context['changeQuizResults']['yesNo']
    howManyTimes = context['changeQuizResults']['howManyTimes']

    if actualChanges > 0:
        side1 = results['side1']
        side2 = results['side2']
        feedbackImageA = visual.ImageStim(win,image=side1,mask=None,units='norm',pos=[-0.3,-0.72],size=[0.45,0.6])
        feedbackImageB = visual.ImageStim(win,image=side2,mask=None,units='norm',pos=[0.3,-0.72],size=[0.45,0.6])
        if actualChanges>1:
            feedbackChange = visual.TextStim(win,'Your performance on trial ' + str(trialNum) +
                '\n\nVowel task:\n     Correct responses: ' + str(int(successes)) +
                '\n     Incorrect responses: ' + str(int(mistakes)) + '\n\nImage change task:\n     Image ' +
                changeOptions[target] + ' changed ' + str(actualChanges) +
                ' times (see below).\n\n***Press the SPACE key to proceed when ready***',
                pos=[0,0.5],height=0.06)
        else:
            feedbackChange = visual.TextStim(win,'Your performance on trial ' + str(trialNum) +
                '\n\nVowel task:\n     Correct responses: ' + str(int(successes)) + '\n     Incorrect responses: ' +
                str(int(mistakes)) + '\n\nImage change task:\n     Image ' + changeOptions[target] + ' changed ' + 
                str(actualChanges) +
                ' time (see below).\n\n***Press the SPACE key to proceed when ready***',
                pos=[0,0.5],height=0.06)
        feedbackChange.draw()
        feedbackImageA.draw()
        feedbackImageB.draw()
    else:
        feedbackNoChange = visual.TextStim(win,'Your performance on trial ' + str(trialNum) +
                '\n\nVowel task:\n     Correct responses: ' + str(int(successes)) + 
                '\n     Incorrect responses: ' + str(int(mistakes)) + '\n\nImage change task:\n     ' +
                'No images changed during this trial\n\n***Press the SPACE key to proceed when ready***',
            pos=[0,0.5],height=0.06)
        feedbackNoChange.draw()
        feedbackImageA = visual.ImageStim(win,image='AM_3.jpg',mask=None,units='norm',pos=[-0.3,-0.72],size=[0.45,0.6])
        feedbackImageB = visual.ImageStim(win,image='AM_3.jpg',mask=None,units='norm',pos=[0.3,-0.72],size=[0.45,0.6])
        feedbackDebug = visual.TextStim(win, '(No target image on the practice trial)', pos=[0,-0.7],height=0.05)
    
    win.flip()
    proceedOrQuit(win)

    return context
