from typing import *

def subsets(nums: List[int]) -> List[List[int]]:
    r = []
    s = set()
    for i in range(len(nums)):
        ls = []
        s= set()
        for j in range(len(nums)):
            if nums[j] not in s:
                ls.append(nums[j])
                s.add(nums[j])
                r.append(ls.copy())

    return r


a = subsets([1,2,3])
print(a)