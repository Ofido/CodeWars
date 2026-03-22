"""
Write a function that will solve a 9x9 Sudoku puzzle.
The function will take one argument consisting of the 2D puzzle array,
with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy"
(i.e. determinable; there will be no need to assume and test
possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.
"""


def check_can_be(puzzle: list[list[int]], row: int, col: int) -> set[int]:
    default = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    line = set(puzzle[row])
    column = set([puzzle[a][col] for a in range(len(puzzle))])
    row_box = (row // 3) * 3
    col_box = (col // 3) * 3
    box = set(
        [
            puzzle[a][b]
            for a in range(row_box, row_box + 3)
            for b in range(col_box, col_box + 3)
        ]
    )
    missing = default - (line | column | box)
    return missing


def sudoku(puzzle: list[list[int]]) -> list[list[int]]:
    """return the solved sudoku puzzle as a 2d array of 9 x 9"""
    has_zero = True
    made_progress = True
    while has_zero:
        has_zero = False
        made_progress = False
        for row, col in [
            (a, b) for a in range(9) for b in range(9) if not puzzle[a][b]
        ]:
            can_be = check_can_be(puzzle, row, col)
            if len(can_be) == 1:
                puzzle[row][col] = can_be.pop()
                made_progress = True
            else:
                has_zero = True
        if not made_progress and has_zero:
            print("sudoku mais dificil que o planejado")
            raise NotImplementedError()
    return puzzle


puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


print(sudoku(puzzle) == solution)
