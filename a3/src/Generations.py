from Individual import individual
from GeneticOperators import select, crossover, mutate

def newGeneration(records: list[individual], sumfitness: float, pcross: float, pmutation: float) -> list[str]:
    """Create new generation through select, crossover, and mutation.
    Note: Generation assume an even-numbered popsize; odd-numbered popsize gets rounded down (popsize -= 1).

    Args:
        records (list[individual]): Records of population with fitness data.
        sumfitness (float): Total fitness score of population in current generation.
        pcross (float): Probability of cross occuring.
        pmutation (float): Probability of mutation.

    Returns:
        list[str]: Population of new generation.
    """
    npop: list[str] = []    # new population
    mate1: str              # first mate in pair
    mate2: str              # second mate in pair
    
    for _ in range(len(records) // 2):
        # --- Reproduction ---
        mate1 = select(records, sumfitness)["chrom"]    # Note: mate1 and mate2 can be the same
        mate2 = select(records, sumfitness)["chrom"]
        # --- Crossover ---
        child1, child2 = crossover(mate1, mate2, pcross)
        # --- Mutation ---
        child1, _ = mutate(child1, pmutation)
        child2, _ = mutate(child2, pmutation)
        # --- New Gen ---
        npop.extend([child1, child2])
    return npop