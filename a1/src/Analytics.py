from tabulate import tabulate

analytic: dict = {}

def newRecord(name: str, data: list | None) -> None:
    analytic[name] = {
        "nodesExpanded": 0,
        "solutionDepth": 0
    }

def incrementRecord(name: str, key: str, amount: int = 1) -> None:
    analytic[name][key] += amount

def displayTable() -> str:
    data: list = [
        [, "h1", , "h2", , "h3"],
        [, "Nodes Expanded", "Solution Depth", "Nodes Expanded", "Solution Depth", "Nodes Expanded", "Solution Depth"]
    ]
    for 
    
    