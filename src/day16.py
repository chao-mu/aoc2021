#!/usr/bin/env python3

import io
from dataclasses import dataclass
import re
from typing import Optional
from functools import reduce

from aoc2021.util import print_solutions, import_strs

class Reader:

    def __init__(self, path):
        self.path = path
        self.bits_reader = None

    @property
    def bits(self):
        if self.bits_reader is None:
            with open(self.path) as f:
                raw = f.read()
            b = "".join(format(int(h, 16), "04b") for h in raw.strip())
            self.bits_reader = io.StringIO(b)

        return self.bits_reader

    def tell(self):
        return self.bits.tell()

    def read(self, n):
        b = self.bits.read(n)
        if b == "":
            raise Exception("EOF")

        #print(f"Read: {b}")
        return b

    def peek(self, n):
        pos = self.bits.tell()
        b = self.bits.read(n)
        self.bits.seek(pos)
        return b

    def peek_one(self):
        return self.peek(1)[0]

    def skip(self, n):
        self.bits.read(n)

class Field:
    def __post_init__(self):
        pass
        #print(self)

@dataclass
class Literal(Field):
    value: int

@dataclass
class Version(Field):
    value: int

@dataclass
class ID(Field):
    value: int

@dataclass
class Operator(Field):
    packets: list

@dataclass
class Header(Field):
    version: Version
    type_id: ID

@dataclass
class Packet(Field):
    header: Header
    literal: Optional[Literal] = None
    operator: Optional[Operator] = None

class Parser:

    def __init__(self, path):
        self.reader = Reader(path)

    def read_int(self, n):
        return int(self.reader.read(n), 2)

    def read_version(self):
        return Version(value=self.read_int(3))

    def read_id(self):
        return ID(value=self.read_int(3))

    def read_literal(self):
        number_b = ""
        last_flag = False
        while not last_flag:
            b = self.reader.read(1)
            last_flag = b == "0"
            number_b += self.reader.read(4)

        return Literal(value=int(number_b, 2))

    def read_header(self):
        return Header(
            version=self.read_version(),
            type_id=self.read_id()
        )

    def read_operator(self):
        packets = []
        if self.reader.read(1) == "0":
            bits_left = self.read_int(15)
            while bits_left > 0:
                pos = self.reader.tell()
                packets.append(self.read_packet())
                new_pos = self.reader.tell()
                bits_left -= new_pos - pos
                pos = new_pos
        else:
            packets_left = self.read_int(11)
            packets += [self.read_packet() for _ in range(packets_left)]

        return Operator(packets=packets)

    def read_packet(self):
        pos = self.reader.tell()
        packet = Packet(header=self.read_header())
        if packet.header.type_id.value == 4:
            packet.literal = self.read_literal()
        else:
            packet.operator = self.read_operator()

        return packet

    def parse(self):
        return self.read_packet()

def part_1(parser):
    tree = parser.parse()

    return count_versions(tree)

def count_versions(thingy):
    if thingy is None:
        return 0

    if isinstance(thingy, Operator):
        return sum(count_versions(p) for p in thingy.packets)

    if isinstance(thingy, Packet):
        v = thingy.header.version.value
        return v + count_versions(thingy.literal) + count_versions(thingy.operator)

    if isinstance(thingy, Literal):
        return 0

def part_2(parser):
    return eval_p(parser.parse())

def eval_p(thingy):
    if thingy.literal is not None:
        return thingy.literal.value

    ops = {
        0: sum_p,
        1: product_p,
        2: min_p,
        3: max_p,
        5: gt_p,
        6: lt_p,
        7: eq_p
    }

    return ops[thingy.header.type_id.value](thingy.operator.packets)

def sum_p(packets):
    return sum(eval_p(p) for p in packets)

def product_p(packets):
    return reduce(lambda a, b: a * b, [eval_p(p) for p in packets])

def min_p(packets):
    return min(eval_p(p) for p in packets)

def max_p(packets):
    return max(eval_p(p) for p in packets)

def gt_p(packets):
    return int(eval_p(packets[0]) > eval_p(packets[1]))

def lt_p(packets):
    return int(eval_p(packets[0]) < eval_p(packets[1]))

def eq_p(packets):
    return int(eval_p(packets[0]) == eval_p(packets[1]))

def main():
    print_solutions(
        ["resources/day16-test.txt", "resources/day16.txt"],
        #["resources/day16-test.txt"],
        Parser,
        part_1
    )

    print_solutions(
        ["resources/day16-test.txt", "resources/day16.txt"],
        Parser,
        part_2
    )

if __name__ == "__main__":
    main()
