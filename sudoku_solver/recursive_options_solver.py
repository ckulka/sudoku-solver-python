import copy

from sudoku_solver import options_solver, sudoku_verifier


def solve(sudoku):
    options = options_solver.generate_options(sudoku)

    for x in range(9):
        for y in range(9):
            if sudoku[x][y] is not None:
                options_solver.set_field(sudoku, options, sudoku[x][y], x, y)

    return solve_recursive(sudoku, options, 0, 0)


def solve_recursive(sudoku, options, x_offset, y_offset):
    for x in range(x_offset, 9):
        for y in range(y_offset, 9):
            # Find the next empty field
            if sudoku[x][y] is None:
                options_backup = copy.deepcopy(options[x][y])
                # Try out one number after another
                for number in options_backup:
                    # print(f'Attempting number {number} in {x}/{y}')
                    options_solver.set_field(sudoku, options, number, x, y)
                    # If we found a valid solution, return the result
                    if solve(sudoku) is not None:
                        return sudoku
                # No number is valid, therefore abort
                sudoku[x][y] = None
                options[x][y] = options_backup
                return None

    # All fields are populated, verify the result
    # print('Verifying possible solution:')
    # sudoku_verifier.print_sudoku(sudoku)
    if sudoku_verifier.is_solved(sudoku):
        # print('Solution is valid!')
        return sudoku
    else:
        # print('Solution is not valid, stepping back')
        return None
