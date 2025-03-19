from typing import *


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    visited = [False] * len(graph)
    visited[0] = True
    r = []
    traverse(0, len(graph) - 1, visited, graph, [0], r)
    return r


def traverse(start: int, destination: int, visited: List[bool], graph: List[List[int]], tempList: List[int],
             r: List[List[int]]):
    if start == destination:
        r.append(tempList.copy())
        return

    nodes_connected = graph[start]

    for node in nodes_connected:
        if not visited[node]:
            visited[node] = True
            tempList.append(node)
            traverse(node, destination, visited, graph,tempList,r)
            tempList.pop()
            visited[node] = False


a = allPathsSourceTarget(graph = [[1,2],[3],[3],[]])
print(a)