import math

def dijkstra(graph, start):
    n = len(graph)
    dist = [math.inf] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        # Select unvisited node with smallest distance
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        visited[u] = True

        # Relax edges
        for v in range(n):
            if graph[u][v] != 0:  # conexión válida
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist
