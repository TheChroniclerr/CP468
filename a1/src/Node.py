class Node:
    def __init__(self, state: any, parent: any, action: str | None, pathCost: int = 1) -> None:
        """Node constructor

        Args:
            state (any): Current state.
            parent (any): Parent node.
            action (str | None): Action parent node took to reach current state, None for root node.
            pathCost (int, optional): g(n) - the cost from initial state to current state. Defaults to 1.
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.pathCost = pathCost    # g(n)
    
    def __str__(self) -> str:
        return f"Node(state={self.state}, action={self.action}, pathCost={self.pathCost})"
    
    def getAncestors(self) -> list:
        """Retrieves all direct ancestors of current node.

        Returns:
            list: A list of direct ancestors ordered from ancestors to descendants.
        """
        ancestors: list = [self]
        while ancestors[-1].parent:
            ancestors.append(ancestors[-1].parent)
        
        return ancestors[::-1]  # slice notation - reverse list