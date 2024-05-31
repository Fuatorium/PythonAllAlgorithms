from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def scc_util(self, u, low, disc, stack_member, stack):
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stack_member[u] = True
        stack.append(u)

        for v in self.graph[u]:
            if disc[v] == -1:
                self.scc_util(v, low, disc, stack_member, stack)
                low[u] = min(low[u], low[v])
            elif stack_member[v]:
                low[u] = min(low[u], disc[v])

        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = stack.pop()
                print(w, end=' ')
                stack_member[w] = False
            print("")

    def scc(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stack_member = [False] * self.V
        stack = []
        for i in range(self.V):
            if disc[i] == -1:
                self.scc_util(i, low, disc, stack_member, stack)

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    g.scc()
