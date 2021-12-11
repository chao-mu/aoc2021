#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs

from math import inf

Openings = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">",
}

PointsPart1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def part_1(lines):
    total = 0
    for line in lines:
        stack = []
        for char in line:
            if char in Openings:
                stack.append(char)
            else:
                if not stack or Openings[stack[-1]] != char:
                    total += PointsPart1[char]
                    break

                stack.pop()

    return total

PointsPart2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def part_2(lines):
    scores = []
    for line in lines:
        stack = []
        error = False
        for char in line:
            if char in Openings:
                stack.append(char)
            else:
                if not stack or Openings[stack[-1]] != char:
                    error = True
                    break

                stack.pop()

        if error:
            continue

        score = 0
        for char in reversed(stack):
            score = score * 5 + PointsPart2[Openings[char]]

        scores.append(score)

    scores.sort()

    return scores[len(scores) // 2]

def main():
    print_solutions(
        ["resources/day10-test.txt", "resources/day10.txt"],
        import_strs,
        part_1
    )
#
    print_solutions(
        ["resources/day10-test.txt", "resources/day10.txt"],
        import_strs,
        part_2
    )

if __name__ == "__main__":
    main()
