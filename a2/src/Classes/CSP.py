from __future__ import annotations
from copy import deepcopy

class CSP:
    """The state of a CSP problem including X, D, C.
    Deepcopy arguments upon instantiation.
    """
    def __init__(
        self, variables: dict[int, int | None],
        domains: dict[int, list[int]],
        constraints: dict[int, list[int]]
    ) -> None:
        """Class constructor.

        Args:
            initialState (list): The starting state. (deepcopy)
            goalState (list): The final state to reach. (deepcopy)
            heuristic (Heuristics.Type): The type of heuristic used to approximate cost. (deepcopy)
        """
        self.X = deepcopy(variables)
        self.D = deepcopy(domains)
        self.C = deepcopy(constraints)
        
    def __deepcopy__(self) -> CSP:
        """Deepcopy current CSP instance.

        Returns:
            CSP: Current CSP instance.
        """
        return CSP(deepcopy(self.X), deepcopy(self.D), deepcopy(self.C))