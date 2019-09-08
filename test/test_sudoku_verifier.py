from sudoku_solver import sudoku_verifier


def test_incomplete_sudoku():
    sudoku = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ]
    actual = sudoku_verifier.is_solved(sudoku)
    assert actual is False


def test_incorrectly_solved():
    sudoku = [
        [9, 8, 6, 7, 2, 3, 4, 5, 1],
        [3, 4, 1, 5, 6, 8, 2, 7, 9],
        [2, 5, 7, 1, 4, 9, 6, 3, 8],
        [8, 3, 5, 6, 9, 2, 1, 4, 7],
        [4, 6, 9, 3, 7, 1, 5, 8, 2],
        [7, 1, 2, 8, 5, 4, 3, 9, 6],
        [1, 9, 3, 2, 8, 5, 7, 6, 4],
        [6, 2, 8, 4, 3, 7, 7, 1, 5],
        [5, 7, 4, 9, 1, 6, 8, 2, 3]
    ]
    actual = sudoku_verifier.is_solved(sudoku)
    assert actual is False


def test_correctly_solved():
    sudoku = [
        [9, 8, 6, 7, 2, 3, 4, 5, 1],
        [3, 4, 1, 5, 6, 8, 2, 7, 9],
        [2, 5, 7, 1, 4, 9, 6, 3, 8],
        [8, 3, 5, 6, 9, 2, 1, 4, 7],
        [4, 6, 9, 3, 7, 1, 5, 8, 2],
        [7, 1, 2, 8, 5, 4, 3, 9, 6],
        [1, 9, 3, 2, 8, 5, 7, 6, 4],
        [6, 2, 8, 4, 3, 7, 9, 1, 5],
        [5, 7, 4, 9, 1, 6, 8, 2, 3]
    ]
    actual = sudoku_verifier.is_solved(sudoku)
    assert actual is True


def test_correct_quadrant():
    quadrant = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    actual = sudoku_verifier.is_quadrant_solved(quadrant, 0)
    assert actual is True


def test_incomplete_quadrant():
    quadrant = [
        [1, 2, 3],
        [4, None, 6],
        [7, 8, 9]
    ]
    actual = sudoku_verifier.is_quadrant_solved(quadrant, 0)
    assert actual is False


def test_incorrect_quadrant_row():
    quadrant = [
        [1, 2, 3],
        [4, 6, 6],
        [7, 8, 9]
    ]
    actual = sudoku_verifier.is_quadrant_solved(quadrant, 0)
    assert actual is False


def test_correct_quadrant_row_offset_1():
    quadrant = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    actual = sudoku_verifier.is_quadrant_solved(quadrant, 1)
    assert actual is True


def test_correct_quadrant_row_offset_2():
    quadrant = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    actual = sudoku_verifier.is_quadrant_solved(quadrant, 2)
    assert actual is True


def test_correct_quadrant_column_and_row_offset():
    quadrant = [
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, 1, 2, 3],
        [None, None, None, 4, 5, 6],
        [None, None, None, 7, 8, 9]
    ]
    actual = sudoku_verifier.is_quadrant_solved(quadrant, 4)
    assert actual is True


def test_incorrect_quadrant_column():
    quadrant = [
        [1, 5, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    actual = sudoku_verifier.is_quadrant_solved(quadrant, 0)
    assert actual is False


def test_correct_quadrant_column_offset_1():
    quadrant = [
        [None, None, None, 1, 2, 3],
        [None, None, None, 4, 5, 6],
        [None, None, None, 7, 8, 9]
    ]
    actual = sudoku_verifier.is_quadrant_solved(quadrant, 3)
    assert actual is True


def test_correct_quadrant_column_offset_2():
    quadrant = [
        [None, None, None, None, None, None, 1, 2, 3],
        [None, None, None, None, None, None, 4, 5, 6],
        [None, None, None, None, None, None, 7, 8, 9]
    ]

    actual = sudoku_verifier.is_quadrant_solved(quadrant, 6)
    assert actual is True
