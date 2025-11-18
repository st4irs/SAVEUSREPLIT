import math

def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    dist = [math.inf] * n
    parent = [-1] * n

    dist[0] = 0

    for _ in range(n):
        # pick smallest unvisited node
        u = -1
        for i in range(n):
            if not selected[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        selected[u] = True

        # relax edges
        for v in range(n):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < dist[v]:
                dist[v] = graph[u][v]
                parent[v] = u

    mst = []
    for i in range(1, n):
        mst.append((parent[i], i, graph[parent[i]][i]))

    return mst
