from modules import trustGame

def run(context):
    trialImages = context['trialImages']
    imageList = context['imageList']

    for index in range(4):
        imageList[index].setImage(trialImages[index])

    context['trustGameDemo'] = False

    return trustGame.run(context)
