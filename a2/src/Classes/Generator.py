import random
from collections import defaultdict
N = 9

def idx_to_rc(idx):
    """
    index to row and coloum
    """
    return idx // N, idx % N

def rc_to_idx(r, c):
    """
    row and coloum to index
    """
    return r * N + c

def conflict_indices(idx):
    """
    return indices that are in the same row, col, or 3x3 box
    """
    r, c = idx_to_rc(idx)
    s = set()
    # row
    for cc in range(N):
        s.add(rc_to_idx(r, cc))
    # col
    for rr in range(N):
        s.add(rc_to_idx(rr, c))
    # box
    br, bc = (r//3)*3, (c//3)*3
    for rr in range(br, br+3):
        for cc in range(bc, bc+3):
            s.add(rc_to_idx(rr, cc))
    return s
CONFLICTS = [conflict_indices(i) for i in range(N*N)]

def generate():
    """
    uses indices asa  way to randomly add each value while picking the the most legal option to add while doing so
    """
    grid = [None]*(N*N)
    used_indices = set()
    number_lists = {n:[n]*9 for n in range(1,10)}

    global_indices = list(range(N*N))
    random.shuffle(global_indices)
    for num in range(1, 10):
        avail = set(global_indices) - used_indices
        while number_lists[num]:
            if not avail:
                avail = set(global_indices) - used_indices
            chosen = min(avail, key=lambda idx: len(CONFLICTS[idx] & avail))
            grid[chosen] = num
            number_lists[num].pop()
            used_indices.add(chosen)
            avail -= CONFLICTS[chosen]
            avail &= set(global_indices) - used_indices

    # convert to 9x9 grid
    final_grid = [[0]*N for _ in range(N)]
    for idx, val in enumerate(grid):
        r, c = idx_to_rc(idx)
        final_grid[r][c] = val

    return final_grid

def print_grid(grid):
    """
    print the grid
    """
    for row in range(9):
        if row%3==0 and row!=0:
            print("------+-------+------")
        row_string=[]
        for col in range(9):
    
            if col%3==0 and col!=0:
                row_string.append("|")
            if grid[row][col]==None:
                row_string.append(".")
            else:
                row_string.append(str(grid[row][col]))
        print(" ".join(row_string))

def unsolve(amount,grid):
    """
    randomly unsolve the sudoku for the ai to solve later
    """
    index=list(range(N*N))
    for i in range(amount):
        idx=random.choice(index)
        index.remove(idx)
        idx1,idx2=idx_to_rc(idx)
        grid[idx1][idx2]=None
    return grid

def generateGrid(size: int) -> list[int | None]:
    lis2D: list[list[int]] = unsolve(81 - size, generate())
    lis1D: list[int | None] = [i for lis in lis2D for i in lis]    # reduce 2d list
    return lis1D