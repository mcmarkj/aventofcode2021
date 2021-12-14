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
        if flash:
            print(x, y)
        # print(f"incrementing {x} {y}")
        matrix[x][y] += 1
    except IndexError:
        print(f"Index error at {x} {y}")
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


def flash(matrix: np.array, flashes: int) -> Tuple[int, np.array]:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("NEW RUN")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    flash_count = flashes
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            value = matrix[x][y]
            if value > 9:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"~~~~~ Flash Found at {x}x{y} Before ~~~~~")
                print(matrix)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                matrix = increment_axis(matrix, x, y)  # itself
                matrix = increment_axis(matrix, x - 1, y)  # left
                matrix = increment_axis(matrix, x + 1, y)  # right
                matrix = increment_axis(matrix, x, y - 1)  # above
                matrix = increment_axis(matrix, x, y + 1)  # below
                matrix = increment_axis(matrix, x - 1, y + 1)  # bottomleft
                matrix = increment_axis(matrix, x + 1, y + 1)  # bottomright
                matrix = increment_axis(matrix, x - 1, y - 1)  # topleft
                matrix = increment_axis(matrix, x + 1, y - 1, True)  # topright
                print("~~~~~ Flash Found After ~~~~~")
                print(matrix)
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            value = matrix[x][y]
            if value > 9:
                flash_count += 1

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
        if determine_flash(matrix_a):
            # print("***** FLASHING ****")
            # print(matrix_a)
            flashes, matrix_a = flash(matrix_a, flashes)
            matrix_a = reset(matrix_a)
        print(matrix_a)
        # print(flashes)
        with open(f"advent/eleven/debugging/{i+1}_out.txt", "w") as f:
            f.write(f"{matrix_a}")
    print(flashes)
