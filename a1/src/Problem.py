import math
import copy

from Node import Node

initialState: list = []
def setInitialState(s: list) -> list:
    initialState = s
    return copy.deepcopy(s)

def up(s: list) -> list | None:
    """Move the tile below the blank tile upwards.

    Args:
        s (list): Current state of the n-puzzle.

    Returns:
        list | None: Return list if move successful, else None.
    """
    assert type(s) == list and math.sqrt(len(s)).is_integer() , "Incorrect size of puzzle."
    # Variables
    s: list = copy.deepcopy(s)              # do not change the argument list
    width: int = int(math.sqrt(len(s)))     # get the n of n-puzzle (n by n)
    blankPos: int = _findBlankTileIndex(s)  # index of blank tile
    srcPos: int = blankPos + width          # index of tile to move to blank tile
    assert blankPos != -1, "Puzzle has no blank tile."
    # Process
    # !puzzle index starts at 1 whereas python list index starts at 0
    if 1 <= srcPos <= len(s) + 1:           # does cross puzzle top/bottom boundary
        s[blankPos - 1] = s[srcPos - 1]     # move number from source tile to blank tile
        s[srcPos - 1] = None                # clear the original source tile number
        return s
    
    return None

def down(s: list) -> list | None:
    """Move the tile above the blank tile downward.

    Args:
        s (list): Current state of the n-puzzle.

    Returns:
        list | None: Return list if move successful, else None.
    """
    assert type(s) == list and math.sqrt(len(s)).is_integer() , "Incorrect size of puzzle."
    # Variables
    s: list = copy.deepcopy(s)
    width: int = int(math.sqrt(len(s)))
    blankPos: int = _findBlankTileIndex(s)
    srcPos: int = blankPos - width          # index of tile to move to blank tile
    assert blankPos != -1, "Puzzle has no blank tile."
    # Process
    if 1 <= srcPos <= len(s) + 1:
        s[blankPos - 1] = s[srcPos - 1]
        s[srcPos - 1] = None
        return s
    
    return None

def right(s: list) -> list | None:
    """Move the tile left of the blank tile rightward.

    Args:
        s (list): Current state of the n-puzzle.

    Returns:
        list | None: Return list if move successful, else None.
    """
    assert type(s) == list and math.sqrt(len(s)).is_integer() , "Incorrect size of puzzle."
    # Variables
    s: list = copy.deepcopy(s)
    width: int = int(math.sqrt(len(s)))
    blankPos: int = _findBlankTileIndex(s)
    srcPos: int = blankPos - 1              # index of tile to move to blank tile
    assert blankPos != -1, "Puzzle has no blank tile."
    # Process
    if (1 <= srcPos <= len(s) + 1           # case 1: moving from out of bound
    or not(blankPos % width == 1)):         # case 2: moving from left bound
        s[blankPos - 1] = s[srcPos - 1]
        s[srcPos - 1] = None
        return s
    
    return None
    
def left(s: list) -> list | None:
    """Move the tile left of the blank tile rightward.

    Args:
        s (list): Current state of the n-puzzle.

    Returns:
        list | None: Return list if move successful, else None.
    """
    assert type(s) == list and math.sqrt(len(s)).is_integer() , "Incorrect size of puzzle."
    # Variables
    s: list = copy.deepcopy(s)
    width: int = int(math.sqrt(len(s)))
    blankPos: int = _findBlankTileIndex(s)
    srcPos: int = blankPos + 1              # index of tile to move to blank tile
    assert blankPos != -1, "Puzzle has no blank tile."
    # Process
    if (1 <= srcPos <= len(s) + 1           # case 1: moving from out of bound
    or not(blankPos % width == 0)):         # case 2: moving from right bound
        s[blankPos - 1] = s[srcPos - 1]
        s[srcPos - 1] = None
        return s
    
    return None
    
def _findBlankTileIndex(s: list) -> int:
    i: int = 1
    
    for tile in s:
        if tile == None or tile == 0:
            return i
        i += 1

    return -1

actions: dict = {
    "U": up,
    "D": down,
    "L": left,
    "R": right
}

# def s():
#     return actions

# def result(n: Node, a) -> Node:
#     return

def g(sX: any, sY: any = [1, 2, 3, 4, 5, 6, 7, 8, None]) -> bool:
    """Goal Test - Determines whether a given state is a goal state.

    Args:
        sX (any): Current state.
        sY (any): Goal state.

    Returns:
        bool: True if goal state is reached, else False.
    """
    
    if type(sX) != type(sY):
        return False
    elif type(sX) == list:
        for i, j in sX, sY:
            if i != j: return False
    else:
        if i != j: return False
    
    return True

def c(sX: any | None = None, a: function | None = None, nY: any | None = None) -> int:
    return 1