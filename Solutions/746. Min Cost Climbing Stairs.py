from typing import *


def minCostClimbingStairs(cost: List[int]) -> int:
    r = [1001]
    dp:Dict[Tuple[int,int],int] = {}

    recursion(cost, 0, 0, r,dp)
    recursion(cost, 1, 0, r,dp)

    return r[0]


def recursion(cost: List[int], currentPos: int, tempCost: int, r: List[int] , dp:Dict[Tuple[int,int],int]):

    if currentPos >= len(cost):
        r[0] = min(r[0],tempCost)
        return tempCost


    if (currentPos,tempCost+cost[currentPos]) not in dp:
        # choose and jump one time
        a = recursion(cost, currentPos + 1, tempCost + cost[currentPos], r,dp)
        #choose and jump two time
        b = recursion(cost, currentPos + 2, tempCost+cost[currentPos], r,dp)
        dp[(currentPos,tempCost)] = min(a,b)
        return min(a,b)
    else:
        return dp[(currentPos,tempCost)]

a = minCostClimbingStairs( cost = [1,100,1,1,1,100,1,1,100,1])
print(a)
