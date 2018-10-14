from modules import practiceTrustGameIntro, trustGame
from lib.runner import go


subModules = [practiceTrustGameIntro, trustGame]

silhouette = 'silhouette.jpg'

def run(context):
    for image in context['imageList']:
        image.setImage(silhouette)

    context['trustGameDemo'] = True

    return go(subModules, context)
