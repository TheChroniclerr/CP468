from typing import TypedDict
from dt.individual import individual

class stats(TypedDict):
    min: individual
    max: individual
    avg: float
    sum: float
