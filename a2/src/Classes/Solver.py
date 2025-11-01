from __future__ import annotations
from Classes.Pruning import AC_3
from Classes.Search import Backtracking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Classes.CSP import CSP
    from Classes.Problem import Problem

def Solver(problem: Problem) -> CSP | None:
    """Solve the given CSP problem using backtracking search with inference.

    Args:
        problem (Problem): The Problem instance.

    Returns:
        CSP | None: The solved CSP instance or None if no solution found.
    """
    resultCSP: CSP | None = AC_3(problem.csp, problem.analytics)
    
    if resultCSP is None:
        return None    # no solution possible after initial AC-3 pruning
    if problem.isComplete():
        # AC-3 ensures consistency, only check for completeness
        problem.analytics.inferenceSolved = True
        return resultCSP    # solution found after AC-3 pruning
    
    # run backtracking for remaining unassigned variables
    resultCSP: CSP | None = Backtracking(problem)
    
    if resultCSP:
        problem.analytics.backtrackingSolved = True
        problem.csp = resultCSP
        if not problem.isSolution():
            print("There is a mistake in your code.")
    
    return resultCSP