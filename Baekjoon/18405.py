from collections import deque

n, k = map(int, input().split())
graph, virus = [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] != 0:
            virus.append((graph[i][j], i, j, 0))

s, a, b = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

virus.sort()  # 낮은 번호의 바이러스가 먼저 증식
queue = deque(virus)

while queue:
    v, x, y, time = queue.popleft()
    if time == s:
        break
    if graph[x][y] == 0:
        continue

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = v
            queue.append((v, nx, ny, time + 1))


print(graph[a - 1][b - 1])
