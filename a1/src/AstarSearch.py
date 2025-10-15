from typing import Callable
from Node import Node
from Actions import Actions
import Problem
import Analytics

def AstarSearch(n: Node, h: Callable[[Node], int]) -> Node | None:
    """Using A* search algorithm to solve the problems as graph searches.

    Args:
        n (Node): The root node representing the initial state.
        h (function): The heuristic function used to estimate cost from current state to goal state.

    Returns:
        Node: The node of the goal state.
    """
    
    Analytics.newRecord(h.__name__)
    frontierQueue: list[Node] = [n]
    
    while frontierQueue:
        currNode: Node = frontierQueue.pop(0)
        
        # check if current state reached goal state
        if Problem.reachGoal(currNode.state):
            return currNode
        
        currActions: Actions = Actions(currNode.state)
        for actionName in ["U", "D", "L", "R"]:
            # find new state
            newState: list | None = currActions.result(actionName)
            if newState is None: 
                continue
            
            # compute new node data
            frontierQueue.append(Node(newState, currNode, actionName, Problem.getPathCost() + currNode.pathCost))
            Analytics.incrementRecord(h.__name__, "nodesExpanded")
        
        # sort frontier by ascending f(n), where f(n) = g(n) + h(n)
        frontierQueue.sort(key=lambda p: p.pathCost + h(p.state))
    
    return None