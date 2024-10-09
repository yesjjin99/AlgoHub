from collections import deque


dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i],
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    return maze[n - 1][m - 1]


n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

print(bfs(0, 0))
