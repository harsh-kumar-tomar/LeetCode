import heapq
import math

temp = [["A", "D", 4], ["A", "E", 4], ["D", "E", 2], ["A", "C", 3], ["E", "C", 4], ["C", "F", 5], ["C", "B", 2],
         ["B", "F", 2], ["C", "G", 5], ["G", "F", 5], ["E", "G", 5]]
n = 11
edges = {}

for edge in temp:
    s, e, w = edge
    edges[(s, e)] = w
    edges[(e, s)] = w

heap = []

vertex_weight = {"A": math.inf, "B": math.inf, "C": math.inf, "D": 0, "E": math.inf, "F": math.inf}
visited = {"A": False, "B": False, "C": False, "D": 0, "E": False, "F": False}


heap.append((0, "D"))
heapq.heapify(heap)

while heap:

    weight,vertex = heapq.heappop(heap)

    for i in range(n):
        if (vertex,i) in edges and  not visited[i]:
            weight[i] = min(weight[i],weight[v]+graph[v][i])
            heap.append((weight[i],i))
