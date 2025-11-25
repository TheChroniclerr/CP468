from dt.stats import stats
from dt.individual import individual

def getStats(pop: list[individual]) -> stats:
    """Calculate population statistics - max, min, avg, sum.
    Add statistics to Generation data.

    Args:
        pop (list[individual]): Records of population with fitness data.

    Returns:
        tuple[individual, individual, int, int]: (cpy)
            Max fitness score individual, 
            min fitness score individual,
            avg fitness score of population, 
            sum of population fitness scores
    """
    _sum: float = sum(ind["fitness"] for ind in pop)
    avg: float = _sum / len(pop)
    
    nstats: stats = {
        "max": max(pop, key=lambda ind: ind["fitness"]),
        "min": min(pop, key=lambda ind: ind["fitness"]),
        "sum": _sum,
        "avg": avg
    }
    return nstats