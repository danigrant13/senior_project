from modules import trustGameInstructions2, attentionGameInstructions, initialize, practiceTrial, controlTrial,\
                    experimentTrial, practiceTrustGame, experimentTrustGame, trustGameInstructions
from lib.runner import go

modules = [
    initialize,
    # attentionGameInstructions,
    trustGameInstructions2,
    practiceTrial,
    controlTrial,
    experimentTrial,
    practiceTrustGame,
    experimentTrustGame
]

results = go(modules)
print(results)
