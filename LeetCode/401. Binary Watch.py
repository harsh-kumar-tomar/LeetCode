from typing import *


def readBinaryWatch(turnedOn: int) -> List[str]:
    r = []
    recursion([False] * 10, 0, turnedOn, r)
    return r


def recursion(space: List[bool], currentPointer: int, lightsAvailable: int, r: List[str]):
    if lightsAvailable == 0:
        hr = calculateHour(space)
        min = calculateTime(space)
        if hr < 12 and min < 60:
            r.append( str(hr) + ":" + (f"0{min}" if min < 10 else f"{min}"))
        return

    if currentPointer == len(space):
        return

    space[currentPointer] = True
    recursion(space, currentPointer + 1, lightsAvailable - 1, r)
    space[currentPointer] = False

    recursion(space, currentPointer + 1, lightsAvailable, r)


def calculateHour(space: List[bool]) -> int:
    multiplier = 1
    hour = 0
    for i in range(3, -1, -1):
        if space[i]:
            hour += multiplier

        multiplier *= 2

    return hour


def calculateTime(space: List[bool]) -> int:
    minute = 0
    multiplier = 1

    for i in range(len(space) - 1, 3, -1):
        if space[i]:
            minute += multiplier

        multiplier *= 2

    return minute


a = readBinaryWatch(turnedOn=1)
print(a)
