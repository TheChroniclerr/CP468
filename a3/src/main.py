import random
from typing import Callable
from Individual import individual

MAX_POP = 10        # max population size
MAX_STRING = 20      # max string length

PROBABILITY_MUTATION = 0.05
PROBABILITY_CROSS = 1

def select(records: list[individual], sumfitness: float) -> individual:
    """Select a single individual via roulette wheel selection.
    Weighted random selection with replacement.

    Args:
        records (list[individual]): Records of population with fitness data.
        sumfitness (float): Total fitness score of population in current generation.

    Returns:
        individual: Selected individual (ref).
    """
    partsum: float = 0
    rand: float = random.uniform(0, sumfitness)
    
    for ind in records:
        partsum += ind["fitness"]
        if partsum >= rand:
            return ind
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

def decode_2d(chrom: str) -> tuple[int, int]:
    """Decode string as two unsigned binary integers.
    Used to substitute x and y in objective functions.

    Args:
        chrom (str): Chromosome as str

    Returns:
        int: Chromosome as normal int, interpreted as binary bit (e.g. '101' -> 5). 
    """
    mid: int = len(chrom) // 2
    return int(chrom[:mid], 2), int(chrom[mid:], 2)

def getFitness(objfunc: Callable, chrom: str) -> float:
    """Fitness function to get fitness score of chromosome.
    Note: Grants higher fitness for minima, not maxima. 

    Args:
        objfunc (Callable): Objective function.
        chrom (str): Chromosome.

    Returns:
        float: Fitness score.
    """
    chrom1, chrom2 = decode_2d(chrom)
    # Sample space for fitness = [0, 1]. Prevent div-by-0 error.
    return 1 / (1 + objfunc(chrom1, chrom2))

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
        x, y = decode_2d(chrom)
        ind: individual = {
            "chrom": chrom,
            "x": x,
            "y": y,
            "fitness": getFitness(objfunc, chrom)
        }
        records.append(ind)
    return records

def getStatistics(records: list[individual]) -> tuple[individual, individual, float, float]:
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
    sumfitness: float = sum(ind["fitness"] for ind in records)
    avg: float = sumfitness / len(records)
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
    print(fmax["fitness"], fmin["fitness"], avg, sumfitness)
    
    newpop: list[str] = newGeneration(records, sumfitness, PROBABILITY_CROSS, PROBABILITY_MUTATION)
    records: list[individual] = getRecords(DeJongSphere, newpop)
    fmax, fmin, avg, sumfitness = getStatistics(records)
    print(fmax["fitness"], fmin["fitness"], avg, sumfitness)