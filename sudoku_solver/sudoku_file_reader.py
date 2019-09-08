
def parse(filename):
    return parse_for_each_loop(filename)


def parse_for_each_loop(filename):
    sudoku = []

    file = open(filename)
    lines = file.readlines()

    for line in lines:
        fields = line.split(",")
        sudoku_line = []
        for field in fields:
            if field.strip() == "":
                sudoku_line.append(None)
            else:
                sudoku_line.append(int(field.strip()))
        sudoku.append(sudoku_line)

    return sudoku
