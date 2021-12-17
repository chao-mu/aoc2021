#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_matrix

from math import inf

from heapq import heapify, heappop, heappush

def part_1(graph):
    return navigate(graph)

def part_2(graph):
    max_y = max(xy[1] for xy in graph)
    max_x = max(xy[0] for xy in graph if xy[1] == max_y)
    items = list(graph.items())

    for y_quad in range(0, 5):
        for x_quad in range(0, 5):
            cost_offset = x_quad + y_quad
            for xy, cost in items:
                x, y = xy
                new_xy = (x + x_quad * (max_x + 1), (y + y_quad * (max_y + 1)))
                new_cost = (cost + cost_offset - 1) % 9 + 1
                graph[new_xy] = new_cost

    return navigate(graph)

def navigate(graph):
    end_y = max(coord[1] for coord in graph)
    end_x = max(coord[0] for coord in graph if coord[1] == end_y)
    end = (end_x, end_y)

    costs = {coord: inf for coord in graph}
    start = (0, 0)
    costs[start] = 0
    q = [(costs[start], start)]
    heapify(q)
    while q:
        weight, coord = heappop(q)
        for neighbor in neighbors(coord):
            if neighbor not in graph:
                continue

            neighbor_cost = weight + graph[neighbor]
            if costs[neighbor] <= neighbor_cost:
                continue

            costs[neighbor] = neighbor_cost
            if neighbor == end:
                return costs[neighbor]

            heappush(q, (neighbor_cost, neighbor))

def neighbors(coord):
    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    return [(coord[0] + x, coord[1] + y) for x, y in offsets]

def main():
    print_solutions(
        ["resources/day15-test.txt", "resources/day15.txt"],
        import_matrix,
        part_1
    )

    print_solutions(
        ["resources/day15-test.txt", "resources/day15.txt"],
        import_matrix,
        part_2
    )

if __name__ == "__main__":
    main()
