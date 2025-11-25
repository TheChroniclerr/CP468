from typing import TypedDict

class individual(TypedDict):
    chrom: str          # The encoded string
    x: int              # The first decoded value
    y: int              # The second decoded value
    fitness: float      # The fitness score
