#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs

from math import inf

import re

def part_1(puzzle):
    points, folds = puzzle
    folding = {"x": fold_x, "y": fold_y}
    for axis, at in folds:
        points = folding[axis](points, at)
        break

    return len(points)

def fold_x(points, at):
    return set((abs(p[0] - at) - 1, p[1]) for p in points)

def fold_y(points, at):
    return set((p[0], abs(p[1] - at) - 1) for p in points)

def print_points(points):
    out = ""
    for y in range(0, max(p[1] for p in points) + 1):
        for x in range(0, max(p[0] for p in points) + 1):
            if (x, y) in points:
                out += "#"
            else:
                out += "."
        out += "\n"

    print(out)

def part_2(puzzle):
    points, folds = puzzle
    folding = {"x": fold_x, "y": fold_y}
    for axis, at in folds:
        points = folding[axis](points, at)

    print_points(points)

def import_puzzle(path):
    lines = import_strs(path)
    folds = []
    points = set()
    for line in lines:
        m = re.match(r"^(\d+),(\d+)$", line)
        if m:
            points.add((int(m[1]), int(m[2])))
            continue

        m = re.search("(x|y)=(\d+)", line)
        if m:
            folds.append((m[1], int(m[2])))

    return points, folds

def main():
    print_solutions(
        ["resources/day13-test.txt", "resources/day13.txt"],
        import_puzzle,
        part_1
    )

    print_solutions(
        ["resources/day13-test.txt", "resources/day13.txt"],
        import_puzzle,
        part_2
    )

if __name__ == "__main__":
    main()
