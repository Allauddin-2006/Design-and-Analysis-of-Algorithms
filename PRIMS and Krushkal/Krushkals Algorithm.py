def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(V))
    cost = 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    print("MST Edges:")

    for u, v, w in edges:
        a = find(u)
        b = find(v)

        if a != b:
            parent[a] = b
            cost += w
            print(u, "--", v, "Weight:", w)

    print("MST Cost =", cost)


V = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(V, edges)
