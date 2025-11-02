import csv


def read_sudoku(path):
    sudoku = []
    with open(path, newline="") as file:
        for row in csv.reader(file):
            for char in row:
                clean_char = (char or "").strip()

                try:
                    int_clean_char = int(clean_char)
                    sudoku.append(int_clean_char if 1 <= int_clean_char <= 9 else None)

                except ValueError:
                    sudoku.append(None)

    return sudoku


def write_sudoku_csv(path, grid):

    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        for r in range(0, 81, 9):
            w.writerow([(grid[r+c] if grid[r+c] is not None else 0) for c in range(9)])
#henlo