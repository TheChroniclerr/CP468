# import Analytics
import Generator
from Problem import Problem
from AstarSearch import AstarSearch
from Node import Node   # type hint

# Default values
_8_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, None]   # 3x3
_15_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]   # 4x4
_24_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, None]   # 5x5

initialState: list = Generator.generateRandom(3, 70, 70)      # Generate puzzle
print(initialState)
# list of problems
problems: list = [
    Problem(initialState, _8_PUZZLE_GOAL_STATE, "h1"),
    Problem(initialState, _8_PUZZLE_GOAL_STATE, "h2"),
    Problem(initialState, _8_PUZZLE_GOAL_STATE, "h3")
]
# print
for problem in problems:
    print(problem.hTag)
    goalNode: Node = AstarSearch(problem)       # Run A* search on the problem instance
    print(goalNode)

# GOOD TEST CASE
# problem = Problem([1, 5, 4, 2, None, 3, 6, 8, 7], _8_PUZZLE_GOAL_STATE, "h3")
# print(problem.hTag)
# goalNode: Node = AstarSearch(problem)       # Run A* search on the problem instance
# print(goalNode)

# # FIXED - closed set
# # failed cases: [6, 4, 2, 1, None, 5, 7, 8, 3] 
# # [5, 4, None, 7, 6, 1, 8, 2, 3]

# # FIXED - heapq better perf (if it's way too large, then it simply takes forever to run, not a bug)
# failed cases: [5, 4, 3, 7, 6, 1, 2, 8, 13, 11, 12, 15, 14, 10, 9, None]