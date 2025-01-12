import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()  # 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하도록 정렬


def dfs(v, visited):
    visited[v] = 1
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

def bfs(v, visited):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


visited = [0] * (n + 1)
dfs(v, visited)
print()

visited = [0] * (n + 1)
bfs(v, visited)