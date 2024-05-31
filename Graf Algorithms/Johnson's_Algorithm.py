from collections import defaultdict
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def bellman_ford(self, src):
        dist = [float("Inf")] * (self.V + 1)
        dist[src] = 0
        for i in range(self.V):
            for u in range(self.V + 1):
                for v, w in self.graph[u]:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        for u in range(self.V + 1):
            for v, w in self.graph[u]:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    print("Graph contains negative weight cycle")
                    return None
        return dist

    def dijkstra(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        pq = set()
        pq.add((0, src))
        while pq:
            (d, u) = pq.pop()
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    if (dist[v], v) in pq:
                        pq.remove((dist[v], v))
                    dist[v] = dist[u] + w
                    pq.add((dist[v], v))
        return dist

    def johnson(self):
        self.graph[self.V] = [(i, 0) for i in range(self.V)]
        h = self.bellman_ford(self.V)
        if h is None:
            return
        del self.graph[self.V]
        for u in range(self.V):
            for i in range(len(self.graph[u])):
                v, w = self.graph[u][i]
                self.graph[u][i] = (v, w + h[u] - h[v])
        dist = []
        for u in range(self.V):
            dist.append(self.dijkstra(u))
        for u in range(self.V):
            for v in range(self.V):
                dist[u][v] += h[v] - h[u]
        print("All pairs shortest paths:")
        for d in dist:
            print(d)

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)
    g.johnson()
