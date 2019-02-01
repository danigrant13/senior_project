from psychopy import core, visual, event, gui
import random, time

initialOptions = {
  '   Age': 0,
  '   Gender': '.', #must be male or female
  '   Subject number':0,
  ' Block length (secs)':120,          # for experiment = 120 sec
  ' Practice length (secs)':30,          # for practice = 30 sec
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
        ['F_1.jpg', 'F_2.jpg', 'F_3.jpg', 'F_4.jpg', 'F1'],
        ['F_5.jpg', 'F_6.jpg', 'F_7.jpg', 'F_8.jpg', 'F2'],
        ['F_9.jpg', 'F_10.jpg', 'F_11.jpg', 'F_12.jpg', 'F3'],
        ['F_13.jpg', 'F_14.jpg', 'F_15.jpg', 'F_16.jpg', 'F4'],
        ['F_17.jpg', 'F_18.jpg', 'F_19.jpg', 'F_20.jpg', 'F5']
    ],
    'pf': ['PF_1.jpg', 'PF_2.jpg', 'PF_3.jpg', 'PF_4.jpg', 'PF_1b.jpg'],
    'm': [
        ['M_1.jpg', 'M_2.jpg', 'M_3.jpg', 'M_4.jpg', 'M1'],
        ['M_5.jpg', 'M_6.jpg', 'M_7.jpg', 'M_8.jpg', 'M2'],
        ['M_9.jpg', 'M_10.jpg', 'M_11.jpg', 'M_12.jpg', 'M3'],
        ['M_13.jpg', 'M_14.jpg', 'M_15.jpg', 'M_16.jpg', 'M4'],
        ['M_17.jpg', 'M_18.jpg', 'M_19.jpg', 'M_20.jpg', 'M5']
    ],
    'pm': ['PM_1.jpg','PM_2.jpg', 'PM_3.jpg', 'PM_4.jpg', 'PM_1b.jpg'],
}

windowX = 1920
windowY = 1080

def run(context):
    infoDlg = gui.DlgFromDict(dictionary=initialOptions, title='Attention study', fixed=['Date'])
    if not infoDlg.OK:
        print('User Cancelled')
        core.quit()

    win = visual.Window(
        [windowX,windowY],
        rgb=(-1,-1,-1),
        allowGUI=False,
        winType='pyglet'
    )

    imageList = [
        visual.ImageStim(win,image='F_1.jpg',mask=None,units='norm',pos=[-0.7,0.7],size=[0.375,0.5]),
        visual.ImageStim(win,image='F_2.jpg',mask=None,units='norm',pos=[0.7,0.7],size=[0.375,0.5]),
        visual.ImageStim(win,image='F_3.jpg',mask=None,units='norm',pos=[-0.7,-0.7],size=[0.375,0.5]),
        visual.ImageStim(win,image='F_4.jpg',mask=None,units='norm',pos=[0.7,-0.7],size=[0.375,0.5])
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
        print('Error: gender mut be on of f or m!')
        print('Subject number was set to: ' + str(options['   Subject number']))
        core.quit()

    #check subject number for integer format
    try:
        subject = int(options['   Subject number'])
    except:
        print('Error: subject number must be a positive integer!')
        print('Subject number was set to: ' + str(options['   Subject number']))
        core.quit()

    try:
        age = int(options['   Age'])
    except:
        print('Error: age must be a positive integer!')
        print('age was set to: ' + str(options['   Age']))
        core.quit()
    #check subject number for range
    if not subject>=0:
        print('Error: subject number must be a positive integer!')
        print('Subject number was set to: ' + str(options['   Subject number']))
        core.quit()

    if not age>=18:
        print('Error: must be 18 years or older')
        print('age was set to: ' + str(options['   Age']))
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
