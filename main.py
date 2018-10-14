from modules import attentionGameInstructions, initialize, practiceTrial, controlTrial,\
                    experimentTrial, practiceTrustGame, experimentTrustGame, trustGameInstructions
from lib.runner import go

modules = [
    initialize,
    attentionGameInstructions,
    trustGameInstructions,
    practiceTrial,
    controlTrial,
    experimentTrial,
    practiceTrustGame,
    experimentTrustGame
]

results = go(modules)
print(results)
