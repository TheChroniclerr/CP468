from __future__ import annotations
from copy import deepcopy

class CSP:
    """The state of a CSP problem including X, D, C.
    Deepcopy arguments upon instantiation.
    """
    def __init__(
        self,
        variables: dict[int, int | None],
        domains: dict[int, list[int]],
        constraints: dict[int, list[int]]
    ) -> None:
        """Class constructor

        Args:
            variables (dict[int, int | None]): Mapping from variable index to value.
            domains (dict[int, list[int]]): Mapping from variable index to possible values.
            constraints (dict[int, list[int]]): Constraint graph as adjacency lists.
        """
        self.X = deepcopy(variables)
        self.D = deepcopy(domains)
        self.C = deepcopy(constraints)
        
    def __deepcopy__(self, memo=None) -> CSP:
        """Deepcopy current CSP instance.

        Returns:
            CSP: Current CSP instance.
        """
        return CSP(deepcopy(self.X), deepcopy(self.D), deepcopy(self.C))
    
    def __repr__(self) -> str:
        return f"CSP(X={self.X}, D={{...}}, C={{...}})"