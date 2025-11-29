import random
from typing import Callable
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

def generateRange(maxpop: int, maxstr: int, objfunc: Callable, bounds: tuple[float, float], corner1: tuple[float, float], corner2: tuple[float, float]) -> list[individual]:
    """Randomly generate a population of within range corner1 and corner 2.

    Args:
        maxpop (int): Size of population.
        maxstr (int): Length of strings.
        objfunc (Callable): Objective function.
        bounds (tuple[float, float]): Bounding square length.
        corner1 (tuple[float, float]): Bottom left corner of range.
        corner2 (tuple[float, float]): Top right corner of range.

    Returns:
        list[individual]: Population. (cpy)
    """
    assert bounds[0] <= corner1[0] <= corner2[0] <= bounds[1], "Invalid range."
    assert bounds[0] <= corner1[1] <= corner2[1] <= bounds[1], "Invalid range."

    lstr: list[str] = []
    
    for _ in range(maxpop):
        x: float = random.uniform(corner1[0], corner2[0])   # get random point in range
        y: float = random.uniform(corner1[1], corner2[1])
        s: str = encode_2d_scaled(maxstr, (x, y), bounds)   # convert random point to bin string
        lstr.append(s)
    return toPop(objfunc, lstr, bounds)

def encode_2d_scaled(maxstr: int, point: tuple[float, float], bounds: tuple[float, float]) -> str:
    """Encode point coordinate in bound to relative binary string.

    Args:
        maxstr (int): Lengthe of strings.
        point (tuple[float, float]): Absolute point coordinate.
        bounds (tuple[float, float]): Bounding square length.

    Returns:
        str: Binary string. (cpy)
    """
    lbound: float = bounds[1] - bounds[0]
    
    # Normalize
    xnorm: float = (point[0] - bounds[0]) / lbound
    ynorm: float = (point[1] - bounds[0]) / lbound
    
    # Relative binary size
    half: int = maxstr // 2
    maxint: int = (2**half) - 1
    xbin: int = round(xnorm * maxint)
    ybin: int = round(ynorm * maxint)
    
    return format(xbin, f"0{half}b") + format(ybin, f"0{half}b")