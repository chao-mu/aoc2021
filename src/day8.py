#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs

from math import inf

from itertools import permutations

import copy

def part_1(clock):
    uniqs = 0
    for face in clock:
        _, signals = face
        for signal in signals:
            if len(signal) in [2, 4, 3, 7]:
                uniqs += 1

    return uniqs

Numbers = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

def part_2(clock):
    total = 0
    for face in clock:
        patterns, signals = face
        assignments = backward_search({c: "*" for c in "abcdefg"}, patterns)

        number = ""
        for s in signals:
            correct_s = "".join(sorted(assignments[c] for c in s))
            number += str(Numbers[correct_s])

        total += int(number)

    return total

def backward_search(assignments, patterns):
    unassigned = None
    domain = set("abcdefg")
    for s, e in assignments.items():
        if e == "*":
            unassigned = s
        else:
            domain.remove(e)

    if unassigned is None:
        return assignments

    for d in domain:
        local = copy.deepcopy(assignments)
        local[unassigned] = d
        if consistent(local, patterns):
            local = backward_search(local, patterns)
            if local is not None:
                return local

    return None

def consistent(assignments, patterns):
    for pattern in patterns:
        new_str = "".join(assignments[s] for s in pattern)
        candidates = [s for s in Numbers if len(s) == len(new_str)]
        candidate_found = False

        for candidate in candidates:
            matched = True
            for idx, char in enumerate(new_str):
                if char != "*" and char not in candidate:
                    matched = False
                    break

            if matched:
                candidate_found = True

        if not candidate_found:
            return False

    return True

def import_clock(path):
    clock = []
    lines = import_strs(path)
    for line in lines:
        patterns, signals = line.strip().split(" | ")
        clock.append([patterns.split(" "), signals.split(" ")])

    return clock

def main():
    print_solutions(
        ["resources/day8-test.txt", "resources/day8.txt"],
        import_clock,
        part_1
    )

    print_solutions(
        ["resources/day8-test.txt", "resources/day8.txt"],
        import_clock,
        part_2
    )

if __name__ == "__main__":
    main()
