def parse(filename):
    return parse_with_lambdas(filename)


def parse_with_for_loop(filename):
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


def parse_with_lambdas(filename):
    sudoku = []

    file = open(filename)
    for line in file.readlines():
        fields = line.split(",")
        fields = map(lambda text: text.strip(), fields)
        fields = map(lambda text: None if text == "" else int(text), fields)
        sudoku.append(list(fields))

    return sudoku
