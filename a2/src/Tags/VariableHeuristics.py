import Classes.Heuristics as Heuristics
from typing import Literal, Callable

Type = Literal["DFS", "RV", "MRV", "LNC"]

Function: dict[str, Callable] = {
    "DFS": Heuristics.DFS,
    "RV": Heuristics.RV,
    "MRV": Heuristics.MRV,
    "LNC": Heuristics.LNC
}