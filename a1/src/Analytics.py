class Analytics:
    def __init__(self) -> None:
        self.nodesExpanded = 0
        self.solutionDepth = 0
    
    def recordExpansion(self) -> None:
        self.nodesExpanded += 1
    
    def recordDepth(self) -> None:
        self.solutionDepth += 1