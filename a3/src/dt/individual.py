from typing import TypedDict

class individual(TypedDict):
    chrom: str          # The encoded string
    x: float            # The first decoded value
    y: float            # The second decoded value
    fitness: float      # The fitness score
