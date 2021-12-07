#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs

import timeit


def part_1(segments):
    points = set()
    counted = set()
    count = 0
    for a, b in segments:
        for point in boring_segment(a, b):
            starting_len = len(points)
            points.add(point)
            if starting_len == len(points):
                counted.add(point)

    return len(counted)

def boring_segment(a, b):
    if a[0] == b[0]:
        i, j = (0, 1)
    elif a[1] == b[1]:
        i, j = (1, 0)
    else:
        return

    start = min(a[j], b[j])
    end = max(a[j], b[j])
    for v in range(start, end + 1):
        new_point = [None, None]
        new_point[i] = a[i]
        new_point[j] = v

        yield tuple(new_point)

def part_2(segments):
    points = set()
    counted = set()
    count = 0
    for a, b in segments:
        for point in fun_segment(a, b):
            starting_len = len(points)
            points.add(point)
            if starting_len == len(points):
                counted.add(point)

    return len(counted)

def fun_segment(a, b):
    if a[0] == b[0] or a[1] == b[1]:
        for point in boring_segment(a, b):
            yield point

        return

    #8,0 0,8
    if a[0] < b[0]:
        x_range = range(a[0], b[0] + 1)
    else:
        x_range = reversed(range(b[0], a[0] + 1))

    if a[1] < b[1]:
        y_range = range(a[1], b[1] + 1)
    else:
        y_range = reversed(range(b[1], a[1] + 1))

    for x, y in zip(x_range, y_range):
        yield (x, y)

def read_lines(path):
    segments = []
    for line in import_strs(path):
        segment = []
        for point in line.split(" -> "):
            segment.append(tuple(map(int, point.split(","))))

        segments.append(tuple(segment))

    return segments

def main():
    print_solutions(
        ["resources/day5-test.txt", "resources/day5.txt"],
        read_lines,
        part_1
    )

    print_solutions(
        ["resources/day5-test.txt", "resources/day5.txt"],
        read_lines,
        part_2
    )


if __name__ == "__main__":
    main()
