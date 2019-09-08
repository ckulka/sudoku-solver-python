from sudoku_solver import sudoku_file_reader
from sudoku_solver.observer_pattern import Sudoku


def solve_with_file(filename: str):
    input_data = sudoku_file_reader.parse(filename)
    actual = Sudoku(input_data).solve()
    # actual.print()
    assert actual is not None
    assert actual.is_solved() is True


def is_solved_with_file(filename: str, expect_solved: bool):
    input_data = sudoku_file_reader.parse(filename)
    actual = Sudoku(input_data)
    # actual.print()
    assert actual.is_solved() is expect_solved


def test_solve_easy_sudoku():
    solve_with_file("test/data/easy.txt")


def test_solve_missing_quadrant_3():
    solve_with_file("test/data/missing_quadrant_3.txt")


def test_solve_missing_quadrant_5():
    solve_with_file("test/data/missing_quadrant_5.txt")


def test_solve_realistic_easy_sudoku():
    solve_with_file("test/data/realistic_easy.txt")


def test_is_solved_incorrectly():
    is_solved_with_file("test/data/incorrectly_solved.txt", False)


def test_is_solved_incompletely():
    is_solved_with_file("test/data/incompletely_solved.txt", False)


def test_is_solved_empty():
    is_solved_with_file("test/data/empty.txt", False)


def test_is_solved_correctly():
    is_solved_with_file("test/data/correctly_solved.txt", True)
