from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(x, y, visited):
    total = land[x][y]
    country = [(x, y)]
    visited[x][y] = 1
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(land[nx][ny] - land[x][y]) <= r:  # 절대값!
                    queue.append((nx, ny))
                    country.append((nx, ny))
                    total += land[nx][ny]
                    visited[nx][ny] = 1

    if len(country) <= 1:
        return 0
    now = total // len(country)
    for a, b in country:
        land[a][b] = now
    return 1


land = []
n, l, r = map(int, input().split())
for _ in range(n):
    land.append(list(map(int, input().split())))

answer = 0
while True:
    temp = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                temp += bfs(i, j, visited)
    if temp == 0:
        break
    answer += 1

print(answer)
