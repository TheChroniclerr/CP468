from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Classes.CSP import CSP

class Node:
    def __init__(self, csp: CSP, action: list[int], parent: Node | None) -> None:
        """Node constructor for CSP

        Args:
            csp (CSP): The CSP state at this node. (modified in place)
            action (list[int]): The next possible action/assignment to take [unassigned index, value to assign].
            parent (Node | None): Parent node. (modified in place)
        """
        self.state = csp
        self.parent = parent
        self.action: list[int] = action     # index and variable to assign to index
