n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (use 99999 for no edge, 0 on diagonal):")
dist = [list(map(int, input().split())) for _ in range(n)]
inf = 99999

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] != inf and dist[k][j] != inf:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print("All-pairs shortest distance matrix:")
for row in dist:
    print(" ".join("INF" if value == inf else str(value) for value in row))
print("Time Complexity: O(V^3)")
print("Auxiliary Space: O(V^2)")