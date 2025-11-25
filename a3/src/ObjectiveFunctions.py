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