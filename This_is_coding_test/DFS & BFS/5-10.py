from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    ice[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                queue.append((nx, ny))
                ice[nx][ny] = 1


n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input())))

count = 0
for i in range(n):
    for j in range(m):
        if ice[i][j] == 0:
            bfs(i, j)
            count += 1

print(count)
