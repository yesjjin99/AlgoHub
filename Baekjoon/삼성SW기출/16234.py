from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1
    union = [(x, y)]
    total = graph[x][y]

    while queue:  # 연합 생성
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    union.append((nx, ny))
                    total += graph[nx][ny]

    if len(union) <= 1:
        return 0
    total //= len(union)
    for x, y in union:  # 인구수 갱신
        graph[x][y] = total

    return 1

result = 0
while True:
    check = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                check += bfs(i, j, visited)

    if check == 0:  # 더 이상 인구 이동이 발생하지 않는다면 종료
        break
    result += 1

print(result)
