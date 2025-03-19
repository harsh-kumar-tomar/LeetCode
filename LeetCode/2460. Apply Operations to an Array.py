
from typing import *

def applyOperations(nums: List[int]) -> List[int]:

    n = len(nums)

    for i in range (n-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0

    tempNum = []

    for el in nums:
        if el != 0:
            tempNum.append(el)

    tempNum = tempNum + [0]*(len(nums)-len(tempNum))

    return tempNum







a = applyOperations(nums = [1,2,2,1,1,0])
print(a)