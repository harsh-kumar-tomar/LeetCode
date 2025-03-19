

from typing import *


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    distanceBetween = {}
    graph = {}
    used = [False]*n
    r = {}

    for edge in edges:
        distanceBetween[(edge[0],edge[1])] = edge[2]
        distanceBetween[(edge[1],edge[0])] = edge[2]


        graph.setdefault(edge[0],[]).append(edge[1])
        graph.setdefault(edge[1],[]).append(edge[0])

    for i in range(n):
        used[i] = True
        ls = []
        traverse(i,graph,distanceBetween,distanceThreshold,used,ls)
        r[i] = ls
        used[i] = False

    print(r)

    minLength = float('inf')
    minIndex = []

    for index,l in r.items():
        if minLength > len(l):
            minLength = len(l)
            minIndex.append(index)

    return minIndex[0]



def traverse (sourceNode:int , graph:Dict[int,List[int]],distanceBetween:Dict[Tuple[int,int],int],distanceThreshold:int,used:List[bool],tempList:List[int]):

    if distanceThreshold < 0:
        return

    for i in graph[sourceNode]:
        if not used[i] and distanceThreshold-distanceBetween[sourceNode,i] >= 0:
            used[i] = True
            tempList.append(i)
            traverse(i,graph,distanceBetween,distanceThreshold-distanceBetween[sourceNode,i],used,tempList)
            tempList.pop()
            used[i] = False








a = findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)
print(a)