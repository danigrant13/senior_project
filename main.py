from modules import demoTrial, initialize, practiceTrial, controlTrial, experimentTrial, practiceTrustGame
from lib.runner import go

modules = [
    initialize,
    demoTrial,
    practiceTrial,
    controlTrial,
    experimentTrial,
    practiceTrustGame
]

results = go(modules)
print(results)
