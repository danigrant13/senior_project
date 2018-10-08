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
    if trialNum > 0:
        # tally points
        pointTotal = 0
        if successes==0:
            vowelPoints = 0
        else:
            vowelPoints = round((successes / (successes + 2*mistakes))*50, 2)
        if actualChanges>0:
            if yesNo=='y':
                if whichImage.lower()==changeOptions[target].lower() and int(howManyTimes)==actualChanges:
                    imagePoints = 50
                else:
                    imagePoints = 10
            else:
                imagePoints = 0
        else:
            if yesNo=='y':
                imagePoints = 10
            else:
                imagePoints = 50
        score1 = visual.TextStim(win,'Points earned from vowel task: ' + str(vowelPoints) + ' / 50' +
            '\nPoints earned from image change task: ' + str(imagePoints) + ' / 50',
            pos=[0, 0], height=0.06, wrapWidth=1.5)
        pointTotal += vowelPoints + imagePoints
        score2 = visual.TextStim(win,'Total points earned on this trial: ' + str(vowelPoints + imagePoints) + ' / 100' +
            '\nRunning average of points per trial: ' + str(round(pointTotal/trialNum, 2)) + ' / 100',
            pos=[0, -0.2], height=0.1, wrapWidth=1.5)
        score1.draw()
        score2.draw()
    win.flip()
    proceedOrQuit(win)

    return context
