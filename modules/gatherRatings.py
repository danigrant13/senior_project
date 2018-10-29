from psychopy import visual
from lib.utils import proceedOrQuit

ratingScaleText = """\
      Please answer a few questions about your reaction to these four
                                         faces during the trial.
                           Enter a number between 0 and 7, with 
       0 = "Not at all" or "Very bad" and 7 = "Very much" or "Very good."

    Not at all ---------------------------------------------------------------- Very much
          1             2             3             4             5             6             7
     Very bad ---------------------------------------------------------------- Very good

"""

question1Text = 'How much do you like this person?'
question2Text = 'What is your overall impression of this person?'
question3Text = 'How threatening do you find this person?'
question4Text = 'How much do you trust this person?'
question5Text = 'How intimidating do you find this person?'
question6Text = 'How attractive do you find this person?'
question7Text = 'How interested are you in being paired with this person in a future study?'

yourAnswer = 'Your answer:'


def __drawRatings(win, imageStim, ratingVisuals, screenNum, questionNum, answers):
    for instruction in ratingVisuals['instructions']:
        instruction.draw()

    for q in range(questionNum+1):
        question, prompt = ratingVisuals['questions'][q]
        prompt.setText(yourAnswer + answers[screenNum][q])
        question.draw()
        prompt.draw()

    imageStim.draw()

    win.flip()

def __handleRangeInput(input, screen, question, answers):
    for key in input:
        if key in ['1', '2', '3', '4', '5', '6', '7']:
            answers[screen][question] = key
        elif key == 'lshift':
            return -1
        elif key == 'space':
            return 1
    return 0

def __initAnswersArray(numQuestions=7):
    answerList = ['' for x in range(numQuestions)]
    return [answerList, list(answerList), list(answerList), list(answerList)]

def __setData(context, answers):
    trial = 'control' if context['trialNum'] == 0 else 'exp'
    headerFormat = '{}_{}_Q{}'
    letterList = ['A', 'B', 'C', 'D']
    for index, answerList in enumerate(answers):
        headers = [headerFormat.format(letterList[index], trial, question + 1) for question in range(7)]
        context['report']['headers'] += headers
        context['report']['data'] += answerList

def run(context, collectData=False):
    win = context['window']
    imageList = context['imageList']
    answers = __initAnswersArray()

    ratingInstructions1 = visual.TextStim(win, ratingScaleText,
            pos=[0,0.70],height=0.04,wrapWidth=0.95)
    ratingInstructions2 = visual.TextStim(win,'Press the SPACE key after each response to continue.',
                                          pos=[0,-0.7],height=0.05,wrapWidth=0.9)

    rating1 = visual.TextStim(win, question1Text, pos=[0,0.45], height=0.05, wrapWidth=1.5)
    rating2 = visual.TextStim(win, question2Text, pos=[0,0.33], height=0.05, wrapWidth=1.5)
    rating3 = visual.TextStim(win, question3Text, pos=[0,0.21], height=0.05, wrapWidth=1.5)
    rating4 = visual.TextStim(win, question4Text, pos=[0,0.09], height=0.05, wrapWidth=1.5)
    rating5 = visual.TextStim(win, question5Text, pos=[0,-0.03], height=0.05, wrapWidth=1.5)
    rating6 = visual.TextStim(win, question6Text, pos=[0,-0.15], height=0.05, wrapWidth=1.5)
    rating7 = visual.TextStim(win, question7Text, pos=[0,-0.27], height=0.05, wrapWidth=1.5)

    rating1a = visual.TextStim(win, yourAnswer, pos=[0,0.39], height=0.05, wrapWidth=1.5)
    rating2a = visual.TextStim(win, yourAnswer, pos=[0,0.27], height=0.05, wrapWidth=1.5)
    rating3a = visual.TextStim(win, yourAnswer, pos=[0,0.15], height=0.05, wrapWidth=1.5)
    rating4a = visual.TextStim(win, yourAnswer, pos=[0,0.03], height=0.05, wrapWidth=1.5)
    rating5a = visual.TextStim(win, yourAnswer, pos=[0,-0.09], height=0.05, wrapWidth=1.5)
    rating6a = visual.TextStim(win, yourAnswer, pos=[0,-0.21], height=0.05, wrapWidth=1.5)
    rating7a = visual.TextStim(win, yourAnswer, pos=[0,-0.33], height=0.05, wrapWidth=1.5)

    ratingVisuals = {
        'instructions': [ratingInstructions1, ratingInstructions2],
        'questions': [
            (rating1, rating1a),
            (rating2, rating2a),
            (rating3, rating3a),
            (rating4, rating4a),
            (rating5, rating5a),
            (rating6, rating6a),
            (rating7, rating7a)
        ]
    }

    for x in imageList:
        x.setOri(0)

    for screen, image in enumerate(imageList):
        question = 0
        while question < 7:
            __drawRatings(win, image, ratingVisuals, screen, question, answers)

            input = proceedOrQuit(win, keys=['escape','lshift','space','1','2','3','4','5','6','7'])
            proceed = __handleRangeInput(input, screen, question, answers)
            if proceed < 0 and question > 0:
                question -= 1
            elif proceed > 0 and answers[screen][question] != '':
                question += 1

    if context['collectData']:
        __setData(context, answers)

    return context
