from collections import deque

n, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1
    unions = [(x, y)]  # 연합
    total = arr[x][y]  # 연합인 칸의 인구 수 합

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue

            if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                unions.append((nx, ny))
                total += arr[nx][ny]

    if len(unions) <= 1:  # 인구 이동이 일어나지 않은 경우
        return 0, visited

    total //= len(unions)  # 인구 이동 후 연합 각 칸의 인구수
    for x, y in unions:
        arr[x][y] = total
    return 1, visited

answer = 0
while True:
    check = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                c, visited = bfs(i, j, visited)
                check += c

    if check == 0:  # 인구 이동이 일어나지 않은 경우
        break

    answer += 1

print(answer)