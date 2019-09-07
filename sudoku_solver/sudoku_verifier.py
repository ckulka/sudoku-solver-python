
def is_sudoku_solved(sudoku):
    # Verify all rows are complete
    for index in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        if not is_row_complete(sudoku, index):
            return False

    # Verify all rows are complete
    for index in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        if not is_column_complete(sudoku, index):
            return False

    # Verify all quadrants are complete
    for quadrant_index in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        if not is_qudrant_solved(sudoku, quadrant_index):
            return False

    return True

def is_row_complete(sudoku, row_index):
    '''
    return true if the row has all numbers
    '''
    for number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if number not in sudoku[row_index]:
            return False
    return True


def is_column_complete(sudoku, column_index):
    '''
    return true if the row has all numbers
    '''
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row_index in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        number = sudoku[row_index][column_index]
        if number not in numbers:
            return False
        else:
            numbers.remove(number)
    
    return len(numbers) == 0

def is_qudrant_solved(sudoku, quadrant_index):
    '''
    returns true if the 3x3 qudrant is solved
    '''
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x_offset = (quadrant_index % 3) * 3
    y_offset = int(quadrant_index / 3) * 3
    for x in [0, 1, 2]:
        for y in [0, 1, 2]:
            number = sudoku[x_offset + x][y_offset + y]
            if number not in numbers:
                return False
            else:
                numbers.remove(number)

    return len(numbers) == 0

def print_sudoku(sudoku):
    for row_index in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print(str(sudoku[row_index]))