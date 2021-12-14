from advent.utils import filetostringlist
import pandas


def find_lowpoints(df: pandas.DataFrame) -> int:

    lowpoints = []
    for y in range(df.shape[0]):  # iterate over rows
        for x in range(df.shape[1]):  # iterate over columns
            current = df[x][y]
            try:
                leftmost = df[x - 1][y]
            except:
                leftmost = 999
            try:
                rightmost = df[x + 1][y]
            except:
                rightmost = 999
            try:
                upmost = df[x][y - 1]
            except:
                upmost = 999
            try:
                downmost = df[x][y + 1]
            except:
                downmost = 999

            if (
                current < leftmost
                and current < downmost
                and current < rightmost
                and current < upmost
            ):
                lowpoints.append(current + 1)

    return sum(lowpoints)


def partb(df: pandas.DataFrame) -> int:
    for y in range(df.shape[0]):  # iterate over rows
        for x in range(df.shape[1]):  # iterate over columns
            basin(x, y, df)
    return 0


def basin(x: int, y: int, df: pandas.DataFrame) -> int:
    for y in range(df.shape[0]):  # iterate over rows
        for x in range(df.shape[1]):  # iterate over columns
            print(x, y)
    return 0


if __name__ == "__main__":
    inputList = filetostringlist("advent/nine/test.txt")
    df = pandas.DataFrame(
        list([int(a) for a in str(line)] for line in inputList), dtype=int
    )
    # print(find_lowpoints(df))
    print(partb(df))
