from typing import Callable
from Stats import getStats
from Utilities import toPop
from GeneticOperators import select, crossover, mutate
from dt.stats import stats
from dt.individual import individual
from dt.generation import generation

def newGeneration(num: int, pop: list[individual]) -> generation:
    """Create new generation data given a population of individuals.

    Args:
        num (int): Number for the current generation.
        pop (list[individual]): Records of population with fitness data.

    Returns:
        generation: Generation data. ("population" ref, "statistics" cpy)
    """
    cstats: stats = getStats(pop)
    
    gen: generation = {
        "number": num,
        "population": pop,
        "statistics": cstats
    }
    return gen

def nextGeneration(gen: generation, objfunc: Callable, bounds: tuple[float, float], pcross: float, pmutation: float) -> generation:
    """Create new generation through select, crossover, and mutation.
    Note: Generation assume an even-numbered popsize; odd-numbered popsize gets rounded down (popsize -= 1).

    Args:
        pop (generation): Previous generation data.
        objfunc (Callable): Objective function.
        bounds (tuple[float, float]): Length of bounding square.
        pcross (float): Probability of cross occuring.
        pmutation (float): Probability of mutation.

    Returns:
        generation: New generation data. (cpy)
    """
    pop: list[individual] = gen["population"]
    sumfitness: float = gen["statistics"]["sum"]
    
    nstr: list[str] = []    # list of strings
    mate1: str              # first mate in pair
    mate2: str              # second mate in pair
    
    for _ in range(len(pop) // 2):
        # --- Reproduction ---
        mate1 = select(pop, sumfitness)["chrom"]    # Note: mate1 and mate2 can be the same
        mate2 = select(pop, sumfitness)["chrom"]    # mate1 and mate2 are refs
        # --- Crossover ---
        child1, child2 = crossover(mate1, mate2, pcross)
        # --- Mutation ---
        child1, _ = mutate(child1, pmutation)
        child2, _ = mutate(child2, pmutation)
        # --- New Gen ---
        nstr.extend([child1, child2])
        
    npop: list[individual] = toPop(objfunc, nstr, bounds)
    return newGeneration(gen["number"] + 1, npop)