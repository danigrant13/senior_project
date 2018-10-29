from psychopy import event, visual
from lib.utils import proceedOrQuit

def __drawImages(imageList, markerList):
    for index in range(4):
        imageList[index].draw()
        markerList[index].draw()

def __dataHeaders():
    return [
        "Did any of the images change during the trial? (y/n)",
        "Which image changed? (A, B, C, D)",
        "How many times did this image change?",
        "Most frequent:",
        "2nd most frequent:",
        "3rd most frequent:",
        "Least frequent:"
    ]

def __setData(context):
    report = context['report']
    results = context['changeQuizResults']

    report['headers'] += __dataHeaders()
    report['data'] += [
        results['yesNo'],
        results['whichImage'],
        results['howManyTimes'],
        results['first'],
        results['second'],
        results['third'],
        results['fourth']
    ]

def run(context):
    win = context['window']
    imageList = context['imageList']
    markerList = context['markerList']
    question = """
    Did one of the images change during this trial? 
                         
                                     (y/n)"""
    quiz1 = visual.TextStim(win, question, pos=[0,0],height=0.06)

    quiz1.draw()
    __drawImages(imageList, markerList)
    win.flip()

    yesNo = '.'
    whichImage = '.'
    howManyTimes = '.'

    gettingInput = True
    quizQuestions = False
    while gettingInput:
        input = proceedOrQuit(win, keys = ['escape', 'y','n'])
        for thisKey in input:
            if thisKey in ['n']:
                yesNo = thisKey
                gettingInput = False
            if thisKey in ['y']:
                yesNo = thisKey
                gettingInput = False
                quizQuestions = True
    if quizQuestions:
        quiz1.setText('          Which image changed during the trial?' +
            '\n\n' +
            'Press the letter key that corresponds to the image.')
        quiz1.draw()
        __drawImages(imageList, markerList)
        win.flip()
        gettingInput = True
        while gettingInput:
            input = proceedOrQuit(win, keys = ['escape', 'a','b','c','d'])
            for thisKey in input:
                if thisKey in ['a','b','c','d']:
                    whichImage = thisKey
                    gettingInput = False
        quiz1.setText('How many times did image ' + thisKey + ' change during the trial?' +
        '\n\n          Please enter a number between 1 and 9')
        quiz1.draw()
        __drawImages(imageList, markerList)
        win.flip()
        gettingInput = True
        while gettingInput:
#changed from original for all key boards
            input = proceedOrQuit(win, keys = ['escape', '1','2','3','4','5','6','7','8','9'])
            for thisKey in input:
                if thisKey in ['1','2','3','4','5','6','7','8','9']:
                    howManyTimes = thisKey
                    gettingInput = False
    # forced choice of highest frequency image
    validKeys = ['a','b','c','d']
    # prompt for input of most frequent image to least frequent image
    text = """
     During the trial, it may have appeared that some images were rotating more frequently than 
        were other images. Please rank the 4 images from the trial in order of the image that 
                 rotated MOST frequently to the image that rotated LEAST frequently. 
                 For each choice, press the letter key that corresponds to the image."""
    
    forcePrompt = visual.TextStim(win, text,
        pos=[0, .2], height=0.06, wrapWidth=1.4)
    forceAns1 = visual.TextStim(win,'Most frequent: ', # most frequent image input
        pos=[0, -0.2], height=0.06, wrapWidth=1.4)
    forcePrompt.draw()
    forceAns1.draw()
    __drawImages(imageList, markerList)
    win.flip()
    gettingInput = True
    while gettingInput:
        input = event.waitKeys()
        for thisKey in input:
            if thisKey in validKeys:
                first = thisKey
                validKeys.remove(thisKey)
                gettingInput = False
    # second most frequent image prompt & input
    forceAns1.setText('Most frequent: ' + first)
    forceAns2 = visual.TextStim(win,'2nd most frequent: ',
        pos=[0, -0.3], height=0.06, wrapWidth=1.4)
    forcePrompt.draw()
    forceAns1.draw()
    forceAns2.draw()
    __drawImages(imageList, markerList)
    win.flip()
    gettingInput = True
    while gettingInput:
        input = event.waitKeys()
        for thisKey in input:
            if thisKey in validKeys:
                second = thisKey
                validKeys.remove(thisKey)
                gettingInput = False
    # third most frequent image prompt & input
    forceAns2.setText('2nd most frequent: ' + second)
    forceAns3 = visual.TextStim(win,'3rd most frequent: ',
        pos=[0, -0.4], height=0.06, wrapWidth=1.4)
    forcePrompt.draw()
    forceAns1.draw()
    forceAns2.draw()
    forceAns3.draw()
    __drawImages(imageList, markerList)
    win.flip()
    gettingInput = True
    while gettingInput:
        input = event.waitKeys()
        for thisKey in input:
            if thisKey in validKeys:
                third = thisKey
                validKeys.remove(thisKey)
                gettingInput = False
    # fourth most frequent image prompt & input
    forceAns3.setText('3rd most frequent: ' + third)
    forceAns4 = visual.TextStim(win,'4th most frequent: ',
        pos=[0, -0.5], height=0.06, wrapWidth=1.4)
    forcePrompt.draw()
    forceAns1.draw()
    forceAns2.draw()
    forceAns3.draw()
    forceAns4.draw()
    __drawImages(imageList, markerList)
    win.flip()
    gettingInput = True
    while gettingInput:
        input = event.waitKeys()
        for thisKey in input:
            if thisKey in validKeys:
                fourth = thisKey
                validKeys.remove(thisKey)
                gettingInput = False

    context['changeQuizResults'] = {
        'yesNo': yesNo,
        'whichImage': whichImage,
        'howManyTimes': howManyTimes,
        'first': first,
        'second': second,
        'third': third,
        'fourth': fourth
    }

    if context['collectData']:
        __setData(context)

    return context
