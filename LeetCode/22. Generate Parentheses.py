from typing import *


def generateParenthesis(n: int) -> List[str]:
    r = []
    recursiveCall(n, n, "", r)
    return r


def recursiveCall(leftCount, rightCount, temp, r: List[int]):
    if rightCount == leftCount == 0:
        r.append(temp)
        return

    if leftCount != 0:
        recursiveCall(leftCount - 1, rightCount, temp + "(", r)

    if rightCount > leftCount :
        recursiveCall(leftCount, rightCount - 1, temp + ")", r)




a = generateParenthesis(1)
print(a)
