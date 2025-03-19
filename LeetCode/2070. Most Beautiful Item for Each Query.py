from typing import *


def maximumBeauty(items: List[List[int]], queries: List[int]) -> List[int]:
    pair = {}
    arr = []
    r = []
    for item in items:
        price, beauty = item
        if price not in pair:
            pair[price] = beauty
            arr.append(price)
        else:
            pair[price] = max(pair[price], beauty)

    arr.sort()
    max_value = -1
    for value in arr:
        max_value = max(max_value, pair[value])
        pair[value] = max_value

    for query in queries:
        val = binarySearch(arr, query)
        if val == -1:
            r.append(0)
        else:
            r.append(pair[val])

    return r


def binarySearch(arr: List[int], target: int) -> int:
    n = len(arr)
    start = 0
    end = n - 1
    mid = 0

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    if arr[mid] < target:
        return arr[mid]
    elif arr[mid - 1] < target:
        return arr[mid - 1]
    else:
        return -1


a = maximumBeauty(items=[[10, 1000]], queries=[5])
print(a)
