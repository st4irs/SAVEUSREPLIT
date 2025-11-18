def dfs(graph, start):
    visited = [False] * graph.n
    order = []

    def rec(u):
        visited[u] = True
        order.append(u)
        for v in graph.adj[u]:
            if not visited[v]:
                rec(v)

    rec(start)
    return order
