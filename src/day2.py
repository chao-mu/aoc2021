#!/usr/bin/env python3

from aoc2021.util import print_solutions

import timeit

def part_1(commands):
    totals = {"down": 0, "up": 0, "forward": 0}
    for cmd, dist in commands:
        totals[cmd] += dist

    return (totals["down"] - totals["up"]) * totals["forward"]

def part_2(commands):
    aim = 0
    depth = 0
    horizontal = 0
    for cmd, dist in commands:
        if cmd == "down":
            aim += dist
        elif cmd == "up":
            aim -= dist
        elif cmd == "forward":
            horizontal += dist
            depth += aim * dist

    return depth * horizontal

def import_commands(path):
    with open(path) as f:
        lines = f.readlines()

    commands = []
    for cmd_raw in lines:
        cmd, dist = cmd_raw.strip().split(" ")
        commands.append((cmd, int(dist)))

    return commands

def main():
    print_solutions(
        ["resources/day2-test.txt", "resources/day2.txt"],
        import_commands,
        part_1
    )
    print_solutions(
        ["resources/day2-test.txt", "resources/day2.txt"],
        import_commands,
        part_2
    )

if __name__ == "__main__":
    main()
