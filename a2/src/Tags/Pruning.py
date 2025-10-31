from typing import Literal, Callable
import Classes.Pruning as Pruning

Type = Literal["FC", "CP"]

Function: dict[str, Callable] = {
    "FC": Pruning.ForwardChecking,
    "CP": Pruning.ConstraintPropogation
}