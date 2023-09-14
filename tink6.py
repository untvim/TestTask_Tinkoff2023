class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]

n, m = map(int, input().split())
dsu = DSU(n)
results = []

for _ in range(m):
    query = input().split()
    if query[0] == '1':
        x, y = int(query[1]) - 1, int(query[2]) - 1
        dsu.union(x, y)
    elif query[0] == '2':
        x, y = int(query[1]) - 1, int(query[2]) - 1
        if dsu.find(x) == dsu.find(y):
            results.append("YES")
        else:
            results.append("NO")
    elif query[0] == '3':
        x = int(query[1]) - 1
        results.append(str(dsu.size[dsu.find(x)]))

print('\n'.join(results))