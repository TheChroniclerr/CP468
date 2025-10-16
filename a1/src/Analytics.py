import os
import csv
from Problem import Problem     # type hint

DEFAULT_DIR: str = "a1/output"

FILENAMES: dict = {
    9: "/8_Puzzle.csv",
    16: "/15_Puzzle.csv",
    25: "/24_Puzzle.csv"
}

CSV_HEADER: list = [
    "initial_state", "h1_steps", "h1_expanded", "h2_steps", "h2_expanded", "h3_steps", "h3_expanded"
]

class Analytics:
    def __init__(self, problem: Problem):
        self.initialState: str = str(problem.initialState)
        # self.filePointer  # points to location in CSV
        self.fileDir: str = DEFAULT_DIR + FILENAMES[len(problem.initialState)]
        self.data: list[dict] = self._loadExistingCSV()     # a copy of whole CSV data to modify and overwrite back to
        self.changes: dict = {      # record data to be added/changed, key - column name, value - stored data
            f"{problem.hTag}_steps": 0,
            f"{problem.hTag}_expanded": 0
        }
    
    def recordSteps(self, steps: int) -> None:
        for key in self.changes:
            if "steps" in key:
                self.changes[key] = steps

    def incrementNodesExpanded(self) -> None:
        for key in self.changes:
            if "expanded" in key:
                self.changes[key] += 1
    
    def writeCSV(self) -> None:
        # find record if already exists
        record = None
        for row in self.data:
            if row["initial_state"] == self.initialState:
                record = row
                break
        
        # create record if not exist, append to data
        if record is None:
            record = self._newRecord()
            self.data.append(record)
        
        # apply changes to data (using record) and overwrite CSV
        for columnName, newValue in self.changes.items():
            record[columnName] = newValue
        self._overwrite()
        
    def _newRecord(self) -> dict:
        record: dict = {
            "initial_state": self.initialState
        }
        for h in ["h1", "h2", "h3"]:
            record[f"{h}_steps"] = "TIMEOUT"
            record[f"{h}_expanded"] = "TIMEOUT"

        return record
    
    def _loadExistingCSV(self) -> list:
        if not os.path.exists(self.fileDir):
            with open(self.fileDir, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
                writer.writeheader()
            return []
        
        with open(self.fileDir, 'r', newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _overwrite(self) -> None:
        with open(self.fileDir, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
            writer.writeheader()
            writer.writerows(self.data)