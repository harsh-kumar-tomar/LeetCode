
from typing import *


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    r = []
    candidates.sort()
    recursion(candidates,0 ,target,[],r)
    return r


def recursion(candidates:List[int],pointer:int , target:int , ls:List[int] , r:List[List[int]]):

    if target == 0:
        r.append(ls.copy())
        return

    if target < 0 or pointer == len(candidates) :
        return

    # choosing but  moving forward
    ls.append(candidates[pointer])
    recursion(candidates,pointer+1,target-candidates[pointer],ls ,r)
    ls.pop()

    # not choosing but moving forward
    recursion(candidates,pointer+1,target,ls,r)




a = combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
print(a)
