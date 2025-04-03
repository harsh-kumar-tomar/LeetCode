from typing import List


def maximumTripletValue(nums: List[int]) -> int:
    s = 0
    n = len(nums)

    for i in range(n):
        for j in range( i +1 ,n):
            for k in range( j +1 ,n):
                s = max(s ,(nums[i] -nums[j]) *nums[k])

    return s

a = maximumTripletValue(nums = [12,6,1,2,7])
print(a)