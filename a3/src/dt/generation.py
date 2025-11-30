from typing import TypedDict
from dt.stats import stats
from dt.individual import individual

class generation(TypedDict):
    number: int
    population: list[individual]
    statistics: stats
