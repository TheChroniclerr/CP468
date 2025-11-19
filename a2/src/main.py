# from Classes import Generator
from Classes.Generator import generateGrid
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
    
    # Pure Backtracking solvable
    X_empty: list[int | None] = [None] * 81
    
    # No solution
    X_non = [
        1, None, None, None, 2, None, None, 4, None,
        None, None, 3, None, 8, None, None, None, None,
        None, 2, None, None, None, None, 1, 6, 8,
        None, 1, None, None, 5, None, None, 8, 7,
        None, None, 2, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None,
        None, 1, 8, 3, None, None, None, None, None,
        None, 2, 1, 9, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None
    ]

    # AC-3 & Backtracking solvable
    X_20 = [
        None, 6, None, None, None, None, 9, None, None,
        None, None, None, None, None, None, None, 2, None,
        None, None, None, 3, 1, 6, None, None, None,
        None, None, 6, 5, None, 3, None, 7, None,
        None, 2, None, None, None, None, None, None, None,
        None, 7, None, None, None, None, 6, 7, 1,
        None, None, None, None, 9, None, None, None, 5,
        None, None, None, None, 7, None, None, 4, None,
        None, None, None, None, None, 3, None, None, None
    ]
    
    X_30 = [
        None, 6, None, 5, 2, None, 9, None, None,
        4, None, 3, None, None, None, 7, 2, None,
        None, 2, None, 9, None, None, None, None, None,
        None, 1, 4, None, None, 2, None, None, 7,
        None, 8, None, 3, None, 1, 6, 5, None,
        None, None, 6, None, 7, None, None, 1, None,
        None, None, None, 8, None, None, None, 9, None,
        None, None, None, 2, None, None, None, None, 6,
        None, None, 9, None, 6, 5, None, None, 1
    ]
    
    X_sample2 = [ 
        8,None,None,None,None,None,None,None,None,
        None,None,3,6,None,None,None,None,None,
        None,7,None,None,9,None,2,None,None,
        None,5,None,None,None,7,None,None,None,
        None,None,None,None,4,5,7,None,None,
        None,None,None,1,None,None,None,3,None,
        None,None,1,None,None,None,None,6,8,
        None,None,8,5,None,None,None,1,None,
        None,9,None,None,None,None,4,None,None
    ]
    
    X_sample1 = [
        3,4,None,7,None,6,None,None,1,8,7,None,None,None,None,9,None,6,None,None,None,8,9,1,None,None,3,None,None,None,None,None,3,5,6,8,6,8,None,None,5,4,None,None,7,9,1,None,6,None,None,None,None,None,None,3,None,4,None,None,None,8,None,5,9,None,None,None,None,7,3,None,7,None,None,5,3,8,None,1,9
    ]

    # Generate Sudoku instance
    X: list[int | None] = generateGrid(35)
    
    unprotectedCsp = ClassicSudoku(X_sample2).getCSP()  # Conver from custom list format to CSP
    csp: CSP = CSP(*unprotectedCsp)     # CSP does deepcopy
    problem: Problem = Problem(csp, "DFS", "FV", "CP")
    result: CSP | None = Solver(problem)
    if isinstance(result, CSP):
        grid: list[int | None] = ClassicSudoku.toGrid(result)
        format = ClassicSudoku(grid)    # Convert from CSP back to custom list
        print(format)
        print(problem.analytics)
    if result is None:
        print("no solution")
    # print(result)
    # print(type(result))