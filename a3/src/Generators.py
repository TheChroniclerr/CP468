import random
from typing import Callable
from index import index
from Utilities import toPop
from dt.individual import individual

def generateRand(maxpop: int, maxstr: int, objfunc: Callable, bounds: tuple[float, float]) -> list[individual]:
    """Randomly generate a population of size maxpop,
    where each string has length maxstr.

    Args:
        maxpop (int): Size of population.
        maxstr (int): Length of strings.
        objfunc (Callable): Objective function.
        bounds (tuple[float, float]): Bounding square length.

    Returns:
        list[individual]: Population. (cpy)
    """
    lstr: list[str] = []
    
    for _ in range(maxpop):
        s = "".join(random.choice("01") for _ in range(maxstr))
        lstr.append(s)
    return toPop(objfunc, lstr, bounds)