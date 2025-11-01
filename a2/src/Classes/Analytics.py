class Analytics:
    def __init__(self) -> None:
        """Class constructor
        """
        self.QLs = []       # Queue lengths
        self.inferenceSolved = False
        self.SLs = []       # Stack lengths
        self.backtrackingSolved = False
    
    def addQLRecord(self, record: int) -> None:
        """Record current queue length.

        Args:
            record (int): Current queue length.
        """
        self.QLs.append(record)
        return
    
    def addSLRecord(self, record: int) -> None:
        """Record current stack length.

        Args:
            record (int): Current queue length.
        """
        self.SLs.append(record)
        return
    
    def __str__(self) -> str:
        result: str = f"Solved by AC-3: {self.inferenceSolved}\n";
        result += f"Solved by Backtracking: {self.backtrackingSolved}\n"
        
        result += f"\nAC-3\n"
        for i, length in enumerate(self.QLs):
            result += f"Step {i}: Queue Length = {length}\n"
            
        result += f"\nBacktracking:\n"
        for i, length in enumerate(self.SLs):
            result += f"Step {i}: Queue Length = {length}\n"
        return result