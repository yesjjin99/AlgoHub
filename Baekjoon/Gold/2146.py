import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))  # 0은 바다, 1은 육지

answer = int(1e9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# DFS로 같은 섬의 경우 같은 번호로 표시 #
# 각 좌표에서 상하좌우 탐색
# if 범위 벗어나거나 육지인 경우 -> continue
# BFS를 통해 -> 같은 섬이 아닌 육지 만나는 최소 이동거리 구하기
# 섬의 모든 좌표에서 탐색하여 최소값 갱신

def dfs(x, y, c):
    graph[x][y] = c
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny, c)


def bfs(c):  # 같은 섬이 아닌 육지 만나는 최소 이동거리 구하기
    global answer

    queue = deque()
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == c:
                visited[i][j] = True
                queue.append((i, j, 0))

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue

            if graph[nx][ny] != 0 and graph[nx][ny] != c:
                answer = min(answer, dist)
                return

            queue.append((nx, ny, dist + 1))
            visited[nx][ny] = True


c = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j, c)  # 동일한 섬의 육지끼리 동일한 번호로 표시
            c += 1

for v in range(1, c):
    bfs(v)

print(answer)