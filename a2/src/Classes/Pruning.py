from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Analytics import Analytics
    from Classes.CSP import CSP

def AC_3(csp: CSP, analytics: Analytics) -> CSP | None:
    """Using AC-3 algorithm to prune search space for CSP via inference.
    Does not guarantee solution, requires backtracking search afterwards.

    Args:
        csp (CSP): The CSP instance. (modified in place)

    Returns:
        CSP | None: The pruned CSP instance or None if no solution possible.
    """
    # TODO: use deque for performance?
    queue: list[int] = []    # a list of indexes to check for inference
    # initialize queue with all pre-defined variables
    for i, Xi in csp.X.items():
        if Xi is not None:
            queue.append(i)
    analytics.addQLRecord(len(queue))
    
    while queue:
        newAssigned: list[int] | None = ForwardChecking(csp, queue.pop(0))
        if newAssigned is None:
            return None    # no solution possible
        queue.extend(newAssigned)
        analytics.addQLRecord(len(queue))
    
    return csp

# --- MAC ---

# Constraint Propogation also runs AC-3 except it is called after initial pruning during Backtracking search stage
def ConstraintPropogation(csp: CSP, j: int) -> CSP | None:
    """Using AC-3 algorithm starting from a given variable index.
    Does not guarantee solution, requires backtracking search afterwards.

    Args:
        csp (CSP): The CSP instance. (modified in place)
        j (int): The starting variable index.

    Returns:
        CSP | None: The pruned CSP instance or None if no solution possible.
    """
    # TODO: use deque for performance?
    queue: list[int] = [j]
    
    while queue:
        newAssigned: list[int] | None = ForwardChecking(csp, queue.pop(0))
        if newAssigned is None:
            return None    # no solution possible
        queue.extend(newAssigned)
        # TODO: track each iteration/cycle for analytics
    
    return csp
    
def ForwardChecking(csp: CSP, j: int) -> list[int] | None:
    """Perform forward checking after assigning a value to a variable.
    Remove inconsistent values from the domains of neighboring variables to maintain AC.

    Args:
        csp (CSP): The CSP instance. (modified in place)
        j (int): The variable index that has been assigned a value.

    Returns:
        list[int] | None: List of newly assigned variables or None if no solution possible.
    """
    newAssigned: list[int] = []

    Xj = csp.X[j]      # assigned value at index j
    for i in csp.C[j]:      # all neighboring indexes
        if Xj in csp.D[i]:      # if neighbor's domain contains assigned value
            csp.D[i].remove(Xj)
            if len(csp.D[i]) == 0:
                return None   # no solution possible
            if len(csp.D[i]) == 1 and csp.X[i] is None:
                csp.X[i] = csp.D[i][0]    # assign the only domain to variable
                newAssigned.append(i)   # track new index to run AC-3 on
    
    return newAssigned