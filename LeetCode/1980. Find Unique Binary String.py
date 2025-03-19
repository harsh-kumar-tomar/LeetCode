
from typing import *

def findDifferentBinaryString(nums: List[str]) -> str:
    n = len(nums)
    r = []
    recursion(n,"",r)
    nums.sort()
    r.sort()
    print(nums,r)

    for i in range (len(r)):
        if r[i] != nums[i]:
            return r[i]

    return r[len(nums)]

def recursion(n:int,tempString:str,r:List[str]):
    if n == 0:
        r.append(tempString)
        return

    recursion(n-1,tempString+"0",r)
    recursion(n-1,tempString+"1",r)




a = findDifferentBinaryString(nums = ["111","011","001"])
print(a)


# Alternate solution

# ls = []
#
# for i in range(len(nums)):
#     if nums[i][i] == "0"
#         ls.append("1")
#     else:
#         ls.append("0")
#
# return "".join(ls)