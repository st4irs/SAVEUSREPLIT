import math

def floyd(graph):
    n = len(graph)
    dist = [[math.inf] * n for _ in range(n)]

    # Initialize distances
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
        dist[i][i] = 0

    # Floyd–Warshall dynamic programming
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
