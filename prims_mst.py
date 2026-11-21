def prim(graph):
    n = len(graph)
    key = [float("inf")] * n
    parent = [-1] * n
    used = [False] * n
    key[0] = 0

    for _ in range(n):
        u = min((v for v in range(n) if not used[v]), key=lambda v: key[v], default=-1)
        if u == -1 or key[u] == float("inf"):
            print("Graph is disconnected; MST does not exist.")
            return
        used[u] = True
        for v in range(n):
            if graph[u][v] > 0 and not used[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    total = 0
    print("MST edges:")
    for v in range(1, n):
        print(f"{parent[v]} - {v} : {graph[parent[v]][v]}")
        total += graph[parent[v]][v]
    print("Total MST weight:", total)
    print("Time Complexity: O(V^2)")


n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (0 means no edge):")
graph = [list(map(int, input().split())) for _ in range(n)]
prim(graph)