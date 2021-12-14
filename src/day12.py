#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs

def part_1(graph):
    paths = navigate(graph, ["start"])

    return len(paths)

def navigate(graph, path):
    node = path[-1]
    if node == "end":
        return [path]

    paths = []
    for neighbor in graph[node]:
        if neighbor.islower() and neighbor in path:
            continue

        paths += navigate(graph, path + [neighbor])

    return paths


def part_2(graph):
    print(graph)
    paths = navigate_2(graph, ["start"])

    return len(paths)

def navigate_2(graph, path):
    node = path[-1]
    if node == "end":
        return [path]

    if len(path) > 1 and node == "start":
        return []

    small_visits = {}
    can_double_visit = True
    for existing_node in path:
        if existing_node.islower() and existing_node in small_visits:
            can_double_visit = False
            break

        small_visits[existing_node] = True

    paths = []
    for neighbor in graph[node]:
        if not can_double_visit and neighbor.islower() and neighbor in path:
            continue

        paths += navigate_2(graph, path + [neighbor])

    return paths

def import_graph(path):
    graph = {}
    for line in import_strs(path):
        left, right = line.split("-")
        for node in [left, right]:
            if node not in graph:
                graph[node] = set()

        graph[left].add(right)
        graph[right].add(left)

    return graph

def main():
    print_solutions(
        ["resources/day12-test.txt", "resources/day12.txt"],
        import_graph,
        part_1
    )

    print_solutions(
        ["resources/day12-test.txt", "resources/day12.txt"],
        import_graph,
        part_2
    )

if __name__ == "__main__":
    main()
