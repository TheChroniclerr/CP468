import math
from Node import Node

"""
Estimate true cost from current state to goal state via number of misplaced tiles.
"""
def h1(n: Node) -> int:
    # current state must be a list, and list must have size = n*n, for n-puzzle
    assert type(n.state) == list and math.sqrt(len(n.state)).is_integer() , "Heuristic does not apply."
    # Variables
    misplacedTiles: int = 0
    # Process
    goalNum: int = 1
    for currNum in n.state:
        misplacedTiles += 1 if currNum != goalNum else 0
        goalNum += 1
    
    return misplacedTiles

"""
Estimate true cost from current state to goal state via total Manhattan distance.
Manhattan distance is the sum of the distances of the tiles from their goal positions.
"""
def h2(n: Node) -> int:
    assert type(n.state) == list and math.sqrt(len(n.state)).is_integer() , "Heuristic does not apply."
    # Variables
    totalManhattanDistance: int = 0
    # Process
    currPos: int = 1
    # the number on the tile == index of its goal position
    for goalPos in n.state:
        width: int = int(math.sqrt(len(n.state)))   # get the n of n-puzzle (n by n)
        diff: int = goalPos - currPos
        
        totalManhattanDistance += diff // width     # vertical displacement
        totalManhattanDistance += diff % width      # horizontal displacement
        currPos += 1
    
    return totalManhattanDistance