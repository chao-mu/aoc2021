#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_ints_line

from math import inf

def part_1(crabs):
    min_cost = inf
    for pos in range(1, len(crabs) + 1):
        cost = sum(abs(crab - pos) for crab in crabs)
        min_cost = min(min_cost, cost)

    return min_cost

def part_2(crabs):
    min_cost = inf
    for pos in range(1, len(crabs) + 1):
        cost = 0
        for crab in crabs:
            cost += sum(range(1, abs(crab - pos) + 1))

        min_cost = min(min_cost, cost)

    return min_cost

def main():
    print_solutions(
        ["resources/day7-test.txt", "resources/day7.txt"],
        import_ints_line,
        part_1
    )
#
    print_solutions(
        ["resources/day7-test.txt", "resources/day7.txt"],
        import_ints_line,
        part_2
    )

if __name__ == "__main__":
    main()
