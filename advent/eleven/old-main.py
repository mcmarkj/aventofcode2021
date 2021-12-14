from typing import Tuple, Union

from advent.utils import filetostringlist
import numpy as np


def increment(matrix: np.array) -> np.array:
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            matrix = increment_axis(matrix, x, y)
    return matrix


def increment_axis(matrix: np.array, x: int, y: int, flash: bool = False) -> np.array:
    try:
        matrix[x][y] += 1
    except IndexError:
        return matrix
    return matrix


def determine_flash(matrix: np.array) -> bool:
    if np.count_nonzero(matrix > 9) != 0:
        return True
    return False


def reset(matrix: np.array) -> np.array:
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if matrix[x][y] > 9:
                matrix[x][y] = 0
    return matrix


def increment_around(
    matrix: np.array, x: int, y: int, existing_flashes: list, flash_count: int
):
    matrix = increment_axis(matrix, x - 1, y)  # left
    matrix, existing_flashes, flash_count = count_flashes(
        matrix, existing_flashes, flash_count, x - 1, y
    )
    matrix = increment_axis(matrix, x + 1, y)  # right
    matrix, existing_flashes, flash_count = count_flashes(
        matrix, existing_flashes, flash_count, x + 1, y
    )
    matrix = increment_axis(matrix, x, y - 1)  # above
    matrix, existing_flashes, flash_count = count_flashes(
        matrix, existing_flashes, flash_count, x, y - 1
    )
    matrix = increment_axis(matrix, x, y + 1)  # below
    matrix, existing_flashes, flash_count = count_flashes(
        matrix, existing_flashes, flash_count, x, y + 1
    )
    matrix = increment_axis(matrix, x - 1, y + 1)  # bottomleft
    matrix, existing_flashes, flash_count = count_flashes(
        matrix, existing_flashes, flash_count, x - 1, y + 1
    )
    matrix = increment_axis(matrix, x + 1, y + 1)  # bottomright
    matrix, existing_flashes, flash_count = count_flashes(
        matrix, existing_flashes, flash_count, x + 1, y + 1
    )
    matrix = increment_axis(matrix, x - 1, y - 1)  # topleft
    matrix, existing_flashes, flash_count = count_flashes(
        matrix, existing_flashes, flash_count, x - 1, y - 1
    )
    matrix = increment_axis(matrix, x + 1, y - 1)  # topright
    matrix, existing_flashes, flash_count = count_flashes(
        matrix, existing_flashes, flash_count, x + 1, y - 1
    )
    return matrix, existing_flashes, flash_count


def count_flashes(
    matrix: np.array, existing_flashes: list, flash_count: int, x: int, y: int
) -> Tuple[np.array, list, int]:
    try:
        value = matrix[x][y]
        if value > 9:
            if [x, y] not in existing_flashes:
                flash_count += 1
                existing_flashes.append([x, y])
                matrix[x][y] = 0
            else:
                matrix[x][y] = 0
                print(existing_flashes)
        return matrix, existing_flashes, flash_count
    except IndexError:
        return matrix, existing_flashes, flash_count


def flash(matrix: np.array, flashes: int) -> Tuple[int, np.array]:
    existing_flashes = []
    flash_count = flashes
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            value = matrix[x][y]
            if value > 9:
                print(f"~~~~~ Flash Found at {x}x{y} ~~~~~")
                matrix, existing_flashes, flash_count = count_flashes(
                    matrix, existing_flashes, flash_count, x, y
                )
                matrix, existing_flashes, flash_count = increment_around(
                    matrix, x, y, existing_flashes, flash_count
                )

    return flash_count, matrix


if __name__ == "__main__":
    inputList = filetostringlist("advent/eleven/test.txt")
    inputs = list(list(map(int, row)) for row in inputList)
    matrix_a = np.array(inputs)

    flashes = 0
    for i in range(100):
        with open(f"advent/eleven/debugging/{i+1}_in.txt", "w") as f:
            f.write(f"{matrix_a}")
        print(f"***** RUN {i+1} ****")
        matrix_a = increment(matrix_a)
        while determine_flash(matrix_a):
            flashes, matrix_a = flash(matrix_a, flashes)
        with open(f"advent/eleven/debugging/{i+1}_out.txt", "w") as f:
            f.write(f"{matrix_a}")
    print(flashes)
