from CSP import CSP
from a2.src.Classes.Pruning import AC_3
from Problem import Problem
from Search import Backtracking

def Solver(problem: Problem) -> CSP | None:
    """Solve the given CSP problem using backtracking search with inference.

    Args:
        problem (Problem): The Problem instance.

    Returns:
        CSP | None: The solved CSP instance or None if no solution found.
    """
    resultCSP: CSP | None = AC_3(problem.csp)
    
    if resultCSP is None:
        return None    # no solution possible after initial AC-3 pruning
    if problem.isComplete():
        # AC-3 ensures consistency, only check for completeness
        return resultCSP    # solution found after AC-3 pruning
    
    # run backtracking for remaining unassigned variables
    resultCSP: CSP | None = Backtracking(problem)
    
    if resultCSP:
        problem.csp = resultCSP
        if not problem.isSolution():
            print("There is a mistake in your code.")
    
    return resultCSP