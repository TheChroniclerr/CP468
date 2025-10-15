import math
from typing import Literal

Type = Literal["h1", "h2", "h3"]

def h1(s: list) -> int:
    """Heuristic - estimate true cost from current state to goal state via number of misplaced tiles.

    Args:
        s (list): Current node.

    Returns:
        int: Number of misplaced tiles.
    """
    # current state must be a list, and list must have size = n*n, for n-puzzle
    assert type(s) == list and math.sqrt(len(s)).is_integer() , "Invalid heuristic."

    misplacedTiles: int = 0

    goalNum: int = 1
    for currNum in s:
        misplacedTiles += 1 if currNum != goalNum else 0
        goalNum += 1
    
    return misplacedTiles

def h2(s: list) -> int:
    """Heuristic - estimate true cost from current state to goal state via total Manhattan distance.
    Manhattan distance is the sum of the distances of the tiles from their goal positions.

    Args:
        s (list): Current node.

    Returns:
        int: Manhattan distance
    """
    assert type(s) == list and math.sqrt(len(s)).is_integer() , "Invalid heuristic."

    totalManhattanDistance: int = 0

    # the number on the tile == index of its goal position
    currPos: int = 1
    for goalPos in s:
        width: int = int(math.sqrt(len(s)))   # get the n of n-puzzle (n by n)
        diff: int = goalPos - currPos
        
        totalManhattanDistance += diff // width     # vertical displacement
        totalManhattanDistance += diff % width      # horizontal displacement
        currPos += 1
    
    return totalManhattanDistance

def h3(s: list) -> int:
    return 0

Function: dict = {
    "h1": h1,
    "h2": h2,
    "h3": h3
}