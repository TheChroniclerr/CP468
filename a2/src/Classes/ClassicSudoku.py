from __future__ import annotations
from typing import TYPE_CHECKING, cast
from Utilities import alldiff
if TYPE_CHECKING:
    from Classes.CSP import CSP

WIDTH = 9
SIZE = 81
DEFAULT_CONSTRAINTS = [
    # Rows
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22, 23, 24, 25, 26],
    [27, 28, 29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42, 43, 44],
    [45, 46, 47, 48, 49, 50, 51, 52, 53],
    [54, 55, 56, 57, 58, 59, 60, 61, 62],
    [63, 64, 65, 66, 67, 68, 69, 70, 71],
    [72, 73, 74, 75, 76, 77, 78, 79, 80],
    # Columns
    [0, 9, 18, 27, 36, 45, 54, 63, 72],
    [1, 10, 19, 28, 37, 46, 55, 64, 73],
    [2, 11, 20, 29, 38, 47, 56, 65, 74],
    [3, 12, 21, 30, 39, 48, 57, 66, 75],
    [4, 13, 22, 31, 40, 49, 58, 67, 76],
    [5, 14, 23, 32, 41, 50, 59, 68, 77],
    [6, 15, 24, 33, 42, 51, 60, 69, 78],
    [7, 16, 25, 34, 43, 52, 61, 70, 79],
    [8, 17, 26, 35, 44, 53, 62, 71, 80],
    # Boxes
    [0, 1, 2, 9, 10, 11, 18, 19, 20],
    [3, 4, 5, 12, 13, 14, 21, 22, 23],
    [6, 7, 8, 15, 16, 17, 24, 25, 26],
    [27, 28, 29, 36, 37, 38, 45, 46, 47],
    [30, 31, 32, 39, 40, 41, 48, 49, 50],
    [33, 34, 35, 42, 43, 44, 51, 52, 53],
    [54, 55, 56, 63, 64, 65, 72, 73, 74],
    [57, 58, 59, 66, 67, 68, 75, 76, 77],
    [60, 61, 62, 69, 70, 71, 78, 79, 80]
]


class ClassicSudoku:
    def __init__(self, grid: list[int | None]) -> None:
        self._isValid(grid)
        
        self.grid = grid 
        self.X = self._getVariables()
        self.D = self._getDomains()
        self.C = self._getConstraints()

    def _isValid(self, grid: list[int | None]) -> None:
        """Check whether input grid is valid.
        Errors if not valid.

        Args:
            grid (list[int | None]): The grid.
        """
        assert(len(grid) == SIZE)
        for Xi in grid:
            assert(Xi is None or 1 <= Xi <= 9)
        return
    
    def _getVariables(self) -> dict[int, int | None]:
        """Generate variable dictionary from grid.

        Returns:
            dict[int, int | None]: Variable dictionary
        """
        return {i: self.grid[i] for i in range(SIZE)}
    
    def _getDomains(self) -> dict[int, list[int]]:
        """Generate domain dictionary from grid.
        If a variable is pre-defined, make its domain equivalent to that variable.

        Returns:
            dict[int, list[int]]: Domain dictionary
        """
        return {
            # cast to satisfy type checker, we know self.grid[i] is not None in else case
            i: list(range(1, 10)) if self.grid[i] is None else [cast(int, self.grid[i])]
            for i in range(SIZE)
        }
    
    def _getConstraints(self) -> dict[int, list[int]]:
        """Generate constraint dictionary from grid.

        Returns:
            dict[int, list[int]]: Constraint dictionary
        """
        C: dict[int, list[int]] = {i: [] for i in range(SIZE)}
        for constraint in DEFAULT_CONSTRAINTS:
            alldiff(constraint, C)
        return C

    def getCSP(self) -> tuple[
        dict[int, int | None], dict[int, list[int]], dict[int, list[int]]
    ]:
        """Generate CSP representation of the Sudoku puzzle.
        Returns an unprotected copy of all values. 

        Returns:
            tuple[dict[int, list[int]], dict[int, list[int]]]: Variables, domains and constraints. (unprotected references)
        """
        return self.X, self.D, self.C
    
    
    # TODO: display() method
    def __str__(self) -> str:
        """String representation of the Sudoku puzzle.
        Sample output:
        5 3 _ | _ 7 _ | _ _ _ 
        6 _ _ | 1 9 5 | _ _ _ 
        _ 9 8 | _ _ _ | _ 6 _ 
        ------+-------+------
        8 _ _ | _ 6 _ | _ _ 3 
        4 _ _ | 8 _ 3 | _ _ 1 
        7 _ _ | _ 2 _ | _ _ 6 
        ------+-------+------
        _ 6 _ | _ _ _ | 2 8 _ 
        _ _ _ | 4 1 9 | _ _ 5 
        _ _ _ | _ 8 _ | _ 7 9 

        Returns:
            str: String representation
        """
        WIDTH = 9
        result = ""
        for i in range(WIDTH):
            for j in range(WIDTH):
                val = self.grid[i * WIDTH + j]
                if val is None:
                    result += "_ "
                else:
                    result += str(val) + " "
                if j in [2, 5]:
                    result += "| "
            result += "\n"
            if i in [2, 5]:
                result += "------+-------+------\n"
        return result
    
    def toGrid(self, csp: CSP) -> list[int | None]:
        """Takes a CSP instance, convert to formmated list grid.

        Args:
            csp (CSP): The CSP instance.

        Returns:
            list[int | None]: The grid.
        """
        return [csp.X[i] for i in range(SIZE)]
    
    def toIndex(self, x: int, y: int) -> int:
        """Convert Sudoku coordinate to index.
        Index starts from 0 at top left to
        80 to bottom right

        Args:
            x (int): _description_
            y (int): _description_

        Returns:
            int: _description_
        """
        return (9 - y) * 9 + (x - 1)

    def toCoordinate(self, index: int) -> tuple[int, int]:
        """Convert Sudoku index to coordinate.
        Coordinate starts from (1, 1) at bottom left to
        (9, 9) at top right

        Args:
            index (int): Sudoku index

        Returns:
            tuple[int, int]: Sudoku coordinate
        """
        x = (index % 9) + 1
        y = 9 - (index // 9)
        return (x, y)