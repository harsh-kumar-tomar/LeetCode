from typing import List


def minimumOperations(nums: List[int]) -> int:

    s = set([i  for i in nums if i != 0 ])
    return len(s)

a = minimumOperations(nums = [1,5,0,3,5])
print(a)