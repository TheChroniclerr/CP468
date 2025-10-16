# import Analytics
import Problem
from Node import Node
from typing import Callable
from Actions import Actions     # type hint

def AstarSearch(problem: Problem) -> Node | None:
    """Using A* search algorithm to solve the problem instances as graphs.

    Args:
        problem (Problem): The problem instance.

    Returns:
        Node: The node of the goal state.
    """
    # Analytics.newRecord(problem.h.__name__)
    # Analytics.incrementRecord()
    rootNode: Node = Node(problem.initialState, None, None, 0)
    frontierQueue: list[Node] = [rootNode]
    
    while frontierQueue:
        currNode: Node = frontierQueue.pop(0)
        
        # check if current state reached goal state
        if problem.reachGoal(currNode.state):
            return currNode
        
        currActions: Actions = problem.setAction(currNode.state)
        for actionName in currActions.validActions:
            # find new state
            newState: list | None = currActions.result(actionName)
            if newState is None: 
                continue
            
            # compute new node data
            frontierQueue.append(Node(newState, currNode, actionName, problem.getPathCost() + currNode.pathCost))
            # Analytics.incrementRecord(problem.h.__name__, "nodesExpanded")
        
        # sort frontier by ascending f(n), where f(n) = g(n) + h(n)
        frontierQueue.sort(key=lambda p: p.pathCost + problem.h(p.state))   # O(n log(n))
    
    return None