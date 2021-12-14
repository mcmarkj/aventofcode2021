from typing import Tuple, Union

from advent.utils import filetostringlist
import numpy as np

FLASH_AXIS = set()


def increment(matrix: np.array) -> np.array:
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            matrix = increment_axis(matrix, x, y)
    return matrix


def increment_axis(matrix: np.array, x: int, y: int) -> np.array:
    try:
        matrix[x][y] += 1
    except IndexError:
        return matrix
    return matrix


def check_for_pending_flash(matrix: np.array) -> np.array:
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if matrix[x][y] > 9 and (x, y) not in FLASH_AXIS:
                FLASH_AXIS.add((x, y))
                matrix = increment_axis(matrix, x - 1, y)  # left
                matrix = increment_axis(matrix, x + 1, y)  # right
                matrix = increment_axis(matrix, x, y - 1)  # above
                matrix = increment_axis(matrix, x, y + 1)  # below
                matrix = increment_axis(matrix, x - 1, y + 1)  # bottomleft
                matrix = increment_axis(matrix, x + 1, y + 1)  # bottomright
                matrix = increment_axis(matrix, x - 1, y - 1)  # topleft
                matrix = increment_axis(matrix, x + 1, y - 1)  # topright
    return matrix


def reset(matrix: np.array) -> np.array:
    for coords in FLASH_AXIS:
        matrix[coords[0]][coords[1]] = 0
    return matrix


if __name__ == "__main__":
    inputList = filetostringlist("advent/eleven/test.txt")
    inputs = list(list(map(int, row)) for row in inputList)
    matrix_a = np.array(inputs)

    flashes = 0
    for i in range(100):
        with open(f"advent/eleven/debugging/{i+1}_in.txt", "w") as f:
            f.write(f"{matrix_a}")

        print(f"***** RUN {i+1} ****")
        flashes += len(FLASH_AXIS)
        FLASH_AXIS = set()  # resetting the list of flashed octopussi
        matrix_a = increment(matrix_a)
        stable = False
        while not stable:
            flashes_count = len(FLASH_AXIS)
            matrix_a = check_for_pending_flash(matrix_a)
            stable = len(FLASH_AXIS) == flashes_count
        print(FLASH_AXIS)
        matrix_a = reset(matrix_a)
        with open(f"advent/eleven/debugging/{i+1}_out.txt", "w") as f:
            f.write(f"{matrix_a}")
    print(flashes)
