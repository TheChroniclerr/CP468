import random
from dt.individual import individual

def select(pop: list[individual], sumfitness: float) -> individual:
    """Select a single individual via roulette wheel selection.
    Weighted random selection with replacement.

    Args:
        pop (list[individual]): Records of population with fitness data.
        sumfitness (float): Total fitness score of population in current generation.

    Returns:
        individual: Selected individual (ref).
    """
    partsum: float = 0
    rand: float = random.uniform(0, sumfitness)
    
    for ind in pop:
        partsum += ind["fitness"]
        if partsum >= rand:
            return ind
    return pop[-1]

def crossover(parent1: str, parent2: str, pcross: float) -> tuple[str, str]:
    """Cross two parent strings, place in two child strings.

    Args:
        parent1 (str): First parent string.
        parent2 (str): Second parent string.
        pcross (float): Probability of cross occuring.

    Returns:
        tuple[str, str]: Two child strings. (cpy)
    """
    if random.uniform(0, 1) > pcross:
        # No cross
        return parent1, parent2
    
    # TODO: string length of 1?
    site: int = random.randint(1, len(str(parent1)) - 1)    # cross site
    
    child1 = parent1[:site] + parent2[site:]
    child2 = parent2[:site] + parent1[site:]
    return child1, child2 

def mutate(chrom: str, pmutation: float) -> tuple[str, int]:
    """Mutate on all alleles in chromosome each with probability pmutation,
    count the number of mutations.

    Args:
        chrom (str): Chromosome.
        pmutation (float): Probability of mutation.

    Returns:
        tuple[str, int]: The mutated allele, and the number of mutations happened. (cpy)
    """
    nchrom: str = ""        # new string after mutation
    mutations: int = 0      # mutations counter    
    
    for allele in chrom:
        iallele: str = "1" if allele == "0" else "0"    # invert of allele bit value
        if random.uniform(0, 1) < pmutation:
            # Mutate
            nchrom += iallele
            mutations += 1
        else:
            nchrom += allele
    return nchrom, mutations