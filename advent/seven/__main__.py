from statistics import median, mean

from advent.utils import filetostringlist
from typing import List


def part_a(crabs: List[int]) -> int:
    crab_med = median(crabs)
    return int(sum(abs(pos - crab_med) for pos in crabs))


def part_b(crabs: List[int]):
    ymin = min(crabs)
    ymax = max(crabs)

    def cost(y, crabs):
        return int(sum([abs(y - xi) * (abs(y - xi) + 1) / 2 for xi in crabs]))

    fuel = []
    for y in range(ymin, ymax + 1):
        fuel.append(cost(y, crabs))

    print("y = {}, fuel = {}".format(fuel.index(min(fuel)), min(fuel)))


if __name__ == "__main__":
    inputList = filetostringlist("advent/seven/input.txt")[0].split(",")
    crabs = list(map(int, inputList))
    print(part_a(crabs))
    print(part_b(crabs))
