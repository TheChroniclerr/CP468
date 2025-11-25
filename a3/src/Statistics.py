from Individual import individual

def getStatistics(records: list[individual]) -> tuple[individual, individual, float, float]:
    """Calculate population statistics - max, min, avg, sum.

    Args:
        records (list[individual]): Records of population with fitness data.

    Returns:
        tuple[individual, individual, int, int]:
            Max fitness score individual, 
            min fitness score individual,
            avg fitness score of population, 
            sum of population fitness scores
    """
    fmax: individual = max(records, key=lambda ind: ind["fitness"])
    fmin: individual = min(records, key=lambda ind: ind["fitness"])
    sumfitness: float = sum(ind["fitness"] for ind in records)
    avg: float = sumfitness / len(records)
    return fmax, fmin, avg, sumfitness