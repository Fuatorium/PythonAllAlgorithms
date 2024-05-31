import sys

def min_distance(dist, spt_set, V):
    min = sys.maxsize
    min_index = -1
    for v in range(V):
        if dist[v] < min and spt_set[v] == False:
            min = dist[v]
            min_index = v
    return min_index

def dijkstra(graph, src, V):
    dist = [sys.maxsize] * V
    dist[src] = 0
    spt_set = [False] * V

    for cout in range(V):
        u = min_distance(dist, spt_set, V)
        spt_set[u] = True
        for v in range(V):
            if (graph[u][v] > 0 and spt_set[v] == False and
                    dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]
    print("Vertex \tDistance from Source")
    for node in range(V):
        print(node, "\t", dist[node])

if __name__ == "__main__":
    graph = [[0, 1, 4, 0, 0, 0],
             [1, 0, 4, 2, 7, 0],
             [4, 4, 0, 3, 5, 0],
             [0, 2, 3, 0, 4, 6],
             [0, 7, 5, 4, 0, 7],
             [0, 0, 0, 6, 7, 0]]
    dijkstra(graph, 0, len(graph))
