from sudoku_solver import sudoku_file_reader, sudoku_verifier


def test_parse_with_for_loop():
    expected = [
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

    input_file = "test/data/easy.txt"
    actual = sudoku_file_reader.parse_with_for_loop(input_file)
    # sudoku_verifier.print_sudoku(actual)

    assert expected == actual


def test_parse_with_lambdas():
    expected = [
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

    input_file = "test/data/easy.txt"
    actual = sudoku_file_reader.parse_with_lambdas(input_file)
    # sudoku_verifier.print_sudoku(actual)

    assert expected == actual
