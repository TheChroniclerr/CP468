# from Classes import Generator
import Utilities
from Classes.ClassicSudoku import ClassicSudoku
from Classes.CSP import CSP
from Classes.Problem import Problem
from Classes.Solver import Solver

if __name__ == "__main__":
    # Variables
    # AC-3 Solvables
    X_hard = [5, 3, None, None, 7, None, None, None, None,
        6, None, None, 1, 9, 5, None, None, None,
        None, 9, 8, None, None, None, None, 6, None,
        8, None, None, None, 6, None, None, None, 3,
        4, None, None, 8, None, 3, None, None, 1,
        7, None, None, None, 2, None, None, None, 6,
        None, 6, None, None, None, None, 2, 8, None,
        None, None, None, 4, 1, 9, None, None, 5,
        None, None, None, None, 8, None, None, 7, 9]
    
    X_quick = [
        None, 2, 3, 4, 5, 6, 7, 8, 9,
        4, None, 6, 7, 8, 9, 1, 2, 3,
        7, 8, None, 1, 2, 3, 4, 5, 6,
        2, 3, 4, None, 6, 7, 8, 9, 1,
        5, 6, 7, 8, None, 1, 2, 3, 4,
        8, 9, 1, 2, 3, None, 5, 6, 7,
        3, 4, 5, 6, 7, 8, None, 1, 2,
        6, 7, 8, 9, 1, 2, 3, None, 5,
        9, 1, 2, 3, 4, 5, 6, 7, None
    ]
    
    # Backtracking solvable
    X: list[int | None] = [None] * 81
    
    unprotectedCsp = ClassicSudoku(X).getCSP()  # Conver from custom list format to CSP
    csp: CSP = CSP(*unprotectedCsp)     # CSP does deepcopy
    problem: Problem = Problem(csp)
    result: CSP | None = Solver(problem)
    if isinstance(result, CSP):
        grid: list[int | None] = ClassicSudoku.toGrid(result)
        format = ClassicSudoku(grid)    # Convert from CSP back to custom list
        print(format)
        print(problem.analytics)
    # print(result)
    # print(type(result))