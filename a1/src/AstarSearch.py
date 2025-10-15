from Node import Node
from Actions import Actions
import Problem
import Heuristics
import Analytics

def AstarSearch(n: Node, h: function) -> Node | None:
    """Using A* search algorithm to solve the problems as graph searches.

    Args:
        n (Node): The root node representing the initial state.
        h (function): The heuristic function used to estimate cost from current state to goal state.

    Returns:
        Node: The node of the goal state.
    """
    Analytics.newRecord(h.__name__)
    frontierQueue: list = [n]
    while(frontierQueue and not Problem.g(frontierQueue[0].state)):         # check for goal state
        oldNode: Node = frontierQueue.pop(0)
        oldActions: Actions = Actions(oldNode.state)
        for actionName in ["U", "D", "L", "R"]:
            newS: list | None = oldActions.result(actionName)
            newP: Node = oldNode
            newA: function = actionName
            newPC: int = Problem.c() + oldNode.pathCost    # g(n)
            
            if not(newS is None):
                frontierQueue.append(Node(newS, newP, newA, newPC))
                Analytics.incrementRecord(h.__name__, "nodesExpanded")
            
        frontierQueue.sort(key=lambda p: p.pathCost + Heuristics.h1(n))     # f(n) = g(n) + h(n)
    
    if frontierQueue: return frontierQueue[0]
    return None


def g(n: Node) -> int:
    """Determine cost to reach current node n from the start node.
    In other words, the cost from initial state to current state.

    Args:
        n (Node): The node of the current expanded state.

    Returns:
        int: The total cost.
    """