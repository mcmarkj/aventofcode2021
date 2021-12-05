import numpy

from advent.utils import filetostringlist
from typing import List


def increment_coords(coord: List[List[int]], matrix: numpy.array) -> numpy.array:
    for row in coord:
        matrix[row[1]][row[0]] += 1
    return matrix


def split_input(line: str) -> List[List[str]]:
    return list(line.split(",") for line in line.split(" -> "))


def tidy_coords(coord: List[str]) -> List[List[int]]:
    x1 = int(coord[0][0])
    x2 = int(coord[1][0])
    y1 = int(coord[0][1])
    y2 = int(coord[1][1])
    lowerx = min(x1, x2)
    lowery = min(y1, y2)
    upperx = max(x1, x2)
    uppery = max(y1, y2)

    final = []
    for x in range(lowerx, upperx + 1):
        for y in range(lowery, uppery + 1):
            final.append([x, y])
    return final


def parta(matrix: numpy.array, coords: List) -> int:
    newmatrix = matrix
    for row in coords:
        if row[0][0] == row[1][0] or row[0][1] == row[1][1]:
            newmatrix = increment_coords(tidy_coords(row), newmatrix)
    return (newmatrix >= 2).sum()


def partb(matrix: numpy.array, coords: List) -> int:
    ### Got stuck on this, thanks to https://gist.github.com/Surye/55a566bebb7fc3b3481a3a3595218a71 via Reddit for help
    newmatrix = matrix
    for row in coords:
        x1, x2, y1, y2 = int(row[0][0]), int(row[1][0]), int(row[0][1]), int(row[1][1])
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                newmatrix[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                newmatrix[(x, y1)] += 1
        else:
            x_mod = -1 if x1 > x2 else 1
            y_mod = -1 if y1 > y2 else 1
            for x, y in zip(range(x1, x2 + x_mod, x_mod), range(y1, y2 + y_mod, y_mod)):
                newmatrix[(x, y)] += 1

    return (newmatrix >= 2).sum()


if __name__ == "__main__":
    inputList = filetostringlist("advent/five/input.txt")
    coords = list(split_input(row) for row in inputList)
    matrix = numpy.zeros((999, 999), dtype=numpy.int8)
    print(parta(matrix, coords))
    matrix = numpy.zeros((999, 999), dtype=numpy.int8)
    print(partb(matrix, coords))
