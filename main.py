from modules import demoTrial, initialize, practiceTrial, controlTrial,\
                    experimentTrial, practiceTrustGame, experimentTrustGame
from lib.runner import go

modules = [
    initialize,
    demoTrial,
    practiceTrial,
    controlTrial,
    experimentTrial,
    practiceTrustGame,
    experimentTrustGame
]

results = go(modules)
print(results)
