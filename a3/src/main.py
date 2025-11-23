import random
from typing import Callable
from Individual import individual

MAX_POP = 10        # max population size
MAX_STRING = 7      # max string length

PROBABILITY_MUTATION = 0.05
PROBABILITY_CROSS = 1

def select(records: list[individual], sumfitness: int) -> individual:
    """Select a single individual via roulette wheel selection.
    Weighted random selection with replacement.

    Args:
        records (list[individual]): Records of population with fitness data.
        sumfitness (int): Total fitness score of population in current generation.

    Returns:
        individual: Selected individual (ref).
    """
    partsum: int = 0
    rand: int = int(random.uniform(0, 1) * sumfitness)
    
    for individual in records:
        partsum += individual["fitness"]
        if partsum >= rand:
            return individual
    return records[-1]

def crossover(parent1: str, parent2: str, pcross: float) -> tuple[str, str]:
    """Cross two parent strings, place in two child strings.

    Args:
        parent1 (str): First parent string.
        parent2 (str): Second parent string.
        pcross (float): Probability of cross occuring.

    Returns:
        tuple[str, str]: Two child strings (cpy).
    """
    if random.uniform(0, 1) > pcross:
        # No cross
        return parent1, parent2
    
    site: int = random.randint(1, len(str(parent1)) - 1)    # cross site
    
    child1: str = parent1[0:site-1] + parent2[site:-1]
    child2: str = parent2[0:site-1] + parent1[site:-1]
    return child1, child2 

def mutate(chrom: str, pmutation: float) -> tuple[str, int]:
    """Mutate on all alleles in chromosome each with probability pmutation,
    count the number of mutations.

    Args:
        chrom (str): Chromosome.
        pmutation (float): Probability of mutation.

    Returns:
        tuple[str, int]: The mutated allele, and the number of mutations happened (cpy).
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

def newGeneration(records: list[individual], sumfitness: int, pcross: float, pmutation: float) -> list[str]:
    """Create new generation through select, crossover, and mutation.

    Args:
        records (list[individual]): Records of population with fitness data.
        sumfitness (int): Total fitness score of population in current generation.
        pcross (float): Probability of cross occuring.
        pmutation (float): Probability of mutation.

    Returns:
        list[str]: Population of new generation.
    """
    npop: list[str] = []    # new population
    mate1: str              # first mate in pair
    mate2: str              # second mate in pair
    
    for _ in range(len(records)):
        # --- Reproduction ---
        mate1 = select(records, sumfitness)["chrom"]    # TODO: mate1 and mate2 the same?
        mate2 = select(records, sumfitness)["chrom"]
        # --- Crossover ---
        child1, child2 = crossover(mate1, mate2, pcross)
        # --- Mutation ---
        child1, _ = mutate(child1, pmutation)
        child2, _ = mutate(child2, pmutation)
        # --- New Gen ---
        npop.extend([child1, child2])
    return npop

def decode(chrom: str) -> int:
    """Decode string as unsigned binary integer.

    Args:
        chrom (str): Chromosome as str

    Returns:
        int: Chromosome as normal int, interpreted as binary bit (e.g. '101' -> 5). 
    """
    bchrom: int = 0
    
    for i, allele in enumerate(chrom):
        bchrom += 2 ** i if allele == "1" else 0
    return bchrom

def getFitness(objfunc: Callable, chrom: str) -> int:
    """Fitness function to get fitness score of chromosome.

    Args:
        objfunc (Callable): Objective function.
        chrom (str): Chromosome.

    Returns:
        int: Fitness score.
    """
    bchrome: int = decode(chrom)
    return objfunc(bchrome)

def getRecords(objfunc: Callable, pop: list[str]) -> list[individual]:
    """Get rocords of population from curren generation.
    Individual consist of a record of its string, decoded value, and fitness score.

    Args:
        objfunc (Callable): Objective function.
        pop (list[str]): Population.

    Returns:
        list[individual]: Records of individuals.
    """
    records: list[individual] = []
    
    for chrom in pop:
        ind: individual = {
            "chrom": chrom,
            "x": decode(chrom),
            "fitness": getFitness(objfunc, chrom)
        }
        records.append(ind)
    return records

def getStatistics(records: list[individual]) -> tuple[individual, individual, int, int]:
    """Calculate population statistics - max, min, avg, sum.

    Args:
        records (list[individual]): Records of population with fitness data.

    Returns:
        tuple[individual, individual, int, int]:
            Max fitness score individual, 
            min fitness score individual,
            avg fitness score of population, 
            sum of population fitness scores
    """
    fmax: individual = max(records, key=lambda ind: ind["fitness"])
    fmin: individual = min(records, key=lambda ind: ind["fitness"])
    sumfitness: int = sum(ind["fitness"] for ind in records)
    avg: int = int(sumfitness / len(records))
    return fmax, fmin, avg, sumfitness

def generate(maxpop: int, maxstr: int) -> list[str]:
    """Randomly generate a population of size maxpop,
    where each string has length maxstr.

    Args:
        maxpop (int): Size of population.
        maxstr (int): Length of strings.

    Returns:
        list[str]: Population.
    """
    pop: list[str] = []
    
    for _ in range(maxpop):
        s = "".join(random.choice("01") for _ in range(maxstr))
        pop.append(s)
    return pop

def DeJongSphere(x: float, y: float) -> float:
    """De Jong function for optimization problems.
    Objective function with single-objective.

    Args:
        x (float): Variable x.
        y (float): Variable y.

    Returns:
        float: Objective value (i.e. fitness score).
    """
    return x**2 + y**2

if __name__ == "__main__":
    pop: list[str] = generate(MAX_POP, MAX_STRING)
    records: list[individual] = getRecords(DeJongSphere, pop)
    fmax, fmin, avg, sumfitness = getStatistics(records)
    newpop: list[str] = newGeneration(records, sumfitness, PROBABILITY_CROSS, PROBABILITY_MUTATION)