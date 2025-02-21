from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    ls = [i for i in range(1, n + 1)]
    r = []

    recursion(ls, k, 0, [], r)
    return r


def recursion(ls: List[int], k: int, currentPointer: int, tempList: List[int], r: List[List[int]]):
    if len(tempList) == k:
        r.append(tempList.copy())
        return

    if currentPointer == len(ls):
        return

    # choose
    tempList.append(ls[currentPointer])
    recursion(ls, k, currentPointer + 1, tempList, r)
    tempList.pop()

    # note choose
    recursion(ls, k, currentPointer + 1, tempList, r)


a = combine(n=1, k=1)
print(a)
