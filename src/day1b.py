#!/usr/bin/env python3

from aoc2021.util import import_ints

import timeit

def f(depths):
    increases = 0
    window = depths[:3]
    for idx in range(3, len(depths)):
        new_window = window[1:] + [depths[idx]]
        if sum(new_window) > sum(window):
            increases += 1

        window = new_window

    return increases

def print_solutions(paths, solve):
    for path in paths:
        depths = import_ints(path)
        increases = solve(depths)
        print(increases)

def main():
    print_solutions(["resources/day1-test.txt", "resources/day1.txt"], f)

if __name__ == "__main__":
    main()
