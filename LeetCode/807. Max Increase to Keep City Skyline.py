

from typing import List
import heapq

def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:

    s = sum(el for row in grid for el in row)

    horizontal = [max(row)for row in grid]    
    vertical = [max(col) for col in zip(*grid)]

    for i in range(len(grid)):
        for j in range (len(grid[0])):
            grid[i][j] = min(horizontal[i],vertical[j])

    temp = sum(el for row in grid for el in row)

    return temp-s
    

a = maxIncreaseKeepingSkyline( grid = [[0,0,0],[0,0,0],[0,0,0]])
print(a)

