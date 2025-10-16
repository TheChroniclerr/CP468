import multiprocessing
import Generator
from Problem import Problem
from AstarSearch import AstarSearch
from typing import Callable
from Node import Node   # type hint

# Default values
TIMEOUT = 5    # seconds
GENERATIONS = 100   # amount generated

_8_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, None]   # 3x3
_15_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]   # 4x4
_24_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, None]   # 5x5

def runWithTimeout(timeout_: int, func: Callable, args=()):
    with multiprocessing.Pool(1) as pool:
        result = pool.apply_async(func, args)
        try:
            return result.get(timeout=timeout_)
        except multiprocessing.TimeoutError:
            # print("Timeout reached. Terminating process.")
            pool.terminate()  # force stop safely
            pool.join()
            return None

if __name__ == "__main__":
    # comment one of the for loop out to not generate
    # change GENERATIONS in range for different number of problem instances to solve
    
    # !there can be duplicate generations, double check CSV for 100 unique initial states.
    for i in range(0, GENERATIONS):     # 8-puzzle
        initialState: list = Generator.generateRandom(3, 70, 70)      # Generate puzzle
        print("ini: " + str(initialState))
        for heuristic in ["h1", "h2", "h3"]:
            problem: Problem = Problem(initialState, _8_PUZZLE_GOAL_STATE, heuristic)
            result: Node|None = runWithTimeout(TIMEOUT, AstarSearch, (problem,))
            if result:
                print(heuristic + ": Success")
            else:
                print(heuristic + ": Timeout")
    
    for i in range(0, GENERATIONS):     # 15-puzzle
        initialState: list = Generator.generateRandom(4, 100, 100)      # Generate puzzle
        print("ini: " + str(initialState))
        for heuristic in ["h1", "h2", "h3"]:
            problem: Problem = Problem(initialState, _15_PUZZLE_GOAL_STATE, heuristic)
            result: Node|None = runWithTimeout(TIMEOUT, AstarSearch, (problem,))
            if result:
                print(heuristic + ": Success")
            else:
                print(heuristic + ": Timeout")
    
    for i in range(0, GENERATIONS):     # 24-puzzle
        initialState: list = Generator.generateRandom(5, 70, 70)      # Generate puzzle
        print("ini: " + str(initialState))
        for heuristic in ["h1", "h2", "h3"]:
            problem: Problem = Problem(initialState, _24_PUZZLE_GOAL_STATE, heuristic)
            result: Node|None = runWithTimeout(TIMEOUT, AstarSearch, (problem,))
            if result:
                print(heuristic + ": Success")
            else:
                print(heuristic + ": Timeout")

# # SINGLE TEST CASE
# problem = Problem([1, 5, 4, 2, None, 3, 6, 8, 7], _8_PUZZLE_GOAL_STATE, "h3")
# print(problem.hTag)
# goalNode: Node = AstarSearch(problem)       # Run A* search on the problem instance
# print(goalNode)

# FIXED - closed set
# failed cases: [6, 4, 2, 1, None, 5, 7, 8, 3] 
# [5, 4, None, 7, 6, 1, 8, 2, 3]

# MILESTONE - proof of concept case, convincing me that code is not bugged for larger cases
# suceeded case: [1, 5, 4, 2, None, 3, 6, 8, 7]

# FIXED - heapq better perf (if it's way too large, then it simply takes forever to run, not a bug)
# failed cases: [5, 4, 3, 7, 6, 1, 2, 8, 13, 11, 12, 15, 14, 10, 9, None]

# MILETONE - the only 1/100 24-puzzle that failed for generateRandom(5, 70, 70)
# failed case: [1, 3, 8, 15, 5, 6, 2, 19, 14, 10, 11, 7, 4, 18, 20, 16, 12, 13, None, 9, 21, 17, 22, 23, 24]