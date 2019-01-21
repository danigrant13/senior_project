from psychopy import core, event, visual
from lib.utils import proceedOrQuit
import random

##### Module inputs #######

# context['window']                         - reference to the primary window object
# context['imageList']                      - references to the primary image objects

# context['target']                         - speficied target, -1 no target (equal rotate probability)
# context['nonTargetList']                  - references to all other image indices
#                                           - optional if target is set to -1
# context['changeProb']                     - probability that target will rotate on each round

# context['numberOfChanges']                - number of times the target should flip
#                                           - set to 0 if no changes desired
# context['changeSide1']                    - the file name of the target image
# context['changeSide2']                    - the file name of the target mirror
#
# context['options']['blockLength']         - duration of the trial
# context['options']['letterInterval']      - duration the letter is displayed for
# context['options']['letterPause']         - time between letters
# context['options']['vowelProb']           - probability of a vowel
# context['options']['rotateMin']           - minimum time between rotations
# context['options']['rotateMax']           - max time between rotations
# context['options']['speed']               - frames per second of the image rotations

def __drawImages(imageList):
    for x in imageList:
        x.draw()

def __setLetter(letterStim, vowelList, consList, vowelProb):
    if random.random() <= vowelProb:
        letterStim.setText(random.choice(vowelList))
        return True
    else:
        letterStim.setText(random.choice(consList))
        return False

def shouldForceChange(duration, numberOfChanges, actualChanges, clock):
    if actualChanges == numberOfChanges:
        return False
    elif actualChanges < 1 and clock.getTime()>=duration/(numberOfChanges+1.0):
        return True
    elif actualChanges >= 1 and clock.getTime()>=duration*((numberOfChanges)/(numberOfChanges+1.0)):
        return True

    return False

def run(context):
    target = context['target']
    targetSide1 = True
    changeSide1 = context['changeSide1']
    changeSide2 = context['changeSide2']
    nonTargetList = context['nonTargetList']
    numberOfChanges = context['numberOfChanges']
    changeProb = context['changeProb']
    shouldChange = numberOfChanges > 0
    actualChanges = 0

    duration=context['attentionDuration']
    letterInterval = context['options']['letterInterval']
    letterPause = context['options']['letterPause']
    mistakes = successes = 0.0
    vowelProb = context['options']['vowelProb']
    vowelList = ['a','e','i','o','u']
    consList = ['b','c','d','f','g','h','j','k','m','n','p','q','r','s','t','v','w','x','y','z']

    # visuals
    win = context['window']
    imageList = context['imageList']
    letterStim = visual.TextStim(win, '')
    correctStim = visual.ImageStim(win,image='right.png',mask=None,units='norm',pos=[0,-0.5],size=[0.2,0.2])
    wrongStim = visual.ImageStim(win,image='wrong.png',mask=None,units='norm',pos=[0,-0.5],size=[0.2,0.2])

    #clocks
    globalClock = core.Clock()
    letterClock = core.Clock()
    rotateClock = core.Clock()

    #rotation
    currentRotator = 0
    rotateMin = context['options']['rotateMin']
    rotateMax = context['options']['rotateMax']
    rotateSpeed = context['options']['speed']
    rotateInterval = random.uniform(rotateMin, rotateMax)

    # status flags
    changed = False
    displayCorrect = False
    displayWrong = False
    feedbackRefresh = False
    isVowel = False
    letterCleared = False
    letterMissed = False
    letterRefresh = False
    letterRight = False
    letterWrong = False
    missFlag = False
    quizQuestions = False
    rotating = False
    forceChange = False

    event.clearEvents()

    trialInProgress = True
    while trialInProgress:
        #update orientation
        if rotating:
            imageList[currentRotator].setOri(
                imageList[currentRotator].ori + rotateSpeed
            )
            if forceChange:
                if imageList[currentRotator].ori == 180:
                    if targetSide1:
                        imageList[currentRotator].setImage(changeSide2)
                        targetSide1 = False
                    else:
                        imageList[currentRotator].setImage(changeSide1)
                        targetSide1 = True
                    actualChanges += 1
                    forceChange = False

        #check for letter change
        if letterClock.getTime() >= letterInterval:
            letterClock.reset()
            letterRefresh = True
            letterCleared = False
            if isVowel and not letterRight:
                mistakes+=1
                letterMissed = True
            displayCorrect = displayWrong = letterRight = letterWrong = False
            isVowel = __setLetter(letterStim, vowelList, consList, vowelProb)
        #check for new rotation
        if rotateClock.getTime() >= rotateInterval:
            rotateClock.reset()
            rotating = True
            rotateInterval = random.uniform(rotateMin, rotateMax)

            if shouldChange:
                if forceChange or (actualChanges < numberOfChanges and random.random() <= changeProb):
                    currentRotator = target
                    forceChange = True
                else:
                    currentRotator = random.choice(nonTargetList)
            elif target >= 0:
                if random.random() <= changeProb:
                    currentRotator = target
                else:
                    currentRotator = random.choice(nonTargetList)
            else:
                currentRotator = random.choice([0, 1, 2, 3])

        #update images
        if rotating:
            __drawImages(imageList)
            letterStim.draw()
            if letterWrong or letterMissed:
                wrongStim.draw()
            if letterRight:
                correctStim.draw()
            win.flip()
        elif letterRefresh:
            if letterClock.getTime() >= letterPause:
                __drawImages(imageList)
                letterStim.draw()
                letterRefresh = False
                win.flip()
            elif not letterCleared:
                letterCleared = True
                __drawImages(imageList)
                if letterMissed:
                    wrongStim.draw()
                win.flip()
        elif displayCorrect:
            __drawImages(imageList)
            letterStim.draw()
            correctStim.draw()
            win.flip()
        elif displayWrong:
            __drawImages(imageList)
            letterStim.draw()
            wrongStim.draw()
            win.flip()
        #refresh image update flags
        if imageList[currentRotator].ori == 360:
            imageList[currentRotator].setOri(0)
            rotating = False
        if letterClock.getTime() > letterPause:
            letterMissed = False
        if shouldForceChange(duration, numberOfChanges, actualChanges, globalClock) and not rotating:
            forceChange = True
        displayCorrect = displayWrong = False
        #continually check for key presses
        input = event.getKeys(keyList = ['lshift'], timeStamped=globalClock)
        if len(input) > 0:
            if isVowel and not letterRight:
                successes+=1
                displayCorrect = True
                letterRight = True
            elif not isVowel and not letterWrong:
                mistakes += 1
                displayWrong = True
                letterWrong = True
        #check for end of trial
        if globalClock.getTime() > duration:
            trialInProgress = False
    win.flip()
    core.wait(0.5)

    if shouldChange:
        imageList[target].setImage(changeSide1)

    trialNum = context['trialNum']
    context['attentionResults' + str(trialNum)] = {
        'successes': successes,
        'mistakes': mistakes,
        'actualChanges': actualChanges,
        'numberOfChanges': numberOfChanges,
        'target': target,
        'side1': changeSide1,
        'side2': changeSide2
    }
    context['numberOfChanges'] = 0
    context['changeSide1'] = ""
    context['changeSide2'] = ""
    context['changeProb'] = 0.25

    for image in imageList:
        image.setOri(0)

    return context
