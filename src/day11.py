#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_matrix

from math import inf

def part_1(dumbos):
    flashes = 0
    for _ in range(100):
        for coord in dumbos:
            dumbos[coord] += 1

        flashed = set()
        for coord, dumbo in dumbos.items():
            if coord not in flashed and dumbo > 9:
                flash(dumbos, coord, flashed)

        flashes += len(flashed)

    return flashes

def part_2(dumbos):
    flashes = 0
    step = 0
    while True:
        step += 1

        for coord in dumbos:
            dumbos[coord] += 1

        flashed = set()
        for coord, dumbo in dumbos.items():
            if coord not in flashed and dumbo > 9:
                flash(dumbos, coord, flashed)


        if len(flashed) == len(dumbos):
            return step

def flash(dumbos, coord, flashed):
    if coord not in dumbos:
        return

    if coord in flashed:
        return

    dumbos[coord] += 1

    if dumbos[coord] <= 9:
        return

    dumbos[coord] = 0
    flashed.add(coord)

    for offset in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
        flash(dumbos, tuple(map(sum, zip(coord, offset))), flashed)

def main():
    print_solutions(
        ["resources/day11-test.txt", "resources/day11.txt"],
        import_matrix,
        part_1
    )

    print_solutions(
        ["resources/day11-test.txt", "resources/day11.txt"],
        import_matrix,
        part_2
    )

if __name__ == "__main__":
    main()
