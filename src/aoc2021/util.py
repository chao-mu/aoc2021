import http.client

def import_strs(path):
    with open(path) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]

def import_ints(path):
    with open(path) as f:
        lines = f.readlines()

    return [int(line.strip()) for line in lines]

def print_solutions(paths, read, solve):
    for path in paths:
        inputs = read(path)
        result = solve(inputs)
        print(result)

