import Generator
import Problem
from Node import Node
from AstarSearch import AstarSearch
import Heuristics
import Analytics

initialStateCpy: list = Problem.setInitialState(Generator.generateRandom(3, 7, 7))      # Generate puzzle
rootNode: Node = Node(initialStateCpy, None, None, 0)                                   # Create root node for graph search
goalNode: Node = AstarSearch(rootNode, Heuristics.h1)                                   # Run A* search on node
print(goalNode)                                                                         # print result
Analytics.displayTable()

