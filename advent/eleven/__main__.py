from typing import Tuple, Union

from advent.utils import filetostringlist
import numpy as np


def increment(matrix: np.array) -> np.array:
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            matrix = increment_axis(matrix, x, y)
    return matrix


def increment_axis(matrix: np.array, x: int, y: int) -> np.array:
    if x < 0 or x > 9 or y < 0 or y > 9:
        # print("Invalid matrix")
        return matrix
    try:
        matrix[y][x] += 1
    except IndexError:
        # print(f"Index error at {x}x{y}")
        return matrix
    return matrix


def check_for_pending_flash(matrix: np.array, flash_axis: set) -> np.array:
    new_flashers = set()
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if matrix[y][x] > 9 and (y, x) not in flash_axis:
                new_flashers.add((y, x))

    for (y, x) in new_flashers:
        matrix = increment_axis(matrix, x - 1, y)  # left
        matrix = increment_axis(matrix, x + 1, y)  # right
        matrix = increment_axis(matrix, x, y - 1)  # above
        matrix = increment_axis(matrix, x, y + 1)  # below
        matrix = increment_axis(matrix, x - 1, y + 1)  # bottomleft
        matrix = increment_axis(matrix, x + 1, y + 1)  # bottomright
        matrix = increment_axis(matrix, x - 1, y - 1)  # topleft
        matrix = increment_axis(matrix, x + 1, y - 1)  # topright

    flash_axis = set.union(new_flashers, flash_axis)
    return matrix, flash_axis


def reset(matrix: np.array, flash_axis: set) -> np.array:
    for (y, x) in flash_axis:
        matrix[y][x] = 0
    return matrix


def part_a(matrix_a: np.array, runs: int, break_on_sync: bool) -> int:
    flash_axis = set()
    flashes = 0
    for i in range(runs):
        with open(f"advent/eleven/debugging/{i+1}_in.txt", "w") as f:
            f.write(f"{matrix_a}")

        print(f"***** RUN {i+1} ****")
        flash_axis.clear()  # resetting the list of flashed octopussi
        matrix_a = increment(matrix_a)
        stable = False
        while not stable:
            flashes_count = len(flash_axis)
            matrix_a, flash_axis = check_for_pending_flash(matrix_a, flash_axis)
            stable = len(flash_axis) == flashes_count
        matrix_a = reset(matrix_a, flash_axis)
        flashes += len(flash_axis)
        with open(f"advent/eleven/debugging/{i+1}_out.txt", "w") as f:
            f.write(f"{matrix_a}")

        if break_on_sync and matrix_a.sum() == 0:
            return i
    return flashes


if __name__ == "__main__":
    inputList = filetostringlist("advent/eleven/input.txt")
    inputs = list(list(map(int, row)) for row in inputList)
    matrix_a = np.array(inputs)
    print(part_a(matrix_a, 100, False))
    print(part_a(matrix_a, 350, True))
