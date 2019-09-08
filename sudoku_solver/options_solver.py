def solve(sudoku):
    options = generate_options(sudoku)

    for x in range(9):
        for y in range(9):
            if sudoku[x][y] is not None:
                set_field(sudoku, options, sudoku[x][y], x, y)

    return sudoku


def set_field(sudoku, options, value, x, y):
    # print(f'Setting {x}/{y} to {value}')
    sudoku[x][y] = value
    update_row_options(sudoku, options, value, y)
    update_column_options(sudoku, options, value, x)
    update_quadrant_options(sudoku, options, value, x, y)
    # print_with_options(sudoku, options)


def print_with_options(sudoku, options):
    for x in range(9):
        print("[", end="")
        for y in range(9):
            if sudoku[x][y] is not None:
                print(f" {sudoku[x][y]} ,", end="")
            else:
                print(f" {len(options[x][y])}?,", end="")
        print("]")


def generate_options(sudoku):
    options = []
    for x in range(9):
        options.append([])
        for y in range(9):
            if sudoku[x][y] is None:
                options[x].append(set(range(1, 10)))
            else:
                options[x].append([sudoku[x][y]])

    return options


def update_row_options(sudoku, options, value, y):
    """Updates the available options of all fields in the row"""
    for x in range(9):
        # Skip fields that are already known
        if sudoku[x][y] is not None:
            continue

        # Remove the number from the options, as it's already set
        # somewhere else in the row
        options[x][y].discard(value)

        # Check if a new number was determined
        if len(options[x][y]) == 1:
            # print(f"Found a new number in {x}/{y}!")
            set_field(sudoku, options, options[x][y].pop(), x, y)


def update_column_options(sudoku, options, value, x):
    """Updates the available options of all fields in the column"""
    for y in range(9):
        if sudoku[x][y] is not None:
            continue

        options[x][y].discard(value)

        if len(options[x][y]) == 1:
            # print(f"Found a new number in {x}/{y}!")
            set_field(sudoku, options, options[x][y].pop(), x, y)


def update_quadrant_options(sudoku, options, value, x, y):
    """Updates the available options of all fields in the quadrants"""
    x_offset = int(x / 3) * 3
    y_offset = int(y / 3) * 3
    for x in range(x_offset, x_offset + 3):
        for y in range(y_offset, y_offset + 3):
            if sudoku[x][y] is not None:
                continue

            field_options = options[x][y]
            field_options.discard(value)

            if len(field_options) == 1:
                # print(f"Found a new number in {x}/{y}!")
                set_field(sudoku, options, field_options.pop(), x, y)
