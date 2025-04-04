from typing import *


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [-1]*(n+1)

    dp[0] = cost[0]
    dp[1] = min(cost[0],cost[1])
    cost.append(0)

    for i in range(2,n+1):
        dp[i] = min(cost[i]+dp[i-1],cost[i]+dp[i-2])

    return min(dp[n-1],dp[n-2])


a = minCostClimbingStairs( cost = [10,15,20])
print(a)











#
#
# def minCostClimbingStairs(self, cost: List[int]) -> int:
#     r = [1001]
#     dp: Dict[Tuple[int, int], int] = {}
#
#     self.recursion(cost, 0, 0, r, dp)
#     self.recursion(cost, 1, 0, r, dp)
#
#     return r[0]
#
#
# def recursion(self, cost: List[int], currentPos: int, tempCost: int, r: List[int], dp: Dict[Tuple[int, int], int]):
#     if currentPos >= len(cost):
#         r[0] = min(r[0], tempCost)
#         return tempCost
#
#     if (currentPos, tempCost + cost[currentPos]) not in dp:
#         # choose and jump one time
#         a = self.recursion(cost, currentPos + 1, tempCost + cost[currentPos], r, dp)
#         # choose and jump two time
#         b = self.recursion(cost, currentPos + 2, tempCost + cost[currentPos], r, dp)
#         dp[(currentPos, tempCost)] = min(a, b)
#         return min(a, b)
#     else:
#         return dp[(currentPos, tempCost)]
#
