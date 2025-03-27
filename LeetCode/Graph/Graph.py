class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v, weight=1, directed=False):
        self.add_node(u)
        self.add_node(v)
        self.adj_list[u].append((v, weight))
        if not directed:
            self.adj_list[v].append((u, weight))

    def display(self):
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")

# Example Usage
g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("B", "C", 5)
g.add_edge("B", "D", 10)
g.add_edge("C", "D", 3)

g.display()
