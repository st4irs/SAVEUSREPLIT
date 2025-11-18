from collections import deque

def bfs(residual, s, t, parent):
    n = len(residual)
    visited = [False] * n
    queue = deque([s])
    visited[s] = True

    while queue:
        u = queue.popleft()

        for v in range(n):
            if not visited[v] and residual[u][v] > 0:
                parent[v] = u
                visited[v] = True
                if v == t:
                    return True
                queue.append(v)

    return False

def edmonds_karp(capacity, s, t):
    n = len(capacity)
    residual = [row[:] for row in capacity]
    parent = [-1] * n
    max_flow = 0

    while bfs(residual, s, t, parent):
        path_flow = float("inf")
        v = t

        # find path flow
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        max_flow += path_flow

        # update residual
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

    return max_flow
