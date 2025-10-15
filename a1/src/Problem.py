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

def reachGoal(sX: any, sY: any = [1, 2, 3, 4, 5, 6, 7, 8, None]) -> bool:
    """Goal Test - Determines whether a given state is the goal state.

    Args:
        sX (any): Current state.
        sY (any): Goal state.

    Returns:
        bool: True if goal state is reached, else False.
    """
    
    if type(sX) != type(sY):
        return False
    elif type(sX) == list:
        for i, j in sX, sY:
            if i != j: return False
    else:
        if i != j: return False
    
    return True

def getPathCost(sX: any | None = None, a: function | None = None, nY: any | None = None) -> int:
    return 1