#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_ints_line

def part_2(fishes, days):
    count_cache = {}
    count = sum(calc_fish(fish, days, count_cache) for fish in fishes)
    print(count)

def calc_fish(fish, days, count_cache):
    key = (fish, days)
    if key in count_cache:
        return count_cache[key]

    if days <= 0:
        return 1

    count = 0
    if fish <= 0:
        fish = 7
        count += calc_fish(8, days - 1, count_cache)

    count += calc_fish(fish - 1, days - 1, count_cache)

    count_cache[key] = count

    return count

def part_1(fishes, days):
    for _ in range(days):
        new_fishes = []
        for idx, fish in enumerate(fishes):
            if fish <= 0:
                fish = 6
                new_fishes.append(8)
            else:
                fish -= 1

            fishes[idx] = fish

        fishes += new_fishes

    print(len(fishes))

def main():
    part_1(import_ints_line("resources/day6-test.txt"), 18)
    part_2(import_ints_line("resources/day6-test.txt"), 18)
    part_1(import_ints_line("resources/day6.txt"), 80)
    part_2(import_ints_line("resources/day6.txt"), 80)

    part_2(import_ints_line("resources/day6-test.txt"), 256)
    part_2(import_ints_line("resources/day6.txt"), 256)

if __name__ == "__main__":
    main()
