from CSP import CSP
from Node import Node
from typing import cast
from copy import deepcopy
from Problem import Problem
from Tags import ValueHeuristics, VariableHeuristics, Pruning

def Backtracking(problem: Problem) -> CSP | None:
    """Backtracking Search algorithm for CSP.
    Uses variable and value heuristics to select the next variable and value to assign.

    Args:
        csp (CSP): The CSP instance.
    
    Returns:
        CSP | None: The solved CSP instance or None if no solution found.
    """
    # TODO: inference needs X and D, while non-inference only need X. Optimize by minimizing deepcopy.    
    # the stack for DFS
    stack: list[Node] = []

    # select ordered list of unassigned variable indexes
    indexLis: list[int] = cast(list[int], problem.findVars())   # type hinting
    currIndex: int = 0      # track current index in indexLis
    
    # select orderedd list of values from variable domain
    valueLis: list[int] = problem.findVals(currIndex)
    currIndex += 1
    
    # initialize stack Nodes
    for val in reversed(valueLis):
        # Node with the same parent references the same csp since the states are the same
        node: Node = Node(problem.csp, [indexLis[0], val], None)    # no deepcopy for problem.csp - it is done in while loop
        stack.append(node)    
    
    while stack:
        currNode: Node = stack.pop()
        
        # assign a new variable, add to problem.csp
        newCSP: CSP = deepcopy(currNode.state)
        newCSP.X[currNode.action[0]] = currNode.action[1]
        problem.csp = newCSP
        
        if problem.inference:
            result = problem.infer(newCSP)
            if result is None:
                continue    # no solution possible, backtrack
            if problem.isComplete():
                # does not check for consistency because inference already did that
                return result    # solution found
            
            # find next index to assign value to
            index: int = cast(int, problem.findVars(mode=1))   # type hinting
            
            # add new Nodes to stack based on updated inference
            valueLis: list[int] = ValueHeuristics.Function[problem.valH](problem.csp, index)
        else:
            # check if assignment violate constraints
            if not problem.isConsistent(currNode.action[0]):
                continue    # no solution possible, backtrack
            if problem.isComplete():
                return newCSP    # solution found
            
            # add new Nodes to stack
            valueLis: list[int] = ValueHeuristics.Function[problem.valH](problem.csp, indexLis[currIndex])
            currIndex += 1

        # shared actions (for both inference and non-inference)
        for val in reversed(valueLis):
                node: Node = Node(problem.csp, [indexLis[0], val], None)      # does not need parent because stack enforces DFS
                stack.append(node)

    # no solution found from all possible combination of values for unassigned variables
    return None