# import Analytics
import Generator
from Problem import Problem
from AstarSearch import AstarSearch
from Node import Node   # type hint

# Default values
_8_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, None]   # 3x3
_15_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]   # 4x4
_24_PUZZLE_GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, None]   # 5x5

# initialState: list = Generator.generateRandom(3, 7, 7)      # Generate puzzle
initialState = [1, 3, 8, 15, 5, 6, 2, 19, 14, 10, 11, 7, 4, 18, 20, 16, 12, 13, None, 9, 21, 17, 22, 23, 24]
print(initialState)
# list of problems
problems: list = [
    Problem(initialState, _24_PUZZLE_GOAL_STATE, "h1"),
    Problem(initialState, _24_PUZZLE_GOAL_STATE, "h2"),
    Problem(initialState, _24_PUZZLE_GOAL_STATE, "h3")
]
# print
result = []
for problem in problems:
    # print(problem.hTag)
    result.append(AstarSearch(problem))       # Run A* search on the problem instance
    # print(goalNode)

for item in result:
    print(item)
