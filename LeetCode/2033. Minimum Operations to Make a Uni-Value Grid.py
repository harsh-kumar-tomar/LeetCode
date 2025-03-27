from typing import List


def minOperations(grid: List[List[int]], x: int) -> int:
    linear_arr = [i for row in grid for i in row]
    linear_arr.sort()

    remainder = linear_arr[0]%x

    for i in linear_arr:
        if i%x != remainder:
            return -1

    median = linear_arr[len(linear_arr)//2]

    r = 0

    for i in linear_arr:
        r += abs(i-median)//x

    return r

a = minOperations( grid = [[1,5],[2,3]], x = 1)
print(a)