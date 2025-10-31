from __future__ import annotations
from Tags import ValueHeuristics, VariableHeuristics, Pruning
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Classes.CSP import CSP

class Problem:
    def __init__(
        self, 
        csp: CSP,
        varHeuristic: VariableHeuristics.Type = "DFS",
        valHeuristic: ValueHeuristics.Type = "FV",
        inference: Pruning.Type | None = None
    ) -> None:
        """Class constructor.

        Args:
            csp (CSP): The CSP instance. (modified in place)
            varHeuristic (VariableHeuristics.Type, optional): Variable heuristic to use. Defaults to "DFS".
            valHeuristic (ValueHeuristics.Type, optional): Value heuristic to use. Defaults to "FV".
            inference (Pruning.Type | None, optional): Inference method to use. Defaults to None.
        """
        self.csp = csp
        # search heuristics/ strategies
        self.varH = varHeuristic
        self.valH = valHeuristic
        self.inference = inference
        # analysis
        self.records: list[CSP] = []    # record of states generated per iteration
        
    # def createRecord(self) -> None:
    #     """Create a record of the current CSP state.
    #     Used for analytics.
    #     """
    #     self.records.append(Node(self.X, self.D, None))
    #     return

    def findVars(self, mode: int = 0) -> list[int] | int:
        """Gate function that forces Heuristics function to be called in Problem instance.
        Find the variable heuristic index for the current csp.
        
        Args:
            mode (int): Determines return type.

        Returns:
            list[int] | int: List of unassigned variable indexes ordererd by heuristic or
                single unassigned variable index if using inference.
        """
        if mode == 1:
            return VariableHeuristics.Function[self.varH](self.csp, mode=1)
        return VariableHeuristics.Function[self.varH](self.csp)
    
    def findVals(self, i: int) -> list[int]:
        """Gate function that forces Heuristics function to be called in Problem instance.
        Find the value heuristic list for a given variable index.

        Args:
            i (int): The variable index to find values for.
        
        Returns:
            list[int]: List of values from the variable's domain ordered by heuristic.
        """
        return ValueHeuristics.Function[self.valH](self.csp, i)
    
    def infer(self, csp: CSP) -> CSP | None:
        """Gate function that forces Pruning function to be called in Problem instance.
        Perform inference on the given CSP instance.

        Args:
            csp (CSP): The CSP instance. (modified in place)
        
        Returns:
            CSP | None: The pruned CSP instance or None if no solution possible.
        """
        if self.inference is None:
            return csp    # no inference to perform
        
        return Pruning.Function[self.inference](csp)

    def isConsistent(self, j: int) -> bool:
        """Consistency Check - Determines whether the current assignment is consistent with the constraints.
        Check for consistent partial assignment.

        Args:
            j (int): The variable index that was most recently assigned.

        Returns:
            bool: True if the assignment is consistent, else False.
        """
        Xj: int | None = self.csp.X[j]
        for i in self.csp.C[j]:
            Xi = self.csp.X[i]
            if Xi is not None and Xi == Xj:
                return False
        return True
    
    def isComplete(self) -> bool:
        """Completeness Check - Determines whether all variables have been assigned.
        Check for complete assignment.

        Returns:
            bool: True if all variables are assigned, else False.
        """
        return all(Xi is not None for Xi in self.csp.X.values())

    def isSolution(self) -> bool:
        """Goal Test - Determines whether a complete consistent assignment has been reached.
        Check for consistent complete assignment.

        Returns:
            bool: True if solution found, else False.
                False does not distinguish between incomplete or inconsistent assignments.
        """
        return (
            self.isComplete() and
            all(self.isConsistent(i) for i in range(0, len(self.csp.X)))
        )