class Node:
    def __init__(self, state: any, parent: any, action: str | None, pathCost: int = 1) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.pathCost = pathCost