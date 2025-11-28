import numpy as np

def Slope(x: float, y: float) -> float:
    """Slope for optimization problems.
    Objective function with a simple slope that
    pushes points in one direction.

    Args:
        x (float): Variable x.
        y (float): Variable y.

    Returns:
        float: Objective value (i.e. fitness score).
    """
    return x + y

def DeJongSphere(x: float, y: float) -> float:
    """De Jong function for optimization problems.
    Objective function with single-objective.

    Args:
        x (float): Variable x.
        y (float): Variable y.

    Returns:
        float: Objective value (i.e. fitness score).
    """
    return x**2 + y**2

def RosenbrockValley(x: float, y: float) -> float:
    """Rosenbrock's Valley for optimization problems.
    Objective function with single-objective.

    Args:
        x (float): Variable x.
        y (float): Variable y.

    Returns:
        float: Objective value (i.e. fitness score).
    """
    a: float = 1
    b: float = 1
    return (a - x)**2 + b * (y - x**2)**2

def HimmelblauFunction(x: float, y: float) -> float:
    """Himmelblau's Function for optimization problems.
    Objective function with multi-objectives.

    Args:
        x (float): Variable x.
        y (float): Variable y.

    Returns:
        float: Objective value (i.e. fitness score).
    """
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2