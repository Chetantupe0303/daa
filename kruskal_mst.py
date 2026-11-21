class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        elif self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[b] = a
            self.rank[a] += 1
        return True


n, m = map(int, input("Enter number of vertices and edges: ").split())
edges = []
print("Enter each edge as: source destination weight (0-based vertices)")
for _ in range(m):
    u, v, weight = map(int, input().split())
    edges.append((weight, u, v))

dsu = DSU(n)
total = count = 0
print("MST edges:")
for weight, u, v in sorted(edges):
    if dsu.union(u, v):
        print(f"{u} - {v} : {weight}")
        total += weight
        count += 1
        if count == n - 1:
            break

if count != n - 1:
    print("Graph is disconnected; MST does not exist.")
else:
    print("Total MST weight:", total)
print("Time Complexity: O(E log E)")