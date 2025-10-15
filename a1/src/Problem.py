from Node import Node
import copy

initialState: list = []
def setInitialState(s: list) -> list:
    initialState = s
    return copy.deepcopy(s)

def getSuccessors(n: Node) -> list:
    """Successor Function - Retrieves all current node's direct successors.

    Args:
        n (Node): Current node.

    Returns:
        list: A list of successors ordered from ancestor to descendant.
    """
    successors: list = [n]
    
    currNode: Node = n
    while(currNode.parent):
        successors.insert(0, currNode.parent)
        currNode = currNode.parent

    return successors

def reachGoal(sX: list, sY: list = [1, 2, 3, 4, 5, 6, 7, 8, None]) -> bool:
    """Goal Test - Determines whether a given state is the goal state.

    Args:
        sX (list): Current state.
        sY (list, optional): Goal state. Defaults to [1, 2, 3, 4, 5, 6, 7, 8, None].

    Returns:
        bool: True if goal state is reached, else False.
    """
    return sX == sY

def getPathCost(sX: list = None, a: function | None = None, nY: list = None) -> int:
    """Path Cost - Assigns a numeric cost to each path (action) from previous to current state.
    For this specific problem, the action cost is always 1.

    Args:
        sX (list, optional): Initial state. Defaults to None.
        a (function | None, optional): Action function. Defaults to None.
        nY (list, optional): Final state. Defaults to None.

    Returns:
        int: 1
    """
    return 1