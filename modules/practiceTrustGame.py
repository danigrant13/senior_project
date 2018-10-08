from modules import trustGame

silhouette = 'silhouette.jpg'

def run(context):
    for image in context['imageList']:
        image.setImage(silhouette)
    return trustGame.run(context)
