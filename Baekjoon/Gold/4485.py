from collections import deque
import sys
# input = sys.stdin.readline

t = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

while True:
    t += 1
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]

    # BFS
    queue = deque([(0, 0)])  # 시작점
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = graph[0][0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            tmp = visited[x][y] + graph[nx][ny]
            if visited[nx][ny] == -1 or tmp < visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = tmp

    print(f"Problem {t}: {visited[n - 1][n - 1]}")