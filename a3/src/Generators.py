import random

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