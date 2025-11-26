import index
import threading
from Visualizer import visualize
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

def main() -> None:
    # wait for visualizer initiation
    index.index["lock"].wait()
    
    # Code    
    pop: list[individual] = generateRand(MAX_POP, MAX_STRING, OBJECTIVE_FUNCTION)
    gen: generation = newGeneration(pop)    # pop in-place ref
    print(gen["statistics"]["min"]["fitness"], gen["statistics"]["max"]["fitness"], gen["statistics"]["avg"], gen["statistics"]["sum"])
    
    while True:
        newgen: generation = nextGeneration(gen["population"], gen["statistics"]["sum"], OBJECTIVE_FUNCTION, PROBABILITY_CROSS, PROBABILITY_MUTATION)
        print(newgen["statistics"]["min"]["fitness"], newgen["statistics"]["max"]["fitness"], newgen["statistics"]["avg"], newgen["statistics"]["sum"])
        newgen: generation = gen

if __name__ == "__main__":
    # --- Global Variables ---
    index.index["pop"] = []
    index.index["lock"] = threading.Event()
    
    # --- Generation ---
    bounds = [-(2 ** (MAX_STRING // 2 - 1)), 2 ** (MAX_STRING // 2 - 1) - 1]
    objfunc = DeJongSphere
    
    t = threading.Thread(target=main, daemon=True)
    t.start()
    
    # --- Visualization ---
    visualize(bounds, objfunc)