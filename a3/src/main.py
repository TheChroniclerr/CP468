from Generators import generateRand
from inputs.ObjectiveFunctions import DeJongSphere
from Generation import newGeneration, nextGeneration
from dt.individual import individual
from dt.generation import generation

MAX_POP = 10        # max population size
MAX_STRING = 20      # max string length

PROBABILITY_MUTATION = 0.05
PROBABILITY_CROSS = 1

OBJECTIVE_FUNCTION = DeJongSphere

if __name__ == "__main__":
    pop: list[individual] = generateRand(MAX_POP, MAX_STRING, OBJECTIVE_FUNCTION)
    gen: generation = newGeneration(pop)    # pop in-place ref
    print(gen["statistics"]["min"]["fitness"], gen["statistics"]["max"]["fitness"], gen["statistics"]["avg"], gen["statistics"]["sum"])
    
    newgen: generation = nextGeneration(gen["population"], gen["statistics"]["sum"], OBJECTIVE_FUNCTION, PROBABILITY_CROSS, PROBABILITY_MUTATION)
    print(newgen["statistics"]["min"]["fitness"], newgen["statistics"]["max"]["fitness"], newgen["statistics"]["avg"], newgen["statistics"]["sum"])