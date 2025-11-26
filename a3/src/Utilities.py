from typing import Callable
import index
import time
from dt.individual import individual

def decode_2d(chrom: str) -> tuple[int, int]:
    """Decode string as two unsigned binary integers. (Unused)
    Used to substitute x and y in objective functions.

    Args:
        chrom (str): Chromosome as str

    Returns:
        int: Chromosome as normal int, interpreted as binary bit (e.g. '101' -> 5).
    """
    mid: int = len(chrom) // 2
    return int(chrom[:mid], 2), int(chrom[mid:], 2)

def decode_2d_signed(chrom: str) -> tuple[int, int]:
    """Decode string as two signed integers using two's complement.
    
    Args:
        chrom (str): Chromosome as str

    Returns:
        int: Chromosome as normal int, interpreted as binary bit (e.g. '101' -> 5).
    """
    mid = len(chrom) // 2

    def twos_complement(bits: str) -> int:
        value = int(bits, 2)
        # if MSB (most significant bit) is 1, it's negative
        if bits[0] == '1':
            value -= 1 << len(bits)
        return value

    return twos_complement(chrom[:mid]), twos_complement(chrom[mid:])

def getFitness(objfunc: Callable, chrom: str) -> float:
    """Fitness function to get fitness score of chromosome.
    Note: Grants higher fitness for minima, not maxima. 

    Args:
        objfunc (Callable): Objective function.
        chrom (str): Chromosome.

    Returns:
        float: Fitness score.
    """
    chrom1, chrom2 = decode_2d_signed(chrom)
    # Sample space for fitness = [0, 1]. Prevent div-by-0 error.
    return 1 / (1 + objfunc(chrom1, chrom2))

def toPop(objfunc: Callable, lstr: list[str]) -> list[individual]:
    """Get rocords of population from curren generation.
    Individual consist of a record of its string, decoded value, and fitness score.

    Args:
        objfunc (Callable): Objective function.
        lstr (list[str]): Population.

    Returns:
        list[individual]: Records of individuals. (cpy)
    """
    pop: list[individual] = []
    index.index["pop"] = pop

    for chrom in lstr:
        x, y = decode_2d_signed(chrom)
        ind: individual = {
            "chrom": chrom,
            "x": x,
            "y": y,
            "fitness": getFitness(objfunc, chrom)
        }
        pop.append(ind)
        time.sleep(0.3)
    return pop