from advent.utils import filetostringlist
from typing import List
from collections import Counter


def enumerate_list(inputList: List[str]) -> dict:
    elements = {}
    for line in inputList:
        for idx, val in enumerate(line):
            elements.setdefault(idx, [])
            elements[idx].append(val)
    return elements


def get_most_common(inputList: List[str], reverse: bool = False) -> str:
    elements = enumerate_list(inputList)
    binary = ""
    for idx in elements:
        counter = Counter(elements[idx])
        try:
            if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                binary += str(1)
                continue
        except IndexError:
            binary += str(counter.most_common(1)[0][0])
            continue
        binary += str(counter.most_common(1)[0][0])

    if reverse:
        return reverse_binary(binary)
    else:
        return binary


def reverse_binary(inputString: str) -> str:
    return inputString.replace("1", "2").replace("0", "1").replace("2", "0")


def life_support_rating(inputList: List[str], reverse: bool) -> str:
    newlist = inputList
    gammaRate = get_most_common(newlist, reverse)
    for i in range(len(gammaRate)):
        gammaRate = get_most_common(newlist, reverse)
        removals = []
        for row in newlist:
            if row[i] != gammaRate[i]:
                removals.append(row)
        for row in removals:
            newlist.remove(row)
        if len(newlist) == 1:
            return str(newlist[0])


def multiply(binarya: str, binaryb: str) -> int:
    return int(int(binarya, 2) * int(binaryb, 2))


def calculate(inputList: List[str]) -> int:
    gammaRate = get_most_common(inputList)
    epsilonRate = get_most_common(inputList, True)

    return multiply(gammaRate, epsilonRate)


if __name__ == "__main__":
    inputList = filetostringlist("advent/three/input.txt")
    print(calculate(inputList))

    oxygenRate = life_support_rating(filetostringlist("advent/three/input.txt"), False)
    cosRate = life_support_rating(filetostringlist("advent/three/input.txt"), True)
    print(multiply(oxygenRate, cosRate))
