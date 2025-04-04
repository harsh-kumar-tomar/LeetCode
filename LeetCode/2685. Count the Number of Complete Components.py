from typing import List


def traverse(v, visited,graph):

    for vertex in graph[v]:
        if not visited:
            visited = True
            traverse(vertex,visited,graph)
            visited = False



def countCompleteComponents(n: int, edges: List[List[int]]) -> int:
    graph = {}
    vertex = set()

    for edge in edges:
        x, y = edge
        graph[x] = graph.setdefault(x, []).append(y)
        graph[y] = graph.setdefault(y, []).append(x)
        vertex.add(x)
        vertex.add(y)

    visited = [False]*len(vertex)


    for v in range(0, len(vertex)):
        traverse(v,visited)


a = countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]])
