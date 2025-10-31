from __future__ import annotations
import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Classes.CSP import CSP
    

def _getAllUnassigned(csp: CSP) -> list[int]:
    """Get a list of all unassigned variable indexes.

    Args:
        csp (CSP): The CSP instance.

    Returns:
        list[int]: All unassigned variables.
    """
    return [i for i, Xi in csp.X.items() if Xi is None]

# --- Variable Heuristics ---
# include 2 modes for better time complexity in Backtracking with inference

def DFS(csp: CSP, mode: int = 0) -> list[int] | int:
    """Depth First Search. No heuristic.
    Order of assignment by the order whcih it is found.

    Args:
        csp (CSP): The CSP instance.
        mode (int): Determines return type.

    Returns:
        list[int] | int: Returns based on mode.
            0: return list of unassigned variable indexes.
            1: return single unassigned variable index (first found).
                Used by Backtracking search with inference.
    """
    if mode == 1:
        return next(i for i, Xi in csp.X.items() if Xi is None)
    return _getAllUnassigned(csp)

def RV(csp: CSP, mode: int = 0) -> list[int] | int:
    """Random Variable. No heuristic.
    Order of assignment is random.

    Args:
        csp (CSP): The CSP instance.
        mode (int): Determines return type.

    Returns:
        list[int] | int: Returns based on mode.
            0: return list of unassigned variable indexes.
            1: return single unassigned variable index (randomly selected).
                Used by Backtracking search with inference.
    """
    lis = _getAllUnassigned(csp)
    if mode == 1:
        return random.choice(lis)
    random.shuffle(lis)
    return lis

def MRV(csp: CSP, mode: int = 0) -> list[int] | int:
    """Minimum Remaining Values heuristic.
    Order of assignment by domain size ascending.
    MRV only orders by domain size of local/current state,
    for global/absolute ordering use along with inference.

    Args:
        csp (CSP): The CSP instance.
        mode (int): Determines return type.

    Returns:
        list[int] | int: Returns based on mode.
            0: return list of unassigned variable indexes.
            1: return single unassigned variable index (smallest domain size).
                Used by Backtracking search with inference.
    """
    lis = _getAllUnassigned(csp)
    if mode == 1:
        return min(lis, key=lambda i: len(csp.D[i]))    # O(n)
    return sorted(lis, key=lambda i: len(csp.D[i]))     # O(n log n)

def LNC(csp: CSP, mode: int = 0) -> list[int] | int:
    """Largest Number of Constraints heuristic.
    Order of assignment by number of binary constraints descending.
    Does not apply for Classic Sudoku as all variables have the same number of constraints.

    Args:
        csp (CSP): The CSP instance.
        mode (int): Determines return type.

    Returns:
        list[int] | int: Returns based on mode.
            0: return list of unassigned variable indexes.
            1: return single unassigned variable index (most constraints).
                Used by Backtracking search with inference.
    """
    lis = _getAllUnassigned(csp)
    if mode == 1:
        return max(lis, key=lambda i: len(csp.C[i]))    # O(n)
    return sorted(lis, key=lambda i: -len(csp.C[i]))    # O(n log n)

# --- Value Heuristics ---

def FV(csp: CSP, i: int) -> list[int]:
    """First Value. No heuristic.
    Order of value assignment by the order which it is found.

    Args:
        csp (CSP): The CSP instance.
        i (int): Selected variable index.

    Returns:
        list[int]: Order to expand values in the current domain.
    """
    return csp.D[i]

def LCV(csp: CSP, i: int) -> list[int]:
    """Least Constraining Value heuristic.
    Order of value assignment by least constraining to most constraining.
    "Constraining" defined by amount of values from neighboring domains the current value would rule out.

    Args:
        csp (CSP): The CSP instance.
        i (int): Selected variable index.

    Returns:
        list[int]: Order to expand values in the current domain.
    """
    def countConstraints(Xj: int) -> int:
        j: int = i
        count: int = 0
        for neighborIndex in csp.C[j]:
            if Xj in csp.D[neighborIndex]:
                count += 1
        return count

    return sorted(csp.D[i], key=lambda Xj: countConstraints(Xj))