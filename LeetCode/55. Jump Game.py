
from typing import *

def canJump(nums: List[int]) -> bool:
    nums.reverse()
    countZero = 0

    for i in nums:
        if i > countZero:
            countZero = 0
        else:
            countZero += 1

    return True if countZero == 0 else False

a = canJump([2,0])
print(a)

