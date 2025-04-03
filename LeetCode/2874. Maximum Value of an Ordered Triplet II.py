from collections import deque
from typing import List


def maximumTripletValue(nums: List[int]) -> int:
    n = len(nums)
    max_left = [nums[0]]
    max_right = deque([nums[-1]])
    s = 0

    for i in range(1, n):
        max_left.append(max(max_left[-1], nums[i]))

    for i in range(n-2, -1,-1):
        max_right.appendleft(max(max_right[-1], nums[i]))


    for i in range(1,n-1):
        s = max(s,(max_left[i-1]-nums[i])*max_right[i+1])

    return s


a = maximumTripletValue(nums=[12, 6, 1, 2, 7])
print(a)
