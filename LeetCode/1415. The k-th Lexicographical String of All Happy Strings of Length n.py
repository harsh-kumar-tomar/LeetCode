from typing import *


def getHappyString(n: int, k: int) -> str:
    r = []
    recursion(["a", "b", "c"], "", n, r)
    return r[k-1] if k <= len(r) else ""


def recursion(choices: List[str], temp: str, n, r):
    if len(temp) == n:
        r.append(temp)
        return

    for choice in choices:
        if temp == "" or choice != temp[-1]:
            recursion(choices, temp + choice, n, r)


a = getHappyString(n = 1, k = 3)
print(a)
