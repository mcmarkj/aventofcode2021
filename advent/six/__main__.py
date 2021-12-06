from advent.utils import filetostringlist
from typing import List


def increment_spawn(fish: List[int]) -> List[int]:
    new_fish = []
    baby_time = 8
    for i, age in enumerate(fish):
        if age == 0:
            fish[i] = 6
            new_fish.append(baby_time)
        else:
            fish[i] = age - 1

    for baby_fish in new_fish:
        fish.append(baby_fish)
    return fish


def generate_days(days: int, fish: List[int]) -> int:
    for i in range(days):
        increment_spawn(fish)
    return len(fish)


def optimised_generate_days(days: int, fish: List[int]) -> int:
    # I had no idea how to optimise my code, so thanks to
    # https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnfwy7r/?utm_source=share&utm_medium=web2x&context=3
    # for the inspiration
    agegroup = [0] * 9  ## 0-8 days old
    for swimmer in fish:
        agegroup[swimmer] += 1
        print(agegroup)
    for d in range(days):
        agegroup[(d + 7) % 9] += agegroup[d % 9]
    return sum(agegroup)


if __name__ == "__main__":
    inputList = filetostringlist("advent/six/input.txt")[0].split(",")
    fish = list(map(int, inputList))
    print(generate_days(80, fish))
    print(optimised_generate_days(256, fish))
