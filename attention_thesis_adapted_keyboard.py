from psychopy import core, visual, event, gui
import time, random, math
#                                  functions             #################
#escape function
def escapeInput(input):
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
#                                           Initialization                     #################
#dialogue box for experimenter to enter age, gender, subject number, condition, & other variables
info = {
    '   Age': 0,
    '   Group': '0', #group can equal 1, 2, 3, 4, 5
    '   Gender': 'f', #must be male or female
    '   Subject number':1,
    ' Practice length (secs)':30,       #for experiment = 30 sec
    ' Block length (secs)':120,          # for experiment = 120 sec
    'Date':time.strftime("%m-%d-%Y@%H.%M", time.localtime()),
    'Vowel probability':0.3,
    'Letter change interval (secs)':2.75,
    'Rotation speed (degrees/frame)':15,
    'Min rotation interval (secs)':1.75,
    'Max rotation interval (secs)':3.75,
    'Letter blink duration (secs)':0.250
}
infoDlg = gui.DlgFromDict(dictionary=info, title='Attention study', fixed=['Date'])
if not infoDlg.OK:
    print 'User Cancelled'
    core.quit()
#extract variables from dictionary
gender = info['   Gender']
group = info['   Group']

demographicKey = group.lower() + gender.lower()
print demographicKey
vowelProb = info['Vowel probability']
interval = info['Letter change interval (secs)']
speed = info['Rotation speed (degrees/frame)']
rotateMin = info['Min rotation interval (secs)']
rotateMax = info['Max rotation interval (secs)']
pracLength = info[' Practice length (secs)']
blockLength = info[' Block length (secs)']
letterPause = info['Letter blink duration (secs)']

#check if group is in range 1-5
if group not in ['1', '2', '3', '4', '5']:
    print 'Error: group must be one of 1, 2, 3, 4, or 5!'
    print 'Subject number was set to: ' + str(info['   Subject number'])
    core.quit()
 
if gender not in ['f', 'm']:
    print 'Error: gender mut be on of f or m!'
    print 'Subject number was set to: ' + str(info['   Subject number'])
    core.quit()

#check subject number for integer format
try:
    subject = int(info['   Subject number'])
except:
    print 'Error: subject number must be a positive integer!'
    print 'Subject number was set to: ' + str(info['   Subject number'])
    core.quit()
#check subject number for range
if not subject>=0:
    print 'Error: subject number must be a positive integer!'
    print 'Subject number was set to: ' + str(info['    Subject number'])
    core.quit()

#All Experiment Images
introImage = 'layout.bmp'
demoPicA = 'demo_a.jpg'
demoPicB = 'demo_b.jpg'
#                                 Welcome to Experiment Window                      ######################
#define welcome screen
win = visual.Window([1400,800],rgb=(-1,-1,-1),allowGUI=False,winType='pyglet')      #changed from (1600,900)
welcome = visual.TextStim(win, 'Welcome to the experiment!' +
    '\n' +
    'press the SPACE key to begin.' +
    '\n\n' +
    '(Experimenter: press escape to quit.)')
#display welcome screen
welcome.draw()
win.flip()
# wait for user input -- close experiment if 'escape'
input = event.waitKeys()
escapeInput(input)
#                                     Instructions for Experiment                          ##################
# define instruction screen 1
instructions1 = visual.TextStim(win,'In this experiment, you will be presented' +
    ' with a steady stream of letters at the center of the screen, surrounded by 4' +
    ' images which will periodically rotate and sometimes change to a new image.' +
    '\n\n' +
    'The basic visual of each trial will be something like this:' +
    '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n' +
    'Press the SPACE key to advance to ' +
    'the next screen and continue reading the instructions.',
    pos=[0, 0],height=0.06,wrapWidth=1.5)
layout = visual.ImageStim(win, image=introImage, mask=None, units='norm', pos=[0, -0.1], size=[0.88, 1.0])

#display instruction screen 1
instructions1.draw()
layout.draw()
win.flip()

# wait for user input -- close experiment if 'escape'
input = event.waitKeys(keyList = ['escape', 'space'])
escapeInput(input)

# define instrucion screen 2
demoPic = visual.ImageStim(win, image=demoPicA, mask=None, units='norm', pos=[0,-0.1], size=[0.45,0.6])
instructions1 = visual.TextStim(win,'You have two tasks during this experiment:',
    pos=[0,0.85],height=0.06,wrapWidth=1.5)

instructions2 = visual.TextStim(win, '1. Press the SHIFT key whenever the letter' +
    ' currently displayed in the center of the screen is a VOWEL. For example, you' +
    ' should press the key if the letter "a" appears on the screen, but not the letter "f".' +
    '\n\n' +
    '2. Each time an image rotates, there is a small chance that it will change to a similar' +
    '   but different image. At the end of each experimental trial, you will be asked how many image' +
    '   changes there were during the trial.',
    pos=[0,0.50],height=0.06,wrapWidth=1.3)

instructions3 = visual.TextStim(win,'The above image will demonstrate what you are looking for each' +
    ' time an image rotates. Press the SPACE key to watch the image rotate and change to a new image.',
    pos=[0,-0.65],height=0.06,wrapWidth=1.5)

#display instruction screen 2
demoPic.draw()
instructions1.draw()
instructions2.draw()
instructions3.draw()
win.flip()

#wait for key press -- abort on escape
input = event.waitKeys()
escapeInput(input)

#loop that changes from demo image A to B
gettingInput = True
a = True
while gettingInput:
    #rotate the demo image, changing the image halfway through
    for x in range(0,361, speed):
        demoPic.setOri(x)
        if x==180:
            if a:
                demoPic.setImage(demoPicB)
                a = False
            else:
                demoPic.setImage(demoPicA)
                a = True
        demoPic.draw()
        instructions1.draw()
        instructions2.draw()
        instructions3.draw()
        win.flip()

    #define instructions screen 3
    instructions3.setText('To rotate and change the image again, press the BACK key.' +
        '\n\n' +
        'Can you find what is changing in the picture above each time the image rotates?' +
        '\n' +
        'Press the SPACE key to find out...')

    #display instructions screen 1-3
    demoPic.draw()
    instructions1.draw()
    instructions2.draw()
    instructions3.draw()
    win.flip()

    #wait for key press -- if 'escape' pressed close program
    input = event.waitKeys()
    escapeInput(input)
    if 'space' in input:
        gettingInput = False

# introduction screen 3
instructions3 = visual.TextStim(win,'ANSWER: Pay attention to the man\'s eyebrows.' +
    '\n' +
    'The image flips 180 degrees while rotating.' +
    '\n\n' +
    'Press the BACK key to rotate the image.',
    pos=[0,-0.65],height=0.06,wrapWidth=1.5)

demoPic.draw()
instructions1.draw()
instructions2.draw()
instructions3.draw()
win.flip()

#wait for user input, if 'escape' close program
input = event.waitKeys()
escapeInput(input)
gettingInput = True
while gettingInput:
    #rotate the demo image, changing the image halfway through
    for x in range(0,361, speed):
        demoPic.setOri(x)
        if x==180:
            if a:
                demoPic.setImage(demoPicB)
                a = False
            else:
                demoPic.setImage(demoPicA)
                a = True
        
        demoPic.draw()
        instructions1.draw()
        instructions2.draw()
        instructions3.draw()
        win.flip()
    
    instructions3.setText('ANSWER: Pay attention to the man\'s eyebrows.' +
        '\n' +
        'The image flips 180 degrees while rotating.' +
        '\n\n' +
        'Press the BACK key to rotate the image.')

    instructions4 = visual.TextStim(win,'\nWhen you have finished reading the instructions on this screen,' +
        ' press the SPACE key to advance to the next screen.' +
        '\n' +
        'Don\'t worry if you don\'t fully understand both of the tasks yet. We will' +
        'explain them more on the next screen, and you will also get a chance to practice before starting' +
        ' the main experiment.')

    demoPic.draw()
    instructions1.draw()
    instructions2.draw()
    instructions3.draw()
    instructions4.draw()
    win.flip()

    #wait for key press -- abort on escape
    input = event.waitKeys()
    escapeInput(input)
   
    if 'space' in input:
        gettingInput = False

# instruction screen 4
def screen4():
    instructions4 = visual.TextStim(win,'Many of the image changes that you will be looking for can be' +
        ' difficult to detect. You must pay attention to the images closely to successfully detect the changes.' +
        '\n\n' +
        'There are two more things you should know about the image changes.' +
        '\n\n' +
        'First, not every trial of the experiment will have an image change. Some trials will have an image change,' +
        ' other trials will have no image changes, and some trials will have multiple image changes.' +
        '\n\n' +
        'Second, when an image DOES change, it will only ever do so during one of the rotations that occur every' +
        ' couple of seconds. So the best way to successfully detect the image changes is to check each image ' +
        'after it rotates to see if anything has changed or not. If it has, make a mental note of which image ' +
        'it is and how many times it changes over the course of the trial. We will ask you about this at the ' +
        'end of each trial.' +
        '\n\n\n\n' +
        'Press the SPACE key to continue reading the instructions.',
        pos=[0, 0], height=0.06, wrapWidth=1.5)
   
    instructions4.draw()
    win.flip()

# instruction screen 5
def screen5():
    instructions4 = visual.TextStim(win,'\n\n\n\n' +
       'You will now complete two PRACTICE trials.' +
        '\n\n' +
        'The purpose of the practice trials is simply to help you become familiar with the experimental procedure.' +
        ' After the practice trials you will begin the main experimental trials.' +
        '\n\n' +
        'Remember your two tasks:' +
        '\n' +
        '     1. Press the SHIFT key when the letter in the center of the screen is a VOWEL.' +
        '\n' +
        '     2. Keep track of how many times any image changes over the course of the trial.' +
        '\n\n\n\n' +
        'Press the SPACE key to begin the first practice trial.',
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
#                             Define miscellanious variables                         ################

demographicImages = {
    '1f': ['PF_1.jpg', 'PF_2.jpg', 'PF_3.jpg', 'PF_4.jpg', 'PF_1b.jpg'],
    '1m': ['PM_1.jpg', 'PM_2.jpg', 'PM_3.jpg', 'PM_4.jpg', 'PM_1b.jpg'],
    '2f': ['F_1.jpg', 'WF_2.jpg', 'WF_3.jpg', 'WF_4.jpg', 'WF_5.jpg', 'WF_6.jpg', 'WF_7.jpg', 'WF_8.jpg', 'WF_6b.jpg'],
    '2m': ['WM_1.jpg', 'WM_2.jpg', 'WM_3.jpg', 'WM_4.jpg', 'WM_5.jpg', 'WM_6.jpg', 'WM_7.jpg', 'WM_8.jpg', 'WM_7b.jpg'],
    '3f': ['BF_1.jpg', 'BF_2.jpg', 'BF_3.jpg', 'BF_4.jpg', 'BF_5.jpg', 'BF_6.jpg', 'BF_7.jpg', 'BF_8.jpg', 'BF_7b.jpg'],
    '3m': ['BM_1.jpg', 'BM_2.jpg', 'BM_3.jpg', 'BM_4.jpg', 'BM_5.jpg', 'BM_6.jpg', 'BM_7.jpg', 'BM_8.jpg' 'BM_8b.jpg'],
    '4f': ['AF_1.jpg', 'AF_2.jpg', 'AF_3.jpg', 'AF_4.jpg', 'AF_5.jpg', 'AF_6.jpg', 'AF_7.jpg', 'AF_8.jpg', 'AF_7b.jpg'],
    '4m': ['AM_1.jpg', 'AM_2.jpg', 'AM_3.jpg', 'AM_4.jpg', 'AM_5.jpg', 'AM_6.jpg', 'AM_7.jpg', 'AM_8.jpg', 'AM_5b.jpg'],
    '5f': ['LF_1.jpg', 'LF_2.jpg', 'LF_3.jpg', 'LF_4.jpg', 'LF_5.jpg', 'LF_6.jpg', 'LF_7.jpg', 'LF_8.jpg', 'LF_6b.jpg'],
    '5m': ['LM_1.jpg', 'LM_2.jpg', 'LM_3.jpg', 'LM_4.jpg', 'LM_5.jpg', 'LM_6.jpg', 'LM_7.jpg', 'LM_8.jpg', 'LM_5b.jpg']
}

demographicTargets = {
    'pf': 0,
    'pm': 0,
    'wf': 1,
    'wm': 3,
    'bf': 3,
    'bm': 4,
    'af': 3,
    'am': 0,
    'lf': 1,
    'lm': 0
}

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
image0 = visual.ImageStim(win,image='AF_1.jpg',mask=None,units='norm',pos=[-0.7,0.7],size=[0.375,0.5])
image1 = visual.ImageStim(win,image='AF_2.jpg',mask=None,units='norm',pos=[0.7,0.7],size=[0.375,0.5])
image2 = visual.ImageStim(win,image='AF_3.jpg',mask=None,units='norm',pos=[-0.7,-0.7],size=[0.375,0.5])
image3 = visual.ImageStim(win,image='AF_4.jpg',mask=None,units='norm',pos=[0.7,-0.7],size=[0.375,0.5])
imageList = [image0,image1,image2,image3]
vowelList = ['a','e','i','o','u']
consList = ['b','c','d','f','g','h','j','k','m','n','p','q','r','s','t','v','w','x','y','z'] #lower-case L is omitted
temp = '.'
changeA = '.'
changeB = '.'
#define marker lists...                                                       Why are there two lists?
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
    ratingInstructions1 = visual.TextStim(win,
    'Please answer a few questions about your reaction to these four faces during the trial.' +
    '\n' +
    'For each question, enter a number between 0 and 7,' +
    '\n \t \t with 0 = "Not at all" and 7 = "Very Much."' +
    '\n' +
    'Not at all ---------------------------------------------------------------------- Very Much'+
    '\n' +
    '  1             2             3             4             5             6             7',
        pos=[0,0.65],height=0.05,wrapWidth=0.9)
    ratingInstructions2 = visual.TextStim(win,'Press the SPACE key after each response to continue.',
        pos=[0,-0.7],height=0.05,wrapWidth=0.9)
    rating1 = visual.TextStim(win,'How much do you like this person?',                      #like
        pos=[0,0.45],height=0.05,wrapWidth=1.5)
    rating1a = visual.TextStim(win,'Your answer: ',                         #rating 1
        pos=[0,0.39],height=0.05,wrapWidth=1.5)                                 #change this to center
    rating2 = visual.TextStim(win,'What is your overall impression of this person?',        #impression
        pos=[0,0.33],height=0.05,wrapWidth=1.5)
    rating2a = visual.TextStim(win,'Your answer: ',                         #rating 2
        pos=[0,0.27],height=0.05,wrapWidth=1.5)                                 #change this to center
    rating3 = visual.TextStim(win,'How threatening do you find this person?',               #threatening
    pos=[0,0.21],height=0.05,wrapWidth=1.5)                                      #change this to center
    rating3a = visual.TextStim(win,'Your answer: ',                         #rating 3
        pos=[0,0.15],height=0.05,wrapWidth=1.5)                                 #change this to center
    rating4 = visual.TextStim(win,'How much do you trust this person?',                     #trust
        pos=[0,0.09],height=0.05,wrapWidth=1.5)                                  #change this to center
    rating4a = visual.TextStim(win,'Your answer: ',                         #rating 4
        pos=[0,0.03],height=0.05,wrapWidth=1.5)                                 #change this to center
    rating5 = visual.TextStim(win,'How intimidating do you find this person?',              #intimidating
        pos=[0,-0.03],height=0.05,wrapWidth=1.5)                                  #change this to center
    rating5a = visual.TextStim(win,'Your answer: ',                         #rating 5
        pos=[0,-0.09],height=0.05,wrapWidth=1.5)                                 #change this to center
    rating6 = visual.TextStim(win,'How attractive do you find this person?',                #attractive
        pos=[0,-0.15],height=0.05,wrapWidth=1.5)                                 #change this to center
    rating6a = visual.TextStim(win,'Your answer: ',                         #rating 6
        pos=[0,-0.21],height=0.05,wrapWidth=1.5)                                 #change this to center
    rating7 = visual.TextStim(win,'How interested are you in being paired with this person in a future study?', #pairing
        pos=[0,-0.27],height=0.05,wrapWidth=1.5)                                 #change this to center
    rating7a = visual.TextStim(win,'Your answer: ',                         #rating 6
        pos=[0,-0.33],height=0.05,wrapWidth=1.5)                                 #change this to center
    ratingQuestions = [rating1, rating2, rating3, rating4, rating5, rating6, rating7]
    ratingPrompts = [rating1a, rating2a, rating3a, rating4a, rating5a, rating6a, rating7a]
    promptAddons = [['']*7 for _ in range(4)] #7 questions & 4 pictures
    # 2-lists of pictureNums and questionNums
    picByQuestion = [[a, b] for a in range(4) for b in range(7)] #7 questions & 4 pictures
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
        input = event.waitKeys(keyList = ['escape','lshift','space','1','2','3','4','5','6','7'])
        # process input
        for thisKey in input:
            if translate(thisKey) in [str(x) for x in range(8)]:
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
                currentScreen += 1
                temp = ''
            if input == ['escape']:
                print input
                win.close()
                core.quit()
            if input == ['lshift']:
                if currentScreen > 0: currentScreen += -1
#                               noChangeTrial function                                   #######################
def noChangeTrial(blockNum):
    #reset variables
    global currentSet, mistakes, successes, currentRotator, usedPositiveList,usedNeutralList, usedNegativeList, unusedPositiveList, unusedNeutralList, unusedNegativeList
    letterRefresh = feedbackRefresh = rotating = displayRight = displayWrong = letterRight = letterWrong = missFlag = quizQuestions = letterMissed = letterCleared = changed = False
    #global mistakes, successes
    mistakes = successes = 0.0
    a = True
    #global currentRotator
    # reminder to locate VOWEL key = 'lshift'
    
    remind = visual.TextStim(win,'About to begin trial ' + str(trialNum) +
    '\n\n' +
    'Please take this moment to locate the SHIFT key on the keyboard.' +
    '\n\n' +
    'When ready, press the SPACE key to begin the trial.',
    pos=[0, 0], height=0.06, wrapWidth=1.5)
    
    remind.draw()
    win.flip()
    
    input = event.waitKeys(keyList = ['space','escape'])
    escapeInput(input)
   
    # set images
    if blockNum<1:
        if gender == 'f':
            currentSet = demographicImages['pf']
        else:
            currentSet = demographicImages['pm']
    else:
        currentSet = demographicImages[demographicKey][:4] # take first four images
        print 'currentSet: ', currentSet
        print 'target: ', target
        #update image textures

    index = 0
    for x in imageList:
        x.setImage(currentSet[index])
        index += 1

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
            currentRotator = random.choice([0, 1, 2, 3])
            
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
        quiz1.setText('Which image changed during the trial?' +
            '\n\n' +
            'Press the letter key that corresponds to the image.')
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
            feedbackChange = visual.TextStim(win,'Your performance on trial ' + str(trialNum) +
                '\n\nVowel task:\n     Correct responses: ' + str(int(successes)) +
                '\n     Incorrect responses: ' + str(int(mistakes)) + '\n\nImage change task:\n     Image ' +
                imageDict[target] + ' changed ' + str(numOfChanges) +
                ' times (see below).\n\n***Press the SPACE key to proceed when ready***',
                pos=[0,0.5],height=0.06)
        else:
            feedbackChange = visual.TextStim(win,'Your performance on trial ' + str(trialNum) +
                '\n\nVowel task:\n     Correct responses: ' + str(int(successes)) + '\n     Incorrect responses: ' +
                str(int(mistakes)) + '\n\nImage change task:\n     Image ' + imageDict[target] + ' changed ' + 
                str(numOfChanges) +
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
    escapeInput(input)
#                                  Control Block - NO CHANGES                        #####################
#(integer = whichChange = -1 if practice trial, 0 if first change trial, 1 if second change trial, etc.)
#(float = numberOfChanges = 1.0 or 2.0)
isPractice = True
trialNum = '[PRACTICE]'
noChangeTrial(1)
# gather ratings of images (boolean = practice trial?)
gatherRatings(True)
#quiz on image changes
changeQuiz()
#display feedback
#(integer = number of changes)
feedback(0)
#                                   Experiment Block - WITH CHANGES                            #################
#run trial (int = blockNum? 0=practice, 1, 2, or 3)
trialNum = '[PRACTICE]'
noChangeTrial(1)
# gather ratings of images (boolean = practice trial?)
gatherRatings(True)
#quiz on image changes
changeQuiz()
#display feedback and wait
#(integer = number of changes)
feedback(0)
#                                       Begin main experiment                          #######################
isPractice = False
pointTotal = 0
# instructions page 1
def screen1(numTrials):
    instructions = visual.TextStim(win,'You will now begin the main part of the experiment.' +
        '\n\n'
        +'Your task in this part of the experiment is going to be just the same as it was'+
        ' during the practice trials. The experiment consists of a series of ' +
        "{}".format(numTrials) +
        ' trials just like the practice trials that you completed, except somewhat longer.' +
        ' They will take a total of approximately 30 minutes to complete.' +
        '\n\n' +
        'The only difference here is that on these trials you will be awarded a certain amount' +
        ' of POINTS based on your performance each trial. Your goal is to gain as many points as possible' +
        ' over the course of the experiment.' +
        '\n\n' +
        'On the next screen we will explain the point scoring system in more detail.' +
        '\n\n\n\n' +
        'Press the SPACE key to advance to the next screen and continue reading the instructions.',
        pos=[0, 0],height=0.06,wrapWidth=1.6)
    
    instructions.draw()
    win.flip()

# instructions page 2
def screen2():
    instructions = visual.TextStim(win, '\n\n\n\n***Points for the vowel task:***' +
        '\n\n' +
        'The points earned for the vowel task are based on the total number of correct responses' +
        ' (responses that cause the green check mark to appear) and incorrect responses (responses that' +
        ' cause the red X to appear) that you make.' +
        '\n\n' + 
        'First the number of incorrect responses that you make is multiplied by 2.' +
        '\n\n' +
        'Then the number of points that you earn from the vowel task is the proportion of correct responses to total' +
        ' responses, scaled from 0 points to 50 points.' +
        '\n\n' +
        'For example, if you made 10 correct responses and 5 incorrect responses, your proportion of correct responses' +
        ' would be 10 / (10 + 5*2) = 0.5, so you would earn 25 out of 50 points for the vowel task.' +
        '\n\n\n\n' +
        'Press the SPACE key to continue reading the instructions.',
        pos=[0, 0],height=0.06,wrapWidth=1.6)
    instructions.draw()
    win.flip()
# instructions page 3
def screen3():
    instructions = visual.TextStim(win, '\n\n***Points for the image change task:***' +
        '\n\n' +
        'The points earned for the image change task are based on whether you correctly answered whether or ' +
        'not there were any image changes during the trial, and if there were, whether you correctly identified ' +
        'the image that changed and also gave the correct number of total image changes.' +
        '\n\n' +
        'The exact numbers of points earned for each possible response are listed in the table below:' +
        '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n' +
        'Press the SPACE key to continue reading the instructions.',
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
        '\n\n' +
        'Only by being as accurate as possible on both the VOWEL TASK and the IMAGE CHANGE TASK can you maximize the amount ' +
        'of points that you earn. No other strategy (like strategically only answering "Yes" or always answering "No" on the image '+
        'change task) will give you the most points.' +
        '\n\n\n\n' +
        'When you are ready, press the SHIFT key to finish the instructions and advance to the first trial.',
        pos=[0, 0],height=0.06,wrapWidth=1.6)
 
    instructions.draw()
    win.flip()

#block trials
blocks = [
    {"blockNum":1,"feedback":0}
]    
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
        #int = blockNum; 0=practice, 1, 2, or 3
    noChangeTrial(block["blockNum"])
    #gather ratings of images (boolean = practice trial?)
    gatherRatings(False)
    #quiz on image changes
    changeMatrix.append(changeQuiz())
    #display feedback & wait
    #int = number of changes
    feedback(block["feedback"])


#                                       Begin Dictator Game                         ###################
# define instruction screen 1
instructions1 = visual.TextStim(win, 'Next, you and the other participant are going to play a different game.\n' +
    ' In this game, there are two roles: First Mover and Second Mover.' +
    '\n' +
    ' You and the other participants will be randomly assigned to one of these two roles.' +
    '\n' +
    ' The role you are assigned will determine the kinds of actions you can perform in the game.' +
    '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n' +
    'Press the SPACE key to advance to ' +
    'the next screen and continue reading the instructions.',
    pos=[0, 0],height=0.06,wrapWidth=1.5)

image0 = visual.ImageStim(win,image='AF_1.jpg',mask=None,units='norm',pos=[-0.7,0.7],size=[0.375,0.5])
image1 = visual.ImageStim(win,image='AF_2.jpg',mask=None,units='norm',pos=[0.7,0.7],size=[0.375,0.5])

#display instruction screen 1
instructions1.draw()
layout.draw()
win.flip()




#                                                    Write data, End experiment            ######################
# trial list
# trialList = sum([[x]*4 for x in range(1, 19)], [])
# list indicating whether each trial was a changeTrial
# and whether each image changed or not
# changeTrialList = sum([[x]*4 for x in [0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0]], [])
# changePicList = [0 for _ in range(72)]
# for changePic in ['9921.jpg', '2190.jpg', '7390.jpg', '3550.jpg', '6150.jpg', '7545.jpg']:
#     changePicList[images.index(changePic)] = 1
# lists for changeMatrix variables:
# yesNo, whichImage, howManyTimes, first, second, third, fourth
# ERROR NOTE: this records numChanges and rank in the order in which they were presented
# ERROR NOTE: should be recorded in the same pre-determined order as the main DVs!
# numChangesList = [0 for _ in range(72)]
# rankList = ['.' for _ in range(72)]
# for trial, vec in enumerate(changeMatrix):
#     if vec[0]=='y':
#         numChangesList[trial*4 + letterToNum(vec[1])] = vec[2]
#     rankList[trial*4 + letterToNum(vec[3])] = 1
#     rankList[trial*4 + letterToNum(vec[4])] = 2
#     rankList[trial*4 + letterToNum(vec[5])] = 3
#     rankList[trial*4 + letterToNum(vec[6])] = 4
# lists for all evaluation ratings
# grid = [(a, b) for a in range(18) for b in range(4)]
# question1 = [ratingMatrix[x][y][0] for x, y in grid]
# question2 = [ratingMatrix[x][y][1] for x, y in grid]
# question3 = [ratingMatrix[x][y][2] for x, y in grid]
# question4 = [ratingMatrix[x][y][3] for x, y in grid]
# question5 = [ratingMatrix[x][y][4] for x, y in grid]
# question6 = [ratingMatrix[x][y][5] for x, y in grid]
# question7 = [ratingMatrix[x][y][6] for x, y in grid]
# write data to file
# fileName = "subject_{}.csv".format(info['   Subject number']) #saves file name as subject number
# print 'Opening data file: ' + fileName
# dataFile = open(fileName, 'a')
# write data
# for i in range(72):
#     dataFile.write('\n' + str(subject) + ',' + str(between) + ',' + str(condition) + ',' + str(order) + ',' + str(info['Date']) +
#     ',' + str(info['   Gender']) + ',' + str(info['   Age']) + ',' + str(totalSuccesses) + ',' + str(totalMistakes) + ',' + str(images[i]) +
#     ',' + str(trialList[i]) + ',' + str(changePicList[i]) + ',' + str(changeTrialList[i]) + ',' + str(numChangesList[i]) +
#     ',' + str(rankList[i]) + ',' + str(question1[i])  + ',' + str(question2[i]) + ',' + str(question3[i]) +
#     ',' + str(question4[i])  + ',' + str(question5[i])  + ',' + str(question6[i])  + ',' + str(question7[i]) +
#     ',' + str(freqList[i]))
# close data file
# dataFile.close()
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
