from sudoku_solver import sudoku_verifier, options_solver


def test_easy_sudoku():
    sudoku = [
        [9, 8, 6, 7, 2, 3, 4, 5, 1],
        [3, 4, 1, 5, 6, 8, 2, 7, 9],
        [2, 5, 7, 1, 4, 9, 6, 3, 8],
        [8, 3, 5, 6, 9, 2, 1, 4, 7],
        [4, 6, 9, 3, 7, 1, 5, 8, 2],
        [7, 1, 2, 8, 5, 4, 3, 9, 6],
        [1, 9, 3, 2, 8, 5, 7, 6, 4],
        [6, 2, 8, 4, 3, 7, 9, 1, 5],
        [5, 7, 4, 9, 1, 6, 8, 2, None]
    ]

    actual = options_solver.solve(sudoku)
    # sudoku_verifier.print_sudoku(sudoku)
    assert sudoku_verifier.is_solved(actual) is True


def test_realistic_easy_sudoku():
    sudoku = [
        [9, 8, None, 7, None, None, None, None, 1],
        [3, None, None, None, 6, None, None, 7, 9],
        [2, None, 7, None, 4, None, None, None, None],
        [None, 3, None, None, 9, 2, None, None, None],
        [4, 6, 9, None, None, 1, None, 8, 2],
        [None, None, 2, None, None, None, None, None, 6],
        [1, 9, None, 2, 8, None, 7, None, 4],
        [6, None, 8, None, None, 7, None, None, 5],
        [5, 7, None, 9, None, None, None, None, None]
    ]
    expected = [
        [9, 8, None, 7, None, 3, None, None, 1],
        [3, None, None, None, 6, 8, None, 7, 9],
        [2, None, 7, None, 4, 9, None, None, None],
        [8, 3, None, None, 9, 2, None, None, 7],
        [4, 6, 9, None, None, 1, None, 8, 2],
        [7, None, 2, None, None, 4, None, None, 6],
        [1, 9, 3, 2, 8, 5, 7, 6, 4],
        [6, 2, 8, None, None, 7, None, None, 5],
        [5, 7, 4, 9, None, 6, None, None, None]
    ]

    actual = options_solver.solve(sudoku)
    # sudoku_verifier.print_sudoku(sudoku)
    assert actual == expected
