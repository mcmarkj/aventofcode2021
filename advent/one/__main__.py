from advent.utils import filetodpdataframe
import pandas


def parta(input: pandas.DataFrame) -> int:
    diff_array = input.diff()
    negative_values = sum(n > 0 for n in diff_array.values)
    return negative_values

def partb(input: pandas.DataFrame) -> int:
    rolling_array = input.rolling(3).sum().diff()
    negative_values = sum(n > 0 for n in rolling_array.values)
    return negative_values


if __name__ == "__main__":
    input = filetodpdataframe("advent/one/input.txt")
    print(parta(input))
    print(partb(input))