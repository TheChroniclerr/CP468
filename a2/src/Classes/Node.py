from __future__ import annotations
from CSP import CSP
from copy import deepcopy      # TODO: figure out why is leads to an error below

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
        # self.pathCost = pathCost    # not optimization problem
    
    # def setXtoAction(self) -> None:
    #     """Set all predefined variables to action.
    #     Used for initial node in AC-3 algorithm to define initial inference checks.
    #     """
    #     for var, val in self.X.items():
    #         if val is not None:
    #             self.action.append(var)
    #     return
    
    # def trackAssignment(self, var: int) -> None:
    #     """Tracks a new consistent assignment after another domain shrinks to 1 via AC-3.

    #     Args:
    #         var (int): Variable index
    #     """
    #     self.action.append(var)
    #     return
    
    # def __deepcopy__(self) -> Node:
    #     """Deepcopy current Node instance.
    #     This does not copy self.action.

    #     Returns:
    #         Node: Current node instance.
    #     """
    #     return Node(deepcopy(self.X), deepcopy(self.D), self.parent)
    
    # # def __str__(self) -> str:
    # #     return f"Node(state={self.state}, action={self.action}, pathCost={self.pathCost})"
    
    # def getAncestors(self) -> list:
    #     """Retrieves all direct ancestors of current node.

    #     Returns:
    #         list: A list of direct ancestors ordered from ancestors to descendants.
    #     """
    #     ancestors: list = [self]
    #     while ancestors[-1].parent:
    #         ancestors.append(ancestors[-1].parent)
        
    #     return ancestors[::-1]  # slice notation - reverse list