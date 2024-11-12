from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = 0
    while queue:
        v = queue.popleft()
        for i in roads[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1


n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)

bfs(x)
check = False
for i in range(1, n + 1):
    if visited[i] == k:
        check = True
        print(i)

if not check:
    print(-1)
