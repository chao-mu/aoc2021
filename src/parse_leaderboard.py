#!/usr/bin/env python3

import json

from dataclasses import dataclass

@dataclass
class Challenge:
    member: str
    part: int
    day: int
    time: int
    member_id: int

    def __lt__(self, other):
        return str(self) < str(other)

    def __str__(self):
        return ",".join(x.lower() for x in self.to_tuple())

    def to_tuple(self):
        return tuple((str(f).zfill(2) for f in [self.member, self.day, self.part, self.time]))

def main():
    with open("resources/leader_board.json") as f:
        data = json.load(f)

    challenges = []
    for member_id, member_data in data["members"].items():
        member = member_data["name"]
        for day, day_data in member_data["completion_day_level"].items():
            for part, part_data in day_data.items():
                c = Challenge(member=member, member_id=member_id, day=day, part=part, time=part_data["get_star_ts"])
                challenges.append(c)


    for c in sorted(challenges):
        print(c)

if __name__ == "__main__":
    main()
