from typing import List


def start(n: int, edges: List[List[int]]):

    graph = [[float('inf')] * n for _ in range(n)]
    distance = [[float('inf')] * n for _ in range(n)]
    s = set()

    for edge in edges:
        x, y, dist = edge[0], edge[1], edge[2]
        graph[x][y] = dist
        graph[y][x] = dist

    for i in range(n):
        s.add(i)
        recursion(graph[i],i,graph,distance,s)
        s.remove(i)



def recursion(start:List[int],currentPos:int,graph:List[List[int]],distance:List[List[int]],used:set[int],)

n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [3, 2, 1]]
start(n, edges)
