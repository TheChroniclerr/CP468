import index
import threading
from Visualizer import visualize
from Generators import generateRand
from inputs.ObjectiveFunctions import Slope, DeJongSphere, RosenbrockValley, HimmelblauFunction
from Generation import newGeneration, nextGeneration
from dt.individual import individual
from dt.generation import generation

MAX_POP = 80        # max population size
MAX_STRING = 80     # max string length (EVEN NUMBERS RECOMMENDED)

PROBABILITY_MUTATION = 0.05
PROBABILITY_CROSS = 1

BUFFER = 0.01        # Rate to load points in seconds/point
BOUNDS = (-10.0, 10.0)
OBJECTIVE_FUNCTION = RosenbrockValley


def main() -> None:
    # wait for visualizer initiation
    index.index["lock"].wait()
    
    # Code    
    pop: list[individual] = generateRand(MAX_POP, MAX_STRING, OBJECTIVE_FUNCTION, BOUNDS)
    gen: generation = newGeneration(pop)    # pop in-place ref
    print(gen["statistics"]["min"]["fitness"], gen["statistics"]["max"]["fitness"], gen["statistics"]["avg"], gen["statistics"]["sum"])
    
    while True:
        newgen: generation = nextGeneration(gen["population"], gen["statistics"]["sum"], OBJECTIVE_FUNCTION, BOUNDS, PROBABILITY_CROSS, PROBABILITY_MUTATION)
        # print(newgen["statistics"]["min"]["fitness"], newgen["statistics"]["max"]["fitness"], newgen["statistics"]["avg"], newgen["statistics"]["sum"])
        print(newgen["statistics"]["sum"])
        newgen: generation = gen

if __name__ == "__main__":
    # --- Global Variables ---
    index.index["pop"] = []
    index.index["buffer"] = BUFFER
    index.index["lock"] = threading.Event()
    
    # --- Generation ---
    t = threading.Thread(target=main, daemon=True)
    t.start()
    
    # --- Visualization ---
    visualize(BOUNDS, OBJECTIVE_FUNCTION)