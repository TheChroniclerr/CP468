from typing import TypedDict

class individual(TypedDict):
    chrom: str      # The encoded string
    x: int          # The decoded value the string represents
    fitness: int    # The fitness score
