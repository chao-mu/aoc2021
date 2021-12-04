#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs

import timeit

def part_1(consumptions):
    counts = bit_counts(consumptions)
    n = len(counts)
    gamma_b = ["0"] * n
    epsilon_b = ["0"] * n
    mid = len(consumptions) // 2
    for idx, count in enumerate(counts):
        gamma_b[idx] = "1" if count > mid else "0"
        epsilon_b[idx] = "0" if count > mid else "1"

    return int("".join(gamma_b), 2) * int("".join(epsilon_b), 2)

def part_2(consumptions):
    generator_rating = select_rating(consumptions, True)
    scrubber_rating = select_rating(consumptions, False)

    return scrubber_rating * generator_rating

def bit_counts(consumptions):
    n = len(consumptions[0])
    counts = [0] * n
    for cons in consumptions:
        for bit_idx, bit in enumerate(cons):
            if bit == "1":
                counts[bit_idx] += 1

    return counts

def select_rating(ratings, want_common):
    ratings = list(ratings)
    left_bit, right_bit = ("1", "0") if want_common else ("0", "1")

    for bit_idx in range(len(ratings[0])):
        if len(ratings) <= 1:
            break

        counts = bit_counts(ratings)
        count = counts[bit_idx]
        mid = len(ratings) / 2

        target_bit = left_bit if count >= mid else right_bit

        ratings[:] = [row for row in ratings if row[bit_idx] == target_bit]

    return int(ratings[0], 2)

def main():
    print_solutions(
        ["resources/day3-test.txt", "resources/day3.txt"],
        import_strs,
        part_2
    )

if __name__ == "__main__":
    main()
