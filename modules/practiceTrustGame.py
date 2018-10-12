from modules import trustGame, trustGameInstructions
from lib.runner import go


subModules = [trustGameInstructions, trustGame]

silhouette = 'silhouette.jpg'

def run(context):
    for image in context['imageList']:
        image.setImage(silhouette)

    context['trustGameDemo'] = True

    return go(subModules, context)
