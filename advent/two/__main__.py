from advent.utils import filetostringlist
from typing import List
import numpy

INSTRUCTIONS = {
    "down": numpy.array([0, 1]),
    "up": numpy.array([0, -1]),
    "forward": numpy.array([1, 0]),
}


def generate_routedata(data: List[str]) -> numpy.array:
    route = []
    for instruction in data:
        step, op = instruction.split()[0], instruction.split()[1]
        route.append((INSTRUCTIONS[step] * int(op)))
    return route


def part_a(route: numpy.array) -> int:
    result = numpy.prod(numpy.sum(route, axis=0))
    return int(result)


def part_b(route: numpy.array) -> int:
    position = numpy.array([0, 0, 0])
    for action in route:
        position = position + [action[0], action[0] * position[2], action[1]]
    return int(position[0] * position[1])


if __name__ == "__main__":
    input = filetostringlist("advent/two/input.txt")
    route = generate_routedata(input)
    print(part_a(route))
    print(part_b(route))
