from Classes.CSP import CSP

def alldiff(lis: list[int], C: dict[int, list[int]]) -> None:
    """Convert alldiff constraint to binary constraints, append to C.

    Args:
        lis (list[int]): alldiff constraint values
        C (dict[int, list[int]]): binary constraint dictionary
    """
    for i in lis:
        for j in lis:
            if i == j:
                continue
            else:
                if j not in C[i]:
                    C[i].append(j)
    return

def toIndex(x: int, y: int) -> int:
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

def toCoordinate(index: int) -> tuple[int, int]:
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

def toGrid(csp: CSP) -> list[int | None]:
    """Takes a CSP instance, convert to formmated list grid.

    Args:
        csp (CSP): The CSP instance.

    Returns:
        list[int | None]: The grid.
    """
    return [Xi for Xi in csp.X.values()]