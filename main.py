import queue

graph = {
    1: [2, 5],
    2: [1, 5, 4, 3],
    3: [2, 4, 6],
    4: [2, 3, 5, 6],
    5: [1, 2, 4, 6],
    6: [5, 4, 3]
}

edges = [[1, 2], [1, 5], [5, 2], [2, 4], [5, 4], [2, 3], [4, 3], [5, 6], [6, 3], [4, 6]]


def bfs(startNode):
    visited = set()
    q = queue.Queue()
    q.put(startNode)

    while not q.empty():
        node = q.get()

        if node not in visited:
            visited.add(node)
            print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                q.put(neighbor)


def dfs(startNode):
    visited = set()
    stack = [startNode]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


bfs(1)
