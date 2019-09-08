def is_solved(sudoku):
    """
    :param sudoku: the Sudoku to be tested
    :return: True if the Sudoku is solved, false otherwise
    """
    # Verify all rows are complete
    for index in range(9):
        if not is_row_complete(sudoku, index):
            return False

    # Verify all rows are complete
    for index in range(9):
        if not is_column_complete(sudoku, index):
            return False

    # Verify all quadrants are complete
    for quadrant_index in range(9):
        if not is_quadrant_solved(sudoku, quadrant_index):
            return False

    return True


def is_row_complete(sudoku, row_index):
    """
    :returns: true if the row has all numbers
    """
    for number in range(1, 10):
        if number not in sudoku[row_index]:
            return False
    return True


def is_column_complete(sudoku, column_index):
    """
    :returns: true if the column has all numbers
    """
    numbers = list(range(1, 10))
    for row_index in range(9):
        number = sudoku[row_index][column_index]
        if number not in numbers:
            return False
        else:
            numbers.remove(number)

    return len(numbers) == 0


def is_quadrant_solved(sudoku, quadrant_index):
    """
    :returns: true if the 3x3 quadrant is solved
    """
    numbers = list(range(1, 10))
    x_offset = (quadrant_index % 3) * 3
    y_offset = int(quadrant_index / 3) * 3
    for x in range(3):
        for y in range(3):
            number = sudoku[x_offset + x][y_offset + y]
            if number not in numbers:
                return False
            else:
                numbers.remove(number)

    return len(numbers) == 0


def print_sudoku(sudoku):
    for row_index in range(9):
        print(str(sudoku[row_index]))
