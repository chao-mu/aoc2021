#!/usr/bin/env python3

from aoc2021.util import import_ints

def main():
    for path in ["resources/day1-test.txt", "resources/day1.txt"]:
        depths = import_ints(path)

        increases = 0
        for idx, x in enumerate(depths[:-1]):
            if x < depths[idx + 1]:
                increases += 1

        print(increases)

        #print(sum(1 for idx, x in enumerate(depths[:-1]) if x < depths[idx + 1]))

if __name__ == "__main__":
    main()
