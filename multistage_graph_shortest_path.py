INF = float("inf")

n, stages = map(int, input("Enter number of vertices and stages: ").split())
print("Enter adjacency matrix (0 means no edge):")
graph = [list(map(int, input().split())) for _ in range(n)]
stage = list(map(int, input("Enter stage number for each vertex: ").split()))

cost = [INF] * n
next_vertex = [-1] * n
cost[-1] = 0

for u in range(n - 2, -1, -1):
    for v in range(n):
        if graph[u][v] > 0 and stage[v] > stage[u] and cost[v] != INF:
            candidate = graph[u][v] + cost[v]
            if candidate < cost[u]:
                cost[u] = candidate
                next_vertex[u] = v

if cost[0] == INF:
    print("No path from source to destination.")
else:
    path = []
    current = 0
    while current != -1:
        path.append(current)
        if current == n - 1:
            break
        current = next_vertex[current]
    print("Minimum cost:", cost[0])
    print("Path:", " -> ".join(map(str, path)))
    print("Time Complexity: O(V^2) for adjacency matrix")