from modules import trustGameInstructions2, attentionGameInstructions, initialize, practiceTrial, controlTrial,\
                    experimentTrial, practiceTrustGame, experimentTrustGame, thankYou,\
                    trustGameInstructions, trustGameTransition
from lib.runner import go

modules = [
    initialize,
    #attentionGameInstructions,
    #trustGameInstructions2,
    #practiceTrial,
    #controlTrial,
    #experimentTrial,
    trustGameTransition,
    practiceTrustGame,
    experimentTrustGame,
    thankYou
]

results = go(modules)
print(results)
