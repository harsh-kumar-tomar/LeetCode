
from typing import *

def findSmallestSetOfVertices( n: int, edges: List[List[int]]) -> List[int]:
    visited = [False]*n
    ls = []

    for edge in edges:
        visited[edge[1]] = True


    for i  in range(n):
        if not visited[i]:
            ls.append(i)

    return ls


a = findSmallestSetOfVertices(n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]])
print(a)