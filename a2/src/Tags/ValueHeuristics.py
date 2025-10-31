from typing import Literal, Callable
import Classes.Heuristics as Heuristics

Type = Literal["FV", "LCV"]

Function: dict[str, Callable] = {
    "FV": Heuristics.FV,
    "LCV": Heuristics.LCV
}