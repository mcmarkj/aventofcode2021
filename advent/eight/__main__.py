from advent.utils import filetostringlist
from typing import List

OPTIONS = {
    "abcefg": 0,  # 5
    "cf": 1,  # 2
    "acdeg": 2,  # 5
    "acdfg": 3,  # 5
    "bcdf": 4,  # 4
    "abdfg": 5,  # 5
    "abdefg": 6,  # 6
    "acf": 7,  # 3
    "abcdefg": 8,  # 8
    "abcdfg": 9,  # 7
}


class Input:
    def __init__(self, line: str):
        self.line = line
        self.displays = []
        self.output = []
        self.unique_count = 0
        self.didgets = {}

    def split(self):
        tmp = self.line.split(" ")
        self.displays = tmp[:10]
        self.output = tmp[-4:]

    def find_uniques(self) -> int:
        unique_vals = {2, 4, 7, 3}
        for output in self.output:
            if len(output) in unique_vals:
                self.unique_count += 1
        return self.unique_count

    def determine_segments(self):
        for displays in self.displays:
            length = len(displays)
            if length == 2:
                self.didgets[1] = displays
            elif length == 3:
                self.didgets[7] = displays
            elif length == 4:
                self.didgets[4] = displays
            elif length == 7:
                self.didgets[8] = displays
        for displays in self.displays:
            length = len(displays)
            if length == 5:
                if self.get_diff(self.didgets[1], displays) == 3:
                    self.didgets[3] = displays
                elif self.get_diff(self.didgets[4], displays) == 3:
                    self.didgets[5] = displays
                else:
                    self.didgets[2] = displays
            elif length == 6:
                if self.get_same(self.didgets[1], displays) == 1:
                    self.didgets[6] = displays
                elif self.get_same(self.didgets[4], displays) == 4:
                    self.didgets[9] = displays
                else:
                    self.didgets[0] = displays

    def determine_display(self):
        for didget in self.didgets:
            print(didget, self.didgets[didget])
        for output in self.output:
            print(output)

    @staticmethod
    def get_diff(first, second):
        first_set, second_set = set(first), set(second)
        return len((first_set | second_set) - (first_set & second_set))

    @staticmethod
    def get_same(first, second):
        first_set, second_set = set(first), set(second)
        return len(first_set & second_set)


def part_a(input: List[str]) -> int:
    total = 0
    for line in input:
        row = Input(line)
        row.split()
        total += row.find_uniques()
    return total


def part_b(input: List[str]):
    for line in input:
        row = Input(line)
        row.split()
        row.determine_segments()
        row.determine_display()


if __name__ == "__main__":
    inputList = filetostringlist("advent/eight/test.txt")
    print(part_a(inputList))
    # print(part_b(inputList))
    # I couldn't find a solution to part b without crying so I've gave up.
