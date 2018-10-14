from modules import demoTrial, experimentalAttentionInstructions
from lib.runner import go

subModules = [demoTrial, experimentalAttentionInstructions]

def run(context):
    return go(subModules, context)
