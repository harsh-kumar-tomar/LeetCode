from typing import *
import heapq


def eliminateMaximum(dist: List[int], speed: List[int]) -> int:
    n = len(dist)
    time = []
    counter = 0
    monstersCount = 0

    for i in range(n):
        heapq.heappush(time, dist[i] // speed[i])

    while time:
        tempTime = heapq.heappop(time) - counter
        if tempTime == 0:
            return monstersCount if counter != 0 else 1
        monstersCount += 1
        counter += 1

    return monstersCount

a = eliminateMaximum(dist = [3,2,4], speed = [5,3,2])
print(a)