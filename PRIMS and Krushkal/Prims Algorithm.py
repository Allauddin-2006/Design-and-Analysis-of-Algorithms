
import heapq

def prim(V, graph):
    visited = [False] * V
    pq = [(0, 0, -1)]
    cost = 0

    while pq:
        w, u, parent = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        cost += w

        if parent != -1:
            print(parent, "--", u, "Weight:", w)

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v, u))

    print("MST Cost =", cost)


V = 4
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

prim(V, graph)
