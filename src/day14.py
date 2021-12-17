#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs

from collections import Counter

import re

def part_1(puzzle):
    return stepercise(puzzle, 10)

def part_2(puzzle):
    return stepercise(puzzle, 40)

def stepercise(puzzle, steps):
    sequence_str, mappings = puzzle

    pairs = {}
    counts = {}
    for idx in range(len(sequence_str) - 1):
        left, _ = pair = sequence_str[idx:idx+2]
        pairs[pair] = pairs.get(pair, 0) + 1
        counts[left] = counts.get(left, 0) + 1

    counts[sequence_str[-1]] = counts.get(sequence_str[-1], 0) + 1

    for _ in range(steps):
        old_pairs = dict(pairs)
        pairs = {}
        for (left, right), count in old_pairs.items():
            middle = mappings[left + right]
            counts[middle] = counts.get(middle, 0) + count

            a = left + middle
            pairs[a] = pairs.get(a, 0) + count

            b = middle + right
            pairs[b] = pairs.get(b, 0) + count

    return most_least(counts)

def stepercise_old(puzzle, steps):
    sequence, mappings = puzzle

    for _ in range(steps):
        new_seq = ""
        for idx in range(len(sequence) - 1):
            left, right = sequence[idx:idx+2]
            middle = mappings.get(left + right, "")
            new_seq += left + middle

        new_seq += sequence[-1]

        sequence = new_seq

    return most_least(sequence)

def most_least(seq):
    counts = Counter(seq).most_common()

    return counts[0][1] - counts[-1][1]

def import_puzzle(path):
    lines = import_strs(path)
    sequence = lines[0]
    mappings = {}
    for line in lines[2:]:
        m = re.match(r"^([A-Z]{2}) -> ([A-Z])", line)
        assert m

        mappings[m[1]] = m[2]

    return sequence, mappings

def main():
    print_solutions(
        ["resources/day14-test.txt", "resources/day14.txt"],
        import_puzzle,
        part_1
    )

    print_solutions(
        ["resources/day14-test.txt", "resources/day14.txt"],
        import_puzzle,
        part_2
    )

if __name__ == "__main__":
    main()
