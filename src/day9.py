#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs


from math import inf

def part_1(heights):
    risk = 0
    for row_idx, row in enumerate(heights):
        for col_idx, col in enumerate(row):
            if is_low(heights, row_idx, col_idx):
                risk += col + 1

    return risk

def part_2(heights):
    basins = []
    for row_idx, row in enumerate(heights):
        for col_idx, col in enumerate(row):
            if is_low(heights, row_idx, col_idx):
               basins.append(get_basin(heights, row_idx, col_idx))

    top_basins = list(sorted(basins, reverse=True))[0:3]
    total = top_basins[0]
    for basin in top_basins[1:]:
        total *= basin

    return total

def get_basin(heights, row_idx, col_idx, seen=None):
    if seen is None:
        seen = set()

    coord = (row_idx, col_idx)
    if coord in seen:
        return 0

    seen.add(coord)

    height = get_height(heights, row_idx, col_idx)
    if height >= 9:
        return 0

    size = 1
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row_offset, col_offset in offsets:
        size += get_basin(heights, row_idx + row_offset, col_idx + col_offset, seen)

    return size

def is_low(heights, row_idx, col_idx):
    col = heights[row_idx][col_idx]
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row_offset, col_offset in offsets:
        if col >= get_height(heights, row_idx + row_offset, col_idx + col_offset):
            return False

    return True

def get_height(heights, row_idx, col_idx):
    if col_idx < 0 or row_idx < 0:
        return inf

    if row_idx >= len(heights):
        return inf

    row = heights[row_idx]
    if col_idx >= len(row):
        return inf

    return row[col_idx]

def import_input(path):
    lines = import_strs(path)
    heights = []
    for line in lines:
        heights.append(list(map(int, list(line))))

    return heights

def main():
    print_solutions(
        ["resources/day9-test.txt", "resources/day9.txt"],
        import_input,
        part_1
    )

    print_solutions(
        ["resources/day9-test.txt", "resources/day9.txt"],
        import_input,
        part_2
    )

if __name__ == "__main__":
    main()
