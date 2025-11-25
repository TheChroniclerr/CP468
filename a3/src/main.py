from Generators import generate
from ObjectiveFunctions import DeJongSphere
from Utilities import getRecords
from Statistics import getStatistics
from Generations import newGeneration
from Individual import individual

MAX_POP = 10        # max population size
MAX_STRING = 20      # max string length

PROBABILITY_MUTATION = 0.05
PROBABILITY_CROSS = 1

if __name__ == "__main__":
    pop: list[str] = generate(MAX_POP, MAX_STRING)
    records: list[individual] = getRecords(DeJongSphere, pop)
    fmax, fmin, avg, sumfitness = getStatistics(records)
    print(fmax["fitness"], fmin["fitness"], avg, sumfitness)
    
    newpop: list[str] = newGeneration(records, sumfitness, PROBABILITY_CROSS, PROBABILITY_MUTATION)
    records: list[individual] = getRecords(DeJongSphere, newpop)
    fmax, fmin, avg, sumfitness = getStatistics(records)
    print(fmax["fitness"], fmin["fitness"], avg, sumfitness)