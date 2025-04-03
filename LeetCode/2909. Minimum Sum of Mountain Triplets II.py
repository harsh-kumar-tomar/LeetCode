from collections import deque
from typing import List


def minimumSum(nums: List[int]) -> int:

    n = len(nums)
    min_left = [nums[0]]
    min_right = deque([nums[-1]])
    s = float('inf')

    for i in range(1,n):
        min_left.append(min(min_left[-1],nums[i]))


    for i in range(n-2,-1,-1):
        min_right.appendleft(min(min_right[0],nums[i]))

    print(min_right,min_left)

    for i in range(1,n-1):
        if min_left[i-1] < nums[i] and min_right[i+1] < nums[i]:
            s = min(s,min_left[i-1]+nums[i]+min_right[i+1])

    return s if s != float('inf') else -1


a = minimumSum(nums = [8,6,1,5,3])
print(a)