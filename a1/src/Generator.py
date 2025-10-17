import random

blank = None

def isSolvable(state, n):
    """Determines whether a given n x n puzzle can be solved.
    
    Args:
        state (list): Represents contents of the puzzle. One space will be blank.
        n (int): Represent an n x n puzzle.
    
    Returns:
        bool: True if solvable, false otherwise.
    """
    a = [x for x in state if x != blank]
    inversions = 0

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                inversions += 1

    if n % 2 == 1:
        return inversions % 2 == 0

    else:
        blank_i = state.index(blank)
        blank_distance_top = blank_i // n - 1
        blank_distance_bottom = n - blank_distance_top
        return (inversions + blank_distance_bottom) % 2 == 0


def allMoves(state, n):
    """Contains all possible movements for puzzle pieces. The pieces can be shifted up, down, left and right.
    
    Args:
        state (list): Represents contents of the puzzle. One space will be blank.
        n (int): Represent an n x n puzzle.
    
    Returns:
        list: List of moves made.
    """
    blank_i = state.index(None)
    r, c = divmod(blank_i, n)
    moves = []

    if r > 0:
        moves.append(-n)  # up
    if r < n - 1:
        moves.append(n)  # down
    if c > 0:
        moves.append(-1)  # left
    if c < n - 1:
        moves.append(1)  # right
    
    return moves


def doMove(state, move):
    """Executes a move and updates the state of the puzzle.
    
    Args:
        state (list): Represents contents of the puzzle. One space will be blank.
        move (int): Move to perform on puzzle.
    
    Returns:
        list: List of moves made.
    """
    new_state = state.copy()
    blank_i = new_state.index(None)
    target_index = blank_i + move
    
    new_state[blank_i], new_state[target_index] = (
        new_state[target_index],
        new_state[blank_i],
    )
    
    return new_state


def generateRandom(n: int, min: int, max: int) -> list:
    """Generate a random nxn-Puzzle in a []*n list.

    Args:
        n (int): The size of the puzzle; nxn
        min (int): The minimum shifts from original puzzle
        max (int): The maximum shifts from original puzzle

    Returns:
        list: The generated puzzle
    """
    rand = random.randint(min, max)
    state = [i for i in range(1, n * n)] + [blank]

    for i in range(rand):
        moves = allMoves(state, n)
        move = random.choice(moves)
        state = doMove(state, move)

    return state
