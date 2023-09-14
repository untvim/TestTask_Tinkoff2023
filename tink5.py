def can_preserve_states(graph, x, n):
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        for neighbor, weight in graph[node]:
            if weight <= x and not visited[neighbor]:
                dfs(neighbor)

    num_states = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            num_states += 1

    return num_states == 1  # Штатов должно остаться ровно 1

def find_min_x(n, m, roads):
    graph = [[] for _ in range(n + 1)]
    max_road_length = 0

    for v, u, w in roads:
        graph[v].append((u, w))
        graph[u].append((v, w))
        max_road_length = max(max_road_length, w)

    left, right = 0, max_road_length
    result = max_road_length

    while left <= right:
        mid = (left + right) // 2
        if can_preserve_states(graph, mid, n):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

n, m = map(int, input().split())
roads = []
for _ in range(m):
    v, u, w = map(int, input().split())
    roads.append((v, u, w))

x = find_min_x(n, m, roads)
print(x)