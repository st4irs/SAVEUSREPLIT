from collections import deque

def bfs(graph, start):
    visited = [False] * graph.n
    q = deque([start])
    order = []

    visited[start] = True

    while q:
        u = q.popleft()
        order.append(u)

        for v in graph.adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return order
