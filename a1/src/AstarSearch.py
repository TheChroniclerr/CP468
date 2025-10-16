import heapq
import Problem
from Node import Node
from Analytics import Analytics
from Actions import Actions     # type hint

def AstarSearch(problem: Problem) -> Node | None:
    """Using A* search algorithm to solve the problem instances as graphs.

    Args:
        problem (Problem): The problem instance.

    Returns:
        Node: The node of the goal state.
    """
    rootNode: Node = Node(problem.initialState, None, None, 0)
    frontierHeap: list[tuple[float, Node]] = [(problem.h(rootNode.state), rootNode)]    # use heapq for performance
    visited: set = set()    # hash-set to track visited nodes
    visited.add(tuple(problem.initialState))    # convert list to hashable tuple
    
    analytics: Analytics = Analytics(problem)
    while frontierHeap:
        _, currNode = heapq.heappop(frontierHeap)
        analytics.incrementNodesExpanded()
        
        # check if current state reached goal state
        if problem.reachGoal(currNode.state):
            analytics.recordSteps(len(Node.getAncestors(currNode)))
            analytics.writeCSV()
            return currNode
        
        currActions: Actions = problem.setAction(currNode.state)
        for actionName in currActions.validActions:
            # find new state
            newState: list | None = currActions.result(actionName)
            if newState is None: 
                continue
            # skip already visited node
            if tuple(newState) in visited: 
                continue
            visited.add(tuple(newState))
            # compute new node data, add to heap
            newNode: Node = Node(newState, currNode, actionName, problem.getPathCost() + currNode.pathCost)
            f_n: int = newNode.pathCost + problem.h(newState)   # f(n)
            heapq.heappush(frontierHeap, (f_n, newNode))    # sorts by first element (f_n) automatically
    
    return None