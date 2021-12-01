from typing import List
from pandas import DataFrame


def filetostringlist(filename: str) -> List[str]:
    with open(filename) as f:
        input = [line.rstrip() for line in f]
        return input


def filetointlist(filename: str) -> List[int]:
    with open(filename) as f:
        input = [int(line.rstrip()) for line in f]
        return input


def filetodpdataframe(filename: str) -> DataFrame:
    data = filetointlist(filename)
    df = DataFrame(data)
    return df
