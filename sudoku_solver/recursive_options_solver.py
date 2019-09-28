import copy
from typing import List, Optional

from sudoku_solver import sudoku_verifier


def solve(sudoku, options=None, x_offset=0, y_offset=0) -> Optional[List]:
    """
    Attempt to solve the Sudoku.

    :param sudoku: two-dimensional array, where sudoku[y][x]
    :param options: list of possible values for each field, where options[y][x]
    :param x_offset: continue to solve from this position
    :param y_offset: continue to solve from this position
    :return: Solved Sudoku or None if no solution is found
    """
    if options is None:
        options = generate_options(sudoku)

    for y in range(y_offset, 9):
        for x in range(x_offset, 9):
            # Find the next empty field
            if sudoku[y][x] is None:
                # Try out one number after another
                for number in options[y][x]:
                    # print(f'Attempting number {number} in {x}/{y}')
                    sudoku_copy = copy.deepcopy(sudoku)
                    options_copy = copy.deepcopy(options)
                    set_field(sudoku_copy, options_copy, number, x, y)
                    sudoku_copy = solve(sudoku_copy, options_copy, x + 1, y + 1)

                    # If we found a valid solution, return the result
                    if sudoku_copy is not None:
                        return sudoku_copy
                # No number is valid, therefore abort
                return None

    # All fields are populated, verify the result
    if sudoku_verifier.is_solved(sudoku):
        # print('Solution is valid!')
        return sudoku
    else:
        # print('Solution is not valid, stepping back')
        return None


def generate_options(sudoku) -> List:
    options = []
    for y in range(9):
        options.append([])
        for x in range(9):
            if sudoku[y][x] is None:
                options[y].append(set(range(1, 10)))
            else:
                options[y].append([sudoku[y][x]])

    for y in range(9):
        for x in range(9):
            if sudoku[y][x] is not None:
                set_field(sudoku, options, sudoku[y][x], x, y)

    return options


def print_sudoku(sudoku, options=None):
    for y in range(9):
        if y % 3 == 0:
            print("")

        for x in range(9):
            if x % 3 == 0:
                print(" ", end="")

            if sudoku[y][x] is not None:
                print(f" {sudoku[y][x]} ", end="")
            elif options is not None:
                print(f" {len(options[y][x])}?", end="")
            else:
                print(f"   ", end="")
        print("")


def set_field(sudoku, options, value, x, y):
    # print(f'Setting {x}/{y} to {value}')
    sudoku[y][x] = value
    update_row_options(sudoku, options, value, y)
    update_column_options(sudoku, options, value, x)
    update_quadrant_options(sudoku, options, value, x, y)
    # print_sudoku(sudoku, options)


def update_row_options(sudoku, options, value, y):
    """Updates the available options of all fields in the row"""
    for x in range(9):
        # Skip fields that are already known
        if sudoku[y][x] is not None:
            continue

        # Remove the number from the options, as it's already set
        # somewhere else in the row
        options[y][x].discard(value)

        # Check if a new number was determined
        if len(options[y][x]) == 1:
            # print(f"Found a new number in {x}/{y}!")
            # print_sudoku(sudoku, options)
            set_field(sudoku, options, options[y][x].pop(), x, y)


def update_column_options(sudoku, options, value, x):
    """Updates the available options of all fields in the column"""
    for y in range(9):
        if sudoku[y][x] is not None:
            continue

        options[y][x].discard(value)

        if len(options[y][x]) == 1:
            # print(f"Found a new number in {x}/{y}!")
            # print_sudoku(sudoku, options)
            set_field(sudoku, options, options[y][x].pop(), x, y)


def update_quadrant_options(sudoku, options, value, x, y):
    """Updates the available options of all fields in the quadrant"""
    x_offset = int(x / 3) * 3
    y_offset = int(y / 3) * 3
    for y in range(y_offset, y_offset + 3):
        for x in range(x_offset, x_offset + 3):
            if sudoku[y][x] is not None:
                continue

            field_options = options[y][x]
            field_options.discard(value)

            if len(field_options) == 1:
                # print(f"Found a new number in {x}/{y}!")
                # print_sudoku(sudoku, options)
                set_field(sudoku, options, field_options.pop(), x, y)
