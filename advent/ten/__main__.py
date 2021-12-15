from advent.utils import filetostringlist
import pandas
from typing import List

SCORES = {
    "(": 3,
    "[": 57,
    "{": 1197,
    "<": 25137,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def part_a(inputList: List[str]) -> int:
    t = 0
    for row in inputList:
        pos = [0]
        for e in row:
            if e in ("}", ")", ">", "]"):
                if pos[-1] == SCORES[e]:
                    pos.pop(-1)
                else:
                    t += SCORES[e]
                    break
            else:
                pos.append(SCORES[e])
    return t


if __name__ == "__main__":
    inputList = filetostringlist("advent/ten/input.txt")
    print(part_a(inputList))
