import math
from Node import Node

def h1(n: Node) -> int:
    """Heuristic - estimate true cost from current state to goal state via number of misplaced tiles.

    Args:
        n (Node): Current node.

    Returns:
        int: Number of misplaced tiles.
    """
    # current state must be a list, and list must have size = n*n, for n-puzzle
    assert type(n.state) == list and math.sqrt(len(n.state)).is_integer() , "Invalid heuristic."

    misplacedTiles: int = 0

    goalNum: int = 1
    for currNum in n.state:
        misplacedTiles += 1 if currNum != goalNum else 0
        goalNum += 1
    
    return misplacedTiles

def h2(n: Node) -> int:
    """Heuristic - estimate true cost from current state to goal state via total Manhattan distance.
    Manhattan distance is the sum of the distances of the tiles from their goal positions.

    Args:
        n (Node): Current node.

    Returns:
        int: Manhattan distance
    """
    assert type(n.state) == list and math.sqrt(len(n.state)).is_integer() , "Invalid heuristic."

    totalManhattanDistance: int = 0

    # the number on the tile == index of its goal position
    currPos: int = 1
    for goalPos in n.state:
        width: int = int(math.sqrt(len(n.state)))   # get the n of n-puzzle (n by n)
        diff: int = goalPos - currPos
        
        totalManhattanDistance += diff // width     # vertical displacement
        totalManhattanDistance += diff % width      # horizontal displacement
        currPos += 1
    
    return totalManhattanDistance