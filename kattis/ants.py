import sys
from typing import List


def shortest(plank_length: int, ants: List[int]) -> int:
    centre_position = plank_length / 2.0
    smallest_distance_to_center = min([abs(ant - centre_position) for ant in ants])
    return int(centre_position - smallest_distance_to_center)


def longest(plank_length: int, ants: List[int]) -> int:
    return int(max(max(ants), plank_length - min(ants)))


def parse_inputs():
    parts = [int(item) for line in sys.stdin for item in line.split()]
    cases = int(parts[0])
    i = 1
    for _ in range(cases):
        length = parts[i]
        num_ants = parts[i+1]
        yield length, [ant for ant in parts[i + 2:i + num_ants + 2]]
        i += 2 + num_ants


if __name__ == "__main__":
    cases = parse_inputs()
    for length, ant_positions in cases:
        print(shortest(length, ant_positions), longest(length, ant_positions))