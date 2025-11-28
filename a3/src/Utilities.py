import time
from typing import Callable
import index
from dt.individual import individual

def decode_2d(chrom: str) -> tuple[int, int]:
    """Decode string as two unsigned binary integers. (Unused)
    Used to substitute x and y in objective functions.

    Args:
        chrom (str): Chromosome as str

    Returns:
        int: Chromosomes as normal int, interpreted as binary bit (e.g. '101' -> 5).
    """
    mid: int = len(chrom) // 2
    return int(chrom[:mid], 2), int(chrom[mid:], 2)

def decode_2d_signed(chrom: str) -> tuple[int, int]:
    """Decode string as two signed integers using two's complement.
    
    Args:
        chrom (str): Chromosome as str

    Returns:
        int: Chromosomes as two's complement (e.g. '101' -> -3).
    """
    mid = len(chrom) // 2

    def twos_complement(bits: str) -> int:
        value = int(bits, 2)
        # if MSB (most significant bit) is 1, it's negative
        if bits[0] == '1':
            value -= 1 << len(bits)
        return value
    return twos_complement(chrom[:mid]), twos_complement(chrom[mid:])

def decode_2d_sclaed(chrom: str, bounds: tuple[float, float]) -> tuple[float, float]:
    """Decode string into a normalized scale between [0, 1],
    then apply that scale to the square bounds.
    
    Args:
        chrom (str): Chromosome as str
        bounds (tuple[float, float]): Bounding square length.

    Returns:
        tuple[float, float]: Chromosomes scaled to the bounding square.
    """
    mid = len(chrom) // 2
    
    # Normalize
    units: int = 2**mid - 1       # max representations of one chromosome - 1
    xnorm: float = int(chrom[:mid], 2) / units    # normalize to [-1,1]
    ynorm: float = int(chrom[mid:], 2) / units
    
    # Coodinates in bound
    lbound: float = bounds[1] - bounds[0]       # Length of bounds of data range square
    return (bounds[0] + xnorm * lbound, 
            bounds[0] + ynorm * lbound)

def getFitness(objfunc: Callable, chrom1: float, chrom2: float) -> float:
    """Fitness function to get fitness score of chromosome.
    Note: Grants higher fitness for minima, not maxima. 

    Args:
        objfunc (Callable): Objective function.
        chrom1 (str): Chromosome one.
        chrom2 (str): Chromosome two.

    Returns:
        float: Fitness score.
    """
    # Sample space for fitness = [0, 1]. Prevent div-by-0 error.
    return 1 / (1 + objfunc(chrom1, chrom2))
    # return objfunc(chrom1, chrom2)

def toPop(objfunc: Callable, lstr: list[str], bounds: tuple[float, float]) -> list[individual]:
    """Get rocords of population from curren generation.
    Individual consist of a record of its string, decoded value, and fitness score.

    Args:
        objfunc (Callable): Objective function.
        lstr (list[str]): Population.
        bounds (tuple[float, float]): Bounding square length.

    Returns:
        list[individual]: Records of individuals. (cpy)
    """
    pop: list[individual] = []
    index.index["pop"] = pop

    for chrom in lstr:
        x, y = decode_2d_sclaed(chrom, bounds)
        ind: individual = {
            "chrom": chrom,
            "x": x,
            "y": y,
            "fitness": getFitness(objfunc, x, y)
        }
        pop.append(ind)
        time.sleep(index.index["buffer"])
    return pop