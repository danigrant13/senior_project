from modules import trustGameInstructions2, attentionGameInstructions, initialize, practiceTrial, controlTrial,\
                    experimentTrial, practiceTrustGame, experimentTrustGame, genReport, setCollectData, thankYou,\
                    trustGameInstructions, trustGameTransition
from lib.runner import go

modules = [
    initialize,
    attentionGameInstructions,
    trustGameInstructions2,
    practiceTrustGame,
    practiceTrial,
    setCollectData,
    controlTrial,
    experimentTrial,
    trustGameTransition,
    experimentTrustGame,
    genReport,
    thankYou
]

results = go(modules)
print(results)
