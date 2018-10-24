from psychopy import core, visual, event, gui
import random, time

initialOptions = {
  '   Age': 21,
  '   Gender': 'f', #must be male or female
  '   Subject number':1,
  ' Block length (secs)':30,          # for experiment = 120 sec
  ' Practice length (secs)':120,          # for experiment = 120 sec
  'Date':time.strftime("%m-%d-%Y@%H.%M", time.localtime()),
  'Vowel probability':0.3,
  'Letter change interval (secs)':2.75,
  'Rotation speed (degrees/frame)':15,
  'Min rotation interval (secs)':1.75,
  'Max rotation interval (secs)':3.75,
  'Letter blink duration (secs)':0.250
}

demographicImages = {
    'f': [
        ['WF_1.jpg', 'WF_2.jpg', 'WF_3.jpg', 'WF_4.jpg', 'F1'],
        ['BF_1.jpg', 'BF_2.jpg', 'BF_3.jpg', 'BF_4.jpg', 'F2'],
        ['AF_1.jpg', 'AF_2.jpg', 'AF_3.jpg', 'AF_4.jpg', 'F3'],
        ['LF_1.jpg', 'LF_2.jpg', 'LF_3.jpg', 'LF_4.jpg', 'F4'],
        ['LF_1.jpg', 'LF_2.jpg', 'LF_3.jpg', 'LF_4.jpg', 'F5']
    ],
    'pf': ['PF_1.jpg', 'PF_2.jpg', 'PF_3.jpg', 'PF_4.jpg', 'PF_1b.jpg'],
    'm': [
        ['WM_1.jpg', 'WM_2.jpg', 'WM_3.jpg', 'WM_4.jpg', 'M1'],
        ['BM_1.jpg', 'BM_2.jpg', 'BM_3.jpg', 'BM_4.jpg', 'M2'],
        ['AM_1.jpg', 'AM_2.jpg', 'AM_3.jpg', 'AM_4.jpg', 'M3'],
        ['LM_1.jpg', 'LM_2.jpg', 'LM_3.jpg', 'LM_4.jpg', 'M4'],
        ['LM_1.jpg', 'LM_2.jpg', 'LM_3.jpg', 'LM_4.jpg', 'M5']
    ],
    'pm': ['PM_1.jpg','PM_2.jpg', 'PM_3.jpg', 'PM_4.jpg', 'PM_1b.jpg'],
}

windowX = 1920
windowY = 1080

def run(context):
    infoDlg = gui.DlgFromDict(dictionary=initialOptions, title='Attention study', fixed=['Date'])
    if not infoDlg.OK:
        print 'User Cancelled'
        core.quit()

    win = visual.Window(
        [windowX,windowY],
        rgb=(-1,-1,-1),
        allowGUI=False,
        winType='pyglet'
    )

    imageList = [
        visual.ImageStim(win,image='AF_1.jpg',mask=None,units='norm',pos=[-0.7,0.7],size=[0.375,0.5]),
        visual.ImageStim(win,image='AF_2.jpg',mask=None,units='norm',pos=[0.7,0.7],size=[0.375,0.5]),
        visual.ImageStim(win,image='AF_3.jpg',mask=None,units='norm',pos=[-0.7,-0.7],size=[0.375,0.5]),
        visual.ImageStim(win,image='AF_4.jpg',mask=None,units='norm',pos=[0.7,-0.7],size=[0.375,0.5])
    ]

    markerList = [
        visual.TextStim(win,'A',pos=[-0.8,0.38],height=0.13),
        visual.TextStim(win,'B',pos=[0.8,0.38],height=0.13),
        visual.TextStim(win,'C',pos=[-0.8,-0.38],height=0.13),
        visual.TextStim(win,'D',pos=[0.8,-0.38],height=0.13)
    ]

    updated_options = __validate(initialOptions)
    gender = updated_options['gender']
    trialImages = random.sample(demographicImages[gender], 2)

    context['window'] = win
    context['windowX'] = windowX
    context['windowY'] = windowY
    context['options'] = updated_options
    context['imageList'] = imageList
    context['markerList'] = markerList

    context['practiceImages'] = demographicImages['p' + gender]
    context['controlImages'] = trialImages[0][:4]
    context['trialImages'] = trialImages[1][:4]
    context['controlGroup'] = trialImages[0][-1]
    context['trialGroup'] = trialImages[1][-1]

    random.shuffle(context['controlImages'])
    random.shuffle(context['trialImages'])

    # attention task change settings
    context['target'] = 0
    context['changeSide1'] = ""
    context['changeSide2'] = ""
    context['nonTargetList'] = [1, 2, 3]
    context['changeProb'] = 0.25
    # setting 'numberOfChanges' > 0 causes target to flip sides
    # all change settings must be set in this case
    # you should do this in the appropriate module implementing the task
    # e.g. modules/practiceTrial.py
    context['numberOfChanges'] = 0

    context['report'] = {
        'headers': __initHeaders(),
        'data': __initData(context),
    }
    context['collectData'] = False

    return context

def __initHeaders():
    return [
        "Pt #",
        "Age",
        "Gender",
        "Length of control attention trial (seconds)",
        "Length of experimental attention trial (seconds)",
        "Control group",
        "Order of control group pictures",
        "Experimental Group",
        "Order of experimental group pictures"
    ]

def __initData(context):
    return [
        context['options']['subject'],
        context['options']['age'],
        context['options']['gender'],
        context['options']['blockLength'],
        context['options']['blockLength'],
        context['controlGroup'],
        " ".join(context['controlImages']),
        context['trialGroup'],
        " ".join(context['trialImages'])
    ]

def __validate(options):
    gender = options['   Gender']
    vowelProb = options['Vowel probability']
    letterInterval = options['Letter change interval (secs)']
    speed = options['Rotation speed (degrees/frame)']
    rotateMin = options['Min rotation interval (secs)']
    rotateMax = options['Max rotation interval (secs)']
    blockLength = options[' Block length (secs)']
    practiceLength = options[' Practice length (secs)']
    letterPause = options['Letter blink duration (secs)']

    if gender not in ['f', 'm']:
        print 'Error: gender mut be on of f or m!'
        print 'Subject number was set to: ' + str(options['   Subject number'])
        core.quit()

    #check subject number for integer format
    try:
        subject = int(options['   Subject number'])
    except:
        print 'Error: subject number must be a positive integer!'
        print 'Subject number was set to: ' + str(options['   Subject number'])
        core.quit()

    try:
        age = int(options['   Age'])
    except:
        print 'Error: age must be a positive integer!'
        print 'age was set to: ' + str(options['   Age'])
        core.quit()
    #check subject number for range
    if not subject>=0:
        print 'Error: subject number must be a positive integer!'
        print 'Subject number was set to: ' + str(options['   Subject number'])
        core.quit()

    if not age>=18:
        print 'Error: must be 18 years or older'
        print 'age was set to: ' + str(options['   Age'])
        core.quit()

    return {
        'age': age,
        'subject': subject,
        'gender': gender.lower(),
        'vowelProb': vowelProb,
        'letterInterval': letterInterval,
        'speed': speed,
        'rotateMin': rotateMin,
        'rotateMax': rotateMax,
        'blockLength': blockLength,
        'practiceLength': practiceLength,
        'letterPause': letterPause
    }
