from psychopy import core, visual, event, gui
import time, random, math

#                                                     Initialization                                        #################

#dialogue box for experimenter to enter subject number, condition, & other variables
info = {'  Date':time.strftime("%m-%d-%Y@%H.%M", time.localtime()),
    '   Between':1,
    '   setCondition':1,
    '   Order':1,
    '    Subject number':1,
    'Vowel probability':0.3,
    'Letter change interval (secs)':2.75,
    'Rotation speed (degrees/frame)':15,
    'Min rotation interval (secs)':1.75,
    'Max rotation interval (secs)':3.75,
    ' Practice length (secs)':10,
    ' Block length (secs)':10,
    ' changeTrial length (secs)':10,
    'Letter blink duration (secs)':0.250}
infoDlg = gui.DlgFromDict(dictionary=info, title='Attention study', fixed=['Date'])

if not infoDlg.OK:
    print 'User Cancelled'
    core.quit()

#extract variables from dictionary
vowelProb = info['Vowel probability']
interval = info['Letter change interval (secs)']
speed = info['Rotation speed (degrees/frame)']
rotateMin = info['Min rotation interval (secs)']
rotateMax = info['Max rotation interval (secs)']
pracLength = info[' Practice length (secs)']
blockLength = info[' Block length (secs)']
changeTrialLength =info[' changeTrial length (secs)']
letterPause = info['Letter blink duration (secs)']

#check between condition for integer format
try: 
    between = int(info['   Between'])
except:
    print 'Error: Between must be set to 0 or 1!'
    print 'Between was set to: ' + str(info['   Between'])
    core.quit()

#check set condition for integer format
try: 
    condition = int(info['   setCondition'])
except:
    print 'Error: setCondition must be set to 0, 1, 2, or 3!'
    print 'setCondition was set to: ' + str(info['   setCondition'])
    core.quit()

#check order for integer format
try: 
    order = int(info['   Order'])
except:
    print 'Error: order must be set to 0, 1, 2, or 3!'
    print 'Order was set to: ' + str(info['   Order'])
    core.quit()

#check subject number for integer format
try: 
    subject = int(info['    Subject number'])
except:
    print 'Error: subject number must be a positive integer!'
    print 'Subject number was set to: ' + str(info['    Subject number'])
    core.quit()

#check between condition for range
if not between in range(0,2):
    print 'Error: Between must be set to 0 or 1!'
    print 'Between was set to: ' + str(info['   Between'])
    core.quit()

#check set condition for range
if not condition in range(0,4):
    print 'Error: setCondition must be set to 0, 1, 2, or 3!'
    print 'setCondition was set to: ' + str(info['   setCondition'])
    core.quit()

#check order for range
if not order in range(0,4):
    print 'Error: order must be set to 0, 1, 2, or 3!'
    print 'Order was set to: ' + str(info['   Order'])
    core.quit()

#check subject number for range
if not subject>=0:
    print 'Error: subject number must be a positive integer!'
    print 'Subject number was set to: ' + str(info['    Subject number'])
    core.quit()

#bring up initial screen and wait for key press
win = visual.Window([1600,900],rgb=(-1,-1,-1),allowGUI=False,winType='pyglet')
welcome = visual.TextStim(win,'When you are finished filling out the questionnaire form,' +
    ' press the SPACE key to begin the computer-based part of the experiment.' +
    '\n\n(Experimenter: press escape to quit.)')
welcome.draw();
win.flip()
input = event.waitKeys()
if 'escape' in input:
    print input
    win.close()
    core.quit()

# function for converting key names to nominal responses
def translate(x):
    options = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'tab': -0.5, # x-coordinate for "left" response
        'backslash': 0.5, # x-coordinate for "right" response
        'y': 'y',
        'n': 'n',
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'm': 'm',
        'f': 'f',
        'space': 'space', #NEXT/SPACE button
        'escape': 'escape',
        'lshift': 'lshift' #choosing VOWEL/SHIFT button
    }
    
    if not x in options:
        return '`'
        
    return options[x]

#                                               Instructions for Experiment                                  ##################

# instruction screen 1
instructions1 = visual.TextStim(win,'In this experiment, you will be presented' +
    ' with a steady stream of letters at the center of the screen,surrounded by 4' + 
    'images which will periodically rotate and sometimes change to a new image.' +
    '\n\nThe basic visual layout of each trial will be something like this:' +
    '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress the SPACE key to advance to ' +
    'the next screen and continue reading the instructions.',
    pos=[0, 0],height=0.06,wrapWidth=1.5)
layout = visual.ImageStim(win,image='layout.bmp',mask=None,units='norm',pos=[0, -0.1],size=[0.88, 1.0])
instructions1.draw()
layout.draw()
win.flip()

# wait for user input -- close experiment if 'escape'
input = event.waitKeys(keyList = ['escape', 'space'])
if input == ['escape']:
    print input
    win.close()
    core.quit()

# instrucion screen 2
instructions1 = visual.TextStim(win,'You have two tasks during this experiment:',
    pos=[0,0.85],height=0.06,wrapWidth=1.5)
instructions2 = visual.TextStim(win, '1. Press the LEFT SHIFT key whenever the letter ' +
    ' currently displayed in the center of the screen is a SHIFT. For example, you' +
    ' should press the key if the letter "a" appears on the screen, but not the letter "f".' + 
    '\n\n2. Each time an image rotates, there is a small chance that it will change to a similar' +
    ' but different image. At the end of each experimental trial, you will be asked how many image' +
    ' changes there were during the trial.',
    pos=[0,0.50],height=0.06,wrapWidth=1.3)
demoPic = visual.ImageStim(win,image='demo_a.jpg',mask=None,units='norm',pos=[0,-0.1],size=[0.45,0.6])
instructions3 = visual.TextStim(win,'The above image will demonstrate what you are looking for each' +
    ' time an image rotates. Press the SPACE key to watch the image rotate and change to a new image.',
    pos=[0,-0.65],height=0.06,wrapWidth=1.5)
demoPic.draw()
instructions1.draw()
instructions2.draw()
instructions3.draw()
win.flip()

#wait for key press -- abort on escape
input = event.waitKeys()
if 'escape' in input:
    print input
    win.close()
    core.quit()
gettingInput = True
a = True
while gettingInput:
    #rotate the demo image, changing the image halfway through
    for x in range(0,361, speed):
        demoPic.setOri(x)
        if x==180:
            if a:
                demoPic.setImage('demo_b.jpg')
                a = False
            else:
                demoPic.setImage('demo_a.jpg')
                a = True
        demoPic.draw()
        instructions1.draw()
        instructions2.draw()
        instructions3.draw()
        win.flip()
    instructions3.setText("To rotate and change the image again, press the BACK key." +
        "\n\nCan you find what is changing in the picture above each time the image rotates?" + 
        "\nPress the SPACE key to reveal the answer...")
    demoPic.draw()
    instructions1.draw()
    instructions2.draw()
    instructions3.draw()
    win.flip()
    #wait for key press -- if 'escape' pressed close program
    input = event.waitKeys()
    if 'escape' in input:
        print input
        win.close()
        core.quit()
    elif 'space' in input:
        gettingInput = False

# introduction screen 3
instructions3 = visual.TextStim(win,'ANSWER: Watch the yellow bag sitting at the feet of the man on the left.' + 
    '\n\nPress the BACK key to rotate the image.',
    pos=[0,-0.65],height=0.06,wrapWidth=1.5)
demoPic.draw()
instructions1.draw()
instructions2.draw()
instructions3.draw()
win.flip()

#wait for user input, if 'escape' close program
input = event.waitKeys()
if 'escape' in input:
    print input
    win.close()
    core.quit()
gettingInput = True
while gettingInput:
    #rotate the demo image, changing the image halfway through
    for x in range(0,361, speed):
        demoPic.setOri(x)
        if x==180:
            if a:
                demoPic.setImage('demo_b.jpg')
                a = False
            else:
                demoPic.setImage('demo_a.jpg')
                a = True
        demoPic.draw()
        instructions1.draw()
        instructions2.draw()
        instructions3.draw()
        win.flip()
    instructions3.setText("ANSWER: Watch the yellow bag sitting at the feet of the man on the left." +
        "\nWhen you have finished reading the instructions on this screen, press the SPACE key to advance"+
        " to the next screen.\nDon't worry if you don't fully understand both of the tasks yet. We will" +
        "explain them more on the next screen, and you will also get a chance to practice before starting" +
        " the main experiment.")
    demoPic.draw()
    instructions1.draw()
    instructions2.draw()
    instructions3.draw()
    win.flip()
    #wait for key press -- abort on escape
    input = event.waitKeys()
    if 'escape' in input:
        print input
        win.close()
        core.quit()
    elif 'space' in input:
        gettingInput = False

# instruction screen 4
def screen4():
    instructions4 = visual.TextStim(win,'Many of the image changes that you will be looking for can be quite' + 
        ' difficult to detect. You must pay attention to the images closely to successfully detect the changes.' + 
        '\n\nThere are two more things you should know about the image changes.' + 
        '\n\nFirst, not every trial of the experiment will have an image change. Some trials will have an image change,' + 
        ' other trials will have no image changes, and some trials will have multiple image changes.' + 
        '\n\nSecond, when an image DOES change, it will only ever do so during one of the rotations that occur every couple' + 
        ' of seconds. So the best way to successfully detect the image changes is to check each image after it rotates to see' + 
        ' if anything has changed or not. If it has, make a mental note of which image it is and how many times it changes over' + 
        ' the course of the trial. We will ask you about this at the end of each trial.' + 
        '\n\n\n\nPress the SPACE key to continue reading the instructions.',
        pos=[0, 0], height=0.06, wrapWidth=1.5)
    instructions4.draw()
    win.flip()

# instruction screen 5
def screen5():
    instructions4 = visual.TextStim(win,'\n\n\n\nYou will now complete two brief (about 30 seconds) PRACTICE trials.' + 
        '\n\nWe will NOT be keeping track of your performance on these practice trials. The purpose of the practice' + 
        ' trials is simply to help you become familiar with the experimental procedure. After the practice trials you' + 
        ' will begin the main experimental trials.' +
        '\n\nRemember your two tasks:' + 
        '\n     1. Press the SHIFT key when the letter in the center of the screen is a SHIFT.' + 
        '\n     2. Keep track of how many times any image changes over the course of the trial.' +
        '\n\nSome of the images that you will view in this experiment will be somewhat disturbing. Others will be more pleasant.' + 
        ' If you have any questions or concerns about the experiment, please notify the experimenter.' + 
        '\n\n\n\nPress the SPACE key to begin the first practice trial.',
        pos=[0, 0], height=0.06, wrapWidth=1.5)
    instructions4.draw()
    win.flip()

# cycle through instruction screens
screens = [screen4, screen5]
currentScreen = 0
while currentScreen < 2:
    screens[currentScreen]()
    input = event.waitKeys(keyList = ['escape', 'lshift', 'space'])
    if input == ['escape']:
        print input
        win.close()
        core.quit()
    if input == ['lshift']:
        if currentScreen > 0: currentScreen += -1
    if input == ['space']:
        currentScreen += 1

#                                                    Define miscellanious variables                              ################

#create image list, letter lists and define some other variables
setList = [['9140_a.jpg','9181_a.jpg','9500_a.jpg','9571_a.jpg'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['3110_a.jpg','3030_a.jpg','3071_a.jpg','9252_a.jpg'],
    ['2141_a.jpg','9007_a.jpg','9430_a.jpg','2900_a.jpg'],
    ['3350_a.jpg','3301_a.jpg','2800_a.jpg','9040_a.jpg'],
    ['.', '.', '.', '.'],
    ['7705_a.jpg','7035_a.jpg','7030_a.jpg','7235_a.jpg'],
    ['.', '.', '.', '.'],
    ['7233_a.jpg','7217_a.jpg','7090_a.jpg','7000_a.jpg'],
    ['7025_a.jpg','7040_a.jpg','7050_a.jpg','7150_a.jpg'],
    ['5510_a.jpg','5520_a.jpg','5500_a.jpg','5533_a.jpg'],
    ['.', '.', '.', '.'],
    ['1750_a.jpg','1460_a.jpg','1440_a.jpg','1710_a.jpg'],
    ['2050_a.jpg','2040_a.jpg','2070_a.jpg','2058_a.jpg'],
    ['.', '.', '.', '.'],
    ['5910_a.jpg','7502_a.jpg','8170_a.jpg','8501_a.jpg'],
    ['8034_a.jpg','8180_a.jpg','5629_a.jpg','8200_a.jpg']]

targetList = [[0,3,1,2],
                  ['.', '.', '.', '.'],
                  ['.', '.', '.', '.'],
                  [1,2,0,3],
                  [2,1,3,0],
                  [3,0,2,1],
                  ['.', '.', '.', '.'],
                  [0,3,1,2],
                  ['.', '.', '.', '.'],
                  [1,2,0,3],
                  [2,1,3,0],
                  [3,0,2,1],
                  ['.', '.', '.', '.'],
                  [0,3,1,2],
                  [1,2,0,3],
                  ['.', '.', '.', '.'],
                  [2,1,3,0],
                  [3,0,2,1]]

rotateProbMatrix = [0.25, 0.55]

ratingMatrix = [[['.' for _ in range(3)] for _ in range(4)] for _ in range(18)]

freqMatrix = [[0 for _ in range(4)] for _ in range(18)]

usedNegativeList = []

unusedNegativeList = [0,3,4,5]
usedNeutralList = []
unusedNeutralList = [7,9,10,11]
usedPositiveList = []
unusedPositiveList = [13,14,16,17]
image0 = visual.ImageStim(win,image='9420_a.jpg',mask=None,units='norm',pos=[-0.7,0.7],size=[0.375,0.5])
image1 = visual.ImageStim(win,image='9520_a.jpg',mask=None,units='norm',pos=[0.7,0.7],size=[0.375,0.5])
image2 = visual.ImageStim(win,image='2710_a.jpg',mask=None,units='norm',pos=[-0.7,-0.7],size=[0.375,0.5])
image3 = visual.ImageStim(win,image='9432_a.jpg',mask=None,units='norm',pos=[0.7,-0.7],size=[0.375,0.5])
imageList = [image0,image1,image2,image3]
vowelList = ['a','e','i','o','u'] 
consList = ['b','c','d','f','g','h','j','k','m','n','p','q','r','s','t','v','w','x','y','z'] #lower-case L is omitted
temp = '.'
changeA = '.'
changeB = '.'

#define marker lists...                                                                   Why are there two lists?
markerA = visual.TextStim(win,'',pos=[-0.8,0.38],height=0.13)
markerB = visual.TextStim(win,'',pos=[0.8,0.38],height=0.13)
markerC = visual.TextStim(win,'',pos=[-0.8,-0.38],height=0.13)
markerD = visual.TextStim(win,'',pos=[0.8,-0.38],height=0.13)
markerList = [markerA, markerB, markerC, markerD]
markA = visual.TextStim(win,'A',pos=[-0.8,0.38],height=0.13)
markB = visual.TextStim(win,'B',pos=[0.8,0.38],height=0.13)
markC = visual.TextStim(win,'C',pos=[-0.8,-0.38],height=0.13)
markD = visual.TextStim(win,'D',pos=[0.8,-0.38],height=0.13)
markList = [markA, markB, markC, markD]

#initialize various boolean "flag" variables
changedOnce = changedTwice = letterRefresh = feedbackRefresh = rotating = displayRight = displayWrong = letterRight = letterWrong = missFlag = quizQuestions = letterMissed = letterCleared = forceChange = changed = False
currentSet = target = 0
mistakes = successes = 0.0
rotateProb = 0.25
if target==0:
    nonTargetList = [1,2,3]
elif target==1:
    nonTargetList = [0,2,3]
elif target==2:
    nonTargetList = [0,1,3]
elif target==3:
    nonTargetList = [0,1,2]
if random.random()<=rotateProb:
    currentRotator = target
else:
    currentRotator = random.choice(nonTargetList)
imageDict = ['A','B','C','D']
#create empty list to hold answers to change quizzes
changeMatrix = []
#keep track of all vowel ask responses
totalSuccesses = totalMistakes = 0

# function for converting picture letters to 0-3 number range
def letterToNum(x):
    return {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
    }[x]

#                                                  gatherRatings function                                       ###################


def gatherRatings(practice):
    # define stuff
    global currentSet
    ratingInstructions1 = visual.TextStim(win,'Please take just a minute or so to answer a few questions' +
    ' about your reaction to these four images during the trial.\nFor each question, please enter a number' + 
    ' between 0 and 9, with 0 being "Not at all" and 9 being "The most possible."',
        pos=[0,0.65],height=0.05,wrapWidth=0.8)
    ratingInstructions2 = visual.TextStim(win,'Press the SPACE key after each response to continue.',
        pos=[0,-0.65],height=0.05,wrapWidth=0.8)
    rating1 = visual.TextStim(win,'During the trial, how intense was your emotional reaction to this image?',
        pos=[0,0.4],height=0.06,wrapWidth=1.5)
    rating2 = visual.TextStim(win,'During the trial, how interesting did you find this image?',
        pos=[0,0.1],height=0.06,wrapWidth=1.5)
    rating3 = visual.TextStim(win,'How much do you like the scene in this image?',
        pos=[0,-0.2],height=0.06,wrapWidth=1.5)
    ratingQuestions = [rating1, rating2, rating3]
    rating1a = visual.TextStim(win,'Your answer: ',
        pos=[0,0.30],height=0.06,wrapWidth=1.5)
    rating2a = visual.TextStim(win,'Your answer: ',
        pos=[0,0],height=0.06,wrapWidth=1.5)
    rating3a = visual.TextStim(win,'Your answer: ',
        pos=[0,-0.3],height=0.06,wrapWidth=1.5)
    ratingPrompts = [rating1a, rating2a, rating3a]
    promptAddons = [['']*3 for _ in range(4)]
    # 2-lists of pictureNums and questionNums
    picByQuestion = [[a, b] for a in range(4) for b in range(3)]
    
    # define function to draw stuff
    def drawRatings(pictureNum, questionNum):
        ratingInstructions1.draw()
        ratingInstructions2.draw()
        for q in range(questionNum+1):
            ratingPrompts[q].setText('Your answer: ' + promptAddons[picByQuestion[currentScreen][0]][q])
            ratingQuestions[q].draw()
            ratingPrompts[q].draw()
        for x in imageList:
            x.setOri(0)
        imageList[pictureNum].draw()
        for x in markerList:
            x.draw()
        win.flip()

    # cycle through ratings
    currentScreen = 0
    while currentScreen < len(picByQuestion):
        # draw stuff
        drawRatings(picByQuestion[currentScreen][0], picByQuestion[currentScreen][1])
        # collect input
        input = event.waitKeys(keyList = ['escape','lshift','space','1','2','3','4','5','6','7','8','9','0'])
        # process input
        for thisKey in input:
            if translate(thisKey) in [str(x) for x in range(10)]:
                # update question prompt and store temp variable
                promptAddons[picByQuestion[currentScreen][0]][picByQuestion[currentScreen][1]] = translate(thisKey)
                try:
                    temp = int(translate(thisKey))
                except:
                    temp = ''
                if thisKey=='space':
                    gettingInput = False
                try:
                    temp = int(temp)
                except:
                    temp = ''
                if not practice:
                    ratingMatrix[currentSet][picByQuestion[currentScreen][0]][picByQuestion[currentScreen][1]] = temp
                currentScreen += 1
                temp = ''
            if input == ['escape']:
                print input
                win.close()
                core.quit()
            if input == ['lshift']:
                if currentScreen > 0: currentScreen += -1

#                               noChangeTrial function                                        #######################

def noChangeTrial(blockNum):
    #reset variables
    global currentSet, mistakes, successes, currentRotator, usedPositiveList,usedNeutralList, usedNegativeList, unusedPositiveList, unusedNeutralList, unusedNegativeList
    letterRefresh = feedbackRefresh = rotating = displayRight = displayWrong = letterRight = letterWrong = missFlag = quizQuestions = letterMissed = letterCleared = changed = False

    #global mistakes, successes
    mistakes = successes = 0.0

    a = True

    #global currentRotator
    # reminder to locate VOWEL key = 'lshift'
    remind = visual.TextStim(win,'About to begin trial ' + str(trialNum) + ' out of 18.' +
    '\n\nPlease take this moment to locate the SHIFT key on the keyboard.' + 
    '\n\nWhen ready, press the SPACE key to begin the trial.',

    pos=[0, 0], height=0.06, wrapWidth=1.5)

    remind.draw();

    win.flip()

    input = event.waitKeys(keyList = ['space','escape'])
    if 'escape' in input:
        print input
        win.close()
        core.quit()
    
    # set images

    if blockNum<1:
        rotateProb = 0.25 #no rotation bias on practice trials...
        target = 0 #...so it doesn't matter which image is the target
        image0 = visual.ImageStim(win,image='9420_a.jpg',mask=None,units='norm',pos=[-0.7,0.7],size=[0.375,0.5])
        image1 = visual.ImageStim(win,image='9520_a.jpg',mask=None,units='norm',pos=[0.7,0.7],size=[0.375,0.5])
        image2 = visual.ImageStim(win,image='2710_a.jpg',mask=None,units='norm',pos=[-0.7,-0.7],size=[0.375,0.5])
        image3 = visual.ImageStim(win,image='9432_a.jpg',mask=None,units='norm',pos=[0.7,-0.7],size=[0.375,0.5])

    else:
        rotateProb = rotateProbMatrix[between]
        #randomly select current image set from unused image blocks
        if blockNum==1:
            if order==0 or order==1:
                currentSet = random.choice(unusedNeutralList)
                usedNeutralList.append(currentSet)
                unusedNeutralList.remove(currentSet)
            elif order==2:
                currentSet = random.choice(unusedPositiveList)
                usedPositiveList.append(currentSet)
                unusedPositiveList.remove(currentSet)
            elif order==3:
                currentSet = random.choice(unusedNegativeList)
                usedNegativeList.append(currentSet)
                unusedNegativeList.remove(currentSet)
        elif blockNum==2:
            if order==0 or order==3:
                currentSet = random.choice(unusedPositiveList)
                usedPositiveList.append(currentSet)
                unusedPositiveList.remove(currentSet)
            elif order==1 or order==2:
                currentSet = random.choice(unusedNegativeList)
                usedNegativeList.append(currentSet)
                unusedNegativeList.remove(currentSet)
        elif blockNum==3:
            if order==0:
                currentSet = random.choice(unusedNegativeList)
                usedNegativeList.append(currentSet)
                unusedNegativeList.remove(currentSet)
            elif order==1:
                currentSet = random.choice(unusedPositiveList)
                usedPositiveList.append(currentSet)
                unusedPositiveList.remove(currentSet)
            elif order==2 or order==3:
                currentSet = random.choice(unusedNeutralList)
                usedNeutralList.append(currentSet)
                unusedNeutralList.remove(currentSet)
        target = targetList[currentSet][condition]
        print 'currentSet: ', currentSet
        print 'target: ', target
        #update image textures
        index = 0
        for x in imageList:
            x.setImage(setList[currentSet][index])
            index += 1
    if target==0:
        nonTargetList = [1,2,3]
    elif target==1:
        nonTargetList = [0,2,3]
    elif target==2:
        nonTargetList = [0,1,3]
    elif target==3:
        nonTargetList = [0,1,2]
    
    #draw initial images, start clocks, etc.
    for x in imageList:
        x.draw()
    globalClock = core.Clock()
    letterClock = core.Clock()
    rotateClock = core.Clock()
    letter = visual.TextStim(win)
    if random.random()<=vowelProb:
        letter.setText(random.choice(vowelList))
        isVowel = True
    else:
        letter.setText(random.choice(consList))
        isVowel = False
    currentRotateInt = random.uniform(rotateMin, rotateMax)
    right = visual.ImageStim(win,image='right.png',mask=None,units='norm',pos=[0,-0.5],size=[0.2,0.2])
    wrong = visual.ImageStim(win,image='wrong.png',mask=None,units='norm',pos=[0,-0.5],size=[0.2,0.2])
    letter.draw()
    win.flip()
    event.clearEvents()
    
    #begin trial
    if blockNum<1:
        duration = pracLength
    else:
        duration = blockLength
    trialInProgress = True
    while trialInProgress:
        #update orientation
        if rotating:
            imageList[currentRotator].setOri(imageList[currentRotator].ori+speed)
        #check for letter change
        if letterClock.getTime()>=interval:
            letterClock.reset()
            letterRefresh = True
            letterCleared = False
            if isVowel and not letterRight:
                mistakes+=1
                letterMissed = True
            displayRight = displayWrong = letterRight = letterWrong = False
            if random.random()<=vowelProb:
                oldLetter = letter.text
                while letter.text==oldLetter:
                    letter.setText(random.choice(vowelList))
                isVowel = True
            else:
                oldLetter = letter.text
                while letter.text==oldLetter:
                    letter.setText(random.choice(consList))
                isVowel = False
        
        #check for new rotation
        if rotateClock.getTime()>=currentRotateInt:
            rotateClock.reset()
            rotating = True
            currentRotateInt = random.uniform(rotateMin, rotateMax)
            if random.random()<=rotateProb:
                currentRotator = target
            else:
                currentRotator = random.choice(nonTargetList)
            freqMatrix[currentSet][currentRotator] += 1
                
        #update images
        if rotating:
            for x in imageList:
                x.draw()
            letter.draw()
            if letterWrong or letterMissed:
                wrong.draw()
            if letterRight:
                right.draw()
            win.flip()
        elif letterRefresh:
            if letterClock.getTime()>=letterPause:
                for x in imageList:
                    x.draw()
                letter.draw()
                letterRefresh = False
                win.flip()
            elif not letterCleared:
                letterCleared = True
                for x in imageList:
                    x.draw()
                if letterMissed:
                    wrong.draw()
                win.flip()
        elif displayRight:
            for x in imageList:
                x.draw()
            letter.draw()
            right.draw()
            win.flip()
        elif displayWrong:
            for x in imageList:
                x.draw()
            letter.draw()
            wrong.draw()
            win.flip()

        #refresh image update flags
        if imageList[currentRotator].ori==360:
            imageList[currentRotator].setOri(0)
            rotating = False
        if letterClock.getTime()>letterPause:
            letterMissed = False
        displayRight = displayWrong = False
        
        #continually check for key presses
        input = event.getKeys(keyList = ['lshift'], timeStamped=globalClock)
        if len(input)>0:
            if isVowel and not letterRight:
                successes+=1
                displayRight = True
                letterRight = True
            elif not isVowel and not letterWrong:
                mistakes+=1
                displayWrong = True
                letterWrong = True

        #check for end of trial
        if globalClock.getTime()>duration:
            trialInProgress = False
    win.flip()
    core.wait(0.5)

#                                 changeTrial function                                  #################

def changeTrial(whichChange,numberOfChanges):
    #reset variables
    changedOnce = changedTwice = forceChange = letterRefresh = feedbackRefresh = rotating = displayRight = displayWrong = letterRight = letterWrong = missFlag = quizQuestions = letterMissed = letterCleared = changed = False
    global currentSet, mistakes, successes, currentRotator, changeA, changeB, target, trialNum
    mistakes = successes = 0.0
    if whichChange<0:
        rotateProb = 0.0 #correct target rotation probablity on short practice trial by forcing to 0
    else:
        # correct rotation probability to account for forced target changes
        rotateProb = ((changeTrialLength/((rotateMin+rotateMax)/2.0))/4.0 - numberOfChanges)/(changeTrialLength/((rotateMin+rotateMax)/2)) 
        print 'changeTrial rotateProb: ', rotateProb
    a = True # changing image starts on "a" side

    #global currentRotator
    currentRotateInt = random.uniform(rotateMin, rotateMax)
    
    # reminder to locate VOWEL key
    remind = visual.TextStim(win,'About to begin trial ' + str(trialNum) + ' out of 18.' +
    '\n\nPlease take this moment to locate the SHIFT key on the keyboard.' + 
    '\n\nWhen ready, press the SPACE key to begin the trial.',
    pos=[0, 0], height=0.06, wrapWidth=1.5)
    remind.draw();
    win.flip()
    input = event.waitKeys(keyList = ['space','escape'])
    if 'escape' in input:
        print input
        win.close()
        core.quit()

    #draw initial images, reset clocks, etc.
    if whichChange<0: #practice trial
        image0.setImage('5740_a.jpg')
        image1.setImage('7187_a.jpg')
        image2.setImage('2880_a.jpg')
        image3.setImage('7100_a.jpg')
        changeA = '2880_a.jpg'
        changeB = '2880_b.jpg'
        target = 2
    elif whichChange==0:
        if order==0 or order==1:
            currentSet = 6
            image0.setImage('2480_a.jpg')
            image1.setImage('2190_a.jpg')
            image2.setImage('2570_a.jpg')
            image3.setImage('2890_a.jpg')
            changeA = '2190_a.jpg'
            changeB = '2190_b.jpg'
            target = 1
        elif order==2:
            currentSet = 12
            image0.setImage('7390_a.jpg')
            image1.setImage('7282_a.jpg')
            image2.setImage('7460_a.jpg')
            image3.setImage('7400_a.jpg')
            changeA = '7390_a.jpg'
            changeB = '7390_b.jpg'
            target = 0
        elif order==3:
            currentSet = 1
            image0.setImage('2205_a.jpg')
            image1.setImage('9421_a.jpg')
            image2.setImage('6243_a.jpg')
            image3.setImage('9921_a.jpg')
            changeA = '9921_a.jpg'
            changeB = '9921_b.jpg'
            target = 3
    elif whichChange==1:
        if order==0 or order==1:
            currentSet = 8
            image0.setImage('7002_a.jpg')
            image1.setImage('7950_a.jpg')
            image2.setImage('7006_a.jpg')
            image3.setImage('6150_a.jpg')
            changeA = '6150_a.jpg'
            changeB = '6150_b.jpg'
            target = 3
        elif order==2:
            currentSet = 15
            image0.setImage('5870_a.jpg')
            image1.setImage('7545_a.jpg')
            image2.setImage('5750_a.jpg')
            image3.setImage('5220_a.jpg')
            changeA = '7545_a.jpg'
            changeB = '7545_b.jpg'
            target = 1
        elif order==3:
            currentSet = 2
            image0.setImage('3550_a.jpg')
            image1.setImage('6212_a.jpg')
            image2.setImage('9400_a.jpg')
            image3.setImage('6838_a.jpg')
            changeA = '3550_a.jpg'
            changeB = '3550_b.jpg'
            target = 0
    elif whichChange==2:
        if order==0 or order==3:
            currentSet = 12
            image0.setImage('7390_a.jpg')
            image1.setImage('7282_a.jpg')
            image2.setImage('7460_a.jpg')
            image3.setImage('7400_a.jpg')
            changeA = '7390_a.jpg'
            changeB = '7390_b.jpg'
            target = 0
        elif order==1 or order==2:
            currentSet = 1
            image0.setImage('2205_a.jpg')
            image1.setImage('9421_a.jpg')
            image2.setImage('6243_a.jpg')
            image3.setImage('9921_a.jpg')
            changeA = '9921_a.jpg'
            changeB = '9921_b.jpg'
            target = 3
    elif whichChange==3:
        if order==0 or order==3:
            currentSet = 15
            image0.setImage('5870_a.jpg')
            image1.setImage('7545_a.jpg')
            image2.setImage('5750_a.jpg')
            image3.setImage('5220_a.jpg')
            changeA = '7545_a.jpg'
            changeB = '7545_b.jpg'
            target = 1
        elif order==1 or order==2:
            currentSet = 2
            image0.setImage('3550_a.jpg')
            image1.setImage('6212_a.jpg')
            image2.setImage('9400_a.jpg')
            image3.setImage('6838_a.jpg')
            changeA = '3550_a.jpg'
            changeB = '3550_b.jpg'
            target = 0
    elif whichChange==4:
        if order==0:
            currentSet = 1
            image0.setImage('2205_a.jpg')
            image1.setImage('9421_a.jpg')
            image2.setImage('6243_a.jpg')
            image3.setImage('9921_a.jpg')
            changeA = '9921_a.jpg'
            changeB = '9921_b.jpg'
            target = 3
        elif order==1:
            currentSet = 12
            image0.setImage('7390_a.jpg')
            image1.setImage('7282_a.jpg')
            image2.setImage('7460_a.jpg')
            image3.setImage('7400_a.jpg')
            changeA = '7390_a.jpg'
            changeB = '7390_b.jpg'
            target = 0
        elif order==2 or order==3:
            currentSet = 6
            image0.setImage('2480_a.jpg')
            image1.setImage('2190_a.jpg')
            image2.setImage('2570_a.jpg')
            image3.setImage('2890_a.jpg')
            changeA = '2190_a.jpg'
            changeB = '2190_b.jpg'
            target = 1
    elif whichChange==5:
        if order==0:
            currentSet = 2
            image0.setImage('3550_a.jpg')
            image1.setImage('6212_a.jpg')
            image2.setImage('9400_a.jpg')
            image3.setImage('6838_a.jpg')
            changeA = '3550_a.jpg'
            changeB = '3550_b.jpg'
            target = 0
        elif order==1:
            currentSet = 15
            image0.setImage('5870_a.jpg')
            image1.setImage('7545_a.jpg')
            image2.setImage('5750_a.jpg')
            image3.setImage('5220_a.jpg')
            changeA = '7545_a.jpg'
            changeB = '7545_b.jpg'
            target = 1
        elif order==2 or order==3:
            currentSet = 8
            image0.setImage('7002_a.jpg')
            image1.setImage('7950_a.jpg')
            image2.setImage('7006_a.jpg')
            image3.setImage('6150_a.jpg')
            changeA = '6150_a.jpg'
            changeB = '6150_b.jpg'
            target = 3
    if target==0:
        nonTargetList = [1,2,3]
    elif target==1:
        nonTargetList = [0,2,3]
    elif target==2:
        nonTargetList = [0,1,3]
    elif target==3:
        nonTargetList = [0,1,2]
    for x in imageList:
        x.draw()
    globalClock = core.Clock()
    letterClock = core.Clock()
    rotateClock = core.Clock()
    letter = visual.TextStim(win)
    right = visual.ImageStim(win,image='right.png',mask=None,units='norm',pos=[0,-0.5],size=[0.2,0.2])
    wrong = visual.ImageStim(win,image='wrong.png',mask=None,units='norm',pos=[0,-0.5],size=[0.2,0.2])
    if random.random()<=vowelProb:
        letter.setText(random.choice(vowelList))
        isVowel = True
    else:
        letter.setText(random.choice(consList))
        isVowel = False
    letter.draw()
    win.flip()

    #begin trial
    if whichChange<0:
        duration = pracLength
    else:
        duration = changeTrialLength
    trialInProgress = True
    while trialInProgress:

        #update orientation
        if rotating:
            imageList[currentRotator].setOri(imageList[currentRotator].ori+speed)
            if forceChange:
                if imageList[currentRotator].ori==180:
                    if a:
                        imageList[currentRotator].setImage(changeB)
                        a = False
                    else:
                        imageList[currentRotator].setImage(changeA)
                        a = True
                    forceChange = False

        #check for letter change
        if letterClock.getTime()>=interval:
            letterClock.reset()
            letterRefresh = True
            letterCleared = False
            if isVowel and not letterRight:
                mistakes+=1
                letterMissed = True
            displayRight = displayWrong = letterRight = letterWrong = False
            if random.random()<=vowelProb:
                oldLetter = letter.text
                while letter.text==oldLetter:
                    letter.setText(random.choice(vowelList))
                isVowel = True
            else:
                oldLetter = letter.text
                while letter.text==oldLetter:
                    letter.setText(random.choice(consList))
                isVowel = False

        #check for new rotation
        if rotateClock.getTime()>=currentRotateInt:
            rotateClock.reset()
            rotating = True
            currentRotateInt = random.uniform(rotateMin, rotateMax)
            if forceChange:
                currentRotator = target
            else:
                if random.random()<=rotateProb:
                    currentRotator = target
                else:
                    currentRotator = random.choice(nonTargetList)

        #update images
        if rotating:
            for x in imageList:
                x.draw()
            letter.draw()
            if letterWrong or letterMissed:
                wrong.draw()
            if letterRight:
                right.draw()
            win.flip()
        elif letterRefresh:
            if letterClock.getTime()>=letterPause:
                for x in imageList:
                    x.draw()
                letter.draw()
                letterRefresh = False
                win.flip()
            elif not letterCleared:
                letterCleared = True
                for x in imageList:
                    x.draw()
                if letterMissed:
                    wrong.draw()
                win.flip()
        elif displayRight:
            for x in imageList:
                x.draw()
            letter.draw()
            right.draw()
            win.flip()
        elif displayWrong:
            for x in imageList:
                x.draw()
            letter.draw()
            wrong.draw()
            win.flip()

        #refresh image update flags
        if imageList[currentRotator].ori==360:
            imageList[currentRotator].setOri(0)
            rotating = False
        if letterClock.getTime()>letterPause:
            letterMissed = False
        if globalClock.getTime()>=duration/(numberOfChanges+1.0) and not changedOnce and not rotating:
            forceChange = changedOnce = True
        if numberOfChanges>1:
            if globalClock.getTime()>=duration*((numberOfChanges)/(numberOfChanges+1.0)) and not changedTwice and not rotating:
                forceChange = changedTwice = True
        displayRight = displayWrong = False

        #continually check for key presses
        input = event.getKeys(keyList = ['lshift'], timeStamped=globalClock)
        if len(input)>0:
            if isVowel and not letterRight:
                successes+=1
                displayRight = True
                letterRight = True
            elif not isVowel and not letterWrong:
                mistakes+=1
                displayWrong = True
                letterWrong = True

        #check for end of trial
        if globalClock.getTime()>duration:
            trialInProgress = False
    win.flip()
    core.wait(0.5)

#                                         changeQuiz function                                       ########################

def changeQuiz():
    quiz1 = visual.TextStim(win,'Did one of the images change during this trial?\n\nPress the "Y" key for yes.' + 
    '\nPress the "N" key for no.',
    pos=[0,0],height=0.06)
    global quizQuestions, yesNo, whichImage, howManyTimes
    quiz1.draw()
    for x in imageList:
        x.draw()
    for x in markList:
        x.draw()
    win.flip()
    yesNo = '.'
    whichImage = '.'
    howManyTimes = '.'
    gettingInput = True
    quizQuestions = False
    while gettingInput:
        input = event.waitKeys(keyList = ['y','n'])
        for thisKey in input:
            if translate(thisKey) in ['n']:
                yesNo = translate(thisKey)
                gettingInput = False
            if translate(thisKey) in ['y']:
                yesNo = translate(thisKey)
                gettingInput = False
                quizQuestions = True
    if quizQuestions:
        quiz1.setText('Which image changed during the trial?\n\nPress the letter key that corresponds to the image.')
        quiz1.draw()
        for x in imageList:
            x.draw()
        for x in markList:
            x.draw()
        win.flip()
        gettingInput = True
        while gettingInput:
            input = event.waitKeys(keyList = ['a','b','c','d'])
            for thisKey in input:
                if translate(thisKey) in ['a','b','c','d']:
                    whichImage = translate(thisKey)
                    gettingInput = False
        quiz1.setText('How many times did image ' + translate(thisKey) + ' change during the trial?' + 
        '\n\nPlease enter a number between 1 and 9')
        quiz1.draw()
        for x in imageList:
            x.draw()
        for x in markList:
            x.draw()
        win.flip()
        gettingInput = True
        while gettingInput:

#changed from original for all key boards
            input = event.waitKeys(keyList = ['1','2','3','4','5','6','7','8','9'])
            for thisKey in input:
                if translate(thisKey) in ['1','2','3','4','5','6','7','8','9']:
                    howManyTimes = translate(thisKey)
                    gettingInput = False
    
    # forced choice of highest frequency image
    validKeys = ['a','b','c','d']

    # prompt for input of most frequent image to least frequent image
    forcePrompt = visual.TextStim(win,'During the trial, it may have appeared that some images were rotating more' + 
    ' frequently than were other images. Please rank the 4 images from the trial in order of the image that rotated' + 
    ' MOST frequently to the image that rotated LEAST frequently. For each choice, press the letter key that corresponds' + 
    ' to the image.',
        pos=[0, .2], height=0.06, wrapWidth=1.4)
    forceAns1 = visual.TextStim(win,'Most frequent: ', # most frequent image input
        pos=[0, -0.2], height=0.06, wrapWidth=1.4)
    forcePrompt.draw()
    forceAns1.draw()
    for x in imageList:
        x.draw()
    for x in markList:
        x.draw()
    win.flip()
    gettingInput = True
    while gettingInput:
        input = event.waitKeys()
        for thisKey in input:
            if translate(thisKey) in validKeys:
                first = translate(thisKey)
                validKeys.remove(translate(thisKey))
                gettingInput = False

    # second most frequent image prompt & input
    forceAns1.setText('Most frequent: ' + first)
    forceAns2 = visual.TextStim(win,'2nd most frequent: ',
        pos=[0, -0.3], height=0.06, wrapWidth=1.4)
    forcePrompt.draw()
    forceAns1.draw()
    forceAns2.draw()
    for x in imageList:
        x.draw()
    for x in markList:
        x.draw()
    win.flip()
    gettingInput = True
    while gettingInput:
        input = event.waitKeys()
        for thisKey in input:
            if translate(thisKey) in validKeys:
                second = translate(thisKey)
                validKeys.remove(translate(thisKey))
                gettingInput = False

    # third most frequent image prompt & input
    forceAns2.setText('2nd most frequent: ' + second)
    forceAns3 = visual.TextStim(win,'3rd most frequent: ',
        pos=[0, -0.4], height=0.06, wrapWidth=1.4)
    forcePrompt.draw()
    forceAns1.draw()
    forceAns2.draw()
    forceAns3.draw()
    for x in imageList:
        x.draw()
    for x in markList:
        x.draw()
    win.flip()
    gettingInput = True
    while gettingInput:
        input = event.waitKeys()
        for thisKey in input:
            if translate(thisKey) in validKeys:
                third = translate(thisKey)
                validKeys.remove(translate(thisKey))
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
    for x in imageList:
        x.draw()
    for x in markList:
        x.draw()
    win.flip()
    gettingInput = True
    while gettingInput:
        input = event.waitKeys()
        for thisKey in input:
            if translate(thisKey) in validKeys:
                fourth = translate(thisKey)
                validKeys.remove(translate(thisKey))
                gettingInput = False
    
    # end function
    return yesNo, whichImage, howManyTimes, first, second, third, fourth

#                         feedback function                                        #####################


def feedback(numOfChanges):
    global successes, mistakes, changeA, changeB, target, totalSuccesses, totalMistakes, yesNo, whichImage, howManyTimes, trialNum, pointTotal
    totalSuccesses += successes
    totalMistakes += mistakes
    if numOfChanges>0:
        feedbackImageA = visual.ImageStim(win,image=changeA,mask=None,units='norm',pos=[-0.3,-0.72],size=[0.45,0.6])
        feedbackImageB = visual.ImageStim(win,image=changeB,mask=None,units='norm',pos=[0.3,-0.72],size=[0.45,0.6])
        if numOfChanges>1:
            feedbackChange = visual.TextStim(win,'Your performance on trial ' + str(trialNum) + ' out of 18:' +
                '\n\nVowel task:\n     Correct responses: ' + str(int(successes)) + 
                '\n     Incorrect responses: ' + str(int(mistakes)) + '\n\nImage change task:\n     Image ' + 
                imageDict[target] + ' changed ' + str(numOfChanges) + 
                ' times (see below).\n\n***Press the SPACE key to proceed when ready***',
                pos=[0,0.5],height=0.06)
        else:
            feedbackChange = visual.TextStim(win,'Your performance on trial ' + str(trialNum) + ' out of 18:' +
                '\n\nVowel task:\n     Correct responses: ' + str(int(successes)) + '\n     Incorrect responses: ' + 
                str(int(mistakes)) + '\n\nImage change task:\n     Image ' + imageDict[target] + ' changed ' + str(numOfChanges) + 
                ' time (see below).\n\n***Press the SPACE key to proceed when ready***',
                pos=[0,0.5],height=0.06)
        feedbackChange.draw()
        feedbackImageA.draw()
        feedbackImageB.draw()
    else:
        feedbackNoChange = visual.TextStim(win,'Your performance on trial ' + str(trialNum) + ' out of 18:' +
                '\n\nVowel task:\n     Correct responses: ' + str(int(successes)) + '\n     Incorrect responses: ' + str(int(mistakes)) + '\n\nImage change task:\n     No images changed during this trial\n\n***Press the SPACE key to proceed when ready***',
            pos=[0,0.5],height=0.06)
        feedbackNoChange.draw()
        feedbackImageA = visual.ImageStim(win,image='2880_a.jpg',mask=None,units='norm',pos=[-0.3,-0.72],size=[0.45,0.6])
        feedbackImageB = visual.ImageStim(win,image='2880_b.jpg',mask=None,units='norm',pos=[0.3,-0.72],size=[0.45,0.6])
        feedbackDebug = visual.TextStim(win, '(No target image on the practice trial)', pos=[0,-0.7],height=0.05)
    if not isPractice:
        # tally points
        if successes==0:
            vowelPoints = 0
        else:
            vowelPoints = round((successes / (successes + 2*mistakes))*50, 2)
        if numOfChanges>0:
            if yesNo=='y':
                if whichImage.lower()==imageDict[target].lower() and int(howManyTimes)==numOfChanges:
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
    input = event.waitKeys(keyList = ['escape', 'space'])
    if 'escape' in input:
        print input
        win.close()
        core.quit()

#                                   Practice Block 1                                            #################

#run trial (int = blockNum? 0=practice, 1, 2, or 3)
isPractice = True
trialNum = '[PRACTICE]'
noChangeTrial(0)

# gather ratings of images (boolean = practice trial?)
gatherRatings(True)

#quiz on image changes
changeQuiz()

#display feedback and wait
#(integer = number of changes)
feedback(0)

#                                  Practice Block 2                                          #####################

#(integer = whichChange = -1 if practice trial, 0 if first change trial, 1 if second change trial, etc.)
#(float = numberOfChanges = 1.0 or 2.0)
trialNum = '[PRACTICE]'
changeTrial(-1, 2.0)

# gather ratings of images (boolean = practice trial?)
gatherRatings(True)

#quiz on image changes
changeQuiz()

#display feedback 
#(integer = number of changes)
feedback(2)

#                                       Begin main experiment                                #######################

isPractice = False
pointTotal = 0

# instructions page 1
def screen1(numTrials):
    instructions = visual.TextStim(win,'You will now begin the main part of the experiment.' +
        '\n\nYour task in this part of the experiment is going to be just the same as it was'+
        ' during the practice trials. The experiment consists of a series of ' +
        "{}".format(numTrials) +
        ' trials just like the practice trials that you completed, except somewhat longer.' +
        ' They will take a total of approximately 30 minutes to complete.' +
        '\n\nThe only difference here is that on these trials you will be awarded a certain amount' +
        ' of POINTS based on your performance each trial. Your goal is to gain as many points as possible' +
        ' over the course of the experiment.' +
        '\n\nOn the next screen we will explain the point scoring system in more detail.' +
        '\n\n\n\nPress the SPACE key to advance to the next screen and continue reading the instructions.',
pos=[0, 0],height=0.06,wrapWidth=1.6)
    instructions.draw()
    win.flip()

# instructions page 2
def screen2():
    instructions = visual.TextStim(win, '\n\n\n\n***Points for the vowel task:***' +
        '\n\nThe points earned for the vowel task are based on the total number of correct responses' + 
        ' (responses that cause the green check mark to appear) and incorrect responses (responses that cause the red X to appear)' +
        ' that you make.' +
        '\n\nFirst the number of incorrect responses that you make is multiplied by 2.' +
        '\n\nThen the number of points that you earn from the vowel task is the proportion of correct responses to total' + 
        ' responses, scaled from 0 points to 50 points.' +
        '\n\nFor example, if you made 10 correct responses and 5 incorrect responses, your proportion of correct responses' + 
        ' would be 10 / (10 + 5*2) = 0.5, so you would earn 25 out of 50 points for the vowel task.' +
        '\n\n\n\nPress the SPACE key to continue reading the instructions.',
        pos=[0, 0],height=0.06,wrapWidth=1.6)
    instructions.draw()
    win.flip()

# instructions page 3
def screen3():
    instructions = visual.TextStim(win, '\n\n***Points for the image change task:***' +
        '\n\nThe points earned for the image change task are based on whether you correctly answered whether or not there were ' +
        'any image changes during the trial, and if there were, whether you correctly identified the image that changed and also ' +
        'gave the correct number of total image changes.' +
        '\n\nThe exact numbers of points earned for each possible response are listed in the table below:' +
        '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress the SPACE key to continue reading the instructions.',
        pos=[0, 0],height=0.06,wrapWidth=1.6)
    changePoints = visual.ImageStim(win, image='changePoints.bmp', mask=None, units='norm', pos=[-.1, -0.25], size=[0.88, 1])
    instructions.draw()
    changePoints.draw()
    win.flip()

# instructions page 4
def screen4():
    instructions = visual.TextStim(win,'\n\n\n\nAt the end of each trial, the points that you earn on both the SHIFT '+
    'TASK and the IMAGE CHANGE TASK are added together to give the total number of points earned on that trial. Both '+
    'tasks award a maximum of 50 points each. So the maximum number of points that you can earn on each trial is 100 points.' +
        '\n\nOnly by being as accurate as possible on both the VOWEL TASK and the IMAGE CHANGE TASK can you maximize the amount ' +
        'of points that you earn. No other strategy (like strategically only answering "Yes" or always answering "No" on the image '+
        'change task) will give you the most points.' +
        '\n\n\n\nWhen you are ready, press the SHIFT key to finish the instructions and advance to the first trial.',
        pos=[0, 0],height=0.06,wrapWidth=1.6)
    instructions.draw()
    win.flip()

#block trials
blocks = [
    {'change':False,"blockNum":1, "feedback":0}]                          #block 1       noChangeTrial = False
"""    {'change':True, "whichChange":2, "numOfChanges":1.0, "feedback":1},   #block 2       changeTrial = True
    {'change':True, "whichChange":1, "numOfChanges":2.0, "feedback":2},   #block 3
    {'change':False,"blockNum":1, "feedback":0},                          #block4
    {'change':False,"blockNum":1, "feedback":0},                          #block5
    {'change':False,"blockNum":1, "feedback":0},                          #block6
    {'change':True, "whichChange":2, "numOfChanges":2.0, "feedback":2},   #block7
    {'change':False,"blockNum":2, "feedback":0},                          #block8
    {'change':True, "whichChange":3, "numOfChanges":1.0, "feedback":1},   #block9
    {'change':False,"blockNum":2, "feedback":0},                          #block 10
    {'change':False,"blockNum":2, "feedback":0},                          #block 11
    {'change':False,"blockNum":2, "feedback":0},                          #block 12
    {'change':True, "whichChange":4, "numOfChanges":2.0, "feedback":2},   #block 13
    {'change':False,"blockNum":3, "feedback":0},                          #block 14
    {'change':False,"blockNum":3, "feedback":0},                          #block 15
    {'change':True, "whichChange":5, "numOfChanges":1.0, "feedback":1},   #block16
    {'change':False,"blockNum":3, "feedback":0},                          #block17
    {'change':False,"blockNum":3, "feedback":0}                           #block18
]"""

# cycle through instruction screens

screens = [lambda: screen1(len(blocks)), screen2, screen3, screen4]
currentScreen = 0
while currentScreen < 4:
    screens[currentScreen]()
    input = event.waitKeys(keyList = ['escape', 'lshift', 'space'])
    if input == ['escape']:
        print input
        win.close()
        core.quit()
    if input == ['lshift']:
        if currentScreen > 0: currentScreen += -1
    if input == ['space']:
        currentScreen += 1

#                                       Begin block loop                           ###################

for index,block in enumerate(blocks, 1):
    trialNum = index
    if block["change"]:
        #int = whichChange; -1 = practice trial, 0 = first change trial, 1 = second change trial)
        #float = numberOfChanges; 1.0 or 2.0
        changeTrial(block["whichChange"],block["numOfChanges"])
    else:
        #int = blockNum; 0=practice, 1, 2, or 3
        noChangeTrial(block["blockNum"])
    #gather ratings of images (boolean = practice trial?)
    gatherRatings(False)
    #quiz on image changes
    changeMatrix.append(changeQuiz())
    #display feedback & wait
    #int = number of changes
    feedback(block["feedback"])

#                                                    Get gender and age                ##################     Do we need this?

# user input for gender
instructions = visual.TextStim(win,'What is your gender? Please press "m" for Male or "f" for Female.',
    pos=[0,0.2],height=0.06,wrapWidth=1.3)
instructions2 = visual.TextStim(win,'Your answer: ',pos=[0,0],height=0.06,wrapWidth=1.5)
instructions3 = visual.TextStim(win,'Press the SPACE key to submit your answer.',pos=[0,-0.2],height=0.05,wrapWidth=1.5)
instructions.draw()
instructions2.draw()
instructions3.draw()
win.flip()
temp = '.'
gettingInput = True 
while gettingInput:
    input = event.waitKeys()
    for thisKey in input:
        if thisKey in ['m','f']:
            temp = translate(thisKey)
            instructions2.setText('Your answer: ' + translate(thisKey))
            instructions.draw()
            instructions2.draw()
            instructions3.draw()
            win.flip()
        elif thisKey=='space':
            gettingInput = False
            gender = temp
            if not temp in ['m','f']:
                gender = '.'

# get age
instructions = visual.TextStim(win,'What is your age?',
    pos=[0,0.2],height=0.06,wrapWidth=1.3)
instructions2 = visual.TextStim(win,'Your answer: ',pos=[0,0],height=0.06,wrapWidth=1.5)
instructions3 = visual.TextStim(win,'Press the SPACE key to submit your answer and proceed to the next part of the experiment.',
pos=[0,-0.2],height=0.05,wrapWidth=1.5)
instructions.draw()
instructions2.draw()
instructions3.draw()
win.flip()
temp = '.'
gettingInput = True
age = []
while gettingInput:
    input = event.waitKeys(keyList = ['space','lshift','1','2','3','4','5','6','7','8','9','0'])
    for thisKey in input:
        if translate(thisKey) in ['0','1','2','3','4','5','6','7','8','9'] and len(age) < 2:
            age.append(translate(thisKey))
            instructions2.setText('Your answer: ' + ''.join(age))
            instructions.draw()
            instructions2.draw()
            instructions3.draw()
            win.flip()
        elif thisKey=='lshift' and len(age) > 0:
            del age[-1]
            instructions2.setText('Your answer: ' + ''.join(age))
            instructions.draw()
            instructions2.draw()
            instructions3.draw()
            win.flip()
        elif thisKey=='space':
            gettingInput = False
            if len(age) < 1:
                age = '.'
            else: age = ''.join(age)

#                                                    Write data, End experiment                      ######################

# image list
images = ['9140.jpg','9181.jpg','9500.jpg','9571.jpg',
                '2205.jpg','9421.jpg','6243.jpg','9921.jpg',
                '3550.jpg','6212.jpg','9400.jpg','6838.jpg',
                '3110.jpg','3030.jpg','3071.jpg','9252.jpg',
                '2141.jpg','9007.jpg','9430.jpg','2900_1.jpg',
                '3350.jpg','3301.jpg','2800.jpg','9040.jpg',
                '2480.jpg','2190.jpg','2570.jpg','2890.jpg',
                '7705.jpg','7035.jpg','7030.jpg','7235.jpg',
                '7002.jpg','7950.jpg','7006.jpg','6150.jpg',
                '7233.jpg','7217.jpg','7090.jpg','7000.jpg',
                '7025.jpg','7040.jpg','7050.jpg','7150.jpg',
                '5510.jpg','5520.jpg','5500.jpg','5533.jpg',
                '7390.jpg','7282.jpg','7460.jpg','7400.jpg',
                '1750.jpg','1460.jpg','1440.jpg','1710.jpg',
                '2050.jpg','2040.jpg','2070.jpg','2058.jpg',
                '5870.jpg','7545.jpg','5750.jpg','5220.jpg',
                '5910.jpg','7502.jpg','8170.jpg','8501.jpg',
                '8034.jpg','8180.jpg','5629.jpg','8200.jpg']

# trial list
trialList = sum([[x]*4 for x in range(1, 19)], [])

# list indicating whether each trial was a changeTrial
# and whether each image changed or not
changeTrialList = sum([[x]*4 for x in [0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0]], [])
changePicList = [0 for _ in range(72)]
for changePic in ['9921.jpg', '2190.jpg', '7390.jpg', '3550.jpg', '6150.jpg', '7545.jpg']:
    changePicList[images.index(changePic)] = 1

# lists for changeMatrix variables:
# yesNo, whichImage, howManyTimes, first, second, third, fourth
# ERROR NOTE: this records numChanges and rank in the order in which they were presented
# ERROR NOTE: should be recorded in the same pre-determined order as the main DVs!
numChangesList = [0 for _ in range(72)]
rankList = ['.' for _ in range(72)]
for trial, vec in enumerate(changeMatrix):
    if vec[0]=='y':
        numChangesList[trial*4 + letterToNum(vec[1])] = vec[2]
    rankList[trial*4 + letterToNum(vec[3])] = 1
    rankList[trial*4 + letterToNum(vec[4])] = 2
    rankList[trial*4 + letterToNum(vec[5])] = 3
    rankList[trial*4 + letterToNum(vec[6])] = 4

# lists for all evaluation ratings
grid = [(a, b) for a in range(18) for b in range(4)]
intensityList = [ratingMatrix[x][y][0] for x, y in grid]
interestList = [ratingMatrix[x][y][1] for x, y in grid]
likingList = [ratingMatrix[x][y][2] for x, y in grid]

# list of observed frequencies
freqList = [freqMatrix[x][y] for x, y in grid]

# write data to file
fileName = 'attention_thesis_rotData.csv'
print 'Opening data file: ' + fileName
dataFile = open(fileName, 'a')

# write data
for i in range(72):
    dataFile.write('\n' + str(subject) + ',' + str(between) + ',' + str(condition) + ',' + str(order) + ',' + str(info['  Date']) + 
    ',' + str(gender) + ',' + str(age) + ',' + str(totalSuccesses) + ',' + str(totalMistakes) + ',' + str(images[i]) + 
    ',' + str(trialList[i]) + ',' + str(changePicList[i]) + ',' + str(changeTrialList[i]) + ',' + str(numChangesList[i]) + 
    ',' + str(rankList[i]) + ',' + str(intensityList[i]) + ',' + str(interestList[i]) + ',' + str(likingList[i]) + ',' + str(freqList[i]))

# close data file
dataFile.close()

# end experiment instruction screen 
goodbye = visual.TextStim(win,'You have completed the the experiment.' + 
    '\n\nYour final average of points per trial is: ' + str(round((pointTotal/trialNum), 2)) + ' / 100' +  #
    '\n\nWhen you are ready, press the SPACE key to close the program.',
    wrapWidth=1.5)
goodbye.draw();
win.flip()
input = event.waitKeys(keyList = ['escape','space'])

# end experiment
print 'Closed nicely'
win.close()
core.quit()