import math
from typing import Literal, Callable

Type = Literal["h1", "h2", "h3"]

def h1(s: list, g: list) -> int:
    """Heuristic - estimate true cost from current state to goal state via number of misplaced tiles.

    Args:
        s (list): Current state.
        g (list): Goal state.

    Returns:
        int: Number of misplaced tiles.
    """
    # current state must be a list, and list must have size = n*n, for n-puzzle
    assert type(s) == list and math.sqrt(len(s)).is_integer() , "Invalid heuristic."

    misplacedTiles: int = 0

    for i in range(0, len(s)):
        misplacedTiles += 1 if s[i] != g[i] else 0
    
    return misplacedTiles

def h2(s: list, g: list) -> int:
    """Heuristic - estimate true cost from current state to goal state via total Manhattan distance.
    Manhattan distance is the sum of the distances of the tiles from their goal positions.

    Args:
        s (list): Current state.
        g (list): Goal state.

    Returns:
        int: total Manhattan distance
    """
    return int(_findSumOfDists(s, g, lambda currRow, currCol, goalRow, goalCol:     # Manhattan distance formula
        abs(currRow - goalRow) + abs(currCol - goalCol)
    ))

def h3(s: list, g: list) -> float:
    """Heuristic - estimate true cost from current state to goal state via total Euclidean distance.
    Euclidean distance is the distance between two points (current state & goal state in this case) in Euclidean space.

    Args:
        s (list): Current state.
        g (list): Goal state.

    Returns:
        int: Euclidean distance
    """
    return _findSumOfDists(s, g, lambda currRow, currCol, goalRow, goalCol:     # Euclidean distance formula
        math.dist((currRow, currCol), (goalRow, goalCol))
    )

def _findSumOfDists(s: list, g: list, getDist: Callable) -> int | float:
    """Auxillary function, find the sum of distances by the type of distance calculation used.

    Args:
        s (list): Current state.
        g (list): Goal state.

    Returns:
        int: Total distance.
    """
    assert type(s) == list and math.sqrt(len(s)).is_integer() , "Invalid heuristic."

    totalDistance: int = 0
    width: int = int(math.sqrt(len(s)))   # get the n of n-puzzle (n by n)
    indexMap: list = _createIndexMap(g)

    for currPos, tileNum in enumerate(s):
        if tileNum is None: continue
        goalPos: int = indexMap[tileNum]
        # find the x/y position of s and g, then calculate the Manhattan distance
        currRow, currCol = divmod(currPos, width)
        goalRow, goalCol = divmod(goalPos, width)
        totalDistance += getDist(currRow, currCol, goalRow, goalCol)
    
    return totalDistance

def _createIndexMap(s: list) -> list:
    """Auxillary function, map the tile number to its goal index.
    Let list key represent the tile number, and list value represent the goal index.

    Args:
        s (list): Goal state.

    Returns:
        list: Index map.
    """
    indexMap: list = [None] * (len(s) + 1)      # index position 0 is not used, since tile number starts on 1
    
    for goalPos, tileNumb in enumerate(s):
        indexMap[tileNumb] = goalPos            # goalPos start at 0
    
    return indexMap

Function: dict[str, Callable] = {
    "h1": h1,
    "h2": h2,
    "h3": h3
}