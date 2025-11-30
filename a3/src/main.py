import index
import threading
from Visualizer import visualize
from Generators import generateRand, generateRange
from Logs import loadExistingCSV, newRecord, overwrite
from inputs.ObjectiveFunctions import Slope, DeJongSphere, RosenbrockValley, HimmelblauFunction
from Generation import newGeneration, nextGeneration
from dt.individual import individual
from dt.generation import generation

# --- Algorithm Constants ---
MAX_POP = 100        # max population size
MAX_STRING = 80     # max string length (EVEN NUMBERS RECOMMENDED)

PROBABILITY_MUTATION = 0.01
PROBABILITY_CROSS = 1

# --- Visualizer Constants ---
BUFFER = 0.01        # Rate to load points in seconds/point
BOUNDS = (-10.0, 10.0)
OBJECTIVE_FUNCTION = DeJongSphere

# --- Generators Constants ---
BL_RANGE = (0.0, -9.0)
TR_RANGE = (0.0, -9.0)

# --- Logs Constants ---
DEFAULT_DIR: str = "a3/outputs/"
DEFAULT_PATH: str = DEFAULT_DIR + OBJECTIVE_FUNCTION.__name__ + ".csv"
CSV_HEADER: list = ["generation", "min_string", "min_fitness", "max_string", "max_fitness", "avg_fitness", "sum_fitness"]

def main() -> None:
    # wait for visualizer initiation
    index.index["lock"].wait()
    
    # Code    
    pop: list[individual] = generateRange(MAX_POP, MAX_STRING, OBJECTIVE_FUNCTION, BOUNDS, BL_RANGE, TR_RANGE)
    # pop: list[individual] = generateRand(MAX_POP, MAX_STRING, OBJECTIVE_FUNCTION, BOUNDS)
    gen: generation = newGeneration(0, pop)    # pop in-place ref
    print(gen["statistics"]["min"]["fitness"], gen["statistics"]["max"]["fitness"], gen["statistics"]["avg"], gen["statistics"]["sum"])

    records: list[dict] = []
    while True:
        # Log
        record: dict = newRecord(CSV_HEADER, [
            str(gen["number"]), 
            str(gen["statistics"]["min"]["chrom"]), str(gen["statistics"]["min"]["fitness"]),
            str(gen["statistics"]["max"]["chrom"]), str(gen["statistics"]["max"]["fitness"]),
            str(gen["statistics"]["avg"]),
            str(gen["statistics"]["sum"])
        ])
        records.append(record)
        overwrite(DEFAULT_PATH, CSV_HEADER, records)
        
        # Generation
        newgen: generation = nextGeneration(gen, OBJECTIVE_FUNCTION, BOUNDS, PROBABILITY_CROSS, PROBABILITY_MUTATION)
        # print(newgen["statistics"]["min"]["fitness"], newgen["statistics"]["max"]["fitness"], newgen["statistics"]["avg"], newgen["statistics"]["sum"])
        print(newgen["statistics"]["sum"])
        gen: generation = newgen

if __name__ == "__main__":
    # --- Global Variables ---
    index.index["pop"] = []
    index.index["buffer"] = BUFFER
    index.index["lock"] = threading.Event()
    
    # --- Generation ---
    t = threading.Thread(target=main, daemon=True)
    t.start()
    
    # --- Logging ---
    overwrite(DEFAULT_PATH, CSV_HEADER, [])
    
    # --- Visualization ---
    visualize(BOUNDS, OBJECTIVE_FUNCTION)