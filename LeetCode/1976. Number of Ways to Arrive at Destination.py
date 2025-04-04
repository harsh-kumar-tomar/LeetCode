from typing import List


def countPaths(n: int, roads: List[List[int]]) -> int:
    graph = [[0] * n for _ in range(n)]

    for road in roads:
        start, end, time = road
        graph[start][end] = time
        graph[end][start] = time

    visited = [False] * n
    visited[0] = True
    ways = [0]
    traverse(currentNode=0, destinationNode=n - 1, tempMinTime=0, minTime=[float('inf')], ways=ways, visited=visited,graph=graph)

    return ways[0] % (10 ** 7 + 7)


def traverse(currentNode: int, destinationNode: int, tempMinTime: int, minTime: List[int], ways: List[int],  visited: List[bool], graph: List[List[int]]):

    if currentNode == destinationNode:
        if tempMinTime < minTime[0]:
            minTime[0] = tempMinTime
            ways[0] = 1
        elif tempMinTime == minTime[0]:
            ways[0] += 1
        return

    n = len(visited)
    for node in range(0, n):
        if not visited[node] and graph[currentNode][node] != 0:
            visited[node] = True
            traverse(node, destinationNode, tempMinTime + graph[currentNode][node], minTime, ways, visited, graph)
            visited[node] = False


a = countPaths(n = 2, roads = [[1,0,10]])
print(a)
