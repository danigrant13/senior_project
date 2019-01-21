from modules import attentionGameInstructions, attentionRotationQuestionaire, controlTrial,\
                    experimentTrial, experimentTrustGame, genReport, initialize, practiceTrial,\
                    practiceTrustGame, setCollectData, thankYou, trustGameInstructions,\
                    trustGameInstructions2, trustGameTransition
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
    attentionRotationQuestionaire,
    genReport,
    thankYou
] 

results = go(modules)
print(results)
