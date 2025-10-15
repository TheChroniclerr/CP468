import Heuristics
from Actions import Actions
from typing import Callable

class Problem:
    def __init__(self, initialState: list, goalState: list, heuristic: Heuristics.Type):
        self.initialState = initialState
        self.goalState = goalState
        self.h = heuristic

def h(self, s: list) -> int:    # rounding error?
    """Gate function that forces Heuristics function to be called in Problem instance.
    Find the heuristic value for the current state and pre-defined goal state.

    Args:
        s (list): Current state.

    Returns:
        int: estimated cost from current state to goal state.
    """
    return Heuristics.Function[self.h](s, self.goalState)

def setAction(self, s: list) -> Actions:
    """Gate function that forces Actions instantiation from Problem instance.
    Create an Actions instance for current state.

    Args:
        s (list): Current state.

    Returns:
        Actions: Actions instance.
    """
    return Actions(s)

def reachGoal(self, s: list) -> bool:
    """Goal Test - Determines whether a given state is the goal state.

    Args:
        s (list): Current state.

    Returns:
        bool: True if goal state is reached, else False.
    """
    return s == self.goalState

def getPathCost(sX: list = None, a: function | None = None, nY: list = None) -> int:
    """Path Cost - Assigns a numeric cost to each path (action) from previous to current state.
    For this specific problem, the action cost is always 1.

    Args:
        sX (list, optional): Initial state. Defaults to None.
        a (function | None, optional): Action function. Defaults to None.
        nY (list, optional): Final state. Defaults to None.

    Returns:
        int: 1
    """
    return 1