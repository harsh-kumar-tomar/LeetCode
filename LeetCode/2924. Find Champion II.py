
from typing import *

def findChampion(n: int, edges: List[List[int]]) -> int:
    visited = [False]*n
    champion_team = -1

    for edge in edges:
        visited[edge[1]] = True

    for  i in range (n):
        if not visited[i]:
            if champion_team == -1:
                champion_team = i
            else:
                return -1

    return champion_team



a = findChampion( n = 3, edges = [[0,1],[1,2]])
print(a)