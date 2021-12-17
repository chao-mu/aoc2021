import http.client

def import_matrix(path):
    lines = import_strs(path)

    matrix = {}
    for row_idx, line in enumerate(lines):
        for col_idx, char in enumerate(line):
            matrix[(col_idx, row_idx)] = int(char)

    return matrix


def import_strs(path):
    with open(path) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]

def import_ints_line(path):
    with open(path) as f:
        line = f.read()

    return [int(d) for d in line.strip().split(",")]

def import_ints(path):
    with open(path) as f:
        lines = f.readlines()

    return [int(line.strip()) for line in lines]

def print_solutions(paths, read, solve):
    for path in paths:
        inputs = read(path)
        result = solve(inputs)
        print(result)

