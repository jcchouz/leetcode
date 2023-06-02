from typing import List


def setup(paiban: List[int]):
    def backtrace(index: int):
        if len(path) == len(paiban):
            res.append(path.copy())
            return
        for i in range(index, len(paiban)):
            path.append(paiban[i])
            backtrace(i + 1)
            path.pop()

    res = list()
    path = list()
    backtrace(0)
    return res
