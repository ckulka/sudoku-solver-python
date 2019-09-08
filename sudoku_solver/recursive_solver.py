from sudoku_solver import sudoku_verifier


def solve(sudoku):
    for x in range(9):
        for y in range(9):
            # Find the next empty field
            if sudoku[x][y] is None:
                # Try out one number after another
                for number in range(1, 10):
                    # print(f'Attempting number {number} in {x}/{y}')
                    sudoku[x][y] = number
                    # If we found a valid solution, return the result
                    if solve(sudoku) is not None:
                        return sudoku
                # No number is valid, therefore abort
                sudoku[x][y] = None
                return None

    # All fields are populated, verify the result
    # print('Verifying possible solution:')
    # sudoku_verifier.print_sudoku(sudoku)
    if sudoku_verifier.is_solved(sudoku):
        print('Solution is valid!')
        return sudoku
    else:
        # print('Solution is not valid, stepping back')
        return None
