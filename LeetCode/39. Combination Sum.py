from typing import *


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    r = []
    recursion(candidates,0 ,target,[],r)
    return r


def recursion(candidates:List[int],pointer:int , target:int , ls:List[int] , r:List[List[int]]):

    if target == 0:
        r.append(ls.copy())
        return

    if target < 0 or pointer == len(candidates) :
        return

    # choosing but not moving forward
    ls.append(candidates[pointer])
    recursion(candidates,pointer,target-candidates[pointer],ls ,r)
    ls.pop()

    # not choosing but moving forward
    recursion(candidates,pointer+1,target,ls,r)




a = combinationSum(candidates = [2,3,5], target = 8)
print(a)

# old code
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         r = []
#         self.sum(candidates, target, len(candidates), [], r)
#         return r
#
#     def sum(self, candidates, target, n, ls, r):
#         if n <= 0 or target < 0:
#             return
#
#         if target == 0:
#             r.append(ls.copy())
#             return
#
#         ls.append(candidates[n - 1])
#         self.sum(candidates, target - candidates[n - 1], n, ls, r)
#         ls.pop()
#         self.sum(candidates, target, n - 1, ls, r)