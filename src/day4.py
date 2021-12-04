#!/usr/bin/env python3

from aoc2021.util import print_solutions, import_strs

import timeit

Mark = "M"

def part_1(inputs):
    called, boards = inputs

    for target in called:
        for board in boards:
            if mark_board(board, target) and check_board(board):
                return score_board(board) * target

    return None

def score_board(board):
    score = 0
    for num in sum(board, []):
        if num != Mark:
            score += num

    return score

def mark_board(board, target):
    marked = False
    for row in board:
        for col_idx, num in enumerate(row):
            if num == target:
                row[col_idx] = Mark
                marked = True

    return marked

def check_board(board):
    cols = []
    for idx in range(len(board[0])):
        cols.append([row[idx] for row in board])

    for row in board + cols:
        if not list(filter(lambda n: n != Mark, row)):
            return True

    return False

def read_bingo(path):
    with open(path) as f:
        lines = f.readlines()

    first_line = lines[0].strip()
    called = [int(d) for d in first_line.split(",")]
    lines.pop(0)

    board = []
    boards = []
    for line in lines:
        line = line.strip()
        if not line:
            if board:
                boards.append(board)
                board = []
            continue

        row = [int(d) for d in line.split(" ") if d]

        board.append(row)

    if board:
        boards.append(board)

    return (called, boards)

def part_2(inputs):
    called, boards = inputs

    last_score = None
    for target in called:
        boards[:] = [b for b in boards if b]
        if not boards:
            break

        for idx, board in enumerate(boards):
            if score_board(board) == 148:
                print(board)
            if mark_board(board, target) and check_board(board):
                last_score = score_board(board) * target
                boards[idx] = None

    return last_score


def main():
    print_solutions(
        ["resources/day4-test.txt", "resources/day4.txt"],
        #["resources/day4-test.txt"],
        read_bingo,
        part_2
    )

if __name__ == "__main__":
    main()
